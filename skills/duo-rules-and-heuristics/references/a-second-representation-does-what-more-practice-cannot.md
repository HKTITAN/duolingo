---
name: duo-rules-and-heuristics-a-second-representation-does-what-more-practice-cannot
summary: If the notation users already have maps many-to-many onto reality, more practice inside it reinforces the ambiguity — give them an orthogonal representation instead.
metadata:
  internal: true
---

# A Second Representation Does What More Practice Cannot

## Concept

Some errors are not knowledge gaps. They are notation gaps. If the representation a user already has maps many-to-many onto the underlying reality, practising inside it reinforces the ambiguity rather than resolving it, and every extra rep makes the confusion more fluent. The fix is an orthogonal representation with a stable handle for the real unit, so the messy mapping becomes something the user can reason about explicitly instead of something they keep tripping over. Two cousins of the same move: introduce an abstract idea visually before symbolically, and hand over a manipulable object instead of a question about the relationship.

## What Duolingo does

- Rather than teaching English pronunciation through spelling, the pronunciation tab gives **each sound its own symbol** (for example æ) alongside an example word like "cat," explicitly so learners think about individual sounds and not written letters — because English uses single letters for many sounds and many letter combinations for single sounds. The notation exists precisely because the familiar one is many-to-many. Source: blog.duolingo.com/duolingo-english-sounds-tab (Duolingo blog, 2024-11-20; accessed 2026-09-22)
- Duolingo Math teaches fraction comparison **starting with pictures** so learners see which fractions are equal before comparing numerators and denominators, and uses number lines and pictures as the backbone for fraction operations, improper fractions and fraction-to-decimal conversion. The symbols then arrive as notation for something already understood. Source: blog.duolingo.com/4th-grade-math (Duolingo blog, 2026-07-14; accessed 2026-09-22)
- For a relationship between two variables, learners get a **manipulable object rather than a question**: a simplified clock with hands set arbitrarily, where moving the minute hand makes the hour hand respond, so the relation is run rather than recalled. Exercises are engineered per concept instead of reusing one question template. Context for why this matters: **93% of U.S. adults report at least some math anxiety** and **half of high schoolers report very high math anxiety**. Source: blog.duolingo.com/duolingo-launches-math-app (Duolingo blog, 2022-10-26; accessed 2026-09-22)

**Tension.** Bespoke representations do not scale like a generic question template — engineering one interaction per concept is expensive, and the puzzles and Life Skills built this way shipped on iOS only, lagging Android. A second representation is also one more thing to learn, so it earns its place only when the first one is actively causing the errors.

## The transferable pattern

Before adding practice, check the notation. If one label in your system means several different things, or several labels mean the same thing, no amount of repetition will fix the resulting errors — users are drilling an ambiguity.

Three moves, in rough order of cost:

1. **Introduce a clean symbol for the real unit.** When the user's existing vocabulary conflates two things, give the distinction a name of its own. A name creates a place to store a thought that previously had nowhere to live.
2. **Show the concrete form before the symbolic one.** A picture gives a checkable mental model to reason with, so the notation lands as a label for something already understood. Skipping this stage is what makes a topic feel intimidating rather than merely new — and symbol manipulation learned as ritual collapses the moment a case varies.
3. **Hand over a manipulable object instead of a question about it.** A question tests whether the model is already there; a tool that lets the user move one input and watch another respond builds it, because they run their own experiments and watch the invariant hold. Strip it to only the parts that matter, so every degree of freedom they play with is teaching something.

Note the cost honestly. These are bespoke builds, not templates, and each one is another thing to maintain.

## Apply to your product

- Which word in your product vocabulary means two different things to your users? What would a clean name for each of them be?
- What abstract idea do you currently introduce in its symbolic or tabular form first — and what is the picture that should come before it?
- Where do you ask users a question about a relationship you could instead let them manipulate and watch?

## See also

[[where-explicit-instruction-earns-its-place]] · [[make-the-invisible-error-observable]] · [[give-them-a-handle-they-can-hold-under-pressure]]
