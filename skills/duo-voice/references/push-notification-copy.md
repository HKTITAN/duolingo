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

- Notifications are character-driven; they read like a person, not a system.
- Threat copy ([[threat-copy]]) is the most famous variant — exaggerated, in-joke, comically specific.
- Tone is varied: not every notification is unhinged. A user who had a great session yesterday gets an earnest follow-up; a user who's been gone a week gets a different register.
- Personalization is on substance, not just `{firstName}` insertion. The notification references what the user actually did or didn't do.

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
