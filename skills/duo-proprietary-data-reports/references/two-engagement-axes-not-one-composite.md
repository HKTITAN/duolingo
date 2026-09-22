---
name: duo-proprietary-data-reports-two-engagement-axes-not-one-composite
summary: Volume-per-period and frequency-of-return answer different questions and can anticorrelate; rank them separately or you hide the cohort that is cramming and about to churn.
metadata:
  internal: true
---

# Two engagement axes, not one composite

## Concept

Intensity and consistency are different metrics that are routinely collapsed into a single engagement score. Volume per period tells you how much value somebody extracted in a burst. Frequency of return tells you whether the product became a routine. They can move in opposite directions, and a composite hides exactly the case you most need to see: the cohort with the best-looking volume and no habit at all, which is at the highest churn risk while topping your leaderboard. Publishing two rankings instead of one costs a column and reveals a population.

## What Duolingo does

- The Language Report ranks countries and US states separately on two named axes — **"hardest working"** (average lessons completed) and **"most dedicated"** (longest streaks and consistent daily use) — and then deliberately analyses the segments that rank high on one and bottom on the other.
- The gap is large even at national scale: the **US ranked 68th globally for hardest working but 37th for most dedicated**. The extreme case is starker still — **Puerto Rico ranked #1 for hardest working and #1 for LEAST dedicated** in the same edition. A single composite would have averaged those two ranks into something meaningless.
- The reading offered for the Puerto Rico inversion is visitors cramming activity into a short trip. That is inference from the shape of the data, not an established cause, and the post presents it as an explanation rather than a finding — which is the right register for it.
  Source: blog.duolingo.com/us-language-report-2020 (Duolingo blog, 2020-12-15; accessed 2026-09-22)
- The same two-axis instinct appears in geographic cuts, where the two rankings disagree across the same map: the states with the most signups (Florida, New Jersey, Texas) had the **worst** streak retention, while low-signup states (North Dakota, Montana) had the **best**. Acquisition volume and habit formation ranked inversely across identical geography.
  Source: blog.duolingo.com/the-united-states-of-languages-an-analysis-of-duolingo-usage-state-by-state (Duolingo blog, 2017-10-12; accessed 2026-09-22)
- Tension: two rankings produce two leaderboards and two possible headlines, and a segment that wins one will quote that one. You lose control of which number gets repeated. The alternative — one tidy composite — buys that control by deleting the finding.

## The transferable pattern

Pick two axes that can disagree, and publish them unmerged.

1. **Axis one: volume per active period.** How much did this segment do when it showed up.
2. **Axis two: return frequency or consistency.** How reliably did it show up at all.
3. **Never average them into a score.** A composite is defensible only if the inputs correlate, and if they correlated you would not need both.
4. **Report the inversions explicitly.** The segment ranked first on volume and last on consistency is the most useful row in the report, both internally as a churn warning and externally as the thing people share.
5. **Offer a mechanism, labelled as a guess.** Short-lived populations — visitors, seasonal users, trial cohorts, deadline-driven teams — produce high volume and no habit. Say which one you think it is and mark it as a hypothesis.
6. **Use the inversion internally before you publish it.** A segment topping your volume leaderboard while bottoming your consistency leaderboard is a retention forecast, not a trophy.

## Apply to your product

- Do you have a single engagement score, and if so, would its two biggest inputs ever point in opposite directions?
- Which of your segments is highest on volume and lowest on return frequency — and is that segment currently described internally as one of your best?
- What short-lived population (trial, seasonal, deadline-driven, visiting) could be manufacturing your best-looking volume numbers?

## See also

[[growth-relative-to-its-own-base]] · [[the-anomaly-is-the-story]] · [[cut-data-to-a-unit-people-belong-to]]
