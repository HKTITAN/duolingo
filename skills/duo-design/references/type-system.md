---
name: duo-design-type-system
summary: A typography system optimized for legibility-first hierarchy — type carries the brand, but never at the cost of reading.
metadata:
  internal: true
---

# Type System

## Concept

A type system is a typography contract: which fonts, which weights, which sizes, where each is used. The Duolingo system is a single distinctive display face deployed in a small, opinionated scale — the specific families are documented in the Handbook, not publicly. The discipline is restraint: three sizes used consistently beat eight sizes used randomly.

## What Duolingo does

Source: blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

- The 2026 core-tabs refresh was triggered partly by type. Across tabs that each shipped fine on their own, "headers varied in size, typography lacked hierarchy, and spacing felt inconsistent" — and those small details compounded into an experience that "didn't feel polished and cohesive."
- The fix was a scale, not a style guide: "we evolved our type system to be consistent and intentional with a minimal number of styles."
- Hierarchy is carried by header sizes graded to each tab's *purpose*, with the title held in a constant position across tabs. Size varies where it signals something; position never does.
- Whitespace does the separating work containers used to: the team "purposefully us[ed] the whitespace around the components instead of forcing containers around them."
- Large type and minimal scrolling are treated as load reduction rather than styling — the Duolingo English Test uses both to cut visual and working-memory demand (blog.duolingo.com/inclusive-testing-technology (Duolingo blog, 2022-01-27; accessed 2026-09-22)).

**What this shipped as.** Higher engagement across tabs *while core learning metrics held flat* — the right bar for a pure craft pass, since polish compounds into trust rather than into one metric. Typeface names and the token-level scale live in the Handbook (handbook.duolingo.com), not on the blog.

## The transferable pattern

Three rules:

1. **Constrain the scale.** 4–6 type sizes for the entire product. Ad-hoc sizes accumulate and the system frays.
2. **Bold for hierarchy, not decoration.** Bold draws the eye; use it for what should be looked at. Bold-everywhere is bold-nowhere.
3. **Legibility outranks personality.** A distinctive but unreadable typeface is a brand cost. The font that survives in long-form content is the one that wins.

Anti-patterns:
- Light or extra-light weights for body text. Looks designed; reads poorly. Especially fails accessibility.
- Multiple branded typefaces. One distinctive face is a system; two is a fight.

## Apply to your product

- How many distinct type sizes does your product use? Could it use half?
- Where is bold used decoratively rather than hierarchically?
- Does your type scale to user accessibility settings, or override them?

## See also

[[color-tokens]] · [[consistency-vs-purpose]] · [[accessibility-default]] · [[../duo-product/references/polish]]
