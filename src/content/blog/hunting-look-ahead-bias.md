---
title: "Hunting look-ahead bias in my own backtests"
description: "The backtest looked great until I audited where every timestamp came from. Notes from the hunt."
date: 2026-06-12
tags: ["backtesting", "look-ahead-bias", "lessons"]
draft: true
---

<!-- Seed draft (PLAN Phase 4). TODO:ROY markers must be resolved before draft: false. -->

A backtest that looks too good usually is, and the most common reason is the
least dramatic one: somewhere in the pipeline, the strategy peeked at data it
could not have had at decision time.

<!-- TODO:ROY the hook: which backtest was it, what did the equity curve look like,
     and what made you suspicious? (your real story, 2-3 sentences) -->

## Where the future leaks in

The places I now check first, because each of them has bitten me or nearly did:

- Indicator warm-ups computed over the full series before the split.
- Normalization or scaling fitted on all history, then applied to the past.
- Labels whose horizon quietly overlaps the training window.
- Corporate actions and survivorship: today's index members backtested ten
  years into their own past.
- Timestamps: daily bars that "close" with information published after the close.

<!-- TODO:ROY which of these (or what else) was the actual culprit in your case?
     The specific bug is the whole value of this post. -->

## The hunt

<!-- TODO:ROY walk through how you found it: what you instrumented, what the
     before/after metrics were, the moment it clicked. Real numbers or nothing. -->

## What I do differently now

<!-- TODO:ROY your actual checklist/process changes (e.g. point-in-time data
     discipline, purged validation splits, "too good" alarm thresholds) -->

The general lesson I'd offer anyone building their first backtester: treat a
great-looking result as a bug report about your pipeline until proven
otherwise.
