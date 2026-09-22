---
name: duo-production-reliability
description: How to know what production is actually doing, and what to run when it breaks — extracted from Duolingo's engineering blog and made portable to any product. Covers always-on request identity versus sampled tracing, runtime dead-code detection, kill switches that fail open, automatic repair of state users earned, incident command for long-running incidents, dogfooding gates, zero-friction bug intake and feedback aggregation, datasets treated as production software, and continuous quality and security verification. Use when someone asks why is production slow for this one customer, how do we find dead code, what should our kill switch look like, how do we run an incident that lasts all day, how do we compensate users after an outage, should we gate the release on internal telemetry, or why are our bug reports useless.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Production Reliability

Two questions, answered by two different bodies of practice. What is production actually doing right now, and who decides what happens when it stops? Duolingo's engineering blog is unusually candid on both — including where the approach has costs, where it failed, and where the honest version is that a marketing stunt paid for the infrastructure.

This skill is about signals from real production and the response when it fails. Designing, grading and constraining an LLM-driven test or migration agent is a different problem and belongs to the AI agent platform skill, not here.

## Knowing what production is doing

- [[references/sampled-tracing-versus-request-identity]] — sampling finds systemic waste; one customer's problem needs always-on identity you can usually derive from logs you already write.
- [[references/find-code-that-runs-not-code-thats-referenced]] — static analysis cannot see code that is referenced but never executes, which is where concluded experiments leave residue.
- [[references/gate-the-release-on-internal-telemetry]] — internal use of a pre-release build gives a reliable stability signal within hours, if you attach a rule and an owner to it.
- [[references/keep-the-visual-record-your-tests-already-produce]] — your CI already renders every state on every device and locale, then deletes the evidence.
- [[references/make-reporting-free-and-aggregate-every-channel]] — capture the report in place with context attached, then pool every channel and look for what spikes.

## When it breaks

- [[references/the-kill-switch-must-fail-open]] — the tool that controls an outage must have fewer dependencies than the system it controls.
- [[references/repair-earned-state-in-the-incident-tooling]] — automate the repair inside the incident tooling, built from a mechanic the product already runs daily.
- [[references/reassurance-is-load-shedding]] — anxious users retry, and their retries are part of what is keeping you down.
- [[references/long-incidents-need-a-different-playbook]] — past roughly one shift you need a commander who only coordinates, named decision owners, and a written narrative.
- [[references/agree-the-shared-artifact-before-the-incident]] — pick the one place that counts as agreed reality now, not at 3am.

## Quality as a standing function

- [[references/datasets-are-production-software]] — lint in CI, diff in the pull request, deploy blue-green, alert only on failure and staleness.
- [[references/continuous-qa-for-always-on-systems]] — a system with no after cannot be audited in batches; monitor against trend and route anomalies to tiered experts.
- [[references/verify-controls-instead-of-asserting-them]] — advise rather than gate, test your own controls continuously, and buy findings rather than grades from outside testers.

## Funding the work

- [[references/a-dated-public-moment-funds-the-rebuild]] — platform work loses prioritization contests, so bind it to an unmissable date; the post is candid that this is a perverse incentive.

## Sibling skills

- [[../duo-experimentation/SKILL]] — running the tests whose concluded branches become the dead code and the unreproducible bug reports above.
- [[../duo-product/SKILL]] — taking the long view and raising the bar, which is the argument reliability work has to win.
- [[../duo-culture/SKILL]] — candor, ownership and talent density, without which incident command and advisory functions do not work.
- [[../duo-retention/SKILL]] — why the state an outage destroys is worth this much trouble to repair.

## Sources

All claims cite blog.duolingo.com posts by slug and publication date, inside each node's "What Duolingo does" section; the substance is inlined so every node stands alone offline.
