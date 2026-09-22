---
name: duo-infra-cost-efficiency-relax-freshness-to-make-caching-legal
summary: Strict freshness forbids caching and forces every read down the expensive path; ask how stale the data may be before optimizing the database.
metadata:
  internal: true
---

# Relax Freshness to Make Caching Legal

## Concept

Before optimizing a slow, expensive query, interrogate the requirement that makes it necessary. Strict freshness forbids caching, which forces every read to hit the expensive path, so identical requests arriving many times a minute each pay full price.

Freshness is usually inherited from an early design decision rather than a measured product requirement — "how stale can this be?" gets asked once, at the start, by someone with no data, and never again. Relaxing it does not make the system faster by itself. It makes caching legal, and the cache does the rest.

## What Duolingo does

Source: blog.duolingo.com/how-i-saved-duolingo-40000year-in-my-summer-internship (Duolingo blog, 2017-09-30; accessed 2026-09-22)

- The old system serving challenge statistics gave **up-to-the-minute accuracy** — a lesson you had just finished fed into your next session's numbers. That requirement was exactly what kept every request hitting the database.
- An intern established that **day-old data was almost as good** for the purpose, extracted the statistics into a **standalone service**, and **cached answers for a day**.
- Results: the database alone had cost **$60,000/year**; the replacement ran at **$53/day versus $163/day** for service, cache, database and infrastructure combined — **over $40,000/year saved**. Query responses got **20x faster**, average latency fell from **0.5s to 20ms**, and database CPU usage dropped by a **factor of 5** over the two-hour cutover.
- **Tension.** The win was a product concession, not an engineering trick — somebody had to agree that a day of staleness was acceptable. It also only paid because the same answers were requested repeatedly; a workload of unique queries would have gained nothing. Note the date, too: this is a 2017 result on 2017 infrastructure, so the method transfers and the exact ratios are illustrative.

## The transferable pattern

1. **Write the freshness requirement down as a number.** "Real-time" is not a requirement, it is the absence of one. Seconds, minutes, or a day — pick one and attach a reason to it.
2. **Ask who would actually notice.** If the answer is "nobody would notice a day," you have just unlocked an order-of-magnitude cache hit rate.
3. **Check request repetition first.** Caching pays in proportion to how often the same answer is asked for. Measure the repeat rate before investing in it.
4. **Extract before you cache.** Pulling the computation into its own service gives the cache a clean boundary and makes its cost visible as its own line item.
5. **Expect latency to be the headline.** Cost is why you started; the millisecond-scale response is what users and colleagues react to, and it is what gets the next one funded.

## Apply to your product

- Name your most expensive read path. What is its real freshness requirement in seconds, and who decided that — or was it just inherited?
- What fraction of requests to that path ask for an answer someone else already asked for in the last hour?
- Which of your surfaces claim "live" in the interface but would be indistinguishable at an hour old?

## See also

[[audit-the-fan-out-not-the-endpoint]] · [[sample-by-entity-not-by-row]] · [[../duo-backend-architecture/SKILL]]
