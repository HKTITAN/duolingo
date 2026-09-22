---
name: duo-prior-knowledge-transfer-interference-clusters-among-near-neighbours
summary: Confusion concentrates between things that are almost the same, and the near-misses produce confident errors with no detection signal.
metadata:
  internal: true
---

# Interference Lives Among Near Neighbours

## Concept

Interference is not caused by difficulty; it is caused by similarity. Near neighbours share most of their associative connections, so retrieving one partially activates the other and the stronger habit wins. Distant items share nothing, so there is nothing to mis-select — which is why moving from a near-identical competitor is harder than arriving with no model at all. The worst case is the false friend: where two things look identical but behave differently, the prior fires anyway and produces a **confident** error with no signal that anything is wrong. The user never looks it up, because nothing prompted them to.

## What Duolingo does

Source: blog.duolingo.com/transfer-from-first-language (Duolingo blog, 2023-01-10; accessed 2026-09-22)

- Duolingo explains why Spanish speakers struggle *more* with Portuguese than with a distant language: shared cognates connect the two by both sound and meaning, keeping both "volumes" up, and shared grammar makes the wrong rule feel plausible. Similarity is the cause of the interference, not a mitigation of it.
- The framing is symmetric and explicit — "Transfer can be helpful if the properties are the same across the languages, but can present a challenge if they differ." The pronunciation guidance applies it concretely, warning that "your brain naturally wants to use the pronunciations it knows best" and singling out **universidad** and **decisión** — words that look identical to their English counterparts but carry different stress — as the specific hazard (blog.duolingo.com/whats-the-easiest-language-to-learn (Duolingo blog, 2026-08-20; accessed 2026-09-22)).
- Because users will not discover false friends on their own, Duolingo tells learners of two similar systems to spend dedicated weekly time on deliberate contrast — **false-cognate lists** (*burro* is a donkey in Spanish and butter in Italian) and comparison charts for divergent grammar — rather than trusting exposure to surface them. Course designers use the same move, deliberately contrasting similar-yet-different structures so the difference becomes noticeable (blog.duolingo.com/can-you-learn-two-languages-at-the-same-time (Duolingo blog, 2025-02-05; accessed 2026-09-22)).
- Tension: distance is not a free fix. Picking two unrelated things means less confusion **and** less transferable leverage between them. Similarity buys speed at the cost of confusability, and the post is clear that there is no free choice — you pick which problem you want.

## The transferable pattern

- **Predict confusion by similarity, not by complexity.** Your hardest support tickets will cluster around near-matching names, adjacent states, almost-identical settings and endpoints that differ in one argument.
- **Treat near-misses as your most expensive errors.** A wholly unfamiliar feature produces a hesitant user who asks or reads. A near-identical one produces a confident user who is wrong and does not know it, so the error surfaces late and costs more to unwind.
- **You cannot rely on discovery for false friends.** Nothing feels wrong, so nothing triggers a lookup. They have to be flagged explicitly, at the moment of use, in the interface — not buried in a migration appendix.
- **Maintain an actual list.** Enumerate every place where your thing looks like the prior system and behaves differently. That list is a product artifact, not a doc chore — it drives your empty states, your warnings and your onboarding.
- **Name the near-neighbour at the moment of choice.** A warning that fires where the two things are actually confusable beats a comprehensive reference nobody opens, because the user has no idea they need it.
- **Remember the trade you are making.** Deliberately resembling an incumbent buys instant fluency on everything that matches and buys confusion on everything that does not. Both arrive together.

## Apply to your product

- Which two things in your product get mixed up most often, and how many properties do they share? If it is most of them, contrast is the fix, not clearer documentation of each.
- Where does your product look exactly like the tool your users came from and behave differently? Write that list out — how many entries surprised you?
- Are your migration docs organized by *your* feature set or by *their* prior system's concepts? Only the second ordering can warn about a false friend.

## See also

[[train-the-contrast-not-the-items]] · [[mismatched-mappings-make-errors-structural]] · [[difficulty-is-distance-from-what-they-already-know]]
