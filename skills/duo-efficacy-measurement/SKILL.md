---
name: duo-efficacy-measurement
description: Prove your product actually works — with instruments you did not author, on axes that do not substitute for each other, and in a way a skeptic outside your company can check. Covers the four-axis efficacy framework (enjoyment, mastery, real-task application, external standard), borrowing the incumbent's benchmark instead of inventing a metric, authoring an item pool independently of the content you ship, thin-sampling many users to grade your content rather than your users, embedding a pre-test and post-test as a gate, adaptive assessment, partial-credit scoring, and reading calibration off the score distribution. Use when asking how do I show this actually teaches anything, what do I measure besides engagement, should I build my own test or borrow one, how many questions do I need, where does a pre-test go, why is my assessment too easy, or should I report one score.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Efficacy Measurement

Engagement is the metric that arrives free in your event stream, which is why most products prove only that people came back. This skill is about the other three quarters of the claim — did they learn it, can they use it, and does anyone outside your company agree — plus the instrument design that makes those answers survive contact with a skeptic.

The organizing idea: a number you can move at will cannot support a claim about the world. Every node here is a way to hand part of the grading to something you do not control — an external standard, an independently authored item pool, your own population in aggregate, the shape of a distribution.

## Decide what to measure

- [[references/four-axes-that-do-not-substitute]] — enjoyment, mastery, real-task application and external standard are four independent questions, each needing its own method; and none of them is one number.
- [[references/borrow-the-instrument-you-do-not-control]] — run your users through the incumbent's own test, compare against a published study of the incumbent's users, and report the axis where you lose.

## Design the instrument

- [[references/build-the-item-pool-independently-of-the-content]] — questions drawn from the material you shipped measure exposure; an independently authored pool is your holdout set.
- [[references/embed-a-pre-test-and-post-test-in-the-product]] — put the measurement in the path as a gate, ask about the next segment before you teach it, and keep the scores private.
- [[references/thin-sample-many-people-to-grade-the-curriculum]] — a handful of questions per person, aggregated across everyone, grades your content instead of your users and hands you a ranked build list.

## Score it well

- [[references/adaptive-is-shorter-not-easier]] — selecting each item near the running estimate makes every answer informative, so the same standard is reached in far fewer items.
- [[references/partial-credit-beats-binary-scoring]] — binary grading discards the gradations that separate adjacent ability levels, and the symptom is a person who retests far from where they landed before.
- [[references/check-the-distribution-not-the-score]] — calibration is read off the shape of the curve; a ceiling means the instrument stopped separating people exactly where the decisions get made.

## Where the boundary sits

Choosing the next item for a live person in a session — targeting the band between bored and lost, modelling item and user jointly — belongs to [[../duo-difficulty-calibration/SKILL]]. Adaptive machinery appears in both. The split is what the output is for: a score, or evidence about the product, routes here; a session assembled for one individual routes there.

## Sibling skills

- [[../duo-experimentation/SKILL]] — designing the test that tells you whether a change worked, and the ladder of evidence behind it.
- [[../duo-difficulty-calibration/SKILL]] — picking the right next item for a specific person, rather than scoring the product.
- [[../duo-product/SKILL]] — what to do with an efficacy result once you have one, and how it disciplines the roadmap.
- [[../duo-learner-motivation/SKILL]] — why people stay engaged at all, which is the axis efficacy measurement cannot substitute for.

## Sources

Drawn from blog.duolingo.com — efficacy research framework, published proficiency studies, checkpoint and learning quizzes, the placement test, and the Duolingo English Test. Every node carries its own dated citation.
