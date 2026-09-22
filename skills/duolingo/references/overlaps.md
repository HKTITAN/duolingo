---
name: duolingo-overlaps
summary: The skill pairs that get confused, each with the single question that settles it — read this instead of reading both skills.
metadata:
  internal: true
---

# Overlaps — the pairs that blur

## Concept

Most misroutes in this pack are not "wrong topic." They are **right topic, wrong altitude** — the answer is plausible, on-subject, and solves a different problem than the one asked. That failure is hard to catch because nothing looks broken.

Each row below is one question, not two skills to read. Ask it, take the branch, stop.

## What Duolingo does

Duolingo's own teams hit the same seams. The Time Spent Learning Well post is explicitly a *product* decision (which number do we optimize) that kept being mistaken for an *experimentation* decision (which test do we run), and the post exists because the first framing kept producing the wrong experiments. Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22).

## The transferable pattern

### Habit, streaks and returning

| Torn between | Ask | Then |
|---|---|---|
| `duo-retention` / `duo-streak-mechanics` | Are you diagnosing the churn, or designing the chain itself? | Why they leave, and the drop-off shape → retention. Bar height, freezes, pauses, milestones → streak-mechanics. |
| `duo-retention` / `duo-return-triggers` | Do you know *why* they left? | No → retention, diagnose first. Yes, and now you need the next session to start → return-triggers. |
| `duo-retention` / `duo-learner-motivation` | Are they not coming back, or coming back and refusing to try? | Absent → retention. Present but unwilling → learner-motivation. |
| `duo-streak-mechanics` / `duo-gamification` | Is the counter one person's, or does standing depend on other people? | Solo chain → streak-mechanics. Ranking, leagues, shared quests → gamification. |
| `duo-perceived-progress` / `duo-score-credibility` | Who is the number for? | The user, to feel movement → perceived-progress. An outsider who must trust it → score-credibility. |

### Teaching and mastery

| Torn between | Ask | Then |
|---|---|---|
| `duo-memory-and-decay` / `duo-difficulty-calibration` | *When* to bring it back, or *how hard* to make it? | Scheduling and forgetting → memory-and-decay. Targeting ability → difficulty-calibration. |
| `duo-progression-design` / `duo-rules-and-heuristics` | Where a thing sits in the path, or whether it gets stated at all? | Ordering and scaffolding → progression-design. Explain-vs-discover, and how to phrase the rule → rules-and-heuristics. |
| `duo-difficulty-calibration` / `duo-attention-budget` | Is the item too hard, or is the screen asking too much at once? | Correctly targeted but failing → attention-budget. Mis-targeted → difficulty-calibration. |
| `duo-efficacy-measurement` / `duo-measurement-validity` | Proving it works, or proving the instrument is honest? | Did users get better → efficacy-measurement. Will an outsider accept the number → measurement-validity. |
| `duo-progression-design` / `duo-prior-knowledge-transfer` | Are you designing the path, or discovering what they already carry? | The sequence → progression-design. Why one cohort is faster → prior-knowledge-transfer. |

### Deciding and measuring

| Torn between | Ask | Then |
|---|---|---|
| `duo-product` / `duo-metric-design` | Picking what to build, or picking what to be graded on? | What → product. Which number → metric-design. |
| `duo-metric-design` / `duo-experimentation` | Choosing the number, or trusting a result you already have? | Choosing → metric-design. Believing → experimentation. |
| `duo-experimentation` / `duo-experiment-velocity` | Can't afford enough results, or don't believe the one you have? | Throughput and cost per test → experiment-velocity. Causality → experimentation. |
| `duo-adoption-design` / `duo-perceived-progress` | They never start, or they start and feel stuck? | Never start → adoption-design. Stall mid-way → perceived-progress. |
| `duo-freemium-monetization` / `duo-growth-model` | Where the paid line goes, or which lever to staff? | Pricing boundary → freemium-monetization. Which growth input actually moves → growth-model. |

### Reaching people

| Torn between | Ask | Then |
|---|---|---|
| `duo-growth` / `duo-proprietary-data-reports` | Buying attention, or earning it with what you already know? | Loops, referrals, stunts → growth. Publishing your own data → proprietary-data-reports. |
| `duo-proprietary-data-reports` / `duo-timely-data-publishing` | A recurring report, or one finding shipped fast? | Annual, fixed window → proprietary-data-reports. A spike worth publishing this week → timely-data-publishing. |
| `duo-motivation-segmentation` / `duo-motivation-and-attachment` | Asking why they came, or predicting who stays? | Declared motive as a dimension → motivation-segmentation. Which segment retains → motivation-and-attachment. |
| `duo-growth` / `duo-localization` | Same audience, or one that doesn't share your language or constraints? | Same → growth. New locale, script, or bandwidth reality → localization. |
| `duo-localization` / `duo-inclusive-access` | Is the blocker language, or circumstance? | Language, script, market → localization. Device, bandwidth, credentials, disability → inclusive-access. |

### Building it

| Torn between | Ask | Then |
|---|---|---|
| `duo-llm-feature-engineering` / `duo-ai-product-strategy` | Making a model you've committed to behave, or deciding whether to use one at all? | Prompts, evals, output quality → llm-feature-engineering. Where to point AI → ai-product-strategy. |
| `duo-llm-feature-engineering` / `duo-ai-agent-platform` | One feature's output, or the infrastructure many agents run on? | One feature → llm-feature-engineering. Registry, runtime, swapping models → ai-agent-platform. |
| `duo-ml-in-production` / `duo-llm-feature-engineering` | A model you trained, or one you prompt? | Trained, evaluated, deployed → ml-in-production. Prompted → llm-feature-engineering. |
| `duo-backend-architecture` / `duo-production-reliability` | Making it fast, or knowing what it is doing? | Request path → backend-architecture. Tracing, incidents, observability → production-reliability. |
| `duo-backend-architecture` / `duo-infra-cost-efficiency` | Latency, or spend? | Fast → backend-architecture. Cheap, with attribution → infra-cost-efficiency. |
| `duo-mobile-engineering` / `duo-inclusive-access` | App health, or who gets locked out? | Startup, size, cost to change → mobile-engineering. Users excluded by device or bandwidth → inclusive-access. |

### Across the pack

| Torn between | Ask | Then |
|---|---|---|
| `duo-culture` / `duo-product` | Is the blocker how the team works, or what it decided to build? | Team → culture. Decision → product. |
| `duo-voice` / `duo-character-systems` | The sentence, or the cast that says it? | Wording and tone → voice. A reusable character, its look and behaviour → character-systems. |
| `duo-voice` / `duo-naming-and-notation` | Prose the user reads, or the label on the thing? | Messages, copy, errors → voice. What it is called, and symbols → naming-and-notation. |
| `duo-design` / design-engineering | *Why* it should feel that way, or *how* to build it? | Why → duo-design. How → [[design-handoff]]. |
| Any skill / no skill | Would the answer change if the product weren't Duolingo-like at all? | If the honest answer is "this doesn't apply here" — say that. See [[translate]]. |

**When both still look right, answer from the narrower skill and link the other.** A specific skill's values plus a pointer beats a blended answer from two, because blending quietly drops the preconditions that make each one true.

**The frequency check comes first.** Before any row in the habit family, ask whether the product has a genuinely recurring use case. A payroll tool used twice a month does not have a retention problem; it has a frequency that a streak would only punish. See [[translate]].

## Apply to your product

- Which two of your own systems, docs, or teams get confused for each other — and is the confusion about topic, or about altitude?
- For your most-confused pair, what is the single question that settles it? That sentence is worth more than another page of documentation.

## See also

[[chains]] · [[map]] · [[translate]] · [[design-handoff]]
