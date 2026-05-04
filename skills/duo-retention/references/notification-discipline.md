---
name: duo-retention-notification-discipline
summary: Push notifications are the single highest-leverage retention surface and the easiest one to ruin; cadence and content discipline matter more than cleverness.
metadata:
  internal: true
---

# Notification Discipline

## Concept

A push notification is the only product surface that reaches the user when the product is closed. That makes it the highest-leverage retention tool and the easiest one to abuse. The discipline is restraint: most retention damage from notifications comes from sending too many bland ones, not from sending too few.

## What Duolingo does

- Notifications are tightly capped per day; the system tunes timing per user based on past response.
- Each notification is a [[../duo-voice/references/push-notification-copy]] artifact, not a templated string. The voice is part of why users tolerate the cadence.
- Notification rights can be lost: ignored or muted notifications are de-prioritized, not retried at higher volume.
- The handbook explicitly cites notification limits as an example of *Take the Long View* — short-term opens vs. long-term unsubscribes.

## The transferable pattern

Three rules:

1. **Every notification has an unsubscribe cost.** Estimate it explicitly. A notification that lifts open rate by 0.5% but raises unsubscribe rate by 0.2% is usually a long-term loss; the unsubscribed user costs you forever.
2. **Personalize timing before content.** Sending the right user the right thing at 9am vs 9pm matters more than the wording. Most teams flip this.
3. **A notification with no character is a generic tax.** If the user can't tell which app sent it without checking, you've trained them to ignore your icon.

Anti-pattern: re-engagement campaigns that fire when a user has already churned. They don't return that user — they confirm the unsubscribe.

## Apply to your product

- How many notifications does an active user receive per day? Per week? Could you halve it without losing retention?
- Are your notifications written by a person or generated from templates?
- What's your unsubscribe rate, and have you tied it to your notification volume?

## See also

[[habit-loop]] · [[churn-diagnostics]] · [[../duo-voice/references/push-notification-copy]] · [[../duo-voice/references/threat-copy]] · [[forever-product]]
