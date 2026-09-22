---
name: duo-product-bounded-deliberation
summary: Give open-ended decisions a fixed option budget and time box, and tier the advice so each skill level gets a different instruction.
metadata:
  internal: true
---

# Bounded Deliberation, Tiered Advice

## Concept

When the option space is effectively infinite, the binding constraint is the cost of evaluation, not the quality of evaluation. The leverage is therefore in **shrinking the candidate set before analysing**, and in spending the same amount of thought on each candidate so the comparison is honest. The second half of the pattern: guidance presumes a prerequisite, so the right instruction for a novice is usually not a weaker version of the expert instruction but a categorically different one.

## What Duolingo does

Source: blog.duolingo.com/how-to-pick-your-next-chess-move (Duolingo blog, 2026-04-09; accessed 2026-09-22)

- The search space is explicitly unbounded — chess has more possible games than there are atoms in the universe — so the guidance never tries to analyse better, only to bound the search.
- The budget is numeric: shortlist **3-5 candidate moves**, visualise each for about **30 seconds**, rate each one, then play the highest-rated. The fixed per-candidate time is what makes the ratings comparable.
- Advice is **tiered into three levels with different instructions**, not three intensities of one instruction: beginners get "create a plan, even a bad one"; intermediates get the 3-5 candidates and the timed evaluation; advanced players get "make observations about the position's imbalances, then form a plan from them." A shared safety checklist sits above all three.
- Each tier matches that tier's actual binding constraint. Telling a beginner to enumerate candidates is useless — they have no basis for generating them. Telling an expert to "have a plan" is beneath the level at which their errors occur.
- There is a stated **override**: a concrete immediate threat pre-empts the whole procedure. Process discipline yields to urgent state changes.

The tension worth carrying: a fixed budget guarantees you sometimes discard the best option unexamined. The pattern accepts that loss in exchange for decisions actually being made, which is the failure mode an unbounded search produces instead ([[ship-it]]).

## The transferable pattern

1. **Budget the option set before you evaluate it.** Three to five candidates, chosen fast, beats an open field analysed slowly.
2. **Time-box each candidate equally.** Unequal attention silently manufactures a winner — usually whichever option was proposed first or loudest.
3. **Rate, then commit.** The output of the procedure is a decision, not a richer understanding.
4. **Write a different instruction per experience level.** Ask what each group's binding constraint actually is; a novice blocked on generating options and an expert blocked on evaluating them need opposite advice.
5. **Define the override.** Every deliberation procedure needs a stated condition under which it is abandoned, or people will follow it through an emergency.

## Apply to your product

- What recurring decision does your team make with no option budget, and how long does it typically sit?
- Does your onboarding give beginners the expert instruction in simpler words, or a genuinely different first move?
- What is the stated condition under which your team's process is allowed to be skipped — and is it written anywhere?

## See also

[[ruthless-prioritization]] · [[ship-it]] · [[kill-criteria-product]] · [[ownership-clarity]]
