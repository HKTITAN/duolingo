---
name: duo-metric-design-put-the-weight-in-the-formula-not-the-memo
summary: When some actions are worth more than others, encode the ratio as a coefficient in the graded metric — a memo stating priorities changes nothing.
metadata:
  internal: true
---

# Put the Weight in the Formula, Not the Memo

## Concept

Every team optimizes the number it is graded on, not the number it was told to care about. If some user actions genuinely create more value than others, the ratio belongs inside the metric as a coefficient. Written as a priority in a strategy doc, it survives one planning cycle. Written as a `0.5` in the formula that decides whether the quarter went well, it changes what gets built, because shipping toward the heavier term is now the mechanically rational move.

The same discipline applies in reverse: a weighted formula is a compression of a real objective, and compressions mislead in position-dependent ways. Ship the weights *and* the conditions under which they are wrong.

## What Duolingo does

Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

- The company metric is **Time Spent Learning Well (TSLW) = Minutes Learning on Path + 0.5 x Minutes Learning in Other Lessons**. Path lessons — including Stories and personalized practice — count at full value; Practice Hub, Match Madness, Ramp Up, Legendary and Side Quests count at half.
- The `0.5` is a claim about value, not a rounding convenience. An independent 2023 study from Northern Arizona University and East Carolina University found the **number of completed lessons was the strongest predictor of learning gains** — so the term tied to lessons carries full weight.
- Teams then built toward the coefficient: **Daily Quests are ordered so the first is easiest and later ones require path progress**, and XP was rebalanced in the same direction.
- Duolingo is explicit that TSLW is a **proxy**, not the objective, and keeps a separate Efficacy Lab for rigorous measurement. They also say the formula is still being refined — the coefficient is a current best guess, not a law.

A second Duolingo artifact shows the caveat discipline. Its chess explainer assigns **pawn 1, knight 3, bishop 3, rook 5, queen 9, king invaluable** (a queen can control up to **27 squares** versus a pawn's 2) — then spends most of the post on **six caveats**: combinations are not the sum of parts, piece activity matters, equal-point trades are not equal, pawns gain value near promotion, not all pawns are equal, and open versus closed positions change the values. Its flat conclusion: the game is not about collecting points. It keeps the numbers anyway, on the grounds that a fast wrong-ish baseline beats no baseline when you know when to override it. Source: blog.duolingo.com/chess-points-of-pieces (Duolingo blog, 2026-05-21; accessed 2026-09-22)

## The transferable pattern

1. **Name the actions you believe are worth more.** Not categories of feature — categories of user outcome.
2. **Pick a coefficient and defend it with evidence outside the metric.** An external study, a cohort analysis, anything that is not the metric arguing for itself. A weight nobody can source is a political number and will be relitigated every quarter.
3. **Put it in the number the team is reviewed on.** Priorities live in whatever gets read at the review, and the formula always gets read.
4. **Publish the failure conditions alongside the weights.** Where does the score reward the wrong thing? When is a team ahead on the score and behind on the objective? A weighted metric that travels without its caveats gets optimized as if it were the win condition.
5. **Date the weights.** Say out loud that they are a current estimate and name what would make you change them.

The cost is real: a coefficient encodes a judgment that may be wrong, and it makes that judgment binding across the whole org at once. That is exactly why the caveats and the revision path ship with it.

## Apply to your product

- Which two user actions do you believe differ in value by 2x or more, and what ratio would you defend in writing?
- Is that ratio anywhere in the number your team is graded on — or only in a doc?
- If someone optimized your headline metric ruthlessly and stupidly, what would they build? Write that down as your first caveat.

## See also

[[pair-every-growth-metric-with-a-quality-proxy]] · [[threshold-percentage-not-aggregate-total]] · [[../duo-measurement-validity/SKILL]]
