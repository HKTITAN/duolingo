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

Source: blog.duolingo.com/learning-with-hearing-aids (Duolingo blog, 2026-01-20; accessed 2026-09-22) and blog.duolingo.com/inclusive-testing-technology (Duolingo blog, 2022-01-27; accessed 2026-09-22)

- **Escape hatches sit at the granularity of the blocked modality, not the session.** For listening there are four, graduated: "Can't listen now" skips every listening exercise in that lesson; DuoRadio offers "Do this later" and never blocks progress; a settings toggle disables listening exercises outright; and the Practice Hub offers a listening-only lesson for when the learner *does* want it. None of these costs progress or the streak. WHO estimates 1.5 billion people — nearly 20% of the world — live with hearing loss.
- **Every timed stimulus has a decomposed version.** The turtle button replays a sentence slowly with pauses inserted between words; the speaker can be tapped unlimited times, including after entering an answer and before submitting.
- **Load is removed from the task itself, not just restyled.** The Duolingo English Test dropped the test-center visit, shortened the exam with computer-adaptive testing instead of demanding three hours of sustained concentration, and uses large type and minimal scrolling to cut visual and working-memory load. 26% of Americans — one in four — have a disability.
- **The opt-out is honored but not treated as permanent.** A learner who disabled listening and later enters a listening-only practice lesson is re-prompted to turn it back on.
- **Color-not-only, contrast as a token-level invariant, reduce-motion variants, and screen-reader QA** are Handbook-level design rules (handbook.duolingo.com); the public blog does not document them, so do not cite one for them.

**The tension Duolingo names.** Design alone is not sufficient: the DET post concedes that even a well-designed test stays inaccessible for some people, so a human accommodations team is still required. Accessibility work does not terminate in a passing audit.

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
