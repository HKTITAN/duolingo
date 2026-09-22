---
name: duo-ai-agent-platform-standardize-the-integration-surface
summary: The cost centre in many integrations is variance in how they are built and run, not their number — one transport, one auth shape, one URL pattern, hosted centrally.
metadata:
  internal: true
---

# Standardize the Integration Surface

## Concept

Teams assume the pain of connecting an agent to twenty systems scales with twenty. It does not. It scales with how many different shapes those twenty connections take, multiplied by the number of machines they run on.

Every distinct runtime, transport and auth scheme is a separate set of failure modes, and each one multiplies again across every developer's laptop — version mismatches, resource-hungry containers, orphaned processes. The support burden looks like an integration problem and is actually a variance problem.

Collapse the variance and adding the twenty-first integration becomes a config entry rather than a debugging session. That is the thing that lets the count grow at all.

## What Duolingo does

Source: blog.duolingo.com/aislackbot (Duolingo blog, 2026-05-20; accessed 2026-09-22)

- Engineers first wired up integration servers locally with **mixed runtimes (Node, Python, Go, Docker)** and **mixed transports (stdio, SSE, HTTP)**. The result was constant works-on-my-machine failures — mismatched package manager versions, containers eating local resources, zombie processes left behind.
- In **August 2025** Duolingo standardized on **internally hosted HTTP integration servers**: one auth token, one predictable URL pattern. Nothing runs on a laptop, so nothing depends on how that laptop is configured.
- The integration catalogue spans observability, alerting, source control, CI, ticketing, cloud and data warehouse tools — including Honeycomb, Grafana, Sentry, PagerDuty, GitHub, Jenkins, Jira, AWS and BigQuery. Adding a capability to the agent means deploying another server behind the same pattern, with no change to the agent itself.
- The framework was open-sourced at github.com/duolingo/slack-ai-agent, which is its own constraint on drift — a public interface is one you stop quietly special-casing.

**Tension.** Central hosting moves cost rather than removing it. Someone now owns uptime, deploys and auth rotation for every server, and a team with an unusual requirement has to either fit the pattern or go without. That is a real tax on the edge cases, paid to remove a tax on everyone else — worth taking deliberately rather than discovering later.

## The transferable pattern

Pick one of each, and write it down:

1. **One transport.** Not the best one for each case; the one that works acceptably for all of them.
2. **One auth shape.** A single token type obtained the same way, so credential handling is implemented once and rotated once.
3. **One address pattern**, predictable enough that a new integration's location can be guessed correctly.
4. **One place they run.** Centrally hosted beats per-machine, because per-machine multiplies every failure by the number of machines and makes every fix a coordination problem.

Then treat exceptions as a decision with a named owner, not as a default. The measure of success is how long it takes to add integration N+1 — if that number is flat as N grows, the standardization is working; if it climbs, variance has crept back in.

## Apply to your product

- List your current integrations by transport, auth scheme and where they run. How many distinct shapes is that, and which ones exist only because of who built them first?
- How much of your support load is version and environment drift on individual machines rather than the integrations themselves?
- What would adding your next integration cost — an afternoon of config, or a week of debugging someone else's setup?

## See also

[[adoption-is-lost-at-every-configuration-step]] · [[separate-what-an-agent-is-from-how-it-runs]] · [[../duo-culture/references/no-process-without-purpose]]
