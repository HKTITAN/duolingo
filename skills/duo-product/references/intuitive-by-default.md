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

Source: blog.duolingo.com/product-principles (Duolingo blog, 2024-02-21; accessed 2026-09-22)

- Duolingo's VP of Product makes "build for the global user" a standing review question, and the test is comprehension without explanation: *"Will our typical user understand what we just did? Will they understand what this main action button does? When they read what's on the screen, will it make sense to them?"* He estimates **about half the time** the team has to be reminded to design for the international, older, or low-tech-literacy user rather than for themselves.
- The clearest application: when learners kept saying they weren't sure they were using Duolingo *"the 'correct' or 'best' way,"* the fix was not documentation. Duolingo replaced the branching skill "tree" home screen with a single linear **path**, launched to all learners **November 1, 2022** — one circle per crown level, next step always obvious (blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)).
- Onboarding teaches by *doing the thing*, not explaining it. The first lesson is a lesson, not a tutorial about lessons.
- Where explanation is unavoidable, it's compressed into a single line of voice ([[../duo-voice/references/onboarding-copy]]) rather than a multi-screen tutorial.
- Complexity is hidden by default — advanced features (paths, scores, league details) only surface when relevant.

Tension, honestly recorded in the path post: removing the branching surface removed the per-circle labels too, and Duolingo had to **add tap-to-reveal popups and rewrite unit headers** to put the lost information back. "Intuitive" did not mean "explains nothing" — it meant moving the explanation to the moment of need instead of the front of the flow. The path is also visibly longer than the tree, and a power user loses their self-directed route.

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

[[raise-the-bar]] · [[polish]] · [[difficulty-with-mitigations]] · [[fit-the-artifact-to-the-moment]] · [[../duo-voice/references/onboarding-copy]] · [[../duo-retention/references/churn-diagnostics]]
