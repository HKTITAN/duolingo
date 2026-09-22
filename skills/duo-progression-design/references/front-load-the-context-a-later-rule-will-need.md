---
name: duo-progression-design-front-load-the-context-a-later-rule-will-need
summary: Plant cheap contextual material early so a hard rule can be induced from examples later instead of asserted.
metadata:
  internal: true
---

# Front-Load the Context a Later Rule Will Need

## Concept

A rule the user derives from examples is stored together with the evidence that supports it, so it generalizes to cases you never showed them. A rule that is asserted has to be held on faith and is retrieved only when the user happens to remember it exists. The difference is not in how the rule is worded — it is in whether the user had enough material on hand to notice the pattern themselves. That material has to be planted earlier, deliberately, in a unit whose apparent purpose is something else. Front-loading cheap contextual content is what makes induction possible at the moment the hard concept arrives.

Note the boundary: this node is about *where the supporting evidence sits in the sequence*. Whether the rule ever gets written down, and in what compressed form, is a separate decision that belongs to the rules-and-heuristics skill.

## What Duolingo does

Source: blog.duolingo.com/what-makes-arabic-hard-and-why-that-shouldnt-stop-you-from-learning-it (Duolingo blog, 2026-04-27; accessed 2026-09-22)

- The Arabic course teaches **a wide range of Arabic first names in its earliest lessons** — material that looks like ordinary beginner vocabulary and is cheap to learn — specifically so that, **units later**, gendered verb forms can always be introduced alongside a disambiguating name.
- The payoff: the feminine verb arrives in أين تسكنين يا رانيا؟ (Rania) and the masculine in أين تسكن يا عمر؟ (Omar). The name does the disambiguating work, so the learner internalizes the gender pattern **without a grammar lecture**. The early lesson was a setup for a lesson several units downstream.
- The scaffold is allowed to be **unfaithful to the real system** if the distortion removes load that is not part of what you are teaching. Duolingo's example: Mexican students write each level of a Mayan numeral (**1s, 20s, 400s**) in a **different color** to keep the place values distinct — **even though the actual Mayan system used a single color throughout**. The color is a redundant cue that marks the structure, freeing working memory for the operation being learned, and it can be dropped once the structure is internalized, so nothing is permanently mis-taught (blog.duolingo.com/mexican-students-math-class-hieroglyphics (Duolingo blog, 2023-11-21; accessed 2026-09-22)).

## The transferable pattern

Work backwards from the concepts you know are hard. For each one, ask: *what would a user need to already have in hand for this pattern to be obvious from three examples?* Then find a place early in the sequence to plant that material under its own pretext, where it is cheap and looks like ordinary content.

The mechanics:

- **Plant cheap, harvest expensive.** The front-loaded material should be low-effort and independently useful, so it does not read as a detour. Its real job is invisible until later.
- **Design the example set so the pattern is forced.** At the moment of introduction, the examples must differ on exactly one dimension — the one you want noticed. Vary two and the user induces nothing, or induces the wrong thing.
- **A deliberate distortion is permitted if it is removable.** Adding a redundant cue that marks structure the real system does not mark is fine when it offloads something that is not the target skill, and when you can strip the cue later. Permanent distortions are lies; temporary ones are scaffolding.
- **Audit for orphaned hard concepts.** Any concept currently introduced by assertion, with no earlier material supporting it, is one that will be held on faith and forgotten.

## Apply to your product

- Take the three concepts your users most often get wrong. What cheap material, planted five steps earlier, would let each one be inferred rather than announced?
- At the moment each hard concept appears, do your examples vary on one dimension or several?
- Which of your simplifications are unfaithful to the real system? For each, is the distortion removable later — and have you scheduled the removal?

## See also

[[sequence-by-task-not-by-taxonomy]] · [[make-the-scaffold-removable-by-the-user]] · [[recognition-then-guided-then-production]] · [[scaffold-and-fade-on-a-schedule]]
