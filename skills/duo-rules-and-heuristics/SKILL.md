---
name: duo-rules-and-heuristics
description: Decide whether to explain something at all, when the explanation should land, and how to compress a rule into something a user can actually execute under pressure. Use when you are writing docs, tooltips, onboarding copy, error messages, a runbook or a training guide and are not sure anyone will absorb it. Triggers on phrases like should we document this or let people figure it out, nobody reads our docs, users keep making the same mistake, how do I explain this simply, our error messages do not help, turn this table into something usable, ship a rule of thumb, is it OK that the shortcut is only 90 percent right, how do I know if they actually learned it, our expert cannot explain what they do, write the spec from how the team actually works.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Rules and Heuristics

Most documentation fails for a reason that has nothing to do with how it is written. It loads the wrong memory system, arrives before the user has anything to attach it to, or states a rule that is correct but too slow to run at the moment of decision. This skill covers the three decisions underneath that: **whether to explain at all**, **when the explanation lands**, and **what shape a rule has to be in** to survive contact with a user under pressure.

It does not cover the order or scaffolding of the path a rule sits in, and it does not cover anchoring a new concept to a system the user already brings from somewhere else — that is transfer. This skill owns the representations you invent to teach with.

## Whether to explain at all

- [[references/two-memory-systems-explanation-loads-the-wrong-one]] — knowing a rule and being able to run it are stored separately; documentation only builds the first, and the measurement rule that follows.
- [[references/let-them-induce-it-from-volume-then-confirm]] — a stuck user is usually an exposure problem, not a wording problem; supply instances, let them form a theory, confirm it afterwards.
- [[references/where-explicit-instruction-earns-its-place]] — explanation earns its keep only for what exposure will never make salient; its job is attention-direction, not transmission.
- [[references/mistakes-are-the-signal-not-the-defect]] — error is the mechanism, and any task passable by a plausibility shortcut trains only the shortcut.

## When it lands

- [[references/explanation-lands-at-the-moment-of-the-error]] — the same text is inert before the mistake and sticky right after it; name the rule that fired, not just the verdict.
- [[references/make-the-invisible-error-observable]] — users cannot correct what they cannot perceive; instrument the signal, then rank the review and name one focus.

## Shaping the rule

- [[references/ship-the-shortcut-with-its-coverage-rate]] — lead with the heuristic, state its hit rate, quarantine the real mechanism behind an opt-in header.
- [[references/turn-the-table-into-a-procedure]] — convert an N-entry lookup into an ordered question sequence with worked traces, and mark the required minimum.
- [[references/give-them-a-handle-they-can-hold-under-pressure]] — acronyms, surface cues, named patterns and bundled chunks, because the failure is retrieval, not understanding.
- [[references/fix-the-model-instead-of-memorising-the-exception]] — a recurring exception is a bug report about your model; reframe so the right answer becomes the intuitive one.
- [[references/name-the-arbitrary-and-kill-the-folk-theory]] — label what is genuinely arbitrary, and falsify the story users have already invented to explain it.
- [[references/a-second-representation-does-what-more-practice-cannot]] — when the notation is causing the errors, more reps inside it make the confusion fluent.

## Getting the rule out of people's heads

- [[references/the-practitioner-cannot-state-their-own-rule]] — expertise compiles out of conscious reach, so extract rules from observed behaviour and check them, never from self-report.

## Sibling skills

- [[../duo-experimentation/SKILL]] — once you have a rule, how to measure whether it changed anything.
- [[../duo-voice/SKILL]] — the wording of the error message this skill tells you where to put.
- [[../duo-product/SKILL]] — whether the thing you are about to explain should exist at all.

## Sources

Distilled from 49 extracted claims across posts on blog.duolingo.com, each node carrying its own dated citation; the pack's full bibliography lives in `scripts/sources.json`.
