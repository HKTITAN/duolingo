---
name: duo-streak-mechanics-activation-threshold-as-one-shared-target
summary: Find the tenure number past which return probability jumps, publish it internally, and aim every early surface at it.
metadata:
  internal: true
---

# Activation Threshold as One Shared Target

## Concept

Early retention is not a smooth decay curve. There is usually a point past which behaviour becomes cheap to sustain — the action stops needing to be re-motivated each time and starts being triggered by context. Below that point every session is an argument you have to win again.

Finding that number and publishing it internally is what makes the early lifecycle optimisable at all. Without it, onboarding copy, notifications, celebration design and lifecycle email each optimise a different proxy. With it, they all push the same user across the same line, and you can tell whether any of them worked.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-streak-builds-habit (Duolingo blog, 2022-01-31; accessed 2026-09-22)

- Duolingo treats the **7-day streak** as its activation bar and writes that exact number into product copy ("Reach a 7 day streak..."), reminders, and the celebration design.
- The supporting figures: learners who reach a 7-day streak are **2.4x more likely to use Duolingo the next day** than learners with no streak, and **3.6x more likely to complete their course**.
- Scale as of January 2022: **over 6 million people** were on a 7+ day streak.
- The same 7-day number and the **2.4x** next-day figure are reused in learner-facing goal-setting advice, so the internal threshold and the external coaching are the same number (blog.duolingo.com/2022-language-learning-goals (Duolingo blog, 2021-12-07; accessed 2026-09-22)).

## The transferable pattern

- Look for a step, not a slope. Plot next-period return probability against consecutive-period count and find where the curve bends. That bend is your threshold.
- **The number is observational, and you should say so.** Users who reach day seven were probably already more likely to stick — the multiple is partly selection, not causation. It is still useful as a shared target; it is not a promise that pushing someone across the line converts them at the same rate. The causal version comes from an experiment on the mechanic, not from the correlation.
- Publish one number, not three. The value of a threshold comes from every surface aiming at the same line; a team with three activation definitions has none.
- Aim spend at the pre-threshold window. Effort spent carrying a user from day two to day seven is worth far more than the same effort spent on someone already at day forty, who is cheaper to keep than to re-acquire.

## Apply to your product

- What is the consecutive-usage count past which your return rate visibly jumps, and does anyone on your team know it?
- Do your onboarding copy, your notifications and your first celebration all reference that same number, or does each pick its own milestone?
- What percentage of new users currently cross it, and what happens to the ones who stall one step short?

## See also

[[fixed-low-bar-separate-ambition-dial]] · [[scarce-recovery-token]] · [[../duo-retention/references/habit-loop]] · [[../duo-experimentation/references/metric-selection]]
