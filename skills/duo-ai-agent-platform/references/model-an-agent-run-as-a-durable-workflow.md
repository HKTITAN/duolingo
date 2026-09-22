---
name: duo-ai-agent-platform-model-an-agent-run-as-a-durable-workflow
summary: An agent run hangs, crashes and varies, so give it the retry policy, persisted state and step-level visibility of any long-running job.
metadata:
  internal: true
---

# Model an Agent Run as a Durable Workflow

## Concept

A model call looks like a function call and is not one. A real run takes minutes, calls external systems, sometimes waits on a human, and fails in ways that do not reproduce. Run it as a process and you get the worst properties of a batch job with none of the machinery — no retry policy, no persisted state, no way to see which step burned eleven minutes before dying.

The fix is unglamorous. Model the run as a durable workflow. Each step is one retryable unit with its own timeout and its own retry policy, and its inputs and outputs are recorded. A flaky call then costs one step instead of the whole run, and a failure is something you can look at instead of something you have to reproduce.

The same logic pushes you to make steps small, and to keep the model out of the steps that were never ambiguous.

## What Duolingo does

Source: blog.duolingo.com/agentic-workflows (Duolingo blog, 2025-12-11; accessed 2026-09-22)

- Multi-step agentic workflows run on Temporal, where each step contains a single retryable activity with its own timeouts and retry policy. That is what lets one agent make many model calls without nondeterminism restarting the whole process. The illustrated workflow runs **5 tasks across an 11-minute runtime** — one bad call at minute nine does not replay minutes one through eight.
- With the Temporal plugin, MCP tool calls become activities, so every call's inputs, outputs, failures and retries are visible in the UI; all model requests are routed through an internal LLM Gateway for cost tracking and provider abstraction (blog.duolingo.com/production-ready-ai-agent-platform (Duolingo blog, 2026-08-04; accessed 2026-09-22)).
- A large automated migration was decomposed into ordered steps, each producing its own PR before the next began — **5 upgrade steps**, the first alone bundling 3 components (build tool, JDK and language version), then the framework and base library, then the next JDK, then the OS base image, then the telemetry library. Small steps let prompts be tuned per step, localise failures to one component, and make a rerun cost one step (blog.duolingo.com/automating-jvm-golden-path (Duolingo blog, 2025-12-17; accessed 2026-09-22)).
- Where the next step is deterministic, the model is skipped entirely. Duolingo's mobile test tooling curbed occasional rogue behaviour by adding checks in the software layer, or avoiding the model layer altogether when a clear next step could be executed directly (blog.duolingo.com/reduced-regression-testing (Duolingo blog, 2025-02-07; accessed 2026-09-22)).

**Tension.** The workflow engine constrains the design rather than only serving it. Because activities can run on different workers, cloning a repository and then operating on it cannot be split into separate activities — which forces coarser, less reusable steps than a clean decomposition would suggest. The deterministic escape hatch has limits too: the model still struggled with the most complex task types, including long nuanced comparisons and timed interactions.

## The transferable pattern

Treat any multi-step automated run as infrastructure, not as a script:

1. **One retryable unit per step**, each with its own timeout and retry policy. Ask of every step, "if this fails on attempt three, what work is discarded?" If the answer is "all of it", the step is too big.
2. **Persist inputs and outputs per step.** Nondeterministic failures cannot be reproduced on demand, so the record is the only debugging surface you will ever have.
3. **Make steps as small as they can independently be verified**, and let each one emit its own reviewable output.
4. **Spend model calls only where ambiguity lives.** A generated step you could have hard-coded buys nothing and costs you reproducibility.

Expect the engine's boundaries to shape your decomposition. That is an acceptable trade — a slightly uglier step graph that survives failure beats an elegant one that restarts.

## Apply to your product

- In your longest automated job, what is the unit of retry today? If it is the whole job, what does one flaky external call currently cost you in time and spend?
- Which steps in that job are genuinely ambiguous, and which are you handing to a model out of habit?
- When a run fails overnight, what can you see the next morning — a stack trace, or the actual inputs and outputs of the step that failed?

## See also

[[separate-what-an-agent-is-from-how-it-runs]] · [[every-producer-needs-a-janitor]] · [[grade-the-artifact-not-the-prose]]
