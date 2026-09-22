---
name: duo-ai-agent-platform
description: Run LLM agents as production infrastructure instead of demos — split what an agent is (prompt, tools, access, output schema) from how it runs (runtime, model, SDK, environment), make every step durable and retryable, grade the diff instead of the prose, cap retries on automated producers, and get non-engineers actually using the thing. Use when standing up an agent platform, wiring an agent into CI, deciding whether a repetitive task is worth automating, writing agent evals, or asking why nobody uses the internal tool you shipped. Triggers on phrases like build an agent platform, agent registry, durable workflow, Temporal, agent evals, LLM as judge, MCP server, auto-generated PRs, bot account permissions, internal tool adoption, our agent retries forever, should we automate this.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo AI Agent Platform

How to run LLM agents as infrastructure rather than as demos — the orchestration, the guardrails, the evaluation, and the unglamorous work of getting the capability adopted.

Distilled from Duolingo's engineering blog, where a company running hundreds of microservices put agents into CI, into migrations, into QA and into chat. The reader here is assumed to be building something else entirely; every node ends in questions about your product.

**This skill does not own trained models that make product decisions.** Ranking, evaluation metric design and generation pipelines belong to the ML-in-production skill; this one owns orchestration, tooling and adoption.

## Architecture — what an agent is, and how it runs

- [[references/separate-what-an-agent-is-from-how-it-runs]] — definition in a registry, execution in one shared platform, so a new agent takes minutes and a vendor swap is a parameter.
- [[references/model-an-agent-run-as-a-durable-workflow]] — every step one retryable unit with its own timeout, so a flaky call costs a step and not an eleven-minute run.
- [[references/standardize-the-integration-surface]] — the cost is variance in how integrations are built and run, not how many there are.

## Guardrails — what the agent may touch, and when to stop

- [[references/constrain-the-blast-radius-at-the-platform-layer]] — enforce write scope and one auditable identity in the platform, because a prompt expresses intent, not permission.
- [[references/every-producer-needs-a-janitor]] — a retry cap, a staleness deadline and a cooldown, or the system re-attempts its own failures forever.

## Evaluation — proving it worked

- [[references/grade-the-artifact-not-the-prose]] — deterministic graders over the diff, a consistency check against the agent's self-report, a model judge only as a supplement.
- [[references/run-it-manually-and-categorize-failures-first]] — weeks of manual runs, every failure categorized, as a free structural audit of your own system.
- [[references/verification-becomes-the-bottleneck]] — automating generation relocates the queue to review; plan the whole chain first.

## Adoption — getting it used

- [[references/distribute-the-prompt-not-the-person]] — the leverage is the distribution mechanism, not the prompt; a form beats a codebase as an authoring surface.
- [[references/adoption-is-lost-at-every-configuration-step]] — each setup step filters most users out, so move the capability into the surface they already sit in.

## Where to start

- Standing up the first agent — [[references/separate-what-an-agent-is-from-how-it-runs]], then [[references/model-an-agent-run-as-a-durable-workflow]].
- Considering automating an existing manual job — [[references/run-it-manually-and-categorize-failures-first]], then [[references/verification-becomes-the-bottleneck]].
- It works but nobody uses it — [[references/adoption-is-lost-at-every-configuration-step]].
- It works and is now generating mess — [[references/every-producer-needs-a-janitor]] and [[references/constrain-the-blast-radius-at-the-platform-layer]].

## Sibling skills

- [[../duo-experimentation/SKILL]] — measuring whether the automated change actually helped, and when to kill it.
- [[../duo-product/SKILL]] — deciding what deserves building at all before deciding to automate it.
- [[../duo-culture/SKILL]] — the candor, ownership and clock-speed norms that decide whether internal tooling gets adopted.

## Sources

Distilled from blog.duolingo.com posts published 2021-03-17 to 2026-08-04 — agentic-workflows, production-ready-ai-agent-platform, ai-ios-unit-test-generation-pipeline, automating-jvm-golden-path, buildingaiagents, aislackbot, reduced-regression-testing, open-sourcing-metasearch-our-one-tool-to-search-them-all, and life-at-duolingo-julie-wang. Each node carries its own dated citation.
