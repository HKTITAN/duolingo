---
name: duolingo-map
summary: Every skill in the pack, one line each, grouped by family — open this when the router tables did not match.
metadata:
  internal: true
---

# Map — the whole pack

## Concept

44 skills, grouped into 8 families. The router's tables handle the common phrasings; this is the full index for when they don't match.

Every skill is self-contained — the numbers and mechanisms live in its nodes, not behind a link.

## What Duolingo does

Duolingo organizes its own public writing by audience rather than by internal team, which is why the engineering posts and the learning-science posts read as one body of work. Source: blog.duolingo.com/hub/design/ (Duolingo blog; accessed 2026-09-22). This index copies that: families are named for the problem the reader has, not for the department that would own it.

## The transferable pattern

### They stop coming back

Habit, streaks, churn, and re-entry.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-retention/SKILL]] | 12 | Why people stop coming back, how to find the day they leave, and what the shape of that drop-off tells you to fix. |
| [[../duo-streak-mechanics/SKILL]] | 7 | How to design an unbroken-chain commitment counter — how low to set the daily bar, how much slack to build in, when to let it pause, and what it will quietly certify that you did not intend. |
| [[../duo-return-triggers/SKILL]] | 12 | How to cause the next session to start — the cue, the surface, the permission ask, and the re-entry path for someone who already stopped. |
| [[../duo-perceived-progress/SKILL]] | 7 | How to make effort feel like it is going somewhere — the granularity of your progress number, the size of your completion unit, the honesty of your timeline, and what to do when the user stalls because they succeeded. |
| [[../duo-motivation-and-attachment/SKILL]] | 7 | How to find out which users will still be here in a year and why — segmenting by motive rather than demographics — and how to build the attachment, safety and permission that keep an optional behaviour worth doing. |

### They are here but flat

Reward, play, and willingness to try.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-gamification/SKILL]] | 17 | The reward layer — points, levels, celebration, and the line where a loop stops being fun and starts feeling owed. |
| [[../duo-learner-motivation/SKILL]] | 13 | Get people to keep attempting the thing — by lowering what it costs to be visibly bad at it, replacing unreachable goals with ones they can score, and telling them in advance how bad it will feel. |

### The product has to teach them something

Duolingo's deepest public knowledge, and the least copied.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-memory-and-decay/SKILL]] | 13 | Decide when to bring something back in front of a user, and treat every capability they have as something that is quietly rotting rather than something they banked. |
| [[../duo-progression-design/SKILL]] | 13 | Decide what to teach, in what order, with how much support — and design the removal of that support rather than leaving it in forever. |
| [[../duo-rules-and-heuristics/SKILL]] | 13 | Decide whether to explain at all, when the explanation lands, and how to compress a rule into something a user can actually execute under pressure. |
| [[../duo-difficulty-calibration/SKILL]] | 10 | Put each user at the edge of what they can currently do — model ability and item difficulty together, target a band rather than a floor, and use live signals to tell whether the model is honest. |
| [[../duo-prior-knowledge-transfer/SKILL]] | 11 | Work with the model your users already carry from somewhere else — it is why some things are free, why the near-misses are your most expensive errors, and why confusion clusters exactly where two things are almost the same. |
| [[../duo-attention-budget/SKILL]] | 10 | Treat working memory as the binding constraint on any screen, session or document — cap what competes for it, strip what wastes it, and deliberately spend what is left on the one thing you are trying to teach. |
| [[../duo-efficacy-measurement/SKILL]] | 8 | Prove the thing actually works — with instruments you did not author, on axes that do not substitute for each other, and in a way a sceptic outside your company can check. |

### The words and the face

Voice, characters, naming, and interface rationale.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-voice/SKILL]] | 17 | A product voice that survives more than one writer — push copy, error messages, empty states, and what tone costs the reader. |
| [[../duo-character-systems/SKILL]] | 11 | How to build a reusable cast, illustration style, animation vocabulary and voice set that a small team can produce at volume, and how to make those assets do real product work instead of decorating it. |
| [[../duo-naming-and-notation/SKILL]] | 13 | How to name things, design symbols and write reference material so people can derive the answer instead of memorizing it — and how to handle the near-misses, overloaded tokens and silent misreadings that generate confident wrong behaviour. |
| [[../duo-design/SKILL]] | 17 | How an interface decision gets made and what the result claims about the person using it. Craft routes out to design-engineering. |
| [[../duo-inclusive-access/SKILL]] | 11 | How to stop your product from filtering on circumstance — removing preconditions, building escape hatches at the level of the blocked capability, and making sure you are not scoring people on things you never meant to measure. |

### Deciding and measuring

What to build, what number to chase, how to know it moved.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-product/SKILL]] | 17 | The rules a product org writes down and then has to hold when schedule and metric pressure arrive. |
| [[../duo-metric-design/SKILL]] | 7 | How to choose, weight and defend the single number a team is graded on, so that moving it means users actually got value rather than just spent time. |
| [[../duo-score-credibility/SKILL]] | 7 | How to design a score, rating or level that you show to users and outsiders so it resists gaming, means something beyond your product, and survives scrutiny from people with an incentive to attack it. |
| [[../duo-adoption-design/SKILL]] | 12 | How to get a shipped feature actually used — lowering the cost of starting, giving one obvious next step, and designing for the moment the user stalls, is embarrassed, is in the wrong place, or gets it wrong. |
| [[../duo-freemium-monetization/SKILL]] | 13 | Where to draw the paid line when the free tier is your distribution engine — what to charge for, what to never charge for, and when the upsell costs more than it earns. |
| [[../duo-category-entry/SKILL]] | 10 | How to pick and enter a new market or add a second product line — where to attack an incumbent, what to port from the thing that already works, and what to rebuild from a blank page. |
| [[../duo-growth-model/SKILL]] | 8 | Decide what to measure and which single lever to staff when your top-line engagement number has gone flat — and how to read demand that arrives from outside your product. |
| [[../duo-experimentation/SKILL]] | 18 | Establishing that your change caused the effect — hypothesis, metric, guardrails, and when to kill it. |
| [[../duo-experiment-velocity/SKILL]] | 6 | How to drive the marginal cost of an experiment toward zero — shared platform, self-serve tooling, standard readouts — so a team runs hundreds of tests a quarter instead of three. |

### Reaching people

Distribution, markets, and earning attention with what you already know.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-growth/SKILL]] | 17 | Distribution other people perform for you — the friend graph, the shareable artifact, earned attention. |
| [[../duo-localization/SKILL]] | 8 | Ship your product to people who do not share your language, script, reading direction, demographics, narrative conventions or fluency with software — and decide which markets that opens. |
| [[../duo-proprietary-data-reports/SKILL]] | 8 | Turn the behavioural logs you already hold into a recurring public report with a fixed window and published exclusions, so journalists, researchers and buyers cite it instead of discounting it. |
| [[../duo-timely-data-publishing/SKILL]] | 7 | Ship one finding fast — a spike, a commissioned survey, a score — so it gets picked up, and build in the baselines, hedges and caveats that stop a sceptical reader from dismissing it. |
| [[../duo-motivation-segmentation/SKILL]] | 7 | Ask users to declare why they are here, treat that answer as a first-class dimension alongside behaviour, and learn where self-report and telemetry each lie to you. |
| [[../duo-measurement-validity/SKILL]] | 10 | Design and report a number that survives an outsider's scrutiny: prove the outcome on an instrument you did not build, ship a breakdown only when it adds information, audit the instrument for bias, and disclose where your own hand touched the evidence. |
| [[../duo-expert-content-engine/SKILL]] | 9 | Run your in-house expertise as a standing, credentialed publishing program fed by the questions users already send you — and earn the reader's trust by marking, in public, where your evidence stops. |

### Building it

The systems under the product.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-backend-architecture/SKILL]] | 11 | How to make a server request fast and hard to break — what to delete from the request path, what to precompute versus inject, how long to hold a lock, and how to move a live system to a new runtime without stopping it. |
| [[../duo-mobile-engineering/SKILL]] | 13 | How to make a shipped client app start fast, stay small and remain cheap to change — startup budgets tied to conversion, perceived latency, payload discipline, and the mechanics of migrating a large codebase without freezing the product. |
| [[../duo-production-reliability/SKILL]] | 14 | How to know what production is actually doing and what to run when it breaks — always-on request identity, runtime dead-code detection, dogfooding and bug intake, incident command, kill switches that fail open, and repairing state users earned. |
| [[../duo-infra-cost-efficiency/SKILL]] | 7 | How to see, attribute and cut infrastructure spend without slowing the company down — hourly cost tagging, waste versus spend, sampling, provisioning headroom, and storage that expires by default. |
| [[../duo-ml-in-production/SKILL]] | 12 | How to decide where a learned model beats hand-written rules, what to evaluate it on, and how to run a generation pipeline that does not quietly produce errors at scale. |
| [[../duo-ai-agent-platform/SKILL]] | 10 | How to run LLM agents as production infrastructure rather than demos — separating what an agent is from how it runs, durable retryable steps, grading artifacts instead of prose, give-up rules for automated producers, and getting the capability adopted internally. |
| [[../duo-llm-feature-engineering/SKILL]] | 10 | How to build an LLM or agent feature that still works on the ten-thousandth call: prompt structure, task decomposition, grounding, memory, verification, evals, and the guardrails that keep a model's mistakes cheap. |
| [[../duo-ai-product-strategy/SKILL]] | 8 | Where to point AI so it changes your cost structure instead of adding a feature — which bottleneck to attack, how to divide labor between your experts and your models, when to adopt, and how to make an AI-driven product trustworthy enough to buy. |

### The team

How the people who build it work.

| Skill | Nodes | Owns |
|---|---|---|
| [[../duo-culture/SKILL]] | 18 | How the team runs — operating principles, talent density, candor, hiring signal, and ramping new people. |

### Out of this pack

UI craft — easing, contrast, tokens, component behaviour — is owned by the external
[design-engineering](https://github.com/AgentsORG/design-engineering) skill. See [[design-handoff]].

## Apply to your product

- If your own docs had to be grouped by the problem the reader arrives with rather than by team, what would the groups be?
- Which two of your groups would a newcomer confuse — and what one question separates them?

## See also

[[overlaps]] · [[chains]] · [[translate]] · [[sources]] · [[design-handoff]]
