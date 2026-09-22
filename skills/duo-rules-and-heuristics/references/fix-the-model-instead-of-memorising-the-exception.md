---
name: duo-rules-and-heuristics-fix-the-model-instead-of-memorising-the-exception
summary: A repeated exception usually means the mental model is wrong — reframe so the correct behaviour becomes the intuitive one, and teach the parameter rather than the list.
metadata:
  internal: true
---

# Fix the Model Instead of Memorising the Exception

## Concept

An override competes with an intuition every single time the situation arises, and under time pressure the intuition wins. That makes "remember that X is special" a permanent tax rather than a fix. When users keep tripping over the same exception, the exception is usually evidence that the model you handed them is wrong. The better move is to look for a reframing under which their existing intuition produces the correct behaviour, so no ongoing suppression is required. The same economics run upward: where one setting predicts several downstream behaviours, teach the setting.

## What Duolingo does

- Rather than teaching "gustar" as a backwards verb with a memorised override, Duolingo tells learners to read it as literally **"to be pleasing to"** — "Me gusta la película" becomes "The movie is pleasing to me" and the agreement stops being weird. **1 reframe covers 5+ verbs**: encantar, emocionar, interesar and molestar come along for free. Source: blog.duolingo.com/verbs-like-gustar-in-spanish (Duolingo blog, 2023-10-05; accessed 2026-09-22)
- The Senior Curriculum Designer applies the same reframe to object pronouns: "my dress was pleasing to her" makes the indirect object the obvious choice, and the reframe transfers to encantar and interesar rather than being a one-off. Source: blog.duolingo.com/direct-indirect-objects-spanish (Duolingo blog, 2022-04-12; accessed 2026-09-22)
- Word order is taught as **one parameter, headedness**, rather than a catalogue: a language that puts the verb before its complement (head-initial) will probably also put prepositions before nouns; head-final languages use postpositions. Head-initial: English, French, Hawaiian, Irish, Italian, Portuguese, Spanish, Thai. Head-final: Hindi, Japanese, Korean, Persian, Turkish. Mixed: Dutch, German, Russian. Source: blog.duolingo.com/verb-order-headedness (Duolingo blog, 2025-05-27; accessed 2026-09-22)
- A cheaper cousin of the same move: the chess guide gives **3 different descriptions of one identical knight move** and tells the reader to use whichever makes the most sense to them, rather than asserting a canonical description. Source: blog.duolingo.com/knight-chess-piece (Duolingo blog, 2026-05-21; accessed 2026-09-22)

**Tension.** The headedness post is explicit that the parameter is a tendency, not a guarantee: "there are always exceptions," mixed languages show both patterns, and knowing the parameter "doesn't guarantee you'll see these patterns, it can be a useful guide." A generative rule shipped without that caveat produces confident errors — see [[ship-the-shortcut-with-its-coverage-rate]].

## The transferable pattern

Treat a recurring exception as a bug report about your mental model, not about your users.

**Before writing the override, spend an hour looking for the reframing.** The question is: under what description of this system does the correct behaviour become the obvious one? A good reframe is recognisable because it pays for itself — it also explains three neighbouring cases you were about to document separately. If your reframe covers exactly one case, it is an override wearing a costume.

**Look for the generating parameter.** Systems have correlated structure. If one setting predicts several downstream conventions, teaching the setting transfers to cases the user has never met, which a memorised list can never do. Ship the parameter with its reliability stated as a tendency, not a law.

**Do not insist on one canonical framing.** Different users have different existing structures to attach a new idea to. Offering two or three equivalent descriptions and inviting the user to pick costs a paragraph and makes the idea reachable for people whose prior model does not fit your favourite phrasing.

Boundary: this skill covers representations you invent to teach with. Anchoring a new concept to a system the user already brings from somewhere else is transfer, and belongs elsewhere.

## Apply to your product

- What is the exception your users hit most often? What would have to be true about your model for that behaviour to be the default rather than the exception?
- Is there a single setting in your system that predicts several behaviours users currently learn one by one?
- Have you ever explained a core concept two different ways and watched which one landed with which kind of user?

## See also

[[name-the-arbitrary-and-kill-the-folk-theory]] · [[turn-the-table-into-a-procedure]] · [[ship-the-shortcut-with-its-coverage-rate]]
