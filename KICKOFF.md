# KICKOFF.md — from zero to first autonomous session

## 1. Prerequisites (one-time, on the Mac)
- Node.js 20 LTS (`node -v` to confirm; install via https://nodejs.org or homebrew)
- Python 3.10+ with `pip install nbconvert` (used by the notebook converter)
- Git configured with your GitHub account (`git config user.name / user.email`)
- VS Code 1.98+ with the **Claude Code** extension: Extensions view (Cmd+Shift+X)
  → search "Claude Code" → Install → sign in when prompted. The extension is the
  recommended way to run Claude Code in VS Code and bundles its own CLI for the
  chat panel. (Optional: `npm install -g @anthropic-ai/claude-code` if you also
  want `claude` in the integrated terminal.) Docs: https://code.claude.com/docs/en/vs-code

## 2. Repository setup
```bash
# on github.com: create PUBLIC repo named exactly: royywn.github.io  (no template)
git clone https://github.com/royywn/royywn.github.io.git
cd royywn.github.io
mkdir -p notebooks/strategies notebooks/blog content-sources/private public scripts
printf "content-sources/private/\nsrc/content/**/generated-*\n" > .gitignore
# copy in: CLAUDE.md ARCHITECTURE.md DESIGN.md PLAN.md DECISIONS.md BLOCKERS.md KICKOFF.md
# copy in: public/Roy_Yang_CV.pdf
git add -A && git commit -m "chore: project scaffold docs" && git push
```

## 3. GitHub settings (web UI, two minutes)
- Repo → Settings → Pages → Build and deployment → Source: **GitHub Actions**
- Repo → Settings → General → Features → enable **Discussions** (for giscus, Phase 3;
  config IDs come from https://giscus.app later — see BLOCKERS B-04)

## 4. Resolve the remaining pre-flight blockers (BLOCKERS.md)
- B-02: write `content-sources/bio.md` in your own words (the CV summary is a seed;
  add the human bits — why you like this work, what you tinker with)
- B-03: drop the current CV PDF into `public/`, confirm LinkedIn URL and a public
  email (consider an alias) — paste them into BLOCKERS.md as resolved

## 5. First session (Phase 1) — paste this prompt into Claude Code
Open the repo folder in VS Code → open the Claude Code panel → **Plan mode** for the
first run (review the plan before approving) → paste:

```
Read CLAUDE.md, ARCHITECTURE.md, DESIGN.md, PLAN.md, DECISIONS.md, and BLOCKERS.md
in full before touching anything. These six files are the project contract.

Then execute PLAN.md Phase 1 ONLY, following the session loop and hard rules in
CLAUDE.md exactly:
- smallest complete increments; run `npm run build` and `npx astro check` before
  every commit; conventional commits
- implement DESIGN.md tokens literally (CSS variables, fonts via @fontsource,
  light/dark modes including the honey-accent flip in dark mode)
- never invent content: placeholders are <!-- TODO:ROY --> plus a BLOCKERS.md entry
- tick PLAN.md checkboxes with a one-line note as you complete items
- if blocked, log to BLOCKERS.md and move to the next unblocked item

Stop when Phase 1 verification passes, when all remaining items are blocked, or
after 3 consecutive failed build attempts on one item (log it). Do NOT start
Phase 2. Finish with a summary: what's done, what's blocked, what I should review.
```

## 6. Review ritual (after every phase — 10 minutes, non-negotiable)
1. `npm run dev` → click through every page; check light AND dark mode.
2. Read the git diff at a skim level; read PLAN.md ticks and any new BLOCKERS entries.
3. Commit/push if not already pushed. Resolve blockers you can.
4. Start the NEXT phase in a FRESH Claude Code conversation (new tab/session) with:
   "Read the six contract docs, then execute PLAN.md Phase N only. Same rules as
   recorded in CLAUDE.md. Note: Phases 1..N-1 are complete — verify their checkboxes
   match reality before starting."

## 7. Phase-specific notes
- Phase 4 (content): BEFORE the session, copy your real .ipynb files into
  notebooks/strategies/ and add the frontmatter raw cell (template below). The agent
  must never guess at results — real notebooks in, real pages out.
- Phase 5 (deploy): after the Actions run goes green, check https://royywn.github.io
  on your phone too.
- Phase 6 (polish): provide GoatCounter code + Formspree id first, or let the agent
  log them as blocked and skip.

## Notebook frontmatter template (first cell, type = Raw)
```yaml
---
title: "Regime detection with hidden Markov models"
description: "One-sentence hook for the index page and SEO."
category: "strategies"        # strategies | optimization | risk | infra
status: "backtested"          # idea | researching | backtested | paper-trading
tags: ["regime-detection", "hmm", "python"]
date: 2026-06-15
repo: "https://github.com/royywn/your-repo"   # optional
draft: false
---
```
Cells tagged `# HIDE` (first line of a code cell) are stripped at publish time —
use for data paths, keys, and setup noise.

## Publishing loop after launch (the whole point)
save notebook → copy/update into notebooks/... → `git add -A && git commit -m
"content: <title>" && git push` → live in ~2 minutes. Writing a plain markdown
post: drop the .md straight into src/content/blog/ instead.
