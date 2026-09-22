---
name: duo-backend-architecture-duplication-can-beat-the-abstraction
summary: When the abstraction that removes duplication triples the line count, take the duplication — but extract genuinely variant-agnostic logic into a core library.
metadata:
  internal: true
---

# Duplication Can Beat The Abstraction

## Concept

De-duplication optimizes one cost: the risk that two copies drift apart. It ignores a second cost that every future reader pays — comprehension. When the machinery that removes the duplication becomes the hardest thing in the codebase, you have traded a cheap, visible cost for an expensive, invisible one. The useful test is not "is this duplicated?" but "which version is easier to change safely six months from now?" Sometimes that is the shared abstraction. Sometimes it is two straightforward copies and a deleted layer. The judgment turns on what actually differs between the variants: if the difference is a thin edge, share the middle; if the difference runs all the way through, stop fighting it.

## What Duolingo does

Source: blog.duolingo.com/async-python-migration (Duolingo blog, 2025-03-25; accessed 2026-09-22)

- To share its Microservice Client — auth, retries, metrics, circuit breaker, log delivery — between synchronous and asynchronous libraries, Duolingo built a **sans-I/O state machine**. It worked, reached about **1,000 lines**, and was hard to understand.
- Reimplemented with I/O-dependent code in each variant, it shrank to about **300 lines** — roughly a **3.3x reduction**. They took the duplication.
- **They did not abandon sharing.** They kept a **core library** pattern for genuinely I/O-agnostic logic: `duo_metrics_core` holds the transport-independent metrics logic with its own request/response data types, and the async HTTP client knows only how to convert an async response into those objects — it knows nothing about the metrics system underneath.
- **The core library has its own admitted friction.** It can contain neither blocking code (async programs must not run it) nor async code (sync callers cannot run it without an event loop), which sharply limits what may live there — and a straightforward change can require **three pull requests**: core, sync, async.

The opposite lesson applies to configuration. Duolingo treats environment setup as code that must be kept single-sourced across repositories: shared tools baked into one repo-agnostic base image, hook scripts chained from base image to a self-updating org CLI to an optional per-repo script, and an open-source bulk-edit tool used to declare the same lean config across the vast majority of repos — necessary once they had **hundreds** of microservice environments. Duplicated config rots exactly like duplicated code, except nobody reviews it, and a layered hook chain lets you change behavior for all existing environments without recreating them (blog.duolingo.com/developer-onboarding-with-github-codespaces (Duolingo blog, 2022-10-14; accessed 2026-09-22)).

## The transferable pattern

1. **Count lines and comprehension, not just repetition.** If removing duplication multiplies the code and concentrates the difficulty, the abstraction is the more expensive artifact.
2. **Find the true axis of difference.** Two variants usually differ only at the boundary — how bytes move, which runtime drives them — while the domain logic is identical. Isolate the agnostic middle; let each variant own only its boundary translation. Translation code is shallow enough that duplicating it is safe.
3. **A shared core has a floor cost per change.** Multiple repositories or packages means multiple reviews for one behavior change. Factor that into whether the sharing is worth it.
4. **"Don't share" is not the lesson — "don't share through elaborate machinery" is.** A plain library of pure functions is a good shared thing. A state machine that exists purely to avoid writing two loops usually is not.
5. **Configuration is the one place to be dogmatic about de-duplication.** It is invisible, unreviewed, and drifts silently across every repository. Single-source it, layer it so it can be changed in place, and use tooling to apply changes in bulk.

## Apply to your product

- Where in your codebase is the hardest file to understand an abstraction whose only job is to prevent duplication — and what would the duplicated version actually look like?
- For your two-variant problem (two runtimes, two transports, two platforms), what genuinely differs: the domain logic, or only the translation at the edge?
- How many copies of your build, deploy or environment configuration exist across your repositories, and when did anyone last diff them?

## See also

[[prefer-a-loading-state-to-a-rollback]] · [[pitch-migrations-in-the-sponsors-currency]] · [[extract-what-blocks-its-own-improvement]]
