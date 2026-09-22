---
name: duo-efficacy-measurement-adaptive-is-shorter-not-easier
summary: Selecting each item near the running ability estimate makes every answer informative, so confidence arrives in far fewer items.
metadata:
  internal: true
---

# Adaptive Is Shorter, Not Easier

## Concept

A fixed-length assessment is assembled with no knowledge of who will take it, so most of its items land far from any given person's ability. Those items carry almost no information — the taker gets them all right or all wrong, and either outcome was predictable before they answered. Selecting the next item near the current estimate makes every item discriminating, so the estimate converges in a fraction of the length. Shorter is a consequence of better targeting, not of a lowered bar.

## What Duolingo does

Source: blog.duolingo.com/digital-sat-future-of-testing (Duolingo blog, 2022-01-28; accessed 2026-09-22)

- Duolingo built the Duolingo English Test as the first digital-first high-stakes computer adaptive test, **launched more than five years before January 2022**, and used the **digital SAT's announced one-hour reduction** as the teaching example for why adaptive tests are shorter without being less accurate. Adaptive forms can run hours shorter than their fixed-form counterparts.
- The DET itself runs in **1 hour with one adaptive section**, described as producing "personalized exams that are considerably shorter than traditional standardized tests" (blog.duolingo.com/doctoral-award-winners-2021 (Duolingo blog, 2021-11-19; accessed 2026-09-22)).
- The same post names the next constraint honestly: current item-selection algorithms **"cannot improve by learning from response data."** Duolingo funded Aritra Ghosh's research at UMass Amherst on replacing the static selector with a trainable one — an admission that the shipped version is frozen at its designer's assumptions.
- The low-stakes version of the same mechanism: Duolingo's placement test **starts by assuming novice and escalates difficulty as answers come in correct**, then unlocks the skills it infers the person already has, so onboarding ends in real work rather than in a transcript (blog.duolingo.com/partial-credit-improvements-to-duolingos-placement-test (Duolingo blog, 2018-09-14; accessed 2026-09-22)).

Adaptivity is not free. It needs a calibrated item pool large enough to have good items at every level, and a live estimator — which is why a fixed form remains the right call when the pool is small or the population narrow.

## The transferable pattern

- **Re-estimate after every response, and pick the next item from the estimate.** Each answer narrows the plausible range; the next question should sit where the remaining uncertainty is, not where a fixed script put it.
- **Length is the payoff, difficulty is not.** If you find yourself defending an adaptive design as "gentler", the design is wrong. It is the same standard reached with fewer questions.
- **For onboarding, optimize for exit speed.** The point of an entry assessment is to get someone into real work quickly, not to produce a record. Start with a prior, escalate, stop early.
- **Prefer a selector that learns.** A hand-written rule for choosing the next item is frozen at the moment it was written; a selector trained on accumulated response data improves as the corpus grows. Ship the rule first, but know it is a placeholder.
- **Watch the pool, not just the algorithm.** Adaptive selection can only choose from what exists. Thin coverage at the high end silently caps what the instrument can resolve.

## Apply to your product

- Where does your product ask everyone the same fixed sequence of questions, and what fraction of those answers were predictable from the previous ones?
- If an entry assessment had to end in a third of the time, what would you cut — and does anything you would cut actually change the outcome?
- Is your next-item logic a static rule nobody has revisited, and how much response data is now sitting unused that could replace it?

## See also

[[partial-credit-beats-binary-scoring]] · [[check-the-distribution-not-the-score]] · [[../duo-difficulty-calibration/references/model-the-item-and-the-user-jointly]] · [[../duo-difficulty-calibration/SKILL]]
