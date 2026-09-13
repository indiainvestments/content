# Working on the wiki

The wiki is a [Hugo](https://gohugo.io) site. Pages are plain Markdown in
`content/`. Every push to `main` rebuilds and deploys automatically — there is no
separate publishing step and no GitBook.

## Edit one page (no setup needed)

Open the page on the site, click **Update this page →** in the freshness banner at
the top. That drops you into the GitHub editor for the right file. Commit to a
branch, open a pull request, done.

## Run it locally

Only if you want to. Editing on GitHub works fine without it.

```bash
git clone https://github.com/indiainvestments/content.git
cd content
hugo server -D          # http://localhost:1313
```

Any Hugo v0.158 or newer. No `extended` build needed, no submodules, no npm, no
Sass — the stylesheet is plain CSS and the layouts are in this repo.

## Layout

```
content/          the pages — mirrors the site's URLs exactly
.gitbook/assets/  images, served at /images/<filename>
layouts/          the templates — all of them, no theme
assets/css/main.css   the stylesheet (plain CSS, all colour tokens at the top)
assets/js/site.js     theme toggle, sidebar folding, search
scripts/          CI checks
.github/workflows/  build, check, deploy
```

## Front matter

```yaml
---
title: "Why should I invest in Direct Plans instead of Regular Plans?"
description: "One line, used for search results and link previews."
weight: 12              # position in the sidebar within its section
rotClass: fast-rot      # fast-rot | slow-drift | evergreen
lastReviewed: 2026-04-12
lastUpdated: 2026-04-12
---
```

`rotClass` sets how long a page stays "fresh" before the banner turns into a
staleness warning:

| rotClass | Review cadence | Use for |
|---|---|---|
| `fast-rot` | 12 months | tax rates, limits, regulations, platform and broker specifics, "best X" |
| `slow-drift` | 24 months | product categories, fund types, insurance structures |
| `evergreen` | 36 months | principles, maths, mental models |

**`lastReviewed` means a human confirmed the page is still true.** Bump it only
when you have actually checked the facts — not when you fix a typo. That date is
what readers see, so an inflated one is worse than an old one.

## Writing rules

- One `# H1` at the top of every page — it is the page title on screen.
- Callouts use GitHub alert syntax:
  ```
  > [!NOTE]
  > Useful context.
  ```
  Available: `NOTE`, `TIP`, `WARNING`, `CAUTION`.
- Images: `![alt text](/images/filename.png)`. Put the file in `.gitbook/assets/`.
- Internal links are site-absolute with a trailing slash:
  `[direct plans](/faqs/mfs/direct-vs-regular/)`.
- YouTube: `{{< youtube VIDEO_ID >}}`.

## Renaming or moving a page

**Old URLs must keep working.** Years of r/IndiaInvestments comments link into this
wiki; a dead link is lost traffic and a lost reader. When you move a page, add its
previous path to the new page's front matter:

```yaml
aliases:
  - "/faqs/old-location-of-this-page"
```

`scripts/check_urls.py` runs on every pull request and fails the build if any URL
that the old GitBook site served stops resolving. `scripts/check_links.py` fails on
any broken internal link or missing image. Both must pass before a PR can merge.

## The annual sweep

India's Union Budget lands 1 February; the Finance Act is enacted in late March and
takes effect 1 April. **April is the real review month.** Work through every
`rotClass: fast-rot` page, verify the figures against primary sources, fix what
changed, and bump `lastReviewed`. A lighter February pass can flag announced but
not-yet-enacted changes.


## Look and feel

There is no theme. `layouts/` holds every template and `assets/css/main.css` is a
single plain-CSS file — no Sass, no build step, nothing to install.

The palette is defined once as custom properties at the top of `main.css`: a
`:root` block for light, then the same tokens redefined under
`:root[data-theme="dark"]` and under `@media (prefers-color-scheme: dark)`. To
recolour the site, change those tokens and nothing else — every component reads
from them.

Light is a warm newspaper stock in the Financial Times tradition — warm paper,
deep blue, claret — at its own values rather than another masthead's. Dark takes
its ground from Neil Panchal's Hypersubatomic (`#0f111a`) with the body ink
brightened from that theme's shipped `#8f93a2` (6.15:1 — fine for code, too dim
for prose) to `#d8dce8` (13.74:1).

The two halves are deliberately different temperatures. They hold together
because the hues carry across: links stay blue and the accent stays in the
red-pink family in both. If you change one half, change the other to match in
hue, not in temperature. The toggle in the top bar writes the choice to `localStorage`, and a
tiny inline script in `layouts/_partials/head.html` applies it before first paint
so there is no flash of the wrong palette.

Search is `layouts/index.json` (a generated index of every page) plus about 90
lines in `site.js`. Client-side, no external service, no tracking. Press `/` to
focus it.
