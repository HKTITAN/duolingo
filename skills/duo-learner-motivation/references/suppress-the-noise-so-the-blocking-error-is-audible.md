---
name: duo-learner-motivation-suppress-the-noise-so-the-blocking-error-is-audible
summary: Rank errors by whether they block the goal and demote the rest; flagging everything trains users to ignore everything, or to stop acting.
metadata:
  internal: true
---

# Suppress The Noise So The Blocking Error Is Audible

## Concept

Attention and tolerance for correction are finite budgets. Spend them on deviations that do not change the outcome and there is nothing left when a genuinely blocking error appears — the user has already learned to dismiss your flags.

There is a second cost that is worse. The accumulated sense of being constantly wrong suppresses exactly the production you were trying to increase. A system that surfaces every deviation does not produce careful users; it produces quiet ones.

## What Duolingo does

- On pronunciation, the guidance opens by telling users to **"focus on things that help you communicate, instead of trying to sound some particular way"** — an explicit instruction to ignore a whole class of deviation. Source: blog.duolingo.com/how-to-pronounce-french (Duolingo blog, 2025-08-26; accessed 2026-09-22)
- The grammatical gender column goes further and quantifies the blast radius. **"There are relatively few cases where using the wrong gender changes the meaning or keeps you from being understood, so it's ok to make mistakes!"** It then names the actual downside case — confusing *der Kiwi* (the bird) with *die Kiwi* (the fruit) — to show how narrow the real consequence is. Naming the worst case is what makes the permission credible; a bare "don't worry about it" is not. Source: blog.duolingo.com/learning-grammatical-gender-rules (Duolingo blog, 2026-03-31; accessed 2026-09-22)
- **The tension is unresolved in the corpus.** The same gender column spends roughly **2,800 words** teaching the rules it then tells you not to worry about. The honest position is that both are true at different moments — precision is worth building, and worth ignoring while you are mid-attempt — and Duolingo never says which mode a product should default to.
- Explicit permission to skip is treated as content in its own right. The reflexive-pronouns guide, after noting that English speakers are actively inventing new uses, says: **"that doesn't mean you have to learn them all — just practice the most common uses for the English you're learning."** The preterite guidance similarly says to start with the base pattern and add exceptions gradually. Source: blog.duolingo.com/reflexive-pronouns-in-english (Duolingo blog, 2026-05-06; accessed 2026-09-22)
- The target of that permission is not the struggling user. It is the competent one: **completionism is what stalls people who are already good**, because a user who believes the whole surface is required treats every unexplained edge case as a gap in their own competence.

## The transferable pattern

- **Rank every error your system can emit by whether it blocks the user's actual goal.** Most systems have never done this, which is why everything ships at the same severity.
- **Demote or suppress the non-blocking tier** on surfaces where production is the metric. Keep it available for users who go looking; do not push it.
- **Name the worst case concretely when you grant permission.** "This rarely matters, and here is the one time it does" is trusted. "Don't worry about it" is not.
- **Tell users explicitly what they may skip.** Naming the long tail as optional is as valuable as teaching the core, because it lets a user stop auditing themselves against a standard nobody meets.
- **Decide which mode each surface is in, and say so.** Precision mode and production mode want opposite defaults, and a surface that has not chosen defaults to precision by accident.

## Apply to your product

- List every warning, flag and validation your product emits. How many of them, if ignored, would still leave the user with a working result?
- Which parts of your surface area are genuinely optional, and where do you tell users that out loud?
- Which of your screens is for producing work and which is for checking it — and do they currently behave differently?

## See also

[[set-success-at-functional-adequacy]] · [[the-blocker-is-willingness-to-be-visibly-bad]] · [[../duo-voice/references/error-copy]]
