---
name: duo-production-reliability-a-dated-public-moment-funds-the-rebuild
summary: Platform work loses prioritization contests because its benefit is diffuse, so bind it to an unmissable dated event and the headroom you build outlives the campaign.
metadata:
  internal: true
---

# A dated public moment funds the rebuild

## Concept

Infrastructure work that everyone agrees is necessary can go unfunded for years, not because anyone objects but because its benefit is diffuse and its deadline is never. It competes each quarter against features with owners, dates and forecastable numbers, and it loses each quarter for the same structural reason. A dated, public, unmissable event changes the arithmetic. It converts "we should modernize this eventually" into a fixed deadline with a named owner and a visible cost of failure — and the capacity you build to survive that one moment does not go away when the moment passes. This is a real lever. It is also a symptom of a broken prioritization process, and it is worth being honest about both.

## What Duolingo does

Source: blog.duolingo.com/super-bowl-commercial-2024 (Duolingo blog, 2024-02-12; accessed 2026-09-22)

- The plan was to fire a push notification to the whole user base **simultaneously with a Super Bowl ad airing**. None of the existing tooling could do it, so Duolingo had to **redesign its entire notification system**.
- **Three engineering teams** built a proof of concept starting in **October**, tested continuously through to the game, and shipped **contingency runbooks for game day** rather than trusting the happy path.
- Numbers: the push reached **4 million learners — 95% within 3.9 seconds and 99% within 5.7 seconds** of the ad airing. The **previous record was 500,000 in 60 seconds, and that one caused crashes.**
- Tension, and the post says it plainly: this is **a perverse incentive**. The tooling limitation was long known and only got fixed because a marketing stunt depended on it. The lesson is not "wait for a stunt." It is that a diffuse benefit needs a concrete forcing function, and if your process cannot supply one, an external date will.
- Note what came with the date and is doing much of the work: an early start, continuous testing against the real target, and written contingencies. The deadline created urgency; the discipline created the result.

## The transferable pattern

1. **Find the event that requires the rebuild.** Not one that would benefit from it — one that cannot happen without it. A launch, a regulatory date, a contract cutover, a conference demo, a partner integration going live.
2. **Scope it to the capability, not the campaign.** Build the general capacity the event demands, so the artifact that survives is a platform rather than a one-off script that gets deleted in March.
3. **Start absurdly early relative to the event.** Duolingo began four months out for a single notification. The date is only a forcing function if there is time to discover what is broken.
4. **Write the contingency runbook as a deliverable.** For a fixed public moment there is no reschedule, so the failure branches have to be decided in advance and by someone not panicking.
5. **Convert the peak into a floor.** After the event, keep the headroom, the load tests and the runbooks. The point was never the one spike.
6. **Do not mistake the lever for a strategy.** If the only way your platform work gets funded is by attaching to marketing, that is a finding about your prioritization, and it should be said out loud rather than celebrated.

## Apply to your product

- Which known limitation have you deferred for more than a year, and what upcoming dated commitment would be impossible to meet without fixing it?
- If you hit that date, what part of the work becomes permanent capacity and what part is scaffolding you will throw away?
- What is your current record for the peak this system must survive, and how did that attempt actually go?

## See also

[[find-code-that-runs-not-code-thats-referenced]] · [[gate-the-release-on-internal-telemetry]] · [[../duo-growth/SKILL]]
