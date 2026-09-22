---
name: duo-production-reliability-sampled-tracing-versus-request-identity
summary: Sampling finds systemic waste; answering what happened to one specific request needs an always-on identity layer you can usually derive from logs you already write.
metadata:
  internal: true
---

# Sampled tracing versus request identity

## Concept

Sampled tracing and per-request identity are two different jobs, and most teams buy one tool and expect it to do both. Sampling tells you what your system does on average, which is how you find systemic waste. It cannot tell you what happened to one specific request, because a rare failure or one complaining customer is statistically absent from a one-in-N sample. The second job needs identity on every request, always on. That sounds expensive, so teams defer it — but the raw material is usually already being written to disk by load balancers and gateways, and the cost is only in stitching it together on demand.

## What Duolingo does

Source: blog.duolingo.com/improving-the-duolingo-experience-with-request-tracing (Duolingo blog, 2021-01-20; accessed 2026-09-22)

- Duolingo ran sampled tracing with Jaeger first. It surfaced systemic patterns but could not answer questions about an individual request, which is what most real complaints are.
- They then found that AWS's `X-Amzn-Trace-Id` header supports arbitrary fields, and propagated a custom `Caller` field through their microservices.
- Full call stacks are reconstructed **on demand** from ELB access logs using Athena and Python. There is no per-request overhead, because the access logs are written regardless — the only cost is the query when someone asks.
- During incidents they rank likely culprit services with a **PageRank-style algorithm** over the derived service dependency graph, rather than paging every team at once.
- Numbers: a **10% reduction in overall Duolingo latency** within the first weeks of testing, traced to one finding — a common internal method querying DynamoDB repeatedly for the same data instead of caching it. Much of the always-on tracing work was **an intern project**.
- Tension worth keeping: the inefficiency was "reasonable when first added" and only became expensive as it was called more often and queried more data over years. The failure mode was drift, not a bad decision — so this is a detector you leave running, not an audit you do once.

## The transferable pattern

1. **Name which question you are buying an answer to.** "Where is the aggregate time going" and "what happened to this one request at 14:32" are answered by different mechanisms. A sampling tool will quietly fail the second question rather than tell you it cannot answer it.
2. **Look for identity you already emit before you buy it.** Gateways, proxies and load balancers already log every request. If you can propagate one field end to end, you can reconstruct the call graph after the fact instead of instrumenting every service.
3. **Pay at query time, not at request time.** Deriving the graph on demand keeps the hot path free, which is what makes always-on affordable.
4. **Rank suspects, do not just display the graph.** During an incident the graph is too big to read. A cheap ranking over the dependency structure turns it into a first place to look.
5. **Assume the expensive path is one that drifted.** The thing burning your latency budget was usually correct when written and grew into a problem, so the detector has to run continuously.

## Apply to your product

- When a single customer says "it was slow for me at 3pm yesterday," what exactly do you run? If the honest answer is "I grep and guess," you have sampling but no identity.
- What field could you propagate through every hop that you are not propagating today, and what would it cost — nothing, or a rewrite?
- Which of your slow paths were fine when they were written? Name one, and ask what would have caught its drift.

## See also

[[find-code-that-runs-not-code-thats-referenced]] · [[gate-the-release-on-internal-telemetry]] · [[../duo-product/SKILL]]
