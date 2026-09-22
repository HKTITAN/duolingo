---
name: duo-localization-layout-overrides-your-content-policy
summary: Containers sized for the source string quietly revert your content decisions, and a denser script can buy explanation a longer one cannot.
metadata:
  internal: true
---

# Layout Overrides Your Content Policy

## Concept

Content rules lose to pixels. The careful, precise, non-presumptuous phrasing is almost always longer than the blunt one, so if a container was sized for the source string, every overflow gets resolved by reverting to the short form — the one carrying the assumption you were trying to avoid. Nobody decides this; the design decides it, quietly, per string. The same mechanism runs in reverse: where the writing system is denser, the same box holds an explanation instead of a label, and that extra explanation converts. Both directions say the same thing — space is a content budget, and you set it before the copy is written.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-keeps-its-spanish-localization-inclusive-2 (Duolingo blog, 2021-07-13; accessed 2026-09-22)

- The Spanish team weighs "constraints around spacing, design, and context" against its writing guide, and accepts divergence from the source when the neutral construction will not fit. Where the neutral welcome (*te damos la bienvenida*) overflows, the string becomes *hola*.
- The fallback keeps neutrality and tone but loses the original meaning — a greeting where there was a welcome. The layout, not the policy, made that call.
- Spacing constraints are also the stated reason several achievement names kept a gendered form rather than a rewritten one.

Source: blog.duolingo.com/copy-testing-experiments (Duolingo blog, 2022-01-14; accessed 2026-09-22)

- Chinese localization ran the inverse. Because the script is denser, the same components could hold a benefit description instead of a feature name — the label for unlimited hearts became "no heart loss on errors", and the mastery quiz became "test your knowledge anytime".
- The expanded labels **increased free trial sign-ups**. The post notes the same move was **not feasible in any of their longer languages**.
- Retired-system note: hearts have since been replaced by an energy system, so the specific label is gone. The mechanism — same pixels, more meaning, better conversion — is what carries.

Tension worth naming: the Chinese win is a per-language ceiling, not a portable improvement. Treating it as a global lesson would produce truncated strings everywhere else.

## The transferable pattern

- **Size containers for the longest rendering you intend to allow, not the source one.** Run the measurement before the component is built; afterwards, every fix is a copy compromise disguised as a translation decision.
- **Make overflow a visible failure, not a silent one.** If the only signal is a shortened string in a review tool, your content policy is being overruled without a ticket. Flag it as a layout bug so it gets a layout fix.
- **Let copy length follow the writing system.** Some locales can afford explanation where others afford only a label. Allow per-locale copy length rather than forcing one structure everywhere, and expect the wins to be uneven.
- **Never generalise a density-driven win.** A result that depends on characters-per-pixel is scoped to scripts with that property. Ship it where it applies and say why it stops there.
- Pixel craft itself — how the component reflows, what the type scale is — is a design-engineering question; hand it over rather than inventing values here.

## Apply to your product

- What is your longest supported rendering of your most important label, and was any component in your product sized against it?
- When a translated string overflows today, who decides what gets cut, and does anyone downstream ever see that decision?
- Are there locales where your components have slack that you are currently filling with a terse label instead of a reason to buy?

## See also

[[rewrite-rather-than-default-the-assumption]] · [[localize-to-a-consumption-budget]] · [[../duo-design/SKILL]]
