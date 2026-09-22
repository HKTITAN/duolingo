---
name: duo-infra-cost-efficiency-tag-every-dimension-at-hourly-granularity
summary: Cost problems are visibility problems; tag every dimension and record spend hourly so a change lines up with a deploy.
metadata:
  internal: true
---

# Tag Every Dimension, at Hourly Granularity

## Concept

A monthly invoice tells you that spend went up. It does not tell you what changed, who changed it, or whether the change bought anything.

Two properties turn a bill into a debuggable signal. **Dimensions** — feature, team, service, customer segment, model — let you compare two things that should cost the same and notice when they don't. **Hourly granularity** lets you align a cost jump with a specific deploy window, which collapses root-cause analysis from a week of changes to a few hours of changes, and turns a cost drop into direct evidence that a specific rollout worked.

## What Duolingo does

Source: blog.duolingo.com/finops (Duolingo blog, 2025-09-08; accessed 2026-09-22)

- An engineer added internal **per-feature text-to-speech cost tracking**. It showed Video Call's TTS costing **60–100x** Roleplay's for near-identical functionality. The cause was not the model or the volume — Roleplay had an **in-memory response cache** and Video Call didn't. Adding the cache cut **overall TTS cost by 40%**.
- A FinOps dashboard caught a **10x spike in OpenAI spend** tied to a single user category. Because the data was hourly and tagged, it was traced and **reverted within hours** instead of going unnoticed for weeks.
- The programme runs with a **FinOps team of 5** and scripts monitoring **100+ microservices** — that is the scale of the attribution work, not of the engineering fixes it finds.

The instructive part is the ratio, not the cache. Nobody suspected a 60–100x gap between two features built by the same company for the same purpose. The gap was invisible until a dimension existed to make the two comparable.

## The transferable pattern

1. **Tag by unit of decision.** If a team, a feature or a customer tier can be changed independently, it needs its own line. Tags that don't map to an owner are decoration.
2. **Record hourly.** Daily granularity smears a deploy across everything else that shipped that day. Hourly is the resolution at which cost becomes a deploy signal.
3. **Look for the ratio, not the total.** The strongest finding is two near-identical things costing wildly different amounts. That difference is always explainable, and the explanation is usually a cheap fix someone already knows how to make.
4. **Extend past the biggest vendor.** The dimension you didn't instrument is where the 10x spike hides, and third-party API spend is often the fastest-growing line.

The cost is real and ongoing — tagging discipline decays, and somebody has to own the dashboards. Treat that headcount as the price of admission rather than as overhead.

## Apply to your product

- Pick your two most similar features. Can you state what each costs per day? If not, that is the first dimension to add.
- If spend doubled last Tuesday, how long would it take you to name the deploy that did it — and would you be guessing?
- Which of your third-party API bills has no owner, no tag, and no alert?

## See also

[[put-the-number-where-engineers-already-look]] · [[audit-the-fan-out-not-the-endpoint]] · [[../duo-llm-feature-engineering/SKILL]]
