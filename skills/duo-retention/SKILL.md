---
name: duo-retention
description: Duolingo-style retention engineering for any product — habit loops, streaks, leagues, churn diagnostics, day-N drop-off, and the discipline of building a "forever product." Use when the user asks how to keep users coming back, debug churn, design a streak system, time push notifications, run a leaderboard, or shift a product's metric from acquisition to retention. Source the Duolingo Handbook (Take the Long View) and blog data posts; translate every pattern to the user's actual product.
license: MIT
metadata:
  author: HKTITAN
  version: "1.0.0"
  graph: true
---

# Duolingo Retention — Map of Content

Duolingo's central business bet is that retention compounds and acquisition does not. The handbook frames the company as a "forever product": every decision is judged by long-term retention, not short-term revenue. This skill packages that bet into reusable patterns.

This skill is structured as a **graph**: scan the descriptions below, follow only the `[[wikilinks]]` you need. Don't read every node up front.

## Foundations

- [[references/forever-product]] — the operating premise: optimize for users who stick around for years, not quarters.
- [[references/habit-loop]] — trigger → action → variable reward → investment, the spine of every retention move.
- [[references/retention-vs-revenue]] — the explicit tradeoff Duolingo makes (and limits) between monetization and long-term return.

## Behavioral mechanics

- [[references/streak-mechanics]] — the daily-counter habit engine that became the company's icon.
- [[references/streak-freeze]] — why protecting the streak is the retention move, not the gentle one.
- [[references/loss-aversion]] — the asymmetry that makes streaks work: losing hurts more than winning feels good.
- [[references/variable-reward]] — unpredictable payoffs (chests, league finishes) outperform predictable ones.
- [[references/friction-as-stickiness]] — small required actions that build identity and habit.

## Social and competitive layers

- [[references/leagues]] — weekly time-boxed competition with promotion and demotion.
- [[references/daily-quests]] — short-horizon goals that set up the long-horizon streak.

## Diagnosing and fixing churn

- [[references/churn-diagnostics]] — how to find the day where users drop and what each drop-off shape implies.
- [[references/notification-discipline]] — the long-term cost of over-notifying, and how Duolingo decides cadence.

## Sibling skills

- [[../duo-gamification/SKILL]] — the play layer (XP, juicy feedback, hearts) that makes the retention loops survivable.
- [[../duo-voice/SKILL]] — the copy layer that makes a push notification fire instead of fizzle.
- [[../duo-experimentation/SKILL]] — every retention claim in this skill was originally an A/B test; here's how to run yours.
- [[../duo-product/SKILL]] — the "forever product" mental model lives in the product skill too; the long-view bet starts there.

## Sources

- Duolingo Handbook (2025), Principle #1: *Take the Long View*
- blog.duolingo.com — streak society, league design, push-notification science posts
