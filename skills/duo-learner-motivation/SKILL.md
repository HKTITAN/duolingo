---
name: duo-learner-motivation
description: Keep people attempting a skill they believe they are bad at — by lowering what it costs to be visibly wrong, replacing unscoreable goals with ones they can hit, pre-announcing how bad early progress will feel, and supplying the attribution that turns a failure into information instead of a verdict. Use when users churn in week two saying they are "not good at this", when nobody will try the scary core action, when a promise like "fluent" or "proficient" or "mastery" gives users no win to register, when hard content reads as a test rather than a puzzle, or when you need words for a plateau. Triggers on "users say they're bad at it", "week two churn", "they won't try the main feature", "how do I set a goal that doesn't demoralize", "onboarding feels like a test", "what do I say when progress slows", "should I tell users they don't need all of it".
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# duo-learner-motivation

Why users stop attempting, and what to change so they start again.

This skill owns the **frame, the stakes and the attribution around failing** — the things that decide whether a correctly-targeted difficulty is tolerated or fatal. It does not own the difficulty target itself. If your content is genuinely mis-calibrated, no amount of reframing rescues it; fix the calibration and come back.

Most of what follows is copy, defaults and ordering rather than new features. That is the point — the cheapest interventions in this set are sentences.

## Diagnose first

Before picking a fix, work out which input is missing and whether the block is emotional or structural.

- [[references/exposure-and-need-are-both-required]] — skill is exposure × need; either at zero makes the result zero, so more content never rescues an unmotivated user.
- [[references/anxiety-spends-the-same-budget-as-the-task]] — anxiety eats the working memory the task needs, so nervous users score below their real ability and then believe the score.
- [[references/the-blocker-is-willingness-to-be-visibly-bad]] — "I can't do this" is usually avoidance wearing a capacity story; build cheaper failure, not better explanation.

## Make the goal scorable

An unmeasurable promise makes every state the user occupies a state of failure.

- [[references/decompose-a-goal-nobody-can-score]] — split the untestable binary into components and can-do bands, and tell users where they may stop.
- [[references/flag-the-stretch-goal-as-a-stretch]] — marking the ambitious outcome in advance keeps its pull and deletes its failure.
- [[references/set-success-at-functional-adequacy]] — define success as "it worked", not "it was correct", and sanction the degraded path by name.

## Unblock the attempt

The scary core action is the one that decides whether anything else in your product matters.

- [[references/declassify-the-perceived-prerequisite]] — find the one capability users think disqualifies them and rule it non-blocking in a sentence.
- [[references/lower-the-cost-of-the-first-public-attempt]] — pre-exposure, filler to buy thinking time, and an undo written from inside the changed state.
- [[references/ship-an-easier-variant-for-people-who-failed-before]] — a completable low-exception version so a returner can accumulate evidence against their own verdict.

## Frame the difficulty and the failure

Same effort, opposite meaning, depending on what you said beforehand and what you say when it goes wrong.

- [[references/pre-announce-how-bad-it-will-feel]] — specific, unflattering expectations set before the first attempt turn a bad week into confirmation they are on track.
- [[references/attribution-decides-whether-they-continue]] — ship the mechanism with the correction; an unexplained failure becomes evidence about the user.
- [[references/reframe-the-difficulty-rather-than-removing-it]] — a puzzle frame makes the user the agent; an evaluation frame makes them the subject. Check the frame before you sand anything down.
- [[references/suppress-the-noise-so-the-blocking-error-is-audible]] — rank errors by whether they block the goal, and tell users out loud what they may skip.

## Sibling skills

- [[../duo-retention/SKILL]] — once they are attempting, what brings them back tomorrow. Churn diagnosis starts there and routes here when the cause is "I'm bad at this".
- [[../duo-gamification/SKILL]] — XP, progression and the difficulty ramp itself. This skill frames the difficulty; that one sets it.
- [[../duo-voice/SKILL]] — the actual wording for error copy, onboarding and celebration. Most fixes here land as copy changes there.
- [[../duo-experimentation/SKILL]] — how to test whether a reframe moved anything, and which guardrail catches it if the reframe cost you accuracy.

## Sources

Distilled from blog.duolingo.com — 32 posts spanning 2020-02-27 to 2026-05-06, each cited in dated form inside the node that uses it; see `scripts/sources.json` for the full bibliography.
