---
name: duo-mobile-engineering-measure-from-your-worst-region-and-device
summary: A check invisible at 20ms is a product-killing block at 1000ms — measure from the worst end of your distribution, fetch only the slice in use, and test on the worst hardware in the building.
metadata:
  internal: true
---

# Measure From Your Worst Region and Device

## Concept

Latency distributions are geographic and infrastructural, and engineering teams sit at the fastest end of them — good hardware, good network, close to the origin. Every synchronous call on your critical path is therefore evaluated under conditions almost none of your users experience, and the users on the bad end of that distribution are usually the ones you are trying to grow.

The same asymmetry applies to payload size. A large response is not only a download cost; it is CPU, memory and deserialization cost paid on every session regardless of how little of it the user touches. Past a certain size the data model becomes a veto on the roadmap — new features get killed not because they are bad but because the payload cannot absorb another field.

And it applies to defects. Timing-dependent bugs are invisible on fast devices because the fast path always wins the race. A constrained device makes the ordering bug deterministic.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- The app made a **blocking startup request to check site availability**. In regions like **India this took over 1 second**. Making it non-blocking produced a **15% reduction in startup time** — for a call that was imperceptible from the office.
- Flagship course models (English to Spanish, for example) had grown to **multiple megabytes**, slow to download and taking **several seconds to de/serialize**, though learners touch only a small part at a time. They sectioned the data and fetched only the relevant chunk. Duolingo notes this **required substantial refactoring on both backend and client**, and that the payoff included **unblocking features previously shut down for causing performance regressions**.

Source: blog.duolingo.com/unique-engineering-problems (Duolingo blog, 2024-05-15; accessed 2026-09-22)

- Moving from fetching entire course metadata at startup to fetching only the current section was **up to a 90% reduction in metadata** for the largest courses.

Source: blog.duolingo.com/duolingo-stories-the-journey-to-android (Duolingo blog, 2020-02-21; accessed 2026-09-22)

- An engineer testing an early prototype on **an Android phone with below-average memory and compute** noticed cover images intermittently failing to appear. It was a **race condition invisible on normal devices**.

## The transferable pattern

1. **Instrument by segment, not in aggregate.** A p50 that includes your team's machines and your best region tells you nothing about the population whose experience is deciding your growth. Slice by device tier and by region before you decide what to optimize.
2. **Audit every synchronous call on the critical path against the worst segment's round-trip time.** Cheap-here is not cheap-there, and the call that costs 20ms locally is the one nobody thought to question.
3. **Fetch the slice in use, not the whole object.** Chunk the payload along the boundary the user actually moves through. The refactor is real work on both ends — budget it as a platform project, not a performance tweak.
4. **Hand internal builds to teammates on the worst hardware you have.** Constraint is a test oracle: it makes the ordering bugs that matter for most of your users reproducible for the one person who can fix them.

## Apply to your product

- What is your slowest region or network tier, and do you have a single dashboard that shows it separately rather than folded into an average?
- Which response in your product is the largest, and what fraction of it does a typical session actually read?
- Who on your team uses the cheapest device or the worst connection, and are they on the internal build — or is everyone testing on the same fast laptop?

## See also

[[defer-everything-the-first-screen-doesnt-need]] · [[optimize-against-conversion-not-milliseconds]] · [[../duo-product/references/dogfooding]]
