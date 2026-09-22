---
name: duo-prior-knowledge-transfer
description: Work with the mental model your users already carry from a prior system — where it transfers free, where it fires a confident wrong answer, and how to redirect it instead of fighting it. Use when users keep doing things the old way after a migration or redesign, when switchers from a near-identical competitor struggle more than blank-slate signups, when two features keep getting mixed up, when onboarding is trivial for one segment and brutal for another, or when you need to teach something that looks like a familiar thing but behaves differently. Triggers on phrases like they came from the other tool and expect it to work that way, muscle memory, old habits, these two settings get confused constantly, false friends, near-miss, interference, mental model mismatch, confident wrong answers, migration onboarding, competitor switchers, why is this group so much faster.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Prior Knowledge and Transfer — Map of Content

Nobody arrives empty. Every user brings a complete, automatic model from whatever they used before, and that model runs first, by default, beneath conscious control. It is why some parts of your product are free for one cohort, why the near-misses are your most expensive errors, and why confusion clusters exactly where two things are almost the same.

This skill is a **graph**. Scan the lines below and follow only the `[[wikilinks]]` you need — don't read all eleven nodes up front.

**Boundary.** "It's too hard for this segment" lands here when the cause is the segment's prior system, and with `duo-difficulty-calibration` when the cause is their ability level. The distinguishing symptom is confident wrong answers rather than blank ones.

## Start here — the shape of the problem

- [[references/difficulty-is-distance-from-what-they-already-know]] — difficulty is a relation between your product and each user's existing model, uneven across axes; stop shipping one rating.
- [[references/the-old-model-is-suppressed-not-erased]] — a redesign never deletes a habit, it inhibits it; budget the switch cost and expect regression under load.
- [[references/interference-clusters-among-near-neighbours]] — confusion concentrates between things that are almost the same, and false friends produce confident errors with no detection signal.

## Diagnosing the errors you are already seeing

- [[references/mismatched-mappings-make-errors-structural]] — when your model splits what theirs merged, the errors are in the mapping; cluster reports by source system and say the mistakes are expected.
- [[references/write-the-path-for-their-source-system]] — pace onboarding by transfer profile rather than by level, and clone paths across structurally similar sources.

## Using the prior instead of fighting it

- [[references/hand-them-the-mapping-rule-and-the-prior-becomes-a-predictor]] — state the correspondence rule and the old model starts generating correct guesses about things they've never opened.
- [[references/anchor-to-a-reflex-they-already-execute]] — map a new distinction onto a reaction they already perform, or onto the vestigial version they already operate.
- [[references/analogy-plus-its-exception-clause]] — an analogy must map the whole contrast and name itself as breakable, or it hardens into a superstition.

## Teaching the difference between two confusable things

- [[references/train-the-contrast-not-the-items]] — side by side, everything else held constant, and show what the wrong choice actually does rather than labelling it wrong.
- [[references/breadth-of-variation-beats-depth-in-the-standard-case]] — robustness comes from exposure to the real distribution; the expert in the clean case is worst at the variant.
- [[references/separate-the-contexts-when-the-risk-is-confusion]] — when two near-identical tracks run in parallel, give each its own context and refuse symmetric effort.

## Sibling skills

- [[../duo-progression-design/SKILL]] — what order to teach things in once you know what each cohort already has.
- [[../duo-memory-and-decay/SKILL]] — the other reason users get it wrong today: they knew it and it faded, rather than importing a conflicting model.
- [[../duo-voice/SKILL]] — how to word a correction so a structural error doesn't read as a verdict on the user.
- [[../duo-experimentation/SKILL]] — how to measure whether a contrast set or a source-specific path actually moved the error rate.

## Sources

blog.duolingo.com — course creation by source language, first-language transfer, the bilingual brain and switch costs, minimal-pair pronunciation lessons, Explain My Answer, prepositions across six languages, and the hardest/easiest-language posts. Every node carries its own dated citation.
