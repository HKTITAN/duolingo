---
name: duo-experimentation-outcome-not-engagement
summary: Engagement proves a feature was tolerable; only a holdout delta on the failure it targeted proves it worked.
metadata:
  internal: true
---

# Outcome, Not Engagement

## Concept

Engagement, completion rate and self-reported satisfaction all answer the same question: did users tolerate this? None of them answer the question you built the feature for. A feature exists to remove a specific downstream failure — a specific error, a specific drop-off, a specific unresolved request. The only evidence that it did is a measured drop in that failure, in the treated group, against a holdout that never received the feature. Without the holdout you cannot rule out that the failure rate would have fallen anyway through ordinary use.

## What Duolingo does

Duolingo shipped a set of French present-tense Grammar Lessons to a small percentage of learners and compared them against learners on the standard course who never received the skill. The measured outcome was not lesson completion or time in app — it was the rate of present-tense-specific mistakes afterwards. The treated group made fewer. Source: blog.duolingo.com/language-rules-learning-grammar-on-duolingo (Duolingo blog, 2020-10-02; accessed 2026-09-22)

The paired pre/post controlled experiment on the same mechanism is the sharper number: the control group moved from 40% to 54% accuracy (+14 points) while the group that received the explicit grammar treatment moved from 36% to 86% (+50 points) — a group that started *behind* the control and finished far ahead. Source: blog.duolingo.com/how-duolingo-works-with-learners (Duolingo blog, 2022-04-04; accessed 2026-09-22)

Two things make the read trustworthy and both are cheap to skip:

- The control group improved substantially on its own (+14 points). A single-arm before/after study would have credited the whole +14 to the feature.
- The treatment group started lower. Without randomization into arms, the starting gap would have looked like the feature making things worse.

Tension: the published rollout is "a small percent of learners" with no absolute error rates or sample size. The direction is auditable; the effect size on the shipped version is not.

## The transferable pattern

1. **Name the failure before you build.** Write down the specific thing that goes wrong today and how you count it. If you cannot count it, you cannot claim the feature fixed it.
2. **Instrument that counter, not a proxy for enthusiasm.** Usage of the fix is an input, not the outcome.
3. **Hold out a comparable group.** The baseline is not zero — people improve, adapt and self-serve without you. The holdout is what converts "it got better" into "we made it better."
4. **Expect the arms to differ at baseline** and report both start and end, not the delta alone.

Anti-pattern: a launch review that opens with adoption numbers and never mentions the failure rate the feature targeted.

## Apply to your product

- For the feature you shipped most recently, what specific failure was it supposed to reduce, and do you have a counter for it?
- Did anyone stay on the old experience long enough to serve as a comparison, or did you roll out to everyone at once?
- If your control group improves on its own by a meaningful amount, how much of your last "win" survives?

## See also

[[metric-selection]] · [[ladder-of-evidence]] · [[ab-test-structure]] · [[guardrail-metrics]]
