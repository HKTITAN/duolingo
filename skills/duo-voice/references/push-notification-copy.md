---
name: duo-voice-push-notification-copy
summary: The highest-leverage copy surface; rules for notifications that get tapped instead of muted.
metadata:
  internal: true
---

# Push Notification Copy

## Concept

A push notification is a copy artifact with one job: get the user back into the product *without* burning the right to send the next one. The copy is the entire interface — there's no UI to compensate for a flat line, and there's an unsubscribe one tap away.

This is the highest-leverage copy surface in the whole product, and the most under-invested one in most companies.

## What Duolingo does

Source: blog.duolingo.com/hi-its-duo-the-ai-behind-the-meme (Duolingo blog, 2020-09-03; accessed 2026-09-22) · blog.duolingo.com/product-principles (Duolingo blog, 2024-02-21; accessed 2026-09-22)

The copy is hand-written; the *selection* is a machine. Duolingo keeps a pool of pre-written notification templates and, since 2019, picks one per learner per day with a bandit algorithm trained on **~200 million practice reminders collected over 34 days**. Four findings from that system are the real content of this node:

- **Template quality varies enormously, and it varies by language.** "Time for [language]" is one of the best options for Chinese learners and usually a poor one for English learners. The winner is per-audience, not global.
- **Scoring had to be de-biased.** Some templates only fire for learners with a streak wager, or only on Mondays — audiences that would have completed a lesson regardless. Each template is scored only against other templates sent to the same type of learner.
- **Novelty decays, and they measured it.** A notification a learner has never seen is unusually persuasive, and repetition kills that. Because a conventional bandit converges on one winner and reuses it, they had to explicitly demote recently-seen reminders — spacing repeats using the same **forgetting curve** they use to schedule vocabulary review.
- **Volume is deliberately capped.** Their VP of Product names the tempting alternative and rejects it: a growth team "could get quick wins by increasing our daily active users" by sending a lot of push notifications. "That's why we invest heavily in the daily streak and don't send tons of push notifications to our users every day."

Personalization is on substance — streak, language studied, what the learner did or didn't do — not `{firstName}` insertion.

## The transferable pattern

A useful frame for any notification:

| Element | Rule |
|---|---|
| Speaker | Which character or persona is sending this? |
| Tone | Is this earnest, playful, or unhinged? Match to the user's last interaction. |
| Reason | Why is this notification firing *now*? If you can't answer, don't send it. |
| Tap target | What do they land on? Generic home screens are wasted notifications. |

Three anti-patterns:

1. **Generic re-engagement.** "We miss you!" — sender, register, reason all unspecified. Mute rate spikes.
2. **`{firstName}`-only personalization.** Trivially detectable; doesn't make the line less generic.
3. **Notifications written by the team that ships features, not the team that owns voice.** Predictable result.

## Apply to your product

- Read your last five notifications. Could any of them have been sent by a competitor without changing a word?
- Which of your notifications has the highest mute rate? Why?
- Is one person responsible for notification voice, or is it a shared problem (which means: nobody's problem)?

## See also

[[threat-copy]] · [[wholesome-unhinged]] · [[character-archetypes]] · [[../duo-retention/references/notification-discipline]]
