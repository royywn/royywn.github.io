---
title: "ML classification for directional trading"
description: "Feature engineering, ensembles, and the long list of ways a promising classifier fails to become a profitable strategy."
category: "trend"
tags: ["machine-learning", "feature-engineering", "ensembles", "backtesting", "python"]
status: "researching"
date: 2026-06-12
draft: true
---

<!-- Rewritten from MkDocs book ch. 7 (ADR-005). draft: true until Roy confirms
     what was actually implemented and supplies real artifacts (BLOCKERS B-05). -->

The recipe sounds simple: engineer features from price and volume, train a
classifier to predict direction, trade the predictions. Everything interesting
about this strategy lives in the gap between that recipe and a system you'd
trust with money.

## Thesis

Cross-sectional and time-series features (returns over multiple lookbacks,
volatility, moving-average ratios, RSI/MACD-style indicators, volume ratios)
carry weak but real predictive signal for short-horizon direction. An ensemble
of simple models, validated walk-forward, can harvest some of it — if feature
leakage, label design, and costs are treated as first-class problems rather
than afterthoughts.

## Data & methodology

- Daily OHLCV for a universe of liquid names; features computed strictly from
  information available at the close being traded on.
- Feature families: multi-period returns and volatilities, price/MA and
  price/EMA ratios, oscillators (RSI, stochastic), MACD, ATR, volume ratios.
- Labels: forward return sign over a fixed horizon, with a dead zone around
  zero to avoid training on noise.
- Models: tree ensembles first (random forest / gradient boosting) — they're
  hard to beat on tabular features and easy to interrogate with feature
  importances; anything deeper has to earn its complexity.
- Validation: purged walk-forward splits; feature importance stability across
  folds matters more than any single fold's accuracy.

<!-- TODO:ROY confirm which feature set, universe, horizon, and models your
     implementation actually used — see also the local "TA feature importance"
     notebooks (B-05) -->

## Results

No published backtest yet. The book chapter this entry replaces claimed
nothing verifiable, and I won't either until real out-of-sample runs are
attached.

<!-- TODO:ROY attach real out-of-sample metrics and an equity curve with costs
     from the actual notebook (B-05) -->

## Limitations

- Look-ahead bias is the default state of this pipeline, not an edge case:
  indicator warm-ups, label horizons, and normalization fitted on full
  history all leak future information unless explicitly prevented.
- Class imbalance plus a dead zone means accuracy is a misleading metric;
  cost-aware PnL per prediction is the one that counts.
- Tabular ML degrades as the signal-to-noise ratio drops; most published
  accuracy numbers in this space don't survive realistic costs and turnover.
- Single-market training data bakes in one regime's behaviour.

## Code links

<!-- TODO:ROY link the real notebook/repo once placed in notebooks/strategies/ (B-05) -->
Implementation notebook pending — will land via the notebook pipeline.
