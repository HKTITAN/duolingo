---
name: duo-gamification-ramp-up-difficulty
summary: Difficulty calibrated to keep users in flow state — never too easy, never a wall.
metadata:
  internal: true
---

# Ramp-Up Difficulty

## Concept

Flow state (Csikszentmihalyi) is the band between boredom (too easy) and anxiety (too hard). A learning product is most engaging when it spends most of the user's session in that band. Pacing is the engineering: harder content arrives just as the user is ready, not before, not after.

## What Duolingo does

Duolingo's stated target is Krashen's **i + 1** — input just slightly beyond what the learner already has — which they map onto Vygotsky's zone of proximal development. The curve is specified in numbers, not vibes. Source: blog.duolingo.com/right-level-of-difficulty (Duolingo blog, 2024-04-02; accessed 2026-09-22)

- **5–7 new words per lesson.** Everything else in the sentence is already-taught vocabulary, so the unfamiliar share stays inside what's decodable.
- **90/10 in Stories.** Learning designers hold 90% of a story to known vocabulary and grammar; the remaining 10% is new and has to be guessed from context. Anything harder to guess gets a check-the-meaning exercise attached.
- A new concept introduces with high-context exercises (recognize the word) before requiring full production (type it out yourself).
- The path interleaves review nodes with new content so learners hit older material at calibrated intervals.
- Difficulty is calibrated per learner by **Birdbrain**, a model that predicts whether a specific learner will get a specific exercise right, and feeds that to the lesson generator. It reached 20%+ of lessons personalized within seven months of launch. Source: blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain (Duolingo blog, 2020-10-07; accessed 2026-09-22)

Duolingo names both failure modes explicitly: "i + 20" content discourages and loses the learner, "i + 0" content stagnates and bores them.

## The transferable pattern

Three rules:

1. **Introduce before testing.** Every new concept gets a low-stakes first encounter before it's required for completion.
2. **Reset the floor at each grouping.** A new unit shouldn't start at the previous unit's end-difficulty; users need a runway.
3. **Calibrate by data, not gut.** "This feels right" produces curves designed for the designer, not the median user. Use completion rate as the primary signal.

A useful starting ratio, borrowed from Duolingo's Stories spec: **~90% of any unit of content should be material the user has already met, ~10% new.** That is a concrete, checkable target — unlike "make it challenging but not too hard.

## Apply to your product

- Does your product have a difficulty/complexity curve, or does every user hit everything at full force from day one?
- If you have a curve, do you measure success rate per stage?
- Where is the first wall a typical user hits? Should it be there?

## See also

[[xp-system]] · [[progression-design]] · [[anti-grind]] · [[../duo-experimentation/references/metric-selection]]
