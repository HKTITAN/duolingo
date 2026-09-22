---
name: duo-production-reliability-the-kill-switch-must-fail-open
summary: The tool that controls an outage must have fewer dependencies than the system it controls and must fail open, or it is decoration.
metadata:
  internal: true
---

# The kill switch must fail open

## Concept

Incident tooling is used at exactly the moment the normal stack is broken. Every dependency it shares with production is therefore a way for it to be unavailable precisely when it matters. This inverts the usual instinct: the right architecture for a kill switch is the least sophisticated one that works, because sophistication is dependency count. The second rule follows from the first. If the switch itself errors, the system must carry on as though the switch said nothing. A control plane that can escalate an outage by failing is worse than no control plane, because you will hesitate to use it.

## What Duolingo does

Source: blog.duolingo.com/protecting-streaks-from-site-issues (Duolingo blog, 2021-11-01; accessed 2026-09-22)

- Duolingo's kill switch is called the **Big Red Button (BRB)**. It pauses traffic to the app during a major incident and shows a maintenance page.
- A dedicated microservice was **designed and then rejected** on dependency count. The shipped design is a **plain file in S3 that clients poll** — high availability, no new services to operate, and one of the fewest moving parts available.
- It fails open by construction: **if a client errors while reading the BRB file, it ignores BRB entirely.** A broken switch degrades to normal behavior, never to a self-inflicted outage.
- Recovery is staged rather than binary: requests are brought back in controlled subsets using **multiple S3 files**, instead of reopening to the full population at once and re-crushing whatever just recovered.
- The storage choice paid a second dividend — **S3 access logs double as the record of who was affected**, which is what makes automatic repair possible afterward.
- Tension, stated in the post: the simple design gave up real-time querying. Duolingo can only run Athena over the access logs **after** recovery. That was acceptable only because their repair is not time-critical. If yours is, this exact tradeoff does not transfer.
- Second tension: BRB is **all-or-nothing**. It cannot disable a subset of features, so a partial failure still takes the whole product down. Duolingo also names single-cloud dependence as an open risk.

## The transferable pattern

1. **Count dependencies, not features.** The correct question for a control-plane design is "what has to be healthy for this to work," and the answer should be shorter than the list for the system it controls.
2. **Fail open, always.** Define the behavior when the switch cannot be read, and make it "carry on normally." Then test that path, because it is the one you will hit under stress.
3. **Prefer boring storage to a new service.** A polled object in durable storage has an availability profile you did not have to earn and an operational cost of zero.
4. **Stage the recovery.** Coming back is a second incident. Return traffic in subsets you can abort.
5. **Get the audit trail for free if you can.** Whatever medium carries the switch should also record who was affected, so remediation does not need a separate pipeline built during the incident.
6. **Say out loud what your switch cannot do.** An all-or-nothing switch is a real constraint, not a detail. People need to know before they are deciding at 3am.

## Apply to your product

- If your feature-flag service is down, can you still turn things off? Trace the dependency chain of your emergency control and see whether it crosses anything that could be part of the outage.
- What happens today when your switch is unreadable — does the client block, retry, or proceed? If nobody knows, that is the answer.
- Can you shed one subsystem, or only everything? Name the partial failure you would most want to isolate, and price building that granularity.

## See also

[[repair-earned-state-in-the-incident-tooling]] · [[reassurance-is-load-shedding]] · [[long-incidents-need-a-different-playbook]]
