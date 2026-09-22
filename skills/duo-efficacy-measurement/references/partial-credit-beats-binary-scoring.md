---
name: duo-efficacy-measurement-partial-credit-beats-binary-scoring
summary: Binary grading discards the gradations that separate adjacent ability levels, producing a high-variance estimate from the same items.
metadata:
  internal: true
---

# Partial Credit Beats Binary Scoring

## Concept

An estimator updates on each response, so the information content of a single answer bounds how fast and how accurately the estimate converges. Collapsing "right structure, one small element wrong" into the same bucket as "completely wrong" throws away exactly the gradations that distinguish adjacent ability levels. The estimate comes out high-variance, and the visible symptom is that the same person, retested, lands somewhere quite different.

## What Duolingo does

Source: blog.duolingo.com/partial-credit-improvements-to-duolingos-placement-test (Duolingo blog, 2018-09-14; accessed 2026-09-22)

- The motivating failure was the author's own: **two placement attempts a year apart produced very different placements.** The instrument, not the person, had moved.
- The fix assigned **fractional correctness by mistake category** — a missing noun costs more than a missing article — **and by challenge type**, with translation graded more leniently than transcription. Those fractional scores were then fed into the existing adaptive machinery rather than replacing it.
- **Simulations varying the number of correct answers from 10 to 15** showed the partial-credit scheme placing learners ahead of the binary one. Where no mistake category is assigned, the two schemes are **identical** — so the change degrades gracefully to the old behaviour instead of introducing a new failure mode.
- Shipped **on web first**, because web had the richest grading data. The rollout order was chosen by where the signal was, not by where the users were.

The honest admission sits in the same post: the correctness weights were **"pulled out of thin air"** rather than derived, and should be computed from real user response data. A judgement-based weighting that improves on binary is worth shipping — and is not the same thing as a calibrated one.

## The transferable pattern

- **Grade the response, not the verdict.** Wherever your system currently emits pass/fail, ask what intermediate states it is flattening. Those states are the signal.
- **Weight by failure category and by task type.** Not all errors are equally diagnostic, and not all tasks are equally demanding — a lenient task and a strict task producing the same binary result are not the same evidence.
- **Feed the richer score into the estimator you already have.** This is a scoring change, not an architecture change. It needs no new model, only a better input.
- **Design the fallback to equal the old behaviour.** When no category applies, the new scheme should reduce exactly to the old one. That makes the change safe to ship before the weights are good.
- **Ship where the data is richest.** Roll out first on the surface that produces the most detailed responses, then generalize once the weights have something to be fit against.
- **Then go back and derive the weights.** Hand-set weights are a starting position with a known expiry, and saying so in public is the thing that keeps the follow-up on the roadmap.

## Apply to your product

- Where does your product collapse a graded outcome into a binary one, and what would the intermediate categories be if you named them?
- If the same user ran through your assessment twice a week apart, how far apart would the two results land — and has anyone checked?
- Are the weights in your scoring derived from response data or chosen in a meeting, and which is it honest to call them in public?

## See also

[[adaptive-is-shorter-not-easier]] · [[check-the-distribution-not-the-score]] · [[../duo-difficulty-calibration/SKILL]]
