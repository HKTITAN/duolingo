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

- **Power is bought by ramping rollout, not by waiting.** Duolingo's growth guideline is to roll experiments out to as many learners as you can, as quickly as you can, and the stated reason is exactly the sample-size argument: to have enough confidence in the results they need a large number of users treated into the experiment. Parking a test at a small rollout while the team moves on to the next thing is named as the common failure. Source: blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22)
- **Launch on your biggest platform first** — same post, same logic. If Android has significantly more users, running there first and porting to iOS reaches decision power sooner than the reverse.
- **Uncertainty is rendered, not requested.** The internal A/B suite shows confidence intervals and time series by default, across the thousands of A/B tests Duolingo runs every year. Source: blog.duolingo.com/duolingos-secret-weapon-our-beautiful-and-powerful-analytics-tools (Duolingo blog, 2021-03-22; accessed 2026-09-22)
- Tests run long enough to absorb day-of-week cycles, and longer still for changes prone to novelty ([[novelty-effects]]) — where Duolingo's own decay estimate came from a 34-day window, not a one-week one.

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

[[ab-test-structure]] · [[hypothesis-design]] · [[novelty-effects]] · [[kill-criteria]] · [[probes-inside-the-product]]
