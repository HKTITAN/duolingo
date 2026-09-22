---
name: duo-gamification-rate-by-opponent-strength
summary: Score users by how hard what they beat was, not by how many times they won — and ship the caveat that the rating lags real improvement.
metadata:
  internal: true
---

# Rate by Opponent Strength

## Concept

A count-of-wins score is farmable. If every win is worth the same, the optimal strategy is to hunt the weakest available opposition, and the number stops measuring the skill it claims to measure.

A relative rating fixes this by making the reward proportional to how surprising the result was. Beating something you were expected to beat pays almost nothing; beating something above you pays a lot; losing to something below you costs a lot. Farming becomes pointless because the easy win is worth nearly zero, and the score self-corrects downward if you were overrated.

## What Duolingo does

Duolingo rates chess learners with **Elo**, the same system FIDE uses, and runs the standard probability model.

- Elo treats performance as a normally distributed variable around a player's rating, and settles each result against the expected outcome: beating a much lower-rated player gains little while losing to one costs more than losing to a stronger player. **A draw against a much weaker player can lose you points.** The rating never goes negative regardless of losses. Source: blog.duolingo.com/what-is-an-elo-rating-in-chess (Duolingo blog, 2026-06-02; accessed 2026-09-22)
- The same scale carries external, legible thresholds: **Grandmaster at 2500 plus three norms; International Master 2400; FIDE Master 2300; Candidate Master 2200**, with norms requiring classical tournaments of **at least nine rounds** against an average participant rating of **2380+**. The titles date to **1950**. Source: blog.duolingo.com/how-to-become-a-chess-grandmaster (Duolingo blog, 2026-02-24; accessed 2026-09-22)
- Duolingo also uses the Elo algorithm to track learner progress more broadly, not only in chess.

The honest part is the caveat Duolingo ships alongside the number: it tells learners directly that **Elo does not always reflect their progress**, and pairs the rating with advice to review their own games and find one small improvement. That concession is structural, not modesty — a relative rating measures you against a population that is also improving, so genuine gains can read flat or negative for a stretch. A user who treats the number as identity will read that stretch as failure.

The other cost: relative ratings need volume and comparable opposition to converge, so early or infrequent users sit on a number that is mostly noise.

## The transferable pattern

1. **Weight each result by its expected outcome.** The reward should be proportional to the surprise, which makes seeking out easy wins strictly unprofitable.
2. **Let the score fall.** A number that only goes up cannot correct an overrating, which is what makes it farmable in the first place.
3. **Publish fixed, external-sounding thresholds on top of the relative scale.** Named tiers give the continuous number something to aim at, and they are legible outside your product.
4. **Ship the caveat with the number.** If your metric can be honestly flat during real improvement, say so at the point of display and pair it with a qualitative next step — otherwise the number alone tells the user they wasted their effort.

## Apply to your product

- Does your scoring distinguish a hard success from an easy one, or pay the same for both?
- Can a user's score go down? If not, what stops someone farming the easiest available path?
- What would your users misread as failure — and what caveat or next step would you show right next to it?

## See also

[[xp-system]] · [[beat-your-own-best]] · [[anti-grind]] · [[../duo-retention/references/leagues]]
