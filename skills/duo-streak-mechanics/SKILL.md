---
name: duo-streak-mechanics
description: Design an unbroken-chain commitment counter — how low to set the daily bar, how much slack to build in, when to let it pause, and what it will quietly certify that you never intended. Covers decoupling the trivial daily bar from the user's ambitious target, finding the activation threshold where return probability jumps, scarce recovery tokens, sanctioned pauses timed at your own usage dip, voluntary stakes with a dated payoff, two-sided shared chains, and the token-action failure where the engagement chart climbs while outcomes stall. Use when adding or repairing streaks, daily goals, habit counters or consecutive-period mechanics, and for questions like should the streak break on one missed day, will freezes get abused, how high should the daily goal be, or why is our streak number rising while results stay flat.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Streak Mechanics

A streak is a commitment device. It works by accumulating something the user does not want to lose, then putting it at risk every day. That makes it the most powerful retention mechanic most products can ship — and the easiest one to point at the wrong behaviour.

Seven decisions determine whether yours helps or hurts. How low the bar sits, what number you are aiming users at, what happens on a miss, what happens on a structural gap, whether users can raise their own stakes, what the cheapest qualifying action is, and what the counter actually certifies.

This skill covers the chain itself — the reason to care about continuity. It does not cover **delivering the cue** that gets someone to open the product on a given day (reminders, widgets, permission prompts, win-back flows), and it does not cover progress meters that **move rather than break**.

## Setting the bar

- [[references/fixed-low-bar-separate-ambition-dial]] — decouple the chain's trivial bar from the user's self-chosen target; the most ambitious tier is a churn signal, not a commitment signal.
- [[references/activation-threshold-as-one-shared-target]] — find the tenure number past which return probability jumps, publish it internally, and aim every early-lifecycle surface at that one number.
- [[references/trivial-floor-protects-the-chain-not-the-outcome]] — a minimum viable day under two minutes, an alternate low-effort format, and one counter fed by every product line.

## Building in slack

- [[references/scarce-recovery-token]] — a finite, countable, auto-applying allowance that absorbs a miss while keeping loss aversion and scarcity intact.
- [[references/scheduled-pause-at-the-known-dip]] — find the trough already visible in your usage data and ship a sanctioned pause aimed at it; plus an operational suspend for groups who cannot comply.

## Raising the stakes

- [[references/voluntary-stake-with-a-dated-payoff]] — let users risk something they already earned on their own promise, and date the payoff exactly at the retention horizon you care about; the paired version and its opt-out.

## What it is really measuring

- [[references/the-chain-will-certify-a-token-action]] — any habit metric satisfiable by a token action will be satisfied that way; track continuity and outcome as two numbers and say so in your copy.

## How to use this skill

1. Start with the bar. Most broken streak designs are ambition targets wearing a chain's clothing.
2. Then pick the threshold you are driving toward, so every surface aims at one number.
3. Then design the slack — token for random bad days, pause for structural gaps. They are different instruments.
4. Only then add stakes, sharing or leaderboards, and ship the opt-out in the same release.
5. Before launch, write down the laziest way to satisfy the counter and the outcome metric it will not move.

## Sibling skills

- [[../duo-retention/SKILL]] — the wider retention system the chain sits inside, including the freeze, loss aversion and churn diagnostics.
- [[../duo-gamification/SKILL]] — XP, leagues, power-ups and self-imposed stakes; the reward economy a streak spends and earns.
- [[../duo-experimentation/SKILL]] — how to test a core mechanic change without fooling yourself, and which guardrails to keep on it.
- [[../duo-learner-motivation/SKILL]] — why users pick goals they cannot keep, and how to frame a stretch target as a stretch.

## Sources

Every node cites blog.duolingo.com posts in the dated form; the primary ones here are `improving-the-streak` (2020-11-19), `how-duolingo-streak-builds-habit` (2022-01-31), `how-streaks-keep-duolingo-learners-committed-to-their-language-goals` (2017-05-10), `friend-streak` (2024-08-05), `product-lessons-friend-streak` (2024-09-20), `tips-for-maintaining-streak` (2022-12-19), `time-spent-learning-well` (2024-06-13) and `why-are-conversations-in-other-languages-so-hard` (2024-09-03), all accessed 2026-09-22.
