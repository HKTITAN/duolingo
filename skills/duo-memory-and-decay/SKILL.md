---
name: duo-memory-and-decay
description: Decide when to bring something back in front of a user, and treat every capability they have as quietly rotting rather than banked. Covers spacing versus massing at equal cost, per-item half-life scheduling instead of fixed interval ladders, retrieval versus re-exposure, delayed retries, error-driven practice queues, graded decay, reactivating lapsed users without resetting them to zero, visible decay states on completed things, sleep consolidation, context variability, and making forward motion do the reviewing. Use when asked how long until users forget this, when to resurface an item, why a re-test passes while real retention does not, how to win back a lapsed user, why a completed badge goes stale, or how to design a review or practice mode. Difficulty targeting and ability estimation are a different model and belong to the difficulty-calibration skill.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Memory and Decay — Map of Content

Most products model capability as something a user banks: they completed it, so they have it. They do not have it. From the moment of acquisition it is decaying, on a curve that differs per item and per person, and a product whose value depends on retained capability needs a maintenance loop rather than only an acquisition funnel.

This skill owns one decision: **when to bring something back in front of a user.** It does not own how hard the next item should be for that user — choosing *when* an item returns and choosing *how hard* to make it are different models, and difficulty belongs to the difficulty-calibration skill.

This skill is a **graph**: scan the descriptions, follow only the `[[wikilinks]]` you need.

## How memory actually behaves

- [[references/spacing-beats-massing-at-equal-cost]] — the same repetitions spread across days survive; massed into one sitting they buy a passing score and nothing else. Frequency is the parameter, not length.
- [[references/sleep-is-a-free-consolidation-pass-you-can-skip]] — traces migrate to long-term storage overnight, so a one-block schedule deletes passes the user's brain would have run for free.
- [[references/decay-is-graded-and-fine-grain-goes-first]] — specifics rot fast, structure is durable, recognition outlives production. Decay is a shape, not a switch.

## Scheduling: what comes back, and when

- [[references/per-item-half-life-not-a-fixed-ladder]] — fit a decay model to your own logs and schedule where lag approximates half-life, instead of walking a ladder someone picked in a meeting.
- [[references/delay-the-retry-and-weight-the-queue]] — an immediately re-served item is answered from working memory; hold the retry, and order the queue on recency *and* error.
- [[references/own-errors-are-the-highest-value-practice-set]] — a session built from this person's recorded failures spends every slot at their frontier; a population-average set wastes most of them.
- [[references/make-forward-motion-do-the-reviewing]] — if step N+1 structurally requires step N, retrieval happens as a side effect of the thing the user already wants to do.

## Designing the practice itself

- [[references/retrieval-not-re-exposure]] — review that shows the answer strengthens recognition; review that makes the user produce it cold strengthens what real use requires.
- [[references/three-conditions-for-practice-to-pay]] — target the unmastered, require active retrieval, return feedback immediately. Drop one and you are burning the user's time.
- [[references/vary-the-encoding-context]] — vary the surfaces, voices and settings aggressively, or the capability binds to the one context you trained it in.

## Maintenance, lapse and comeback

- [[references/give-mastered-things-a-visible-decay-state]] — a permanently-complete badge is a lie; render the decay on the object so the review request lives in the map instead of a notification.
- [[references/what-protects-a-skill-through-a-lapse]] — depth reached before the gap, a real reason to use it, a community and positive feeling predict survival. Hours logged does not.
- [[references/reactivate-dont-restart]] — forgotten capability is inaccessible, not destroyed. Probe for the residue; never hand a returner the beginner flow.

## Sibling skills

- [[../duo-retention/SKILL]] — habit loops, streaks and churn diagnostics: how users come back at all, before this skill decides what to show them.
- [[../duo-gamification/SKILL]] — progression, XP and anti-grind: the systems most likely to quietly delete your maintenance loop in a redesign.
- [[../duo-experimentation/SKILL]] — how to run the test that spacing will initially appear to fail.
- [[../duo-product/SKILL]] — taking the long view, which is the only frame in which a decay model is worth funding.

## Sources

All claims trace to dated posts on `blog.duolingo.com`, cited inline in each node's `## What Duolingo does` section; slugs are verified against `scripts/sources.json`.
