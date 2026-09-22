---
name: duo-ml-in-production-pick-the-metric-sensitive-where-users-care
summary: A precise metric that barely moves across the decisions users care about is worse than a coarser one calibrated to outcomes.
metadata:
  internal: true
---

# Pick the Metric Sensitive Where Users Care

## Concept

Teams default to the metric with the finest resolution, because fine resolution feels like rigor. But resolution is not the same as sensitivity. What you need is a measure whose units move when the thing the user cares about moves — one where a change of one unit means roughly the same amount of real-world difference everywhere on the scale.

A linear internal metric usually fails this. It measures accumulated quantity, not the probability of the outcome, so it is wildly over-sensitive in regions where the outcome is already decided and under-sensitive near the boundary where everything is actually at stake. Converting to an outcome-probability scale costs you granularity and buys you a scale on which "large change" and "important change" are finally the same statement.

## What Duolingo does

Source: blog.duolingo.com/engineering-game-review (Duolingo blog, 2026-09-08; accessed 2026-09-22)

- Chess Game Review classifies mistakes and blunders from changes in **expected Win-Draw-Loss, E(WDL)** — not from centipawn loss, the field's standard evaluation unit.
- **A centipawn is 1/100 of a pawn.** The scale is linear in material: **grandmaster games average under 10 centipawns of loss per move; strong amateurs under 30.**
- The failure is at the extremes. In an already-winning position a move can show an enormous centipawn loss while still guaranteeing the win — the number screams, the user experiences nothing. E(WDL) is compressed at the extremes and steep near equality, so a unit of change corresponds to a unit of change in what the user is trying to achieve.
- The scales genuinely disagree: **a Stockfish evaluation of 1.0 — a 50% self-play win rate — maps to an E(WDL) of 0.75**, not 0.5.
- The linear metric also has no natural top. **Checkmate has to be hacked in as an arbitrary value of roughly 10,000 centipawns**, which is a sign the scale was never measuring outcome.
- **The tension is real and unresolved.** E(WDL) discards granularity that experienced players are used to reading, and the team still has to consume centipawn output from the engine and convert it back through a sigmoidal curve. They pay a conversion step on every evaluation to get the better scale.

## The transferable pattern

Test a candidate metric by asking two questions:

1. **Does a large change in it always mean a large change for the user?** If there are regions of the scale where the number moves dramatically and the user's outcome does not, the metric will generate alarms nobody should act on.
2. **Does the scale need a magic number at the boundary?** If your terminal state has to be represented by an arbitrary constant well outside the normal range, the metric is measuring an intermediate quantity and calling it an outcome.

The fix is usually a monotonic transform onto outcome probability, not a new measurement system. You keep the existing instrument — it is well-tested and cheap — and convert its output at the point of interpretation. Accept the two costs openly: you lose resolution your experts liked, and you now maintain a conversion curve, which is one more thing that can silently be wrong.

Importantly, this is a decision about the *evaluation* metric, not the training objective. The model can keep optimizing the convenient quantity; what changes is the scale you threshold, alert on, and show to a person.

## Apply to your product

- Which number does your team threshold on, and is there a region of its range where it moves a lot and the user feels nothing?
- Does your scale need an arbitrary constant to represent the best or worst possible outcome?
- If you converted to probability-of-the-outcome-the-user-wants, what granularity would you lose, and who would complain?

## See also

[[calibrate-the-same-measurement-per-skill-level]] · [[surprise-requires-a-model-of-the-expected]] · [[../duo-experimentation/references/metric-selection]]
