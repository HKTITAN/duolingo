---
name: duo-ml-in-production
description: Decide where a learned model beats a hand-written rule tree, judge it on a metric that moves where users actually care, and run a generation pipeline that does not quietly produce errors at scale — ranking noisy queues instead of filtering them, harvesting training labels from the human review step, calibrating thresholds per skill level, resolving identity before trusting any funnel number, and staging rollout as a published coverage curve. Use when replacing years of accumulated branching logic with one model, choosing an offline metric, triaging user reports, building an item bank or a content generator, or asking why your new-user numbers look wrong. Triggers on phrases like should this be a model or rules, ranking model, AUC, which metric should we optimize, cold start for a new segment, candidate generation, generated content at scale, identity resolution, gradual model rollout.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo ML in Production

How to tell when a learned model earns its keep against hand-written rules, what to judge it on, and how to run a generation pipeline that does not manufacture errors quietly.

Distilled from Duolingo's engineering and product blog, where models decide what each user sees, rank what staff look at, and produce content no team could author by hand. The reader here is building something else entirely — every node ends in questions about your product, not theirs.

**This skill does not own LLM agent orchestration.** Agent runtimes, durable workflows, graders and internal agent tooling belong to [[../duo-ai-agent-platform/SKILL]]. This one owns trained models and generation pipelines that make or produce the product.

## Model versus rules — when learning wins

- [[references/replace-the-rule-tree-with-one-learned-decision]] — years of won experiments compound into logic nobody can reason about; collapse the tree into one call, and scope v1 to need no new infrastructure.
- [[references/rank-the-noise-dont-filter-it]] — when 90% of submissions are wrong, reorder them instead of discarding them, and capture the reviewer's verdict as training data.
- [[references/shrink-the-candidate-set-instead-of-speeding-the-search]] — attack the exponent with cheap heuristics, then spend all your compute on the survivors.

## Features and cold start

- [[references/shallow-features-let-new-segments-inherit-performance]] — surface-only features let one pooled model serve every segment, so a week-old segment inherits everything the others learned.

## Evaluation — measuring the thing users feel

- [[references/pick-the-metric-sensitive-where-users-care]] — resolution is not sensitivity; a metric needing a magic number at its boundary is measuring the wrong quantity.
- [[references/calibrate-the-same-measurement-per-skill-level]] — one instrument, many calibration curves, one threshold on the calibrated output.
- [[references/surprise-requires-a-model-of-the-expected]] — you cannot detect impressive without a model of what a typical person would have done.

## Generation pipelines — producing content you cannot author

- [[references/generate-from-one-parameterized-primitive]] — find the smallest configurable object that produces the whole family, then move authoring to whoever owns the iteration loop.
- [[references/pair-every-generator-with-an-inspector]] — the generator, the inspector and the corrector are one project; funding only the first builds a machine for producing errors at scale.
- [[references/integrity-by-construction-not-secrecy]] — when every instance is assembled at request time, a leaked instance is worthless.

## Shipping and trusting the numbers

- [[references/ship-coverage-as-the-progress-metric]] — expand slice by slice on live traffic and publish coverage, paired with per-slice quality so it cannot be gamed.
- [[references/resolve-identity-before-you-trust-the-funnel]] — a fragmented join key overstates churn and acquisition at the same time, and the errors cancel in the top line.

## Where to start

- Considering replacing rules with a model — [[references/replace-the-rule-tree-with-one-learned-decision]], then [[references/pick-the-metric-sensitive-where-users-care]].
- The model works but a new segment has no data — [[references/shallow-features-let-new-segments-inherit-performance]].
- A human queue is drowning — [[references/rank-the-noise-dont-filter-it]].
- About to generate content at scale — [[references/generate-from-one-parameterized-primitive]], then [[references/pair-every-generator-with-an-inspector]].
- The numbers disagree with what you see in the product — [[references/resolve-identity-before-you-trust-the-funnel]].

## Sibling skills

- [[../duo-ai-agent-platform/SKILL]] — LLM agents as infrastructure, which is where "we want to use AI for this" usually belongs instead.
- [[../duo-experimentation/SKILL]] — proving the learned version actually beat the rules, and when to kill it.
- [[../duo-difficulty-calibration/SKILL]] — modeling item and user jointly, the sibling problem to calibrating a threshold per skill level.
- [[../duo-production-reliability/SKILL]] — treating the datasets and pipelines underneath all of this as production software.

## Sources

Distilled from blog.duolingo.com posts published 2019-12-16 to 2026-09-08 — machine-learning-ads, how-machine-learning-helps-duolingo-prioritize-course-improvements, engineering-game-review, chess-computers-vs-humans, growth-model-duolingo, developing-math, world-character-visemes, is-the-duolingo-english-test-hard, and learning-how-to-help-you-learn-introducing-birdbrain. Each node carries its own dated citation.
