---
name: duo-growth-model-decompose-a-flat-metric-into-state-transitions
summary: When a top-line number stops moving, rebuild it as user states plus transition rates and staff a team against one transition.
metadata:
  internal: true
---

# Decompose a Flat Metric into State Transitions

## Concept

A top-line engagement number is an aggregate of many unrelated behaviours. That is why it is a good scoreboard and a terrible target: no single team owns a mechanism that moves it, and no experiment against it has a clean hypothesis. The fix is not a better dashboard. It is to model the number as a small set of mutually exclusive user states plus the probabilities of moving between them, then attack one transition. A transition rate has a specific population and a specific behaviour attached to it, which is what makes it testable and ownable.

## What Duolingo does

Source: blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)

- Duolingo's DAU had stalled since **2018**. Rather than optimize DAU directly, the team built a **Growth Model**: a Markov model that classifies **every learner, every day**, into **7 mutually exclusive states** — New, Current, Reactivated, Resurrected, At-Risk WAU, At-Risk MAU, Dormant.
- The model measures the transition probability between each pair of states, so the top-line number becomes an output of roughly a dozen rates rather than a thing you push on.
- They then **simulated a uniform lift applied to each transition on its own** and compared downstream DAU. **Current User Retention Rate (CURR)** — today's active user still active tomorrow — dominated everything else.
- They staffed a team against **CURR alone**. **DAU grew roughly 4x from 2019** under that focus; as of early 2023 about **80% of users were acquired organically** and **7% of MAU** subscribed to Super Duolingo.
- Tension they name explicitly: the simulation only showed correlation. Before betting headcount they had to verify **two separate things** — that CURR was movable at all, and that moving CURR actually moved DAU. A transition can be perfectly predictive and completely inert.

## The transferable pattern

1. **Enumerate states, not segments.** Every user, every period, lands in exactly one bucket. Mutually exclusive and exhaustive is the whole trick — it makes the arithmetic close.
2. **Measure the arrows, not the boxes.** The boxes are the number you already have. The arrows are the levers.
3. **Simulate before you staff.** Apply the same hypothetical lift to each arrow in isolation and rank by downstream effect on the top line. Small populations with huge rates usually lose to large populations with modest ones.
4. **Prove movability separately from importance.** An arrow that predicts the outcome is not necessarily an arrow you can pull. Run a cheap experiment against the transition before you commit a team to it.
5. **Give the winning arrow an owner.** The point of the exercise is a team with one number that a weekly experiment can actually move.

## Apply to your product

- Write the five to eight states a user of your product can be in on a given day or week. Does every user land in exactly one, and do they sum to your top-line number?
- Which transition, lifted by the same fixed amount as every other, would move your top line most? Have you simulated that, or are you guessing from intuition about which users matter?
- Before staffing that transition: what is the cheapest experiment that would tell you it is movable at all?

## See also

[[movable-metrics-have-a-shelf-life]] · [[attack-the-widest-funnel-step-not-the-deepest]] · [[../duo-experimentation/references/metric-selection]]
