---
name: duo-retention-churn-diagnostics
summary: How to find the day where users drop off, and what each drop-off shape implies.
metadata:
  internal: true
---

# Churn Diagnostics

## Concept

Most "we have a retention problem" framings are too coarse to act on. The first move is to localize: *which day* of the user lifecycle drops, and *what shape* is the curve. Different shapes imply different fixes.

## What Duolingo does

Source: blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)

In 2018 DAU growth stalled and the team could not find A/B tests that moved it. Their fix was to stop treating DAU as one number. The **Growth Model** is a Markov model that classifies every learner into one of **7 mutually exclusive daily states** — New, Current, Reactivated, Resurrected, At-Risk WAU, At-Risk MAU, Dormant — and tracks the transition rate between each pair. DAU is then just the sum of the active states.

They simulated pulling each transition lever 2% month-over-month and found one dominated: **Current User Retention Rate (CURR)**. A team was staffed on CURR alone. **DAU grew 4x from 2019.**

One state they measured by hand first: **resurrection** (≥30 days inactive, then back). It was much bigger than expected — **~5% of DAU on a given day** — and those users are **~20% less likely than a new user to still be active at both 7 and 14 days**. The day a newsletter announced the Japanese course launch, resurrections spiked from 5% to 8% of DAU (blog.duolingo.com/back-from-the-brink-what-duolingo-learned-about-its-resurrected-users (Duolingo blog, 2017-08-30; accessed 2026-09-22)).

Tension Duolingo names: the fix ate itself. Current Users are now **90% of DAU**, so CURR has become an average over a monolith again — "an increasingly imprecise measure," at risk of becoming unmovable exactly the way DAU was in 2018. A segmentation that works stops working once the segment you optimized swallows the population.

The handbook's *Show Don't Tell* principle ([[../duo-experimentation/references/show-dont-tell]]) means each segment gets its own experiment program, not one omnibus "improve retention" project.

## The transferable pattern

Four common drop-off shapes and what each typically means:

| Shape | Implication | First place to look |
|---|---|---|
| Day-1 cliff | Onboarding fails to deliver value before the user leaves | First-session experience, [[../duo-voice/references/onboarding-copy]] |
| Day-3 to day-7 decay | Habit isn't forming; no second/third reason to return | [[habit-loop]], [[streak-mechanics]], [[notification-discipline]] |
| Day-30 erosion | Long-term motivation drains; novelty exhausted | [[leagues]], [[../duo-gamification/references/progression-design]] |
| Sudden plateau then steep drop | Specific blocker (paywall, difficulty wall, broken UX) | Funnel each step; look for the screen with the cliff |

Diagnostic discipline:

1. Plot the curve before proposing fixes.
2. Treat each segment as a separate problem with its own metrics.
3. The fix that helps day-1 retention often does nothing for day-30 retention. Don't assume.

## Apply to your product

- Plot your cohort retention by day. Which day has the steepest drop?
- Does that drop look like a cliff (UX bug) or a decay (habit failure)?
- Which of the four shapes above does your worst segment match? What does that imply?

## See also

[[habit-loop]] · [[notification-discipline]] · [[../duo-experimentation/references/metric-selection]] · [[../duo-product/references/intuitive-by-default]]
