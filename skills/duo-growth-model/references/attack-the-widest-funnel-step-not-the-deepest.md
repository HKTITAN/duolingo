---
name: duo-growth-model-attack-the-widest-funnel-step-not-the-deepest
summary: Write the funnel from eligible to fully engaged, then optimize the step with the largest population rather than the one with the loudest users.
metadata:
  internal: true
---

# Attack the Widest Funnel Step, Not the Deepest

## Concept

Optimization effort is fungible; funnel steps are not. An equal percentage gain at the step holding the largest population converts far more people in absolute terms than a big gain among the users who are already deepest in. Teams drift the other way, because deep users are loud, articulate and easy to measure, while the people stuck at step one are silent and indistinguishable from non-users. That drift is precisely backwards. The discipline is to write the whole chain — from everyone eligible to fully engaged — before optimizing anything, so the population at each step is visible as a number rather than as a feeling.

## What Duolingo does

Source: blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)

- Building Friend Streak, the team decomposed success into a **6-step funnel**: eligible → sends an invite → maintains one shared streak → sends more invites → has **5** shared streaks → maintains them daily without spending Streak Freezes.
- Having written it out, they identified **the initial invite as the biggest hurdle** and judged that **a 1% gain at the invite step beats optimizing for users who already have 5 Friend Streaks** — a much larger population multiplied by a much smaller improvement.
- The same failure shows up on opt-in surfaces, where the neglected step is installation rather than invitation. Duolingo's home-screen widget launched on iOS with **only organic discovery**, then the team tested in-app promotions after lesson completion — including an animated explainer of how to install it. **Installs skyrocketed**, and promo content, placement and frequency became a **permanent workstream** rather than a launch task (blog.duolingo.com/widget-feature (Duolingo blog, 2023-08-29; accessed 2026-09-22)).
- Tension named in that post: the widget cost **months of engineering** with an opportunity cost that would have been too high if people had not installed it. Low install rate, not low utility, is the default failure mode for anything opt-in.

## The transferable pattern

1. **Write the chain before you touch it.** Start at everyone eligible, not at everyone who has already opted in. Steps you do not write down are steps nobody owns.
2. **Put a headcount on every step.** Rank by population times plausible lift, not by how interesting the step is to work on.
3. **Suspect any plan that targets your deepest users.** They generate the clearest feedback and the smallest absolute wins. If your roadmap is full of depth work, check whether that is evidence or availability bias.
4. **Budget the awareness workstream up front.** For anything a user must deliberately turn on, adoption is gated by knowing it exists and knowing how, not by whether it is good. Give that funnel step the same experiment rigor as the feature.
5. **Treat promotion as permanent.** Placement and frequency keep decaying; a one-off launch push hands back the gain.
6. **Re-derive the widest step after every win.** Fixing the top step moves the constraint down the chain, so the ranking you computed last quarter is stale by construction.

## Apply to your product

- Write your last shipped feature as a chain from everyone eligible to fully engaged. How many people sit at each step, and which step is widest?
- Which step is your team currently optimizing — and is it the widest one, or the one where the feedback is loudest?
- For your most recent opt-in surface: what fraction of eligible users ever turned it on, and who owns that number next quarter?

## See also

[[decompose-a-flat-metric-into-state-transitions]] · [[compounding-makes-timing-a-lever]] · [[../duo-growth/SKILL]]
