---
name: duo-category-entry-port-the-incumbents-goal-not-their-safeguards
summary: An incumbent's controls compensate for constraints your medium does not have; port the goal they served, not the controls.
metadata:
  internal: true
---

# Port the Incumbent's Goal, Not Their Safeguards

## Concept

When you move a category into a new medium, the incumbent's rulebook looks like a specification. It is not. It is a pile of compensations for the physics of the old delivery model — and each compensation carries failure modes of its own. Copy the controls and you import those weaknesses while forfeiting the leverage that made the new medium worth adopting in the first place. Ask instead what outcome each control was buying, then buy that outcome the cheapest way your medium allows.

## What Duolingo does

Source: blog.duolingo.com/testsecurity (Duolingo blog, 2021-04-23; accessed 2026-09-22)

- The Duolingo English Test was designed digital-first, not as a digitized test centre. Rather than replicating proctoring, Duolingo catalogued what the test-centre model actually fails at.
- The catalogue is specific: in an average testing centre **one proctor supervises over 25 test takers at a time**; a **single rule-breaker can invalidate hundreds of co-located exams**; and proctors are **locally contracted**, which makes them reachable by bribes and by threats.
- Having named the goal those controls served — a score an institution can trust — the team designed for that goal directly and ended up both more accessible and more secure than the model it replaced.
- The same discipline shows up in content structure. Realigning existing courses such as German to the CEFR framework meant **restructuring from the ground up**, starting from "what would a learner need to know first?" rather than patching the old ordering — while reusing the prior version's data on which grammar points and which specific sentences learners had struggled with. Source: blog.duolingo.com/the-nuts-and-bolts-of-course-creation-at-duolingo (Duolingo blog, 2020-06-11; accessed 2026-09-22)
- Tension worth naming: re-deriving from the goal buys you no inherited legitimacy. Duolingo spent years afterwards producing the research evidence that incumbents got for free by being old — see [[attack-the-axes-the-incumbent-cannot-move]].

## The transferable pattern

Separate three layers before you copy anything from a competitor.

1. **The goal** — the outcome the customer is actually paying for. This transfers. Re-derive it in your own words before you look at anyone's implementation.
2. **The safeguards** — the controls that exist because the old delivery model leaked somewhere. These are the most tempting thing to copy and the least likely to be right. Each one is an admission of a weakness; list the weakness, not the control.
3. **The structure** — the ordering, the taxonomy, the units. When the constraints change, incremental patching produces a hybrid that satisfies neither the old shape nor the new one. Start from a blank page.

The one asset that does transfer across a rebuild is **failure data**. Old-version telemetry records where real users broke down, and that is true regardless of how you restructure. Keeping the old structure to preserve the old work is how you inherit the old problems; keeping the old failure data is how you avoid repeating them.

## Apply to your product

- Pick one control your main competitor has that you were planning to match. What weakness in their delivery model is it compensating for, and do you have that weakness?
- If you rebuilt your core structure from "what does a new user need first?", what would change — and what would you lose by patching toward that answer instead?
- What failure data do you already hold that would survive a ground-up rebuild? Who owns it, and is it in a shape you could seed a new version with?

## See also

[[attack-the-axes-the-incumbent-cannot-move]] · [[optimize-for-the-side-nobody-has-served]] · [[check-whether-your-core-abstraction-survives]]
