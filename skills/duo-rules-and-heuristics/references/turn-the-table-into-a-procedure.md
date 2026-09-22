---
name: duo-rules-and-heuristics-turn-the-table-into-a-procedure
summary: Replace an N-entry lookup table with an ordered question sequence plus worked traces, and say which slots are actually required.
metadata:
  internal: true
---

# Turn the Table Into a Procedure

## Concept

A flat table of N entries requires N separate retrievals with nothing to fall back on when one fails. An ordered sequence of questions has bounded branching at each step, so the user holds only one small choice in mind at a time — and a user who has forgotten the entry can still re-derive it. The same conversion has three companions that make it actually executable: a worked trace proving the procedure runs end to end, a named unit so the user does not substitute the visible surface unit, and an explicit statement of the minimum required subset so they can produce a valid output before they have learned all of it.

## What Duolingo does

- Italian has **11 article forms** (un, uno, una, un', il, l', lo, la, i, gli, le). Duolingo shows the table, then immediately replaces it with **4 ordered questions**: definite or indefinite? masculine or feminine? singular or plural? what sound does the next word start with? It also surfaces a form-level regularity that makes the first question free — every definite article contains an "l", every indefinite one starts with "u". Source: blog.duolingo.com/definite-and-indefinite-italian-articles (Duolingo blog, 2026-06-25; accessed 2026-09-22)
- Spanish negative commands are taught as a **4-step algorithm** — take the yo form, drop the -o, attach the opposite ending, add an -s — with **2 complete worked traces** (correr → corras, usar → uses), and the **14-verb** conjugation table only afterwards, as reference. Formal commands are then a one-line delta on the same procedure: same steps, don't add the -s. Source: blog.duolingo.com/just-do-it-how-to-make-commands-in-spanish (Duolingo blog, 2023-01-30; accessed 2026-09-22)
- German word order is taught as numbered slots — "the second slot of the sentence is always saved for a verb" — with an explicit warning that a slot is not a word: "it can be the second word, but it could also be the third, fourth, seventh, or even tenth word!" Source: blog.duolingo.com/german-sentence-structure (Duolingo blog, 2023-05-30; accessed 2026-09-22)
- The gustar formula is a **5-column** diagram of which only **2 columns are marked required** — "Me gusta" is a complete sentence — and the post closes by telling learners to learn the most important parts first and add the rest when ready. Source: blog.duolingo.com/verbs-like-gustar-in-spanish (Duolingo blog, 2023-10-05; accessed 2026-09-22)

**Tension.** A procedure shrinks the memorisation list rather than eliminating it: the commands post still concedes a short irregular set (ser, ir, ver) where no procedure works. And the slot template is admitted to be a simplification — "the whole story is more complicated than this, but this is the rule for all the basic sentences." You buy correctness on the common case at the price of eventual unlearning.

## The transferable pattern

When you find yourself writing a reference table, try converting it into an ordered decision sequence first:

1. **Find the question with the highest information gain** and ask it first. Each subsequent question should be answerable without holding the previous ones in mind.
2. **Ship at least one complete worked trace.** The trace is what proves the procedure is executable rather than merely stated, and it is the thing users copy. Two traces covering different branches is better than one.
3. **Name the unit the steps operate on**, explicitly, and warn where it differs from the obvious surface unit. Users default to whatever is visible — the word, the row, the file — and nearly every error follows from that substitution.
4. **Mark the minimum required subset.** A user who can produce one valid output immediately enters a feedback loop; one who must assemble every part before anything works never does. Find the two-element core inside the five-element schema and ship that first.

Keep the table. Just demote it to reference, underneath the procedure, where it belongs.

## Apply to your product

- What is the biggest lookup table in your docs, and what three or four ordered questions would select the right row?
- Does your configuration guidance include one complete worked example, or only a list of available fields?
- In your most complex object, which fields are genuinely required to get a working result — and does anything in your interface say so?

## See also

[[ship-the-shortcut-with-its-coverage-rate]] · [[fix-the-model-instead-of-memorising-the-exception]] · [[give-them-a-handle-they-can-hold-under-pressure]]
