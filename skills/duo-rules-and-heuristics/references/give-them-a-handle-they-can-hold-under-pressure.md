---
name: duo-rules-and-heuristics-give-them-a-handle-they-can-hold-under-pressure
summary: The failure mode is retrieval at the decision point, so compress the rule into an acronym, a surface cue, a named pattern or a bundled chunk.
metadata:
  internal: true
---

# Give Them a Handle They Can Hold Under Pressure

## Concept

The usual failure is not misunderstanding. It is retrieval under time pressure. A long correct explanation lives in the document; a five-letter handle lives in the head and can be scanned against a live situation in about a second, which is all the time the user has. Four kinds of handle do this work: a compressed mnemonic, a cheap surface cue that correlates with the right decision, a named pattern that turns slow search into fast recognition, and a bundled chunk that stores an inseparable attribute with its item so it can never be separately forgotten.

## What Duolingo does

- **Mnemonics.** Duolingo built **4 acronyms for 2 binary choices**: DOCTOR (Date, Occupation, Characteristics, Time, Origin, Relationships) for ser vs PLACE (Position, Location, Action, Condition, Emotions) for estar; DREAM (Duration, Reason, Exchange, Action, Means) for por vs PERFECT (Purpose, Effect, Recipient, Future dates, Employment, Conclusion, Toward) for para — **6+5 and 5+7 uses** respectively. Source: blog.duolingo.com/por-vs-para (Duolingo blog, 2022-11-22; accessed 2026-09-22)
- **Surface cues.** Nearly every grammar guide ships a "signal words" block: "todos los días / en aquella época / siempre" flag the Spanish imperfect, and learners are told to start their own keyword list as they go. A cue is checkable in one glance and requires no model of the system. Source: blog.duolingo.com/imperfect-tense-spanish (Duolingo blog, 2023-05-23; accessed 2026-09-22)
- **Bundled chunks.** Never write a bare noun on a flashcard: write "la casa", better "la casa rossa", so multiple words carry the agreement — plus a selection rule, choose adjectives with visible endings rather than invariant ones like Italian "blu", so the chunk actually encodes the attribute. Source: blog.duolingo.com/learning-grammatical-gender-rules (Duolingo blog, 2026-03-31; accessed 2026-09-22)
- **Whole units where parts mislead.** The Japanese "no" post enumerates **7+ distinct uses of one two-letter particle** and, for weather phrases, instructs learners to store the whole phrase rather than each part, because there is no word-for-word equivalent to decompose into. Source: blog.duolingo.com/japanese-particle-no (Duolingo blog, 2023-05-25; accessed 2026-09-22)
- **Opaque chunks used before they are understood.** Beginners get **4 phrases as fixed combinatorial slots** — hay, necesito, tengo que, me gustaría — and are told explicitly that it is fine to use "me gustaría" without understanding the pronoun and conditional ending inside it. Source: blog.duolingo.com/common-spanish-phrases-for-sentences (Duolingo blog, 2025-05-08; accessed 2026-09-22)
- **Named patterns.** The chess course teaches named mating motifs (back rank, smothered, Damiano's, Arabian) while stating that learning the names is not necessary — the value is spotting the configuration you would otherwise miss. Source: blog.duolingo.com/how-to-checkmate-in-chess (Duolingo blog, 2026-08-27; accessed 2026-09-22)

**Tension.** The acronyms are lossy, and both posts hedge with "some of the most common uses." A handle is a heuristic that will be wrong at the edges, so it has to ship with its limits stated ([[ship-the-shortcut-with-its-coverage-rate]]) or users apply it confidently outside its coverage.

## The transferable pattern

For any decision your users must make in the moment, the deliverable is not the explanation. It is the handle.

- **Compress to something holdable.** An acronym, a two-word name, a single question. If it does not fit in one breath, it will not be there at the decision point.
- **Give a cheap surface cue** that correlates with the right answer, so users can act correctly before they understand why. Cue-following is a legitimate intermediate stage: correct behaviour generates the exposure from which the real model is later induced.
- **Name your recurring patterns**, even if the names are never required knowledge. A labelled pattern library converts search into recognition and transfers to adjacent situations you never taught.
- **Bundle inseparable attributes into one unit.** Two facts require two retrievals and the second fails under pressure. Where meaning is not derivable from parts, store the whole thing and let users operate it as an opaque block — capability now, comprehension later.

Always ship the handle with its coverage, so being wrong at an edge does not discredit it.

## Apply to your product

- What is the decision your users make most often under time pressure, and what is the handle for it? If your answer is a paragraph, you do not have one yet.
- What one-glance cue in your interface correlates with the right choice, and is it visible at the moment of choosing?
- Which two facts do your users have to retrieve separately that could be stored as one unit?

## See also

[[ship-the-shortcut-with-its-coverage-rate]] · [[name-the-arbitrary-and-kill-the-folk-theory]] · [[turn-the-table-into-a-procedure]]
