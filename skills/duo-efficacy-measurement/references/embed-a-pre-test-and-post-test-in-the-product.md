---
name: duo-efficacy-measurement-embed-a-pre-test-and-post-test-in-the-product
summary: Make each user their own control by testing them on a segment before and after it, and keep the scores private.
metadata:
  internal: true
---

# Embed a Pre-Test and Post-Test in the Product

## Concept

Self-paced products have no controlled cohort. Everyone arrives with different prior knowledge, moves at a different speed, and leaves when they like, so post-hoc analytics cannot separate what you taught from what the user already knew. Testing the same person before and after a segment removes that problem without recruiting anyone: each user becomes their own control, and the gap between the two measurements is the closest thing to a causal estimate a self-paced product can get for free.

## What Duolingo does

Source: blog.duolingo.com/doing-our-homework-checking-in-on-how-well-were-teaching (Duolingo blog, 2020-01-31; accessed 2026-09-22)

- The Checkpoint Quiz sits between course sections and **must be passed to unlock the next one** — measurement as a gate, not an optional survey, so response rates are structural rather than voluntary.
- It **deliberately includes questions on material not yet taught**. That portion is the pre-test for the section the learner is about to start, collected at zero extra cost inside a quiz they were already taking.
- Results are **scored only in aggregate** and are not shown to the individual. Keeping them private removes the incentive to game, and it is precisely what licenses asking deliberately hard, not-yet-taught questions without demoralizing anyone.
- Aggregated results feed resource allocation — which sections get rewritten, where teaching is weak.
- The same checkpoint carries a **freeform writing item capped at 200 characters**, answering an open prompt, added explicitly to assess how well concepts like the past tense were being taught and to separate receptive skill (reading, listening) from productive skill (writing, speaking) (blog.duolingo.com/how-weve-improved-the-duolingo-learning-experience-this-year-and-a-sneak-peek-toward-2020 (Duolingo blog, 2019-12-11; accessed 2026-09-22)).

Duolingo states the limitation directly rather than letting the design imply more than it proves: this **cannot exclude learning the user acquired from other sources** during the course. Pre/post within one product is a strong design against prior knowledge and a weak one against concurrent outside exposure.

## The transferable pattern

- **Put the measurement in the path, not beside it.** A gate everyone passes through produces a representative sample. An opt-in survey produces the enthusiasts.
- **Ask about the next segment before you teach it.** The pre-test rides along inside an assessment the user is already completing, so it costs one extra question rather than one extra experience.
- **Score in aggregate, hide from the individual.** Private scores can be hard. Visible scores become a target, and a measure that users optimize against stops measuring.
- **Add one open-ended production item.** Recognition tasks are passed by partial knowledge, so they overstate competence and hide which concepts failed to land. Forcing unaided production is the only feedback that improves what you built rather than just ranking the user.
- **Name what the design cannot rule out.** Each-user-as-own-control kills prior knowledge, not concurrent outside learning. Say so before a critic does.

## Apply to your product

- Is there already a gate or milestone in your flow where a few questions could ride along, before and after the thing you want to prove?
- What would you dare to ask if the user never saw their score — and what does it say about your current metrics that you would not dare ask it today?
- Where in your product could one open-ended, unaided task replace three multiple-choice ones that everyone passes?

## See also

[[thin-sample-many-people-to-grade-the-curriculum]] · [[build-the-item-pool-independently-of-the-content]] · [[../duo-experimentation/references/baseline-at-first-contact]] · [[../duo-experimentation/references/quasi-experiments]]
