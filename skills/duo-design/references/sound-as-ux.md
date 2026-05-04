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

- Lessons have sound design throughout: correct answer, wrong answer, lesson complete, level up — each distinct, recognizable, calibrated.
- Sound is *consistent across surfaces* — the lesson-complete sound is the same on iOS, Android, and web. It's part of the brand.
- Sound respects the user: mute on the device mutes the product, system-level audio settings are honored.
- Notifications have sound IDs assigned to context (streak vs. league vs. friend activity), so users learn to recognize the sender by sound.

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
