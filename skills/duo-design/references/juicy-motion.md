---
name: duo-design-juicy-motion
summary: Bouncy, slightly-overshot easing curves that make every interaction feel responsive instead of mechanical.
metadata:
  internal: true
---

# Juicy Motion

## Concept

Motion is one of the cheapest ways to make a product feel alive. The default in most engineering stacks is *linear* (machine-like) or *ease-in-out* (acceptable but neutral). "Juicy" motion overshoots and settles — like a real object with mass and a little bounce. The user doesn't notice the curve consciously, but they feel the difference.

This is the [[../duo-gamification/references/juicy-feedback|juicy-feedback]] node viewed from the design system side.

## What Duolingo does

- Easing curves on tap, success, and progress events use slight overshoot (a value briefly exceeding its target then settling).
- Motion durations are calibrated, not stock — fast enough to never feel laggy, slow enough to feel deliberate.
- Spring physics show up in character animations, panel transitions, and progress increments.
- Reduce-motion preferences are respected: the same product gets a quieter, non-bouncy version for users who opt out ([[accessibility-default]]).

## The transferable pattern

Three rules:

1. **Default to spring, not ease.** A modest spring-physics feel beats a polished cubic-bezier in most micro-interactions. Engines support it natively now.
2. **Calibrate duration.** Motion under 100ms feels like a glitch; over 400ms feels like a delay. Most micro-interactions live in 200–300ms.
3. **Reduce-motion is non-optional.** A motion-heavy design that breaks accessibility is a bug, not a tradeoff.

Anti-patterns:
- Linear easing on user-triggered events. Reads as machine-generated.
- Motion just for the sake of motion. Ambient animation that doesn't carry information becomes noise.

## Apply to your product

- Pick your most-frequent interaction. Is its motion linear, eased, or spring? Could it be juicier without becoming distracting?
- Have you tested the product with reduce-motion enabled? What breaks?
- Is your motion calibrated by data (eye-tracking, user testing) or by gut?

## See also

[[../duo-gamification/references/juicy-feedback]] · [[celebration-design]] · [[accessibility-default]] · [[sound-as-ux]]
