---
name: duo-infra-cost-efficiency-sample-by-entity-not-by-row
summary: Hash a stable entity key and sort storage by it, so the sample is deterministic, cohorts stay whole, and the engine skips the rest.
metadata:
  internal: true
---

# Sample by Entity, Not by Row

## Concept

Random row sampling fails twice. Per-entity metrics computed from randomly sampled rows are simply wrong, because one entity's events land partly inside and partly outside the sample. And a random filter saves no input/output, because the engine still reads everything before discarding most of it.

Hashing a stable entity key to a sortable value and **physically clustering storage on that column** fixes both. The sample is the same set every time, entities stay whole, and the selected rows are contiguous — so the engine skips the remainder instead of scanning and throwing it away.

## What Duolingo does

Source: blog.duolingo.com/speed-up-data-analysis-sampling-68x (Duolingo blog, 2025-05-23; accessed 2026-09-22)

- For each row they hash the user id into a **sampling value between 0 and 1** and **cluster the table by that column**. A 10% sample is then just `sampling_value < 0.1`, which BigQuery satisfies without touching the remainder.
- On a query spanning two years of lessons: **100% — 68s, $2.67, 2.18 TB scanned**; **10% — 5s, $0.13, 332 GB, 0.12% average error**; **1% — under 1s, under $0.01, 56 GB, 0.17% average and 0.61% maximum error**; **0.1% — 0.57% average and 2.52% maximum error**. A **68x speedup** for well under one percent of error.
- The target was explicit — **sub-10-second interactive queries** — because when answers come back in seconds people ask the follow-up question, and when they take minutes they ask one and stop.
- The motive was growth, not this year's bill. Data is **roughly doubling every year since 2019, to about 13 trillion rows**, and they say plainly that they were not excited about doubling BigQuery spend annually. Buying capacity changes the constant; sampling changes the exponent.
- They then **built the heuristic into the tooling**, which inspects the data volume and automatically recommends a sampling rate.
- **Tension.** BigQuery's built-in table sampling could not be used, because it samples rows randomly rather than consistently. On small datasets the technique costs more accuracy than it buys speed, and it breaks outright for any analysis needing an exact count.

## The transferable pattern

1. **Sample the entity, not the record.** Choose the key your metrics are computed per, hash it, and let the hash decide membership. Every record for a selected entity is in.
2. **Make it deterministic.** The same sample every run means two analyses are comparable, and a surprising result can be re-checked rather than re-rolled.
3. **Sort storage by the sampling column.** Without physical clustering you get a faster aggregation over the same scan. With it you skip the scan — and that is where the money is.
4. **Set a latency target, not a precision target.** Under ten seconds keeps a chain of questions alive. Precision past the second decimal is usually precision nobody uses.
5. **Build the technique into the tool and let it pick the default.** An optional best practice decays toward zero adoption as headcount grows.
6. **Gate it.** Anything billed, reported externally, or audited takes the full scan.

## Apply to your product

- What is the entity your analytics are actually about, and is there a stable key you could hash?
- How long does your most common exploratory query take, and how many follow-ups do people ask before giving up?
- Which of your reports genuinely need exact counts, and which have been exact only because nobody offered them the alternative?

## See also

[[relax-freshness-to-make-caching-legal]] · [[target-waste-not-spend]] · [[../duo-measurement-validity/SKILL]]
