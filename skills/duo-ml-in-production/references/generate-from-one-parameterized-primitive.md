---
name: duo-ml-in-production-generate-from-one-parameterized-primitive
summary: When content varies combinatorially, generate it from one parameterized primitive — then move authoring to whoever owns the iteration loop.
metadata:
  internal: true
---

# Generate From One Parameterized Primitive

## Concept

Manual asset production scales linearly with the number of variations, while the variation count scales as the product of every axis you vary along: difficulty band, domain, locale, theme. The two curves diverge immediately, so any amount of hand-authoring becomes the bottleneck long before the catalogue is interesting. A parameterized primitive collapses that product back into one thing to build and maintain.

The second decision arrives later and is easy to miss. Once the primitive exists, the question stops being *can we express this* and becomes *who should own changing it*. If the primitive lives in platform code, every visual tweak needs an engineer and every new platform needs a rewrite. Those costs are invisible at the start and dominant at scale.

## What Duolingo does

Source: blog.duolingo.com/developing-math (Duolingo blog, 2024-10-18; accessed 2026-09-22)

- For Duolingo Math, **one class — GriddedGraphView — generates every visual** for area, perimeter, decimals, shapes and coordinates. On iOS it is a CAShapeLayer drawing a dynamic M-by-N grid, with masks, lines, buttons and labels placeable anywhere on it, and it doubles as the base for interactive challenges such as building quadrilaterals.
- That one class let them swap design components, change colours and inject localized text programmatically.
- **Scale of the collapse:** addition skills alone scale the maximum result from 10 to 100 to 500, producing **hundreds of variations of the countable-block visual**; across all content domains the count runs into the **thousands**.
- **Then they reversed the implementation.** The code-drawing approach "worked for a while" and hit two walls: some visuals became extremely hard to draw in code — **a few required mathematical proofs written into the code comments** — and **the Swift did not carry over to Android**.
- They moved authoring into **Rive**, an animation tool that accepts programmatic inputs, keeping the dynamic behaviour while shifting development time to design. In-house Creative Technologists then made the visuals more expressive than engineers had — a wave of water in a liquid-volume challenge, an actual fraction pie.
- **Math launched on iOS first; Android launched roughly a month before the October 2024 post.** The original in-code decision was correct at its scale and wrong at the next one.

## The transferable pattern

Two decisions, taken in order, not at once.

**First, find the primitive.** Look for the smallest configurable object that, given parameters, produces every member of the family. The test is whether a new variation is a new argument or a new file. If it is a new file, you do not have a primitive yet — you have a template, and templates multiply.

**Then choose where the primitive lives, by who owns the iteration loop.** Not by what is technically expressible — code can express anything, which is exactly why this decision gets made by default. If the output needs repeated aesthetic judgment, or must run on several platforms, move authoring into a tool that exports everywhere and accepts runtime parameters. You keep the dynamic behaviour and relocate iteration to the people making the judgment calls.

The reversal is the part worth keeping. Building it in code first was not a mistake; it was right for one platform and simple output. Watch for the two signals that the answer has changed: someone has to prove something to produce an asset, and a second platform is on the roadmap. Either one alone is tolerable. Both together mean the authoring surface, not the code, is now the constraint.

## Apply to your product

- Which family of assets in your product is currently produced one at a time, and what is the product of its variation axes?
- For your most parameterized asset, does a new variation mean a new argument or a new file?
- Who changes that asset today, and how many of those changes actually needed an engineer rather than an engineer's tooling?

## See also

[[pair-every-generator-with-an-inspector]] · [[integrity-by-construction-not-secrecy]] · [[../duo-design/SKILL]]
