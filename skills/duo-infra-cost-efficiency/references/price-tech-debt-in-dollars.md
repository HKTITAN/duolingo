---
name: duo-infra-cost-efficiency-price-tech-debt-in-dollars
summary: A recurring invoice converts an aesthetic argument into an arithmetic one; the same move wins capped-upside cases by shrinking their cost side.
metadata:
  internal: true
---

# Price Tech Debt in Dollars

## Concept

Code quality arguments are contested because quality is subjective and its payoff is deferred. A recurring monthly invoice is neither. Attaching the number to the debt converts an aesthetic argument into an arithmetic one, and the cleanup delivers the quality benefit as a side effect. Cost optimisation and code health turn out to be the same project approached from opposite ends.

## What Duolingo does

Source: blog.duolingo.com/reducing-cloud-spending (Duolingo blog, 2024-10-30; accessed 2026-09-22)

- The cost programme uncovered **ancient ElastiCache clusters, entire unused databases, and a whole abandoned microservice** — all belonging to legacy features whose code had never been cleaned up. The team's explicit conclusion was that cost work and code health go together.
- Their FinOps team **frames tech debt as real dollars to win leadership buy-in**, and names the debt work that paid for itself directly — **Graviton migration, cheaper instance types, removing unnecessary API calls, Python and Java version upgrades** (blog.duolingo.com/finops (Duolingo blog, 2025-09-08; accessed 2026-09-22)).

The same arithmetic runs from the other side — instead of inflating a project's benefit, shrink its cost. Duolingo's ads-optimization model had a bounded upside, so they built it with **dbt and BigQuery ML**, because dbt already powered all of their data pipelines. Training, evaluation and hyperparameter tuning were a few lines of code and inference was just a SQL query, so the marginal infrastructure was close to zero and a modest gain cleared the bar (blog.duolingo.com/machine-learning-ads (Duolingo blog, 2025-03-18; accessed 2026-09-22)).

**Tension.** Pricing debt funds the debt that happens to be expensive. Debt that is merely dangerous — fragile, undocumented, one-person-deep — has no invoice attached and stays unfunded. Dollars are a lever for a subset of the problem, not a ranking of all of it.

## The transferable pattern

1. **Convert "this is messy" into "this costs $X a month."** The second sentence gets scheduled. The first gets sympathy.
2. **Follow the spend to the dead code.** Orphaned infrastructure is the fingerprint of a feature that was removed from the interface but never from the system.
3. **Deprecation work is cost work.** Runtime and platform upgrades, cheaper instance families, deleting calls nobody consumes — these ship as savings and land as hygiene.
4. **When upside is capped, attack the denominator.** Build on the stack your team already operates, so ongoing maintenance stays near zero. Most of a model's lifetime cost is operational surface, not training.
5. **Keep a second list for unpriceable risk**, or the cheap-and-fragile will outlive everything you cleaned up.

## Apply to your product

- Take your three worst pieces of tech debt. What does each cost per month in infrastructure, and which one would a finance partner fund today?
- Which of your running resources belongs to a feature no longer reachable from your interface?
- For the next project you have to justify, could you cut its infrastructure ask to near zero by building it on something you already run, instead of arguing the upside up?

## See also

[[put-the-number-where-engineers-already-look]] · [[target-waste-not-spend]] · [[../duo-ml-in-production/SKILL]]
