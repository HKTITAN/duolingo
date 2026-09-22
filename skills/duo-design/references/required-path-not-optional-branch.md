---
name: duo-design-required-path-not-optional-branch
summary: Users satisfice against whatever you mark as required, so put the behaviour you actually want on the main route and get depth by serializing across sessions.
metadata:
  internal: true
---

# Required Path, Not Optional Branch

## Concept

Whatever your interface marks as required becomes the definition of "done" for almost everyone. Optional depth reads as skippable no matter how valuable it is, so hiding the behaviour you want in a side branch is the same as not shipping it. The fix is structural: move it onto the mandatory route. The obvious objection is that the route then gets longer — and session length is the constraint that governs whether people start at all. The way out is to serialize instead of inflate: keep each session the same length and get the depth from continuity across sessions, which has the side benefit of supplying a reason to come back.

## What Duolingo does

Source: blog.duolingo.com/how-well-does-duolingo-teach-english (Duolingo blog, 2022-09-19; accessed 2026-09-22)

- The old home screen offered **5 levels per skill but required only level 1**, and Duolingo observed that many learners simply never levelled up. The depth was there and unused.
- The redesign condensed each skill to **3 levels** and placed every level, plus practice and Stories, inline on the learner's single route rather than behind an optional tap.
- The naming changed with the structure: unit headers were rewritten as tasks the learner would be able to do, such as "get directions" in place of "City 3" (blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)).
- Depth without longer sessions came from serialization: advanced Stories run **one storyline across 3 separate stories** in different formats, which the team says "helps us tell longer stories without making each individual lesson longer" (blog.duolingo.com/duolingo-advanced-stories (Duolingo blog, 2022-10-19; accessed 2026-09-22)).

**Tension.** The restructure shipped partly on inference. Duolingo states it *believes* learners will do at least as well under the new structure, on the grounds that the external alignment and the count of skills are unchanged — but the efficacy data was collected under the old design. Moving a behaviour onto the required path is a strong lever precisely because it changes what most people experience, which is also why its effects should be measured rather than assumed.

## The transferable pattern

Three rules:

1. **Required is a design decision, not an engineering one.** Audit what your product marks as optional and ask which of those you would be upset to learn most people skip.
2. **Hold the session length fixed.** It governs whether anyone starts. Depth that lengthens the unit trades a certain cost for an uncertain gain.
3. **Serialize for depth.** Link units into a continuing arc so each one stays short and the next one has a pull.

Anti-patterns:
- Making the deep thing required *and* longer, which converts a skip into an abandon.
- Solving low uptake of optional depth with promotion instead of structure.
- Restructuring the main route and keeping the old efficacy claim.

## Apply to your product

- What is the one behaviour you most wish more users did, and is it currently on the required path or beside it?
- How long is your core session, and what happens to starts if it grows by a third?
- Could the depth you want be split across consecutive sessions with a thread connecting them?

## See also

[[capability-labels]] · [[progress-bars]] · [[../duo-retention/SKILL]] · [[../duo-gamification/references/progression-design]]
