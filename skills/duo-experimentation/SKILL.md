---
name: duo-experimentation
description: Duolingo-style experimentation as a decision protocol — hundreds of A/B tests a week, opinions resolved by data, ideas killed quickly. Covers hypothesis design, metric selection, guardrails, sample size, novelty effects, and explicit kill criteria. Use when the user wants to run an A/B test, decide between two designs without arguing, set up an experiment program, debug why a test isn't moving, or build a culture where "show don't tell" replaces seniority-based decisions. Source the Duolingo Handbook (Show Don't Tell) and engineering blog posts.
license: MIT
metadata:
  author: HKTITAN
  version: "1.0.0"
  graph: true
---

# Duolingo Experimentation — Map of Content

Duolingo runs hundreds of experiments per week and treats the result as the decision, not as one input. The handbook calls this *Show Don't Tell*: when people disagree, the experiment is the answer, not the more senior person's intuition. This skill packages that protocol.

This skill is structured as a **graph**: scan the descriptions below, follow only the `[[wikilinks]]` you need.

## The protocol

- [[references/show-dont-tell]] — the principle: metrics decide, not titles.
- [[references/hypothesis-design]] — what makes a testable hypothesis vs. a wish.
- [[references/ab-test-structure]] — variant/control, randomization unit, exposure rules.

## Metrics

- [[references/metric-selection]] — picking a primary metric that actually maps to long-term retention, not the easiest-to-move one.
- [[references/guardrail-metrics]] — the metrics that *must not* go down, even if the primary does up.
- [[references/sample-size]] — how big, how long; the cost of stopping early.

## Pitfalls

- [[references/novelty-effects]] — the lift that decays after week three; how to detect and discount it.
- [[references/ship-and-iterate]] — when "good enough to ship" beats "perfect to test."

## Discipline

- [[references/kill-criteria]] — the threshold for stopping an experiment instead of milking it.
- [[references/experiment-cadence]] — weekly review rhythm that keeps "hundreds per week" survivable.

## Sibling skills

- [[../duo-retention/SKILL]] — every retention claim has an A/B test under it; cite both.
- [[../duo-product/SKILL]] — *Ship It* and *Show Don't Tell* are the same culture seen from two angles.
- [[../duo-culture/SKILL]] — experimentation only works if disagreement is safe; that's a culture problem too.

## Sources

- Duolingo Handbook (2025), Principle #4: *Show Don't Tell*
- blog.duolingo.com — engineering and experimentation posts
