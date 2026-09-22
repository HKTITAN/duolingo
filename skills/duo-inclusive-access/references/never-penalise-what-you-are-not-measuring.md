---
name: duo-inclusive-access-never-penalise-what-you-are-not-measuring
summary: Penalising a motor slip or a near-miss punishes the wrong thing and corrupts your own data; when the grader compares the wrong property, change the representation, not the threshold.
metadata:
  internal: true
---

# Never Penalise What You Are Not Measuring

## Concept

A penalty is a claim. It says *you failed at the thing this product is about*. When the penalty lands on a mistyped character, a fumbled tap, or a near-miss on something adjacent to the real competence, the claim is false twice over: it punishes the user for something you never set out to build in them, and it writes a failure into your own records at a moment when the underlying knowledge was demonstrably present. You have degraded the experience and your measurement in one move.

There is a stronger version of this when the penalty comes from an automated grader. If the grader is comparing the wrong *property*, no amount of threshold tuning fixes it — a threshold only trades false positives against false negatives along an axis that was already wrong. Changing what you compare removes the entire error class instead of rebalancing it.

## What Duolingo does

Source: blog.duolingo.com/improving-how-duolingo-teaches-chinese-and-other-languages (Duolingo blog, 2020-02-03; accessed 2026-09-22)

- Chinese has many character homophones, so off-the-shelf speech recognition would transcribe a perfectly pronounced answer into the **wrong character** — 他, 她 and 它 are all *tā* — and the exercise would mark it wrong. The learner's pronunciation, the thing actually being assessed, had been correct.
- Duolingo's fix was not a looser text-match threshold. Speaking-exercise grading was switched from **text match to phonetic match**, comparing sounds instead of characters, and the same fix was then applied to Korean. The error class disappeared rather than shrinking.

Source: blog.duolingo.com/product-highlights (Duolingo blog, 2025-12-10; accessed 2026-09-22)

- In **2025** Duolingo made tap exercises more forgiving so learners can correct small mistakes without penalty — a motor slip stops being recorded as a knowledge failure.

## The transferable pattern

Separate two questions that teams habitually merge: *did the user get it wrong* and *did the user fail at the thing we care about*. Every penalty in your product should be traceable to the second. Typos, mis-taps, formatting, ordering, casing, a near-miss on a field you were not evaluating — these are noise, and charging for them corrupts whatever signal you were collecting.

When something automated is issuing the penalty, interrogate the comparison before you touch the tolerance. Ask what property the comparison is actually sensitive to, and whether that is the property you meant. If it is not, changing the representation you compare on — a different encoding, a different normalisation, a different feature entirely — eliminates the failure mode. Tuning the threshold just moves the victims from one group to another.

## Apply to your product

- Walk your scoring, gating or rejection logic. For each penalty, name the competence it is claiming the user lacks. Any you cannot name is a bug.
- Where does your product punish a slip the user would instantly fix if you let them? What would it cost to let them?
- Is any automated check comparing a proxy for the thing you care about? What would you compare instead, and would that remove the error class rather than shrink it?

## See also

[[strip-every-demand-you-are-not-measuring]] · [[audit-fairness-against-the-delivery-context]] · [[../duo-experimentation/SKILL]]
