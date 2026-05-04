---
name: duo-experimentation-metric-selection
summary: Picking a primary metric that maps to long-term retention, not the easiest one to move.
metadata:
  internal: true
---

# Metric Selection

## Concept

The metric you pick decides what your experiments optimize for. Pick the wrong primary, and a year of testing will move it — at the cost of the metric you actually cared about. Most teams pick proximate metrics (clicks, sessions, immediate revenue) because they're easier to detect. Duolingo's discipline is to pick metrics that *map to long-term retention* even when they're harder to move.

## What Duolingo does

- The primary metric for most retention experiments is some flavor of cohort retention — Day-1, Day-7, Day-30, Day-90 — not session count or DAU.
- Revenue tests are bound to retention guardrails ([[../duo-retention/references/retention-vs-revenue]]) — a revenue lift that costs retention is a loss.
- "Engagement" is broken into specific behaviors (lessons completed, perfect lessons, streak extended) rather than treated as a single number.
- The handbook's *Take the Long View* is what authorizes choosing harder-to-move metrics.

## The transferable pattern

A useful hierarchy:

| Tier | Metric type | Example | Use for |
|---|---|---|---|
| 1 (north star) | Long-term retention | 30/90-day cohort retention | All experiments, even if hard to move |
| 2 (proxy) | Behavior strongly correlated with tier 1 | Sessions per week, completed core action | When tier 1 is too noisy at small N |
| 3 (operational) | Immediate response | CTR, conversion, time-on-screen | Diagnostic only, never primary |

Three rules:

1. **Tier-1 is the boss.** A tier-3 win that costs tier-1 is a loss.
2. **Tier-2 metrics need to be *validated* against tier-1 quarterly.** Proxies drift; what correlated with retention last year may not now.
3. **Never let proximate metrics become primary by default.** They sneak in because they're easy.

## Apply to your product

- What is your team's current primary metric for product experiments? Is it tier 1, 2, or 3?
- Have you validated that your tier-2 proxies still correlate with your real long-term metric?
- What experiment did you ship recently that won on a proxy? Did the long-term metric follow?

## See also

[[show-dont-tell]] · [[guardrail-metrics]] · [[../duo-retention/references/forever-product]] · [[../duo-retention/references/churn-diagnostics]]
