---
name: duo-experimentation-probes-inside-the-product
summary: Embed the measurement inside ordinary usage instead of building a separate test surface — honest data at volume, for the cost of one item.
metadata:
  internal: true
---

# Probes Inside the Product

## Concept

A separate assessment surface has two defects that no amount of design fixes. Selection bias: only motivated users open it, so you measure your best users and call it your population. Observer effects: people behave differently when they know they are being graded, so you measure their effort, not their state. A probe embedded in ordinary usage — an item indistinguishable from normal content — avoids both. It samples everyone in their natural state, and it costs one extra unit of work rather than a whole surface with its own navigation, empty state and adoption problem.

## What Duolingo does

Duolingo slips a Review Exercise into ordinary lessons: an item randomly sampled from material the learner saw earlier. Answering it correctly is evidence the earlier material was retained. To the learner it is just another question in the lesson. Source: blog.duolingo.com/review-exercises-help-measure-learner-recall (Duolingo blog, 2021-12-02; accessed 2026-09-22)

The volume is the point: roughly **300,000 Review Exercise answers every day**. That is a retention measurement running continuously across the whole population, with no assessment surface, no opt-in and no completion rate to worry about.

The stated limit is as important as the number. A single item is a noisy signal for any individual learner — one answer confuses recall with luck, attention and item difficulty. The instrument is trustworthy only in aggregate, which means it measures the *curriculum*, not the person. Duolingo uses it to ask which material is being retained and which is not, and pairs it with quasi-experimental analysis to attribute the difference to specific product decisions rather than treating it as a per-user score.

Tension: embedded probes displace real content. Every probe is an item of ordinary experience you took away to spend on measurement, so the sampling rate is a budget, not a free parameter — and a probe that becomes recognizable stops being a probe.

## The transferable pattern

1. **Find the unit of ordinary work** in your product — a step, a card, a question, a confirmation — and make the probe one of those, not a new surface.
2. **Sample randomly and sparsely.** Random selection is what makes the aggregate unbiased; sparseness is what keeps the cost invisible and the probe unrecognizable.
3. **Read it at population level only.** Never surface a single probe result as a per-user score, and never let it gate anything — the moment it has consequences, both the honesty and the disguise are gone.
4. **State the noise floor.** Decide up front how many observations you need before a difference means anything, so nobody reads a daily wobble as a finding.

Anti-pattern: building a dedicated quiz, survey or health-check surface, then reporting its results as if the 4% who completed it represented everyone.

## Apply to your product

- Where in your core flow could one unit of ordinary work double as a measurement without the user noticing a mode change?
- What are you currently inferring about all users from a surface only your most engaged users ever open?
- If you added a probe, how many observations would you need before a week-over-week change meant something?

## See also

[[baseline-at-first-contact]] · [[quasi-experiments]] · [[metric-selection]] · [[sample-size]]
