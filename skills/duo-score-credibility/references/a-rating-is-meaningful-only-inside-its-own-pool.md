---
name: duo-score-credibility-a-rating-is-meaningful-only-inside-its-own-pool
summary: A relative rating encodes standing within one population and nothing else; never compare across pools, and say plainly that yours is separate.
metadata:
  internal: true
---

# A Rating Is Meaningful Only Inside Its Own Pool

## Concept

A rating derived from results against other participants encodes relative standing in that population — and nothing else. It is not a measurement of the person; it is a measurement of the person against whoever else happened to be in the pool. Two pools with different composition therefore produce systematically offset numbers for identical skill. Users do not intuit this. They assume a number is a number, so they either feel cheated when an outside body rates them lower or over-trust an inflated one. If you run a rating, the disclosure that it is pool-local is not a legal footnote; it is part of the design.

## What Duolingo does

- Duolingo gives chess players an Elo that updates after each game against Oscar or against other players, and states outright that your Duolingo Elo will not affect your rating elsewhere, and that games played in real life or on any other online platform will never affect your Duolingo Elo. The pools are declared separate before anyone can be disappointed by it.
- The published cross-pool offsets are large enough to make the point on their own: **USCF ratings run roughly 100 points higher than FIDE ratings** for players rated by both. Some online platforms rate top players **over 3300**, while the **highest FIDE rating ever achieved is 2882** (Magnus Carlsen, May 2014).
- Even the floors differ: **FIDE's rating floor is 1400; USCF's is 100**. The same system, adopted by **USCF in 1960 and FIDE in 1970**, produces numbers that are not interchangeable across the bodies that run it.
- Source: blog.duolingo.com/what-is-an-elo-rating-in-chess (Duolingo blog, 2026-06-02; accessed 2026-09-22)

## The transferable pattern

- **Name the pool in the definition of the number.** A rating without its population attached is a claim nobody can check. Internally, treat "rating" and "rating within pool P at time T" as different quantities.
- **Refuse cross-pool comparison in the interface, not just in the docs.** Do not show an external rating next to yours, do not offer import, and do not let a leaderboard mix populations. Whatever you put side by side, users will subtract.
- **Say the separation early and in plain words.** One sentence before the user earns the number costs nothing. The same sentence after they compare it with an outside body reads as an excuse.
- **Watch for pool drift.** Composition changes as you grow, segment, or add a new tier, and the same number silently means something different than it did a year ago. If you rebase, publish that you rebased and when.
- **Show the rating's uncertainty early on.** A number derived from a handful of results is mostly noise, and displaying it at full confidence teaches users to distrust it once it swings. Either hold it back until enough results accumulate or show it as provisional.
- **Distinguish relative from absolute measures deliberately.** A rating answers "who is stronger"; an anchored level answers "what can this person do". Ranking is cheap to compute and worthless outside; anchoring is expensive and portable. Pick per use case, and do not let one quietly stand in for the other.

## Apply to your product

- Is your score relative to other users or absolute against a fixed criterion — and would a user reading it in your UI be able to tell which?
- Where does your product place your number near an outside number, and what wrong inference does that adjacency invite?
- If your user base composition shifts, does the same score still mean what it meant last year, and who is responsible for noticing that it does not?
- How many results does a new user need before you show their rating at all, and what do you show them in the meantime?

## See also

[[anchor-to-an-external-published-standard]] · [[one-legible-number-plus-a-content-manifest]] · [[../duo-gamification/SKILL]]
