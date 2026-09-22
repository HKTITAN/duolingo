---
name: duo-infra-cost-efficiency-audit-the-fan-out-not-the-endpoint
summary: One inbound request can fan out fivefold internally, so deleting a call at the top of the chain removes cost at every level below it.
metadata:
  internal: true
---

# Audit the Fan-Out, Not the Endpoint

## Concept

In a service architecture the expensive number is not requests received, it is requests generated. One inbound call can trigger a chain of internal calls several times its size, and every internal hop multiplies three separate costs — bandwidth, load balancing, and the capacity each downstream service must provision to absorb the volume.

Removing one call at the top of the chain removes all three at every level below it. That is why the leverage is superlinear, and why endpoint-level optimisation misses it entirely.

## What Duolingo does

Source: blog.duolingo.com/reducing-cloud-spending (Duolingo blog, 2024-10-30; accessed 2026-09-22)

- Inbound traffic fans out into a roughly **fivefold** chain of internal calls.
- They refactored a legacy service that was making API calls **as indirect side effects** — calls no caller had asked for. That single refactor eliminated **2.1 billion unnecessary calls per day**.
- They extended an **ETag cache TTL from one minute to one hour** on data that rarely changes, cutting traffic to the downstream service by **over 60%**.
- **Tension.** A longer TTL is a staleness decision, not a cost decision. An hour of staleness has to be acceptable to the product before it is available to the bill.

Write amplification is the same problem in a different shape. Birdbrain stores a learner's per-course scores as a single DynamoDB row to keep API latency low, so A/B testing two models at once would have implied doubling storage writes. Rather than test fewer models, Duolingo **sharded the input stream by user id** — guaranteeing one worker sees every record for a given user, which makes in-memory buffering safe without coordination — and added an **LRU write buffer**, so state is written once per batch instead of once per event. Running grammar and vocabulary model tests **simultaneously is now 50% cheaper than running the original grammar model alone** (blog.duolingo.com/unique-engineering-problems (Duolingo blog, 2024-05-15; accessed 2026-09-22)).

## The transferable pattern

1. **Measure amplification, not volume.** Internal calls per inbound request is the ratio that predicts your bill. If nobody knows yours, that is the first number to get.
2. **Hunt for calls nobody asked for.** Side-effect calls buried in helpers and middleware are the cheapest deletions in any system, because no behaviour depends on them.
3. **Raise TTLs on things that rarely change.** The default TTL is almost always a guess made in the first week. Match it to the real change rate, not to the guess.
4. **Fix write amplification at the writer.** When per-event writes get expensive, partition the stream by the entity key so one worker owns an entity, buffer in memory, and evict least-recently-used. Writes fall by the buffer factor and memory stays bounded.
5. **Cheap experimentation compounds.** Once running two variants costs less than one used to, you stop rationing experiments and start evolving continuously.

Choosing the new request-path shape is a design problem, not a cost problem — hand it to [[../duo-backend-architecture/SKILL]] once the fan-out audit has told you where to aim.

## Apply to your product

- For your busiest inbound endpoint, how many internal calls does one request generate? Count them, including the ones hidden in shared middleware.
- Which cached resource has the shortest TTL and the slowest real rate of change?
- Where do you write once per event for data that only needs to be correct once per batch?

## See also

[[relax-freshness-to-make-caching-legal]] · [[tag-every-dimension-at-hourly-granularity]] · [[../duo-backend-architecture/SKILL]]
