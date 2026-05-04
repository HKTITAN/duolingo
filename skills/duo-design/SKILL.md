---
name: duo-design
description: UI patterns from the Duolingo design system — juicy motion, the character system as the emotional channel, design tokens (color/type/spacing), sound as a UX surface, accessibility as a default not a checklist, and "error-as-delight" detailing. Use when the user is designing a screen for a gamified or learning product, reviewing a design for "why does this feel flat," picking a motion system, building a character mascot, or auditing for accessibility. Source the Duolingo design system at design.duolingo.com.
license: MIT
metadata:
  author: HKTITAN
  version: "1.0.0"
  graph: true
---

# Duolingo Design — Map of Content

The Duolingo design system is publicly documented at [design.duolingo.com](https://design.duolingo.com). This skill extracts the *patterns* (not the literal tokens) so they apply to any gamified or learning product, not just language apps.

This skill is structured as a **graph**: scan the descriptions below, follow only the `[[wikilinks]]` you need.

## Motion and feeling

- [[references/juicy-motion]] — the bouncy, slightly-overshot easing curves that make every interaction feel responsive.
- [[references/celebration-design]] — visual grammar for "you did the thing" — confetti, scaling, character cameos.

## The character layer

- [[references/character-system]] — Duo and friends as the emotional API of the product; how to build one for any brand.

## Tokens

- [[references/color-tokens]] — the role/value split (e.g. *correct-feedback* vs. *green-500*) that lets a brand evolve without rewriting screens.
- [[references/type-system]] — Feather Bold, weight rules, and the legibility-first hierarchy.

## Surfaces

- [[references/sound-as-ux]] — non-optional audio feedback; cheap to add, disproportionately rewarding.
- [[references/progress-bars]] — the most important UI element in a gamified product, treated as such.
- [[references/bottom-bar-navigation]] — five tabs, character-icon recognition, never moves.

## Defaults

- [[references/accessibility-default]] — color-not-only, type-scaling, motion-reduce, screen-reader paths as ship blockers, not nice-to-haves.
- [[references/error-as-delight]] — an error state is a free chance to be the brand instead of break it.

## Sibling skills

- [[../duo-gamification/SKILL]] — *juicy-feedback* is design + gamification; the implementation lives here.
- [[../duo-voice/SKILL]] — celebrations and errors are also a copy problem.
- [[../duo-retention/SKILL]] — the bottom bar exists because retention requires a stable home.

## Sources

- design.duolingo.com — the public design system
- @duolingo product surfaces — observed motion and sound
