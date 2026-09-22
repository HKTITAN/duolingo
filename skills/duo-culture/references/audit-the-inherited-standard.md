---
name: duo-culture-audit-the-inherited-standard
summary: Which variant became "the standard" records who held authority when it was written, not which variant was better.
metadata:
  internal: true
---

# Audit the Inherited Standard

## Concept

Every team inherits rules nobody in the room chose: a style guide, a lint config, a review checklist, a "best practice" that arrived with a previous hire. Each comes with a rationale that sounds reasonable. The trap is that the rationale is generated after the adoption, not before it — so a good-sounding justification is no evidence the choice was ever evaluated against an alternative.

The mechanism is ordinary: incumbency produces familiarity, and familiarity feels like fitness. A rule that everyone has followed for years feels clearer, more natural and more readable than its alternatives, for no reason other than exposure.

## What Duolingo does

Duolingo writes about this in its own domain, where the effect is unusually well documented.

- **It states the general law flatly**: "Whatever pronunciation, word, phrase, or grammar the people in power use, there ends up being an explanation why that is a better way of speaking." Standard varieties are "kind of a myth," and it is "no accident" that they coincide with whichever region or city ends up being politically powerful. Old English's West-Saxon variety became the standard because Alfred of Wessex commissioned writing in it. Source: blog.duolingo.com/dialect-vs-accent-definition (Duolingo blog, 2025-11-25; accessed 2026-09-22)
- **It names the selection rule directly**: "a particular variety doesn't become the standard because it's neutral, the most accessible, or a natural choice. Rather, language standards typically reflect power relationships within a nation state." Written standards reflect it most sharply, because literacy was restricted to the wealthy. Source: blog.duolingo.com/history-of-standardization (Duolingo blog, 2025-12-23; accessed 2026-09-22)
- **It separates prescriptive from descriptive rules and dismantles three famous prescriptions.** "Never end a sentence with a preposition" was coined by an English bishop trying to make English resemble Latin. French "chez le coiffeur" preserves an era when tradespeople lived where they worked. Spanish "haiga" is a regular analogical formation attested since at least the 17th century and once widely accepted. The French Academy accepted feminine profession titles only in 2019 — thirty years after Quebec French did in 1989. Source: blog.duolingo.com/language-discrimination (Duolingo blog, 2025-08-28; accessed 2026-09-22)
- **The downstream cost is documented, not asserted.** The same post links the ranking of variants to measurable consequences for annual income and access to housing, sourced to university research — and notes that the creator-engagement asymmetry it also reports is self-reported rather than from a controlled study.

## The transferable pattern

1. **Ask for the provenance before you defend the rule.** Who wrote it, in what year, to settle what dispute, with authority over whom? A rule whose origin nobody can name is a rule nobody has evaluated.
2. **Treat "it's just clearer" as a claim needing evidence.** Clearer to whom, measured how? That phrasing is exactly the shape a retrospective rationalization takes.
3. **Keep prescriptive and descriptive rules in separate lists.** One describes how your people actually work; the other tells them how they should. Conflating them lets an old preference masquerade as an observation, and enforcing it then costs real time for no correctness gain.
4. **Audit the enforcement points, not the document.** The rules that matter are the ones a reviewer or a tool blocks on, and those are rarely the same set as the ones the guide contains.

Tensions worth naming. Provenance is not refutation: a rule adopted for bad reasons can still be the right rule, and consistency has value independent of which variant won. The useful outcome of this audit is usually a shorter enforced list plus an honest label — "this is our convention, not a correctness requirement" — rather than a rewrite. And auditing costs time that the rule itself was supposed to save.

## Apply to your product

- Name a rule your team enforces in review. Who wrote it, and what problem were they solving?
- Which of your enforced rules describe how your team actually works, and which describe how someone once thought it should?
- When a new person violates a convention, do they get a reason or a citation?

## See also

[[conventions-ratify-practice]] · [[no-process-without-purpose]] · [[candor-what-not-who]] · [[../duo-product/references/ship-it]]
