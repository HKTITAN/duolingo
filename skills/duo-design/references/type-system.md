---
name: duo-design-type-system
summary: A typography system optimized for legibility-first hierarchy — type carries the brand, but never at the cost of reading.
metadata:
  internal: true
---

# Type System

## Concept

A type system is a typography contract: which fonts, which weights, which sizes, where each is used. The Duolingo system uses a single primary typeface (Feather Bold for branding/display, with variants for body) deployed in a small, opinionated scale. The discipline is restraint — three sizes used consistently beat eight sizes used randomly.

## What Duolingo does

- A small set of type tokens (e.g. `display`, `heading`, `body`, `caption`) used everywhere; no ad-hoc font sizes.
- A primary typeface that's distinctive (carries brand) but legible at small sizes (carries content).
- Weight rules: bold for headings and prompts, regular for content, never lighter than regular for body text.
- Type scales tied to user accessibility settings — Dynamic Type respected, not overridden.

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

[[color-tokens]] · [[accessibility-default]] · [[../duo-product/references/polish]]
