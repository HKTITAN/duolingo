---
name: duo-ai-product-strategy-simplify-until-automatable-name-what-must-survive
summary: Write down the one thing the feature must keep doing, then standardize everything else until automation is feasible — and budget for the sameness you bought.
metadata:
  internal: true
---

# Simplify Until Automatable, Name What Must Survive

## Concept

Automation fails on variation, and most of the variation in a hand-made artifact is incidental rather than valuable. It is there because different people made different choices on different days, not because any of it carries the thing users came for.

So the sequence is: name the one thing the feature must keep doing, then standardize everything else until a pipeline can produce it. Naming the core first does two jobs. It gives you permission to strip the rest, which teams otherwise defend out of loss aversion. And it gives the pipeline an acceptance test that is not "does this look like the old one" — a test you can never pass at scale, because the old one was a thousand unrepeatable judgment calls.

## What Duolingo does

Source: blog.duolingo.com/scaling-duoradio (Duolingo blog, 2025-03-11; accessed 2026-09-22)

- To scale DuoRadio with generative AI, Duolingo simplified parts of the format while **explicitly preserving its core educational value** — listening practice that re-exposes grammar and vocabulary from lessons in new context. That sentence is the acceptance test the pipeline is held to; everything not in it was negotiable.
- One concrete simplification worth generalizing — they **stopped letting the model sequence exercises freely** and instead used **learner session data** to fix exercise order and placement. The model kept the generative job it was good at; a decision that had a better source of truth was taken away from it and settled empirically.
- The removal instinct generalizes beyond automation. In Duolingo's Duologues series, Ian Silber (Head of Design at OpenAI) argued for designing **the interaction, not the interface** — treating the shape of the exchange as the product — and for constantly questioning whether features could be **simplified or removed entirely** (blog.duolingo.com/duologues-design-conversations (Duolingo blog, 2024-12-18; accessed 2026-09-22)).

**Tension, and Duolingo names it themselves.** The bill arrives later. Having scaled, the team is back **refining session length and exercise variety to ensure each episode stays fresh** — standardization bought volume at the price of sameness. That is not a reason to skip the simplification; it is a reason to schedule the variety work as a known, dated follow-up rather than discovering it as a complaint.

## The transferable pattern

1. **Write the core value in one sentence**, in terms of what the user gets, not what the artifact contains. If you cannot, you are not ready to automate — you will end up preserving the artifact's surface instead of its function.
2. **Inventory the variation.** For each varying dimension, ask whether a user could tell it changed and would care. Most cannot and would not. Those are your standardization candidates.
3. **Take decisions away from the model where you have better evidence.** Generative freedom is valuable where no ground truth exists and wasteful where your usage data already answers the question.
4. **Price the sameness up front.** Standardization always trades variety for volume. Decide before you ship how you will detect staleness and what the follow-up work is, so the fix is a plan rather than a surprise.
5. **Keep asking what could be removed entirely.** New capability tends to accrete surface; the removal question is the only reliable brake.

## Apply to your product

- Write the one sentence that says what your feature must keep doing for the user. Would your team agree on it today, and does it mention any implementation detail it should not?
- Which dimensions of your output vary today, and for how many of them could a user tell the difference and care?
- If you standardized to reach volume, how would you detect that your output had become repetitive — and who owns the fix, on what date?

## See also

[[spend-the-automation-budget-on-the-gate]] · [[adopt-early-gate-on-your-own-quality-bar]] · [[author-a-pool-deliver-an-instance]]
