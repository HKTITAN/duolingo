---
name: duo-category-entry-validate-in-the-cheapest-shape-first
summary: Test the risky question before paying for the expensive one — fake the connected parts, prove it on one surface, and reuse existing content for reps.
metadata:
  internal: true
---

# Validate in the Cheapest Shape First

## Concept

Every new line has an expensive part and a risky part, and they are almost never the same part. The expensive part is the infrastructure — the backend, the edge cases, the second platform. The risky part is whether anyone enjoys the behaviour at all. Building them together means paying for the expensive part to learn the answer to the risky one. Separating them buys the answer first, at a fraction of the cost, and the fake version surfaces design problems while they are still cheap to fix.

## What Duolingo does

Source: blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)

- The first internal build of Friend Streak — a two-person shared streak — was **entirely on-device**. If you started a Friend Streak with someone, **they were never told**. Nothing connected to anything.
- The team calls this an "uber prototype". Colleagues enjoyed even that hacky version, and that reaction is what won leadership buy-in for the real build. The feature was **started in January 2024 and launched in September 2024**.
- One surface first, then rebuild rather than port. Duolingo ABC launched **iOS-only in 2020**, iterated and pivoted in isolation, collected external validation (**Time Best Inventions of 2020**, a **2021 Webby**), and only then was **rebuilt from scratch for Android** rather than ported. The stated house pattern is single platform, tweak in isolation, iterate, pivot, then expand. Source: blog.duolingo.com/a-good-read-building-duolingo-abc-for-android (Duolingo blog, 2022-10-06; accessed 2026-09-22)
- **Tension.** Android users are **more than half** of the flagship app's base — more than iOS and web combined. Single-platform-first means deliberately deferring the majority of your users, and platform fragmentation makes the delayed build harder rather than easier. The pattern trades reach for cheap pivots, and that trade is not always correct.
- Cheap shapes also apply to volume. To get practice reps for speaking, Duolingo added a microphone to **ordinary existing typed exercises** so a learner could speak the answer instead of typing it, and only later built dedicated speaking-only sets on top of the same material. Source: blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-speaking-skills (Duolingo blog, 2026-02-09; accessed 2026-09-22)

## The transferable pattern

Split the new line into the risky question and the expensive machinery, then buy the answer to the risky question in the cheapest shape that can produce it.

- **Fake the connected parts.** If the feature involves other people, other systems or other organizations, build the version where none of that is real. You are testing whether the behaviour is worth having, not whether the integration works. A fake that people enjoy is stronger evidence than a real one nobody has used yet.
- **Prove it on one surface.** Pivots cost one unit of work on one surface and N units on N. Once the direction is proven, rebuild for the second surface rather than porting — a port carries the first surface's accumulated compromises into the second, while a rebuild spends the validated design on the right architecture for that context.
- **Reuse existing material for reps.** New capabilities usually stall on supply of content, not on the capability. Letting people use a new input mode against material you already have multiplies reps at near-zero content cost, and lowers their activation cost because nothing else about the task is unfamiliar.

Name the trade out loud before you take it. Deferring your largest audience to keep pivots cheap is a real decision with a real cost, not a free optimization.

## Apply to your product

- For the thing you are about to build — what is the risky question, and what is the expensive machinery? Can you answer the first without building the second?
- What would the version that connects to nothing and stores everything locally look like, and who could try it next week?
- Which surface or segment could you prove this on alone, and what are you giving up by deferring the rest?

## See also

[[repeated-inbound-requests-are-the-spec]] · [[check-whether-your-core-abstraction-survives]] · [[../duo-experimentation/SKILL]] · [[../duo-product/SKILL]]
