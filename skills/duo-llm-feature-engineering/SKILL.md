---
name: duo-llm-feature-engineering
description: Make an LLM or agent feature survive its ten-thousandth call — split the prompt into a fixed constraint zone and per-instance slots, decompose a long interaction into one narrow prompt per move, isolate the high-stakes generation into its own call, over-generate and let expert-owned evaluators hold the quality bar, prefer examples from your own corpus over more instructions, and carry memory as extracted facts not replayed transcripts. Use when a prompt works in a demo but drifts in production, when output gets worse as you add rules, when an AI conversation rambles or never ends, or when scaling generated content without losing the bar. Triggers on phrases like prompt template, prompt engineering, my prompt got worse, LLM feature quality, AI content pipeline, agent memory, LLM as a judge, generate variations, hallucination guardrails, chatbot ignores the user.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo LLM Feature Engineering

Getting a model to do something once is a demo. Getting it to do that thing on the ten-thousandth call, for a user you have never met, without anyone noticing that quality slid — that is the work this skill covers.

Distilled from Duolingo's public engineering and product writing across test-item generation, audio content at scale, conversational practice and large-scale code migration. The reader is assumed to be building something else entirely; every node ends in questions about your product.

**Scope note.** Whether to build the AI feature at all, where in the business to point AI, what it does to unit economics, and how to divide labour between your expert org and your models across a whole pipeline belong to the `duo-ai-product-strategy` skill. This one starts after that decision and is about making the thing not break.

## Prompt structure — the artifact, not the message

- [[references/prompt-as-template-not-freeform]] — fixed constraints in one zone, per-instance slots in the other, so operators supply judgement and never format.
- [[references/examples-from-your-corpus-beat-more-instructions]] — when output is poor, add curated in-domain exemplars and delete rules; instructions describe the target, examples are it.
- [[references/find-the-context-optimum]] — prompt size has a peak, not a budget; the worked example earns its place by frequency.

## Decomposition — one job per call

- [[references/one-narrow-prompt-per-move]] — build a conversational feature as a small state machine with a mid-flight override and a programmed ending, not one long free-running prompt.
- [[references/isolate-the-high-stakes-generation]] — split the critical artifact into its own call, because constraint competition sacrifices the rule the feature exists for.
- [[references/memory-as-extracted-facts-not-transcripts]] — extract a bounded, typed fact list at the session boundary instead of replaying history forever.

## Holding a quality bar at volume

- [[references/scope-generation-to-work-with-no-rhetorical-goal]] — the first filter on any AI content pipeline; work that needs coverage rather than persuasion is the work that clears the bar.
- [[references/the-filter-holds-the-bar-not-the-generator]] — over-generate, score against named criteria, let domain experts own the evaluator, and reuse the rejects as hard negatives.
- [[references/dont-collapse-the-candidate-set]] — never silently pick one answer; put the human, or the end user, at the ranking step.

## Bounding what the model can do

- [[references/human-authored-frame-model-improvises-inside]] — humans fix the scenario, the opening and the destination; the user's measured level goes in as imperative constraints every turn.

## Sibling skills

- [[../duo-ai-agent-platform/SKILL]] — running agents as infrastructure: registries, durable workflows, tool allowlists, evals and adoption.
- [[../duo-production-reliability/SKILL]] — keeping always-on systems honest: telemetry gates, kill switches, incident playbooks, free reporting.
- [[../duo-rules-and-heuristics/SKILL]] — when to state a rule explicitly versus let someone induce it, and how to ship a shortcut with its coverage rate.
- [[../duo-experimentation/SKILL]] — proving a change helped, which is the only way a prompt edit stops being a matter of opinion.

## Sources

Distilled from blog.duolingo.com — scaling-duoradio, large-language-model-duolingo-lessons, test-creation-machine-learning, chatbot-language-practice, ai-and-video-call, duolingo-max, automating-jvm-golden-path, how-to-use-online-translators-and-dictionaries. Each node carries its own dated citation.
