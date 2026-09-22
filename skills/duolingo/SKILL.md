---
name: duolingo
description: Router over the Duolingo skill pack — 44 skills distilled from 750 posts on blog.duolingo.com plus the Duolingo Handbook. Ask it which skill fits the problem in front of you and in what order to run them. Use when you don't know which skill covers a question, when two seem to overlap, when a job spans several (a new feature, a retention fix, a launch, a curriculum, a rebuild), or when you want the Duolingo take on a product, habit, learning, growth, brand, engineering, or team problem. Design and UI craft routes out to the design-engineering skill. Triggers on, even without the word "duolingo", phrases like which skill, what would duolingo do, streak, habit loop, gamification, XP, leaderboard, churn, day-N drop-off, push notification, A/B test, spaced repetition, forgetting curve, adaptive difficulty, curriculum, onboarding, viral loop, earned media, annual data report, metric design, freemium, LLM feature, agent platform, mobile app size, observability, hiring bar, team culture.
license: MIT
compatibility: Agent-agnostic. Plain Markdown, no scripts and no network — every skill is self-contained, so it keeps working if blog.duolingo.com changes. Design routing targets the optional AgentsORG/design-engineering plugin and degrades gracefully when it is absent.
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
  router: true
---

# /duolingo

44 skills. You don't remember which one covers what, so ask here first.

Answer with **one or two skills, never five**. Name them, say in one line why, then run them. Loading four at once spreads attention across four playbooks and applies none of them.

**Match the requested outcome, not a word mentioned in passing.** "Our streak feature crashes on Android" is a mobile-engineering question that happens to contain the word *streak*. Route on what the user wants to end up with.

## Gate — check these first, in order

First match wins. If one fires, take it and stop.

| # | If… | Then |
|---|---|---|
| 1 | The question is about **UI craft** — visual design, motion, easing, layout, type, colour, component behaviour | Hand off per [[references/design-handoff]]. This pack does not own pixel craft. |
| 2 | The user **named a skill** ("use duo-streak-mechanics") | Go straight there. Don't re-route a decision already made. |
| 3 | The user wants **the catalogue** ("what's in this pack") | [[references/map]], then stop. Don't start solving. |
| 4 | It's **Duolingo trivia**, not a pattern to borrow | Answer normally; say no skill applies. This pack teaches transfer, not facts about Duolingo. |
| 5 | The job spans **three or more skills** (a launch, a feature end-to-end, a curriculum, a rebuild) | [[references/chains]] for the ordering, then run it. |

## Route in two questions

### 1. What posture is the user in?

This decides what the answer should *look like*. Misrouting on posture is the most common failure: someone still deciding gets handed an implementation, or someone asking for a build gets a lecture on tradeoffs.

| Posture | They're saying | What you hand back |
|---|---|---|
| **Diagnose** | "users drop at day 3", "engagement is falling and I don't know why" | The mechanism first, the fix second. Never lead with a feature. |
| **Build** | "design a streak", "write the push copy", "structure this curriculum" | The thing, built, using the skill's actual values. |
| **Decide** | "should we add leagues?", "is gamification right for a B2B tool?" | A call, with the trade named. Often the answer is no. |
| **Critique** | "review my onboarding", "is this loop healthy?" | Findings. Don't rewrite their product unless asked. |
| **Explain** | "what is half-life regression?" | The concept, then the transfer, then stop. |

### 2. Which family, then which skill?

Find the family, then pick the row. Full one-line index of all 44: [[references/map]].

**They stop coming back** — habit, streaks, churn, re-entry

| The user says… | Route to |
|---|---|
| "why do people leave", "day-3 drop-off", "what's our retention shape" | [[../duo-retention/SKILL]] |
| "should the streak break on one missed day", "will freezes get abused" | [[../duo-streak-mechanics/SKILL]] |
| "when do we ask for push permission", "how do we win back a lapsed user", "the widget gets no taps" | [[../duo-return-triggers/SKILL]] |
| "they say they aren't making progress", "level band or a number" | [[../duo-perceived-progress/SKILL]] |
| "which segment actually retains", "our keenest signups churn fastest" | [[../duo-motivation-and-attachment/SKILL]] |

**They're here but flat** — reward, play, willingness to try

| The user says… | Route to |
|---|---|
| "add XP", "leaderboard", "it feels like a grind", "celebrate the win" | [[../duo-gamification/SKILL]] |
| "they won't attempt it", "fear of looking stupid", "they quit after one failure" | [[../duo-learner-motivation/SKILL]] |

**The product has to teach them something** — the deepest, least-copied part of Duolingo

| The user says… | Route to |
|---|---|
| "they forget between sessions", "when should we resurface this", "review scheduling" | [[../duo-memory-and-decay/SKILL]] |
| "what order do we teach this in", "scaffolding", "curriculum structure" | [[../duo-progression-design/SKILL]] |
| "should we explain the rule or let them figure it out", "docs vs practice" | [[../duo-rules-and-heuristics/SKILL]] |
| "how hard should the next thing be", "adaptive difficulty", "what error rate is right" | [[../duo-difficulty-calibration/SKILL]] |
| "our users already know a similar tool", "why is this group faster" | [[../duo-prior-knowledge-transfer/SKILL]] |
| "the screen asks too much at once", "cognitive load" | [[../duo-attention-budget/SKILL]] |
| "does our product actually work", "prove the learning outcome" | [[../duo-efficacy-measurement/SKILL]] |

**The words and the face** — voice, characters, naming, interface rationale

| The user says… | Route to |
|---|---|
| "write the push copy", "our errors are cold", "brand voice drifts between writers" | [[../duo-voice/SKILL]] |
| "build a mascot", "a cast that stays consistent", "character reactions" | [[../duo-character-systems/SKILL]] |
| "what do we call this", "our labels confuse people", "symbol and notation design" | [[../duo-naming-and-notation/SKILL]] |
| "why does this screen feel flat", "what does our UI claim about the user" | [[../duo-design/SKILL]] |
| "users without good hardware/bandwidth/credentials can't get in" | [[../duo-inclusive-access/SKILL]] |

**Deciding and measuring** — what to build, what number to chase, how to know

| The user says… | Route to |
|---|---|
| "what do we build next", "how do we prioritize", "quality bar" | [[../duo-product/SKILL]] |
| "are we optimizing the right number", "our metric is getting gamed" | [[../duo-metric-design/SKILL]] |
| "our score/rating needs to resist gaming and convince outsiders" | [[../duo-score-credibility/SKILL]] |
| "we shipped it and nobody uses it" | [[../duo-adoption-design/SKILL]] |
| "where do we draw the paid line", "free tier vs subscription" | [[../duo-freemium-monetization/SKILL]] |
| "should we enter this market", "a second product line" | [[../duo-category-entry/SKILL]] |
| "our top-line number stopped moving", "which lever do we staff" | [[../duo-growth-model/SKILL]] |
| "how do I A/B test this", "the result looks fake", "when do we kill it" | [[../duo-experimentation/SKILL]] |
| "we only ship three tests a quarter", "build or buy an experiment platform" | [[../duo-experiment-velocity/SKILL]] |

**Reaching people** — distribution, markets, and earning attention with what you know

| The user says… | Route to |
|---|---|
| "grow without paid", "referral", "make it spread", "launch stunt" | [[../duo-growth/SKILL]] |
| "ship to a market that doesn't share our language or script" | [[../duo-localization/SKILL]] |
| "turn our usage data into an annual report", "methodology people trust" | [[../duo-proprietary-data-reports/SKILL]] |
| "we spotted a spike — is that worth publishing", "one finding, fast" | [[../duo-timely-data-publishing/SKILL]] |
| "ask users why they're here and segment on it" | [[../duo-motivation-segmentation/SKILL]] |
| "will this number survive outside scrutiny", "is our instrument valid" | [[../duo-measurement-validity/SKILL]] |
| "turn our in-house experts into a publishing program" | [[../duo-expert-content-engine/SKILL]] |

**Building it** — the systems under the product

| The user says… | Route to |
|---|---|
| "make the request path fast", "what do we delete from the hot path" | [[../duo-backend-architecture/SKILL]] |
| "app startup is slow", "binary size", "the client rewrite" | [[../duo-mobile-engineering/SKILL]] |
| "what is production actually doing", "tracing", "incident response" | [[../duo-production-reliability/SKILL]] |
| "our infra bill", "cost attribution without slowing everyone down" | [[../duo-infra-cost-efficiency/SKILL]] |
| "model or rules", "what do we evaluate it on", "ship the model" | [[../duo-ml-in-production/SKILL]] |
| "run agents as infrastructure", "agent registry", "swap the runtime" | [[../duo-ai-agent-platform/SKILL]] |
| "the AI demo breaks in production", "prompt structure", "eval the output" | [[../duo-llm-feature-engineering/SKILL]] |
| "where should we point AI", "build on it now or wait" | [[../duo-ai-product-strategy/SKILL]] |

**The team**

| The user says… | Route to |
|---|---|
| "how do we run the team", "hiring bar", "too many meetings", "who owns this", "write values people use" | [[../duo-culture/SKILL]] |

**No row matched?** Say so. Check [[references/map]]. If it still doesn't fit, answer normally and say no skill applies.

## Before you answer

1. **[[references/translate]] is mandatory.** The user is almost never building Duolingo. A node that describes what Duolingo did and stops has failed. Every answer ends in *their* product.
2. **Cite the node you used** — `skills/duo-streak-mechanics/references/<node>.md` — so they can read it and disagree.

## When two skills both look right

Don't read both. [[references/overlaps]] holds the confusable pairs and the one question that settles each. The sharpest ones:

- **retention vs streak-mechanics** — diagnosing the churn, or designing the chain itself?
- **memory-and-decay vs difficulty-calibration** — *when* to bring it back, or *how hard* to make it?
- **progression-design vs rules-and-heuristics** — where a thing sits in the path, or whether it gets stated at all?
- **llm-feature-engineering vs ai-product-strategy** — making a model you've committed to behave, or deciding whether to use one at all?
- **experiment-velocity vs experimentation** — can't afford enough results, or don't believe the one you have?
- **retention vs learner-motivation** — not returning, or returning and refusing to try?

**Before any habit-family route, check frequency.** A product genuinely used twice a month does not have a retention problem, and a daily loop will only manufacture guilt. Say so rather than building one.

## What this pack does not cover

Product, habit, learning, voice, growth, measurement, team, and the engineering and AI decisions behind them. **Not**: pixel-level UI craft ([[references/design-handoff]]), backend implementation detail beyond the patterns, legal, finance, or hiring logistics. Stretching a skill over a database schema question produces confident nonsense the user can't distinguish from a real answer. Say no skill applies.

## Provenance

Every skill is **self-contained** — the numbers, mechanisms and tradeoffs are in the nodes, not behind a link, because sources rot. Citations are stamped with the date they were true. [[references/sources]] records what was read, what was left out, and where Duolingo has since changed course.
