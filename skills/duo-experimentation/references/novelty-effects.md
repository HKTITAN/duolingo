---
name: duo-experimentation-novelty-effects
summary: The lift that decays after week three; how to detect novelty and discount it before shipping.
metadata:
  internal: true
---

# Novelty Effects

## Concept

A novelty effect is a temporary engagement lift caused by *change itself* rather than the change being better. New UI, new feature, new copy — users notice, engage more for a few days, and then return to baseline. Tests run for a week look like wins; the same change measured at month two shows no lift.

Most teams ship novelty as if it were durable improvement and discover the truth too late.

## What Duolingo does

Duolingo's push-notification bandit is the clearest published case of *measuring* novelty rather than assuming it. Source: blog.duolingo.com/hi-its-duo-the-ai-behind-the-meme (Duolingo blog, 2020-09-03; accessed 2026-09-22)

- They **hypothesized** that a notification a learner had never seen would be unusually persuasive and that the effect would wear off — then **confirmed it in the data**, against the results of **~200 million practice reminders sent over a 34-day period** (the dataset is public on Harvard Dataverse; the method was published at KDD 2020).
- The fix is structural, not a warning in a doc: the bandit **demotes templates the learner has seen recently**, and the spacing between repeats is set by **the same forgetting curve Duolingo uses to model vocabulary decay**. The interval you'd wait before re-testing a word is roughly the interval to wait before reusing a message.
- This runs directly against how bandits are supposed to behave. A conventional bandit finds the best arm and exploits it repeatedly — which is precisely the behavior that destroys that arm. They had to teach their own optimizer to stop over-exploiting.

The reframe worth stealing: novelty decay is not a reason to distrust a result. It is a quantity you can estimate from your own logs and then schedule around.

## The transferable pattern

Three rules:

1. **Novelty-prone changes need longer tests.** UI / copy / new-feature changes especially. A one-week test is not enough.
2. **Plot the daily curve, not just the aggregate.** A flat lift means real change. A declining lift means novelty fading.
3. **Some changes deserve a second test after ship.** A few months later, re-test against an opposite holdout: does the change still beat the previous baseline?

Anti-pattern: shipping every win on a one-week test and being confused by flat retention three months later.

## Apply to your product

- Have you shipped changes that "won" tests but didn't move long-term metrics? How would you have detected novelty?
- For your next UI or copy test, plot the daily lift curve. Does it stay flat or fade?
- Do you have any system for catching decay after ship?

## See also

[[sample-size]] · [[hypothesis-design]] · [[ship-and-iterate]] · [[../duo-retention/references/forever-product]]
