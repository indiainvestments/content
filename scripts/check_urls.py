#!/usr/bin/env python3
"""Assert every URL the GitBook site served still resolves in public/.

These paths are linked from years of r/IndiaInvestments comments. Breaking one
silently loses real traffic, so this runs on every PR and every deploy.
Add an `aliases:` entry in a page's front matter when a page legitimately moves.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUBLIC = os.path.join(ROOT, "public")
URLS = os.path.join(os.path.dirname(__file__), "legacy-urls.txt")


def resolves(url):
    p = url.strip("/")
    if not p:
        return os.path.exists(os.path.join(PUBLIC, "index.html"))
    return (os.path.exists(os.path.join(PUBLIC, p, "index.html"))
            or os.path.exists(os.path.join(PUBLIC, p + ".html")))


def main():
    urls = [l.strip() for l in open(URLS) if l.strip() and not l.startswith("#")]
    missing = [u for u in urls if not resolves(u)]
    print(f"legacy URL parity: {len(urls) - len(missing)}/{len(urls)}")
    if missing:
        print("\nThese URLs no longer resolve:", file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)
        print("\nAdd the path to the target page's `aliases:` front matter, "
              "or restore the page.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
