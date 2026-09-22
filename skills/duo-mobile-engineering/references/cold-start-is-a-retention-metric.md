---
name: duo-mobile-engineering-cold-start-is-a-retention-metric
summary: Treat startup latency as retention, not polish — and precompute the warmup rather than relying on mechanisms that learn from usage if you ship faster than they can warm up.
metadata:
  internal: true
---

# Cold Start Is a Retention Metric

## Concept

Startup time gets filed under polish, which is why it never wins a prioritization argument. Filed under retention it wins immediately, because retention has an owner, a dashboard and a target. The reframe is not rhetorical — the user who abandons during launch is indistinguishable, in your data, from the user who churned, and they churn in the same place every single day.

The second idea is subtler and easier to get wrong. Many platforms offer adaptive optimizations that observe real usage and then optimize the hot paths. These need days of stable installs to pay off. If your release cadence is faster than that warmup period, the optimization resets before it ever matures, and *every* user permanently experiences the un-optimized path. The fix is to precompute the profile at build time and ship it with the artifact, so the benefit lands on first launch.

## What Duolingo does

Source: blog.duolingo.com/slashed-android-startup-time-baseline-profiles (Duolingo blog, 2025-05-02; accessed 2026-09-22)

- Duolingo adopted Android **baseline profiles** after observing that faster startup correlated with users sticking around — the work was justified as retention, not as craft.
- Cloud profiles, the adaptive mechanism that learns from aggregate usage, were **useless to them**: those take days to generate and **reset on every update**, and Duolingo **releases weekly**. The warmup never completed.
- Shipping a precomputed profile inside the build moved the benefit to first launch instead.
- Measured result: **~30% startup time improvement in production metrics**, **25–40% in macrobenchmark tests**, and **JIT thread busy time dropped from 25% to 3%** — the clearest evidence that the work was moved off the critical path rather than merely reordered.
- A side effect they did not set out to buy: **reduced jank in music lessons**, because the same ahead-of-time compilation helps any latency-sensitive path, not just launch.

The cost, named honestly: this optimization is invisible until you verify it end to end, and Duolingo shipped an entirely inert version of it first. That failure is its own node — see [[verify-the-harness-and-route-around-vendors]].

## The transferable pattern

- **Reframe the metric to the owner who can fund it.** "Startup is slow" is an engineering complaint. "We lose X% of sessions before the first screen" is a retention number, and retention has a budget.
- **Audit any optimization that learns from usage against your release cadence.** If the mechanism needs N days of stability and you ship every N/3 days, you are paying for it and receiving nothing. This applies well beyond app launch — caches, adaptive indexes, JIT-style warmups, and model-serving warm pools all have this shape.
- **Precomputing at build time converts a warmup into a constant.** The artifact you ship already contains the answer, so the first user gets what the thousandth user would have got.
- **Look for the secondary beneficiaries.** Work that removes contention from the critical path usually improves every other contended moment too; instrument those before you start so you can claim the win.

## Apply to your product

- What fraction of your users abandon before reaching your first useful screen, and is that number on anyone's dashboard next to churn?
- Do you depend on anything that has to warm up — a cache, an adaptive optimizer, a pool — and does your deploy frequency give it enough time to ever pay off?
- Which of your slow paths could be precomputed and shipped as data with the build, instead of computed on the user's device or machine?

## See also

[[optimize-against-conversion-not-milliseconds]] · [[defer-everything-the-first-screen-doesnt-need]] · [[../duo-retention/references/churn-diagnostics]]
