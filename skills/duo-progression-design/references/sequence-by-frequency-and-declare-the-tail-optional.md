---
name: duo-progression-design-sequence-by-frequency-and-declare-the-tail-optional
summary: Derive the high-frequency head from a real corpus, teach it first, and say out loud that the long tail is not required.
metadata:
  internal: true
---

# Sequence by Frequency, Declare the Tail Optional

## Concept

Natural systems are long-tailed. A small head covers most real encounters, and head items compound — once you hold them, you can infer much of the rest from context. That makes frequency a better first-pass ordering than any taxonomy. Two things separate this from folklore. First, derive the head from a real corpus of actual usage rather than from what feels common to the expert who built the product; intuition systematically over-weights the interesting and under-weights the boring. Second, say explicitly that the tail is optional. Completeness anxiety is what pushes users to attempt the whole inventory and then quit, and only you can give them permission to stop.

## What Duolingo does

Source: blog.duolingo.com/expressions-academic-english (Duolingo blog, 2025-01-15; accessed 2026-09-22)

- Duolingo publishes **the 20 most frequent academic phrases** drawn from the **Cambridge Academic English Corpus — 3 million words** of lectures, seminars, presentations, journals, essays and textbooks from U.K. and U.S. institutions. The head is measured, not guessed.
- The permission is stated in the post itself: **"you don't need to know every one of these expressions to succeed in an academic setting."** Twenty items, and even those are not all mandatory.
- The same rule is applied personally rather than globally in the dialect guidance — start from your own daily routine ("Is it at the supermarket? At work? With friends?"), because becoming familiar with high-frequency items makes it easier to work out the rest from context. Your corpus should be the user's context, not the domain's average (blog.duolingo.com/arabic-dialects (Duolingo blog, 2023-11-09; accessed 2026-09-22)).
- **Expect the head itself to have structure.** Duolingo's learning research finds that learners recognize and use **content words (nouns, verbs, adjectives) more easily than function words (pronouns, conjunctions, articles, auxiliaries)**, and that a content-words-only sentence is still comprehensible while being ungrammatical — which is exactly why common mistakes concentrate in the function layer long after the content layer is solid (blog.duolingo.com/are-some-words-unnecessary (Duolingo blog, 2024-05-14; accessed 2026-09-22)).

## The transferable pattern

Two steps, in order.

**Measure the head.** Pull a corpus of what your users actually encounter — support tickets, query logs, real documents, session recordings, the API calls that are actually made — and rank by frequency. Then compare that ranking to your current teaching order. The mismatch is usually large and usually in the same direction: the reference-ordered curriculum front-loads things that are structurally first and empirically rare.

**Declare the tail.** Put a line in the product that says the remaining inventory is optional. This feels like undermining your own content and it is the highest-leverage sentence on the page, because the alternative is a user who reads the length of the list as the size of the commitment and closes the tab.

Then expect the head to decompose the same way. Users acquire the *objects* of a system — the things they can point at and verify — before its *connectives*, the elements whose meaning is purely relational and which therefore require the surrounding structure to already be in place. A list of objects is usable while being malformed, which is why errors cluster in the connective layer long after the object layer looks solid. Plan a separate, later pass on connectives rather than expecting them to arrive with everything else.

Where frequency fails: a rare item with a catastrophic cost outranks a common item with none. Frequency is the first pass; consequence is the override.

## Apply to your product

- What corpus of real user encounters could you rank by frequency today? How far does that ranking diverge from your current teaching order?
- What is the sentence in your product that tells users the rest is optional? If there isn't one, where would it go?
- Which parts of your domain are objects the user can point at, and which are purely relational? Are you teaching them in the same pass?

## See also

[[rank-what-you-teach-by-cost-of-getting-it-wrong]] · [[sequence-by-task-not-by-taxonomy]] · [[structured-coverage-catches-what-use-never-surfaces]] · [[borrow-an-external-standard-as-the-spine]]
