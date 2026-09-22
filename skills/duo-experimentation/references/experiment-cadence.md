---
name: duo-experimentation-experiment-cadence
summary: A weekly review rhythm that makes "hundreds per week" survivable instead of overwhelming.
metadata:
  internal: true
---

# Experiment Cadence

## Concept

A high-volume experimentation culture (Duolingo runs a few hundred experiments *simultaneously* in a given week, and launches hundreds per quarter) only works if the review rhythm is bounded. Without a cadence, the team drowns in dashboards. With one, the volume is digestible: every test has a known review moment, every decision has a known committer.

## What Duolingo does

- **The readout is never what the meeting is waiting on.** The experiments service generates statistical reports *every night* for every running experiment, so results exist before anyone asks. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)
- **The stated guideline is to decide the moment the data is sufficient**, not on a calendar. Duolingo's growth write-up names the specific failure: teams letting experiments sit on the back burner to "collect more data," checking in every now and then. Source: blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22)
- **They quantify the cost of the delay.** In their worked example, a 1% retention win launched one week earlier is already adding **7.2% more users per day** by the end of that week — and the gap keeps widening. Review latency is not neutral; it is compounding you never get back.
- **Ramping rollout is part of the cadence.** "Roll out experiments to as many learners as you can, as quickly as you can" — a test parked at a small rollout is a test that will take longer to decide.
- A small set of decision-makers per surface — clear ownership ([[../duo-culture/references/ownership-clarity-culture]]) prevents diffuse responsibility.

## The transferable pattern

Three rules:

1. **Reviews are decision moments, not discovery moments.** If the meeting is the first time anyone's looking at the data, the meeting is wasted.
2. **One owner per decision.** The "we should ship this" or "kill it" call has one name on it.
3. **Speed of review = speed of learning.** A test reviewed three weeks late produces three-weeks-late insight.

Anti-pattern: an experiment program with no scheduled review. Tests pile up, decisions stall, the org loses faith that experiments matter.

## Apply to your product

- Do you have a recurring experiment review? How frequent? Who attends?
- Are decisions made in the meeting, or punted to "let's discuss async"?
- How long does a typical experiment sit between completion and decision?

## See also

[[show-dont-tell]] · [[kill-criteria]] · [[ship-and-iterate]] · [[../duo-culture/references/clock-speed]] · [[../duo-culture/references/no-process-without-purpose]]
