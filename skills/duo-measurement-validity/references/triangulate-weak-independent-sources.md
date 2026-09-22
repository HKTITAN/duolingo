---
name: duo-measurement-validity-triangulate-weak-independent-sources
summary: Three imperfect signals whose biases fail in different ways beat one that fails silently, and disagreement between them localises the error.
metadata:
  internal: true
---

# Triangulate Weak Independent Sources

## Concept

On the questions that matter most, there is often no single authoritative measurement and there never will be. Waiting for one is a decision to have no answer. Several weak sources whose biases are uncorrelated do better than one strong-looking source whose bias you cannot see, because agreement across mechanisms that fail differently is hard to produce by accident, and disagreement tells you which mechanism broke. The requirement is not quality, it is independence of failure mode. Three flawed instruments wired to the same underlying assumption are one flawed instrument.

## What Duolingo does

Source: blog.duolingo.com/how-languages-used-to-be-pronounced (Duolingo blog, 2024-10-29; accessed 2026-09-22)

- Nobody recorded Middle English, so the outcome is unobservable in principle. Linguists reconstruct it from **three independent lines of evidence within the language**, each weak on its own — modern pronunciations compared across many surviving dialects, the misspellings people made for a given word (a misspelling encodes what the writer heard), and what contemporary writers said about how words sounded.
- Each source fails in a different direction. Modern dialects have drifted; misspellings are sparse and inconsistent; contemporary commentary is opinionated and describes prestige speech. Because those failures are unrelated, convergence across all three is informative in a way that any one of them could not be.
- A fourth constraint comes from outside the language entirely — comparison with related languages, restricted by **three named regular sound-change patterns**: final devoicing, intervocalic voicing, and voicing assimilation. A reconstruction that violates a known regularity is ruled out regardless of how well the other sources agree.
- The tension Duolingo states plainly is that this never produces certainty. There is always some degree of uncertainty, and far more is known about some languages than others — so the honest output is a range, and the range is wider for the cases with fewer surviving sources. Triangulation narrows a range; it does not collapse one.

## The transferable pattern

- **Inventory your sources by failure mode, not by quality.** Ask of each one, what would make this wrong? If two sources answer the same way, they are one source and you should stop counting them twice.
- **Accept weak inputs deliberately.** A support-ticket theme, a sales-call pattern, a usage curve and a small survey are each dismissible alone. Together, if they fail differently and agree, they are a result you can act on.
- **Treat disagreement as the most valuable output.** Convergence gives you a number; divergence tells you which instrument is broken, which is usually the more actionable finding and the one teams skip past.
- **Add an external regularity as a hard constraint.** A known conservation rule, an accounting identity, a physical limit, a rate that cannot exceed its parent — any of these vetoes a conclusion that all your soft sources agreed on, and that veto is the cheapest error check you have.
- **Write down what each source would say if the answer were the opposite.** A source that predicts the same reading either way is decoration, and it will still make the set of three look reassuringly full.
- **Report a range with its width justified.** The width is the honest carrier of how much evidence you actually have, and a point estimate quietly discards it.

## Apply to your product

- Name the most important quantity in your business that nobody can measure directly. What are three signals about it that fail for unrelated reasons?
- Which two of the numbers you currently treat as independent confirmation actually come from the same pipeline or the same assumption?
- Is there a hard constraint — an identity, a ceiling, a conservation rule — that any answer must satisfy, and do you check your conclusions against it before publishing them?

## See also

[[sample-cases-that-could-not-have-influenced-each-other]] · [[resemblance-is-not-lineage]] · [[../duo-experimentation/references/ladder-of-evidence]]
