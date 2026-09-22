---
name: duo-memory-and-decay-decay-is-graded-and-fine-grain-goes-first
summary: Specific items rot far faster than structure, and recognition outlives production — so decay is a shape to model, not a switch that flips.
metadata:
  internal: true
---

# Decay Is Graded, and Fine Grain Goes First

## Concept

Capability does not vanish; it erodes unevenly, and the order is predictable.

Fine-grained, individually rare items go first. Each one has a weak, isolated trace that nothing else reinforces. Structural knowledge — the rules, the shape of the thing, the general procedure — is far more durable, because *every single instance that uses it* rehearses it. Two layers, two completely different clocks.

The second ordering is between recognition and production. The ability to understand something persists long after the ability to generate it is gone. A user who can still follow along cannot necessarily still do it, which means any audit based on recognition will report that nothing has decayed while production has quietly collapsed.

So the honest model is not present-or-absent. It is a structure that stays standing while individual pieces fall off it.

## What Duolingo does

Source: blog.duolingo.com/can-you-forget-your-first-language (Duolingo blog, 2024-02-20; accessed 2026-09-22)

- Duolingo states the ordering directly: someone not using a language forgets **individual words far more quickly than they forget grammar and pronunciation**, and the ability to *understand* persists long after the ability to *speak* is gone.
- Their metaphor for the shape: knowledge is less like a sock — present, or vanished — and more like **a house that loses a shingle here and a floorboard there and stays standing a very long time**.
- Duolingo's own bilingual staff describe fluctuation as the normal state rather than an edge case: "language attrition is so real," with proficiency, speed of recall and even accent shifting according to how much exposure each language is currently getting (blog.duolingo.com/what-does-it-feel-like-to-be-bilingual (Duolingo blog, 2023-09-19; accessed 2026-09-22)).

**The tension.** Duolingo also notes that the contents of a skill shift daily *even with constant use*, because life phases change which topics come up. So what looks like decay is partly drift: the specific pieces you hold are being swapped, not only lost. A maintenance system that assumes disuse is the only cause will keep resurfacing things the user has genuinely finished with, and miss the new gaps that changed circumstances opened.

## The transferable pattern

1. **Model at least two decay rates.** Specifics and structure are not one variable. A single "last used" timestamp on a whole capability averages two things that move at different speeds and tells you about neither.
2. **Refresh the fast layer, not the whole thing.** When someone returns after a gap, the expensive structural layer is probably intact. Re-teaching it is wasted effort and reads as an insult.
3. **Never audit decay with a recognition check.** If your health signal is "can they still identify it," you will report full health right up until someone has to produce something.
4. **Distinguish decay from drift.** Some of what a user no longer has, they no longer need. Ask what has changed in their situation before you schedule a refresh, or your maintenance queue fills with obsolete items.
5. **Report graded state, not a binary.** Partial is the true answer almost always, and the interface that only offers complete or not will force you to lie in one direction.

## Apply to your product

- If a user came back after six months, which parts of their capability would you assume are intact and which would you re-check? Can your data model even express that difference?
- Is your staleness signal one timestamp per user, or per capability, per layer?
- How would you tell the difference between something a user forgot and something they stopped needing?

## See also

[[reactivate-dont-restart]] · [[give-mastered-things-a-visible-decay-state]] · [[what-protects-a-skill-through-a-lapse]]
