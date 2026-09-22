---
name: duo-production-reliability-gate-the-release-on-internal-telemetry
summary: Internal use of a pre-release build produces a reliable stability signal within hours, so gate rollout on it with an explicit no-blocking-bugs rule and a named owner.
metadata:
  internal: true
---

# Gate the release on internal telemetry

## Concept

Internal use of a pre-release build is usually treated as goodwill: people are asked to try it, and someone might mention something. That wastes the most valuable property it has, which is that a small internal population running real devices under real conditions generates enough crash, hang and performance data to detect a regression within hours — long before a staged public rollout would, and without exposing anyone outside the company. To use it you have to do two unglamorous things: put that telemetry on a dashboard nobody has to go hunting for, and write down a rule that stops the rollout. A signal with no rule attached to it is a report, and reports get read after the release.

## What Duolingo does

Source: blog.duolingo.com/dogfooding-app (Duolingo blog, 2024-03-01; accessed 2026-09-22)

- A **Release Dashboard** shows telemetry **as soon as a build enters dogfooding**: ANR events, crashes, out-of-memory events, frame rates, plus Crashlytics segmentation.
- The stated latency of the signal is **within a few hours** per build. That is the whole argument for gating on it — it is faster than any external rollout can be.
- The rule is explicit and procedural: **every Monday morning QA reviews the weekend's dogfooding bugs**, and **rollout does not begin unless nothing is blocking or significantly degrading the experience.** A named function owns the call.
- Numbers: the Music course crash bug surfaced **roughly 2,000 crash events** and was diagnosed and fixed **a few weeks before the iOS Math and Music launch** — after employees had already been using those courses internally for months. The long internal exposure is what made the volume large enough to be unambiguous.
- Tension worth carrying: an internal population is biased. It skews toward new devices, fast networks, high engagement and people who know the product's intended path. It catches crashes and regressions very well; it is close to useless for discovering that a flow is confusing.

## The transferable pattern

1. **Instrument the internal build the same way you instrument production.** If the pre-release build reports less than the shipped one, the fastest signal you own is the one you are throwing away.
2. **Write the gate as a rule with an owner and a cadence.** "No blocking or significantly degrading issues, reviewed by this function, at this time, before rollout starts." A dashboard with no rule attached does not stop anything.
3. **Prefer volume over ceremony.** The signal works because a lot of people use the build a lot, for months, doing their real work. Mandatory testing sessions produce far less than habitual use.
4. **Segment immediately.** Aggregate crash counts hide the regression that only affects one device class or one locale, which is the kind a staged rollout would also miss.
5. **Know what this gate cannot see.** Internal populations do not represent your slow-network, old-device, first-time users. Gate stability on internal telemetry; do not gate comprehension or desirability on it.

## Apply to your product

- Does your pre-release build report crashes, hangs and performance to somewhere anyone looks? If not, what is the earliest signal you actually have today?
- Write your gate as one sentence with a named owner and a time. If you cannot, you do not have a gate.
- Which properties of your real user base are entirely absent from your internal population, and which decisions are you therefore not allowed to make from this data?

## See also

[[make-reporting-free-and-aggregate-every-channel]] · [[sampled-tracing-versus-request-identity]] · [[../duo-experimentation/SKILL]]
