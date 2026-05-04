---
name: duo-experimentation-novelty-effects
summary: The lift that decays after week three; how to detect novelty and discount it before shipping.
metadata:
  internal: true
---

# Novelty Effects

## Concept

A novelty effect is a temporary engagement lift caused by *change itself* rather than the change being better. New UI, new feature, new copy — users notice, engage more for a few days, and then return to baseline. Tests run for a week look like wins; the same change measured at month two shows no lift.

Most teams ship novelty as if it were durable improvement and discover the truth too late.

## What Duolingo does

- Long-running experiments (two weeks, sometimes longer) on changes prone to novelty — UI redesigns, new mechanics, copy refreshes.
- Decay analysis: explicitly checking whether the lift in week 1 holds in week 2 and week 3.
- Some tests carry post-ship monitoring even after they're shipped, to catch decay that wasn't visible at the test horizon.
- "Look good early, fade later" is a recognized pattern; experiments are designed to detect it before deciding.

## The transferable pattern

Three rules:

1. **Novelty-prone changes need longer tests.** UI / copy / new-feature changes especially. A one-week test is not enough.
2. **Plot the daily curve, not just the aggregate.** A flat lift means real change. A declining lift means novelty fading.
3. **Some changes deserve a second test after ship.** A few months later, re-test against an opposite holdout: does the change still beat the previous baseline?

Anti-pattern: shipping every win on a one-week test and being confused by flat retention three months later.

## Apply to your product

- Have you shipped changes that "won" tests but didn't move long-term metrics? How would you have detected novelty?
- For your next UI or copy test, plot the daily lift curve. Does it stay flat or fade?
- Do you have any system for catching decay after ship?

## See also

[[sample-size]] · [[hypothesis-design]] · [[ship-and-iterate]] · [[../duo-retention/references/forever-product]]
