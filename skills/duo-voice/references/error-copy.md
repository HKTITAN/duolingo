---
name: duo-voice-error-copy
summary: Wrong answers, network failures, validation errors as moments of brand instead of friction.
metadata:
  internal: true
---

# Error Copy

## Concept

An error is the moment a user expected one thing and got another. The default response is corporate apology ("Something went wrong. Please try again."). The opportunity is exactly here — error copy is read carefully (the user is paying attention; something just broke) and rarely written carefully. The asymmetry is enormous.

## What Duolingo does

- Wrong-answer copy is gentle, not punitive: it shows the right answer, lightly explains, lets the user retry.
- A wrong-answer animation is its own juicy moment ([[../duo-gamification/references/juicy-feedback]]) — feedback, not failure.
- Network/server errors are character-styled: a Duo "this is awkward" image instead of a generic toast.
- Long-form errors (account locked, payment failed) are written in the same voice as the rest of the product, not handed off to a legal-toned default.

## The transferable pattern

Five rules:

1. **No corporate apology defaults.** "Something went wrong" is brand abdication. Write the line.
2. **Tell the user what to do next.** An error without a next step is a dead end.
3. **Match register to severity.** Validation typo = playful. Account suspended = serious. Don't be unhinged about the wrong things.
4. **Match register to the user's emotional state.** A failed payment is not the moment for a joke.
5. **Errors get the same review as marketing copy.** Because users read them more carefully.

Anti-pattern: shipping every error string the engineer typed first.

## Apply to your product

- Read your top five most-frequent error messages. Could any of them be sent by any product?
- Does each error tell the user what to do next?
- When an error string was last edited — by whom, and was it reviewed for voice?

## See also

[[wholesome-unhinged]] · [[push-notification-copy]] · [[empty-states]] · [[../duo-design/references/error-as-delight]]
