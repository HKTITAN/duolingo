---
name: duo-ai-agent-platform-separate-what-an-agent-is-from-how-it-runs
summary: Put the definition of an agent in a registry and its execution in one shared platform, so a new agent is a config entry and a vendor swap is a parameter.
metadata:
  internal: true
---

# Separate What an Agent Is From How It Runs

## Concept

Two things get tangled in the first agent anyone builds. There is what the agent **is** — its prompt, the tools it may call, what it is allowed to reach, the shape of its output. And there is how it **runs** — which runtime, which model vendor, which SDK, which environment, whose credentials, where the traces land.

Couple them and you pay twice. Every new agent re-solves credentials, cloning, tool wiring and observability from scratch, so quality depends on how much patience the author had that week. And every runtime change is a rewrite of every agent, which means you cannot move when the ecosystem does.

Split them and the definition becomes data. The platform becomes the only place durability, observability and evaluation are implemented, and every agent inherits them whether its author thought about them or not.

## What Duolingo does

Source: blog.duolingo.com/production-ready-ai-agent-platform (Duolingo blog, 2026-08-04; accessed 2026-09-22)

- An agent registry holds the definition — an `AgentDefinition` carrying name, owner, system prompt, model, MCP servers and output type. A workflow wrapper holds the execution. New agents inherit durability, observability, orchestration and evaluation rather than re-implementing them.
- Standing up a production-ready agent went from **several weeks of setup to about 10 minutes**.
- The OpenAI Agents SDK was added later as just another implementation behind the same interface, sitting alongside the Claude Agents SDK and Codex CLI runtimes. Adding a runtime did not touch any agent definition.
- A single internal coding-agent library wraps both the Codex CLI and the Claude Code SDK; with API keys already in the environment, calling an agent means declaring a prompt, and in most cases switching agents is one enum parameter (blog.duolingo.com/agentic-workflows (Duolingo blog, 2025-12-11; accessed 2026-09-22)).
- The same split was applied to a mass migration — a YAML config defines an upgrade as a collection of smaller upgrades, each component naming its deterministic recipe, whether a model is needed at all, and which prompt template to use, one config file per upgrade, so the runner outlives the migration and the next one is a config change (blog.duolingo.com/automating-jvm-golden-path (Duolingo blog, 2025-12-17; accessed 2026-09-22)).

**Tension — keep the layer thin.** Duolingo built two parallel versions of a feature-flag-removal agent over 1–2 weeks, then discarded both when a new CLI shipped and three looped prompts collapsed into one that worked; the prototype was running in about a day and productionized in about a week once the stack settled (blog.duolingo.com/buildingaiagents (Duolingo blog, 2025-12-04; accessed 2026-09-22)). They also accepted real ugliness to move — running a CLI as a subprocess with approvals bypassed, on an isolated instance, giving up structured output and deterministic parsing. And generality did not survive heterogeneity: getting the migration workflow to work on one service was easy, on hundreds it was not, because template drift meant there was no consistent way a service was built.

## The transferable pattern

Write down, for your automation, which fields describe intent and which describe execution. Intent is the instruction, the permitted tools, the scope of access, the output contract. Execution is the runtime, the vendor, the credentials, the retries, the telemetry.

Then:

1. **Intent becomes data** — a registry entry, a config file, a form submission. Reviewable, diffable, ownable by the person who understands the task.
2. **Execution becomes one shared substrate** with exactly one implementation per concern.
3. **One interface between them**, wide enough that a second vendor is an added implementation and not a fork.

The payoff is not elegance, it is optionality. Price, quality and availability in a fast-moving capability area move faster than your code can, and the abstraction is what converts a vendor migration from a project into an edit. Keep the wrapper thin and expect to throw it away — a deep custom framework in a domain that changes monthly is a sunk cost you then have to maintain.

## Apply to your product

- In your current automation, where is the vendor name actually written down? If it appears in more than one place, you have coupled definition to execution.
- What would it cost you today to run the same task on a different provider — an afternoon, or a quarter?
- Which parts of your recurring jobs are genuinely one-off, and which are a config file plus a runner you would otherwise rebuild next quarter?

## See also

[[model-an-agent-run-as-a-durable-workflow]] · [[distribute-the-prompt-not-the-person]] · [[standardize-the-integration-surface]]
