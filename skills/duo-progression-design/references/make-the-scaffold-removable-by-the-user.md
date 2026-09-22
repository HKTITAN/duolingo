---
name: duo-progression-design-make-the-scaffold-removable-by-the-user
summary: Ship a visible off switch for the training wheels and label them temporary; accept that many users never flip it.
metadata:
  internal: true
---

# Make the Scaffold Removable by the User

## Concept

A fixed scaffold has to guess. Set it high and strong users are held back and bored; set it low and weak users fall off. A user-toggled scaffold stops the system from having to infer readiness at all — each person sits at their own edge and moves when they feel the support has become slack. Two things make the toggle work rather than decorate the settings screen: it has to be visible at the moment of use, not buried in preferences; and the scaffold has to be *named as temporary* when it is introduced. A support presented as permanent truth gets clung to, and then resented when reality contradicts it.

## What Duolingo does

Source: blog.duolingo.com/japanese-writing-systems (Duolingo blog, 2026-07-21; accessed 2026-09-22)

- The Japanese course shows **romaji** — Roman-letter pronunciation — alongside hiragana and katakana **from the very first exercise**, so a beginner does real lessons before knowing a single character. Three writing systems are taught (hiragana, katakana, kanji); romaji is a **fourth, optional layer** that exists only to be removed.
- Romaji can be switched off **in settings or mid-lesson**. Hiragana can likewise be displayed as a pronunciation guide over kanji and then turned off. The scaffold is not gating the real task; it is riding alongside it.
- **The honest cost, which the post itself frames:** turning romaji off is presented as an extra challenge learners take on "when they feel comfortable" — which means many never will, and for those users the temporary layer is permanent.
- The same pattern in writing practice: word-bank exercises carry a **keyboard icon in the bottom-left** so a learner can abandon the bank and type the answer unaided, with the explicit advice "don't rely on word banks in translation exercises!" The escape hatch is on the exercise, one tap away (blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-writing-skills (Duolingo blog, 2026-07-02; accessed 2026-09-22)).
- Duolingo also labels its scaffolds as disposable at the point of teaching. It hands beginners a slot formula (Subject + Verb + Object) framed explicitly as a trick "you will not need for long," then immediately shows that this order is not even the most common one worldwide — **SOV is**, and OVS and OSV are used by only a handful of languages (blog.duolingo.com/how-to-make-sentences-in-spanish-french (Duolingo blog, 2025-04-11; accessed 2026-09-22)).

## The transferable pattern

Prefer a removable support over a gate. Gating the real task behind proving mastery of a prerequisite delays the first success and the feedback loop that motivates everything after it. A removable support keeps the loop and converts the eventual removal into a challenge the user chose.

Design rules that make the toggle real:

- **Put the control where the work happens.** One tap from the task, in the same surface, at the moment the user notices the support is unnecessary. A settings-screen toggle is a toggle nobody finds.
- **Say it is temporary when you introduce it.** "This is a simplification you will outgrow" costs one sentence and buys you the credibility to be inexact.
- **Show the boundary.** Immediately demonstrating a case the simplification does not cover pre-empts the credibility hit later and tells the user what "outgrowing it" looks like.
- **Instrument the off switch.** If almost nobody flips it, your users are not ready, the control is invisible, or turning it off has no visible payoff. Those need different fixes.

The tradeoff to accept up front: user-controlled removal means some users never remove it. If the capability is high-consequence, do not rely on a toggle — schedule the fade yourself.

## Apply to your product

- Which support in your product is a gate that could be a removable training wheel instead, letting users start the real task in their first session?
- Where is the off switch, and what fraction of users have ever found it? If the number is near zero, is that a readiness problem or a placement problem?
- Which of your simplifications are presented as permanent truths? What one sentence would mark each as temporary, and which counterexample would you show alongside it?

## See also

[[scaffold-and-fade-on-a-schedule]] · [[do-the-real-thing-badly-on-day-one]] · [[pick-one-variant-and-name-the-choice]] · [[front-load-the-context-a-later-rule-will-need]]
