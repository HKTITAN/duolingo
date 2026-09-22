---
name: duo-progression-design-sequence-by-task-not-by-taxonomy
summary: Order a path by what the user needs to accomplish first, not by the subject's own internal structure.
metadata:
  internal: true
---

# Sequence by Task, Not by Taxonomy

## Concept

Every domain has an internal structure that experts find obvious: alphabet, then numbers, then colors; entities, then schema, then endpoints; primitives, then composition, then application. That order is the expert's compressed mental model, assembled after they already understood the whole thing. It is almost never the order a newcomer should meet the material in. A prerequisite taught before any task needs it has nothing to attach to and no retrieval cue later — the user files it as trivia and cannot recall it at the moment it would help. Sequence by task instead and every primitive arrives already attached to a reason.

## What Duolingo does

Source: blog.duolingo.com/why-doesnt-duolingo-start-with-abcs (Duolingo blog, 2024-06-25; accessed 2026-09-22)

- Courses skip the ABCs entirely and open with phrases like "Coffee, please!" The alphabet turns out to be primarily useful to advanced learners who need spelling precision — a late need that looks like a first step.
- The team writes communicative objectives per level and covers ordering food, handling a minor emergency, passport control, and finding supplies in a store **within the first 15 units**.
- Numbers arrive when you pay a bill or tell the time. Colors arrive with clothing. Each primitive is introduced at the moment a task demands it, not in a block of its own.
- Duolingo states the assumptions this rests on rather than hiding them: that users are adults already literate in a first system, and that they want to *use* the thing rather than study it for its own sake. Writing systems such as Japanese force exceptions.
- Units pair a mechanism with the situation that uses it — question formation taught inside a shopping scenario, so the sentences read like real speech rather than a conjugation table (blog.duolingo.com/the-nuts-and-bolts-of-course-creation-at-duolingo (Duolingo blog, 2020-06-11; accessed 2026-09-22)).
- **The tension shows up in Duolingo's own A/B data.** Theme-free lessons with explicit conjugation tables beat the integrated themed version on preterite accuracy, **36% → 86%** versus **40% → 54%**. Task-first sequencing won the motivation argument; the stripped-down drill won that particular accuracy test. Both results are real.

## The transferable pattern

Take your table of contents and ask of each item: *what can the user do at the end of it that they could not do before?* If the answer is "nothing yet, it's needed for chapter 6," that item is structural filler in first position.

The move is to invert the dependency. Start from the first outcome the user came for, work backwards to only the primitives that outcome requires, and teach exactly those. Everything else waits for the task that needs it. Concretely:

- Onboarding opens on a real job completed end to end in crude form, not on a tour of the object model.
- Reference structure and teaching structure are different artifacts. Keep the taxonomy-ordered version — as documentation, not as the path.
- Measure the tradeoff. Task-first ordering usually wins on completion and motivation, and can lose on precision for any single sub-skill. If precision on one high-consequence item matters more than flow, break that item out and drill it explicitly, and say why you did.

## Apply to your product

- What is the first genuinely useful thing a new user could finish in their first session, and what is the minimum set of concepts that task requires?
- Which concepts in your current onboarding exist only because a later step needs them? What happens if you move each one to the step that needs it?
- Is there one high-consequence skill where an isolated, taxonomy-ordered drill would beat the integrated version? How would you know?

## See also

[[borrow-an-external-standard-as-the-spine]] · [[rank-what-you-teach-by-cost-of-getting-it-wrong]] · [[front-load-the-context-a-later-rule-will-need]] · [[../duo-gamification/references/progression-design]]
