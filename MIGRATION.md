# GitBook → Hugo migration

This folder is the converted wiki, ready to drop into `indiainvestments/content`.
It reproduces the live site's structure and every one of its URLs, on GitHub Pages,
built by GitHub Actions.

## What to do with it

**Unzip first, verify, then delete.** Not the other way round — if anything is wrong
with the new files you want the old ones still sitting there. Nothing in the zip
collides with the old tree (the only shared filename is `.gitignore`, and the one in
the zip already carries the old entries forward), and Hugo ignores the stale
directories, so the site builds and verifies correctly *before* you remove anything.

### 1. Unzip into the repo

The zip has a wrapper folder. You want the **contents** of `wiki-hugo/` at the repo
root, not the folder itself — `hugo.toml` must end up next to `.gitbook/`, not inside
another directory.

```bash
cd path/to/content
git checkout -b hugo-migration

unzip -o ~/Downloads/wiki-hugo.zip -d /tmp/wh
cp -r /tmp/wh/wiki-hugo/. .
```

PowerShell:

```powershell
cd C:\ramesh_data\working_data\II wiki\content
git checkout -b hugo-migration

Expand-Archive -Path $HOME\Downloads\wiki-hugo.zip -DestinationPath $env:TEMP\wh -Force
Copy-Item -Path "$env:TEMP\wh\wiki-hugo\*" -Destination . -Recurse -Force
```

Check it landed right: `hugo.toml`, `content/`, `layouts/`, `assets/`, `scripts/`
and `static/` should all be at the repo root, alongside the existing `.gitbook/`.

### 2. Verify before deleting anything

```bash
hugo --gc --minify
python3 scripts/check_urls.py     # must print 132/132
python3 scripts/check_links.py    # must print 0 broken
hugo server -D                    # look at http://localhost:1313
```

If you would rather not install Hugo locally, commit and push at this point and let
the PR checks do it — they run exactly these three commands.

### 3. Remove the old GitBook tree

Only once step 2 passes. Use `git rm -r` on its own — it clears the index *and* the
working tree in one step, and it refuses to touch anything git isn't tracking, which
is the safety net a bare `rm -rf` does not give you.

```bash
git rm -r -q SUMMARY.md content.json model.json package.json yarn.lock \
             disclaimers-and-disclosures.md \
             faqs how-to stocks excel bonds misc start-here contributors \
             discord-and-reddit
```

Keep `README.md` (it is the repo's GitHub landing page — the wiki homepage is now
`content/_index.md`), `LICENSE`, `.all-contributorsrc`, and all of `.gitbook/`.

### 4. Deal with the old Discord workflow

`.github/workflows/discord.yml` survives the unzip and is now broken: it globs
`faqs/*.md`, which no longer exists, and posts links built from a `GITBOOK_DOMAIN`
secret. It only fires when you publish a release, so it is dormant rather than
dangerous — but fix it or delete it now rather than being confused by it later.

To keep it, change `faq_glob` to `content/faqs/**/*.md` and point the URL secret at
the new domain. To drop it: `git rm .github/workflows/discord.yml`.

### 5. Commit and push

```bash
git add -A
git commit -m "Migrate wiki from GitBook to Hugo"
git push -u origin hugo-migration
```

Open a PR, let the checks run, merge.

## Turning on GitHub Pages

Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
The first push to `main` after that deploys the site. Nothing else to configure —
`.github/workflows/deploy.yml` handles the rest.

The site will be live at `https://indiainvestments.github.io/content/` immediately.

## Pointing indiainvestments.wiki at it (do this last)

Only after the GitHub Pages build is confirmed good.

1. `static/CNAME` already contains `www.indiainvestments.wiki`.
2. Whoever holds the Cloudflare account sets:
   - `CNAME  www  →  indiainvestments.github.io` (**DNS only — grey cloud, not proxied**)
   - apex `indiainvestments.wiki` → redirect rule to `https://www.indiainvestments.wiki/`,
     or four `A` records pointing at GitHub Pages' IPs
3. Repo **Settings → Pages → Custom domain** → `www.indiainvestments.wiki`, then
   tick **Enforce HTTPS** once the certificate is issued (can take up to an hour).

Cloudflare's orange-cloud proxy in front of GitHub Pages breaks GitHub's certificate
issuance. Leave it grey until HTTPS is enforced; you can turn the proxy on afterwards
if you want Cloudflare's caching, with SSL mode set to Full (strict).

## What changed, and what did not

**Unchanged:** every page, every URL, the sidebar order, the section grouping, all
506 images, the CC BY-NC-SA licence, the contributor credits.

**No theme, no toolchain.** Every template is in `layouts/`, the stylesheet is one
plain-CSS file, and the search is vanilla JS. No submodule, no npm, no Sass, no
`extended` Hugo build — nothing that can break from upstream. GitHub Actions builds
it on push; you never run Hugo unless you want a local preview.

**Fixed during conversion:**

| | |
|---|---|
| 12 orphaned duplicate pages | deleted (stale forks of renamed pages, never served) |
| `BEGINNER'S GUIDE TO INVESTING` | 3 dead nav entries removed; the 3 URLs now redirect to `/start-here/zero-to-investing/` |
| 11 malformed image URLs in `faqs/stocks/` | repaired where the file survived; 8 lost screenshots unlinked |
| 25 legacy `indiainvestments.gitbook.io` links | rewritten to live paths |
| 19 broken FAQ links in the Discord-bot page | remapped to current locations |
| 1 malformed kfintech link | fixed |
| 60 `{% hint %}` blocks | converted to GitHub alert syntax (`> [!NOTE]`) |
| 49 `{% embed %}` | YouTube shortcodes / plain links |
| 52 `{% page-ref %}` / `{% content-ref %}` | ordinary Markdown links |
| 51 duplicate dark-mode images | dropped (the theme handles dark mode itself) |

**Added:**

- A freshness banner on every page, seeded from each file's real last-commit date.
  All 129 currently read as stale — because they are. That is the point.
- `rotClass` on every page (fast-rot / slow-drift / evergreen) driving the cadence.
- `scripts/check_urls.py` — fails CI if any URL the old site served stops resolving.
  This is what protects a decade of Reddit backlinks from a careless rename.
- `scripts/check_links.py` — fails CI on any broken internal link or missing image.
- Full-text client-side search — a generated `index.json` plus ~90 lines of vanilla
  JS. No external service, no tracking. `/` focuses it.
- A gruvbox palette with a light/dark toggle, defined as CSS custom properties in
  one place. Recolour the whole site by editing those tokens.
- `CONTRIBUTING-hugo.md` — how to edit, front matter reference, the April sweep.

## Verification at time of conversion

```
legacy URL parity: 132/132
images: 156 ok, 0 broken
links : 18400 ok, 0 broken
117 pages in the search index
```
