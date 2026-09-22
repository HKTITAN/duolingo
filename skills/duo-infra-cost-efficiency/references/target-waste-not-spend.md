---
name: duo-infra-cost-efficiency-target-waste-not-spend
summary: Score efficiency as spend down at unchanged quality, which makes a neutral result a win; overprovisioning and unexpiring storage are the reliable reservoirs.
metadata:
  internal: true
---

# Target Waste, Not Spend

## Concept

Cost and value are not the same axis. A policy that counts only dollars saved will cut the expensive things that work alongside the expensive things that don't, and teams stop proposing valuable spend at all.

Define the win as **spend down with quality unchanged** and two things follow. A neutral experiment result becomes a success rather than a null, and the expensive-but-earning line item is safe from the blanket cut.

## What Duolingo does

Source: blog.duolingo.com/finops (Duolingo blog, 2025-09-08; accessed 2026-09-22)

- The FinOps team **explicitly celebrates neutral experiment metrics** — a change that moves cost down and moves nothing else is the outcome they want.
- They **pay for more expensive LLMs on Video Call specifically to preserve a character's voice**, while separately **migrating their priciest CloudWatch metrics to Prometheus with no loss of observability**. Same programme, opposite directions, one rule.
- **Tension.** The stated rule is user experience before short-term savings, which means known, quantifiable waste is deliberately left on the table when cutting it would degrade the product. The discipline is knowing which is which, not cutting.

Two reservoirs supply most of the genuine waste (blog.duolingo.com/reducing-cloud-spending (Duolingo blog, 2024-10-30; accessed 2026-09-22)):

- **Provisioning headroom.** Duolingo tested real headroom instead of accepting defaults and found **almost all services ran comfortably at 90% memory utilisation, some at 95%**. They downgraded allocations, lowered minimum task counts, and made autoscaling add tasks less aggressively. Fixing task allocation on **one** overscaled service saved **hundreds of thousands of dollars a year**; moving one database to Aurora I/O-optimized saved **several hundred thousand a year**.
- **Storage with no expiry.** They added S3 lifecycle rules to their largest buckets, added missing DynamoDB TTL rules, and audited verbose unsampled production logging — singling out stack traces as a disproportionately large payload not to emit in production. **Tension.** They flag that a new TTL rule **does not delete existing rows**, and that evicting them afterwards is a real pain, so retention is far cheaper to decide before the data exists than after.

## The transferable pattern

1. **Score the experiment on two axes.** Cost must fall; the quality metric must not move. Publish both, and let "cost down, quality flat" count as a win.
2. **Treat defaults as untested guesses.** A provisioning setting was chosen once under uncertainty and never revisited. The absence of an incident is evidence it isn't too small — not evidence it is right. Measure actual headroom.
3. **Give every store a death date at creation.** Lifecycle rules, TTLs, log sampling. Retrofitting expiry costs more than the storage did, and does not act retroactively.
4. **Name the spend you refuse to cut, and why.** An explicit exception list is what stops the policy from hardening into a blanket freeze.

## Apply to your product

- What would you cut first if you had to remove 20%, and which of those cuts would a user notice? That second list is your exception list — write it down now.
- Pick one service and find its real memory and CPU ceiling. How far is it from what you provisioned?
- Which of your data stores has no deletion policy, and how fast does it grow per month?

## See also

[[price-tech-debt-in-dollars]] · [[tag-every-dimension-at-hourly-granularity]] · [[../duo-experimentation/SKILL]]
