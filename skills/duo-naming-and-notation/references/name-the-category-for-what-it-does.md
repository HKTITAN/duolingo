---
name: duo-naming-and-notation-name-the-category-for-what-it-does
summary: Users read names as definitions and reason forward from them — name a category after an accident of one member and they will build a model you later have to demolish.
metadata:
  internal: true
---

# Name the Category for What It Does

## Concept

A name is not a label. Users treat it as a definition and reason forward from it, generating confident predictions about behaviour they have never observed. So a category named after a salient attribute of one member invites reasoning about that attribute — which is not merely useless but actively expensive, because the user spends effort building a model that has to be torn down later.

The companion rule is regularity. A compositional, derivable name is one rule; an irregular name is one item, and N irregular names are N items. Irregular names for the first few members of a series are historical accidents that every later user pays for, and — worse — they hide the pattern that governs everything after them.

## What Duolingo does

- Duolingo tells German learners outright that the three grammatical gender categories "could just as easily be called Category A, Category B, and Category C," and that they are "unrelated to human gender, sexuality, or identity." The name is doing active damage: it recruits a real-world concept that has no bearing on the behaviour.
- The third category's name does its own separate damage — calling it **"neuter"** makes learners think "it's more than just a third category," when it works exactly like the other two. German has **3** categories; Zulu has **19**, which is evidence that the count is arbitrary and the names are conveniences, not descriptions. Source: blog.duolingo.com/german-gender-der-die-das (Duolingo blog, 2022-10-04; accessed 2026-09-22)
- **The tension, and Duolingo takes the pragmatic side:** the post keeps using the misleading names throughout, because those are the terms the learner will meet everywhere else. You often cannot fix an established bad name. What you can do is pre-empt the wrong inference in the first paragraph, which is exactly what Duolingo does.
- On regularity: English **"eleven" and "twelve"** are frozen subtraction words (Old English *enleofan*, "one left" after ten) that break the *-teen* pattern, so the pattern only becomes visible at **13** — and in some languages not until 16. Japanese, Mandarin and Korean name 11-19 transparently as "ten-one," "ten-two," and Duolingo's math and language teams cite research (NCBI PMC7721146) that this transparency makes it easier for young children to start learning math. Tally marks grouped in fives date back nearly **30,000 years**. Source: blog.duolingo.com/words-for-eleven-twelve (Duolingo blog, 2024-06-11; accessed 2026-09-22)

## The transferable pattern

1. **Name by function, not by exemplar.** If your category is named after the first or loudest thing you put in it, every later member reads as an exception. Ask what the category *does* and whether that verb can be the name.
2. **Run the forward-inference test before shipping a name.** Show the name alone, with no definition, and ask people what they think it does. Whatever they say is what your name actually means. If their answer imports a concept from outside your system, the name is recruiting a model you will have to demolish.
3. **Make series names derivable.** If a user can generate the name of item N without being told it, you have shipped one rule instead of N facts — and they can name items you have not built yet.
4. **Irregular names at the start of a series are the expensive ones**, because they conceal the pattern that governs the rest. Sacrifice the elegant special-case label for positions one and two; the payoff compounds across every later position.
5. **Watch for the name that implies rank.** A label like "neuter", "basic", "legacy" or "advanced" adds an ordering the system does not have, and users then reason about that ordering. If the members are peers, the names must read as peers.
6. **When the bad name is already established elsewhere, keep it and pre-empt.** Renaming a term your users meet in every other tool trades one confusion for two. State the wrong inference explicitly and immediately, then use the standard name throughout — the correction is cheaper than the fork.

## Apply to your product

- Take your three most-used category names. Which was named after a member's attribute rather than the category's job? What does a new user predict from each one, and how wrong are they?
- Can a user derive the name of the next item in any of your series without being told? If not, what would the compositional scheme be, and what does the migration cost?
- Do any of your peer categories carry names that imply one ranks above another? What do users infer from that ordering, and is it true?
- Which of your names is wrong but standard in your industry? Have you written down the misinference, once, at the top of the doc — or are you letting each user find it alone?

## See also

[[motivated-form-and-one-symbol-one-thing]] · [[split-one-overloaded-primitive-into-named-senses]] · [[meaning-mutates-when-a-term-crosses-a-boundary]]
