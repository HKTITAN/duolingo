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

- **Randomization unit** is typically the user (sometimes the device, rarely the session) — never the request, which leaks variants to the same user.
- **Mutual exclusion** for related tests: a user in test A is held out of test B if the two could interact.
- **Holdout cohorts** for long-running platform changes — a small group always sees control, so cumulative drift can be detected.
- **Exposure logged at the moment the user could have seen the difference**, not at session start. This avoids inflating the denominator.

## The transferable pattern

Five structure rules:

1. **Randomize at the right unit.** User-level for product changes; session-level only for things genuinely sessional. Request-level randomization is almost always wrong.
2. **Mutually exclude related tests.** Two tests touching the same surface will interact and confuse both.
3. **Log exposure at the change moment.** Counting users who never saw the variant is the most common silent failure.
4. **Maintain a holdout.** A 1–5% always-control group catches cumulative regression that individual tests miss.
5. **Document the exposure rule.** "What counts as exposed" must be written down; teams often disagree without realizing.

Anti-patterns:
- Quasi-experiments (compare this week to last week with the change shipped). Almost never reliable.
- Testing on engaged users only. Bias the sample, bias the result.

## Apply to your product

- What is your randomization unit? Is it the same across all tests?
- Do related tests interact in your stack, or are they kept mutually exclusive?
- Do you log exposure at the moment of difference, or at some earlier event?

## See also

[[show-dont-tell]] · [[hypothesis-design]] · [[sample-size]] · [[guardrail-metrics]]
