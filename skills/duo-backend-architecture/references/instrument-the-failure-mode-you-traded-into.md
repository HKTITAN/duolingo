---
name: duo-backend-architecture-instrument-the-failure-mode-you-traded-into
summary: A fix that swaps one failure mode for another is not done until the new one is measured — instrument before the migration, not after the first incident.
metadata:
  internal: true
---

# Instrument The Failure Mode You Traded Into

## Concept

Most performance fixes are trades. You give up a guarantee and buy speed: locking becomes retrying, synchronous becomes eventually consistent, a blocking call becomes a queue. The trade is sound only if the new bad case is rare — and that is a claim about live production, not a claim you can reason your way to. So the instrumentation for the new failure mode ships *before* the change, not after the first incident. Doing it in that order also converts the rollout decision from an argument between engineers into a reading off a dashboard, which is exactly what lets you move quickly on a system you are afraid of.

## What Duolingo does

Source: blog.duolingo.com/optimistic-locking (Duolingo blog, 2025-12-22; accessed 2026-09-22)

- Before migrating, Duolingo built a **replica database driven by simulated mock traffic** to measure the change, added **explicit tracking for how often a transaction retried** because the version ID had moved, and put the whole switch behind a **feature flag** so users could be migrated gradually and reverted instantly without a deploy.
- They rehearsed the schema change itself: adding the version-ID column was measured at **22ms of downtime** before it was run for real. Final cutover took **a few seconds**.
- The stated cost: testing every step against a mock database **took extra time**. The post names this explicitly as the price of a smooth transition, not as free diligence.
- The post's own summary is that monitoring the failure modes is almost as important as the fix.

A second story shows what happens when the instrumentation is missing. During a Python 3.9/Alpine to 3.12/Debian migration of Duolingo's China SMS service, a nightly batch (around **23:00 Beijing time**) blocked all **10 uWSGI worker threads per worker** on TLS setup; `/health` had no thread left to answer, Kubernetes killed the pods as unhealthy, and the CPU-constrained nodes could not reschedule them — high latency, upstream 5xx and repeated restarts inside a **6-minute window**, with emergency scaling pushing minimum pods to **32**. The underlying defect — a new HTTP client per request — had been in the codebase for years. Fixing it dropped peak CPU per pod to **under 3.5%** (roughly a **97% reduction**) and minimum pods to **8**, below the pre-migration baseline of **18** (blog.duolingo.com/reduce-cpu-usage-97-percent (Duolingo blog, 2026-06-22; accessed 2026-09-22)).

## The transferable pattern

1. **Name the new failure mode out loud before you ship.** "Retries," "stale reads," "duplicate delivery," "queue backlog." If you cannot name it, you do not understand the trade.
2. **Ship the counter first, in the old system.** A metric that predates the change gives you a baseline; one added afterwards only tells you the world is on fire.
3. **Rehearse the irreversible step against a replica.** Schema changes, cutovers and backfills can be timed in advance. A measured 22ms is a decision; an unmeasured one is a gamble.
4. **Make the switch a flag, not a deploy.** Gradual migration plus instant revert is what turns a scary change into a routine one.
5. **When a platform change breaks something, assume it exposed a defect rather than created one.** A new runtime shifts the performance envelope until a long-tolerated inefficiency crosses a threshold. Reverting restores the hiding place; investigating often leaves you better off than before the change.
6. **Never let a health endpoint share the exhausted resource.** If liveness competes for the same worker pool as real traffic, your orchestrator will kill healthy processes and deepen the shortage it is reacting to.

## Apply to your product

- What guarantee is your next performance change actually giving up, and which counter would show you that trade going bad?
- Which of your recent incidents were blamed on a platform upgrade, and did anyone check whether the defect predated it?
- Does your health check consume the same threads, connections or pool as production traffic — and what does it report when that pool is empty?

## See also

[[hold-the-lock-only-over-shared-work]] · [[pitch-migrations-in-the-sponsors-currency]] · [[../duo-experimentation/SKILL]]
