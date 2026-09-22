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

The hypothesis is a field in the experiment setup flow, not a norm. Duolingo calls identifying the expected result "perhaps the most important part of an experiment," and uses it to establish the baseline for success or failure before any data exists; the service then computes the analysis against it. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

PMs are expected to form and test hypotheses for anything from a copy change to an entirely new section of the app, and everyone can read past experiment data. Source: blog.duolingo.com/why-i-interned-at-duolingo-rebecca-hu-product-management-intern (Duolingo blog, 2022-08-26; accessed 2026-09-22)

The mechanism is the part that gets tested — and the part that usually fails to travel:

- German learners were opting into push notifications less often. The hypothesis named a mechanism: the copy never said notifications help you learn. Rewriting it to say so produced an **8% increase in opt-in** for German learners.
- Duolingo then ran the same change in Spanish, expecting the mechanism to generalize. **No significant impact.** Their conclusion: it was not a one-size-fits-all solution. Source: blog.duolingo.com/copy-testing-experiments (Duolingo blog, 2022-01-14; accessed 2026-09-22)

A hypothesis that names a mechanism is what makes that second result legible as information rather than noise. A hypothesis that only named a direction would have shipped the Spanish copy on the German evidence.

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

[[show-dont-tell]] · [[ab-test-structure]] · [[metric-selection]] · [[novelty-effects]] · [[baseline-at-first-contact]]
