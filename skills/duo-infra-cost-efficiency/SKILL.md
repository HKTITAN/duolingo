---
name: duo-infra-cost-efficiency
description: Make infrastructure spend visible, attributable and cuttable without slowing the company down — hourly per-dimension cost tagging, pushing the number into channels engineers already read, defining a win as waste removed rather than spend removed, pricing tech debt in dollars, auditing internal fan-out and cache TTLs, relaxing freshness so caching becomes legal, and deterministic entity-level sampling. Use when someone says our cloud bill is out of control, we cannot tell which team or feature is spending, costs jumped last month and nobody knows why, our LLM spend grows faster than usage, how do we justify infrastructure work to leadership, our analytics queries are slow and expensive, or should we just buy more capacity. For the architectural fix itself, route to duo-backend-architecture.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Infra Cost Efficiency

Most cost problems are not hard to fix. They are hard to see, hard to attribute to
a person who could reverse them, and hard to argue for once seen. This skill owns
that chain — attribution, framing, governance — not the rewrite at the end of it.

The order matters. Visibility first, because you cannot cut what you cannot name.
Framing second, because a cut scored only in dollars will eventually cut something
that was earning its keep. Technique last, because the specific moves below only
pay off once someone is watching the number.

## Seeing the spend

- [[references/tag-every-dimension-at-hourly-granularity]] — a single aggregate number tells you nothing; tagged hourly spend aligns a cost change with a deploy window and makes two similar features comparable.
- [[references/put-the-number-where-engineers-already-look]] — the count of eyes on the number is the lever, not the sophistication of the analysis; quote unit economics in each audience's own unit.

## Framing the work

- [[references/target-waste-not-spend]] — define an efficiency win as spend down with quality unchanged, which makes a neutral experiment result a success; overprovisioning and never-expiring storage are the two reliable reservoirs.
- [[references/price-tech-debt-in-dollars]] — a recurring invoice supplies the urgency that "this is messy" never does, and an ML case is easier to win by shrinking its cost side than by inflating its benefit side.

## Cutting it

- [[references/audit-the-fan-out-not-the-endpoint]] — one inbound request can trigger a five-fold chain of internal calls, so deleting a call at the top removes bandwidth, load balancing and provisioned capacity at every level below.
- [[references/relax-freshness-to-make-caching-legal]] — interrogate the freshness requirement before optimizing the database; most systems advertising real-time accuracy inherited it from an early decision nobody revisited.
- [[references/sample-by-entity-not-by-row]] — hash a stable entity key and physically sort storage by it, so the sample is deterministic, cohorts stay whole, and the engine skips the rest instead of scanning and discarding it.

## Boundary

This skill stops at the point where you know what to change and why it is worth
changing. The redesign itself — request-path structure, caching architecture,
migration staging — belongs to [[../duo-backend-architecture/SKILL]]. If the bill
is a symptom of an unreliable system rather than a wasteful one, start at
[[../duo-production-reliability/SKILL]] instead.

## Sibling skills

- [[../duo-backend-architecture/SKILL]] — how to restructure the request path once cost has told you where to look.
- [[../duo-production-reliability/SKILL]] — what production is actually doing, in traces and incidents rather than invoices.
- [[../duo-ml-in-production/SKILL]] — whether a model is worth operating at all, and what to evaluate it on.
- [[../duo-measurement-validity/SKILL]] — when an approximate number is still a trustworthy one, which is the question sampling forces.

## Sources

Distilled from blog.duolingo.com posts on FinOps practice (2025-09-08), cloud spend reduction (2024-10-30), sampling for data analysis (2025-05-23), an internship caching project (2017-09-30), engineering constraints at scale (2024-05-15) and machine learning for ads (2025-03-18). Each node carries its own dated citation.
