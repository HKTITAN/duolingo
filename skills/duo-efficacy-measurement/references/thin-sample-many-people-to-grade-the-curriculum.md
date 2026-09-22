---
name: duo-efficacy-measurement-thin-sample-many-people-to-grade-the-curriculum
summary: A quiz too short to grade any individual is, at population scale, a precise map of what you teach badly.
metadata:
  internal: true
---

# Thin-Sample Many People to Grade the Curriculum

## Concept

Assessing one person needs enough items to beat that person's noise. Assessing one piece of content needs enough people to beat it — and you have far more people than you have patience-per-person. So flip the axis: ask each user a handful of questions drawn from a large pool, and aggregate across everyone. The result cannot grade anybody, and it does not need to. It grades what you built.

## What Duolingo does

Source: blog.duolingo.com/how-are-duolingo-courses-evolving (Duolingo blog, 2019-04-03; accessed 2026-09-22)

- The end-of-section quiz gives each learner **15 questions drawn from a large pool** — explicitly **not enough to assess any one person** — and aggregates across millions of learners to locate weak spots.
- The aggregate surfaced learners producing **"Yo gusto el chocolate"** instead of "Me gusta el chocolate". That single ranked error led directly to adding more practice for that structure. The quiz is therefore a content-generation pipeline, not a report card.
- The same logic runs publicly: Duolingo published the **top 5 mistakes** English learners make — third-person -s, present progressive -ing, placement of "not", adjective order, infinitive "to" after need/want/have — with the framing that focusing on the most common errors speeds up progress (blog.duolingo.com/most-common-english-mistakes (Duolingo blog, 2023-01-04; accessed 2026-09-22)).
- Scaled up, this is an org function rather than a one-off: a dedicated efficacy research team evaluates how well courses teach, and "when we find gaps, we create new features to address them." Weak listening outcomes produced **DuoRadio in 2023**, an in-app short-form podcast, because listening is the prerequisite for speaking (blog.duolingo.com/duolingo-company-strategy (Duolingo blog, 2025-04-07; accessed 2026-09-22)).

The tradeoff is that this design forecloses a user-facing score forever. A 15-item sample is statistically indefensible as an individual result, so the quiz can never double as a credential or a progress badge.

## The transferable pattern

Point your assessment at your content, not at your users, and the sample size problem inverts in your favour.

- **Thin per person, wide across people.** Each user answers a small random draw. The burden stays low enough that they do not avoid it, and the population still resolves every item in the pool.
- **Rank failures by frequency.** Users cannot see their own error distribution — every mistake feels idiosyncratic and equally weighted. You see it in aggregate. The top few items are the highest-leverage thing you can build or write, and they are handed to you rather than guessed.
- **Treat it as a feature pipeline, not a marketing asset.** Feature ideas sourced from requests and competitor parity are biased toward what users can articulate and what rivals already shipped. Outcome measurement surfaces the deficit nobody complained about because they could not name it.
- **Publishing the ranking is itself a feature.** Handing users a prioritized list of the mistakes they are already making gives them an ordering they had no way to construct.

## Apply to your product

- What would you ask if each user answered only a handful of questions, and the answer only had to be valid across your whole population?
- What is the top item in your error distribution right now, and when did anyone last build against it?
- Which of your last five features came from an outcome measurement rather than from a request or a competitor?

## See also

[[build-the-item-pool-independently-of-the-content]] · [[embed-a-pre-test-and-post-test-in-the-product]] · [[../duo-experimentation/references/metric-selection]]
