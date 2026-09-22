---
name: duo-backend-architecture-split-data-by-sharing-pattern
summary: Classify data as expensive-but-shared (precompute offline, cache) or cheap-but-per-user (caller injects it); almost no request-time lookups survive.
metadata:
  internal: true
---

# Split Data By Sharing Pattern

## Concept

Most services organize their data access by module — this component owns that table. A far more useful axis is how the data is shared. Put every piece of data your request path needs into one of two buckets. **Expensive to compute but identical across all users** amortizes: do it once, offline, write the result into cheap immutable storage, and cache it in memory. **Cheap to compute but unique per user** cannot amortize at all, so paying for it at request time is acceptable — but only if the caller already holds it and can pass it in rather than making your service go fetch it. Run the split honestly and you find that almost nothing legitimately requires a live lookup.

## What Duolingo does

Source: blog.duolingo.com/rewriting-duolingos-engine-in-scala (Duolingo blog, 2017-01-31; accessed 2026-09-22)

- Course data — heavy to process, identical for everyone studying the same course — was processed **offline**, serialized to flat files on S3, then fetched and held in an **in-memory cache**. It is never computed during a request.
- Per-user personalization data — light to compute, different for every learner — was fetched by the **API servers** and **injected into the request** to the Session Generator. The engine itself performs no user lookup.
- After the split, the service's total average latency was **14ms**, and most of that remaining 14ms was the occasional re-download of course data from S3 when the in-memory cache expired. The dominant remaining cost was cache refill, not lookups.
- Note the direction of the tradeoff: immutable precomputed files are stale by construction. A content change is not live until the offline job reruns, which is the price of removing the read.

## The transferable pattern

Take the data your hot path needs and sort it on two questions — is it costly to produce, and is it the same for every caller?

| | Same for everyone | Different per caller |
|---|---|---|
| **Expensive** | Precompute offline, store immutably, cache in memory | The real problem — redesign or move it off the request |
| **Cheap** | Embed it or cache it trivially | Have the caller inject it into the request |

Three consequences worth planning for:

1. **The precomputed half needs a publish pipeline, not a cache-invalidation strategy.** Immutable artifacts with a version in the name beat mutable keys you have to expire correctly.
2. **The injected half moves a cost onto your caller.** That is fine when the caller genuinely already has the value in hand; it is a regression when the caller now has to make a lookup of its own to satisfy you.
3. **The interesting quadrant is expensive-and-personal.** Anything landing there is a design smell — either it can become shared with a coarser key, or it belongs in a background job whose result the user reads later.

## Apply to your product

- Take the five slowest reads in your hot path. For each, is the result identical for every caller, or genuinely per-caller — and have you ever checked rather than assumed?
- Which values does your upstream caller already hold at the moment it calls you, that you are currently re-fetching yourself?
- If you precomputed the shared half nightly, how stale would the worst case be, and would anyone notice?

## See also

[[delete-dependencies-from-the-request-path]] · [[move-the-ui-definition-to-the-server]] · [[hold-the-lock-only-over-shared-work]]
