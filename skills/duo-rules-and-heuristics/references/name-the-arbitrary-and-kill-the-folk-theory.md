---
name: duo-rules-and-heuristics-name-the-arbitrary-and-kill-the-folk-theory
summary: Label genuinely arbitrary conventions as arbitrary and falsify the plausible folk explanation, because asserting arbitrariness does not dislodge a story users already believe.
metadata:
  internal: true
---

# Name the Arbitrary and Kill the Folk Theory

## Concept

Humans attach a story to any unexplained convention. The story is then applied to new cases and produces confident errors — worse than not knowing, because the user has no reason to check. So when a rule in your system is genuinely arbitrary, say so out loud: the label tells the user to memorise rather than derive, which is faster and generates no wrong generalisations. But the label alone is not enough. Merely asserting that something is arbitrary does not dislodge a story someone already believes; you have to name the folk theory and show it failing. And the inverse case matters just as much — when users wrongly believe a system is arbitrary, they stop searching for patterns entirely, and the highest-value content you can ship is proof that rules exist.

## What Duolingo does

- The grammatical gender post states flatly that gender is mostly arbitrary and mostly unrelated to meaning, then runs an embedded **true/false pop quiz on the most common folk theory** — that "casa" is feminine because the home was a woman's space — and falsifies it with **3 counterexample languages**: Russian "dom" is masculine, German "Haus" is neuter, and Spanish itself has feminine "casa" but masculine "hogar". Source: blog.duolingo.com/what-is-grammatical-gender (Duolingo blog, 2026-03-03; accessed 2026-09-22)
- Where there is no derivable rule at all, the remaining lever is retrieval cost. Duolingo resolves make/do with two backronyms — MAKE = Money, Arrangements, Keep (things you can touch), Eat; DO = Daily tasks, Occupations — **4 MAKE categories and 2 DO categories** — and then names the limit: "this memory trick will help you learn the most important and most frequent uses of these verbs." Source: blog.duolingo.com/difference-between-do-and-make-in-english (Duolingo blog, 2025-09-15; accessed 2026-09-22)
- The inverse move: the French pronunciation guide opens by inverting the learner's premise — unlike English, where "ough" has **4 different pronunciations** (thought, through, thorough, trough), French pronunciation is predictable from spelling — and then delivers decision procedures rather than lists, plus the CaReFuL mnemonic for the **4 final consonants** that get pronounced. Source: blog.duolingo.com/how-to-pronounce-french (Duolingo blog, 2025-08-26; accessed 2026-09-22)

**Tension.** Duolingo simultaneously publishes a companion post on gender patterns worth looking for. Arbitrary at the level of meaning does not mean patternless at the level of form — but the two messages can cancel each other out, and a user who reads them in the wrong order ends up either memorising what they could have derived or deriving what they should have memorised. If you send both messages, scope each one explicitly.

## The transferable pattern

For every convention in your system, decide which of three categories it is in and say so:

- **Rule-governed** — teach the rule, and if users currently believe otherwise, lead by naming the contrast case that gave them the wrong impression. Belief in arbitrariness kills pattern search, and restoring it changes the user's processing strategy for every item afterwards.
- **Arbitrary but structured at the surface** — no reason behind it, but there are patterns in the form. State both boundaries, or the two messages will cancel.
- **Genuinely arbitrary** — a historical accident, a vendor constraint, a decision nobody would make again. Label it. The label is not an apology; it is instruction to stop deriving and start memorising.

For that third category, the only remaining lever is retrieval cost. Compress the set into one handle a user can hold, and say openly that the handle is lossy and covers the frequent cases — a mnemonic presented as complete gets applied confidently outside its coverage, which is worse than no mnemonic.

And pre-empt the story. Ask two or three users why they think the rule exists. Whatever they say is the folk theory; write the counterexample that kills it into your documentation.

## Apply to your product

- Which of your conventions are genuinely arbitrary, and does anything you have written say so?
- What story do users tell themselves about why one of your rules exists — and what is the cleanest counterexample that falsifies it?
- Is there anywhere users believe your system is random when it is actually predictable? What is the one contrast case that convinced them otherwise?

## See also

[[give-them-a-handle-they-can-hold-under-pressure]] · [[fix-the-model-instead-of-memorising-the-exception]] · [[ship-the-shortcut-with-its-coverage-rate]]
