---
name: duo-gamification-ramp-up-difficulty
summary: Difficulty calibrated to keep users in flow state — never too easy, never a wall.
metadata:
  internal: true
---

# Ramp-Up Difficulty

## Concept

Flow state (Csikszentmihalyi) is the band between boredom (too easy) and anxiety (too hard). A learning product is most engaging when it spends most of the user's session in that band. Pacing is the engineering: harder content arrives just as the user is ready, not before, not after.

## What Duolingo does

- A new concept introduces with high-context exercises (matching, listen-and-pick) before requiring full production (translate, speak).
- Content within a unit gets harder; the next unit resets to a new manageable starting point.
- The path visualizes spaced practice — review nodes appear between new content so users hit older material at calibrated intervals.
- Difficulty is *experimentally* calibrated: completion rates, error rates, and session-length metrics tell the team where the curve is too steep or too flat.

## The transferable pattern

Three rules:

1. **Introduce before testing.** Every new concept gets a low-stakes first encounter before it's required for completion.
2. **Reset the floor at each grouping.** A new unit shouldn't start at the previous unit's end-difficulty; users need a runway.
3. **Calibrate by data, not gut.** "This feels right" produces curves designed for the designer, not the median user. Use completion rate as the primary signal.

A useful rule: aim for ~80% success rate on first attempt at any given exercise. Below 50% is punishing; above 95% is unrewarding.

## Apply to your product

- Does your product have a difficulty/complexity curve, or does every user hit everything at full force from day one?
- If you have a curve, do you measure success rate per stage?
- Where is the first wall a typical user hits? Should it be there?

## See also

[[xp-system]] · [[progression-design]] · [[anti-grind]] · [[../duo-experimentation/references/metric-selection]]
