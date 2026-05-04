---
name: duo-gamification-combo-multipliers
summary: Within-session momentum rewards; consecutive correct answers compound, breaking the chain costs.
metadata:
  internal: true
---

# Combo Multipliers

## Concept

A combo multiplier rewards consecutive successes within a session — a streak inside a streak. The first correct answer is worth X. The fifth in a row is worth more. A wrong answer breaks the combo and resets the multiplier. This drives focus, a kind of micro-flow state where the user *cares* about the next answer in a way they didn't a moment ago.

## What Duolingo does

- Some lessons feature combo bonuses — consecutive correct answers compound XP within the session.
- Perfect-lesson rewards are a coarser version of the same idea — getting through a whole lesson with no errors unlocks a special bonus.
- "Legendary" challenge modes amplify the combo: one wrong answer ends the run.

Combos work especially well in time-pressure modes, where the user has to balance speed and accuracy.

## The transferable pattern

Three rules:

1. **Combos reward focus, not skill.** Even an experienced user can break a combo by tapping fast and wrong. This makes combos accessible to all skill levels.
2. **The break must matter.** A combo that costs nothing to break isn't a combo. The reset is the mechanism.
3. **Visible counter.** The user should be able to feel the chain — show the multiplier prominently while it's active.

Anti-pattern: stacking combos with hearts/energy. If a wrong answer costs both a heart and a combo, the combination is too punitive and users disengage.

## Apply to your product

- Are there sessions in your product where consecutive successes would feel earned and rewarded?
- What would a "broken combo" cost — visible loss, or invisible reset?
- Could you add a "perfect session" bonus, even without a full combo system?

## See also

[[juicy-feedback]] · [[xp-system]] · [[../duo-retention/references/loss-aversion]]
