---
name: duo-growth-model-judge-a-campaign-cohort-by-its-day-60-curve
summary: Signup volume measures reach; the day-30 and day-60 curve, and the motivation mix underneath it, measure whether the cohort had a reason to be there.
metadata:
  internal: true
---

# Judge a Campaign Cohort by Its Day-60 Curve

## Concept

Signup volume measures reach. The retention curve measures whether the campaign brought people who had a reason to be there. Those are different questions, and only the second one is worth a budget. Acquisition at a moment of declared intent self-selects for motivation, so the standard heuristic — campaign traffic is low quality — can invert entirely. You only find out by following the cohort past the point where a novelty bump would have faded, and by asking what the arrivals say they came for, because the same signup count can conceal an entirely different population.

## What Duolingo does

Source: blog.duolingo.com/which-countries-are-the-best-at-keeping-their-new-years-resolutions (Duolingo blog, 2016-03-31; accessed 2026-09-22)

- Duolingo tracked everyone who signed up **December 29 to January 4** and compared their active proportion at **5, 30 and 60 days** against the 2015 average cohort, with **95% confidence intervals**. The resolution cohort stayed consistently more active than the typical cohort, **in every country studied, out to 60 days**.
- The **Czech** New Year cohort was **more than 75% more likely to still be active at 30 days** than a typical 2015 cohort. Czech users generally complete **~10% more sessions per day** and are active **3.4 vs 2.6 days per week** versus U.S. users.
- Tension: effect size varied enormously. Even the weakest market studied — **Mexico**, where the drop-off was most dramatic — still beat the 2015 baseline, so a single global average would have hidden both ends of the range.
- Duolingo pairs the spike with a retention mechanic rather than just capturing it: the 2017 resolution research shipped alongside **Language Clubs**, a social nudging and competition feature. Survey detail: **21% of 6,534 adults** across US/Brazil/Mexico named learning a language as a 2017 resolution — but **43.4% in Mexico, 38.6% in Brazil, 11.2% in the US**, with motives split by market (Mexico work/school **36%**, Brazil travel **30.3%**, US self-challenge **23.8%**); run Nov 29 – Dec 3 2016, **1,184 complete responses**. The post concedes the obvious: whether people keep the resolution is another story (blog.duolingo.com/how-do-your-country-age-and-gender-impact-your-new-years-resolutions (Duolingo blog, 2017-01-09; accessed 2026-09-22)).
- Composition moves under external events even when volume looks stable. March/April 2020 vs 2019: **school as primary motivation rose to 27.9% from 22.6%** while **travel collapsed to 12.7% from 19.9%**, with brain training at **15.9%** (blog.duolingo.com/global-language-report-2020 (Duolingo blog, 2020-12-15; accessed 2026-09-22)).
- The stock-versus-flow version of the same point: Duolingo's Romance-language survey calls **Sardinian (>1.5M speakers) endangered** because of language shift, while **Catalan (>9M) is not**, and **Occitan (~110,000)** is severely endangered. Size is decoupled from the health call — though the post gives no transmission-rate figure, so the judgment stays qualitative (blog.duolingo.com/what-are-romance-languages (Duolingo blog, 2025-04-23; accessed 2026-09-22)).

## The transferable pattern

- **Set the verdict date before the campaign runs.** Pick day 30 and day 60, name the baseline cohort you will compare against, and do not declare victory on the signup chart.
- **Report per market or per channel, never pooled.** A global average that beats baseline can contain a channel that is pure churn and one that outperforms your best organic cohort.
- **Ask arrivals what they came for, and watch that distribution over time.** Motivation mix is a leading indicator; the arrival count is a level. A flat count hiding a motivation shift will quietly invalidate your roadmap.
- **Judge a user base by inbound flow, not headcount.** An installed base persists for roughly one generation of users after acquisition has failed, so headcount keeps reporting health long after the mechanism is dead. The rate at which new entrants arrive is the leading indicator.
- **Ship the retention mechanic before the spike, not during.** A high-intent, low-habit cohort is exactly the profile that churns; capturing free demand with nothing to hold it converts it into free churn.

## Apply to your product

- For your last campaign, what was that cohort's retention at day 60 against your normal cohort — and if you cannot answer, what would it take to instrument?
- Which channel in your blended acquisition average is carrying the others, and which is quietly churning behind it?
- What do new arrivals say brought them, and has that mix shifted in the last two quarters while your signup count stayed flat?

## See also

[[arrive-before-the-intention-is-assigned]] · [[event-sharpness-not-size-predicts-the-spike]] · [[../duo-retention/references/churn-diagnostics]]
