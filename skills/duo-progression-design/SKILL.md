---
name: duo-progression-design
description: Decide what a product teaches, in what order, and with how much support — then design the removal of that support instead of leaving it in forever. Covers sequencing by task rather than by the subject's taxonomy, borrowing an external standard as the progression spine, scaffolding and fading on a schedule, user-removable training wheels, the crutch that exists because it makes content cheap to build, recognition-then-production ordering inside one session, ranking content by the cost of getting it wrong, frequency-first coverage with an explicitly optional tail, and picking one canonical variant out loud. Use when someone asks what order should this go in, should onboarding start with fundamentals or with a real task, what do we cut from the tutorial, when do we take the training wheels off, why do users finish onboarding and still fail the real task, or should we invent our own levels.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Progression Design — Map of Content

Most products teach something, whether or not anyone on the team calls it teaching. Onboarding, tutorials, docs, empty states, the order features unlock, the defaults that hold a novice's hand — all of it is a curriculum, usually one nobody designed. This skill covers the three decisions that make it work: **what goes in, in what order, and with how much support** — plus the decision teams skip, which is how the support comes off.

Duolingo is the case study because it has published unusually candid accounts of these choices, including the A/B results that cut against its own preferences. Your product is the target. Nothing here is about language learning.

**Boundary.** This skill owns where a thing sits in the path and what scaffolding surrounds it. Whether a rule gets stated at all, and in what compressed form, belongs to the rules-and-heuristics skill — sequencing and explaining get conflated constantly, so keep them apart.

Scan the descriptions and follow only the `[[wikilinks]]` you need.

## What goes in, and in what order

- [[references/sequence-by-task-not-by-taxonomy]] — the expert's structural order is the wrong first order; teach each primitive at the moment a real task needs it.
- [[references/rank-what-you-teach-by-cost-of-getting-it-wrong]] — sort by consequence, not completeness, and publish the list of errors that are safe to keep.
- [[references/sequence-by-frequency-and-declare-the-tail-optional]] — derive the head from a real corpus, then tell users out loud that the tail is optional.
- [[references/borrow-an-external-standard-as-the-spine]] — invented levels are unfalsifiable; a borrowed standard gives you a bar you cannot quietly move.
- [[references/front-load-the-context-a-later-rule-will-need]] — plant cheap material early so a hard concept can be induced from examples rather than asserted.

## Support, and how it comes off

- [[references/scaffold-and-fade-on-a-schedule]] — support starts high and decays on a schedule you wrote before shipping; the fade is the design.
- [[references/make-the-scaffold-removable-by-the-user]] — a visible off switch beats a guessed threshold, and many users will never flip it.
- [[references/the-crutch-that-makes-you-cheap-to-build]] — the scaffold that makes content cheap to author is often the one preventing the skill from forming.

## Practice that actually transfers

- [[references/recognition-then-guided-then-production]] — pick, then copy a worked example, then produce unaided, all inside one session.
- [[references/do-the-real-thing-badly-on-day-one]] — put the crude version of the target behaviour in the first session; the one real exception is perception before production.
- [[references/train-the-shared-bottleneck-where-it-is-cheapest]] — when two skills stall on the same resource, drill it in whichever context costs least.

## Honesty about coverage

- [[references/pick-one-variant-and-name-the-choice]] — teach one default, accept the alternatives as correct, and say that you chose.
- [[references/structured-coverage-catches-what-use-never-surfaces]] — usage is distributed by frequency, so a gap presents as the absence of an experience.

## Sibling skills

- [[../duo-gamification/SKILL]] — progression that is *felt*: XP, levels, difficulty ramps. This skill decides the content of each stage; that one decides how reaching it feels.
- [[../duo-product/SKILL]] — ruthless prioritization and raising the bar, applied to the product rather than to the path through it.
- [[../duo-experimentation/SKILL]] — every ordering claim here is testable, and Duolingo's own A/B data contradicts one of them.
- [[../duo-retention/SKILL]] — a curriculum nobody returns to teaches nothing; the habit loop is the precondition for all of this.

## Sources

Thirty-four posts from blog.duolingo.com (crawled 2026-09-22), covering course construction, CEFR alignment, scaffolding and exercise design, pronunciation and grammar prioritization, dialect and variant choices, and the Math and Chess courses. Each node carries its own dated citations.
