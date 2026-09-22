---
name: duo-ml-in-production-rank-the-noise-dont-filter-it
summary: When most user-submitted reports are wrong, rank them instead of filtering — and instrument the human review step so it emits training labels for free.
metadata:
  internal: true
---

# Rank the Noise, Do Not Filter It

## Concept

When a feedback channel is open to everyone, most of what arrives is wrong. The instinct is to build a classifier that throws the wrong ones away. That instinct is backwards: a filter tuned to remove the bulk of the noise will also remove some of the small fraction carrying all the value, and a missed genuine defect costs far more than a reviewer spending three seconds on a bad report.

Ranking keeps everything and reorders it. Recall stays complete by construction, while the reviewer recovers nearly all the throughput a filter would have bought, because the items that matter are now at the top of the queue. Filter versus rank is a choice about which of your two errors you are willing to make permanent and invisible.

## What Duolingo does

Source: blog.duolingo.com/how-machine-learning-helps-duolingo-prioritize-course-improvements (Duolingo blog, 2019-12-16; accessed 2026-09-22)

- Learners submit "Report" flags when an answer they believe is correct gets rejected. **Roughly 10% are correct and need a fix; roughly 90% contain a mistake by the reporter.**
- Rather than filtering, Duolingo shipped a **logistic-regression ranking model** in early 2019 that surfaces the likely-correct reports first for the staff and contributors reviewing in the Incubator.
- The volume is structural, not a process failure: the average translation exercise has **more than 200 acceptable answers**, some long sentences have **up to 30,000**, and one German sentence accumulated **72 accepted translations**. No authoring process enumerates that up front.
- They chose **area under the ROC curve** explicitly because "the system is used to rank reports for human review" — ordering is what the consumer of the output actually experiences, so accuracy at a threshold would have been a vanity number.
- The reviewer's verdict is captured and fed straight back as training data — **both accepted and rejected** decisions — so the label set grows with usage instead of with annotation budget.

## The transferable pattern

Three rules, in rough order of how often they are violated:

1. **Rank, do not filter, whenever a human sits downstream.** A filter converts a recall loss into a silent permanent one, because nobody ever sees what was dropped. A ranking preserves the option to keep reading down the list on a slow day, and makes the cost of being wrong one wasted glance.
2. **Pick the metric that matches how the output is consumed.** If the output is an ordered queue, judge ordering. If it is an automated cutoff, judge precision at that cutoff. Reporting classification accuracy for a ranking system measures something nobody uses.
3. **Instrument the human decision step.** The reviewer already has to decide accept or reject to do the job at all. Capturing that decision costs one event write and yields labels proportional to traffic. A training set that grows with usage compounds; one that grows with annotation spend does not.

The negatives matter as much as the positives. A label set containing only accepted items teaches the model what good looks like and nothing about what bad looks like, and it will rank confidently wrong.

## Apply to your product

- Where does a human triage a noisy queue in your product, and is a machine currently deciding what they never see?
- What fraction of that queue is actually actionable, and what does one false negative cost you compared to one wasted glance?
- Does your review interface write the reviewer's verdict anywhere a training job could read it, or does it only mutate the record and move on?

## See also

[[shallow-features-let-new-segments-inherit-performance]] · [[pick-the-metric-sensitive-where-users-care]] · [[../duo-ai-agent-platform/references/verification-becomes-the-bottleneck]]
