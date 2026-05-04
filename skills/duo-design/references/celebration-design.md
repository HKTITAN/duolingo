---
name: duo-design-celebration-design
summary: Visual grammar for "you did the thing" — confetti, scaling, character cameos, layered to land.
metadata:
  internal: true
---

# Celebration Design

## Concept

A celebration screen is the visual half of [[../duo-gamification/references/celebration-moments]]. The visual grammar is layered: a single effect (just confetti, just a scale-in) reads as cheap. Three or four effects in sequence (character entry → confetti burst → number scaling → final settle) reads as a *moment*. The discipline is composition.

## What Duolingo does

- Lesson-end, streak-milestone, and league-promotion screens use layered animation: character entrance, confetti, number/badge scaling, settling pose.
- Sound (see [[sound-as-ux]]) is part of every celebration, not an optional layer.
- Duration is calibrated — long enough to land, short enough that users don't tap-skip.
- Tier matters: a 7-day streak gets a smaller celebration than a 365-day streak. Visual scaling tracks the milestone weight.

## The transferable pattern

Three rules:

1. **Layer, don't stack.** A celebration is a sequence: things enter at different times, peak together, settle. Composing the timeline is the work.
2. **Match scale to event.** A celebration that fires equally for a small and a big win trains users to ignore both. Tier the visual response.
3. **Tap-to-skip respected.** Users who've seen the celebration 100 times should be able to skip it without feeling punished. Don't gate progression behind animation.

Anti-pattern: maximum-amplitude celebrations on every event. Without contrast, every celebration is the same; the user filters them out.

## Apply to your product

- Pick your strongest "user did something good" moment. Is it celebrated or just acknowledged?
- Does your product have multiple tiers of celebration, or one default?
- Can users skip celebrations they've seen many times before, or are they gated?

## See also

[[../duo-gamification/references/celebration-moments]] · [[../duo-voice/references/celebration-copy]] · [[character-system]] · [[juicy-motion]] · [[sound-as-ux]]
