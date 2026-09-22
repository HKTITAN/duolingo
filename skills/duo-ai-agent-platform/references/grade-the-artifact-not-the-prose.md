---
name: duo-ai-agent-platform-grade-the-artifact-not-the-prose
summary: Judge an agent on what it changed, not what it said — deterministic graders over the diff, a consistency check against its own self-report, and a trace a human can scrub.
metadata:
  internal: true
---

# Grade the Artifact, Not the Prose

## Concept

An agent's summary of its own work is the least reliable output it produces. It will report success having changed nothing, or report a no-op while having edited files, and any grader that reads text passes both. The only thing that cannot be talked around is the artifact — the diff, the record, the changed state.

So make deterministic graders the foundation and treat a second model as a supplement, never the sole signal. A judge model shares the blind spots of the model it is judging, which is exactly the wrong property in an evaluator.

And add the grader people skip — a consistency check comparing what the agent claimed it did against what actually changed. That gap is where the expensive failures live.

## What Duolingo does

Source: blog.duolingo.com/production-ready-ai-agent-platform (Duolingo blog, 2026-08-04; accessed 2026-09-22)

- Agent evals run the real agent against authored scenarios and grade the resulting git diff, not the transcript. Three grader families do the work — `structured_output` (the response matches the declared schema), `diff_assertions` (required strings, forbidden strings, a maximum number of changed files, and path restrictions), and `no_op_consistency` (the agent said it changed nothing; did it?). An LLM judge is available and optional.
- **Tension they name themselves.** Exact diff assertions are too brittle for some scenarios, which is the only reason the judge exists at all — and they still refuse to let it be the only signal. Both halves matter: the deterministic grader is not sufficient, and the model grader is not trustworthy alone.

Source: blog.duolingo.com/reduced-regression-testing (Duolingo blog, 2025-02-07; accessed 2026-09-22)

- Duolingo's QA team first wrote automated mobile tests as explicit tap sequences and spent weeks playing whack-a-mole, because the company ships weekly and runs so many experiment variants that the next screen is genuinely unpredictable. Reframing each test as a broad goal — progress until you reach the completion screen — made runs reliable, cut manual regression workflows by **as much as 70%**, and let non-coders author tests for session progression, onboarding and social features within a few hours.
- **Tension — reliability was bought with detection.** The post says plainly that more reliable runs introduce the potential for missing issues the agent was simply able to work around, and that many bugs do not strictly block progress. A goal-seeking agent treats your defect as an obstacle and routes around it, so a green result proves only that the goal was reachable.
- Their answer is the recorded trace. Runs are recorded and reviewing those recordings became core to the workflow — what used to take several hours for numerous QA people every week became a process of minutes of scrubbing.

## The transferable pattern

1. **Grade the change, not the narration.** Whatever your agent's output object is, assert against it.
2. **Deterministic first.** Schema conformance, required and forbidden content, blast-radius limits like maximum items touched and allowed paths. These are cheap, fast, and do not hallucinate.
3. **Add a consistency grader.** Compare the self-report to the artifact. Silent no-ops and unreported edits are both caught here and nowhere else.
4. **A model judge is a supplement** for the cases assertions are too brittle to express — never the only gate.
5. **Frame instructions as goal states, then keep the trace.** Goal framing survives an environment that changes weekly; the trace is what you trade for it. You are converting execution time into review time, not eliminating the human.

## Apply to your product

- What is the artifact your automation produces, and does any current check look at it — or only at the status it reports?
- If your agent did nothing at all but claimed success, which of your checks would fail?
- If you moved to goal-framed instructions, what would a reviewer scrub afterwards, and does that record exist today?

## See also

[[verification-becomes-the-bottleneck]] · [[constrain-the-blast-radius-at-the-platform-layer]] · [[../duo-experimentation/references/metric-selection]]
