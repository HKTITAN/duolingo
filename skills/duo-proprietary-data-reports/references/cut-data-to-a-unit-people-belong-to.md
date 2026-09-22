---
name: duo-proprietary-data-reports-cut-data-to-a-unit-people-belong-to
summary: Aggregate numbers about your product are about you; the same rows cut to a place or cohort people identify with are about them, and those get forwarded.
metadata:
  internal: true
---

# Cut the data to a unit people belong to

## Concept

A statistic about your whole product is a statistic about you, and nobody forwards it. The unit of aggregation is the entire design decision. Pick a unit your reader already has an identity or a rivalry about — their state, their city, their borough, their age cohort, their industry — and the same rows stop being a company fact and become a fact about them, which they forward in order to argue with the neighbouring unit. The correlation you find while cutting is what makes it credible rather than merely local.

## What Duolingo does

- The 2017 state-by-state analysis cut **57.8 million US users** by state: **Utah highest at 6.78%** of the population signing up in a year, **Mississippi lowest at 2.17%**. It reported a **Spearman correlation of 0.64** between a state's internet access and its share of signups, and named the regional oddities — Spanish top in all 50 states (**avg 45.4%**), **Japanese 17.4% in Hawaii**, Russian in the top five **only in Alaska, at 5.5%**. The post opens with a quiz-style teaser list of findings so a reader can scan for their own state first.
- Tension in that same dataset: the states with the most signups (Florida, New Jersey, Texas) had the **worst** streak retention, while low-signup states (North Dakota, Montana) had the **best**. Acquisition and habit formation ran in opposite directions across the same geography, so the leaderboard you publish depends entirely on which metric you cut by.
  Source: blog.duolingo.com/the-united-states-of-languages-an-analysis-of-duolingo-usage-state-by-state (Duolingo blog, 2017-10-12; accessed 2026-09-22)
- The 2020 UK edition cut **13 million UK downloads** down to per-borough "most dedicated" leaderboards alongside national rankings: Welsh fastest-growing at **+44% year over year with 1.5M learners**; Scottish Gaelic **570,000 learners in under a year, roughly 10x the native speakers counted in the 2011 census**; UK new-user growth **+132% YoY** after the first lockdown; the UK **11th of 194 countries** by lessons completed.
  Source: blog.duolingo.com/uk-language-report-2020 (Duolingo blog, 2020-12-15; accessed 2026-09-22)
- Regional reports cut by place *and* cohort so one dataset yields dozens of separately quotable facts: English share of learners **Colombia 74%, Mexico 71%, Peru 67%, Brazil 63%, Chile 63%, Argentina 55%, Puerto Rico 44%**; **two of three** learners under 30 in Colombia, Mexico and Peru; **20% of Argentine learners are 50+**, with more over-60s than 50-somethings. Six-month window, late 2021 to early 2022.
- Tension: the post's causal readings — remote workers and retirees explaining a shift among Mexican learners over 50 — are written as suggestions, not findings. Cut data supports a correlation and a plausible story, never proof.
  Source: blog.duolingo.com/latin-america-language-learning-trends (Duolingo blog, 2022-06-29; accessed 2026-09-22)

## The transferable pattern

Your logs are already segmented by something. The question is whether the segment is one your reader has a stake in.

1. **Choose the smallest unit that still clears your privacy floor.** A national average has no owner. A borough, a campus, a metro, a company-size band, a job title — those have someone who will defend them.
2. **Rank the units against each other.** A list of values is a table; a list with positions is an argument, and an argument travels.
3. **Cut by a second axis (age, tenure, plan tier) to multiply the findings.** One dataset crossed two ways produces dozens of facts, each with its own natural audience, from a single extraction.
4. **Report one correlation with an outside variable.** It converts "here are our numbers" into "here is something true about the world", and it is cheap.
5. **Do not let the cut imply a cause.** Two segments can rank inversely on acquisition and on habit. Say the two rankings exist; do not merge them into a story you cannot test.

## Apply to your product

- What is the smallest unit in your data — region, team, account tier, campus, job function — that a reader would call "mine"?
- If you ranked those units against each other tomorrow, which rank would somebody screenshot and send to a rival?
- Which outside dataset (census, public index, industry survey) could you correlate one of your columns against, so the finding is about the world rather than about your dashboard?

## See also

[[growth-relative-to-its-own-base]] · [[the-anomaly-is-the-story]] · [[ship-the-raw-data-and-the-privacy-floor]]
