---
name: duo-ai-product-strategy-adopt-early-gate-on-your-own-quality-bar
summary: Adopt a capability while it is still visibly bad if the trajectory is clear — but only against a quality bar you defined before the tool existed.
metadata:
  internal: true
---

# Adopt Early, Gate on Your Own Quality Bar

## Concept

Two rules that are wrong alone and right together.

**Adopt early.** The hard part of a new capability is never the model. It is the integration work, the internal muscle, the pipeline and the review process around it — all of which take years and none of which improve on someone else's budget. Teams that wait for quality start that build from zero at the moment the capability becomes table stakes, and they are years behind on the part that was never going to get cheaper.

**Gate on your own bar.** The brake is a definition of good that you committed to before the tool existed. Without it, adoption is driven by novelty and your product's definition of quality silently drifts to whatever the tool happens to produce well. With it, "the technology got better" becomes a claim you can test rather than a mood.

## What Duolingo does

Source: blog.duolingo.com/duolingo-company-strategy (Duolingo blog, 2025-04-07; accessed 2026-09-22)

- Duolingo embraced text-to-speech early, **despite its early robotic sound**, on the explicit assumption that the technology only gets better — then applied the same posture to content generation and to Video Call.
- What the accumulated pipeline was worth: **7,500 content units shipped in 2024, up from 425 in 2021** — roughly an 18x increase in annual output.
- The brake, from the assessment side of the house — the scientists on the Duolingo English Test are described as **"very mindful of the tools they choose to use,"** with technology required to serve the interest of putting out a test that is **valid, reliable and fair** with a good test-taker experience. That bar predates any particular tool, and it is applied by a team with every incentive to adopt, on a product that is already heavily AI-driven (blog.duolingo.com/antony-kunnan-interview (Duolingo blog, 2022-08-08; accessed 2026-09-22)).
- The bar in practice — Video Call ships in two scaffolding modes, guided scripted practice with Falstaff for beginners and open-ended conversation with Lily for intermediates, and each was validated separately. One Lily study followed Japanese speakers learning English at **Duolingo Score 60-71** who used Video Call **at least twice a day**, measured after **one month** against a standardized speaking test; a second ran with English speakers learning Spanish at **Score 45-55** (blog.duolingo.com/video-call-research-report (Duolingo blog, 2026-03-30; accessed 2026-09-22)).

**Tension.** The strategy post frames early adoption as costless in hindsight, but it counts only the bets that paid off. Nothing here is a general license — "adopt everything early" reads as free advice precisely because the failures are not in the sample.

## The transferable pattern

- Separate the two questions. *Is the capability good enough today?* is about the model. *Can we build the surrounding machine in time?* is about you — and the second question is the one with the multi-year answer.
- Adopt early where the trajectory is clear and the cost of being wrong is a visible, fixable quality gap. Do not adopt early where being wrong is silent, irreversible, or lands on a user who cannot tell.
- Write the quality bar down before evaluating tools, in terms a tool cannot satisfy by definition — what must be true of the output regardless of how it was made. Then every adoption is a measurement, not an argument.
- Where a capability serves populations with different competence, ship it in more than one scaffolding mode and validate each separately. An open-ended surface is a gift to the experienced user and a wall for the novice, and a single average hides both.
- Keep a written record of the bets that did not work. Your own survivorship bias is the thing most likely to turn this pattern into recklessness.

## Apply to your product

- Which capability are you waiting on quality for, and how long would the integration work take if the quality arrived tomorrow?
- What is your quality bar, stated so that a tool's output can fail it? If you cannot state it in one sentence, you do not have one.
- Which of your users would be helped by an open-ended version of your AI feature, and which would be stopped cold by it?

## See also

[[point-ai-at-unit-economics-not-features]] · [[simplify-until-automatable-name-what-must-survive]] · [[../duo-experimentation/SKILL]]
