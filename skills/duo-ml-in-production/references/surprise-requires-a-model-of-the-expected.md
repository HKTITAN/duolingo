---
name: duo-ml-in-production-surprise-requires-a-model-of-the-expected
summary: To recognize something as impressive you need a model of what a typical person would have done — impressiveness is low predicted probability plus high realized gain.
metadata:
  internal: true
---

# Surprise Requires a Model of the Expected

## Concept

A system that only knows what is optimal cannot tell you what is impressive. To an optimality model every correct action looks equally ordinary, because correctness is the only axis it has. Difficulty, rarity and cleverness are all invisible to it.

Impressiveness is a two-term quantity: the action was unlikely for a person like this one, *and* it turned out well. That means you need a second model — one trained to predict what a typical person at that capability level would actually have done — and the surprise is measured as the gap between the two. Without a behavioral prior there is nothing to be surprised against, and every attempt to detect brilliance collapses into detecting correctness.

## What Duolingo does

Source: blog.duolingo.com/engineering-game-review (Duolingo blog, 2026-09-08; accessed 2026-09-22)

- Chess Game Review runs **a family of human-like neural networks (Maia lineage, parameterized by rating strength)** alongside a classical optimality engine. The first predicts what a player at that strength would probably play; the second says what is actually good.
- A move is classed **brilliant** when the behavioral model put **very little probability mass on any of the good moves and the user played one anyway**, or when the move was good, low-probability, and produced a jump in expected Win-Draw-Loss.
- So the rule is explicitly the conjunction: unlikely *and* rewarded. Unlikely alone is just a mistake; rewarded alone is just competence.
- **The tension is acknowledged in the post.** A large grey area remains unclassified — a move that is objectively not the strongest but creates practical problems for a time-pressured opponent has no label, and the "key moment" detector misses many merely teachable ones. Two models produce a richer vocabulary, not a complete one.

## The transferable pattern

If you want to celebrate, highlight or surface something, you need three components, and most teams build only the first two:

1. **A quality model** — was this good? Usually you already have it, because it is the same thing that powers correction and scoring.
2. **A behavioral model** — what would a typical user at this level have done? This is the missing piece. It is trained on what people actually did, not on what they should have done, and it must be conditioned on capability or it will call everything a beginner does surprising.
3. **A gain measure** — how much better off is the user now? Without it you will celebrate rare actions that changed nothing.

The behavioral model is reusable well beyond celebration. The same prior tells you which failures were predictable (and therefore worth teaching against), which user actions are anomalous enough to flag for review, and where your interface is pushing people toward choices they would not otherwise make.

Expect a large unclassified middle and resist the urge to fill it. Forcing a label onto every event is how a surprise detector becomes noise, and the moment users see one unearned celebration, every other one is discounted.

## Apply to your product

- Do you have any model of what a typical user would do next, as distinct from what the correct next action is?
- When you highlight a user's success, are you measuring that it was hard for someone like them, or only that it happened?
- What share of events would your detector leave unlabeled, and are you comfortable shipping that silence rather than diluting the signal?

## See also

[[calibrate-the-same-measurement-per-skill-level]] · [[pick-the-metric-sensitive-where-users-care]] · [[../duo-gamification/SKILL]]
