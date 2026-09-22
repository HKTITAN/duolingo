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

Source: blog.duolingo.com/shape-language-duolingos-art-style (Duolingo blog, 2020-07-02; accessed 2026-09-22)

- Motion is used as an attention instrument, and Duolingo measured the effect: animating the skill icons on a high-ROI screen meant "learners spend more time watching the entire animation play through than they did quickly glancing at a static illustration." The art team also rotates lines and angles *inside* static artwork to steer the eye toward UI or text — motion and composition doing the same job.
- Rhythm and energy are iterated as their own variable over multiple rough-animation passes, held to be "as important to the success of Duo's transformation as the design itself" (blog.duolingo.com/streak-milestone-design-animation (Duolingo blog, 2022-01-21; accessed 2026-09-22)).
- Motion and audio are one synchronized unit in code, not a visual layer with sound bolted on: Duolingo ABC on Android uses Kotlin coroutines' `awaitAll` to fire an icon pulse and its audio cue together and wait for both before advancing, because the callback pattern offered "no clear solution to the simultaneous case" (blog.duolingo.com/a-good-read-building-duolingo-abc-for-android (Duolingo blog, 2022-10-06; accessed 2026-09-22)).
- The character rig is a Rive State Machine, picked to turn a limited asset set into a virtually unlimited number of combinations at a file size small enough to run on Android, iOS, and Web (blog.duolingo.com/world-character-visemes (Duolingo blog, 2022-11-10; accessed 2026-09-22)).
- Reduce-motion behavior is a Handbook-level rule (handbook.duolingo.com); the public blog does not document it ([[accessibility-default]]).

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
