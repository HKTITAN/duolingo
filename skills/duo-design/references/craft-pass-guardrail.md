---
name: duo-design-craft-pass-guardrail
summary: Fund a pure polish project by making the core metric a flat guardrail rather than the target it was never going to move.
metadata:
  internal: true
---

# Craft Pass Guardrail

## Concept

Polish rarely shows up as lift on the number the business cares about most. It compounds into trust, and trust is slow and diffuse. So if you ask a craft project to justify itself by moving the core metric, one of two bad things happens: it never gets funded, or it gets redesigned into something aggressive enough to move the number — which is no longer a craft project. The framing that works is asymmetric: the core metric is a *guardrail* that must not be harmed, and success is measured on secondary engagement plus the qualitative bar. That lets consistency work ship on its own terms.

## What Duolingo does

Source: blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

- The refresh was explicitly a craft project, not a feature: the stated problems were inconsistent headers, typography without hierarchy, and uneven spacing across the core tabs. No new capability was being added.
- The result was reported in exactly the guardrail shape — **higher engagement across tabs while core learning metrics were maintained**. Engagement is the thing polish plausibly moves; the learning metric is the thing that must not slip.
- The quality bar was enforced with process rather than with a metric: engineering partnered on QA, including **self-QA against design overlays**, on top of the existing dogfooding practice across languages and devices.
- Exploration for the project ran as extreme directions prototyped on real phones ([[prototype-the-extremes]]), so the cost of the craft work was front-loaded into cheap probes.

## The transferable pattern

Three rules:

1. **Declare the guardrail before you start.** Name the metric that must not move down and the threshold that counts as harm. Without it, any noise in the number reads as evidence against the work.
2. **Measure on the secondary surface.** Pick the metric polish actually touches — time on the improved surface, depth of navigation, repeat visits to it — and commit to it in advance so the result is not chosen after the fact.
3. **Back the qualitative bar with process, not argument.** Overlay-based self-review and broad internal use produce a defect list; "it feels better" produces a debate.

Anti-patterns:
- Promising the craft pass will lift the headline number. You will either lose the bet or win it by shipping something that was not a craft pass.
- Shipping polish with no measurement at all, which means you cannot detect the case where it made things worse.
- Letting the guardrail become a second target, so the team starts optimizing the thing it was only supposed to protect.

## Apply to your product

- What is the one number a redesign of your main surface is not allowed to harm, and what drop would you call harm?
- Which secondary metric would plausibly move if the surface simply felt better, and are you already collecting it?
- Who reviews craft work today, and do they have a mechanical way to catch drift, or only their opinion?

## See also

[[prototype-the-extremes]] · [[../duo-experimentation/references/guardrail-metrics]] · [[../duo-product/references/polish]] · [[../duo-product/references/dogfooding]]
