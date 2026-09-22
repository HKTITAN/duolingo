---
name: duo-growth-model-compounding-makes-timing-a-lever
summary: A retention gain feeds the next period's base, so launch date dominates lifetime value and roadmap order is a lever independent of scope.
metadata:
  internal: true
---

# Compounding Makes Timing a Lever

## Concept

A retention improvement is not a one-time gain, it is an interest rate. The users it saves today are part of tomorrow's base, which the same improvement then acts on again. Lifetime value therefore depends more on the date you launch it than on its size — and every day of delay is compounding you never recover, a loss that grows with time instead of staying fixed. The same arithmetic makes roadmap *order* a lever independent of scope: two identical projects delivered in opposite sequence produce different totals.

## What Duolingo does

Source: blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22)

- The "sense of urgency" principle is argued with a worked example: a **1% retention lift on 100k DAU** adds **1,000 users on day one** but **1,072 per day one week later** — **7.2% more per day**, purely because it shipped a week earlier. Extend the horizon and the gap keeps widening.
- Two of the five published growth guidelines are ordering rules, not scope rules: **prioritize high-ROI projects first** because "they will have a longer period of paying compound interest", and **launch on your largest platform first, then port** — the post's example is shipping Android before iOS when Android is bigger.
- The regime this runs in: **hundreds of experiments per quarter**, roughly **90% of DAU growth from word of mouth**, DAU **4.9M at the start of 2019 to 21.4M by Q3 2023**.
- Tension the post concedes in its own words: "many reasonable people (and companies) gather as much data as possible, wait to launch until things are perfect." This is an explicit bet that speed beats certainty. It is not proven universal, and it is a bad bet where a reversal is expensive — anything that touches money, trust, safety or data you cannot un-write.

## The transferable pattern

- **Price delay, not just scope.** Before a "let's polish it one more sprint" decision, compute what the change earns per day and multiply by the delay. That number is usually larger than the polish is worth, and it is never zero.
- **Order by return, then by base size.** Highest-return work first, because it compounds longest. Among equivalent work, ship where the audience is largest first and port second — the same percentage on a bigger base compounds harder.
- **The compounding argument only applies to gains that feed their own input.** A retained user creates tomorrow's retained user. A one-off conversion bump or a fixed-fee contract does not compound, so treat it with ordinary prioritization.
- **Set a reversibility bar, not a confidence bar.** Ship fast where a bad outcome can be rolled back in a day. Where it cannot, the "wait for certainty" camp is right and compounding is not a licence.
- **Compounding also punishes the delay you cannot see.** The cost of a slow review process, a monthly release train or a queued approval is the same arithmetic applied to everything in the pipeline at once, which is usually a larger number than any single project's polish.

## Apply to your product

- Take the highest-confidence improvement sitting in your backlog. What does it earn per day once live, and what is the running total of the days it has been waiting?
- Is your roadmap ordered by return, or by which team is free, which quarter it fits, or who asked loudest?
- Which of your pending launches is genuinely reversible within a day, and which would take a month to unwind? Only the first group should be shipped on the speed bet.

## See also

[[attack-the-widest-funnel-step-not-the-deepest]] · [[a-free-tier-buys-statistical-power]] · [[../duo-product/references/ship-it]]
