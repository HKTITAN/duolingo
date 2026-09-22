---
name: duo-difficulty-calibration
description: Put each user at the edge of what they can currently do — estimate item difficulty and user ability in one model, target a band rather than a floor, and use live signals to tell whether the model is honest. Covers joint item-user modelling, the familiar-to-new ratio, error rate read against completion rate, the roughly-half success check, fitted difficulty weights as a content brief, why users grind mastered material, opt-in hard modes priced higher, user-picked difficulty rungs, tail escalation, and training above real load. Use when asked how hard the next thing should be, what error rate means it is working, whether an adaptive system is calibrated, how much new versus familiar material, whether users should pick their own level or the system should infer it, or when an accuracy drop is actually progress. If the screen asks too much at once, use the attention-budget skill instead.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Difficulty Calibration — Map of Content

Most products pick a difficulty once, in a room, for an average user who does not exist. This skill owns the alternative — **putting each user at the edge of what they can currently do**, and knowing whether you actually are.

Three ideas run through everything below. Difficulty is a property of the **pairing** of item and user, not of the item. The target is a **band** with an upper bound, not a floor. And the user's own satisfaction signal points the wrong way, because comfortable repetition feels excellent and teaches nothing.

This skill does **not** own whether a single screen is asking too much at once. "This is too hard" arrives here by default, but an item can be perfectly targeted to the user's ability and still fail because five things compete for attention simultaneously — that is [[../duo-attention-budget/SKILL]].

This skill is a **graph**: scan the descriptions, follow only the `[[wikilinks]]` you need.

## Building the model

- [[references/model-the-item-and-the-user-jointly]] — estimate content difficulty and user ability in one system, because difficulty is a property of the pair and half the signal is useless alone.
- [[references/read-your-difficulty-weights-as-a-content-brief]] — the fitted per-item parameters separate hard-because-unfamiliar from hard-because-structural, which is a redesign queue, not just a scheduling input.

## Choosing the target

- [[references/the-narrow-band-between-bored-and-lost]] — specify an interval, not a threshold; control the familiar-to-new ratio rather than session volume.
- [[references/train-above-the-real-load]] — behavior attenuates under real conditions, so practice at exactly the target level lands below it. Over-constrain on purpose, and pay for it knowingly.

## Knowing whether it works

- [[references/fifty-percent-success-is-the-honest-signal]] — observed success rate is a free, label-free, continuous audit of any adaptive system. A little above half means the model is honest.
- [[references/read-error-rate-with-completion-rate]] — errors up with completion flat is productive difficulty; errors up with completion down is a defect. The error metric alone cannot tell them apart.

## Letting the user in

- [[references/let-users-pick-the-rung]] — a few orthogonal dials, crossed into named and explicitly rated combinations, beat both a slider and a silent guess.
- [[references/opt-in-hard-mode-priced-higher]] — ship the unassisted version as a toggle on a task they already know, and pay it several times more than the scaffolded one.

## Working against the grain

- [[references/users-will-grind-what-they-already-know]] — repetition of mastered material wins on every short-horizon metric and produces nothing. The product has to push the other way.
- [[references/escalate-at-the-tail-not-the-start]] — decide difficulty late, on evidence from this sitting, where you are better informed and the downside is bounded.

## Sibling skills

- [[../duo-attention-budget/SKILL]] — whether the screen asks too much at once. The other half of "this is too hard," and the first thing to rule out.
- [[../duo-memory-and-decay/SKILL]] — *when* to bring something back, as opposed to *how hard* to make it. Different model, adjacent decision.
- [[../duo-progression-design/SKILL]] — the order things are taught in and how scaffolds get removed over time, which sets the ability curve this skill targets against.
- [[../duo-learner-motivation/SKILL]] — whether the user is willing to attempt the hard thing at all, which no amount of correct targeting fixes.

## Sources

All claims trace to dated posts on `blog.duolingo.com`, cited inline in each node's `## What Duolingo does` section; slugs are verified against `scripts/sources.json`.
