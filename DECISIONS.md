# DECISIONS.md — append-only ADR log

Format per entry: ADR-NNN · date · status (proposed/accepted/superseded) · decision ·
context · alternatives considered · consequences.

---

## ADR-001 · 2026-06-12 · accepted · Astro over MkDocs/Hugo/Next.js
**Context:** Existing site is MkDocs Material structured as a "book." Goal shifted to
personal portfolio + blog + selective strategy write-ups for job search.
**Decision:** Build the hub site in Astro 4 (static output, content collections,
Tailwind). MkDocs book content is migrated selectively, not wholesale.
**Alternatives:** MkDocs (docs-shaped, generic look, weak landing/blog ergonomics);
Hugo (fast but Go templating raises iteration cost for agentic editing); Next.js
static export (heavier runtime, unnecessary React payload for content pages).
**Consequences:** One-time migration effort; site itself becomes evidence of
frontend competence; near-zero JS keeps Lighthouse budgets achievable.

## ADR-002 · 2026-06-12 · accepted · Username, repo, and domain
**Context:** Original username `forgetsomething` was weak for a CV. User-site vs
project-site affects base paths and canonical URLs.
**Decision:** Account renamed to `royywn`. Hub site lives in repo `royywn.github.io`,
served at `https://royywn.github.io` with `base: '/'`. Existing MkDocs book remains
a project page at `/algotrading-strategy` until Phase 4 migration completes, then
gets a redirect banner (Phase 6). Custom domain deferred — can be layered on later
with no architectural change.
**Consequences:** No base-path complexity; CV/GitHub/site URLs are consistent;
old book URLs keep working during migration.

## ADR-003 · 2026-06-12 · accepted · No backend; static + third-party services
**Context:** GitHub Pages is static-only; job-search site needs comments, search,
contact, analytics.
**Decision:** giscus (comments), Pagefind (search), Formspree/mailto (contact),
GoatCounter (analytics), GitHub Actions (CI/CD). No servers, no databases.
**Consequences:** Zero hosting cost/ops; all state lives in GitHub or third parties;
acceptable because nothing here is sensitive or transactional.

## ADR-004 · 2026-06-12 · accepted · Reframe "book" → "strategy notebook"
**Context:** Current site presents a 32-chapter book with marketing-style claims
(video tutorials, email support, success metrics) that don't exist. In a hiring
context this reads as unedited AI output and damages credibility.
**Decision:** Strategies section is framed as a working notebook of implemented,
tested techniques. Every entry carries a status badge (idea/researching/backtested/
paper-trading) and a mandatory Limitations section. Chapters without real code or
results are dropped.
**Consequences:** Less apparent volume, far higher credibility; honest status
labelling turns incompleteness into a feature (visible research pipeline).

## ADR-007 · 2026-06-12 · accepted · Notebook-first authoring via build-time nbconvert
**Context:** Roy's technical work lives in Jupyter notebooks; ease of update/
maintenance is the top priority. Astro cannot render .ipynb natively.
**Decision:** Notebooks in `notebooks/` are the source of truth. A converter script
(nbconvert wrapper) renders them to gitignored markdown in `src/content/` on every
dev/build. Frontmatter lives in a raw YAML cell at the top of each notebook.
Notebooks are never executed in CI — outputs publish as saved.
**Alternatives:** Quarto (native .ipynb publishing, lowest friction, but generic
visual identity and loses the custom-design showcase value); manual nbconvert per
post (error-prone, breaks the drop-and-push workflow); MDX islands per notebook
(heavy, unnecessary).
**Consequences:** Publishing = save notebook, copy to folder, push. One-time
converter cost paid in Phase 1; deterministic builds; no CI data dependencies.

## ADR-005 · 2026-06-12 · accepted · MkDocs chapter audit table
**Context:** Phase 4 audit of the `algotrading-strategy` MkDocs book (source:
`~/Desktop/algotrading 2022/royywn/algotrading-strategy/docs`). The nav lists 32
chapters; only 8 markdown files exist on disk.

| Chapter(s) | File state | Verdict | Reason |
|---|---|---|---|
| 7. ML Trading | 750 lines, 6 code blocks | **rewrite** | Substantive technique exposition, but generic AI-tutorial prose; no real backtest artifacts. Rewritten as draft strategy entry, results pending B-05. |
| 8. Market Trend Decision | 471 lines, 7 code blocks | **rewrite** | Same: real technique content (trend classification across horizons), AI-tutorial tone, no artifacts. Rewritten as draft entry. |
| 20. NSGA-III | 635 lines, 6 code blocks | **rewrite** | Most substantial chapter; multi-objective portfolio optimization with pymoo. Rewritten as draft entry. |
| 1. Trend Trading | 28-line "coming soon" stub | **drop** | No content. |
| Front matter (index, why-algo-trading, book-structure, target-audience) | exist | **drop** | Book marketing/meta, not strategy content; the new site's framing (ADR-004) replaces it. |
| 2–6, 9–19, 21–32 (24 chapters) | files do not exist | **drop** | Nav entries only; nothing to migrate. |

**Decision:** Migrate exactly 3 chapters (7, 8, 20) as rewritten `.md` strategy
entries — first-person tone, honest status (`researching`), mandatory Limitations,
`draft: true` until Roy confirms what was actually implemented and supplies real
artifacts (BLOCKERS B-05). The book's AI-generated code is treated as illustrative
sketches, not as Roy's production code; real implementations arrive as notebooks.
**Consequences:** Strategies section starts honest and thin (3 drafts + sample
pipeline); volume grows only with verified content. The old book can be retired
after Phase 6 redirect/banner.

## ADR-006 · _pending_ · Launch quality record
_To be filled in Phase 6: Lighthouse scores, JS payload, link-check result, date._
