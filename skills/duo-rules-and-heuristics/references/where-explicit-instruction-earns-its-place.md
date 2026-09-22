---
name: duo-rules-and-heuristics-where-explicit-instruction-earns-its-place
summary: Explanation earns its keep only for what exposure will never make salient; its job is attention-direction, not transmission.
metadata:
  internal: true
---

# Where Explicit Instruction Earns Its Place

## Concept

Learning by doing is not enough on its own. Some features are simply not noticeable from examples — they never vary in the input the user sees, or the contrast that would reveal them never occurs. For those, and only those, a short explicit explanation is the highest-leverage thing you can ship, and its job is attention-direction rather than transmission: it makes a pattern findable, after which use does the actual work. The test for whether a rule deserves a written explanation is therefore not "is it important?" but "would a user ever notice this from normal exposure?"

## What Duolingo does

- After years of a **purely implicit methodology** — teaching through repeated exposure to whole phrases rather than explanations and drills — Duolingo added Tips: short illustrated explanations of conjugation, pronunciation and non-intuitive distinctions like "tú" vs "usted," with **dozens of new illustrated tips** across Spanish, French and English. This is a stated reversal, justified by research that the combination beats either pure discovery or pure documentation. Source: blog.duolingo.com/how-are-duolingo-courses-evolving (Duolingo blog, 2019-04-03; accessed 2026-09-22)
- The ordering is explicit: patterns are taught inside every exercise, and written explanation is confined to Guidebooks, focused lessons in larger courses, and the blog. The post notes that reciting endings to yourself can get in the way of actually using the language. Source: blog.duolingo.com/does-duolingo-teach-grammar (Duolingo blog, 2023-02-21; accessed 2026-09-22)
- A stranger version of the same move: make people operate a deliberately different system so the assumptions of their default become visible. Mexican primary students learn **Roman, Egyptian and Mayan numerals alongside decimal** specifically to compare advantages — Roman uses **7 letters, each repeatable up to 3 times**; Egyptian symbols repeat **up to 9 times** and are non-positional, so order does not matter; Mayan is **base 20 with three levels** (1s, 20s, 400s). The stated purpose is a nuanced understanding of how symbols represent value. Source: blog.duolingo.com/mexican-students-math-class-hieroglyphics (Duolingo blog, 2023-11-21; accessed 2026-09-22)

**Tension.** Duolingo concedes that adults especially *want* stated rules, and that seeing a rule spelled out does help them notice the pattern — so the company ships both, ordered, rather than defending the purist position. The original implicit-only stance was not wrong so much as incomplete.

## The transferable pattern

Run every candidate explanation through one filter: **would a user discover this from ordinary use?** If yes, delete the explanation and improve the exposure instead ([[let-them-induce-it-from-volume-then-confirm]]). If no — because the distinction never varies where they can see it, or the failure it causes is silent — write it, keep it short, and position it beside practice rather than in front of it.

Documentation that survives this filter has a different shape from documentation that does not. It points at a thing to notice. It does not attempt to transmit the whole model.

The practical consequence for a docs backlog is that most of it should be deleted rather than improved. A page explaining something users already work out is not neutral — it costs attention that the un-inferable things needed, and its existence is why nobody trusts the set enough to read any of it.

There is a second, underused tool for the same problem. When a property of your users' default system is invisible *because* it is always present, do not describe it — make them operate a system that violates it. Handing someone a deliberately different tool for the same job turns every silent assumption into a visible choice, and it teaches the underlying operation rather than your notation for it. That is why a team that has only ever used one stack cannot see its stack's opinions until they ship something on another one.

## Apply to your product

- List the three things you most want users to understand. For each, could they discover it from normal use? Everything that could, does not need a doc.
- What silent failure does your product allow — something a user gets wrong without ever finding out? That is where explanation earns its place.
- Which of your conventions look like laws of nature to your team because you have never built anything that violated them?

## See also

[[let-them-induce-it-from-volume-then-confirm]] · [[explanation-lands-at-the-moment-of-the-error]] · [[a-second-representation-does-what-more-practice-cannot]]
