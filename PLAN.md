# PLAN.md

Work phases in order. An item is DONE only when its verification command/condition
passes. Tick boxes with a one-line note + commit hash.

## Phase 0 — Inputs (human; agent verifies presence only)
- [ ] `content-sources/bio.md` exists (career narrative, ≥300 words, written by Roy)
- [ ] `content-sources/projects.md` exists (notes per project: what/why/stack/links)
- [ ] `public/Roy_Yang_CV.pdf` exists
- [x] GitHub username / repo / custom-domain decision recorded in DECISIONS.md
      (ADR-002 — DONE: username renamed to `royywn`; hub repo `royywn.github.io`)
- VERIFY: files exist; if missing → BLOCKERS.md, proceed to Phase 1 anyway.

## Phase 1 — Scaffold
- [x] `npm create astro@latest` minimal template; add tailwind, sitemap, rss integrations
      (da69b4b — hand-written minimal template pinned to astro@^4 since create-astro@latest
      now scaffolds Astro 5, off the fixed stack; sitemap pinned 3.2.1 for Astro 4 compat)
- [ ] Content collections defined in `src/content/config.ts` with zod schemas per ARCHITECTURE.md
- [ ] DESIGN.md implemented: CSS variables (light + dark incl. honey accent flip),
      @fontsource fonts (Source Serif 4, Inter, JetBrains Mono), base components
      (buttons, cards, badges) match the component specs
- [ ] Base.astro layout: nav (Home/About/Projects/Strategies/Blog), footer band
      per DESIGN.md, meta/OG tags, theme toggle
- [ ] One placeholder entry in each collection validates against schema
- [ ] `scripts/convert_notebooks.py` + npm `convert`/`predev`/`prebuild` hooks;
      generated output gitignored; frontmatter raw-cell validation with clear errors
- [ ] Sample notebook in `notebooks/strategies/` (frontmatter cell + 1 plot output)
      converts and renders end-to-end
- VERIFY: `npm run build && npx astro check` exit 0; dev server renders all nav
  routes INCLUDING the page generated from the sample notebook; image from the
  notebook displays correctly.

## Phase 2 — Core pages
- [ ] Landing page per DESIGN.md zone spec — use the approved hero copy verbatim
      (eyebrow, "Hi, I'm Roy.", two paragraphs, four action buttons)
- [ ] About page rendering content-sources/bio.md content (TODO markers if absent)
- [ ] Projects page with typed project data (QuantPulse, Agentic framework, Local AI infra)
- [ ] 404 page, robots.txt, favicon, og-image placeholder
- VERIFY: build passes; lychee on dist reports 0 broken internal links.

## Phase 3 — Content systems
- [ ] Blog index + [slug] pages + tag pages + RSS at /rss.xml
- [ ] Strategy index (grouped by category) + [slug] pages with status badge
- [ ] Post layout: reading time, conditional TOC, prev/next, giscus mount point
      (giscus repo config → BLOCKERS if not yet provided)
- [ ] Pagefind integrated; /search page works on built output
- VERIFY: build passes; rss.xml validates; pagefind index returns results for a
  known term in `npm run preview`.

## Phase 4 — Content migration & seed content
- [ ] Audit existing MkDocs book: list chapters WITH real code/results vs boilerplate
      → write audit table into DECISIONS.md (ADR-005)
- [ ] Migrate 3–5 strongest chapters: where a real notebook exists, place the .ipynb
      (with frontmatter cell) in notebooks/strategies/; otherwise rewrite as .md
      (tone per CLAUDE.md rules; add Limitations sections; no emoji; no invented results)
- [ ] `royplot.mplstyle` in repo root per DESIGN.md imagery spec (warm white figure
      bg, palette-matched categorical cycle); referenced in KICKOFF notebook notes
- [ ] Seed 2 blog posts from existing material Roy provides (e.g. look-ahead-bias
      hunt write-up; agentic coding setup wizard) — drafts with TODO:ROY markers
      where facts are needed
- VERIFY: every migrated page passes schema; zero TODO:ROY markers remain in
  files NOT marked `draft: true`.

## Phase 5 — Deploy
- [ ] `.github/workflows/deploy.yml` per ARCHITECTURE (check → build → pagefind →
      lychee → deploy to Pages)
- [ ] astro.config `site`/`base` set per ADR-002 decision
- [ ] Production smoke test: fetch deployed homepage, /blog, /strategies, one post —
      all HTTP 200; OG tags present in HTML
- VERIFY: green Actions run on main; deployed URLs return 200.

## Phase 6 — Polish (only after 0–5 complete)
- [ ] Lighthouse CI: Performance ≥95, A11y ≥95 on /, one post, one strategy page
- [ ] GoatCounter snippet (account id → BLOCKERS if absent)
- [ ] Formspree contact form on /about (form id → BLOCKERS if absent)
- [ ] Redirect or banner on old MkDocs site pointing to new site (if old site retained)
- VERIFY: lighthouse scores recorded in DECISIONS.md (ADR-006) with run date.

## Explicitly out of scope (do not build)
Newsletter, CMS/admin UI, auth, server functions, comment systems other than giscus,
client-side charting libraries, i18n.
