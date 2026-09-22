---
name: duo-naming-and-notation
description: How to name things, design symbols, and write reference material so users derive the answer instead of memorizing it — and how to handle the near-misses, overloaded tokens and silent misreadings that produce confident wrong behaviour. Use when asking what should we call this, why do users keep confusing these two things, what do our status icons actually mean to people, how do I document a rule that has exceptions, how should this reference page be ordered, which rows need a warning, why does support keep answering the same question, how do I write an error explanation that fixes the user's model, or what happened to our term after another team started using it. Covers notation redesign, motivated form, false friends, overloaded primitives, symbol ambiguity, labelled defaults, selective marking, and minimal contrasts.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Naming and Notation — Map of Content

Most "users don't understand the product" problems are not comprehension problems. They are notation problems: a name that invites a wrong inference, a symbol whose meaning is set by somebody else's community, a primitive doing five jobs under one label, a table whose uniform typography promises a reliability you do not have.

This skill covers the part of the work that happens in names, symbols and reference material — before the user acts, not during. It owns what a symbol **means**, not how it is drawn, and not what the interface says back the moment something goes wrong.

Scan the descriptions, follow only the `[[wikilinks]]` you need.

## Designing the notation

- [[references/redesign-the-notation-dont-scale-the-training]] — training cost is paid per user forever; when adoption is blocked by learning cost, change the notation, and let a fluent user design it.
- [[references/motivated-form-and-one-symbol-one-thing]] — make each element's form encode what it does, and hold one symbol to one meaning (but only for distinctions users act on).
- [[references/name-the-category-for-what-it-does]] — users reason forward from names; regular compositional names are one rule instead of N facts.
- [[references/split-one-overloaded-primitive-into-named-senses]] — when one thing does five jobs, refuse the unifying definition and document five trigger conditions.

## How users actually receive it

- [[references/near-matches-are-more-dangerous-than-unknowns]] — familiarity suppresses checking, so the near-miss is the silent error and the alien token is the easy one.
- [[references/users-snap-the-new-thing-to-categories-they-already-have]] — anything falling between two of a user's existing categories gets rounded to one, silently.
- [[references/meaning-mutates-when-a-term-crosses-a-boundary]] — the receiving team re-reads your term as a modifier, then generalises it somewhere you never meant.
- [[references/your-symbol-set-is-not-a-shared-language]] — a large minority reads any symbol with a different or opposite valence, and cannot tell that they did.

## Writing the reference material

- [[references/ship-a-labelled-default-with-named-exceptions]] — label the coverage boundary instead of shipping a false universal or a useless hedge; tier inside the document.
- [[references/teach-the-invariant-the-exception-preserves]] — find what an exception is protecting and teach that; name the arbitrary residue as arbitrary.
- [[references/mark-only-what-deviates-and-force-the-unambiguous-form]] — flag exactly the unreliable rows, and where conventions collide, refuse to emit the ambiguous form.
- [[references/document-the-failure-not-just-the-answer]] — enumerate the real failure modes with recovery cues, attach limits inline, and name the false belief rather than the right answer.
- [[references/teach-a-choice-with-a-minimal-contrast]] — hold everything constant but the deciding variable; index by the decision, not by your taxonomy.

## Where to start

- Users keep making the same mistake → [[references/document-the-failure-not-just-the-answer]], then [[references/near-matches-are-more-dangerous-than-unknowns]].
- You are naming something new → [[references/name-the-category-for-what-it-does]], then [[references/motivated-form-and-one-symbol-one-thing]].
- A doc keeps being wrong in the field → [[references/ship-a-labelled-default-with-named-exceptions]], then [[references/mark-only-what-deviates-and-force-the-unambiguous-form]].
- Onboarding keeps getting longer and adoption does not move → [[references/redesign-the-notation-dont-scale-the-training]].

## Sibling skills

- [[../duo-voice/SKILL]] — the wording layer. This skill decides what a thing is called; that one decides how the product talks about it, including live error copy.
- [[../duo-design/SKILL]] — the visual layer. This skill owns what a symbol means; that one owns how it is drawn, animated and shown on screen.
- [[../duo-product/SKILL]] — whether the concept should exist at all, before you name it.
- [[../duo-experimentation/SKILL]] — how to test whether a renaming or a restructured reference page actually moved behaviour.

## Sources

blog.duolingo.com — writing-system history (Hangeul, Cherokee, Adlam), the IPA, Cyrillic and false cognates, Japanese loanwords, Spanish *se*, preterite spelling changes, accent marks, tú/usted, demonstratives, French question structures, German gender, double names, the Duolingo/Slack emoji survey, and the calendar and pronunciation guides. Every claim carries a dated citation inside its node.
