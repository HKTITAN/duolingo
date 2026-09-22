---
name: duo-attention-budget-cap-novelty-then-force-immediate-use
summary: Put a hard ceiling on how much new material arrives per unit, then apply it immediately — introduction without application decays before it lands.
metadata:
  internal: true
---

# Cap Novelty, Then Force Immediate Use

## Concept

Two unfamiliar things in one unit means attention splits and neither is retained. So the cap is not a style preference — it is a hard ceiling enforced at authoring time, with the rest of the unit built from material the user already has.

The second half is timing. Material introduced but never applied has no retrieval cue attached to it, so it decays before the application arrives — and the user experiences the gap as content with no evident purpose, which is indistinguishable from busywork. Introduce a small batch, then make the user use it in the same sitting.

## What Duolingo does

Source: blog.duolingo.com/the-nuts-and-bolts-of-course-creation-at-duolingo (Duolingo blog, 2020-06-11; accessed 2026-09-22)

- Curriculum designers **explicitly manage processing load** as a named part of the job, using both digital tooling and human review to limit new material **per sentence and per skill**. The cap is enforced by tooling, not left to author judgement.
- When a single word has several meanings, Duolingo **deliberately spreads those meanings across the whole course** rather than teaching them together — one new meaning at a time, even though that means revisiting the same object repeatedly.
- Each new item is surrounded by already-seen items, so the budget is spent on the one thing actually being taught.

Source: blog.duolingo.com/intermediate-mini-units (Duolingo blog, 2026-03-04; accessed 2026-09-22)

- The intermediate mini-unit format introduces **just a handful of new words** and then puts them into use right away in Stories, DuoRadio, and Video Call — with listening and speaking sessions appearing **more frequently than in the old long-unit format**.
- The tradeoff: more, smaller units means more transitions and more ceremony per unit of content, and it makes the overall path longer to look at. Duolingo took that in exchange for shortening the gap between introduction and use.

## The transferable pattern

- **Set a number and enforce it in the tool, not the review.** "Keep it light" is not a cap. "At most N new elements per unit, blocked at authoring time" is. Whatever the number, having one changes what gets written.
- **Build the rest of the unit from known material.** A new element surrounded by familiar ones costs almost nothing extra; two new elements together cost more than double.
- **Split ambiguity across time.** When one label, object, or control has several meanings or modes, teach one per encounter. Presenting the full set at once reads as a specification, and specifications are not retained.
- **Close the introduce-to-apply gap inside the same session.** Material a user has seen but never used has no hook. If application is a week away, the introduction was mostly wasted.
- **Accept the packaging cost.** Smaller units mean more boundaries, more transitions, and a path that looks longer. That is the price of the shorter gap.

## Apply to your product

- What is the hard cap on new concepts, terms, or controls in one screen of your product — and is it enforced anywhere, or is it folklore?
- Which of your terms or controls carry more than one meaning? Are you introducing all of them at once because it felt tidier to document them together?
- How long is the gap between where you introduce something and where the user first has to use it? What would it take to close that gap to zero?

## See also

[[hold-everything-but-the-target-constant]] · [[isolate-the-new-element-at-the-front]] · [[three-kinds-of-effort-cap-cut-and-add]]
