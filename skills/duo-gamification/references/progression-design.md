---
name: duo-gamification-progression-design
summary: Visible structure of progress (units, sections, paths); the macro shape that gives daily action long-term meaning.
metadata:
  internal: true
---

# Progression Design

## Concept

Progression is the visible structure between "today's session" and "the goal." It shapes how a user perceives effort: a flat XP counter implies infinite grind; a path with named units implies a journey with chapters and an end. The structure is psychological, not just informational.

## What Duolingo does

Duolingo replaced the old branching **tree** of skills with a single guided **path** for all learners on November 1, 2022 — the tree is retired, don't design against it. Source: blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)

- The home screen is a literal **path** — one circle per level, grouped into units, grouped into sections. One circle equals exactly one crown level of the old tree, so the same content simply got restrung.
- Progress is *spatial* — you move through the path, not "fill up a bar." Spatial progress reads as travel; bars read as tax.
- Levels from different skills are **interleaved** along the path rather than stacked, which bakes spaced repetition into the default route. The old tree let learners gold out one skill at a time; the path makes the scientifically better order the only order.
- Each unit has a descriptive goal-shaped name ("get directions" replaced "City 3") and a visible end — a guidebook, a Legendary challenge.
- Duolingo openly acknowledged the cost: the path *looks* longer than the tree, and they had to answer that in the FAQ.

The counterintuitive finding: **adding content to make the path longer always improved their learning metric, while making lessons shorter hurt it.** Learners want fresh ground, not a shorter treadmill. Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

## The transferable pattern

Four rules for progression:

1. **Make it spatial when you can.** A path, a map, or a chapter sequence feels different from a percentage bar.
2. **Group small units into named bigger units.** Lesson → unit → section. Without grouping, every lesson feels equally weightless.
3. **Show the end of each grouping.** Users need to see a finish line, even if it's the *next* finish line, not the final one.
4. **Visual variety along the path.** Same activity, different scenery — keeps long-term users from feeling treadmilled.

Anti-pattern: a single linear bar with no chapters. It tells the user "this never ends" and trains the brain to treat the action as obligation.

## Apply to your product

- What does long-term progress look like in your product? Linear bar, chapters, map, nothing?
- Does the user know where the *next* milestone is? How far?
- Could you turn a flat counter into a spatial path?

## See also

[[xp-system]] · [[ramp-up-difficulty]] · [[../duo-design/references/progress-bars]]
