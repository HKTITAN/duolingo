---
name: duo-streak-mechanics-fixed-low-bar-separate-ambition-dial
summary: The chain's bar is fixed and trivial; the user's ambitious target is tracked beside it and never gates it.
metadata:
  internal: true
---

# Fixed Low Bar, Separate Ambition Dial

## Concept

Two different jobs get confused into one number. The first job is *keep showing up* — that needs a bar so low a bad day clears it. The second job is *do enough to progress* — that is a target, and targets are meant to be missed sometimes. If you let the ambition target gate the continuity counter, one ordinary day destroys accumulated investment, and the users who set the highest target for themselves break first. The goal picker then quietly sorts your most motivated users into your worst-retaining cohort.

The fix is to decouple them. One trivial qualifying action extends the chain. The ambitious target is shown next to the chain, celebrated when hit, and never allowed to break anything.

## What Duolingo does

Source: blog.duolingo.com/improving-the-streak (Duolingo blog, 2020-11-19; accessed 2026-09-22)

- Originally the streak only advanced if the learner hit the daily goal they had chosen for themselves. Duolingo changed it so that **one lesson** extends the streak, with daily-goal progress displayed separately.
- The change was run as a **full A/B test**, not shipped on intuition, because it altered a core mechanic. Results, all relative: **+3.3% Day-14 retention**, **+1% daily active learners**, and **+10.5% more daily learners on a streak within 20 days** (**+19%** among new learners).
- A year later, learners with **7+ day streaks were up over 40%** — **just over half** of daily learners were on a 7+ day streak, against **about a third** a year earlier.
- The diagnostic that motivated it: among learners who were active two days in a row but had **no streak**, **almost 40%** had chosen the highest ("intense") daily goal. The setting they picked to express commitment was the thing preventing the habit.
- **The admitted cost.** After the change, **fewer learners actually reached their daily goals**. Duolingo traded per-day output for continuity, and says so.

## The transferable pattern

- The continuity counter and the ambition target are different instruments. Wiring one to the other means every miss costs twice.
- A self-selected stretch setting is chosen on an optimistic day and met on a median day. Read the aggressive tier as a **churn risk signal**, not a commitment signal — check its completion rate before you celebrate anyone choosing it.
- Expect the tradeoff to be real. Removing the gate lowers average effort per active day. That is only worth it if the retained days outnumber the lost depth, which is an empirical question you should measure rather than assume.
- Keep the ambitious target visible. Decoupling is not deleting: people who want the harder bar should still be able to see, hit and be congratulated on it.

## Apply to your product

- What single action extends your continuity counter today, and can a distracted user complete it in under two minutes on a bad day?
- If your onboarding asks users to pick a target, pull the data — do the users on the most ambitious tier retain better or worse than the modest tier?
- What would break if hitting the target stopped being a requirement and became a separate, celebrated event?

## See also

[[activation-threshold-as-one-shared-target]] · [[trivial-floor-protects-the-chain-not-the-outcome]] · [[../duo-retention/references/streak-mechanics]] · [[../duo-learner-motivation/references/flag-the-stretch-goal-as-a-stretch]]
