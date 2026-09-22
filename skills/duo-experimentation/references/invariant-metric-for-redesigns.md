---
name: duo-experimentation-invariant-metric-for-redesigns
summary: A structural redesign must be judged on the terminal outcome, because the proxies it was tuned for are not comparable across architectures.
metadata:
  internal: true
---

# The Invariant Metric for Redesigns

## Concept

A structural redesign changes the route users take through the product. That means it changes which proxy metrics can move at all, and by how much. Sessions, completion rate and time-on-surface are defined relative to an architecture; compare them across two architectures and you are comparing two different definitions. The one measure that survives the change is the end state the product exists to deliver — whatever the user is supposed to be able to do afterwards. That is the only fair comparator, and it is the one that catches the worst failure mode: a redesign that lifts engagement while lowering the outcome, which looks like a win on every dashboard for about a year.

## What Duolingo does

In 2022 Duolingo replaced its branching "tree" — where learners chose their own route through optional skills — with a single linear "path." This was not a UI refresh; it removed user choice over sequence, which invalidated comparison on any completion- or navigation-shaped metric.

Duolingo compared cohorts on the old and the new design using reading and listening proficiency scores rather than retention alone. Path learners scored higher than tree learners on both, and exceeded the expected proficiency level for their point in the course. Source: blog.duolingo.com/results-duolingo-efficacy-studies (Duolingo blog, 2024-09-26; accessed 2026-09-22)

Two limits to hold onto:

- Cohorts on the old and new design are separated in time, not randomized. Everything else that changed between the two periods is baked into the result.
- The published figures are directional — higher, above expectation — without a gap size. The comparison design is the transferable part; the magnitude is not auditable.

Mark as retired: the tree is gone. A node, doc or dashboard still describing branching skill selection as current is describing a system Duolingo replaced.

## The transferable pattern

1. **Before a structural change, name the invariant.** The measure that would mean the same thing under either architecture. Usually it is the user's end capability or the job they came to complete, never a funnel step.
2. **Freeze it in advance.** Choosing the comparator after seeing the results is how a regression gets explained away.
3. **Accept the weaker design.** Redesigns rarely run as clean A/B tests at full scale; a pre/post cohort comparison on the invariant beats a rigorous A/B test on a metric that no longer means the same thing.
4. **Set a re-read date.** A year out, check the invariant again against the pre-redesign cohort. Structural changes have slow second-order effects.

## Apply to your product

- What is the one measure in your product that would mean the same thing before and after a full navigation rewrite?
- The last big redesign you shipped — was it judged on that measure, or on the funnel steps the new design created?
- Do you still have a cohort on the old architecture, or instrumented history, that would let you run the comparison today?

## See also

[[metric-selection]] · [[guardrail-metrics]] · [[outcome-not-engagement]] · [[quasi-experiments]]
