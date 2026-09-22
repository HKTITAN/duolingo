---
name: duo-production-reliability-repair-earned-state-in-the-incident-tooling
summary: When an outage can destroy state a user earned, build automatic repair into the incident tooling itself and construct it from a mechanic the product already has.
metadata:
  internal: true
---

# Repair earned state inside the incident tooling

## Concept

Some state your users hold is valuable because it was expensive to earn. When your failure destroys it, a reliability incident becomes a fairness grievance, and those are far more durable than a slow afternoon. The instinct is to handle it afterward through support. That is the worst option available: it puts the cost on the user to notice and ask, produces a support surge exactly when the team is most loaded, and resolves inconsistently by whoever is on shift. The repair belongs inside the incident tooling — automatic, logged, applied on recovery. And it should be built out of a mechanic the product already runs every day, rather than a new privileged code path.

## What Duolingo does

Source: blog.duolingo.com/protecting-streaks-from-site-issues (Duolingo blog, 2021-11-01; accessed 2026-09-22)

- The Big Red Button records **the exact timestamp each learner hit the maintenance page**, then **retroactively applies a streak freeze** to that day for everyone affected once systems recover. No ticket, no request, no judgment call.
- Numbers: **over 2 million streaks protected** to date by this mechanism.
- The repair reuses **exactly the streak-freeze logic that already fills a missed day** for ordinary users. The only change made to build it was logging each person's timestamp. Duolingo added a record, not a remediation system.
- That reuse is the load-bearing part. A bespoke admin path for fixing broken state is exercised rarely and tested rarely, so it is the most likely thing to be wrong the one time you need it. A mechanic users hit daily is continuously validated by production traffic.
- Tension: this only works because Duolingo already had a forgiveness mechanic to borrow. Their repair is also not time-critical, which is what let the switch itself stay dumb (see [[the-kill-switch-must-fail-open]]) and the affected-user query run after recovery.

## The transferable pattern

1. **Inventory what your outage can destroy that the user earned.** Not data you can restore from a backup — progress, standing, position, accrued credit, anything whose value is the effort behind it.
2. **Make the repair a step of the incident, not a follow-up project.** It should run on recovery without anyone filing anything, and it should log what it did.
3. **Build it from an existing mechanic.** If you already have a grace period, a credit, a re-issue, a rollover, a waiver — use that path. It inherits its own correctness and edge-case handling for free.
4. **Log identity at the moment of denial.** The whole approach depends on knowing who was actually affected, which you can only capture while it is happening. Retro-fitting that from aggregate metrics is guesswork.
5. **Be conservative and over-inclusive.** Repairing a few people who were not harmed is cheap. Missing people who were is the failure mode that generates the grievance you were trying to avoid.

## Apply to your product

- What can a two-hour outage take from a user that they cannot simply retry to get back? Write the list; it is usually shorter and more emotional than you expect.
- Which mechanic already in your product could stand in as the repair — a grace period, a credit, an extension — so you are not writing a privileged one-off?
- Are you capturing who got the error page, at the time it happened, in a form you could query tomorrow?

## See also

[[the-kill-switch-must-fail-open]] · [[reassurance-is-load-shedding]] · [[../duo-retention/references/streak-freeze]]
