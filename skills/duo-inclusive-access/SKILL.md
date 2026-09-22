---
name: duo-inclusive-access
description: Stop your product filtering people out on circumstance instead of ability. Covers removing preconditions (location, hardware, contiguous free time), building escape hatches at the level of the blocked capability rather than the session, putting scaffolding on user-controlled toggles, never penalising slips you were not measuring, letting the user own the turn boundary in conversational interfaces, and auditing fairness against delivery context — device, screen size, connection — not just demographics. Use when someone asks who literally cannot use this, is this requirement measuring ability or access, should this be a setting or a change to the completion rules, should the free tier be a weaker product, how do we make onboarding accessible, or how do we build for a community nobody on the team belongs to.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Inclusive Access — Map of Content

Most exclusion in software is not a missing ARIA label. It is a requirement nobody audited: a place you must be, a device you must own, an hour you must control, a channel you must be able to use. Those produce zeros, not smaller numbers — the people they filter out never appear in your funnel to complain, so the gap is invisible from inside.

This skill is about finding those requirements and dismantling them without softening the product. Two ideas run through all of it. First, the difficulty of the *content* and the difficulty of the *experience* are independent dials, and people conflate them. Second, an accommodation that only changes what renders, while the completion rules stay put, is a decoration.

Scan the descriptions, follow only the `[[wikilinks]]` you need.

## Find the requirement

- [[references/strip-every-demand-you-are-not-measuring]] — every incidental demand gets scored alongside the real skill, so it adds noise and penalises people whose constraints differ from yours.
- [[references/a-precondition-produces-a-zero-not-a-smaller-number]] — why a location or hardware gate excludes harder than any price, plus the costs adjacent to yours.
- [[references/audit-fairness-against-the-delivery-context]] — on a self-administered product the environment is part of the instrument; put screen size and connection in the audit.

## Build the way out

- [[references/escape-hatches-at-the-granularity-of-the-blocked-modality]] — size the opt-out to the blocked capability, and put it in the completion rules, not the renderer.
- [[references/route-around-the-block-dont-only-remove-the-step]] — a skip preserves access; a reroute through an intact adjacent capability preserves the outcome.
- [[references/a-slow-decomposed-version-is-not-the-answer-key]] — slowed, seam-exposed, infinitely repeatable versions fix segmentation failures without giving anything away.
- [[references/scaffolding-belongs-on-a-user-controlled-switch]] — the aid that rescues a beginner caps an intermediate, so make it a toggle they can reach in the flow.

## Don't measure the wrong thing

- [[references/never-penalise-what-you-are-not-measuring]] — a penalty is a claim about competence; when the grader compares the wrong property, change the representation, not the threshold.
- [[references/working-memory-is-already-spent-elsewhere]] — capacity going to self-monitoring and to tracking your interface state is subtracted from the task.
- [[references/let-the-user-own-the-turn-boundary]] — silence-threshold turn detection cuts off exactly the hesitant users the feature exists to serve.

## Build with people you are not

- [[references/build-with-the-community-not-for-it]] — named community authors with the pen, contested calls shipped as stated choices, representation written incidentally.

## Boundary

A user who is *failing* is not a user who is *excluded*. How the product reacts to an ordinary wrong answer, how progress is labelled, and general error-message craft belong to the design and voice skills, not here. Illustration, animation and character quality are a design concern. And pixel craft — easing values, contrast ratios, token values, component props — is out of scope for this whole pack; route it per [[../duolingo/references/design-handoff]].

## Sibling skills

- [[../duo-design/SKILL]] — accessibility as a default rather than a checklist, and the design rationale layer above these rules.
- [[../duo-product/SKILL]] — whether a thing should be free, and which number you are optimising.
- [[../duo-experimentation/SKILL]] — how to measure a fairness or accommodation change without fooling yourself.
- [[../duo-voice/SKILL]] — the words around all of this, including how an opt-out is offered.

## Sources

Distilled from 22 posts on blog.duolingo.com dated 2020-02-03 to 2026-07-07, all cited inline and dated in each node; slugs are verified against `scripts/sources.json`.
