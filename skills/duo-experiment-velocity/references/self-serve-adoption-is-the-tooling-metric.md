---
name: duo-experiment-velocity-self-serve-adoption-is-the-tooling-metric
summary: Judge an internal analytics platform by how many non-analysts voluntarily use it, because every unanswerable self-serve question becomes a queued request.
metadata:
  internal: true
---

# Self-Serve Adoption Is the Tooling Metric

## Concept

Internal analytics platforms are usually evaluated on capability — what can it compute, what can it join, how fast does it scan. That is the wrong denominator. Decision throughput is capped by the number of people who can get an answer without asking anyone, because every question a product manager or designer cannot answer alone turns into a ticket that waits behind an analyst's real work. Most of those questions are never asked at all; people quietly guess instead, and the guess is invisible in any usage dashboard. So the metric that predicts how fast an organisation learns is voluntary adoption by non-specialists, and the design property that produces it is ease, not power. This is also the strongest argument for building in house against mature vendor tooling — you cannot buy fit with your own concepts.

## What Duolingo does

Source: blog.duolingo.com/duolingos-secret-weapon-our-beautiful-and-powerful-analytics-tools (Duolingo blog, 2021-03-22; accessed 2026-09-22)

- Duolingo built its own segmentation, dashboard, retention, funnel and experiment-analysis tools rather than assembling them from vendors, and frames the suite as a competitive advantage rather than internal plumbing.
- The stated evidence for the build decision is a comparison, not a feature list. A data scientist who had previously worked at Spotify and Facebook — companies with large dedicated data-tooling teams — described Duolingo's tools as just as powerful and flexible, but easier to use.
- Defaults carry the ease. The A/B analysis surface shows confidence intervals and time series by default, so a non-specialist reading a result sees the uncertainty and the shape over time without knowing to ask for either.
- The load this supports is real — **thousands of A/B tests every year, with hundreds running simultaneously**.
- On when to build the metric at all, Duolingo's cheaper move came first. An intern manually computed daily resurrection rates over **a couple of months of history** from the behaviour database, established the benchmarks by hand, and only then automated the metric onto the internal dashboard — **the whole sequence took a couple of weeks** (blog.duolingo.com/back-from-the-brink-what-duolingo-learned-about-its-resurrected-users (Duolingo blog, 2017-08-30; accessed 2026-09-22)).
- The tension worth naming — an in-house suite is a permanent staffed commitment. Duolingo can carry a data-tooling team; a ten-person company that copies the decision buys itself a second product to maintain.

## The transferable pattern

- **Count the humans, not the features.** How many people outside the data function opened the tool last week and got an answer? That number is your learning capacity.
- **Watch for the silent failure.** Unanswerable questions rarely become tickets. They become opinions asserted in meetings, so a short request queue can mean the tool is unused rather than sufficient.
- **Put the statistics in the defaults.** Uncertainty and time series shown without being requested prevent the most common non-specialist error, which is reading a point estimate as a fact.
- **Ease beats power at the margin.** A tool that answers eighty percent of questions and is used by forty people produces more decisions than one that answers everything and is used by four.
- **Compute it by hand before you instrument it.** A backfilled query over history is cheap and reversible; instrumentation is expensive and permanent. The manual pass turns "should we track this?" from an argument into an observation, and often shows the cohort is too small to matter.
- **Build in house only where your concepts are unusual.** The case for building is fit and usability for your own team, not capability — and it obliges you to staff the tool forever.

## Apply to your product

- Name the last five questions your team answered with a guess. Which of them could a non-analyst have answered alone in your current tooling?
- What does a typical person see first when they open your experiment readout, and does it show uncertainty without being asked?
- Which metric are you about to instrument, and what would a hand-computed version over the last two months of existing data cost you instead?

## See also

[[build-tools-that-can-embarrass-you]] · [[take-the-domain-owner-off-the-engineering-queue]] · [[../duo-measurement-validity/SKILL]]
