# BLOCKERS.md — items requiring human input

Format: B-NN · date raised · status (open/resolved) · what's needed · why it blocks ·
what the agent did meanwhile.

---

## B-01 · 2026-06-12 · RESOLVED 2026-06-12 · GitHub username / domain decision (→ ADR-002)
Resolution: account renamed to `royywn`; hub site repo `royywn.github.io`, base `/`.
astro.config `site` = https://royywn.github.io. Custom domain deferred.

## B-02 · 2026-06-12 · OPEN · Bio source material
Needed: `content-sources/bio.md` — career narrative in Roy's own words (the CV summary
is a fine starting seed, but About page needs first-person voice and a photo decision).
Blocks: Phase 2 About page final copy.
Meanwhile: build the page with TODO:ROY markers.

## B-03 · 2026-06-12 · RESOLVED 2026-06-12 · CV PDF + final contact links
Resolution: Roy dropped `public/Roy_Yang_CV.pdf`; LinkedIn = https://www.linkedin.com/in/roy-yangwn;
public email = wingningyang@gmail.com. Roy also chose to remove the hero "my cv" and
"github" buttons — CV download lives on /about, github link lives in the footer;
hero actions are now linkedin · say hello (deviation from DESIGN.md zone 2 actions, Roy's call).
Original request below.
Needed: `public/Roy_Yang_CV.pdf` (current version), confirmed LinkedIn URL, public
email address for the site (consider an alias rather than the personal gmail).
Blocks: hero/footer links, Phase 2 verification.
Agent note (2026-06-12, Phase 1): found `CV Roy Yang Data Scientist 2026.pdf` in the
private `royywn-site-docs/` folder, but did not copy it to `public/` — publishing it
is Roy's call (confirm it is the public version, then drop it in as Roy_Yang_CV.pdf).
Agent note (2026-06-12, Phase 2): hero and about pages link "my cv"/"download cv" to
/Roy_Yang_CV.pdf, which 404s until the PDF lands; the approved "linkedin" and
"say hello" hero buttons are held as TODO:ROY comments until the URL and a public
email are confirmed. These are the only items keeping Phase 2 verification partial.

## B-04 · 2026-06-12 · OPEN · giscus configuration
Needed: enable GitHub Discussions on the site repo, then giscus repo-id/category-id
from giscus.app.
Blocks: comments mounting (Phase 3); everything else proceeds.

## B-05 · 2026-06-12 · OPEN · Strategy content ground truth
Needed: for each migrated chapter, confirmation of what was actually implemented and
any real backtest artifacts (charts/tables). The agent must not synthesize results.
Blocks: Phase 4 publishing (entries stay `draft: true` until confirmed).
Update (2026-06-12, Phase 4): three rewritten draft entries now exist
(market-trend-detection, nsga3-portfolio-optimization, ml-classification-trading) —
each has TODO:ROY markers for methodology confirmation and real results. To publish:
confirm/correct the facts, attach real artifacts (ideally as notebooks in
notebooks/strategies/ — see KICKOFF frontmatter template), set draft: false.
Both seed blog posts (53eaf6b) need the same treatment.

## B-06 · 2026-06-12 · OPEN · GoatCounter + Formspree accounts
Needed: GoatCounter site code; Formspree form id (both free tiers).
Blocks: Phase 6 only.

## B-07 · 2026-06-12 · OPEN · Project notes source material
Needed: `content-sources/projects.md` — per-project notes (what/why/stack/links) for
QuantPulse, the agentic coding framework, and local AI infra (PLAN Phase 0 input).
Blocks: Phase 2 projects page copy; Phase 1 proceeds with placeholder entries.
Meanwhile: Phase 1 placeholders carry TODO:ROY markers and `draft: true`.
Update (2026-06-12): per Roy, project repo links now point at https://github.com/royywn
as placeholders. Still needed: per-project one-liners, tech tags, and the real repo URLs.
