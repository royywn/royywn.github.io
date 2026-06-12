---
title: "Classifying market trend across time horizons"
description: "Using ML classifiers to label short-, mid-, and long-term trend so downstream strategies know what kind of market they're in."
category: "trend"
tags: ["trend-detection", "classification", "random-forest", "python"]
status: "researching"
date: 2026-06-12
draft: true
---

<!-- Rewritten from MkDocs book ch. 8 (ADR-005). draft: true until Roy confirms
     what was actually implemented and supplies real artifacts (BLOCKERS B-05). -->

Most of my strategy ideas don't fail because the signal is bad — they fail
because the signal is applied in the wrong kind of market. Before any entry
logic runs, I want an honest answer to a simpler question: what is the market
doing right now, and on what time scale?

## Thesis

Trend is not one thing. A market can be in a short-term pullback inside a
mid-term uptrend inside a long-term sideways range, and a strategy tuned for
one of those layers will get hurt trading against the others. The idea here is
to treat trend identification as a supervised classification problem per
horizon — short (days), mid (weeks to months), long (months to years) — and
let downstream strategies condition on the combined label.

## Data & methodology

- Daily OHLCV bars as the base input; longer horizons work on resampled series.
- Features per horizon: multi-period returns and volatilities, price-to-moving-
  average ratios, and momentum indicators, with lookbacks scaled to the horizon.
- A random-forest classifier per horizon, labelling forward windows as
  up / down / sideways from realized forward returns.
- Walk-forward validation rather than a single train/test split — trend
  labels are heavily autocorrelated and a random split flatters the metrics.

<!-- TODO:ROY confirm the actual feature set, labelling thresholds, and validation
     scheme used in your implementation; the above is the book chapter's design (B-05) -->

## Results

No published backtest yet. This entry stays a draft until I can attach real
out-of-sample results from my own runs.

<!-- TODO:ROY attach real artifacts: confusion matrices / accuracy by horizon /
     equity curves from the actual notebook (B-05) -->

## Limitations

- Labels derived from forward returns embed a look-ahead subtlety: the
  threshold separating "sideways" from "trend" is itself a fitted choice and
  easy to overfit.
- Classification accuracy is not tradability — a 55% accurate up/down call
  can still lose money after costs if the wins are small and losses large.
- Regime changes are exactly where the classifier is weakest (the training
  distribution no longer applies) and exactly where you need it most.
- Transaction costs and slippage are not modelled at this stage.

## Code links

<!-- TODO:ROY link the real notebook/repo once placed in notebooks/strategies/ (B-05) -->
Implementation notebook pending — will land via the notebook pipeline.
