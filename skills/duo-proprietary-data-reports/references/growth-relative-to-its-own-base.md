---
name: duo-proprietary-data-reports-growth-relative-to-its-own-base
summary: Absolute rankings re-describe where your users already are; percent change against each segment's own prior activity is the only cut that can show something moved.
metadata:
  internal: true
---

# Growth relative to its own base

## Concept

An absolute leaderboard of your segments is determined by scale that already existed before the period you are measuring. Your biggest markets top it by construction, every edition, and the list therefore carries almost no information about whether anything changed. The alternative is to divide each segment's activity in the measured window by that same segment's activity in a prior window, and rank the ratios. That version can say a campaign worked somewhere you had no presence, or that a market you consider core did nothing this period. Publish both, and treat the disagreement between the two rankings as the finding.

## What Duolingo does

- Duolingo ranked New Year signups two ways: absolutely, and as percent increase over each country's own **October to December** active base. The absolute list was the usual one — the **U.S., Brazil and Mexico** on top, as always. The proportional list was completely different: **India, Taiwan and Yemen** led with roughly **+6%** proportional increases, while **Mexico, third in absolute numbers, was among the three worst proportionally**. **Germany jumped seven rank positions** relative to its usual absolute placement, and **China fell from 8th to 12th**.
- The same post cautions against reading those proportional rankings as clean product signal without local context: China's weak showing is partly explained by Chinese New Year falling on **8 February** that year, so the segment's own resolution moment sat outside the measured window entirely.
  Source: blog.duolingo.com/which-countries-are-the-best-at-keeping-their-new-years-resolutions (Duolingo blog, 2016-03-31; accessed 2026-09-22)
- Regional reports apply the same instinct to individual segments rather than a whole leaderboard: Welsh reported as **+44% year over year** and Scottish Gaelic as **570,000 learners in under a year, roughly 10x the native-speaker count in the 2011 census**, with UK new-user growth at **+132% year over year** after the first lockdown. Each figure is a ratio against that segment's own prior base or against an outside denominator, not a position on an absolute list.
  Source: blog.duolingo.com/uk-language-report-2020 (Duolingo blog, 2020-12-15; accessed 2026-09-22)
- Tension: ratios explode at small denominators. A segment with a tiny base can post a spectacular percentage from a handful of events, which is why a relative ranking is only publishable on top of the minimum-cell-size floor. Relative and absolute are a pair; neither is honest alone.

## The transferable pattern

Every segment ranking you publish should exist in two versions.

1. **Compute each segment's change against its own prior-period base**, not against the global total and not against the largest segment.
2. **Publish both lists side by side and name the disagreements.** The segment that is third absolutely and bottom-three proportionally is the most interesting row in either table.
3. **Apply the minimum-base floor before ranking ratios**, or your top ten becomes a list of rounding artifacts.
4. **Check the calendar of each segment before attributing a ratio to your own work.** A local holiday, fiscal year, school term or regulatory date sitting inside or outside your window will move a segment more than any campaign you ran.
5. **Track rank movement between the two lists.** "Moved up seven places relative to its absolute position" is a compact way to say a segment overperformed its own scale.

## Apply to your product

- Take your top-ten segment list: how much of it is explained purely by where your users already were before the period started?
- Which segment in your data is large in absolute terms and flat or shrinking against its own base — and does anyone on the team know that?
- What is the minimum base a segment needs before you would publish a percentage for it, and can a small segment currently reach your top ten on a handful of events?

## See also

[[report-movement-not-levels]] · [[cut-data-to-a-unit-people-belong-to]] · [[two-engagement-axes-not-one-composite]]
