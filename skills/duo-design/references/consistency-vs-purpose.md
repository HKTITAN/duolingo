---
name: duo-design-consistency-vs-purpose
summary: Consistency exists to lower learning cost and simplicity exists to raise clarity — when either stops serving its own reason, tier the system instead of applying one rule everywhere.
metadata:
  internal: true
---

# Consistency vs Purpose

## Concept

Consistency and simplicity are both means, never ends. Consistency earns its keep by lowering the cost of learning a new screen; the moment a consistent element takes significant space while signalling nothing useful, it has inverted its own justification and become a tax. Simplicity runs the same trap in the opposite direction: removing an element that was quietly carrying meaning buys a small aesthetic gain and pays for it with a real comprehension loss. The resolution is almost never one rule applied everywhere. It is a tiered system — a fixed part that guarantees recognition, and a graded part that lets each surface say what it actually is.

## What Duolingo does

Source: blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

- The redesign team named both tensions out loud and annotated their own mockups with the challenge questions, rather than letting the rules go unexamined: consistency was at odds with the design's purpose, and simplicity was at odds with clarity.
- The resolution was **tiered, not uniform**: header sizes were graded by each tab's purpose, while title position stayed constant across every tab. The constant part is what makes the tabs feel like one product; the graded part is what tells you which tab you are on.
- Type was reduced to a **minimal scale**, so hierarchy is carried by a small number of deliberate steps instead of many near-identical ones.
- Whitespace was used *around* components rather than containers being forced around them — the container was the consistent element that had stopped earning its space.
- The starting condition is worth naming: inconsistent headers, typography without hierarchy, and uneven spacing. Uniformity was the cure for that, and over-applied uniformity was the next failure mode.

## The transferable pattern

Three rules:

1. **Ask what each consistent element buys.** If the answer is only "it is consistent," it is decoration with a rule attached. Consistency is a budget spent on recognition, and it runs out.
2. **Split fixed from graded.** Pick the one or two attributes that must never move — position, order, anchor point — and let the rest vary by the purpose of the surface.
3. **Before removing an element, name what it was communicating.** If nothing, remove it. If something, replace the signal before you delete the carrier.

Anti-patterns:
- A design-system rule with no stated purpose, so no one can tell when it should be broken.
- Treating "we simplified it" as a result. Simplification is a cost paid for clarity; if clarity did not go up, the cost was pure.
- Grading everything, which is just inconsistency with better documentation.

## Apply to your product

- Pick the most repeated element in your interface. What does it tell the user that they could not get otherwise?
- Which one attribute of your primary surfaces must stay fixed for people to stay oriented, and which are free to vary?
- The last thing you removed for cleanliness — what signal went with it, and where did that signal land instead?

## See also

[[prototype-the-extremes]] · [[type-system]] · [[color-tokens]] · [[bottom-bar-navigation]]
