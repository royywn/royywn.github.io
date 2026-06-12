# ARCHITECTURE.md

## Overview
Static portfolio + blog. Jupyter notebooks are the authoring format for technical
content; a build-time converter renders them to markdown. Astro renders markdown
content collections to plain HTML/CSS with near-zero client JS. GitHub Actions
builds on push; GitHub Pages serves.

```
.ipynb in notebooks/ ──► scripts/convert_notebooks.py ──► src/content/*.md
                                                              │
Browser ◄── GitHub Pages ◄── GitHub Actions (convert + astro build + pagefind + link check)
                                                              ▲
                                                    git push to main
```

Site URL: https://royywn.github.io  ·  repo: `royywn.github.io`  ·  base: `/`
(Existing MkDocs book remains a project page at /algotrading-strategy until migrated.)

No backend. Dynamic-feeling features map to static/third-party equivalents:

| Need            | Solution                              |
|-----------------|---------------------------------------|
| Blog comments   | giscus (GitHub Discussions)           |
| Search          | Pagefind (build-time static index)    |
| Contact         | mailto: + Formspree form (free tier)  |
| Analytics       | GoatCounter (single script tag)       |
| RSS             | @astrojs/rss                          |

## Repository layout
```
/
├── CLAUDE.md  ARCHITECTURE.md  PLAN.md  DECISIONS.md  BLOCKERS.md
├── astro.config.mjs          # site URL, integrations (tailwind, sitemap, rss)
├── tailwind.config.mjs
├── public/                   # favicon, CV PDF, og-image, robots.txt
├── notebooks/                # SOURCE OF TRUTH for technical content (committed)
│   ├── strategies/           # one .ipynb per strategy write-up
│   └── blog/                 # notebook-based posts (md posts also allowed directly)
├── scripts/
│   └── convert_notebooks.py  # nbconvert wrapper: ipynb → src/content/*.md + images
├── content-sources/          # RAW human-provided material (bio, project notes)
│   └── private/              # gitignored — never published
├── src/
│   ├── content/
│   │   ├── config.ts         # zod schemas for collections
│   │   ├── blog/             # one .md per post
│   │   └── strategies/       # one .md per strategy/technique write-up
│   ├── layouts/
│   │   ├── Base.astro        # html shell, nav, footer, meta/OG tags
│   │   ├── Post.astro        # blog post layout (toc, date, tags, giscus)
│   │   └── Strategy.astro    # strategy layout (status badge, results, repo link)
│   ├── components/           # Nav, Footer, Card, TagList, ThemeToggle...
│   ├── pages/
│   │   ├── index.astro       # landing
│   │   ├── about.astro
│   │   ├── projects.astro    # project index (cards)
│   │   ├── blog/[...] .astro # index + [slug] from collection
│   │   ├── strategies/[...]  # index + [slug] from collection
│   │   └── rss.xml.js
│   └── styles/global.css
└── .github/workflows/deploy.yml
```

## Sitemap & page specs

### `/` — Landing
- Hero: name, one-line positioning ("Data scientist in finance — ML, quant research,
  agentic AI tooling"), links: GitHub, LinkedIn, CV (PDF), email.
- "Selected work": 3 cards (QuantPulse, Agentic coding framework, Local AI infra)
  → each links to its project entry.
- "Recent writing": latest 3 blog posts.
- Single screen of content; no carousels, no stock imagery.

### `/about`
- Short professional narrative (sourced from content-sources/bio.md; do not invent).
- Skills grouped as on CV. Timeline of roles (compact). CV download button.

### `/projects`
- Card grid from a small typed array or tiny collection. Each card: name, one-liner,
  tech tags, repo link, optional link to a long-form write-up in /strategies or /blog.

### `/strategies` (collection)
- Index grouped by category (trend, mean reversion, optimization, risk, infra).
- Entry frontmatter schema:
  ```ts
  { title, description, category, tags[], status: 'idea'|'researching'|'backtested'|'paper-trading',
    date, updated?, repo?, draft? }
  ```
- REQUIRED sections per entry (enforced by template + review): Thesis · Data &
  methodology · Results (with costs/slippage assumptions) · Limitations · Code links.
- Existing MkDocs book chapters are migrated here selectively (PLAN Phase 4):
  migrate only chapters that have real code/results; rewrite tone (no emoji,
  no marketing claims); the rest are dropped, not ported.

### `/blog` (collection)
- Frontmatter: `{ title, description, date, tags[], draft? }`
- Post layout: reading time, TOC for >800 words, giscus at bottom, prev/next.
- Tag pages generated at `/blog/tags/[tag]`.

### Global
- Dark/light theme (CSS variables + small toggle script; respects prefers-color-scheme).
- OG/meta tags per page (title, description, og:image) — needed for LinkedIn shares.
- 404 page. Sitemap + robots.txt.

## Design language
Fully specified in `DESIGN.md` (palette tokens for light/dark, Source Serif 4 +
Inter + JetBrains Mono pairing, component specs, approved landing copy, voice
rules, do-not list). DESIGN.md is authoritative; this file only owns structure.
- Code blocks: Shiki (Astro default), themes matched to DESIGN.md palette.
- Charts in posts: pre-rendered images from notebooks, styled via the repo's
  `royplot.mplstyle` — no client-side charting library on content pages.

## Notebook publishing pipeline (Roy's daily workflow)
Authoring loop: save notebook → copy into `notebooks/strategies/` or `notebooks/blog/`
→ commit → push. Nothing else.

Mechanics:
1. **Frontmatter cell**: first cell of each notebook is a RAW cell containing the
   YAML frontmatter (title, description, category, status, tags, date, repo).
   The converter validates it against the collection schema and fails the build
   with a clear message if invalid — bad metadata never reaches production.
2. **Conversion**: `convert_notebooks.py` runs `nbconvert --to markdown` per notebook,
   writes output to `src/content/<collection>/<slug>.md` with a `<!-- GENERATED -->`
   header, and copies extracted images to a co-located asset folder rewritten to
   correct paths. Generated .md files are gitignored; notebooks are the only source.
3. **No execution**: notebooks are converted as-saved. CI has no data dependencies
   and results can never silently change. Re-run locally, save, push to update.
4. **Hygiene**: converter strips empty cells and `# HIDE`-tagged cells (for setup/
   credentials cells you don't want published), and warns on outputs > 1 MB
   (suggesting figure downsizing) to keep pages fast.
5. **Plain markdown still works**: dropping a hand-written .md straight into
   `src/content/blog/` (without the GENERATED header) is also supported for
   non-notebook posts.

## Build & deploy
- `deploy.yml`: on push to main → npm ci + pip install nbconvert → convert →
  astro check → astro build → pagefind --site dist → lychee link check on dist →
  upload-pages-artifact → deploy.
- astro.config: `site: 'https://royywn.github.io'`, `base: '/'` (user site — ADR-002).

## Performance & a11y budgets
- Content pages ship ≤ 50 KB JS (theme toggle + pagefind UI only on /search).
- Images: astro:assets with explicit width/height; lazy-load below the fold.
- All interactive elements keyboard-accessible; color contrast AA minimum.
