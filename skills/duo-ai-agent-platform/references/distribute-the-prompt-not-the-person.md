---
name: duo-ai-agent-platform-distribute-the-prompt-not-the-person
summary: A working prompt in one person's editor is capped at their throughput — the leverage is the mechanism that turns it into a tool anyone in the org can run.
metadata:
  internal: true
---

# Distribute the Prompt, Not the Person

## Concept

Someone on your team has a prompt that reliably does a tedious job. Treated as a personal tool, it is used once per invocation by one person, and its value is capped by that person's attention. Treated as a published tool with parameters, the same prompt is run by everyone who would otherwise have done the task by hand — and every improvement to it propagates to all of them at once.

The leverage was never the prompt. It is the distribution mechanism.

The second effect is who gets to author. If the authoring surface is a form rather than a codebase, the person who actually feels the pain of the repetitive task can encode it themselves, instead of queueing behind an engineer who does not feel it and cannot prioritize it.

## What Duolingo does

Source: blog.duolingo.com/agentic-workflows (Duolingo blog, 2025-12-11; accessed 2026-09-22)

- Employees create an agent by filling in a JSON form — a prompt, a target repository, and zero or more parameters — and merging it. The agent then appears in a list of internal tools that any employee can run, with progress notifications posted to chat.
- **Under 5 minutes to create a simple form-defined agent, against 1–2 days on average for a custom workflow written in code.** That ratio is the whole argument: the cheap path has to be cheap enough that people use it for tasks they would never have filed a ticket for.
- Authoring is explicitly not limited to engineers — PMs and researchers set up agents too.
- Deployed examples are unglamorous and recurring, which is the point — removing deprecated feature flags, launching and shutting down experiments, and modifying infrastructure config and opening a pull request for it.
- The plumbing every agent needs is shared rather than re-authored, so a form-defined agent inherits the same identity, permissions and conventions as an engineer-built one.

**Tension.** The simple form pattern is described as too simplistic for anything needing multiple agentic passes, additional tools, or task selection at runtime — those still require real engineering. Two tiers, not one. The failure mode to avoid is letting the easy tier quietly become the only tier, and then bending it into something it was never designed to be. Publish the boundary along with the form.

## The transferable pattern

1. **Find the prompt that already works** and is currently living in one person's editor. That is your candidate, not a hypothetical new capability.
2. **Parameterize the two or three things that change** between runs, and nothing else. A form with fifteen fields is a programming language with bad ergonomics.
3. **Publish it where people already look for tools**, with the same permissions, logging and identity as anything built by engineers.
4. **Make authoring cost minutes, not days.** The threshold matters more than the feature set, because it decides which tasks are worth automating at all.
5. **Name the ceiling.** Say out loud what the simple tier cannot do and where the engineering tier begins, so nobody discovers it three weeks into a project.

## Apply to your product

- Which repetitive task in your org is currently solved by one person's private prompt or script, and what happens to it when that person is on leave?
- If a non-engineer wanted to automate a recurring task tomorrow, what is the shortest path they have, and how many days is it?
- What are the two or three parameters that would make your best internal prompt useful to five other teams?

## See also

[[adoption-is-lost-at-every-configuration-step]] · [[separate-what-an-agent-is-from-how-it-runs]] · [[constrain-the-blast-radius-at-the-platform-layer]] · [[../duo-culture/references/clock-speed]]
