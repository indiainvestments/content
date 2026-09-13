#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
"""Fail the build on broken internal links or missing images in public/."""
import glob, os, re, sys
from collections import Counter
from sitepaths import PUBLIC, site_base, to_site_path, exists

SKIP = ("/icons/",)


def main():
    origin, prefix = site_base()
    bad_l, bad_i, ok_l, ok_i = Counter(), Counter(), 0, 0
    escapes = Counter()   # links that leave the site entirely on a subpath deploy

    for h in glob.glob(PUBLIC + "/**/*.html", recursive=True):
        t = open(h, encoding="utf-8", errors="replace").read()
        page = "/" + os.path.relpath(h, PUBLIC).replace(os.sep, "/")
        for attr, store, tag in (("src", bad_i, "img"), ("href", bad_l, "a")):
            for m in re.finditer(r'<%s[^>]+%s=["\']?([^"\'>\s]+)' % (tag, attr), t):
                raw = m.group(1)
                # On a project page (baseURL with a path), a site-absolute URL
                # that lacks that path escapes to the domain root. It still
                # "resolves" against public/, so it must be caught separately.
                if prefix and raw.startswith("/") and not raw.startswith("//") \
                        and not raw.startswith(prefix + "/") and raw != prefix:
                    escapes[f"{raw}  (on {page})"] += 1
                p = to_site_path(raw, origin, prefix)
                if p is None or p.startswith(SKIP):
                    continue
                if exists(p):
                    if tag == "img":
                        ok_i += 1
                    else:
                        ok_l += 1
                else:
                    store[f"{p}  (on {page})"] += 1

    print(f"images: {ok_i} ok, {len(bad_i)} broken")
    print(f"links : {ok_l} ok, {len(bad_l)} broken")
    if prefix:
        print(f"escapes: {len(escapes)} URLs missing the '{prefix}' base path")
    if not ok_l:
        print("ERROR: no internal links were checked at all — the baseURL prefix "
              "is probably not being stripped correctly.", file=sys.stderr)
        return 1
    for label, c in (("IMAGE", bad_i), ("LINK", bad_l)):
        for k in list(c)[:25]:
            print(f"  broken {label}: {k}", file=sys.stderr)
    for k in list(escapes)[:25]:
        print(f"  ESCAPES the base path: {k}", file=sys.stderr)
    return 1 if (bad_i or bad_l or escapes) else 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main())
