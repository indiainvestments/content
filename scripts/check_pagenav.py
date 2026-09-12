#!/usr/bin/env python3
"""Assert the Previous/Next footer links point the right way.

Hugo's .Next/.Prev walk toward the start of the page collection, so the
template swaps them. That swap is easy to "correct" by mistake, which silently
reverses every series on the site. This checks the rendered HTML instead of
trusting the template: for every page, the Previous link must go to a page that
appears earlier in the sidebar, and Next to one that appears later.
"""
import glob, os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUBLIC = os.path.join(ROOT, "public")

NAV = re.compile(r'<nav class="?page-nav"?.*?</nav>', re.S)
LINK = re.compile(
    r'<a href="?([^"\s>]+)"?>\s*<span>(Previous|Next)</span>([^<]*)</a>', re.S)


def main():
    # The sidebar is rendered in reading order on every page, so it is the
    # ground truth to compare the footer links against.
    failures, checked = [], 0
    for f in glob.glob(PUBLIC + "/**/index.html", recursive=True):
        html = open(f, encoding="utf-8", errors="replace").read()
        nav = NAV.search(html)
        if not nav:
            continue
        # sidebar order on this very page = reading order
        side = re.findall(r'<a href="?(/[^"\s>]*)"?[^>]*>', html)
        seen, seq = set(), []
        for u in side:
            if u not in seen:
                seen.add(u)
                seq.append(u)
        page_url = "/" + os.path.relpath(f, PUBLIC).replace(os.sep, "/")
        page_url = page_url[: -len("index.html")]
        if page_url not in seq:
            continue
        me = seq.index(page_url)
        for m in LINK.finditer(nav.group(0)):
            href, kind, title = m.group(1), m.group(2), m.group(3)
            if href not in seq:
                continue
            them = seq.index(href)
            checked += 1
            if kind == "Previous" and them > me:
                failures.append(f"{page_url}: 'Previous' -> {href} (which comes later)")
            if kind == "Next" and them < me:
                failures.append(f"{page_url}: 'Next' -> {href} (which comes earlier)")

    print(f"page-nav: {checked} links checked, {len(failures)} wrong")
    for x in failures[:25]:
        print("  " + x, file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
