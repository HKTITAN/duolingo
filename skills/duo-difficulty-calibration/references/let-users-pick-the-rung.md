---
name: duo-difficulty-calibration-let-users-pick-the-rung
summary: Expose difficulty as a few orthogonal toggles with explicit labels on each combination, and let open-ended tasks self-calibrate where no model can reach.
metadata:
  internal: true
---

# Let Users Pick the Rung

## Concept

A model inferring capacity from past behavior is always slightly out of date and knows nothing about today — the user's energy, their available attention, whether they want to be stretched right now. The user knows all of that. Where the cost of asking is low, asking beats inferring.

But a difficulty slider labelled "easy / medium / hard" is close to useless, because the user cannot tell what those words mean in your product until after they have chosen. The version that works exposes a small number of **orthogonal** controls whose meaning is concrete, crosses them into a handful of named combinations, and puts an explicit difficulty rating on each one. That turns difficulty into a visible ladder: the user can see there is a rung above them instead of walking off an unmarked cliff, and the rung has a name they can aim at.

The second route needs no controls at all. In an open-ended task, the user decides how much to attempt — so the task calibrates itself to whatever they can currently do, and the gap between what they reach for and what they avoid is a diagnostic you get for free.

## What Duolingo does

Source: blog.duolingo.com/language-practice-with-tv-movies (Duolingo blog, 2023-03-16; accessed 2026-09-22)

- For learning from television, Duolingo crosses **two dials** — audio language and subtitle language — into **five named setups**, each carrying an explicit bracketed difficulty rating: build reading [easy], improve listening [medium-to-hard], immerse [hard], watch like a local with no subtitles [even harder], and target-language audio against a *third* language's subtitles, flagged as an alarm-level tier.
- Each setup carries its own tip for how to stretch **within** that rung, so the ladder has depth as well as steps.
- **The tension.** Two dials produce a clean five-rung ladder precisely because they are few. Add a third control and the labelled combinations stop being enumerable, the ratings stop being comparable, and you are back to an unlabelled slider with more work.

Source: blog.duolingo.com/right-level-of-difficulty (Duolingo blog, 2024-04-02; accessed 2026-09-22)

- Some Spanish and French Stories end with an **open-ended writing exercise** where the learner decides how much to say and which words and structures to use — described as giving a peek into your own current level. Max subscribers get the same self-calibrating shape in Roleplay, an open text conversation about topics from their lessons.
- The reason this measures something a multiple-choice item cannot: constrained tasks measure recognition; open production measures what the user can generate with no scaffolding at all.

## The transferable pattern

Two complementary ways to let the user set the level.

1. **Find the orthogonal dials.** Most products have two or three independent things that make a task harder — how much is given, how much time there is, how much must be produced rather than selected. Those are your axes.
2. **Cross them and name the combinations.** A small enumerated set of named setups beats a continuous slider, because each one can carry a concrete description of what it will feel like.
3. **Label each rung with an explicit difficulty rating.** The rating is the part that makes the ladder legible; a name without a rating is just a preset.
4. **Keep the count small.** Fewer than a handful of rungs, from two or three dials. The value comes from being enumerable.
5. **Use open-ended output where you can afford to grade it.** An unconstrained task self-calibrates with no model, and what the user attempts versus avoids is a capability signal you cannot get from selection-based tasks.
6. **Treat the user's pick as evidence, not a replacement for your model.** What they choose is fresh information about today. Feed it back. See [[model-the-item-and-the-user-jointly]].

## Apply to your product

- What are the two or three independent things that make your core task harder? Are any of them already exposed to the user, and are they labelled?
- If you offered five named configurations of your main flow, what would the hardest one be, and would anyone pick it?
- Is there anywhere a user can produce something open-ended rather than choose from options? What would that tell you about them that your current events do not?

## See also

[[opt-in-hard-mode-priced-higher]] · [[model-the-item-and-the-user-jointly]] · [[escalate-at-the-tail-not-the-start]] · [[../duo-learner-motivation/references/flag-the-stretch-goal-as-a-stretch]]
