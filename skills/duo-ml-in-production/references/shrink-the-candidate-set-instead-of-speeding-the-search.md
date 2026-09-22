---
name: duo-ml-in-production-shrink-the-candidate-set-instead-of-speeding-the-search
summary: When the space is too large to enumerate, encode domain heuristics that narrow it to reasonable candidates and search those deeply.
metadata:
  internal: true
---

# Shrink the Candidate Set Instead of Speeding the Search

## Concept

Combinatorial spaces grow faster than hardware improves, so any effort spent making exhaustive search faster is permanently outpaced. Doubling throughput buys you one more step of depth in a space that branches by ten. The optimization is against the constant when the problem is in the exponent.

The move that works is to attack the exponent: encode the heuristics a domain expert uses to ignore almost all of the space, generate a small set of plausible candidates, and then spend all of your compute examining those deeply. The heuristic does not need to be correct in the sense of never discarding the best option — it needs to be correct in the sense that the surviving set reliably contains something good.

## What Duolingo does

Source: blog.duolingo.com/chess-computers-vs-humans (Duolingo blog, 2026-03-12; accessed 2026-09-22)

- Claude Shannon calculated roughly **10^120 possible chess games** — more than the estimated number of atoms in the visible universe — and explicitly chose not to encode them. Instead he gave his algorithm **parameters for piece values, king safety and basic good-versus-bad strategy** so it would consider only "reasonable" moves.
- The **IBM 704 in 1957** applied **eight preliminary parameters to select seven candidate moves**, each explored **four moves deeper**. It took about **eight minutes to evaluate 2,800 positions**.
- For contrast on the cost of no pruning at all: **Turochamp in 1948, computed by hand, took more than 30 minutes per move.**
- Duolingo's point is that this structure survived the hardware entirely: **modern engines still use parameters to select candidates and then analyze those more deeply.** What changed was the quality of the parameters, not the shape of the algorithm.
- The generational marker: **Deep Blue lost to Kasparov in 1996 (1 win, 2 draws, 3 losses) and beat him in 1997 (2 wins, 3 draws, 1 loss)** — a one-year flip driven by better evaluation, not by exhausting the space, which remains impossible.

## The transferable pattern

When a candidate space is too large to score exhaustively, split the problem in two and give each half a different kind of engineering:

1. **Candidate generation** — cheap, high-recall, heuristic. Its only job is to produce a small set that almost always contains something good. Measure it on recall at K, never on precision.
2. **Deep evaluation** — expensive, high-precision, applied only to survivors. Because the set is small you can afford a model here that would be ruinous at full scale.

This is the shape of practically every large-scale ranking system, and stating it explicitly protects you from two common errors. The first is investing in raw throughput when the space grows faster than throughput ever will. The second is holding candidate generation to the wrong standard — teams tune the cheap stage for precision, it starts discarding good options, and no amount of quality in the deep stage can recover what it never received.

Write your heuristics down as parameters rather than burying them in code. The 1957 structure — a handful of named parameters selecting a handful of candidates — is legible, tunable and testable, and it lets you replace a hand-set weight with a learned one later without redesigning anything.

## Apply to your product

- Where are you scoring far more candidates than you can afford, and what fraction of them were never plausible?
- If you had to cut your candidate set to seven before the expensive stage, which cheap signals would you trust to do the cutting?
- Are you measuring your cheap first stage on recall, or have you accidentally tuned it for precision and started losing good options invisibly?

## See also

[[replace-the-rule-tree-with-one-learned-decision]] · [[generate-from-one-parameterized-primitive]] · [[../duo-backend-architecture/references/predict-only-what-users-dont-care-about]]
