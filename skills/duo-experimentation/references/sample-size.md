---
name: duo-experimentation-sample-size
summary: How big, how long; the cost of stopping early and the cost of waiting too long.
metadata:
  internal: true
---

# Sample Size

## Concept

Sample size determines an experiment's resolving power: the minimum effect you could reliably detect. Too small, and the test is statistical noise (you'll see lifts that aren't there and miss real ones). Too large, and you've spent organizational time on a test you could have decided faster. The decision is upstream of the test, not after.

## What Duolingo does

- Tests are powered to detect the minimum effect that would justify the change — typically pre-computed as a function of baseline metric variance and target lift.
- Tests run for at least one full week to absorb day-of-week and weekend effects on retention metrics; many run two weeks for novelty absorption ([[novelty-effects]]).
- Stopping rules are pre-registered: an experiment doesn't get cut short just because the primary metric looks good early.
- High-traffic surfaces (lesson screen, league screen) hit power quickly; low-traffic surfaces (settings) require longer or are decided by qualitative review instead.

## The transferable pattern

Three rules:

1. **Compute power before running.** "We'll see what happens" is not an experiment, it's a sample. The minimum-detectable-effect (MDE) calculation is upstream homework.
2. **Run at least one full cycle.** Weekly behavior cycles, monthly billing cycles, etc. Cutting before a cycle completes biases the result.
3. **Pre-register the stopping rule.** Peeking at the data and stopping when the line crosses zero is the most common silent statistical sin.

A useful heuristic:
- If you can't detect a 1% lift with your sample size, don't run a test for a 1% lift expectation.
- If you'd ship the change at +0.5% but not at +0.0%, your MDE needs to be below 0.5%.

## Apply to your product

- What's the minimum-detectable-effect of your typical experiment? Is it tighter than the lifts your team usually predicts?
- Do you have a pre-registered stopping rule, or do you eyeball it?
- Have you ever stopped an experiment early because it looked good? Was that the right call in retrospect?

## See also

[[ab-test-structure]] · [[hypothesis-design]] · [[novelty-effects]] · [[kill-criteria]]
