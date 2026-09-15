#!/usr/bin/env python3
"""Markdown dialect check.

Hugo parses these files as CommonMark + GFM (Goldmark). Anything else — GitBook
template tags, Obsidian syntax, kramdown attributes, a shortcode that doesn't
exist — either renders as literal junk or vanishes silently. Silently is worse:
the page still builds, the links still resolve, the other checks still pass, and
nobody notices until a reader does.

This check is the guard against that whole class of bug. Run it locally or let CI
run it; it exits 1 on any error.

    python3 scripts/check_markdown.py
    python3 scripts/check_markdown.py --warnings   # include non-fatal notes
"""
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

ROT_CLASSES = {"fast-rot", "slow-drift", "evergreen"}
ALERTS = {"NOTE", "TIP", "WARNING", "CAUTION", "IMPORTANT"}   # layouts/_markup/render-blockquote.html
BUILTIN_SHORTCODES = {
    "youtube", "vimeo", "figure", "highlight", "instagram", "param",
    "ref", "relref", "gist", "x", "twitter", "qr", "comment", "details",
}

HTML_ELEMENTS = {
    "a","abbr","b","blockquote","br","caption","cite","code","col","colgroup","dd","del",
    "details","div","dl","dt","em","figcaption","figure","h1","h2","h3","h4","h5","h6",
    "hr","i","iframe","img","ins","kbd","li","mark","ol","p","picture","pre","q","s",
    "samp","script","section","small","source","span","strong","sub","summary","sup",
    "table","tbody","td","tfoot","th","thead","tr","u","ul","var","video","audio","wbr",
}

def blank_code(text):
    """Replace fenced blocks and inline code spans with same-length blanks, so
    line and column numbers stay true but code contents are never matched."""
    def blanks(m):
        return "".join("\n" if c == "\n" else " " for c in m.group(0))
    text = re.sub(r"^(?P<f>```|~~~).*?^(?P=f)[^\n]*$", blanks, text, flags=re.S | re.M)
    text = re.sub(r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)", blanks, text, flags=re.S)
    text = re.sub(r"<!--.*?-->", blanks, text, flags=re.S)
    return text

RULES = [
    # (id, regex, message, fatal)
    ("gitbook-tag", r"\{%[^\n]*?%\}",
     "GitBook/Liquid template tag — not markdown, renders as literal text", True),
    ("wikilink", r"\[\[[^\]\n]+\]\]",
     "Obsidian wiki-link — Hugo renders this literally; use [text](/path/)", True),
    ("highlight", r"(?<!=)==[^\s=][^=\n]*==(?!=)",
     "Obsidian ==highlight== — not GFM; use **bold** or <mark>", True),
    ("kramdown-attr", r"\{:\s*[.#][^\}\n]*\}",
     "kramdown attribute block — Goldmark wants {#id} / {.class} without the colon", True),
    ("mdx", r"</?[A-Z][A-Za-z0-9]*[\s/>]",
     "JSX/MDX-style component tag — Hugo has no such thing", True),
]

def check_file(path, warn):
    raw = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    errs, warns = [], []

    def at(text, idx):
        return text.count("\n", 0, idx) + 1

    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        return [(rel, 1, "front-matter", "missing YAML front matter")], []
    fm, body_raw = m.groups()
    offset = raw[: m.start(2)].count("\n")
    body = blank_code(body_raw)

    def field(k):
        mm = re.search(rf"^{k}:\s*\"?([^\"\n]+?)\"?\s*$", fm, re.M)
        return mm.group(1).strip() if mm else None

    # --- front matter ---------------------------------------------------
    if not field("title"):
        errs.append((rel, 1, "front-matter", "no title"))
    rot = field("rotClass")
    if rot and rot not in ROT_CLASSES:
        errs.append((rel, 1, "front-matter", f"rotClass '{rot}' is not one of {sorted(ROT_CLASSES)}"))
    rev = field("lastReviewed")
    if rev and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", rev):
        errs.append((rel, 1, "front-matter", f"lastReviewed '{rev}' is not YYYY-MM-DD"))

    # --- dialect rules --------------------------------------------------
    for rid, pat, msg, fatal in RULES:
        for mm in re.finditer(pat, body):
            found = mm.group(0).strip().replace("\n", " ")[:50]
            (errs if fatal else warns).append(
                (rel, offset + at(body, mm.start()), rid, f"{msg} — {found!r}"))

    # --- shortcodes exist ----------------------------------------------
    known = BUILTIN_SHORTCODES | {
        p.stem for d in ("layouts/_shortcodes", "layouts/shortcodes")
        for p in (ROOT / d).glob("*.html")
    }
    for mm in re.finditer(r"\{\{[<%]\s*/?\s*([a-zA-Z0-9_/-]+)", body):
        name = mm.group(1).split("/")[-1]
        if name not in known:
            errs.append((rel, offset + at(body, mm.start()), "shortcode",
                         f"unknown shortcode {{{{< {name} >}}}} — no layouts/_shortcodes/{name}.html"))

    # --- math flag matches math content ---------------------------------
    # Only $$ counts. A lone $ is a rupee/dollar amount far more often than it is
    # inline math, and Hugo's passthrough is configured for $$ anyway.
    has_math = "$$" in body
    declared = (field("math") or "").lower() == "true"
    if has_math and not declared:
        line = offset + at(body, body.find("$$") if "$$" in body else 0)
        errs.append((rel, line, "math",
                     "math delimiters but no `math: true` — these render as literal $ signs"))
    if declared and not has_math:
        warns.append((rel, 1, "math", "`math: true` but no math on the page — KaTeX loads for nothing"))

    # --- GitHub alert types ---------------------------------------------
    for mm in re.finditer(r"^>\s*\[!([A-Za-z]+)\]", body, re.M):
        if mm.group(1).upper() not in ALERTS:
            errs.append((rel, offset + at(body, mm.start()), "alert",
                         f"[!{mm.group(1)}] is not handled by render-blockquote.html "
                         f"— use one of {sorted(ALERTS)}"))

    # --- pseudo-tags that Goldmark will swallow --------------------------
    for mm in re.finditer(r"<([a-zA-Z][a-zA-Z0-9]*)([^<>\n]*)>", body):
        tag, rest = mm.group(1).lower(), mm.group(2)
        if tag in HTML_ELEMENTS:
            continue
        if "://" in mm.group(0) or "@" in mm.group(0):
            continue                       # <https://...> and <a@b> autolinks are fine
        errs.append((rel, offset + at(body, mm.start()), "pseudo-tag",
                     f"{mm.group(0)!r} looks like an HTML tag and will be silently "
                     f"dropped — wrap it in backticks"))

    # --- exactly one H1, and it comes first -------------------------------
    h1s = [mm for mm in re.finditer(r"^#\s+\S", body, re.M)]
    heads = [mm for mm in re.finditer(r"^#{1,6}\s+\S", body, re.M)]
    if len(h1s) == 0 and body.strip():
        warns.append((rel, 1, "heading", "no H1 — the page renders without a visible title"))
    elif len(h1s) > 1:
        errs.append((rel, offset + at(body, h1s[1].start()), "heading",
                     f"{len(h1s)} H1 headings — there should be exactly one"))
    elif h1s and heads and h1s[0].start() != heads[0].start():
        warns.append((rel, offset + at(body, heads[0].start()), "heading",
                      "a lower-level heading appears before the H1"))

    return errs, warns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--warnings", action="store_true", help="also print non-fatal notes")
    a = ap.parse_args()

    files = sorted(CONTENT.rglob("*.md"))
    if not files:
        print("check_markdown: no content files found — refusing to pass vacuously")
        return 1

    errs, warns = [], []
    for f in files:
        e, w = check_file(f, a.warnings)
        errs += e; warns += w

    for rel, line, rid, msg in sorted(warns, key=lambda r: (str(r[0]), r[1])):
        if a.warnings:
            print(f"warning: {rel}:{line}: [{rid}] {msg}")
    for rel, line, rid, msg in sorted(errs, key=lambda r: (str(r[0]), r[1])):
        print(f"{rel}:{line}: [{rid}] {msg}")

    n = len(files)
    if errs:
        print(f"\ncheck_markdown: {len(errs)} problem(s) in {n} files")
        return 1
    extra = f", {len(warns)} warning(s)" if warns and not a.warnings else ""
    print(f"check_markdown: {n} files clean{extra}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
