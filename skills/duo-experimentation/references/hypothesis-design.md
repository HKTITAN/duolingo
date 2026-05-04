---
name: duo-experimentation-hypothesis-design
summary: What makes a testable hypothesis vs. a wish; the upstream skill of running good experiments.
metadata:
  internal: true
---

# Hypothesis Design

## Concept

A hypothesis is a falsifiable prediction. Most "test ideas" are not hypotheses — they're wishes ("we should make the button blue") with no prediction about what should change and by how much. The upstream cost of weak hypotheses is downstream noise: tests that "succeed" by p-hacking, or fail without anyone learning anything.

A good hypothesis names a mechanism, a metric, and a magnitude.

## What Duolingo does

The handbook describes Duolingo's experimentation culture as data-driven, not data-fishing. In practice this means:

- Every shipping experiment names its primary metric in advance.
- Hypotheses are explicit: "Doubling the streak-freeze cap will increase 30-day retention by 1–2 percentage points because users with one bad week currently churn at the next miss."
- Surprise results trigger a follow-up: was the mechanism we predicted what actually drove the change, or did the metric move for an unrelated reason?

## The transferable pattern

A useful template:

> **If** we change [X], **then** [primary metric] **will move by** [direction and magnitude] **because** [mechanism].

Examples:

- **Bad:** "Let's test a new onboarding."
- **Good:** "If we move the signup wall from screen 1 to screen 4, then 30-day retention will increase by 1.5–3 pp, because users will reach first value before being asked for an account."

Three rules:

1. **Predict magnitude, not just direction.** "It'll go up" is not a hypothesis; it's optimism.
2. **Name the mechanism.** Without a *because*, you can't tell whether the result confirmed your model or just got lucky.
3. **Pre-register the metric.** Decided after the test ran is not a primary metric.

## Apply to your product

- Take the last test your team ran (or proposed). Can you write it in the *if-then-because* form?
- Was the magnitude predicted in advance? If not, how would you have known if it landed?
- For your next test, write the hypothesis before designing the experiment. What changes about the design?

## See also

[[show-dont-tell]] · [[ab-test-structure]] · [[metric-selection]] · [[novelty-effects]]
