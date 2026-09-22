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

Duolingo's version of the combo is not an XP multiplier — it's a **resource that consecutive correct answers refill**.

- **Energy.** "You earn energy when you get multiple answers in a row right." The chain doesn't pay you points; it buys you the ability to keep playing. Source: blog.duolingo.com/duolingo-energy (Duolingo blog, 2025-07-03; accessed 2026-09-22)
- **Perfect-lesson bonuses** are the coarser, whole-session version: the same post grants **bonus energy** for a perfect lesson, alongside adding a friend and reward chests.
- A perfect lesson also unlocks the "hard" exercise set, now fronted by the character Eddy — so the reward for a clean run is *more* work, framed as encouragement. Source: blog.duolingo.com/product-highlights (Duolingo blog, 2025-12-10; accessed 2026-09-22)
- **Perfect Lessons is one of four Personal Record badges** (with Longest Streak, Daily Most XP, Highest League), so the chain also feeds a beat-your-own-best target rather than only a global threshold. Source: blog.duolingo.com/achievement-badges (Duolingo blog, 2023-12-11; accessed 2026-09-22)

Note the design choice: coupling the chain to the *failure meter* rather than to score means a broken chain costs runway, not bragging rights — the punishment is felt immediately and in the currency the user is already watching.

## The transferable pattern

Three rules:

1. **Combos reward focus, not skill.** Even an experienced user can break a combo by tapping fast and wrong. This makes combos accessible to all skill levels.
2. **The break must matter.** A combo that costs nothing to break isn't a combo. The reset is the mechanism.
3. **Visible counter.** The user should be able to feel the chain — show the multiplier prominently while it's active.

Anti-pattern: stacking two independent punishments on one wrong answer. Duolingo avoided this by **merging** them — under Energy there is one meter, and the chain refills it rather than a second counter resetting on top of a heart loss.

## Apply to your product

- Are there sessions in your product where consecutive successes would feel earned and rewarded?
- What would a "broken combo" cost — visible loss, or invisible reset?
- Could you add a "perfect session" bonus, even without a full combo system?

## See also

[[juicy-feedback]] · [[xp-system]] · [[../duo-retention/references/loss-aversion]] · [[beat-your-own-best]]
