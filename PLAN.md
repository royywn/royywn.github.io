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
- [x] Content collections defined in `src/content/config.ts` with zod schemas per ARCHITECTURE.md
      (c05793b — blog + strategies schemas exactly per ARCHITECTURE.md frontmatter specs)
- [x] DESIGN.md implemented: CSS variables (light + dark incl. honey accent flip),
      @fontsource fonts (Source Serif 4, Inter, JetBrains Mono), base components
      (buttons, cards, badges) match the component specs
      (d18c5b7 — tokens verbatim in src/styles/global.css; .btn/.card/.badge classes
      + Badge.astro/Card.astro; fonts self-hosted, woff2 emitted in build)
- [x] Base.astro layout: nav (Home/About/Projects/Strategies/Blog), footer band
      per DESIGN.md, meta/OG tags, theme toggle
      (a6e693c — wordmark=home; linkedin footer link held for B-03; minimal stub
      routes for /, /about, /projects, /blog, /strategies so all nav targets render)
- [x] One placeholder entry in each collection validates against schema
      (e2ce5b6 — draft:true placeholders, rendered in dev only, never in prod builds)
- [x] `scripts/convert_notebooks.py` + npm `convert`/`predev`/`prebuild` hooks;
      generated output gitignored; frontmatter raw-cell validation with clear errors
      (4a5909e — generated-<slug>.md + asset dir match existing gitignore pattern, URL
      slug kept clean via frontmatter slug override; bad-frontmatter path tested, exit 1
      with field-level messages; venv-or-system-python shim in scripts/convert.sh)
- [x] Sample notebook in `notebooks/strategies/` (frontmatter cell + 1 plot output)
      converts and renders end-to-end
      (78e8dfa — sample-pipeline.ipynb, draft:true, saved sine-plot output; HIDE and
      empty cells stripped in output)
- VERIFY: `npm run build && npx astro check` exit 0; dev server renders all nav
  routes INCLUDING the page generated from the sample notebook; image from the
  notebook displays correctly.
  → PASSED 2026-06-12: build + check exit 0 (0 errors/warnings); dev server returned
  200 for / /about /projects /blog /strategies /strategies/sample-pipeline/
  /blog/placeholder-post/; notebook PNG served as valid 600×300 image via astro:assets.

## Phase 2 — Core pages
- [x] Landing page per DESIGN.md zone spec — use the approved hero copy verbatim
      (eyebrow, "Hi, I'm Roy.", two paragraphs, four action buttons)
      (5ee1616 — hero copy verbatim; 2 of 4 action buttons live (my cv, github);
      linkedin + say hello held as TODO:ROY pending B-03; card one-liners pending B-07)
- [x] About page rendering content-sources/bio.md content (TODO markers if absent)
      (655334a — bio.md absent (B-02): structure + TODO markers + CV button only)
- [x] Projects page with typed project data (QuantPulse, Agentic framework, Local AI infra)
      (655334a — typed array in src/data/projects.ts; descriptions/tags/repos TODO per B-07)
- [x] 404 page, robots.txt, favicon, og-image placeholder
      (08c03ed — svg monogram favicon, palette-matched og-image.png, og:image/twitter
      meta wired in Base.astro)
- VERIFY: build passes; lychee on dist reports 0 broken internal links.
  → PASSED 2026-06-12: build + check exit 0; lychee --offline on dist: 53 OK,
  0 errors. (Earlier partial run had 2 errors on /Roy_Yang_CV.pdf; closed when
  Roy dropped the PDF and resolved B-03. Hero actions are now linkedin · say
  hello per Roy — cv button moved to /about, github lives in the footer.)

## Phase 3 — Content systems
- [x] Blog index + [slug] pages + tag pages + RSS at /rss.xml
      (630031a — tag pages at /blog/tags/[tag]; rss alternate link in head; footer
      rss link stays out per Roy's earlier edit)
- [x] Strategy index (grouped by category) + [slug] pages with status badge
      (a8ad810 — fixed category order trend/mean reversion/optimization/risk/infra,
      empty groups hidden; [slug] badge shipped in Phase 1)
- [x] Post layout: reading time, conditional TOC, prev/next, giscus mount point
      (giscus repo config → BLOCKERS if not yet provided)
      (abc53fe — TOC when >800 words; giscus script gated on IDs still pending B-04)
- [x] Pagefind integrated; /search page works on built output
      (24569b3 — postbuild `pagefind --site dist`; UI assets load on /search only)
- VERIFY: build passes; rss.xml validates; pagefind index returns results for a
  known term in `npm run preview`.
  → PASSED 2026-06-12: build + check exit 0; dist/rss.xml well-formed (xmllint) with
  valid channel; pagefind query "QuantPulse" returned 2 results (top hit /projects/)
  against `npm run preview`; lychee on dist: 69 OK, 0 errors. Note: /search is not
  linked from the nav (DESIGN.md nav list has no search entry) — Roy to decide where
  it surfaces.

## Phase 4 — Content migration & seed content
- [x] Audit existing MkDocs book: list chapters WITH real code/results vs boilerplate
      → write audit table into DECISIONS.md (ADR-005)
      (6de64ee — only 8 of 32 nav'd files exist; 3 substantive chapters → rewrite,
      29 → drop; table in ADR-005)
- [x] Migrate 3–5 strongest chapters: where a real notebook exists, place the .ipynb
      (with frontmatter cell) in notebooks/strategies/; otherwise rewrite as .md
      (tone per CLAUDE.md rules; add Limitations sections; no emoji; no invented results)
      (fb5d0e3 — no real notebooks existed; chapters 7/8/20 rewritten as draft .md
      entries with Limitations + TODO:ROY result markers; stay draft until B-05)
- [x] `royplot.mplstyle` in repo root per DESIGN.md imagery spec (warm white figure
      bg, palette-matched categorical cycle); referenced in KICKOFF notebook notes
      (a29bdaa — smoke-tested render; usage note added to KICKOFF.md)
- [x] Seed 2 blog posts from existing material Roy provides (e.g. look-ahead-bias
      hunt write-up; agentic coding setup wizard) — drafts with TODO:ROY markers
      where facts are needed
      (53eaf6b — no source material provided yet, so both are structured drafts in
      Roy's voice with TODO:ROY markers for every factual claim)
- VERIFY: every migrated page passes schema; zero TODO:ROY markers remain in
  files NOT marked `draft: true`.
  → PASSED 2026-06-12: build + check exit 0 (zod schemas pass for all 7 content
  files); all 7 content files containing TODO:ROY are draft: true, zero violations.
  (Page templates still carry TODO:ROY comments tracked by open blockers B-02/B-04/B-07.)

## Phase 5 — Deploy
- [x] `.github/workflows/deploy.yml` per ARCHITECTURE (check → build → pagefind →
      lychee → deploy to Pages)
      (ccd7d40 — pagefind runs via postbuild; configure-pages with enablement:true)
- [x] astro.config `site`/`base` set per ADR-002 decision
      (set since Phase 1 scaffold da69b4b; verified: site https://royywn.github.io, base '/')
- [x] Production smoke test: fetch deployed homepage, /blog, /strategies, one post —
      all HTTP 200; OG tags present in HTML
      (2026-06-12 — / /about /projects /blog /strategies /search /rss.xml CV PDF
      og-image all 200; og:title/description/url/image present; 404 returns 404.
      No individual post page exists in production yet — all content is draft:true
      until B-05 — so "one post" is untestable until first publish.)
- VERIFY: green Actions run on main; deployed URLs return 200.
  → PASSED 2026-06-12: Actions run 27423132875 on ccd7d40 completed success
  (convert, check, build, pagefind, lychee, deploy all green); live URLs return 200.

## Phase 6 — Polish (only after 0–5 complete)
- [x] Lighthouse CI: Performance ≥95, A11y ≥95 on /, one post, one strategy page
      (ADR-006 — 100/100 on / /blog/ /strategies/; post/strategy detail pages don't
      exist in prod until B-05 publishes content — re-run then to fully satisfy)
- [ ] GoatCounter snippet (account id → BLOCKERS if absent) — BLOCKED on B-06
- [ ] Formspree contact form on /about (form id → BLOCKERS if absent) — BLOCKED on B-06
- [ ] Redirect or banner on old MkDocs site pointing to new site (if old site retained)
      — BLOCKED on B-08 (retain-vs-retire decision is Roy's)
- VERIFY: lighthouse scores recorded in DECISIONS.md (ADR-006) with run date.
  → DONE 2026-06-12 for what's verifiable: ADR-006 recorded (100/100 × 3 pages,
  zero bundled JS, lychee 0 errors). Remaining Phase 6 items blocked on B-04
  (giscus), B-06 (GoatCounter/Formspree), B-08 (old-site decision).

## Explicitly out of scope (do not build)
Newsletter, CMS/admin UI, auth, server functions, comment systems other than giscus,
client-side charting libraries, i18n.
