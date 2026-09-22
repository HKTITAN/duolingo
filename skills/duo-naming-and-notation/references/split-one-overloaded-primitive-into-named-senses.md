---
name: duo-naming-and-notation-split-one-overloaded-primitive-into-named-senses
summary: When one primitive does five unrelated jobs, refuse to write the unifying definition — document each job with its own name and trigger condition instead.
metadata:
  internal: true
---

# Split One Overloaded Primitive into Named Senses

## Concept

Every system accumulates a primitive that does too much: one parameter, one status, one endpoint, one keyword that ended up covering five unrelated behaviours. The instinct when documenting it is to find the abstraction that covers all five. Resist that instinct.

An abstraction general enough to cover every sense is necessarily too vague to act on. It tells the user what the primitive *is* and nothing about **which behaviour fires in their case** — which is the only question they ever have. Five named senses with distinct trigger conditions turn one ambiguous rule into five decidable ones. The unified definition is elegant for you and useless to them.

## What Duolingo does

- Duolingo's guide to Spanish **"se"** rejects unification outright. It says plainly that it is more helpful to study each use and meaning separately, then splits a two-letter word into **5 named senses**, each with its own trigger rule and examples: reflexive *se*, pronoun-combination *se*, impersonal *se*, passive *se*, and accidental/no-fault *se*.
- The post also demonstrates why the unified definition would not have helped: one of those senses alone, in a single example sentence (*Ana se lo envía*), admits **8 valid readings**. No general statement about what *se* means narrows that down; only the trigger condition of a specific sense does. Source: blog.duolingo.com/5-meanings-of-spanish-se (Duolingo blog, 2024-08-22; accessed 2026-09-22)
- Note what Duolingo does **not** do: it does not propose renaming or redesigning the primitive. The senses are documented as they are, under names invented for the documentation, not for the system.
- **The tension:** naming five senses means maintaining five entries, and the names are yours, not the system's — so they can drift out of sync with the code, and a sixth behaviour can appear without anyone adding a sixth entry. An overloaded primitive with five documented senses is still an overloaded primitive; splitting it in the docs buys usability, not correctness. Where you control the design, [[motivated-form-and-one-symbol-one-thing]] argues for splitting the thing itself.

## The transferable pattern

When one element of your system has several unrelated behaviours:

1. **Enumerate the behaviours before you write a sentence about the element.** If the list has more than about three entries and they do not share a mechanism, you have an overloaded primitive rather than a flexible one.
2. **Give each behaviour a name of its own**, even if the system has no such name. A named sense is quotable in a bug report, searchable, and teachable. "The no-fault case" beats "the fifth meaning."
3. **Write the trigger condition, not the semantics.** For each sense, state the observable condition under which *that* behaviour fires. The user's question is always "which one am I in," never "what does this mean in general."
4. **Explicitly refuse the unifying definition, in the document.** Saying "these five do not share a single rule; work them separately" is information. A vague umbrella sentence is worse than nothing, because it looks like an answer and the user stops looking.
5. **Show a case that is genuinely ambiguous.** Demonstrating that one input admits several readings tells the user when to stop guessing and go ask — which is a real, actionable outcome.
6. **Own the drift.** Put the sense list next to the code that implements the behaviours, and make adding a sixth behaviour require adding a sixth entry.

## Apply to your product

- Which single field, flag, status or endpoint in your product would you struggle to define in one sentence? List its behaviours. Are they one mechanism or several wearing one name?
- For each behaviour, can you state the condition under which it fires — observable by the user, before they act? If you cannot, they certainly cannot.
- Is your current documentation for that primitive a general definition? What would break if you deleted the general definition and shipped only the named cases?

## See also

[[motivated-form-and-one-symbol-one-thing]] · [[name-the-category-for-what-it-does]] · [[document-the-failure-not-just-the-answer]]
