---
name: duo-ml-in-production-ship-coverage-as-the-progress-metric
summary: Roll a personalization model out as a growing share of eligible sessions, and publish the coverage curve as the progress metric while quality is still improving.
metadata:
  internal: true
---

# Ship Coverage as the Progress Metric

## Concept

A model that decides what each user sees fails in ways that only appear on real traffic, and only on certain slices of content. No offline evaluation surfaces them, because the failures are about the interaction between the model and the specific shape of a slice — not about average accuracy.

So the rollout unit should be the slice, not the population. Expand to one slice, watch it, expand to the next. This also solves a reporting problem that quietly wrecks long model projects: for months there is no headline quality number that moves legibly, which makes the work look stalled. "Percent of sessions this now handles" is a real, honest, monotonically improving number you can publish while quality is still in flux.

## What Duolingo does

Source: blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain (Duolingo blog, 2020-10-07; accessed 2026-09-22)

- Birdbrain, the model that personalizes exercise difficulty per learner, was incorporated **"little by little" into more lesson types over seven months** rather than cut over at once.
- The company's headline progress graph was **percent of lessons personalized over time**: **0% in March 2020, about 5% in July, over 20% by October 2020.**
- Read the shape of that curve honestly. After seven months of work it covered roughly a fifth of sessions — and that was presented as the achievement, because each lesson type added was one more slice validated on live traffic.
- The coverage metric is also what made the work legible outside the team during a period when the underlying model was still being tuned.

## The transferable pattern

Define the unit of expansion before you start, and make it the thing your model's behaviour actually varies over — a content type, a surface, a customer tier, a workflow. Then the rollout is a list, each entry gets validated, and "which slices are live" is a shared artifact anyone can read.

Publish coverage as the progress metric, with two guardrails so it does not become a number gamed at the expense of the thing it is proxying for:

1. **Coverage is a proxy, not the goal.** Pair every coverage report with the quality metric on the slices already live. Coverage rising while per-slice quality falls is a worse outcome than a slower curve.
2. **A slice can come back out.** If the curve can only go up, teams stop removing slices that are underperforming. Make regression a normal, unembarrassing move.

The staged approach costs you calendar time and a period where the system behaves differently for different users — which is a support burden and a measurement complication, since a metric computed across the whole population is now a blend of two regimes. Segment your reporting by whether a slice is live, or you will read a rollout artifact as a product result.

## Apply to your product

- What is the natural slice your model's behaviour varies over, and could you name the full list of slices today?
- While quality is still improving, what number does your team publish as progress — and is it honest, or is it a chart of effort?
- Can a slice be rolled back out of your system without it reading as a failure, and has that ever actually happened?

## See also

[[resolve-identity-before-you-trust-the-funnel]] · [[replace-the-rule-tree-with-one-learned-decision]] · [[../duo-experimentation/references/ship-and-iterate]]
