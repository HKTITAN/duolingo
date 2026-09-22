---
name: duo-metric-design-pair-every-growth-metric-with-a-quality-proxy
summary: A growth metric alone drifts toward whatever is cheapest to repeat; pair it with a daily-readable proxy for whether the user actually got value.
metadata:
  internal: true
---

# Pair Every Growth Metric With a Quality Proxy

## Concept

Raw engagement counts are gameable by low-value actions — not by malicious users, but by your own roadmap. Once a count is the goal, the cheapest way to raise it is to make the counted unit smaller and easier, and a quarter of that drift is very hard to see from inside.

The counterweight is a quality proxy that sits next to the growth metric and asks whether the user got the value, not whether they showed up. The proxy has to be readable *daily*, because the only place it does real work is inside an A/B test, where a two-week experiment cannot wait on a six-month outcome study.

## What Duolingo does

Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

- The core product metric went through **three generations**: Total Sessions, then Time Spent Learning, then **Time Spent Learning Well (TSLW)** — each rewrite triggered by the previous version proving gameable or skewed.
- Total Sessions failed in a specific, instructive way: it **penalized learners who advanced to harder content**. Harder work takes longer, so it produces fewer countable units per unit of time. Average seconds per lesson rises from Intro to A-level to B-level material. The metric was quietly rewarding people for staying easy.
- TSLW is designed as a **proxy for learning that is readable daily in A/B tests**, unlike the formal Efficacy Lab studies Duolingo runs in parallel.
- Stated tension: Duolingo calls TSLW **explicitly a proxy** and maintains the separate Efficacy Lab precisely because the proxy is not the real thing. They say the formula is still being refined.

The structural reason a quality counterweight has to be a stated rule, not a preference: fast levers beat slow mechanics whenever nobody is enforcing otherwise. Duolingo's VP of Product names **"Take the long view"** as the explicit tiebreaker, citing investment in the daily streak over blanket push notifications, which would raise DAU quickly — "that's why we invest heavily in the daily streak and don't send tons of push notifications." The same post calls this a "necessary course correction" against built-in incentives to ship fast and score fast wins, meaning the principle has to be enforced rather than assumed. Source: blog.duolingo.com/product-principles (Duolingo blog, 2024-02-21; accessed 2026-09-22)

## The transferable pattern

1. **Write down how your growth metric could rise while users get less.** If you cannot produce that scenario, you do not understand the metric yet.
2. **Build a proxy for the outcome, at daily resolution.** Perfect measurement of the real outcome is usually slow and expensive; you need something noisy and fast that correlates with it.
3. **Keep the rigorous measurement running separately.** The proxy earns its place by being cheap; the slow study earns its place by being true. One validates the other. Never let the proxy quietly become the definition.
4. **Expect to rewrite the metric.** Three generations is a healthy sign, not a failure. Each rewrite should name the specific way the previous version got gamed.
5. **Make the long-view choice a stated rule.** Otherwise the three-week lever beats the three-month mechanic every time, and picking the mechanic stays an act of individual courage instead of a defensible decision.

## Apply to your product

- Name the cheapest, dumbest way your headline number could double without a single user being better off. Is anything in your roadmap quietly pointed at it?
- What is the fastest signal you have that a user actually got the outcome — and can you read it inside a two-week experiment?
- When a fast lever and a slow structural investment compete for the same team, what written rule decides it?

## See also

[[put-the-weight-in-the-formula-not-the-memo]] · [[threshold-percentage-not-aggregate-total]] · [[refuse-to-measure-the-vague-goal]] · [[../duo-efficacy-measurement/SKILL]]
