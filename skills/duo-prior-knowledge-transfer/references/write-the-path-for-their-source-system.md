---
name: duo-prior-knowledge-transfer-write-the-path-for-their-source-system
summary: Build a separate onboarding path per source system, spending time where that cohort's prior model does not reach and skipping what it already covers.
metadata:
  internal: true
---

# Write the Path for Their Source System

## Concept

Once you accept that difficulty is distance from a prior model, one onboarding path stops being defensible. Two cohorts arriving from different systems need different pacing on the same material — fast through everything their prior model already covers, slow and explicit exactly where it nearly reaches but misses. The payoff is that these paths are cheap to clone: two source systems with similar structure share most of a path, so the second one is an adaptation rather than a rewrite. This is a routing decision about prior systems, not about ability. When a cohort struggles because they lack the underlying capability rather than because they carry a conflicting model, that is a difficulty-calibration problem (`duo-difficulty-calibration`), and the distinguishing symptom is blank answers rather than confident wrong ones.

## What Duolingo does

Source: blog.duolingo.com/the-nuts-and-bolts-of-course-creation-at-duolingo (Duolingo blog, 2020-06-11; accessed 2026-09-22)

- Duolingo does not ship one course per target subject. It writes each course **for the learner's source language**. English-for-Spanish-speakers moves fast through articles and conjugation, because the prior model already covers them. English-for-Chinese-speakers spends **far more time on "the"**, because Chinese has no equivalent and the prior model has nothing to transfer.
- The emphasis follows the transfer profile, not the measured level. Two learners of identical proficiency get different amounts of instruction on the same material depending on what they arrived carrying.
- Cloning is cheap where the profiles are close: the English course built for Spanish speakers was adapted for **Portuguese speakers with only a few changes**, because the transfer profile is nearly the same. The unit of reuse is the profile, not the subject.
- Tension, and it is the important one: transfer cuts both ways within a single cohort. A French speaker learning Spanish grasps grammatical gender instantly — the category transfers whole — but then *el carro* versus *la voiture* makes each individual word's gender **harder** to remember than it would be for someone with no gender system at all. The same prior that buys the concept in one step makes the instances noisier.
- So a source-specific path is not uniformly faster. It is faster on the structural level and slower on the near-miss instances, and the schedule has to reflect both.

## The transferable pattern

- **Capture the prior system at signup**, and make it a real branch rather than a survey answer nobody reads. If you do not know what people arrived from, every other move in this skill is unavailable to you.
- **Pace by transfer profile, not by level.** Compress whatever the prior model already covers; expand exactly where it nearly reaches and diverges. Same content, different time allocation.
- **Cluster source systems into profiles.** Several prior tools usually share one structural shape, so you need a handful of paths, not one per competitor. Build the first properly and adapt.
- **Do not assume a source path is uniformly easier.** Where a concept transfers whole, the instances beneath it often get *harder*, because the prior keeps supplying its own answer. Budget time there even though the cohort looks advanced.
- **Keep this separate from ability targeting.** Confident wrong answers point at a conflicting prior model and belong here. Blank answers and abandonment point at the difficulty level and belong to calibration. The fixes are opposites — one adds a contrast, the other removes a step.

## Apply to your product

- Do you know which tool each new account came from? If not, what is the cheapest place in your signup to ask, and would you branch on the answer?
- Take the top two source systems you see. Which parts of your onboarding could you cut entirely for each — and which single part deserves triple the time?
- Where does a cohort look advanced on the concept and keep getting the individual cases wrong? That is transfer succeeding at one level and interfering at the next.

## See also

[[mismatched-mappings-make-errors-structural]] · [[difficulty-is-distance-from-what-they-already-know]] · [[../duo-progression-design/SKILL]]
