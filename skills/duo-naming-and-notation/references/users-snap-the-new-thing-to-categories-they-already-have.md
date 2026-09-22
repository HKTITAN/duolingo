---
name: duo-naming-and-notation-users-snap-the-new-thing-to-categories-they-already-have
summary: People perceive anything new through the distinctions they already hold — what falls between two of their categories gets rounded to one silently, and the rounded version is what they remember and repeat.
metadata:
  internal: true
---

# Users Snap the New Thing to Categories They Already Have

## Concept

Perception is categorical. The inventory of distinctions someone already holds determines which distinctions they can register at all in new input. A feature of your system that falls between two of a user's existing categories does not register as "something new" — it gets rounded to the nearer category, silently, without the user noticing they discarded information. And the rounded version is what they remember, repeat to colleagues, and build on.

The consequence for design is blunt: **perceived difficulty is mostly distance from the known, not intrinsic complexity.** Conformity to whatever your users already use buys more perceived simplicity than cutting your rule count does.

## What Duolingo does

- The animal-sounds post works as a controlled experiment on rounding. The pig makes the same physical sound everywhere; each language renders it using only the sounds its own system permits. English *oink* uses the diphthong from "oil"; Polish *chrum* opens with a sound that does not exist in English at all. Same input, different discretisation, and no speaker experiences their version as an approximation. **20+ languages compared across 7 animals.**
- Duolingo then looks past the surface variation for the invariant: English *oink*, French *groin*, Indonesian *ngok* and Polish *chrum* all share **3 phonetic features** — a mid vowel, a nasal, and a back consonant. The signal survives the rounding; the surface does not. Source: blog.duolingo.com/animal-sounds-in-different-languages (Duolingo blog, 2023-11-22; accessed 2026-09-22)
- On difficulty as distance: Duolingo's linguists argue all languages are roughly equally complex and the complexity merely sits in different places — Vietnamese has no inflections but is tonal; Inuktitut packs whole clauses into a single word — so what feels hard depends almost entirely on what the person already knows. Source: blog.duolingo.com/language-irregularity-and-complexity (Duolingo blog, 2025-09-16; accessed 2026-09-22)
- **The tension, from the same post:** the reverse illusion is just as real. A system closely related to what you already know feels straightforward only because you have not yet reached the parts that differ. Early ease in a near-neighbour system is a false signal, and it sets up the trap described in [[near-matches-are-more-dangerous-than-unknowns]].

## The transferable pattern

1. **Before simplifying, ask whether the thing is complex or merely unfamiliar.** These have opposite fixes. Genuine complexity is fixed by removing rules. Unfamiliarity is fixed by moving toward prior art — and removing rules from an unfamiliar system often makes it stranger, not simpler.
2. **Name your users' prior system explicitly and steal its conventions** wherever the semantics genuinely match. The imported convention costs you a design compromise once; it saves every user a category they would otherwise have to build.
3. **Expect rounding and go looking for it.** In user research, do not ask whether they understood. Ask them to describe the feature back and watch which of their existing categories they used. The gap between their description and yours is the information that got discarded.
4. **Distrust early-adoption ease when you are a near-neighbour of a known system.** Low friction in week one predicts nothing about week six, because the divergent parts have not been reached yet. Instrument the later sessions instead.
5. **Name the thing they rounded you to, then state the difference.** If every user files your feature under the same familiar category, say so explicitly — "it is like X, except" — rather than fighting for a clean slate you were never going to get.
6. **Look for the invariant under the variation.** When different groups round your feature differently, the shared residue across all their versions is the part that actually transmitted. Build the explanation on that.

## Apply to your product

- Ask three users to describe your newest concept in their own words, without your term for it. Which existing thing did each one snap it to? Those are the categories you are actually shipping into.
- Is your hardest-rated feature genuinely intricate, or just unlike anything your users have met? Check before you simplify it — the two diagnoses lead to opposite work.
- If your feature is consistently rounded to one familiar category, does your own documentation admit that and state the difference — or does it insist the feature is new?
- Where have you invented a convention that a dominant tool in your users' stack already solved? What does your version buy that is worth the retraining?

## See also

[[near-matches-are-more-dangerous-than-unknowns]] · [[meaning-mutates-when-a-term-crosses-a-boundary]] · [[teach-a-choice-with-a-minimal-contrast]]
