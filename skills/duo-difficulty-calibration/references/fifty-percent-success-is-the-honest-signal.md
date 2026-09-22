---
name: duo-difficulty-calibration-fifty-percent-success-is-the-honest-signal
summary: A calibrated difficulty model puts users a little above 50% success; observed success rate is a free, label-free, continuous check on whether the model is honest.
metadata:
  internal: true
---

# Fifty Percent Success Is the Honest Signal

## Concept

An adaptive difficulty system is hard to audit. There is no ground-truth label for "was this the right item," offline metrics need a held-out set nobody maintains, and the model's own confidence is exactly the thing under suspicion. So teams ship the model and then have no continuous way to tell whether it still works.

There is a free check sitting in the event stream. If the system is aiming at the point of maximum useful effort, then by construction the predicted success probability at that point is near one half — and the observed success rate should land there too. Substantially higher and you are spending the user's time on things they already have. Substantially lower and you are modelling someone other than the person in front of you. The number requires no labels, no holdout and no annotation: it is available every day, per cohort and per item class, and it moves the moment the model drifts.

The target sits a little **above** half rather than exactly at it, because the user's experience of the session is part of the product and a coin-flip feels like failure.

## What Duolingo does

Source: blog.duolingo.com/how-we-learn-how-you-learn (Duolingo blog, 2016-12-14; accessed 2026-09-22)

- Duolingo stated the check plainly: if you recall correctly **a little more than half the time** during practice, the half-life predictions are doing their job.
- The model's accuracy sets how tight that check is. Half-life regression reached **mean absolute error 0.13**, meaning a predicted probability of **0.5** corresponded to an actual correctness rate in the band of roughly **37–63%**. A check on a noisier model is a looser check.

Source: blog.duolingo.com/duolingo-flashcards (Duolingo blog, 2025-11-18; accessed 2026-09-22)

- The pass bar is set below mastery on purpose. Flashcards require only **three of five correct** to pass; typos and almost-right pronunciations still count. An incorrect card flips, reveals the answer, plays it aloud, and returns to the back of the stack for another attempt **within the same session**. The session ends with a summary of strengths and what needs work.
- The rationale: a failed attempt costs nothing pedagogically — the retrieval attempt did its work either way — while a hard pass bar makes the session feel like a gate, which reduces the number of sessions, which is the variable that actually matters.
- **The tension.** A forgiving bar makes the pass signal weak evidence of mastery. That is acceptable for practice and disqualifying for assessment: the same exercise cannot serve as both without one of the two jobs being done badly.

## The transferable pattern

Instrument the success rate your targeting system produces, and treat it as the system's health metric rather than as a user-facing score.

1. **Pick the target band and write it down.** Somewhere a little above half is the default for a system aiming at maximum useful effort. A system with a different objective has a different number — but it has one, and most teams have never named it.
2. **Segment the check.** A healthy aggregate hides a cohort sitting at 95% and another at 20%. The aggregate is the least informative version of this metric.
3. **Bound the check by the model's own error.** A model whose predictions are loose supports only a loose acceptance band; reporting the band honestly stops the check from being theater.
4. **Separate the practice bar from the assessment bar.** Forgiving scoring maximizes attempts, which is what practice is for. Do not then read the pass signal as evidence of capability — build a separate, stricter measurement if you need that claim.

## Apply to your product

- What success rate do your users currently experience on adaptive content, and what rate were you aiming for? If those are the same number by coincidence, you have no check.
- Which cohort in your product sits furthest from the target band, and is it the beginners or the experts?
- Does any single surface in your product serve as both the practice loop and the mastery measurement? What breaks if you split them?

## See also

[[model-the-item-and-the-user-jointly]] · [[read-error-rate-with-completion-rate]] · [[escalate-at-the-tail-not-the-start]] · [[../duo-memory-and-decay/references/per-item-half-life-not-a-fixed-ladder]]
