#!/usr/bin/env python3
"""Fail the build on broken internal links or missing images in public/."""
import os, re, sys, glob, urllib.parse
from collections import Counter

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUBLIC = os.path.join(ROOT, "public")
SKIP_PREFIXES = ("/icons/",)


def exists(p):
    p = urllib.parse.unquote(p.split("#")[0].split("?")[0])
    f = os.path.join(PUBLIC, p.lstrip("/"))
    return os.path.exists(f) or os.path.exists(os.path.join(f, "index.html"))


def local(u, base):
    if base and u.startswith(base):
        return u[len(base):] or "/"
    return u if (u.startswith("/") and not u.startswith("//")) else None


def main():
    base = ""
    idx = os.path.join(PUBLIC, "index.html")
    if os.path.exists(idx):
        m = re.search(r'<link[^>]+rel=["\']?canonical["\']?[^>]+href=["\']?([^"\'>\s]+)',
                      open(idx, encoding="utf-8", errors="replace").read())
        if m:
            base = m.group(1).rstrip("/")

    bad_l, bad_i, ok_l, ok_i = Counter(), Counter(), 0, 0
    for h in glob.glob(PUBLIC + "/**/*.html", recursive=True):
        t = open(h, encoding="utf-8", errors="replace").read()
        page = "/" + os.path.relpath(h, PUBLIC)
        for s in re.findall(r'<img[^>]+src=["\']?([^"\'>\s]+)', t):
            p = local(s, base)
            if p is None or p.startswith(SKIP_PREFIXES):
                continue
            if exists(p):
                ok_i += 1
            else:
                bad_i[f"{p}  (on {page})"] += 1
        for a in re.findall(r'<a[^>]+href=["\']?([^"\'>\s]+)', t):
            p = local(a, base)
            if p is None or p.startswith(SKIP_PREFIXES):
                continue
            if exists(p):
                ok_l += 1
            else:
                bad_l[f"{p}  (on {page})"] += 1

    print(f"images: {ok_i} ok, {len(bad_i)} broken")
    print(f"links : {ok_l} ok, {len(bad_l)} broken")
    for label, c in (("IMAGE", bad_i), ("LINK", bad_l)):
        for k in c:
            print(f"  broken {label}: {k}", file=sys.stderr)
    return 1 if (bad_i or bad_l) else 0


if __name__ == "__main__":
    sys.exit(main())
