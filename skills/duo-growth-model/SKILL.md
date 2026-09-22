---
name: duo-growth-model
description: Decide what to measure and which single lever to staff when your top-line engagement number has gone flat, and how to read demand that arrives from outside your product. Covers decomposing a top-line number into user states and transition rates, spotting when a segment metric has stopped resolving anything, ordering a roadmap under compounding, picking the funnel step to optimize, treating a free tier as experimentation capacity, and judging cohorts acquired from a campaign or an external shock. Trigger phrases include "our DAU is flat", "which metric should this team own", "growth model", "user state machine", "which funnel step should we optimize", "was that campaign any good", "should we go free", "why did signups spike".
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Growth Model

Measurement and prioritization for growth. This skill answers two questions: *when the top-line number stops moving, what do you measure and who owns it*, and *how do you read demand that arrives from outside the product*.

It does not tell you how to build the loops, share artifacts or campaigns that move those numbers. This skill tells you the invite step is the constraint; [[../duo-growth/SKILL]] tells you how to build the invite.

## Choosing the metric

- [[references/decompose-a-flat-metric-into-state-transitions]] — rebuild a stalled top-line number as mutually exclusive user states plus transition rates, simulate each transition alone, and staff a team against the winner.
- [[references/movable-metrics-have-a-shelf-life]] — succeeding at a segment metric grows that segment until it is the new monolith; plan the successor while the metric still works, and mine anomalies for the segments you did not know you had.

## Ordering the work

- [[references/compounding-makes-timing-a-lever]] — a retention gain feeds the next period's base, so launch date dominates lifetime value and roadmap order is a lever independent of scope.
- [[references/attack-the-widest-funnel-step-not-the-deepest]] — write the chain from eligible to fully engaged, then optimize the step with the largest population rather than the one with the loudest users.
- [[references/a-free-tier-buys-statistical-power]] — free distribution is R&D spend: volume is what makes small real effects detectable, at the permanent cost of never being able to charge for the core.

## Reading demand you did not create

- [[references/judge-a-campaign-cohort-by-its-day-60-curve]] — signup volume measures reach; the day-30 and day-60 curve, and the motivation mix underneath it, measure whether the cohort had a reason to be there.
- [[references/arrive-before-the-intention-is-assigned]] — an intention is malleable only while it is forming; land just before the occasion, because on the day itself you compete with the occasion.
- [[references/event-sharpness-not-size-predicts-the-spike]] — demand from an external shock tracks how suddenly and uniformly routines break, not the size of the shock; time your response to policy clarity, market by market.

## Sibling skills

- [[../duo-growth/SKILL]] — the loops, referrals, stunts and brand work that actually move the numbers this skill tells you to target.
- [[../duo-experimentation/SKILL]] — how to design the test that proves a transition is movable, and how much traffic it needs.
- [[../duo-retention/SKILL]] — the habit mechanics behind the transition this skill usually points you at.
- [[../duo-product/SKILL]] — prioritization, scope floors and shipping discipline once the lever is chosen.

## Sources

All claims are cited inline, in dated form, against posts on blog.duolingo.com — chiefly `growth-model-duolingo`, `growth-principles`, `duolingo-company-strategy`, `product-lessons-friend-streak`, `which-countries-are-the-best-at-keeping-their-new-years-resolutions`, and `changes-in-duolingo-usage-during-the-covid-19-pandemic`.
