---
name: duo-experimentation-kill-criteria
summary: The threshold for stopping an experiment instead of milking it; pre-registered, not negotiated.
metadata:
  internal: true
---

# Kill Criteria

## Concept

A kill criterion is a pre-registered rule for stopping a test. "If primary metric is flat at week 2, kill." "If guardrail breach exceeds 1%, kill." Without explicit kill criteria, tests get milked: stretched longer, segmented further, repeatedly re-analyzed until something looks positive. This is the most common form of organizational p-hacking.

The fix isn't "be more rigorous." It's to commit, in writing, before the data arrives.

## What Duolingo does

Two published kills, both made against the metric the work itself was optimizing:

- **The ads model that kept improving while revenue didn't move.** Duolingo's first in-house-ad model predicted a learner's baseline probability of buying a subscription. Improving it kept improving the model's own offline performance — and stopped increasing total revenue, because it was cannibalizing purchases from other hooks by targeting learners who would have bought anyway. They abandoned the framing and rebuilt XGBoost as a contextual bandit selecting learners for whom the ad *raised* purchase probability most. Source: blog.duolingo.com/machine-learning-ads (Duolingo blog, 2025-03-18; accessed 2026-09-22)
- **The shorter-lessons test.** Duolingo shortened lessons expecting learners would do more of them. Time Spent Learning Well went *down*. They published the failed hypothesis rather than re-cutting the data until it looked better. Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

Operationally: experiments that break code or hurt metrics are paused until fixed rather than read as results, and unsuccessful experiments are shut down at the end of the ramp. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

The transferable lesson from the ads case: **the kill signal has to sit one level above the metric the team is optimizing**, or the failure is invisible. Every offline number said the project was going well.

## The transferable pattern

Three rules:

1. **Pre-register the kill rule.** A criterion decided after seeing the data is not a criterion.
2. **Killed experiments are still valuable.** They update the team's model. A test that produces "no, that doesn't work" is a successful test.
3. **Avoid the post-hoc rescue.** "But did it work for power users on Tuesdays?" — segmenting until you find a positive subgroup is how you get false positives that don't generalize.

The harder discipline: kill the test when it's *trending positive but underpowered*. "It's almost significant" is not a result; it's an underpowered test, and shipping on it is rolling dice with a story.

## Apply to your product

- Of your last 10 experiments, how many were pre-registered with a kill criterion?
- Have you ever extended a test "for one more week" because you wanted the result to be different?
- Is there a current experiment that should be killed under your stated criteria but is being milked?

## See also

[[show-dont-tell]] · [[sample-size]] · [[ship-and-iterate]] · [[unmeasurable-wins]] · [[../duo-product/references/kill-criteria-product]]
