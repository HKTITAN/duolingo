---
name: duo-production-reliability-continuous-qa-for-always-on-systems
summary: A system that runs continuously has no after in which to audit, so quality needs statistical monitoring against trend and seasonal baselines with tiered human experts in the loop.
metadata:
  internal: true
---

# Continuous QA for always-on systems

## Concept

Batch quality assurance assumes a discrete window: something is administered, it ends, and then you audit what happened. A system available on demand, globally, at all hours, has no after. Drift, gaming and degradation of individual components accumulate silently in the gaps between audits, and by the time a periodic review runs, the affected population has already passed through. The only method that fits is to model what typical looks like over time — including seasonality, since a 24/7 global system has real daily and weekly shape — and alert on deviation from it. That produces anomalies, not answers, so the second half of the design is a routing structure that puts the right human on each one without requiring every human to be an expert.

## What Duolingo does

Sources: blog.duolingo.com/aquaa (Duolingo blog, 2021-03-18; accessed 2026-09-22) and blog.duolingo.com/what-is-online-proctoring (Duolingo blog, 2022-07-21; accessed 2026-09-22)

- **AQuAA** (Analytics for Quality Assurance in Assessment) is an interactive dashboard blending educational data mining with psychometric theory. It **continuously monitors the interaction between items, the adaptive algorithm, and the population taking the test**, flags atypical patterns, and routes them to psychometricians for expert review.
- The loop closes: insights from monitoring feed back into how new items are developed, so the detector improves the thing it watches rather than only guarding it.
- Human review is **tiered by expertise and routed by complexity**, not uniformly staffed: proctors work in **three tiers** — identity verification and behavioral flags, applied-ESL professionals reviewing the spoken interview, and senior experts handling the most complex cases — with escalation between them. Every tier takes **several weeks of training** before independent review.
- That tiering is what makes on-demand review economically possible at all. Most cases are routine and need speed and pattern recognition; a minority need deep judgment that is expensive to hire and slow to train. Routing by difficulty spends scarce expertise only where it changes the outcome.
- Tension, stated by their own scientist: monitoring everything, everywhere, all the time is **a huge undertaking**. And the existing **International Test Commission guidelines were not designed for continuous administration**, so Duolingo had to research and deliberate every indicator itself. Adopting this means accepting that you are writing the standard, not applying one.

## The transferable pattern

1. **Ask whether your system has an after.** If it does not, periodic audit is not a weaker version of monitoring — it is a different method that does not apply.
2. **Baseline on trend and seasonality, not on a fixed threshold.** A global always-on system has legitimate daily and weekly shape. Static thresholds alarm on Tuesday morning and miss the real drift.
3. **Watch the interaction, not just the components.** The failure usually lives in how the algorithm, the content and the current population combine, which none of the three shows on its own.
4. **Design the escalation path before the detector.** An anomaly with no owner is a dashboard nobody opens. Decide who interprets each class of flag.
5. **Tier your reviewers and route by difficulty.** Uniform seniority is unaffordable and uniform juniority is unsafe. Escalation is cheaper than either.
6. **Feed findings back into production of the thing being watched.** Otherwise you have built a guard rather than an improvement loop.
7. **Budget it honestly.** Continuous monitoring is a standing cost with standing staffing, and you may be inventing the indicators yourself because your situation postdates the guidance.

## Apply to your product

- Does your quality process have an audit window that assumes an end, while the product itself never stops? Name the gap in hours.
- What is the seasonal shape of your normal, and would your current alerts fire every week because of it?
- When an anomaly is flagged, who looks at it, what can they decide alone, and to whom do they escalate?

## See also

[[datasets-are-production-software]] · [[verify-controls-instead-of-asserting-them]] · [[../duo-product/SKILL]]
