---
name: duo-gamification-xp-system
summary: A single abstract currency for forward motion; lets every action contribute to one legible number.
metadata:
  internal: true
---

# XP System

## Concept

XP (experience points) is an abstract currency — it doesn't buy anything in the conventional sense, it just goes up. The value is in the **single number**: every meaningful user action contributes to one running total, which gives the user a legible sense of forward motion across a varied product.

Without an XP-equivalent, products with multiple action types ("you did three lessons, two reviews, and one challenge") feel fragmented. With it, everything ladders into one count.

## What Duolingo does

- Every lesson, review, story, and challenge produces XP at calibrated rates.
- XP feeds three downstream systems: the daily quest target ([[../duo-retention/references/daily-quests]]), the league ranking ([[../duo-retention/references/leagues]]), and the long-term level/profile.
- XP per action is *not* equal — harder activities pay more, but the spread is small, so users don't game the easy lane.
- XP boosts (15-min double-XP) are a [[../duo-retention/references/variable-reward]] surface and a monetization option.

## The transferable pattern

A useful XP-equivalent has four properties:

1. **Single number.** Don't fragment forward motion across multiple counters; users will pay attention to at most one.
2. **Tied to core actions.** Every significant action contributes; vanity actions don't.
3. **Calibrated, not equal.** Harder/longer actions pay more, but the ratio is bounded so users don't bypass the intended path.
4. **Feeds downstream systems.** The XP number isn't the reward by itself; it's the input to leagues, levels, quests.

Anti-pattern: XP that buys nothing and feeds nothing. It becomes a vanity counter and users learn to ignore it.

## Apply to your product

- Do you have a single forward-motion number, or multiple fragmented counters?
- If you added one, what would each user action contribute, and what downstream systems would it feed?
- Is the XP-rate calibration honest (harder = more) or accidental?

## See also

[[progression-design]] · [[ramp-up-difficulty]] · [[../duo-retention/references/leagues]] · [[../duo-retention/references/daily-quests]]
