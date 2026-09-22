---
name: duo-experimentation-metric-selection
summary: Picking a primary metric that maps to long-term retention, not the easiest one to move.
metadata:
  internal: true
---

# Metric Selection

## Concept

The metric you pick decides what your experiments optimize for. Pick the wrong primary, and a year of testing will move it — at the cost of the metric you actually cared about. Most teams pick proximate metrics (clicks, sessions, immediate revenue) because they're easier to detect. Duolingo's discipline is to build the metric you actually care about — even when it takes three rewrites and is harder to move than the one you already have.

## What Duolingo does

Duolingo's primary quality metric is not retention and not sessions. It is **Time Spent Learning Well (TSLW)**, a proprietary proxy for learning — and its history is two rejected predecessors. Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

1. **Total Sessions** — rejected. Session length varies enormously, so the metric rewarded learners grinding short easy sessions and penalized ones doing harder, longer, newer content. "More sessions = more learning" was wrong.
2. **Total Time Spent Learning** — rejected as a total. It skewed to a small set of studious learners; a competitive change like Leaderboards could grow it almost entirely through people already doing more than enough. Fixed by changing the target to *the percentage of learners spending at least 15 minutes/day*.
3. **Time Spent Learning Well** — shipped. Not all learning time is equal, so path lessons (the ones that introduce new material) count full and everything else counts half: `TSLW = minutes learning on path + 0.5 × minutes learning in other lessons`.

- The weighting is load-bearing, not cosmetic. Rebalancing XP so path lessons paid proportionately to effort was worth roughly **+1.8M minutes/day** at full adjustment (**+1.1M** at partial).
- Revenue tests are bound to retention guardrails ([[../duo-retention/references/retention-vs-revenue]]) — a revenue lift that costs retention is a loss.
- The stated backstop on all of it: *"they can't learn if they churn."* TSLW is explicitly not to be maximized at the cost of the learner coming back tomorrow — a day where all someone does is extend a streak is an acceptable day.

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

[[show-dont-tell]] · [[guardrail-metrics]] · [[outcome-not-engagement]] · [[invariant-metric-for-redesigns]] · [[../duo-retention/references/forever-product]] · [[../duo-retention/references/churn-diagnostics]]
