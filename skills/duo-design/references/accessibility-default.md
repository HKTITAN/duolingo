---
name: duo-design-accessibility-default
summary: Color-not-only, type-scaling, motion-reduce, screen-reader paths as ship blockers, not nice-to-haves.
metadata:
  internal: true
---

# Accessibility by Default

## Concept

Accessibility is rarely the most exciting part of a design system, but it's the part that decides whether the product is usable by 15–20% of the audience that lives outside default assumptions. Treating it as a checklist at end-of-sprint produces a product that *passes audits* but isn't actually accessible. Treating it as a default produces a product that works for everyone.

The framing matters: accessibility is the floor, not a feature.

## What Duolingo does

- **Color-not-only** for state communication: a wrong answer is red *and* shaped/iconed differently from a correct one.
- **Type respects system scaling**: large-text settings make the product larger, not broken.
- **Motion has a reduce-motion variant**: animations turn off or simplify when the OS preference is set ([[juicy-motion]]).
- **Screen reader paths are tested**: every primary flow can be completed with VoiceOver / TalkBack.
- **Contrast meets WCAG** standards as a default token-level invariant — components can't accidentally produce poor contrast because the role tokens don't allow it.

## The transferable pattern

Five rules:

1. **Color is never alone.** Any state communicated by color must also be communicated by shape, icon, or position.
2. **Type scales.** Don't override system text size; design for it.
3. **Motion is opt-out at the OS level.** Respect reduce-motion automatically.
4. **Screen reader paths are part of QA.** A flow that fails on screen reader fails ship, full stop.
5. **Contrast is a token property, not a per-screen check.** Build it into the system; don't audit it after.

Anti-patterns:
- "We'll fix accessibility in v2." It never happens; the cost compounds.
- Accessibility as a separate spec doc reviewed late in the cycle.
- Treating accessibility audits as a pass/fail check rather than a design input.

## Apply to your product

- Run your product with VoiceOver / TalkBack enabled. What flows break?
- Increase system text size to maximum. What overflows or breaks?
- Enable reduce-motion. Does the product still feel like itself, or does it fall flat?

## See also

[[color-tokens]] · [[type-system]] · [[juicy-motion]] · [[../duo-product/references/polish]] · [[../duo-product/references/raise-the-bar]]
