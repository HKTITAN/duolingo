---
name: duo-backend-architecture
description: Make a server request fast and hard to break, using Duolingo's published engineering results as the case study. Covers what to delete from the synchronous request path, how to split data into precompute-and-cache versus caller-injected, how long to hold a lock and when to go optimistic, instrumenting the failure mode a fix trades you into, server-driven UI and versioning clients without branching on client version, when optimistic rendering is worth its rollback cost, and how to stage, fund and survive a long runtime migration. Use when someone says our API is slow, p99 latency, this endpoint has too many dependencies, database contention, lock timeouts, optimistic locking, we want to ship UI changes without an app release, server-driven UI, optimistic updates, should we roll back the prediction, how do we sell this migration to leadership, or the migration broke production.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Backend Architecture

How to make a server request fast and hard to break — and how to move a live system to a new
shape without stopping it.

The through-line across every node: **latency adds, availability multiplies, and hold time is
the variable you control.** Most of the wins below come from deleting work from the live path
rather than making that work faster. The rest come from being honest about what a fix costs
before you ship it.

Scope note: this skill owns latency and failure modes. Seeing, attributing and governing
infrastructure *spend* is a different discipline and belongs to the cost-efficiency skill in
this pack.

## The request path

- [[references/delete-dependencies-from-the-request-path]] — every shared resource in a live path is both a latency term and an independent failure mode; audit and remove before optimizing inside.
- [[references/split-data-by-sharing-pattern]] — precompute what is expensive-and-shared, have the caller inject what is cheap-and-personal, and almost no request-time lookups survive.
- [[references/hold-the-lock-only-over-shared-work]] — lock duration, not transaction rate, is usually what is killing you; move network calls out of the critical section.
- [[references/instrument-the-failure-mode-you-traded-into]] — a fix that swaps one failure mode for another is not done until the new one is measured, rehearsed and flagged.

## Server-driven clients

- [[references/move-the-ui-definition-to-the-server]] — when release cadence caps your experiment count, ship the interface as a server-sent config plus a per-user data model.
- [[references/version-clients-by-last-good-config]] — cache the last config the client could parse and send data-only responses to old clients, so server code never branches on client version.

## Prediction and rollback

- [[references/predict-only-what-users-dont-care-about]] — the cost of a wrong optimistic render scales with how much the value matters; never predict money, fairness, or hard-won state.
- [[references/prefer-a-loading-state-to-a-rollback]] — check whether a spinner is acceptable first; the duplicated business logic costs more than the latency you save.

## Moving a live system

- [[references/pitch-migrations-in-the-sponsors-currency]] — lead with the number the work moves, and slice it so every unit leaves a working, measurable system.
- [[references/duplication-can-beat-the-abstraction]] — when the de-duplicating machinery triples the line count, take the duplication; share only the genuinely variant-agnostic middle.
- [[references/extract-what-blocks-its-own-improvement]] — if changing a subsystem means redeploying everything, it will never be improved; extract it and keep a revert path.

## Sibling skills

- [[../duo-experimentation/SKILL]] — the experiments that server-driven UI and feature flags exist to make cheap.
- [[../duo-product/SKILL]] — taking the long view on a rewrite, and deciding what is worth shipping at all.
- [[../duo-culture/SKILL]] — talent density and candor, which is what makes "this manual ritual is a bug" a sayable sentence.
- [[../duo-design/SKILL]] — visual craft, motion and tokens, which this skill deliberately does not touch.

## Sources

blog.duolingo.com/rewriting-duolingos-engine-in-scala (Duolingo blog, 2017-01-31; accessed 2026-09-22) · blog.duolingo.com/optimistic-locking (Duolingo blog, 2025-12-22; accessed 2026-09-22) · blog.duolingo.com/server-driven-ui (Duolingo blog, 2024-11-08; accessed 2026-09-22) · blog.duolingo.com/frontend-prediction (Duolingo blog, 2026-04-15; accessed 2026-09-22) · blog.duolingo.com/async-python-migration (Duolingo blog, 2025-03-25; accessed 2026-09-22) · blog.duolingo.com/reduce-cpu-usage-97-percent (Duolingo blog, 2026-06-22; accessed 2026-09-22) · blog.duolingo.com/developer-onboarding-with-github-codespaces (Duolingo blog, 2022-10-14; accessed 2026-09-22) · blog.duolingo.com/how-i-saved-duolingo-40000year-in-my-summer-internship (Duolingo blog, 2017-09-30; accessed 2026-09-22) · blog.duolingo.com/language-irregularity-and-complexity (Duolingo blog, 2025-09-16; accessed 2026-09-22) · blog.duolingo.com/french-homophones-tiktok (Duolingo blog, 2023-05-11; accessed 2026-09-22)
