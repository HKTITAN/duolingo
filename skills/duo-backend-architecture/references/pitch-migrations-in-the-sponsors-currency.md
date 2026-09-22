---
name: duo-backend-architecture-pitch-migrations-in-the-sponsors-currency
summary: Lead with the number the work moves, not the mechanism — and slice the migration so each unit leaves a working, measurable system.
metadata:
  internal: true
---

# Pitch Migrations In The Sponsor's Currency

## Concept

Long migrations rarely die from technical failure. They die when sponsorship evaporates midway — the cost fully sunk, the benefit still hypothetical. Two habits prevent that. First, pitch in the currency of the person approving, not the currency of the technology: a mechanism they cannot evaluate reads as risk, while a metric they already track needs no explanation and justifies itself. Second, slice the work so every unit ends with a system that runs and a number you can read. Each measurement is how you buy the time for the next slice, so the decision to continue keeps getting re-made on fresh evidence instead of resting on the original promise.

## What Duolingo does

Source: blog.duolingo.com/async-python-migration (Duolingo blog, 2025-03-25; accessed 2026-09-22)

- Duolingo found "an efficient I/O paradigm based on an event loop managing non-blocking coroutines" impossible to sell. The pitch that worked: **async Python will let us pay AWS less money to host our Python services, by letting our computers spend less time waiting.**
- That framing bought **one person, two weeks**. The results bought the rest of the project: **~10,000 requests per instance async versus ~7,000 sync** — about **40% more per instance**, implying roughly **30% EC2 savings** per migrated service.
- They migrated the first service **one route at a time**, deploying each migrated route to staging behind a **feature flag** with a small slice of traffic and benchmarking it against the production service with the same features disabled. Final validation split **50% of production traffic** each way; results were close to the initial readings.
- **The cost the pitch does not shrink.** The post is blunt that supporting async Python is about as hard as supporting a new programming language: HTTP clients, auth clients, observability tooling and Python backends all had to be rewritten.
- **A deliberate exception.** They did *not* migrate the first service incrementally, because they needed maximum measured performance immediately to justify the work. Incremental migration only became the plan for later services, once the support existed.

On rollout style, a different Duolingo migration inverted the usual approach: they adopted cloud development environments while **fully supporting local development and never pushing adoption**. Usage grew anyway, highest among summer interns with fresh machines and only **12 weeks** to make an impact — setup that previously took **hours to days** became an **8-minute** spin-up, and the feedback loop went from minutes to seconds. Voluntary adoption under no pressure is a clean measurement; mandated adoption generates compliance and tells you nothing. Real costs came with it: third-party outages now halt work directly, and secret values could be read without the two-factor requirement covering the rest of the organization (blog.duolingo.com/developer-onboarding-with-github-codespaces (Duolingo blog, 2022-10-14; accessed 2026-09-22)).

## The transferable pattern

1. **Translate the mechanism into the approver's metric before the meeting.** Infrastructure spend, headcount hours, incident count, time-to-ship. If you cannot state the mechanism in one sentence, stop explaining it and lead with the number.
2. **Ask for a small first slice, sized to produce a measurement.** Two weeks and one route beats a quarter and a plan.
3. **Every slice must leave the system working.** A migration that is only valuable at the end has no evidence to offer while it needs the most support.
4. **Benchmark like for like.** Compare the migrated unit against the old one with the same features enabled, on real traffic, behind a flag.
5. **Where a change is a tool people adopt rather than a system you cut over, do not mandate it.** Let the population with the most acute pain go first; if adoption spreads without a push, the absence of the push is your evidence.

Note that this node is about buying *time and sponsorship*. Seeing, attributing and governing infrastructure spend as an ongoing discipline is a separate concern, owned by the cost-efficiency skill in this pack.

## Apply to your product

- What number does the person who approves your roadmap actually watch, and can you state your migration's effect on it in one sentence with no jargon?
- What is the smallest slice that would leave you with a working system *and* a defensible measurement?
- Is your proposed change something you cut over, or something people adopt? If the latter, who has the most pain today, and what happens if you never push it on anyone else?

## See also

[[instrument-the-failure-mode-you-traded-into]] · [[duplication-can-beat-the-abstraction]] · [[extract-what-blocks-its-own-improvement]]
