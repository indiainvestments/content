#!/usr/bin/env python3
"""Shared URL helpers for the CI checks.

The site is built with different baseURLs depending on where it is deployed:
  https://www.indiainvestments.wiki/            -> links look like /faqs/
  https://indiainvestments.github.io/content/   -> links look like /content/faqs/

Both must resolve against public/ the same way, so every check strips the
baseURL's path prefix before touching the filesystem. Getting this wrong makes
a check either fail on every link or, worse, silently check nothing.
"""
import os, re, urllib.parse

PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
PUBLIC = os.path.normpath(PUBLIC)


def site_base():
    """-> (origin, path_prefix) read from the homepage's canonical link."""
    idx = os.path.join(PUBLIC, "index.html")
    if not os.path.exists(idx):
        return "", ""
    m = re.search(r'<link[^>]*rel=["\']?canonical["\']?[^>]*href=["\']?([^"\'>\s]+)',
                  open(idx, encoding="utf-8", errors="replace").read())
    if not m:
        return "", ""
    u = urllib.parse.urlsplit(m.group(1))
    return f"{u.scheme}://{u.netloc}", u.path.rstrip("/")


def to_site_path(url, origin, prefix):
    """Absolute-or-relative URL -> site path with the baseURL prefix removed.

    Returns None for anything not local to this site.
    """
    if origin and url.startswith(origin):
        url = url[len(origin):] or "/"
    if not url.startswith("/") or url.startswith("//"):
        return None
    if prefix and (url == prefix or url.startswith(prefix + "/")):
        url = url[len(prefix):] or "/"
    return url


def exists(site_path):
    p = urllib.parse.unquote(site_path.split("#")[0].split("?")[0])
    f = os.path.join(PUBLIC, p.lstrip("/"))
    return os.path.exists(f) or os.path.exists(os.path.join(f, "index.html"))
