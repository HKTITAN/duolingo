---
name: duo-experiment-velocity
description: Drive the marginal cost of an experiment toward zero so a team runs hundreds of tests a quarter instead of three. Covers experimentation as shared internal infrastructure rather than a per-test project, how the cost of the marginal test quietly selects which ideas get tried at all, taking domain owners off the engineering queue for whole classes of test, judging internal analytics tools by non-analyst adoption, building tools that can disconfirm your own beliefs, and curating report templates with standing guardrails that may veto a win. Use when asking why we only run three experiments a quarter, should we build or buy an experimentation platform, how do we let PMs and designers run their own tests, what belongs in every experiment readout, when do we instrument a metric versus compute it by hand, or is a customer-specific fork worth the permanent drag on test velocity.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Experiment Velocity

Most organisations do not have an idea shortage. They have a per-test cost that nobody has ever measured, and that cost silently decides both how many experiments run and which ideas are allowed to be one. This skill is about the machine that produces results — the platform, the tooling, the self-serve surfaces and the standard readout — not about whether any single result is true.

Scan the descriptions, follow only the links you need.

## The economics

- [[references/marginal-cost-decides-which-ideas-get-tested]] — volume tracks the cost of one more test, and expensive tests quietly restrict the portfolio to ideas someone already believes.
- [[references/experiments-as-shared-infrastructure]] — template setup, eligibility, hypothesis and nightly analysis into one internal service so learning rate scales with traffic rather than headcount.

## Get the bottleneck out of the way

- [[references/take-the-domain-owner-off-the-engineering-queue]] — when the person with the judgement is not the person with commit access, a whole class of experiment never gets proposed.
- [[references/self-serve-adoption-is-the-tooling-metric]] — count the non-analysts who get their own answers, because every unanswerable question becomes a queued request or a silent guess.

## What the machine should produce

- [[references/build-tools-that-can-embarrass-you]] — cheap arbitrary cohorting is what lets a finding nobody went looking for reach a decision.
- [[references/curate-the-report-per-experiment-type]] — a per-type metric list plus standing guardrails makes relevance a design-time decision, and lets a guardrail kill a revenue win.

## Boundary

This skill owns the machine. It does not own believing a specific result — choosing the right outcome metric, controlling for selection, and reading a result you cannot randomise live in [[../duo-experimentation/SKILL]] and [[../duo-measurement-validity/SKILL]]. If your question is "is this effect real?", start there.

## Sibling skills

- [[../duo-experimentation/SKILL]] — the protocol for a single test, including hypothesis design, guardrails and kill criteria.
- [[../duo-measurement-validity/SKILL]] — whether the number you produced survives an outsider's scrutiny.
- [[../duo-localization/SKILL]] — the infrastructure that makes a variant resolve per market instead of per build.
- [[../duo-growth-model/SKILL]] — what you do with hundreds of results once the machine is running.

## Sources

blog.duolingo.com — the experiments service, Expurrimenter and CopyCAT, the internal analytics suite, cohorts and correlations, growth principles, and engineering life posts cited node by node.
