---
title: "Multi-objective portfolio optimization with NSGA-III"
description: "Searching for portfolio weights that trade off return, drawdown, and volatility as a Pareto front instead of a single score."
category: "optimization"
tags: ["nsga3", "pymoo", "portfolio", "multi-objective", "python"]
status: "researching"
date: 2026-06-12
draft: true
---

<!-- Rewritten from MkDocs book ch. 20 (ADR-005). draft: true until Roy confirms
     what was actually implemented and supplies real artifacts (BLOCKERS B-05). -->

Collapsing return, risk, and drawdown into one number (pick your favourite
ratio) hides the decision that actually matters: which trade-off you want.
Multi-objective optimizers keep that decision visible by returning a Pareto
front of portfolios instead of a single "best" answer.

## Thesis

Portfolio construction is inherently a many-objective problem — return
maximization, volatility control, drawdown control, and turnover/cost
minimization genuinely compete. NSGA-III is built for that regime: it uses
reference directions to keep the population spread across a high-dimensional
objective space, where simpler genetic algorithms collapse onto a corner of
the front. The deliverable is a front of candidate weight vectors; choosing a
point on it is an explicit risk-preference decision, not a hidden one.

## Data & methodology

- Universe: a basket of liquid equities/ETFs with daily prices.
- Decision variables: portfolio weights (long-only, fully invested, with a
  per-position cap).
- Objectives evaluated over a historical window: annualized return (maximize),
  volatility (minimize), maximum drawdown (minimize); optionally turnover.
- Optimizer: NSGA-III via `pymoo`, SBX crossover + polynomial mutation,
  Das-Dennis reference directions.

<!-- TODO:ROY confirm the universe, constraints, objective set, and pymoo
     configuration actually used in your runs (B-05) -->

## Results

No published results yet. A Pareto front computed on historical data is an
in-sample object; the honest test is how a chosen point behaves out of sample,
and that's the part I still need to publish from my own runs.

<!-- TODO:ROY attach the real Pareto front plot + out-of-sample comparison from
     the actual notebook (B-05) -->

## Limitations

- The whole front is fit to one historical window; weights that look
  efficient in-sample routinely degrade out of sample. Walk-forward
  re-optimization is the minimum bar.
- Objectives estimated from finite samples (especially max drawdown) are
  noisy; the optimizer will happily exploit that noise.
- Evolutionary search is expensive — population × generations × backtest cost
  adds up quickly, which caps universe size and rebalance frequency.
- No transaction costs or slippage in the base formulation; adding turnover
  as an objective helps but doesn't substitute for a cost model.

## Code links

<!-- TODO:ROY link the real notebook/repo once placed in notebooks/strategies/ (B-05) -->
Implementation notebook pending — will land via the notebook pipeline.
