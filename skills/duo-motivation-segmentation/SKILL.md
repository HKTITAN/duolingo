---
name: duo-motivation-segmentation
description: Ask users why they are here, store that declared motive as a first-class dimension next to behaviour, and learn where self-report and telemetry each lie to you. Covers collecting a stated reason at signup, why the biggest segment is usually not the most engaged one, why two cohorts with identical usage curves need opposite interventions, when to exclude a segment instead of pooling it, reading the size of your catch-all bucket as a taxonomy failure, naming and interviewing a motive you never designed for, why cohort splits invert aggregate rankings, and how the motive mix shifts during a shock. Use when you are asking why did this metric move, who is this feature actually for, why does this segment churn, should I add an onboarding question, is my persona real, what does "other" mean in this chart, or why did a surge not stick.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Motivation Segmentation

Behavioural telemetry tells you what changed. It cannot tell you why, because "why" is not a behaviour — it is the reason behind one. Two users with identical usage curves can be here for opposite reasons and need opposite products. This skill is about collecting a declared motive, joining it to everything, and staying honest about the ways both self-report and instrumentation mislead.

Duolingo is the case study throughout: it asks every new learner for a primary reason and publishes the cross-tabs. Your product is the target.

## Collecting the field

- [[references/collect-a-declared-why-at-signup]] — one question at signup turns a correlation into an explanation; plus the two known failure modes of self-report.
- [[references/size-of-other-is-a-taxonomy-diagnostic]] — a catch-all that spikes for one segment is measuring how wrong your category list is there.

## Reading it without fooling yourself

- [[references/largest-segment-is-not-most-engaged]] — the modal reason routinely spends less time in product than a smaller one, so headcount is a bad build order.
- [[references/split-by-cohort-before-concluding-what-users-want]] — the aggregate top row is consensus theatre; the inversions beneath it are where differentiated decisions live.
- [[references/motive-decides-the-lever-and-who-to-exclude]] — match the intervention to the motive, and exclude segments whose causal story is structurally different rather than pooling them.

## When the mix changes

- [[references/name-the-unplanned-motive-then-interview-it]] — an unnamed motive silently receives the experience you tuned for other motives; name it, then go talk to it.
- [[references/in-a-shock-the-motive-mix-moves-first]] — during a disruption, the reason mix and the hour-of-day curve move before the volume line means anything.

## Boundaries

This skill stops at internal use of the declared motive. Publishing it externally for coverage — the annual report, the per-country cut, the press pitch — belongs to [[../duo-proprietary-data-reports/SKILL]]. Validating the psychometric structure of a score you report back to users belongs to [[../duo-measurement-validity/SKILL]].

## Sibling skills

- [[../duo-learner-motivation/SKILL]] — what drives a user internally, as opposed to how you segment on it.
- [[../duo-proprietary-data-reports/SKILL]] — turning first-party aggregate data into publishable material.
- [[../duo-measurement-validity/SKILL]] — whether the thing you are measuring is the thing you think it is.
- [[../duo-experimentation/SKILL]] — testing the interventions a motive split tells you to try.

## Sources

Every claim is cited inline in the dated form `blog.duolingo.com/<slug> (Duolingo blog, YYYY-MM-DD; accessed 2026-09-22)`; 15 distinct posts from blog.duolingo.com, 2020-04-08 through 2025-07-08.
