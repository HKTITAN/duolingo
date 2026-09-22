---
name: duo-production-reliability-make-reporting-free-and-aggregate-every-channel
summary: Capture defect reports in place with diagnostic context attached, then pool every feedback channel into one trend detector because no single channel is large enough to show a spike.
metadata:
  internal: true
---

# Make reporting free, then aggregate every channel

## Concept

Two separate failures kill most feedback systems. The first is friction at the moment of annoyance: if filing a report means leaving the product, opening a tracker and describing what you saw, then report volume is governed by how determined someone is, not by how bad the problem is — so you hear only about the issues somebody was angry enough to chase. The second is that a report without context is not reproducible, so it costs engineering more than it saves and eventually gets ignored. Fix both and you get a new problem: many small streams, each too noisy and too biased on its own to show you anything. The answer to that is not to read them all. It is to pool them and look for what is spiking across sources.

## What Duolingo does

Source: blog.duolingo.com/dogfooding-app (Duolingo blog, 2024-03-01; accessed 2026-09-22)

- **Shake-to-Report**: shaking the device (or a button on web) opens a bug form **in place**. It auto-attaches a screenshot, **the reporter's current experiment treatments**, device and app version, course and lesson data, a log file, and a **Fullstory session recording**.
- The experiment-assignment capture is the underrated part. Without it, an internal report against a product where the server picks the variant is often not reproducible by the engineer reading it.
- **Jeeves**, an internal tool, ingests dogfooding reports plus the beta program, **Reddit, Twitter, Google Play, the App Store and Zendesk**, and uses AI to aggregate them into **spikes** — trending words and phrases — which QA can filter by source.
- The volume itself serves as severity: what matters is the thing rising across several channels at once, which no individual channel has the sample size to reveal.
- Tension, from the blog's own example: spike detection produces false signals. The trending token **`da`** turned out to be a fragment of UUIDs pasted into reports rather than anything about a bug. A trend detector needs a triage human, not an alert rule.

## The transferable pattern

1. **Put the report action where the annoyance happens.** One gesture, no navigation, no context switch. Every step you add filters out the reports from people who were mildly irritated, which is most of them.
2. **Attach the context automatically and do not ask for it.** Build, device, locale, session identifier, feature-flag and experiment assignment, and a recording or screenshot. The reporter should supply one sentence; the system supplies the rest.
3. **Capture variant assignment specifically.** In any server-driven product, a report without it describes a state the reader may be unable to enter.
4. **Pool channels rather than staffing them.** Public forums, app stores, support tickets, internal reports and social all go into one pipeline. You are looking for correlated rises, which are invisible inside any single stream.
5. **Rank by rate of change, not by volume.** A steady complaint is a known cost. A new one climbing fast is the regression you shipped this week.
6. **Keep a human on the spikes.** Clustering over free text will confidently surface artifacts of formatting and tooling. Triage is part of the system, not a sign it is broken.

## Apply to your product

- How many actions does it take a user to report a problem right now? Count them honestly, including finding the menu.
- If a report arrived this afternoon, would you know which variants that person was in, on what build, on what device — without asking them?
- Name your feedback channels. Who reads each one, and who would notice the same complaint appearing in three of them this week?

## See also

[[keep-the-visual-record-your-tests-already-produce]] · [[gate-the-release-on-internal-telemetry]] · [[../duo-experimentation/SKILL]]
