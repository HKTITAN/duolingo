---
name: duo-perceived-progress
description: Make effort feel like it is going somewhere — pick the granularity of your progress number, size the unit of work that ends in a completion event, set an honest timeline, and decide what to say when a user stalls because they succeeded. Covers shipping a fine-grained scalar alongside a coarse tier, anchoring one portable number to an external standard and writing it in can-do terms, publishing the real timeline with a ladder users can locate themselves on, milestones weeks out rather than months, shortening the unit of completion, naming the capability gained at the end, and putting maintenance work on the forward path. Use when progress feels flat, when users quit in the middle, or for questions like should I show a tier or a score, how often does the number need to move, why do users skip review, or what should I promise about how long this takes.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Perceived Progress

Users do not abandon a product because the work got hard. They abandon it because the work stopped visibly counting. Perceived progress is a separate design surface from actual progress, and it has its own failure modes — a number too coarse to move, a promise too optimistic to keep, a unit too long to finish, a valuable action that looks like going backwards.

Four decisions make up most of it. How granular the number is, how long the unit of work is, what you promise about the timeline, and what you say at the boundary between units. A fifth question arrives later, when a user plateaus because they reached good-enough and the feedback that drove them disappeared.

This skill does not cover the streak or any consecutive-day counter — a chain breaks and a measure moves, and they fail for different reasons. That is [[../duo-streak-mechanics/SKILL]]. It also does not cover diagnosing which users are motivated and why, which is [[../duo-learner-motivation/SKILL]].

## The number

- [[references/rate-of-change-beats-absolute-position]] — motivation tracks the delta, not the position; ship a granular scalar with a visible next increment next to the coarse tier, not instead of it.
- [[references/a-portable-number-in-can-do-terms]] — one scalar anchored to an external standard and written as what the holder can now do, exportable to somewhere it has social value; plus what to say when it keeps rising through a flat stretch.

## The promise

- [[references/publish-the-honest-timeline-and-a-ladder]] — an inflated timeline becomes a deadline you miss and the user blames themselves for; publish the real one with a ladder, and stop defining success as the top of it.
- [[references/milestones-in-weeks-not-months]] — a goal nobody can score converts every real gain into evidence of falling short; set the next target weeks out and specific enough to observe daily.

## The unit

- [[references/shorten-the-unit-of-completion]] — halving a unit roughly doubles the rate of completion events at no content cost, and shortens the window in which a user can decide this is going nowhere.
- [[references/name-the-capability-gained-at-the-end]] — say what they can now do, or they will optimise for the progress they can see over the outcome they came for; plus serving advanced users through a side channel instead of a higher floor.

## The work that looks like going backwards

- [[references/put-maintenance-on-the-forward-path]] — if upkeep requires visible regression, users skip it; interleave it into the forward track and label it progress, and know what diagnostic signal you lose by doing so.

## How to use this skill

1. Start with granularity. Open your product as a mid-tenure user and find the longest stretch where nothing on screen changes.
2. Then check the unit length. Time-to-first-completion and the median gap between completions are the two numbers that set your reinforcement rate.
3. Then audit the promise — what your marketing implies about time-to-value against what your cohort data says.
4. Then fix the boundary copy, which is the cheapest change here and usually the most neglected.
5. Last, look for the high-value action your layout renders as a step backwards.

## Sibling skills

- [[../duo-streak-mechanics/SKILL]] — the consecutive-day chain, its trivial bar, its slack and what it quietly certifies; the counter that breaks rather than moves.
- [[../duo-learner-motivation/SKILL]] — why users set goals they cannot keep, how to frame a stretch target, and what to say before something gets hard.
- [[../duo-progression-design/SKILL]] — the sequence underneath the progress bar, including borrowing an external standard as the spine of a curriculum.
- [[../duo-gamification/SKILL]] — points, celebration moments, nested deadlines and the grind guardrails that keep a completion event meaningful.

## Sources

Every node cites blog.duolingo.com posts in the dated form; the primary ones here are `duolingo-score` (2024-10-23), `what-does-duolingo-score-60-mean` (2026-03-05), `can-you-learn-a-language-in-6-months` (2026-08-18), `intermediate-mini-units` (2026-03-04), `intermediate-plateau` (2024-02-27), `duolingo-difficult-exercises` (2021-09-24), `new-duolingo-home-screen-design` (2022-05-06), `sticking-with-it-tips-for-staying-motivated` (2026-06-04), `critical-period-learning` (2026-04-14), `language-learning-myths` (2023-03-23), `ukrainian-learner-stories` (2022-11-11), `whats-the-easiest-language-to-learn` (2026-08-20), `product-highlights` (2025-12-10) and `duos-film-club-podcast` (2024-01-09), all accessed 2026-09-22.
