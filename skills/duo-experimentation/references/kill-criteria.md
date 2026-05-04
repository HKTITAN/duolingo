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

- Every experiment registers a stopping rule before it starts.
- The rule covers both the *win* condition (primary metric clears MDE with confidence) and the *kill* condition (primary flat past X duration, or guardrail breached).
- Killed experiments are reviewed for learnings even though they won't ship — the goal is to update the team's prior, not to recover the test.
- "Let's let it run another week" is not a default; it requires a stated reason that wasn't part of the original criteria.

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

[[show-dont-tell]] · [[sample-size]] · [[ship-and-iterate]] · [[../duo-product/references/kill-criteria-product]]
