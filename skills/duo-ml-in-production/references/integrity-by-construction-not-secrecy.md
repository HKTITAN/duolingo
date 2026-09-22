---
name: duo-ml-in-production-integrity-by-construction-not-secrecy
summary: Generate a large item bank and sample from it in real time — when no two instances are identical, leaked answers are worthless.
metadata:
  internal: true
---

# Integrity by Construction, Not Secrecy

## Concept

Secrecy-based integrity has one failure mode and it is catastrophic and silent: the moment a single copy escapes, every deployment of that artifact is compromised, and you find out long after the damage. Worse, the defence costs you something continuously — distribution controls, embargoes, supervision — while the attack costs one leak, once.

Construction-based integrity removes the artifact worth stealing. If every instance is assembled at request time from a large generated pool, there is no single thing to leak. A leak of one instance degrades nothing, because no one else will ever see that instance. The property you want is not "hard to obtain in advance" but "worthless to obtain in advance."

## What Duolingo does

Source: blog.duolingo.com/is-the-duolingo-english-test-hard (Duolingo blog, 2021-06-14; accessed 2026-09-22)

- Duolingo English Test items are generated with **human-in-the-loop AI trained on expert-labelled words and texts**, producing a bank of **tens of thousands of items**.
- The labelling is against the **CEFR six-level scale, A1 through C2**, so every generated item carries a difficulty label from the moment it exists — which is what makes sampling meaningful rather than random.
- Item selection is **real-time and adaptive**, drawing from that bank per session, which is why Duolingo can state that **"it's impossible to get answers to the test in advance."**
- Note the pairing: the generator produces volume, and the human-in-the-loop labelling produces the metadata without which the bank would be a pile rather than a pool. Volume alone does not give you integrity; volume plus reliable per-item difficulty does.

## The transferable pattern

This applies to anything where a user has an incentive to obtain the artifact before they encounter it — assessments, verification challenges, screening exercises, fraud checks, interview tasks.

The construction has three parts:

1. **A generator that produces far more instances than you will ever serve to one person.** The bank must be large enough that repetition across users is rare, not just large enough to cover one cycle.
2. **A reliable label per instance.** Difficulty, category, or whatever dimension you select on. Without it you cannot sample fairly, and two users get incomparable experiences — which is a worse integrity failure than a leak, because it is invisible and permanent.
3. **Selection at request time.** If instances are assigned in advance, the assignment is the thing to steal and you are back to secrecy.

The honest costs: generated banks need the audit tooling of any generation pipeline, because a defective item that slips through is now unfairly affecting a real decision about a real person. Per-item labels need periodic recalibration against observed outcomes, since a label assigned at authoring time drifts. And the bank has to keep growing, because a static one eventually becomes memorizable in aggregate even if no single instance is.

This is also the reason to prefer it. Secrecy fails all at once and without warning; a generated bank degrades gradually and visibly in your own metrics, which is a failure mode you can actually manage.

## Apply to your product

- What artifact in your product is protected only by not being public yet, and what happens the day one copy leaks?
- Could that artifact be generated from parameters instead of authored, and do you have the per-instance metadata you would need to select fairly?
- If two users received different instances, could you defend the claim that they were equivalent — with data, not with an assertion?

## See also

[[pair-every-generator-with-an-inspector]] · [[generate-from-one-parameterized-primitive]] · [[../duo-difficulty-calibration/references/model-the-item-and-the-user-jointly]]
