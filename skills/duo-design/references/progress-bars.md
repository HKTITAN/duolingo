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

Source: blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)

- The home screen *is* the progress bar. On November 1, 2022 Duolingo replaced the branching skill tree with a single linear path; each circle equals one crown level of a skill, and levels from different skills are interleaved so that review reads as forward motion rather than going "back" to a cracked skill.
- The path is deliberately *longer* than the tree it replaced. The post answers "Did you add a ton of extra lessons?" with no — same content, redistributed, plus practice and Stories inline. Duolingo took a longer-looking bar in exchange for an honest one.
- Progress is tiered and each tier looks different: per-character bars run gray → partially gold → fully gold in the Japanese characters tab (blog.duolingo.com/learning-asian-language-duolingo (Duolingo blog, 2021-12-16; accessed 2026-09-22)), while the Duolingo Score shows a separate bar filling *between* two whole-number scores — "a granular measure of what you've learned" that a CEFR level is too coarse to give (blog.duolingo.com/duolingo-score (Duolingo blog, 2024-10-23; accessed 2026-09-22)).
- Long-scroll navigation got its own affordance rather than a shorter bar: a floating arrow button in the bottom-right jumps you back to your current spot.

**The standard Duolingo holds progress numbers to.** For the 2020 Year in Review the team brainstormed every possible stat, then deliberately omitted streak and percentage-of-course-completed because those values shift when courses are updated — "to avoid confusion over inaccurate information" (blog.duolingo.com/duolingo-2020-year-in-review (Duolingo blog, 2021-05-03; accessed 2026-09-22)). They left their single most emotionally loaded number off the flagship celebration rather than show one they couldn't stand behind.

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

[[../duo-gamification/references/progression-design]] · [[juicy-motion]] · [[celebration-design]] · [[required-path-not-optional-branch]] · [[capability-labels]]
