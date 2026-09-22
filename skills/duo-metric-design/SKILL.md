---
name: duo-metric-design
description: Choose, weight and defend the single number your team is graded on, so that moving it means users actually got value rather than merely spent time. Covers putting activity weights inside the formula instead of a memo, threshold-percentage goals versus aggregate totals, pairing a growth metric with a daily-readable quality proxy, refusing to score a vague goal and decomposing it instead, giving producers leading indicators while they author, per-unit quality maps, and ranking a feedback queue larger than you can read. Use when someone asks what metric a team should own, how to pick a north star, why the number went up while nothing actually improved, how to build a counter-metric next to a growth metric, how to stop metric gaming, how to keep a fast lever from beating a slow structural fix, or how to triage a feedback firehose.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Metric Design — Map of Content

The metric a team is graded on is the only strategy document that gets read every week. This skill is about choosing that number well — how to weight it, where to set its bar, what counter-metric sits beside it, and what caveats must travel with it — so that moving the number means users actually got value.

Scope note: this is the dashboard your own team argues over. Scores you publish *to* users or outsiders — ratings, certifications, proficiency levels, trust scores — have to survive gaming by the people being scored and belong elsewhere.

This skill is a **graph**. Scan the descriptions, follow only the `[[wikilinks]]` you need.

## Shaping the number itself

- [[references/put-the-weight-in-the-formula-not-the-memo]] — when some actions are worth more than others, encode the ratio as a coefficient; a stated priority changes nothing.
- [[references/threshold-percentage-not-aggregate-total]] — grade on the share of users clearing a meaningful bar, not the sum, so a power-user cohort cannot absorb the whole gain.
- [[references/pair-every-growth-metric-with-a-quality-proxy]] — a growth metric alone drifts toward whatever is cheapest to repeat; the counterweight has to be readable daily.

## Deciding what is measurable at all

- [[references/refuse-to-measure-the-vague-goal]] — decline to score the unfalsifiable word in your positioning; decompose it into named sub-competencies and publish the weak one too.

## Getting numbers to the people who can act on them

- [[references/leading-indicators-for-the-people-doing-the-work]] — a metric that arrives after the work is finished cannot change the work; move it into the authoring surface.
- [[references/per-unit-quality-map-not-aggregate-score]] — an overall score says something is wrong; a color-coded per-unit map says which part to open.
- [[references/score-the-feedback-queue-do-not-drain-it]] — past the volume you can review, rank by predicted validity and mine the rejected majority for comprehension failures.

## Reading order

Start with [[references/pair-every-growth-metric-with-a-quality-proxy]] if you are choosing a north star from scratch — it explains the failure mode that every other node here is a response to. Start with [[references/score-the-feedback-queue-do-not-drain-it]] if the immediate problem is a backlog rather than a definition.

## Sibling skills

- [[../duo-measurement-validity/SKILL]] — whether a number means what you think it means, before you grade anyone on it.
- [[../duo-efficacy-measurement/SKILL]] — the slow, rigorous outcome study that a daily proxy is standing in for.
- [[../duo-experimentation/SKILL]] — the A/B machinery your metric has to be readable inside.
- [[../duo-product/SKILL]] — "take the long view" as the stated rule that keeps a fast lever from beating a slow mechanic.

## Sources

blog.duolingo.com — time-spent-learning-well, product-principles, can-duolingo-make-me-fluent, how-were-improving-duolingos-course-creation-process, how-user-reports-improve-course-content, chess-points-of-pieces, duolingo-leagues-leaderboards, duolingo-english-test-readiness, what-languages-do-they-study-in-france
