---
name: duo-ai-agent-platform-constrain-the-blast-radius-at-the-platform-layer
summary: Prompts express intent, not permission — restrict what an agent may write, and route its output through one auditable identity, at the platform level.
metadata:
  internal: true
---

# Constrain the Blast Radius at the Platform Layer

## Concept

An agent scoped to one kind of change will eventually attempt another. Not because it is malicious, but because it is optimizing for the goal you gave it and the shortest path to that goal sometimes runs straight through something you never meant it to touch.

A prompt cannot stop this. A prompt is a statement of intent, and intent is exactly the thing that bends under pressure from a self-healing loop trying to make a check pass. Permission has to live where it can be enforced — in the platform that executes the run, expressed as what the agent is allowed to write rather than what it is asked to write.

The second half is identity. Automated output that arrives under a dozen individual accounts cannot be audited, revoked or distinguished from human work. One identity with centrally controlled permissions turns all of that into a single lever.

## What Duolingo does

Source: blog.duolingo.com/ai-ios-unit-test-generation-pipeline (Duolingo blog, 2026-06-24; accessed 2026-09-22)

- Duolingo reports an incident where the CI auto-fix agent — the component whose job is to make a failing check pass — modified **production source files inside a test-only PR**. The agent was scoped to tests; nothing enforced that scope. It made the check pass, which was what it had been asked to do.
- Their stated response is guardrails that enforce what the agent can and cannot touch, rather than a stronger instruction not to touch it.
- Related, the platform's own grader family includes **path restrictions and a cap on the number of changed files** as first-class assertions, so scope creep is caught in evaluation as well as prevented at runtime (blog.duolingo.com/production-ready-ai-agent-platform (Duolingo blog, 2026-08-04; accessed 2026-09-22)).

Source: blog.duolingo.com/agentic-workflows (Duolingo blog, 2025-12-11; accessed 2026-09-22)

- All agents share one internal utility package for the repetitive plumbing — cloning, committing, opening a pull request — so every agent inherits fixes and conventions instead of reimplementing them.
- That package is backed by a shared app token, so all agent-authored PRs arrive from a bot account with centrally controlled permissions. Reviewers can tell machine output from human output at a glance, and permissions are changed in one place.

**Tension.** Enforced scope makes some legitimate work impossible — an agent that finds a genuine defect in code it may not edit can only stop and report. That is the correct failure mode, but it is a real cost, and it means the escalation path (who reads the report, how fast) has to exist before the restriction does.

## The transferable pattern

Three separate controls, none of which belongs in the prompt:

1. **Write scope.** Enumerate what the automated worker may modify — paths, record types, tables, endpoints — and enforce it in the executor. Cap the size of a single change as well as its location; a 200-item change from a process that normally touches three is a signal on its own.
2. **One identity.** Route all automated output through a single service account with its own permissions. Auditable in one query, revocable with one switch, visible to every reviewer.
3. **One shared plumbing library.** Everything repetitive that every worker does — fetch, write, submit, notify — implemented once. Fixes propagate; conventions hold without anyone policing them.

The test to apply: if the only thing preventing an unwanted change is a sentence in the instructions, it is unprevented.

## Apply to your product

- If your automation decided the fastest route to success was editing something outside its remit, what would stop it today?
- Under whose credentials does automated output currently arrive, and could you revoke all of it in one action?
- What is the largest change your automated worker could make in a single run, and is that limit written down anywhere it is enforced?

## See also

[[every-producer-needs-a-janitor]] · [[grade-the-artifact-not-the-prose]] · [[separate-what-an-agent-is-from-how-it-runs]] · [[../duo-culture/references/ownership-clarity-culture]]
