---
name: duo-naming-and-notation-teach-a-choice-with-a-minimal-contrast
summary: Users fail either/or choices because they cannot map a live situation onto a category — show the same content under two conditions with only the deciding variable changed.
metadata:
  internal: true
---

# Teach a Choice with a Minimal Contrast

## Concept

When users repeatedly pick the wrong one of two options, the instinct is to write better definitions. That almost never helps, because the failure is not comprehension. They understand both definitions. What they cannot do is **map the situation in front of them onto a category** — and a definition is written in the vocabulary of the category, which is precisely the translation step they are stuck on.

A minimal contrast does the mapping for them: the same content shown under two conditions, with only the deciding variable changed. It makes the variable visually isolable, so the reader stops reasoning about definitions and starts pattern-matching on situations. The companion move is indexing: order the options along the variable the user is actually deciding, not along your internal taxonomy.

## What Duolingo does

- The demonstratives guide uses a "YOU SAY… / IF…" table rather than definitions. *"I love this shirt!"* against *"I love that shirt!"*, with the conditions spelled out beside each — "you're holding or wearing the shirt" versus "you are talking about someone else's shirt." **6 paired rows** hold the sentence constant and vary only the situation, resolving **4 demonstratives across 2 variables** (distance × number). No abstract definition of a demonstrative is given anywhere. Source: blog.duolingo.com/what-are-demonstratives (Duolingo blog, 2026-09-10; accessed 2026-09-22)
- On indexing by the live variable: the guide to French questions presents **3 grammatical structures ordered on a formality axis** — least formal (intonation), neutral (*est-ce que*), most formal (inversion) — with a lead graphic showing the **same five questions rendered in all three columns** side by side, plus a full table of **36 example sentences** in all three forms at the end. The structures are the taxonomy; formality is the decision, so formality is the ordering. Source: blog.duolingo.com/questions-in-french (Duolingo blog, 2025-12-03; accessed 2026-09-22)
- **The tension:** a minimal contrast is only honest when a single variable really is decisive. Where several variables interact, a paired table implies a cleanness the system does not have, and users will confidently apply it outside the region where one variable dominates. The demonstratives case needs two variables and two passes; forcing it into one would have been wrong. When you cannot isolate a variable, that is the signal to split into named cases instead — see [[split-one-overloaded-primitive-into-named-senses]].

## The transferable pattern

For any either/or in your product — which plan, which permission level, which export format, which mode:

1. **Hold everything constant except the deciding variable.** Same example, same data, same wording; one thing differs. The reader's eye finds the variable without being told what it is.
2. **State the condition, not the definition.** Each row gets the observable situation that selects it — "if you are holding it," "if the file will be re-imported," "if the recipient is outside your org" — phrased in the user's world, not in your category names.
3. **Order by the deciding variable, not by your internal structure.** Users arrive with a situation, not a taxonomy. Organising by internal structure forces them to first translate their situation into your categories, which is the exact step they came to you unable to do.
4. **Show every option against one identical example, side by side.** The parallel rendering is what makes the difference legible; separate examples per option hide it.
5. **Use enough pairs to cover the variable's range, then stop.** A handful of contrasts that span the decision beat an exhaustive list, which reverts to being a reference the user must again translate into.
6. **Skip the abstract definition entirely** when the contrast carries the meaning. If a reader can choose correctly, they do not need to be able to define the category, and asking them to learn one is a cost with no payoff.

## Apply to your product

- Which either/or choice generates your most repeated support question? Is your current documentation defining the two options, or contrasting them under one held-constant example?
- What is the single variable that decides it, phrased as something the user can observe about their own situation before they know your vocabulary?
- Is your options page ordered by your internal structure or by the axis users are actually deciding on? What would reordering it cost?

## See also

[[users-snap-the-new-thing-to-categories-they-already-have]] · [[document-the-failure-not-just-the-answer]] · [[ship-a-labelled-default-with-named-exceptions]]
