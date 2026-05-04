---
name: duo-product-intuitive-by-default
summary: Products should not have to explain themselves; documentation is a sign the design is incomplete.
metadata:
  internal: true
---

# Intuitive by Default

## Concept

The handbook's *Show Don't Tell* and *Raise the Bar* both contain a version of: *our products don't have to explain themselves — they should be intuitive to everyone.* Tutorials, tooltips, walkthroughs, FAQs are signals that the design is leaning on documentation. Sometimes that's necessary. More often it's a sign to fix the design.

## What Duolingo does

- Onboarding teaches by *doing the thing*, not explaining it. The first lesson is a lesson, not a tutorial about lessons.
- Most UI elements teach themselves through interaction; the home screen path is a path, you tap a tile, you do a lesson.
- Where explanation is unavoidable, it's compressed into a single line of voice ([[../duo-voice/references/onboarding-copy]]) rather than a multi-screen tutorial.
- Complexity is hidden by default — advanced features (paths, scores, league details) only surface when relevant.

## The transferable pattern

Three rules:

1. **Tutorials are debt.** Every "how to use this" screen is a place the design didn't carry its own weight. Inventory them; aim to remove most.
2. **Teach through doing.** A user who completes a small task is a user who has learned more than one who reads a paragraph.
3. **Hide complexity until it's needed.** Default views should feel small. Advanced features uncover as the user accumulates context.

A useful diagnostic: if a new user needs a tooltip to understand the primary action of the home screen, the home screen is the bug, not the tooltip.

## Apply to your product

- How many tooltips, walkthroughs, or "?" icons does your product ship? Could half be removed by redesigning the underlying screen?
- Can a brand-new user reach first value in your product without reading anything?
- What's the most-explained feature in your product? What would it look like if it taught itself?

## See also

[[raise-the-bar]] · [[polish]] · [[../duo-voice/references/onboarding-copy]] · [[../duo-retention/references/churn-diagnostics]]
