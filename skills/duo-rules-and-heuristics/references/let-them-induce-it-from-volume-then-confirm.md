---
name: duo-rules-and-heuristics-let-them-induce-it-from-volume-then-confirm
summary: When users are not internalising a pattern the bottleneck is usually exposure, not wording — supply the data, let them form a theory, then confirm it.
metadata:
  internal: true
---

# Let Them Induce It From Volume, Then Confirm

## Concept

People extract structure from volume without being told. The brain counts co-occurrences and computes transitional probabilities below conscious awareness, so the usual reason an adult fails at a new system is not that they are a worse learner — it is that they cannot get enough data of the right kind. That reframes a stuck user as a supply problem rather than a wording problem. It also inverts the order of teaching: let them form a theory from examples first, because a wrong theory plus corrective feedback points attention at exactly the feature they missed, which is a far more precise signal than a correct statement read passively.

## What Duolingo does

- Duolingo frames its whole daily-habit architecture as a **data-supply problem**, not an instruction problem. The post ends "give it what it wants: more data!" and lists the streak machinery, music, TV and games as additional data channels rather than additional instruction. Its evidence that statistical learning runs below awareness: **babies days old** already track statistical patterns in streams of musical pitches. Source: blog.duolingo.com/how-your-brain-finds-patterns (Duolingo blog, 2023-07-27; accessed 2026-09-22)
- For unfamiliar concepts, learners are told to study many examples, look for what changes predictably, and **form a theory** — framed explicitly as detective work — with mistakes and feedback used to refine it. Written explanations exist but are positioned as reinforcement of what the learner is already working out. Source: blog.duolingo.com/grammar-practice-tips (Duolingo blog, 2022-05-17; accessed 2026-09-22)
- Adjacency does a lot of the work. The 3rd grade math course puts 2x3, 2x4 and 2x5 on **one screen**, and places division problems next to the overlapping multiplication problems so the inverse relation is inferred rather than memorised — a learner who sees 5x9=45 beside 45/5=9 encodes one relation and derives two facts. Intro to division covers facts **2–5**; single-digit multiplication goes up to **9**. Source: blog.duolingo.com/3rd-grade-math (Duolingo blog, 2026-07-14; accessed 2026-09-22)
- In Adventures, unknown words appear inside a rendered scene — a grocery aisle with broken eggs on the floor — rich enough to disambiguate them, instead of being pre-defined. Source: blog.duolingo.com/adventures (Duolingo blog, 2024-09-24; accessed 2026-09-22)

**Tension.** Duolingo names the cost out loud: "This can feel difficult and even frustrating at times." Induction is a desirable difficulty, and desirable difficulties are unpleasant. Duolingo ships an escape hatch — the written explanation — for learners who need it, rather than pretending the frustration is not real.

## The transferable pattern

When users are not internalising something, check exposure before you rewrite the explanation. Count how many times a typical user has actually encountered the pattern in a week. If the answer is three, no phrasing will save you; the fix is scheduling, surfacing, or a second channel that supplies more instances.

Then order the teaching: **instances, theory, confirmation.** Give enough varied examples that a hypothesis is possible, let the user commit to one, and only then state the rule — at which point it labels an intuition they already have instead of arriving as a claim they must take on trust.

Two amplifiers that cost almost nothing:

- **Put related items on the same screen.** Adjacency makes structure visible; separation makes everything look like an unrelated fact. Show an operation next to its inverse, a setting next to its effect, a before next to its after.
- **Embed the unknown in context rich enough to disambiguate it**, instead of defining it up front. Inference is generation: the user who constructs the meaning builds more retrieval routes to it than the user who reads it.

Budget for the frustration and give the impatient user a way out.

## Apply to your product

- How many times does a typical user meet the pattern you want them to internalise in their first week? Is that a wording problem or a supply problem?
- What two things in your interface are currently on separate screens that would teach a relationship if they were adjacent?
- Where do you define a term up front that the surrounding context could have made obvious — and what would you lose by removing the definition?

## See also

[[mistakes-are-the-signal-not-the-defect]] · [[where-explicit-instruction-earns-its-place]] · [[two-memory-systems-explanation-loads-the-wrong-one]]
