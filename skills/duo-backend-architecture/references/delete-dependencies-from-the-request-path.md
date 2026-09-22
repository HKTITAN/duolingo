---
name: duo-backend-architecture-delete-dependencies-from-the-request-path
summary: Every shared resource in a live request path costs latency and adds a failure mode; audit and remove before optimizing inside them.
metadata:
  internal: true
---

# Delete Dependencies From The Request Path

## Concept

A shared resource sitting inside a synchronous request path is never one cost. It is two: a latency term added to every call, and an independent way the whole path can go down. Latency adds; availability multiplies. Four dependencies mean your service can only ever be as fast as the slowest of them and only as available as the product of all their uptimes. Teams usually respond by tuning the dependency — a bigger cache, a faster query. The bigger win is almost always removal: get the lookup out of the live path entirely, and both costs go to zero at once.

## What Duolingo does

Source: blog.duolingo.com/rewriting-duolingos-engine-in-scala (Duolingo blog, 2017-01-31; accessed 2026-09-22)

- Duolingo's Session Generator — the service that assembles each lesson — had accumulated hard dependencies on caches and data stores. Their own architecture diagram marked them red: any single one failing took the engine down.
- The guiding principle of the rewrite was stated plainly as removing as many shared resources as possible, rather than making the calls to them faster.
- Result: average latency **750ms to 14ms**, a **98% drop**. Degraded performance went from **0.1% of the time (~2 hours per quarter) to zero** in the first months. Engine uptime **99.9% to 100%**.
- They are explicit that they do not expect to hold 100% forever — the figure is evidence of robustness, not a durable service-level promise.

A related cost hides in outbound calls rather than inbound ones. In Duolingo's SMS service, `Session().post(...)` constructed a brand-new HTTP client per send, forcing a fresh TCP and TLS handshake every time — invisible at steady traffic, catastrophic under burst (blog.duolingo.com/reduce-cpu-usage-97-percent (Duolingo blog, 2026-06-22; accessed 2026-09-22)).

Counterweight on deleting things you have not traced: Duolingo's linguists note that the "irregular" Spanish imperfect ending *-ía* was once the perfectly regular *-iba*, eroded over centuries and surviving only in one verb. What reads as an arbitrary special case is often a general rule half-decayed (blog.duolingo.com/language-irregularity-and-complexity (Duolingo blog, 2025-09-16; accessed 2026-09-22)).

## The transferable pattern

1. **Inventory before you optimize.** Draw the synchronous path for your single most important request and list every external thing it touches — data store, cache, config service, auth call, third-party API. That list, not a profiler flame graph, is your first artifact.
2. **For each entry, ask "can this be gone?" before "can this be faster?"** Removal candidates: work that can be precomputed, values the caller already holds and could pass in, checks that can move to write time, and side effects that can become asynchronous.
3. **Count failure modes, not just milliseconds.** A dependency that adds 4ms and 0.05% downtime is not cheap. Write the availability as a product and see what the path can structurally promise.
4. **Watch for per-request setup you did not intend.** Connection, client, and session objects constructed inside a handler are handshakes disguised as object allocation.
5. **Trace an oddity before removing it.** In a system that has been under real load for years, the strange branch is usually a fossil of something that still matters. Removing it without finding its origin destroys behavior something depends on.

## Apply to your product

- For your highest-volume endpoint, what is the full list of external resources it touches while the caller waits, and what is the product of their uptimes?
- Which of those could be precomputed, passed in by the caller, or deferred past the response — and what would break if you simply deleted it today?
- Where in your handlers is a client, connection, or session being constructed per request instead of reused?

## See also

[[split-data-by-sharing-pattern]] · [[hold-the-lock-only-over-shared-work]] · [[extract-what-blocks-its-own-improvement]]
