---
name: duo-prior-knowledge-transfer-the-old-model-is-suppressed-not-erased
summary: A redesign never deletes the old habit — it suppresses it, and suppression costs something every time and fails under load.
metadata:
  internal: true
---

# Suppressed, Never Erased

## Concept

When you replace a system someone already knows, their old model does not go away. Both models stay simultaneously active, and using the new one means actively inhibiting the old one. Inhibition draws on the same executive resources that stress, fatigue and time pressure deplete — which is exactly when the old behaviour comes back. The return trip costs too, because going back to the dominant system means undoing the inhibition you just applied. And because the old model runs beneath conscious control, the user does not know they are applying it, so telling them the new rule once changes nothing.

## What Duolingo does

Source: blog.duolingo.com/languages-vs-dialects-in-your-brain (Duolingo blog, 2022-09-05; accessed 2026-09-22)

- Duolingo's model of the multilingual brain is a volume control, not a switch: "all the varieties that a person knows are turned on in the brain," managed by inhibition — "the cognitive equivalent of turning down the volume… like making them quieter without hitting the off switch." Nothing is ever off.
- Moving between systems carries a measurable **switch cost**, timed by how long it takes a bilingual to start naming a pictured object. The costs are small but real — **a few hundredths of a second** — and the return trip is also charged, because the suppressed system has to be released. Structurally related items are named faster than unrelated ones (English *house* / Swedish *hus*) (blog.duolingo.com/bilingual-brain-changes (Duolingo blog, 2022-11-03; accessed 2026-09-22)).
- Duolingo explains an accent as importing the prior system's whole **"operating system"** — individual sounds, rhythm and intonation, and the rules for which sounds may combine. Because that import is subconscious and stored as muscle memory, the prescription is repeated paired exposure (hearing and producing the new form), not explanation. The timeline is long because you are overwriting automatic behaviour, not adding knowledge (blog.duolingo.com/why-is-pronunciation-hard (Duolingo blog, 2022-08-25; accessed 2026-09-22)).
- Tension one — **the cost is not fixed.** A system's cognitive volume rises and falls with use over a lifetime, so switch costs shrink with practice rather than standing as a permanent tax.
- Tension two — **forced single-mode use is not the only stable strategy.** People who deliberately keep both systems live (code-switchers) develop a second, separate skill: managing both volumes at once. Making users pick one is a choice, not a law.
- Tension three — **Duolingo declines to treat the imported model as a defect.** It reframes an accent as a badge of honour, because the goal is communication, not native-likeness. Which imported behaviours to fight and which to accept is the actual product call.

## The transferable pattern

- **Budget for a permanent switch cost** after any migration or redesign, in both directions. Users alternating between the old tool and yours pay twice, which is why a partial cutover feels worse than either endpoint.
- **Expect regression under load.** Incidents, deadlines and interruptions are when the old muscle memory reappears. Measure error rates *during* your users' busiest hours, not on a calm Tuesday.
- **One announcement does not retrain a reflex.** A changelog entry, a tooltip or a migration guide addresses conscious knowledge. Automatic behaviour needs repeated paired exposure — the user encountering the old cue and performing the new action, many times.
- **Committing to one mode for a block of work beats alternating.** If both systems must coexist for a while, design for blocks, not for interleaving.
- **Decide explicitly which imported behaviours you will fight.** Some are worth retraining; some should just be supported. Accepting the residue is cheaper than an unwinnable retraining campaign, and it stops the user concluding they are bad at your product.

## Apply to your product

- After your last migration, which old behaviour still shows up in your logs — and does it spike when your users are under time pressure?
- Where do your users still alternate between the old system and yours? What would it take to give them one uninterrupted block in yours?
- Which imported habit are you fighting that you could simply support instead, and what would supporting it cost?

## See also

[[hand-them-the-mapping-rule-and-the-prior-becomes-a-predictor]] · [[separate-the-contexts-when-the-risk-is-confusion]] · [[../duo-retention/SKILL]]
