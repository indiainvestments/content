#!/usr/bin/env python3
"""Assert the Previous/Next footer links point the right way.

Hugo's .Next/.Prev walk toward the START of the page collection, so the
page-nav partial deliberately swaps them. That swap looks like a bug and is
easy to "correct", which silently reverses every series on the site. This
checks the rendered HTML rather than trusting the template: the sidebar is
rendered in reading order on every page, so Previous must point to a page that
appears earlier in it, and Next to one that appears later.
"""
import glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sitepaths import PUBLIC, site_base, to_site_path

NAV = re.compile(r'<nav[^>]*class=["\']?page-nav["\']?.*?</nav>', re.S)
LINK = re.compile(
    r'<a[^>]*href=["\']?([^"\'>\s]+)["\']?[^>]*>\s*<span>(Previous|Next)</span>', re.S)
ANY_A = re.compile(r'<a[^>]*href=["\']?([^"\'>\s]+)')


def main():
    origin, prefix = site_base()
    failures, checked, pages = [], 0, 0

    for f in glob.glob(PUBLIC + "/**/index.html", recursive=True):
        html = open(f, encoding="utf-8", errors="replace").read()
        nav = NAV.search(html)
        if not nav:
            continue

        # every link on the page, in document order == sidebar reading order
        seq, seen = [], set()
        for m in ANY_A.finditer(html):
            p = to_site_path(m.group(1), origin, prefix)
            if p and p not in seen:
                seen.add(p)
                seq.append(p)

        me_path = "/" + os.path.relpath(f, PUBLIC).replace(os.sep, "/")
        me_path = me_path[: -len("index.html")]
        if me_path not in seq:
            continue
        me = seq.index(me_path)
        pages += 1

        for m in LINK.finditer(nav.group(0)):
            target = to_site_path(m.group(1), origin, prefix)
            kind = m.group(2)
            if target is None or target not in seq:
                continue
            them = seq.index(target)
            checked += 1
            if kind == "Previous" and them > me:
                failures.append(f"{me_path}: 'Previous' -> {target} (comes later)")
            if kind == "Next" and them < me:
                failures.append(f"{me_path}: 'Next' -> {target} (comes earlier)")

    print(f"page-nav: {checked} links on {pages} pages checked, {len(failures)} wrong")
    if checked == 0:
        print("ERROR: no Previous/Next links were checked at all — this check is "
              "not actually testing anything.", file=sys.stderr)
        return 1
    for x in failures[:25]:
        print("  " + x, file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
