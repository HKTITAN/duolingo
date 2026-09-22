---
name: duo-design-prototype-the-extremes
summary: Explore by pushing each competing value to its maximum as a separate complete direction, not by generating variations around the status quo.
metadata:
  internal: true
---

# Prototype the Extremes

## Concept

The default exploration habit is to produce four mockups that differ by a bit of padding, a corner radius, a shade. All four sit near the current design, so comparing them tells you nothing about which dimension actually matters — you end up picking the one that looks nicest today and learning no rule you can reuse tomorrow. Pushing each competing value to its maximum instead produces directions that visibly break in different places, and the breaking points are the finding. You carry them into the real design; you never ship the extremes themselves.

## What Duolingo does

Source: blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

- For the core tabs refresh the team ran a divergent sprint, then scaled the most promising ideas into **4 distinct extreme directions**, each committed to a single value: *Punchy* (solid vibrant headers), *Soft* (calming gradients), *Modular* (card-based composition), *Flat* (minimal, heavy whitespace).
- Each direction was built as a quick, scrappy prototype and **tested on real phones**, not judged as a static frame — so the cost of each extreme showed up as a felt experience rather than an opinion about an image.
- Feedback was collected broadly across the company at this stage, while the work was still cheap to throw away.
- What shipped is not any one of the four taken whole. It is a tiered system assembled from what the extremes proved: header treatment graded by each tab's purpose, a minimal type scale, whitespace used around components instead of containers forced around them. Rollout was iOS first, Android after.

## The transferable pattern

Three rules:

1. **One value per direction, taken to its limit.** If a direction is describable as "a bit more X," it is a variation, not an exploration. Name the value out loud, then over-serve it.
2. **Prototype on the real device.** Extremes fail in ways a static frame hides — a treatment that reads as bold at desk size reads as shouting in the hand.
3. **Harvest, don't choose.** The output of the sprint is a list of where each value stopped working. The final design is built from those limits, not selected from the candidates.

Anti-patterns:
- Running the sprint after the direction is already decided, so it becomes a justification exercise.
- Polishing the extremes. Effort spent making them presentable is effort that makes them hard to discard.
- Showing extremes to people who will read them as ship candidates without framing them as probes.

## Apply to your product

- Name the two or three values currently in tension in the surface you are redesigning. Can you state each as a direction someone could build?
- Are your current explorations distinguishable at a glance from across the room, or only side by side at 100%?
- What would you have to give up to take each value to its maximum, and is that tradeoff documented anywhere?

## See also

[[consistency-vs-purpose]] · [[craft-pass-guardrail]] · [[../duo-experimentation/references/hypothesis-design]] · [[../duo-product/references/ship-it]]
