---
name: duo-design-sound-as-ux
summary: Non-optional audio feedback as a UX surface; cheap to add, disproportionately rewarding when calibrated right.
metadata:
  internal: true
---

# Sound as UX

## Concept

Sound is the most under-used UX surface in product design. Most digital products are silent — partly out of respect (don't disturb), partly out of laziness (sound design is unfamiliar). But sound, calibrated correctly, is one of the cheapest ways to add emotional richness: a correct-answer sound, a level-up sound, a streak-extended sound.

The discipline: sound is *part of the design system*, not a layer added late. Calibration matters as much as inclusion.

## What Duolingo does

Source: blog.duolingo.com/a-good-read-building-duolingo-abc-for-android (Duolingo blog, 2022-10-06; accessed 2026-09-22)

- Audio is load-bearing, not garnish: Duolingo ABC "relies heavily on audio narration and animation," and narration is assembled at runtime from separate clips — *the letter team* + [first letter] + [second letter] + *says* + [phoneme] — so one recorded set covers every letter team in the curriculum.
- Sound and motion are synchronized in code as a single unit. The app uses Kotlin coroutines' `awaitAll` to run an icon pulse and its audio cue simultaneously and wait for both before advancing, precisely because the callback pattern gave "no clear solution to the simultaneous case." Sound added late cannot be synchronized; it has to be in the same execution graph as the animation.
- Sound has a measurable shipping cost: assets are 32% of the app binary, sound effects among them (blog.duolingo.com/emerge-tool-app-size (Duolingo blog, 2023-07-14; accessed 2026-09-22)).
- Audio is controllable at the granularity of the exercise, not the app. The turtle button replays a sentence slowly with pauses inserted between words; the speaker can be tapped unlimited times, including after entering an answer and before submitting; and a learner can skip all listening exercises in a lesson or disable them in settings without losing progress or their streak (blog.duolingo.com/learning-with-hearing-aids (Duolingo blog, 2026-01-20; accessed 2026-09-22)).
- Cross-platform sound identity and per-context notification sound IDs are Handbook material (handbook.duolingo.com); the public blog does not document a sound-design system.

## The transferable pattern

Five rules:

1. **Sound design is design.** Hire for it, document it, calibrate it. Don't outsource sounds to whoever has stock samples.
2. **Map sound to event types, not screens.** A "success" sound should be the same across the app, not different per screen.
3. **Calibrate volume relative to the device.** Sounds that are pleasant on the design machine can be jarring on a phone speaker.
4. **Honor mute aggressively.** A sound that fires when the device is muted is a brand cost. No exceptions.
5. **Distinctive but not annoying.** A sound is heard hundreds of times a week by long-term users. The bar is not "cool"; it's "doesn't fatigue."

Anti-patterns:
- Stock UI sounds copied from a sample pack. Reads as generic, recognizable as not-original.
- Sound triggered by ambient events the user didn't cause. Almost always feels surveillance-y.

## Apply to your product

- Does your product have *any* sound design? Why or why not?
- If yes, are sounds mapped to event types or per-screen ad-hoc?
- Have you tested the product muted, on speaker at a coffee shop, and with headphones at maximum volume?

## See also

[[juicy-motion]] · [[../duo-gamification/references/juicy-feedback]] · [[../duo-gamification/references/celebration-moments]] · [[accessibility-default]]
