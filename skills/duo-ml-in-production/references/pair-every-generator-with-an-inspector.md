---
name: duo-ml-in-production-pair-every-generator-with-an-inspector
summary: A generator without an inspector is a machine that produces errors at scale — budget the audit-and-correct tooling into the same project.
metadata:
  internal: true
---

# Pair Every Generator With an Inspector

## Concept

Automated generation scales the defect rate exactly as fast as it scales the output rate. The pipeline that produces a hundred thousand artifacts also produces a hundred thousand chances to be subtly wrong, and the wrongness is distributed evenly across everything nobody will ever look at.

Without tooling to find and patch bad outputs, you have two remedies, and both are bad: regenerate everything whenever any defect is found, or ship known-wrong artifacts and wait for users to report them. The inspector is not a follow-up project. It is half the factory, and a team that funds only the generating half has funded a machine for manufacturing errors quietly.

## What Duolingo does

Source: blog.duolingo.com/world-character-visemes (Duolingo blog, 2022-11-10; accessed 2026-09-22)

- Duolingo generates mouth-shape animation for its characters across **40+ languages, 100+ courses and 10 World Characters, with 20+ mouth shapes designed per character**. Animating that by hand was "completely out of the question."
- They state the discipline directly: they built up the tools and processes **not only to generate the material, but to audit and correct it when they need to**.
- When the signal they needed did not exist, they harvested it from a model they already owned. Their text-to-speech vendor returned neither pronunciations nor timings, so they **generated the speech and ran it back through their own in-house speech recognition and pronunciation models** — built for a completely different purpose — to recover per-word and per-phoneme timing.
- The output ships as **a state machine runtime file plus timing metadata, not prerendered video**, so it stays inspectable and interruptible: tapping a single word makes the character animate just that word, and finishing early makes it stop mid-sentence.
- **The tension:** this whole apparatus only pays for itself at scale. Manual production was ruled out solely because of volume — at a small catalogue, building the generator plus the inspector plus the correction tooling costs more than doing the work by hand.

## The transferable pattern

Budget three things in the same project, or you have not funded a pipeline:

1. **The generator** — the part everyone wants to build.
2. **The inspector** — automated checks that flag suspect outputs, plus a review surface where a person can see a specific artifact and judge it. Without the second half, the checks just produce a number nobody can act on.
3. **The corrector** — a way to patch one bad output without regenerating the batch. If your only repair is a full rerun, every small defect becomes a scheduling negotiation and most of them never get fixed.

Two design choices make inspection cheap enough to actually happen. Keep the output structured rather than flattened: a description of what should happen, plus data, can be diffed, queried and patched, while a rendered blob can only be looked at. And before buying or building a new signal source, check what your existing internal models already emit as a byproduct — a model built for one purpose often produces intermediate output that is precisely what the new pipeline needs, turning a research project into an integration.

Finally, apply the scale test honestly. The generator-plus-inspector pattern is correct when manual production is impossible, not when it is merely tedious. Below that line the pipeline is a more expensive way to get a worse result.

## Apply to your product

- If your generator emitted a subtly wrong output today, what would detect it — a check, a user, or nothing?
- Can you fix one bad artifact in place, or does every correction require regenerating the batch?
- What signal are you about to buy or build that one of your existing internal models already produces as a byproduct?

## See also

[[generate-from-one-parameterized-primitive]] · [[integrity-by-construction-not-secrecy]] · [[../duo-ai-agent-platform/references/every-producer-needs-a-janitor]]
