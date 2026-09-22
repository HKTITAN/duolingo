---
name: duo-score-credibility
description: Design a score, rating or level that outsiders will accept and insiders cannot game — adaptive item selection, item-bank size as a security property, per-user instances, anchoring to a published external standard, pool-local ratings, cram-proofing, calibrated free practice, anonymous recorded human review, and owning the wait and the result delivery. Use when the user says their score is being gamed or inflated, asks how few questions an assessment actually needs, wants a level or rating that employers and schools will trust, worries that a leaked question set invalidates everyone's results, asks whether to invent their own scale or map onto an existing one, wants to give practice or a free tier away without corrupting the measurement, or asks how to prove a number means what it claims.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Score Credibility — Map of Content

Some numbers are shown only to your team. This skill is about the other kind — the score, rating or level you put in front of users and outsiders, where someone has an incentive to move it without earning it. Duolingo runs two of these in public: the Duolingo English Test, accepted by institutions that have every reason to be skeptical, and Duolingo Score, which claims a meaning outside the app. Both are useful precisely because they are hard to fake.

Credibility here is structural, not rhetorical. A large randomized pool, a per-user instance, an external anchor and a cram-proof design do more for trust than any amount of explaining. The nodes below are each one complete move.

This skill is a **graph**. Scan the descriptions, follow only the `[[wikilinks]]` you need.

## Measure the right thing, in the fewest items

- [[references/stop-presenting-items-that-tell-you-nothing]] — select each next item from the estimate you already hold, and probe the behaviour instead of a correlate of it.
- [[references/design-so-cramming-cannot-move-the-score]] — if preparation for the measurement moves it, it is measuring preparation; plus owning the price, the wait and the delivery of the result.

## Make gaming structurally pointless

- [[references/a-large-item-bank-makes-leakage-structurally-irrelevant]] — a pool big enough to randomize shortens the assessment, kills leakage as a threat, and funds unlimited free practice.
- [[references/unique-instance-per-user-as-a-security-property]] — per-user assembly caps a leak at one person; anonymous recorded review and hired outside attackers cover the rest.

## Make the number mean something outside your product

- [[references/anchor-to-an-external-published-standard]] — map your levels onto a scale the outside world already reads, and publish a can-do statement for each.
- [[references/one-legible-number-plus-a-content-manifest]] — one score with a ceiling and an external meaning, what each level contains, and what your grader actually optimizes for.
- [[references/a-rating-is-meaningful-only-inside-its-own-pool]] — a relative rating encodes standing in one population; never compare across pools, and say so before the user finds out.

## Boundaries

- The internal metric your team optimizes against — north-star choice, guardrails, weighting, thresholds — is not here. That is `duo-metric-design`.
- What you charge for the assessment, and what stays free, is [[../duo-freemium-monetization/SKILL]].
- Whether your measurement is valid in the first place is [[../duo-measurement-validity/SKILL]].

## Sibling skills

- [[../duo-measurement-validity/SKILL]] — a credible score is worthless if the construct underneath it is wrong.
- [[../duo-efficacy-measurement/SKILL]] — proving the number tracks a real outcome, which is what outsiders eventually ask for.
- [[../duo-inclusive-access/SKILL]] — fee waivers, accommodations and setup assumptions decide who the score is credible *for*.
- [[../duo-freemium-monetization/SKILL]] — pricing the certified thing while the practice version stays free.

## Sources

blog.duolingo.com — Duolingo English Test posts (adaptivity, proctoring, practice test, readiness, interactive skills, 2021 improvements), CEFR and course-creation posts, Duolingo Score updates, and the Elo rating explainer. Every node carries its own dated citation.
