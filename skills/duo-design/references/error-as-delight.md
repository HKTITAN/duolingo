---
name: duo-design-error-as-delight
summary: An error state is a free chance to be the brand instead of break it.
metadata:
  internal: true
---

# Error as Delight

## Concept

Most error states are the most generic surface in a product — a default toast, a stock illustration, a corporate apology. They're also some of the most-read screens, because the user is paying close attention (something just broke). The asymmetry is the whole opportunity: invest minimally and the brand pays a tax; invest a little and the brand earns a moment.

This is the design implementation of [[../duo-voice/references/error-copy]].

## What Duolingo does

Source: blog.duolingo.com/adventures (Duolingo blog, 2024-09-24; accessed 2026-09-22)

- Duolingo Adventures uses what the team calls "immersive feedback": a character reacts to a wrong utterance by looking confused and saying something like "Oh, did you mean...?" rather than showing the standard correct/incorrect banner. The mistake is answered the way the world would answer it, not the way a grader would.
- Duolingo has moved the severity of a plain wrong answer *down* over time. Under Hearts, each mistake cost one heart and beginners were **2X more likely to run out mid-lesson** — which the team called "not the most effective way to support learning." Energy replaced it, and reviewing your mistakes at the end of a lesson now costs nothing (blog.duolingo.com/duolingo-energy (Duolingo blog, 2025-07-03; accessed 2026-09-22)).
- Recovery actions are named in the UI instead of implied: "Do this later," "Can't listen now," "Can't speak now" all keep the learner moving rather than leaving them on a dead end.
- **Where the correction threshold sits.** Duolingo's guide for people supporting a learner gives the rule as "let small mistakes go unless they cause confusion" — correct what blocks the goal, not what is merely wrong, because correction has a fixed interruption cost regardless of severity (blog.duolingo.com/how-to-support-a-language-learner (Duolingo blog, 2026-01-06; accessed 2026-09-22)).
- **Correct by recasting, not by flagging.** The same guide scripts the move directly: reflect the corrected form back inside the flow of the exchange instead of stopping to mark the error, because constant correction "can interrupt conversation and make learners anxious." *Tension:* a recast carries less explicit signal than a direct correction, so errors clear more slowly — Duolingo accepts that in exchange for sustained willingness to try.
- Error screens carry characters in on-brand poses and voice-driven copy ([[../duo-voice/references/error-copy]]) instead of stock 404 illustrations; the per-error art direction itself is Handbook material (handbook.duolingo.com).

## The transferable pattern

Three rules:

1. **No generic error screens.** Every error state has a character (or brand element), voice copy, and a clear next action.
2. **Match treatment to severity, and correct only what blocks the goal.** A typo isn't an apocalypse; an account suspension isn't a joke. The visual register matches the user's emotional state.
3. **Recovery comes first.** Even a beautifully-illustrated error is a failure if the user doesn't know what to do next.

Anti-patterns:
- A single "something went wrong" screen used for every error type.
- Errors that are funny but obscure the actual problem. (Cuteness is not a substitute for clarity.)
- Errors with no recovery action — dead ends are dead ends, no matter how charming.

## Apply to your product

- Inventory your top five error states. Are they generic or branded?
- For each, is there a clear next action?
- Is the register appropriate to the severity of each error?

## See also

[[../duo-voice/references/error-copy]] · [[character-system]] · [[../duo-product/references/polish]] · [[../duo-voice/references/empty-states]]
