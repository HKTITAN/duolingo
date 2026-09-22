---
name: duo-growth-model-movable-metrics-have-a-shelf-life
summary: Succeeding at a segment metric grows that segment until it is the new monolith; plan the successor while the metric still works.
metadata:
  internal: true
---

# Movable Metrics Have a Shelf Life

## Concept

A metric earns its keep by isolating a small, behaviourally coherent group. Then you succeed at it — and success means moving more and more users into that group. Eventually the group contains nearly everyone, its average hides exactly the variation you decomposed the aggregate to expose, and you are back where you started with a new name on the chart. The decay is caused by the win, not by neglect. So the successor has to be planned while the current metric is still working, not after it visibly stops.

## What Duolingo does

Source: blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)

- The Growth Model was built because DAU had stagnated from **2018**. Years of driving Current User Retention Rate worked — and by **2023 about 90% of DAU sat in the single Current User state**.
- That recreated the original 2018 problem exactly: one bucket holding almost everybody, its average uninformative, no resolution left to target.
- The stated next step is to move from the top-down, hand-designed state machine to **bottom-up unsupervised segmentation** — let clusters fall out of behaviour instead of being declared in advance.
- Tension they concede: bottom-up clusters are **less interpretable and harder to set goals against** than seven named states, and goal-setting accuracy had become *more* important since the company went public. The better model is the worse management tool.

Cheaper reads that surface structure before you build clustering, from the same company's published data:

- **Anomalies as segment discovery.** A large number of people learning Swedish *inside Sweden* made no sense under the assumed user model; read as a hypothesis it identified immigrant and refugee learners, and led to partnerships with the IRC and UNHCR. Confirmed later: Danish is #2 in Denmark, Norwegian #2 in Norway, and half of those learners study for work or school. Duolingo concedes it cannot directly confirm who these users are — which is why it needed local partners (blog.duolingo.com/our-commitments-to-helping-refugees (Duolingo blog, 2021-06-17; accessed 2026-09-22); **only 3% of refugees worldwide enroll at university vs 37% globally**).
- **Age composition as trajectory.** **83% of U.S. learners of Japanese, Korean or Chinese are under 30 and 42% are 13–17**, versus **65% and 28%** for Spanish/English/French — a decade-younger skew that preceded Japanese reaching **#4 overall in the U.S.** (blog.duolingo.com/special-report-asian-and-pacific-language-trends-on-duolingo (Duolingo blog, 2021-05-13; accessed 2026-09-22)).
- **Intrinsic motivation as the beachhead for adjacent products.** Latin learners — a cohort with almost no practical payoff — were the most likely of any to also take up chess, math and music: **19%+ chess, 14% math, 13% music** (blog.duolingo.com/2025-duolingo-language-report (Duolingo blog, 2025-12-01; accessed 2026-09-22)).

## The transferable pattern

- **Date your metric.** When you adopt a segment-level target, write down the share of users currently in that segment. When that share crosses roughly two thirds, the metric is going blunt and you need a successor in flight.
- **Expect the replacement to be worse to manage.** A discovered segmentation resolves behaviour better and plans worse. Budget for the loss of interpretability instead of being surprised by it.
- **Mine the residue first.** Before building clustering, read the three cheapest structure signals you already have: data points that contradict your assumed user model, age or tenure skew inside a category, and which cohorts adopt your adjacent offerings.
- **A statistical oddity is a hypothesis about who is using the product,** not noise. It is the cheapest segment-discovery method available, and it costs one analyst-day.

## Apply to your product

- What share of your users currently sit in the state your headline metric targets? If it is most of them, what is that metric still telling you?
- Which number in your dashboard makes no sense under your assumed user model — and what kind of person would make it make sense?
- If you segmented today's users by age or tenure rather than by plan or volume, which segment is a decade off your average, and what does it want?

## See also

[[decompose-a-flat-metric-into-state-transitions]] · [[judge-a-campaign-cohort-by-its-day-60-curve]] · [[../duo-experimentation/SKILL]]
