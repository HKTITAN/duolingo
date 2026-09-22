---
name: duo-mobile-engineering-treat-the-build-loop-as-a-shipped-feature
summary: Split along disjoint boundaries so builds parallelize, prebuild and cache slow build-time tooling as a binary, and find which resource actually binds before scaling the obvious one.
metadata:
  internal: true
---

# Treat the Build Loop as a Shipped Feature

## Concept

Build wait is paid on every single iteration, so it multiplies by the number of changes rather than adding once. That makes it one of the few internal costs that genuinely compounds — and one of the few whose fix is straightforwardly profitable, because compute is cheap relative to engineers idling hundreds of times a week.

Three levers, in rough order of leverage. Split the codebase along genuinely disjoint boundaries so the toolchain is permitted to build only what changed and to build parts in parallel — without enforced disjointness it must assume everything depends on everything. For a slow build-time tool, do not optimize its compile; arrange for it almost never to be compiled. And before scaling the obvious resource, find out which one actually binds.

## What Duolingo does

Source: blog.duolingo.com/sped-up-android-ios-builds (Duolingo blog, 2024-12-18; accessed 2026-09-22)

- Android and iOS CI went from **over 50 minutes to under 16 — a 68% reduction**.
- They tested **16 AWS instance types** and learned that **JVM builds are memory-bound, not CPU-bound**, moving to `r7a` for **+21%**. The intuitive lever was the wrong one.
- Other components: **pipeline reordering −20% serial time**, a **remote S3 build cache +25%**, and **replacing the annotation processor with its faster successor plus a language version bump +30%**. On iOS, **Apple Silicon −60%** and **dependency caching ~4 minutes**.
- Two tensions Duolingo names outright. They **abandoned a remote-cache tool after months of cache misses and unexplained build failures** — "not every tool fits every setup." And they **explicitly accepted higher machine costs**, offsetting with savings plans and autoscaling, because the bound resource was human waiting time.

Source: blog.duolingo.com/a-good-read-building-duolingo-abc-for-android (Duolingo blog, 2022-10-06; accessed 2026-09-22)

- Duolingo ABC's Android app was modularized into **disjoint features (onboarding, home, lesson)** with shared concepts extracted into library modules, enabling **parallel builds** and **partial builds that skip unrelated modules** during development. A **fresh full build takes 1 to 2 minutes**.

Source: blog.duolingo.com/ios-mvvm-swift-macros (Duolingo blog, 2025-07-10; accessed 2026-09-22)

- Their macro package added **10–20 seconds to clean builds** when imported through the package manager. Rather than optimizing its compile, they **link the prebuilt binary**, rebuilding only on local package changes, with **CI building and caching the binary in S3 on merge** so everyone else downloads rather than builds it.
- Not fully solved: language restrictions on global-scope names sometimes force an engineer to edit the macro package when adding a new reference, triggering a full rebuild. They mitigate with naming conventions rather than pretending it is fixed.

## The transferable pattern

1. **Measure before you scale.** Benchmark across machine profiles and find the binding resource. Throwing cores at a memory-bound workload buys nothing, and the intuitive lever is wrong often enough to be worth ten minutes of testing.
2. **Pay a higher unit cost when the bound resource is human waiting time.** A pricier machine that halves the wait is profitable even though the line item goes up. Make that argument with the multiplication, not with the hourly rate.
3. **Enforce disjoint boundaries so partial and parallel work is legal.** The boundary is the enabling constraint; without it the toolchain is obliged to be conservative.
4. **Prebuild, cache centrally, link as a binary.** Total cost is compile time multiplied by number of builds, and the second factor is usually cheaper to attack. Most people never touch the tool, so a cached artifact makes their marginal cost zero regardless of how slow a cold build is.
5. **Abandon tools that do not fit.** Months of cache misses and unexplained failures is a result, not a setup problem to keep grinding on.

## Apply to your product

- How many times a day does your team wait on a build, test run or deploy? Multiply by the wait and compare it to a bigger machine.
- Are your module or service boundaries genuinely disjoint, or does every change invalidate everything downstream?
- Is there a slow build-time dependency everyone compiles that only three people ever modify? That is a cached binary waiting to happen.

## See also

[[fix-the-diagnostic-loop-before-the-bug]] · [[generate-the-boilerplate-instead-of-relaxing-the-standard]] · [[put-the-size-delta-on-every-pull-request]]
