---
name: duo-ai-product-strategy-spend-the-automation-budget-on-the-gate
summary: Find the one constraint everything downstream waits on and put the whole automation budget there; its shadow price is far above its direct cost.
metadata:
  internal: true
---

# Spend the Automation Budget on the Gate

## Concept

Automation budgets get spread evenly because every team can name something slow. Spread evenly, they produce a slightly faster version of the same output.

A gate behaves differently. A gating constraint suppresses every option that depends on it, including the options nobody bothers to propose because they are obviously unaffordable. Its shadow price — what the whole business would pay to relieve one more unit of it — is far above its direct cost, and none of that shows up in the budget line. So the evidence that you picked the right target is not "we do more of the same, faster." It is that work which was previously uneconomic becomes merely cheap, and the roadmap changes shape.

## What Duolingo does

Source: blog.duolingo.com/large-language-model-duolingo-lessons (Duolingo blog, 2023-06-22; accessed 2026-09-22)

- The staffing arithmetic is the reason the gate exists at all — **fewer than 1,000 employees** against **more than 21 million daily active users** at the time of writing (June 2023). Headcount cannot scale with usage, so anything that requires headcount per unit of output becomes the ceiling.
- The gate was course content creation. **Most courses shipped new material only a few times a year**, because every unit of it waited on expert authoring capacity.
- LLM-assisted authoring was justified by three unlocks, and this is the part worth copying — none of them is "more of the same":
  1. **Depth** — going further up the CEFR scale into advanced material that was never worth authoring by hand.
  2. **New formats** — freeing expert time for things like Stories and DuoRadio rather than routine production.
  3. **The long tail** — finally serving small courses that never get the spotlight but have dedicated learners.
- That third one is the clearest signal of a real gate. Small-audience work is not blocked by lack of demand or lack of will; it is blocked by the per-unit cost of the gated resource, so it appears the moment the gate loosens.

**Tension.** Relieving a gate does not automatically produce good output at the new volume — it removes the constraint that was implicitly enforcing consistency. Duolingo's own scaling work hit exactly this, and the antidote is in [[simplify-until-automatable-name-what-must-survive]]. Volume that arrives without a quality bar defined first is a different problem, not a solved one.

## The transferable pattern

- Find the resource that everything queues behind. Usually it is a small group of people whose judgment is required per unit of output, and you can spot it by how many roadmap items include the phrase "once we have capacity for."
- Justify the investment with the unlocks, not the throughput. Write the three things you would do if the constraint were ten times cheaper, and check that at least one of them is something you have never seriously proposed. If all three are "the same thing but more," you found a slow step, not a gate.
- Expect long-tail segments to be the first beneficiaries — they are the population whose economics the gate was silently deciding.
- Resist splitting the budget. Two half-relieved constraints leave the queue exactly where it was; the second-slowest step only matters after the first stops gating.

## Apply to your product

- What is the one resource every roadmap item is implicitly waiting on, and how many times per year does it actually deliver?
- If that constraint got ten times cheaper tomorrow, name three things you would do — and mark which of them you have never put on a roadmap because it was obviously unaffordable.
- Which of your customer segments are you not serving because the cost per unit is fixed rather than because they do not want the product?

## See also

[[point-ai-at-unit-economics-not-features]] · [[author-a-pool-deliver-an-instance]] · [[simplify-until-automatable-name-what-must-survive]]
