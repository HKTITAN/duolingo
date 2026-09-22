---
name: duo-score-credibility-stop-presenting-items-that-tell-you-nothing
summary: Choose each next item from the estimate you already hold, and measure the behaviour itself rather than a correlate of it.
metadata:
  internal: true
---

# Stop Presenting Items That Tell You Nothing

## Concept

Every question you put in front of someone costs them time and buys you some quantity of information about them. An item far above or far below their ability has a near-certain outcome, so their answer barely moves your estimate — you spent the time and bought nothing. Two disciplines follow. Spend the item budget only where the outcome is genuinely uncertain, and make the item ask the person to do the thing rather than to answer questions about someone else doing it. A proxy item measures the proxy, and people optimize for whatever the item actually rewards.

## What Duolingo does

- The Duolingo English Test is a computer adaptive test. It draws from a bank of tens of thousands of items and selects each next item at the algorithm's current best guess of the taker's level, so almost every answer narrows the search.
- The payoff is a time collapse with no loss of confidence in the result: the test finishes in under an hour, against roughly **3 hours** average for traditional fixed-form exams.
- Source: blog.duolingo.com/is-the-duolingo-english-test-hard (Duolingo blog, 2021-06-14; accessed 2026-09-22)
- On proxies: rather than play a recorded conversation and ask comprehension questions about it, Interactive Listening has the taker hold a multi-turn conversation with an animated character toward a stated goal — following up with a professor, asking a friend to review a paper — then write a summary of what was said. One item measures comprehension, interaction, literacy and production together.
- Tension Duolingo names itself: each turn is still multiple choice. The item simulates real-time interaction rather than eliciting free production, so it remains a step short of the behaviour it stands in for. They publish the gap instead of claiming it is closed.
- Source: blog.duolingo.com/duolingo-english-test-interactive-skills (Duolingo blog, 2023-05-01; accessed 2026-09-22)

## The transferable pattern

1. **Select adaptively from your current estimate.** Maintain a running belief about the person, then pick the next probe whose outcome you are least able to predict. Items whose result you could have guessed are pure cost — they lengthen the session, raise abandonment, and leave the estimate where it was.
2. **Let precision, not item count, end the session.** Stop when the confidence interval is tight enough for the decision the score feeds. A fixed length is an admission that you are not tracking precision at all.
3. **Probe the behaviour, not a correlate of it.** When the real behaviour is awkward to elicit, teams quietly substitute something correlated and easier to grade. That correlation was measured on a population that was not preparing for your measurement, and it breaks precisely in the population you now measure.
4. **State the residual gap.** If your item still simulates rather than elicits, say which part is simulated. Outsiders discount an unclaimed gap far more harshly than a declared one.
5. **Budget for the calibration you now need.** Adaptive selection only works if you know each item's difficulty before you serve it, which means pre-testing items and re-checking them as your population shifts. That is the standing cost of the shorter session — pay it deliberately rather than shipping an adaptive shell over uncalibrated content.

## Apply to your product

- Which questions in your onboarding, qualification flow, or assessment would you have been able to answer on the user's behalf before asking? Those are the ones to cut.
- Where have you substituted an easy-to-grade signal for the behaviour you actually care about, and who benefits from that substitution once people know it is there?
- If you halved the length of the flow by selecting adaptively, what decision would the resulting estimate no longer be precise enough to support?
- Who owns the difficulty calibration of your items once the population using your product changes, and how would you notice that it had gone stale?

## See also

[[a-large-item-bank-makes-leakage-structurally-irrelevant]] · [[design-so-cramming-cannot-move-the-score]] · [[../duo-measurement-validity/SKILL]]
