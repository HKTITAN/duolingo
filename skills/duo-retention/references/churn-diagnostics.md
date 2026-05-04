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

Duolingo's blog and engineering posts repeatedly describe segmenting cohorts by day-1, day-3, day-7, day-30 retention and treating each as a separate problem. The handbook's *Show Don't Tell* principle ([[../duo-experimentation/references/show-dont-tell]]) means each segment gets its own experiment program, not one omnibus "improve retention" project.

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
