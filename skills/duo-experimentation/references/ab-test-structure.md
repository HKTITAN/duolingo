---
name: duo-experimentation-ab-test-structure
summary: Variant/control, randomization unit, exposure rules; the structural choices that decide whether a test is honest.
metadata:
  internal: true
---

# A/B Test Structure

## Concept

An A/B test is a comparison between a control (current behavior) and one or more variants (proposed change). The structure decisions — who gets what, when they're exposed, what counts as "exposed" — determine whether the result is honest or contaminated. Most flawed experiments are flawed at this layer, before the data even arrives.

## What Duolingo does

Duolingo's internal experiments service forces four structure decisions at setup time — what the experiment does, how many arms and what they look like, who is eligible, and what results are expected. Over 2,000 experiments ran through it in its first three years, with a few hundred live simultaneously in a given week. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

- **Arms encode the real decision, not just on/off.** Adding Leaderboards to desktop collided with the existing Friends feature — both compared progress — so the test ran two branches: Friends kept in the sidebar alongside Leaderboards, or Friends moved to the profile page. An on/off arm would have confounded the feature's value with the damage from the collision.
- **Eligibility is a confound, and scoring has to correct for it.** Duolingo's notification bandit compares each template only against other templates sent to *the same type of learner*, because some are only eligible with a streak wager or only sendable on Mondays — and many learners complete a lesson whatever arrives, especially long-streak ones, which hands those templates an unearned score. Source: blog.duolingo.com/hi-its-duo-the-ai-behind-the-meme (Duolingo blog, 2020-09-03; accessed 2026-09-22)
- **Segment mix decides what a test can even see.** Vietnam's new-learner registration rate ran ~15% below the world average. The cause was the separate under-13 registration flow — 62% registration vs 90% for everyone else, equally broken everywhere, but visible only where under-13s were 2.5x their global share of new learners. The country was the detector, not the cause; the fix shipped globally. Source: blog.duolingo.com/lessons-from-asia-turning-local-research-into-global-experiments (Duolingo blog, 2021-02-02; accessed 2026-09-22)
- **Rollout is gradual and monitored.** Experiments ramp over days against nightly analysis; an experiment found to break code or hurt metrics is paused until fixed, not read as a result.

## The transferable pattern

Five structure rules:

1. **Randomize at the right unit.** User-level for product changes; session-level only for things genuinely sessional. Request-level randomization is almost always wrong.
2. **Mutually exclude related tests.** Two tests touching the same surface will interact and confuse both.
3. **Log exposure at the change moment.** Counting users who never saw the variant is the most common silent failure.
4. **Maintain a holdout — for detection, not for training.** A 1–5% always-control group catches cumulative regression that individual tests miss. Do not reuse it to generate model training data: Duolingo's ads team did exactly that, hit self-inflicted drift because the excluded cohort stopped resembling the population they served, and switched to occasionally acting randomly *inside* the live population instead (blog.duolingo.com/machine-learning-ads (Duolingo blog, 2025-03-18; accessed 2026-09-22)).
5. **Document the exposure rule.** "What counts as exposed" must be written down; teams often disagree without realizing.

Anti-patterns:
- Quasi-experiments (compare this week to last week with the change shipped). Almost never reliable.
- Testing on engaged users only. Bias the sample, bias the result.

## Apply to your product

- What is your randomization unit? Is it the same across all tests?
- Do related tests interact in your stack, or are they kept mutually exclusive?
- Do you log exposure at the moment of difference, or at some earlier event?

## See also

[[show-dont-tell]] · [[hypothesis-design]] · [[sample-size]] · [[guardrail-metrics]] · [[quasi-experiments]] · [[design-the-population]]
