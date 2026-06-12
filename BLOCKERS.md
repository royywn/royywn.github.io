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

## B-03 · 2026-06-12 · OPEN · CV PDF + final contact links
Needed: `public/Roy_Yang_CV.pdf` (current version), confirmed LinkedIn URL, public
email address for the site (consider an alias rather than the personal gmail).
Blocks: hero/footer links, Phase 2 verification.
Agent note (2026-06-12, Phase 1): found `CV Roy Yang Data Scientist 2026.pdf` in the
private `royywn-site-docs/` folder, but did not copy it to `public/` — publishing it
is Roy's call (confirm it is the public version, then drop it in as Roy_Yang_CV.pdf).

## B-04 · 2026-06-12 · OPEN · giscus configuration
Needed: enable GitHub Discussions on the site repo, then giscus repo-id/category-id
from giscus.app.
Blocks: comments mounting (Phase 3); everything else proceeds.

## B-05 · 2026-06-12 · OPEN · Strategy content ground truth
Needed: for each migrated chapter, confirmation of what was actually implemented and
any real backtest artifacts (charts/tables). The agent must not synthesize results.
Blocks: Phase 4 publishing (entries stay `draft: true` until confirmed).

## B-06 · 2026-06-12 · OPEN · GoatCounter + Formspree accounts
Needed: GoatCounter site code; Formspree form id (both free tiers).
Blocks: Phase 6 only.

## B-07 · 2026-06-12 · OPEN · Project notes source material
Needed: `content-sources/projects.md` — per-project notes (what/why/stack/links) for
QuantPulse, the agentic coding framework, and local AI infra (PLAN Phase 0 input).
Blocks: Phase 2 projects page copy; Phase 1 proceeds with placeholder entries.
Meanwhile: Phase 1 placeholders carry TODO:ROY markers and `draft: true`.
