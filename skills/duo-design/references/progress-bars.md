---
name: duo-design-progress-bars
summary: The most important UI element in a gamified product, treated as such — designed, animated, and given weight.
metadata:
  internal: true
---

# Progress Bars

## Concept

A progress bar tells the user *where they are* and *how much is left*. In a gamified product, it's also the smallest unit of forward motion — the single visual element a user looks at most often. Most product progress bars are afterthoughts: a thin gray line, no animation, no satisfaction. The opportunity is to invest in this element disproportionately.

## What Duolingo does

- Progress bars in lessons fill with smooth motion as questions are answered, with a small overshoot when complete.
- Bars are visually weighty — colored, rounded, prominent in the layout.
- Filling animations have rhythm — increments correspond to user actions, not constant time.
- Completion has a small celebration of its own: bar fills, holds, transitions to the next screen.
- Variants exist for unit-level and section-level progress, each visually distinct so users learn to recognize each.

## The transferable pattern

Three rules:

1. **A progress bar is a feature, not a primitive.** Treat it with the same care as a button.
2. **Animate the fill.** A bar that snaps to value reads as a meter. A bar that fills smoothly reads as progress.
3. **Calibrate completion.** The 95–100% transition deserves disproportionate attention; that's where the user's brain rewards them.

Anti-patterns:
- Static bars that update without animation. Functionally informative; emotionally dead.
- Progress bars that lie (fast at first, slow at the end, or vice versa). Users notice; trust drops.
- Multiple progress bars stacked on the same screen with no hierarchy. The user can't tell which one matters.

## Apply to your product

- Does your product have progress visualization? Is it given visual weight?
- Does the fill animate, or does it snap?
- Does the 95–100% transition get any special treatment?

## See also

[[../duo-gamification/references/progression-design]] · [[juicy-motion]] · [[celebration-design]]
