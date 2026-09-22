---
name: duo-proprietary-data-reports
description: Turn behavioural logs you already hold into a recurring public report that journalists, researchers and buyers cite instead of discounting. Covers cadence and a frozen measurement window, which unit to cut the data to so readers find themselves in it, reporting movement rather than levels, ranking growth against each segment's own base, separating intensity from consistency, publishing the exclusions and the minimum cell size, shipping the raw rows behind a privacy floor, and explaining anomalies with outside sources. Use when someone asks you to turn usage data into earned media, when planning an annual index or a state-of-the-category report, when a data release got ignored, or when a methodology note has to be written. Triggers on "annual data report", "state of X report", "turn our usage data into a story", "data PR", "make our numbers citable".
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# duo-proprietary-data-reports

If your product has scale, you are sitting on a dataset no journalist or academic can obtain. This skill is about converting it into a **recurring** public report with a fixed window and published exclusions — the format that gets cited rather than discounted.

Two things separate a citable series from a press release with a statistic in it. The first is repetition against an unchanged window, which is what lets any edition report a change instead of a level. The second is disclosure, which is what lets an outsider attribute your number without hedging it.

This skill owns the recurring program. It does not own one-shot publishing triggered by a news moment, a cultural event or a commissioned survey — that belongs to the sibling skill `duo-timely-data-publishing`. It also does not own how the motivation or segment fields inside the report were collected and interpreted internally, which belongs to `duo-motivation-segmentation`.

## Decide what you are measuring

Get the shape of the series right before the first edition, because the first edition sets the contract.

- [[references/fixed-window-repeated-forever]] — freeze the window, the unit, the floor and the metric definitions; the sixth edition is worth more than the first because every prior one became a baseline.
- [[references/cut-data-to-a-unit-people-belong-to]] — aggregate numbers are about you and nobody forwards them; the same rows cut to a state, city, borough or cohort are about the reader.
- [[references/two-engagement-axes-not-one-composite]] — volume per period and frequency of return can anticorrelate, so rank them separately or you hide the cohort that is cramming and about to churn.

## Decide how you rank it

The same dataset produces a boring table or a story depending on what you divide by and what you lead with.

- [[references/report-movement-not-levels]] — the top of the leaderboard is already known to the reader; the crossover is the only claim a longitudinal dataset can make.
- [[references/growth-relative-to-its-own-base]] — absolute rankings re-describe where your users already were; percent change against each segment's own prior activity is the version that can show something moved.
- [[references/the-anomaly-is-the-story]] — a ranking confirms what everyone assumed; an oddity explained with an independent outside source turns a private metric into a claim about the world.

## Decide what you disclose

Disclosure is not a legal chore appended at the end. It is the mechanism that makes the numbers quotable.

- [[references/publish-the-exclusions-with-the-findings]] — the exact window, the aggregation unit, the sample floor, which fields are self-reported, and the supply bias your own catalogue introduced.
- [[references/ship-the-raw-data-and-the-privacy-floor]] — a linked file of the underlying rows plus a hard minimum-count-per-cell rule, which make each other possible.

## Sibling skills

- [[../duo-growth/SKILL]] — the earned-media strategy this report serves, and the other ways a brand buys attention without buying it.
- [[../duo-efficacy-measurement/SKILL]] — whether the metric you are about to publish measures what you claim it measures. Settle that before an external audience sees it.
- [[../duo-experimentation/SKILL]] — the internal discipline behind the same numbers, including guardrails and what counts as evidence.
- [[../duo-localization/SKILL]] — republishing each edition in your users' languages, which is what makes the report citable outside your home market.

## Sources

Distilled from blog.duolingo.com — 12 posts spanning 2016-03-31 to 2025-12-01, each cited in dated form inside the node that uses it; see `scripts/sources.json` for the full bibliography.
