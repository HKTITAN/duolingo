---
name: duo-adoption-design-workarounds-are-unshipped-requirements
summary: Behaviour that looks like misuse is usually a rule-governed adaptation by capable users — and the workaround that reuses an existing affordance spreads fastest.
metadata:
  internal: true
---

# Workarounds Are Unshipped Requirements

## Concept

Behaviour that looks like misuse is usually a rule-governed adaptation by your most capable users. It looks sloppy from outside because the observer lacks the competence to see the system underneath. Find the rules before you design the fix: the workaround is evidence of a capability your product does not yet support, and it comes with a proven adoption path attached. There is a second, sharper lesson in how these adaptations spread — users repurpose an existing affordance long before they adopt a purpose-built new one.

## What Duolingo does

- Duolingo's post on codeswitching reclaims Spanglish from the deficiency framing — the term was **first recorded in 1958**, coined to deride bilinguals for supposedly incomplete knowledge of both languages — and then documents the actual grammar.
- The rules are strict: English rules apply within English spans, Spanish rules within Spanish spans, and **distinct rules govern the switch point**. Because Spanish *que* is bound to the following verb in a way English "that" is not, bilinguals unconsciously prefer Spanish *que* regardless of what surrounds it. The foundational paper by Shana Poplack is itself titled with a codeswitch: "Sometimes I'll start a sentence in Spanish y termino en español."
- The stated finding: codeswitching **requires high proficiency in both languages** plus sensitivity to the listener's abilities. It is an expert behaviour, not a failure.
- Tension: it does not generalise. Not all bilinguals codeswitch, and heavy switching concentrates in communities with a distinct third culture — the US-Mexico border, Puerto Rico, Caribbean communities in New York and Miami. Reading a power-user behaviour as universal demand would be a mistake.
- On reuse versus invention, Duolingo documented **4 distinct strategies** Spanish speakers use for gender-neutral reference. The frictionless one is reuse: instead of inventing a neutral direct-object pronoun, speakers use the existing indirect-object pronouns *le/les*, and "many dialects of Spanish already use le and les in some situations where lo and la were traditionally the only options." The higher-cost strategies are novel morphology (*-e/-es*: *le hije*, *les alumnes*, *elle es alte*) and verbose doubling (*las cocineras y los cocineros*).
- Tension, stated in that post: the cheapest strategy is the least complete. Doubling "still specifies gender and does not include those who are non-binary." Reuse buys adoption speed by inheriting the old form's limitations.

Source: blog.duolingo.com/spanglish-codeswitching (Duolingo blog, 2021-09-15; accessed 2026-09-22)

Source: blog.duolingo.com/inclusive-language-in-spanish (Duolingo blog, 2024-06-04; accessed 2026-09-22)

## The transferable pattern

When you find users doing something the system did not intend, run this sequence before you fix it:

1. **Assume rules exist and go find them.** The behaviour is almost always consistent, constrained, and sensitive to context you never modelled. Shutting it down destroys capability; documenting its rules tells you what to build.
2. **Check who does it.** If executing the workaround requires high skill, it is a signal from your most competent segment — the users whose needs run ahead of your roadmap.
3. **Check how widespread it actually is.** Concentrated, sub-community behaviour is real demand but not universal demand. Do not promote a specialist adaptation into the default flow.
4. **Prefer overloading an existing affordance over inventing a primitive.** An existing affordance already has conventions, muscle memory, and legitimacy inside some part of your user base, so reuse costs nothing to learn and nothing to justify. A new primitive has to win all three from zero.
5. **Then name what reuse costs you.** The repurposed affordance inherits the old one's limits, and those limits eventually become the reason it fails. Ship the cheap version, and know in advance which case it will not cover.

An overloaded feature in your product is an unshipped requirement with proof of adoption already attached.

## Apply to your product

- What are your power users doing that your team calls misuse? Write down its rules as if it were a designed feature.
- Which of your features is carrying two jobs because the second one was never built? That overload is a spec.
- For the next capability you add, is there an existing affordance users would repurpose instead — and what does that cheaper path fail to cover?

## See also

[[build-for-the-user-your-ladder-skips]] · [[the-progression-selects-give-a-test-out-and-a-side-door]] · [[../duo-experimentation/SKILL]]
