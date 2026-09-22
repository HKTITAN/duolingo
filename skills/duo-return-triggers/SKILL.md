---
name: duo-return-triggers
description: How to cause the next session to start — where the reminder lives, when you have earned the right to ask for notification permission, what an ambient widget or lock-screen surface should show, how to attach a new behaviour to a cue the user already fires, how large your lapsed cohort really is, and what a returning user should see first. Use this when someone says our opt-in rate is terrible, where should the reminder go, users install and never come back, build a win-back flow, reactivation campaign, how do I measure resurrected users, should we ship a widget, people quit halfway through, our push notifications get ignored, how do we get them back without nagging, or what do we show a user who has been gone two months.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Return Triggers

Retention systems are usually judged by what happens inside a session. This skill is about the part before that — the cue, the surface, the permission ask, and the path back in for someone who already stopped.

The distinction that organises everything here: **arrival and caring are different problems.** A streak makes someone care once they are in front of you; it does not put them in front of you. A notification budget buys arrivals but is finite and decays. Cues, ambient surfaces, open loops and bounded calendars generate arrivals without spending that budget. And a returning user is a third cohort — not new, not active — that almost every product serves the wrong screen.

## Cues and surfaces

- [[references/piggyback-an-existing-high-frequency-trigger]] — the scarce resource is the trigger, not the motivation; relocate your entry point into a slot they already touch.
- [[references/bind-the-cue-to-a-person-place-or-time]] — bind recurrence to something external and stable, never to the user's intention.
- [[references/one-signal-ambient-surface]] — a glance outside your app is sub-second; carry exactly one state-of-risk variable.
- [[references/friction-is-symmetric]] — making the competing behaviour harder works as well as making yours easier, and usually costs less.

## Asking to interrupt

- [[references/ask-for-permission-at-an-earned-peak]] — move the opt-in off first launch onto a win or a loss, and test placement, pitch and context separately.
- [[references/process-framing-beats-outcome-framing]] — name the behaviour to build, not the prize; process framing survives a bad day.

## Returns you do not have to buy

- [[references/the-open-loop-returns-users-without-a-push]] — an unresolved loop supplies its own reason to come back, at no notification cost.
- [[references/bounded-windows-create-a-return-date]] — permanent availability flattens attention; a window with hard edges can be anticipated and missed.

## The lapsed cohort

- [[references/resurrected-users-are-their-own-cohort]] — define it, size it, and measure its retention separately, because it is worse than new-user retention.
- [[references/re-entry-resumes-it-does-not-restart]] — they retain more than either of you thinks; resume from the stored state and open with something easy, never a test.
- [[references/new-content-beats-a-guilt-nudge]] — a changed offer reactivates better than a reminder that they left.
- [[references/answer-the-exit-not-the-dialog]] — at the moment of abandonment, address why they are going rather than confirming that they are.

## Boundary

This skill owns what makes the user arrive. It does not own the rules of the chain once they are here — bar height, freezes, pauses and reset behaviour live in [[../duo-retention/SKILL]]. It also does not own why a segment wanted the thing in the first place; that is upstream of every trigger here.

## Sibling skills

- [[../duo-retention/SKILL]] — the streak, the habit loop, churn diagnostics, notification discipline.
- [[../duo-voice/SKILL]] — the wording of the nudge, the push, and the prompt itself.
- [[../duo-experimentation/SKILL]] — how to run the placement, pitch and copy tests this skill keeps asking for.
- [[../duo-gamification/SKILL]] — deadlines, leagues and the reward structures a returning user walks back into.

## Sources

All claims cite blog.duolingo.com posts by slug and publication date inside each node's `## What Duolingo does` section; every slug is checked against `scripts/sources.json` in CI.
