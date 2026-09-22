---
name: duo-production-reliability-datasets-are-production-software
summary: Datasets have the same failure modes as services, so lint conventions in CI, diff the output in the pull request, deploy blue-green, and alert only on failure and staleness.
metadata:
  internal: true
---

# Datasets are production software

## Concept

Analytical data work tends to evolve its own, weaker discipline: conventions in a wiki, changes verified by hand, deploys that overwrite in place, monitoring bolted on after the first silent breakage. This is strange, because a dataset fails in exactly the ways a service fails — inconsistent interfaces, unverified changes, inconsistency mid-deploy, breaking without anyone noticing. Modeling data is structurally the same activity as designing an API: take input, validate it, compute, and emit a shape that is easy for a consumer to use. Once you accept that framing, you do not need to invent practices. The ones that solved these problems in software transfer directly, and the interesting part is which ones you should deliberately not bring.

## What Duolingo does

Source: blog.duolingo.com/dataset-development (Duolingo blog, 2025-03-14; accessed 2026-09-22)

- The **Data Refinery** team was staffed deliberately with **software engineers new to analytics alongside data scientists**, so that engineering practice arrived with people rather than as a mandate.
- **Linting in CI**, posted as **automated pull request comments**. It catches formatting and also **semantic mismatches** — for example a new column named `event_timestamp` that is actually stored as a `DATE`. A convention people have to remember decays as contributor count grows; one that comments on the change does not.
- **Automated data diffs from any pull request**, replacing a manual ritual of building a dev table, hand-writing comparison queries and summarizing results. Framed explicitly as **a verification step, not a CI gate** — for a change to computation logic a large delta is correct, and for a refactor any delta is a bug. Only the author knows which case they are in, so the tool shows the difference cheaply instead of trying to judge it.
- **Blue-green deploys**: backfill, then clone, so consumers never read a half-updated table.
- Monitoring is deliberately **plain Slack alerts for job failures, out-of-date tables, and catch-up notifications**. They **resisted statistical tests and anomaly detection** despite the temptation, because simple alerts are legible to data consumers rather than only to maintainers, which widens the set of people who can catch a problem.
- Numbers: datasets used in **hundreds of A/B test analyses and dashboards**, **over 10,000 queries per week** across the company, and **anyone with some SQL experience can productionize a modeled dataset within a day**.

## The transferable pattern

1. **Treat any shared output as an interface with consumers.** If other teams build on it, it needs versioning, conventions and a deploy story, whatever the file format.
2. **Enforce conventions at the moment of change.** A comment on the pull request beats a style document, because nobody has to have read anything.
3. **Lint semantics, not only syntax.** The expensive inconsistency is a name that promises one thing while the storage does another.
4. **Not every automated check should be pass or fail.** When the correct output cannot be asserted in advance, produce a before-and-after diff and let the author judge it. Gating on it would just teach people to skip it.
5. **Never let consumers read a half-applied change.** Build beside, then swap.
6. **Alert on the two things you will act on — it failed, and it is stale — before reaching for anomaly detection.** Alerts that nobody can interpret or own train everyone to ignore the channel.
7. **Measure the discipline by onboarding time.** "A day, with some query experience" is the real output of all of the above.

## Apply to your product

- Which of your shared outputs would break other teams' work if its shape changed tomorrow, and does it have a review path at all?
- When someone changes that pipeline, how do they currently check they did not break it — and is that check a ritual you could automate into a diff?
- What would your on-call actually do with each alert your data systems fire today? Delete the ones with no answer.

## See also

[[continuous-qa-for-always-on-systems]] · [[gate-the-release-on-internal-telemetry]] · [[../duo-experimentation/SKILL]]
