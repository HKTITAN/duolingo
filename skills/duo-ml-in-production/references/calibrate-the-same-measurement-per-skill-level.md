---
name: duo-ml-in-production-calibrate-the-same-measurement-per-skill-level
summary: An identical state is not an identical situation for a novice and an expert — one fixed threshold necessarily mislabels one of them.
metadata:
  internal: true
---

# Calibrate the Same Measurement Per Skill Level

## Concept

A severity threshold quietly assumes that the same measured state implies the same consequence for everyone. It almost never does. The probability of a bad outcome given a state is conditional on who is in it — the same recoverable situation is trivially recoverable for an expert and effectively terminal for a beginner.

So a single global cutoff is not neutral. It is calibrated for exactly one population, and mislabels everyone else in a predictable direction: it over-alarms the less capable group, whose situations are worse than the number says, and under-alarms the more capable group, whose situations are better. Both errors erode trust in the system, and neither shows up in aggregate accuracy, because the errors point opposite ways and cancel.

## What Duolingo does

Source: blog.duolingo.com/engineering-game-review (Duolingo blog, 2026-09-08; accessed 2026-09-22)

- Chess Game Review converts the engine's centipawn evaluation into expected Win-Draw-Loss, and **the conversion curve is chosen per player strength**.
- The same board position therefore produces **different win probabilities, and therefore different mistake and blunder classifications, depending on the learner's rating**.
- The underlying reason is stated plainly: a one-piece advantage converts to a near-certain win for a strong player and roughly **a coin flip** for a beginner. Calling a move that concedes that advantage a "blunder" is right in one case and misleading in the other.
- Note what is *not* per-user: the engine, the measurement, and the definition of the metric are shared. Only the calibration curve from measurement to outcome probability varies. One model, many curves.

## The transferable pattern

Separate three things that teams routinely collapse into one:

1. **The measurement** — the raw signal your instrument produces. Keep this global. It is expensive to build and you want one of it.
2. **The calibration** — the mapping from measurement to probability of the outcome. This is where capability belongs. A curve per capability tier is cheap: it is a handful of parameters fit on outcomes within that tier.
3. **The threshold** — where you decide to alert, warn, or intervene. Set this once, on the calibrated probability, and it is automatically correct for every tier.

This is far cheaper than the alternative most teams reach for, which is a separate model per tier. You fit one instrument and several small curves, and every tier still benefits from all the data used to build the instrument.

The cost is that tiers must be knowable and reasonably stable, and users near a boundary will see their labels shift as they cross it. If your tiering is noisy, the labels are noisy in a way users will notice and resent — so prefer few, wide tiers over many narrow ones, and make the tier something the user already understands about themselves.

## Apply to your product

- Does your product apply one severity threshold to users whose capability spans a wide range? Which group is it actually tuned for?
- Do you have per-user outcome data with which you could fit a calibration curve per tier, without retraining the underlying model?
- If a user's label would change purely because their tier changed, would that read as the system understanding them better, or as the system being unreliable?

## See also

[[pick-the-metric-sensitive-where-users-care]] · [[surprise-requires-a-model-of-the-expected]] · [[../duo-difficulty-calibration/references/model-the-item-and-the-user-jointly]]
