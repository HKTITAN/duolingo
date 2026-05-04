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

- Error screens feature characters with on-brand poses (Duo confused, Lily unimpressed) instead of stock 404 illustrations.
- Each error has voice-driven copy ([[../duo-voice/references/error-copy]]) — no corporate apology defaults.
- The visual treatment is calibrated to the severity: a wrong answer is gentle and almost playful; a server outage is more serious but still on-brand.
- Recovery actions are visible and clear: "Try again" / "Refresh" / "Continue" — never just an apology with no next step.

## The transferable pattern

Three rules:

1. **No generic error screens.** Every error state has a character (or brand element), voice copy, and a clear next action.
2. **Match treatment to severity.** A typo isn't an apocalypse; an account suspension isn't a joke. The visual register matches the user's emotional state.
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
