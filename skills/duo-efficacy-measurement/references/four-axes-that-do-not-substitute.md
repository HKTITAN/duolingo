---
name: duo-efficacy-measurement-four-axes-that-do-not-substitute
summary: Enjoyment, mastery, application and external standard are four independent questions, each needing its own method.
metadata:
  internal: true
---

# Four Axes That Do Not Substitute

## Concept

Anything that claims to teach or change behaviour can be strong on one axis and hollow on the next. Engagement without mastery is a slot machine. Mastery without application is teaching to the test. Application without an external standard is a claim you grade yourself. These four are not proxies for one another, so measuring only the one that is cheapest to instrument — almost always engagement, because it arrives free in your event stream — hides failure in the other three.

## What Duolingo does

Source: blog.duolingo.com/duolingo-efficacy-research-framework (Duolingo blog, 2022-10-17; accessed 2026-09-22)

- The efficacy research framework poses exactly **4 questions**, each with a different method: **engagement** (UX interviews plus in-app behavioural data), **mastery** (skill testing on what was taught), **application** (simulated real-world tasks), **proficiency** (independent standardized tests).
- The post concedes the failure mode in both directions: "it doesn't matter how expertly-crafted our lessons are if you don't want to come back to them" and "just because we think we're teaching something, doesn't mean our learners are learning it."
- The external axis is anchored to CEFR's **6 levels** (A1, A2, B1, B2, C1, C2), grouped Basic / Independent / Proficient, so the top-line claim uses a scale Duolingo did not author. The in-product score is explicitly a process metric — "most people aren't learning just to earn XP" and "getting everything correct in the app is not the ultimate goal."
- A second axis split runs underneath: Duolingo reports **4 SWRL skills** (speaking, writing, reading, listening) separately rather than as one number, and publishes the receptive/productive distinction — including "receptive bilinguals" who understand fully but are not comfortable producing. Their own framing is that there is no established measure for whether someone "knows" a language; it is not as easy as checking a box (blog.duolingo.com/what-is-bilingual-6-types (Duolingo blog, 2023-03-21; accessed 2026-09-22), which also names **6 types of bilingualism** — simultaneous, sequential, receptive, heritage, bimodal, emergent).

The cost of this framework is real: four axes means four measurement programs, three of which need instruments that do not fall out of your product telemetry.

## The transferable pattern

Score your product on four separate questions, and never let a strong answer to one stand in for a missing answer to another.

1. **Do they come back?** Behavioural data plus interviews. Necessary, never sufficient.
2. **Did they acquire what you taught?** Testing against your own material. Confirms transmission, not usefulness.
3. **Can they do the real task?** A simulated version of the job they came to do, using your output under realistic conditions.
4. **Do they clear a bar someone else set?** An outside standard, scored by an instrument you do not control.

Then refuse to collapse the result into a single number. Split by mode — recognizing versus producing, reading versus doing — because someone can be near-expert at one and a beginner at the other. One averaged score describes nobody and prescribes the wrong next step for everybody.

## Apply to your product

- Which of the four axes are you actually instrumented for today, and which one are you quietly letting engagement stand in for?
- What would the "simulated real task" look like for your product — the thing your user came to accomplish, done unaided with what you taught them?
- Where are you reporting one number that hides two abilities moving in opposite directions?

## See also

[[borrow-the-instrument-you-do-not-control]] · [[build-the-item-pool-independently-of-the-content]] · [[../duo-experimentation/references/outcome-not-engagement]]
