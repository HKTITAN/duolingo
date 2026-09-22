---
name: duo-difficulty-calibration-opt-in-hard-mode-priced-higher
summary: Ship the unassisted version as an opt-in transform of a task the user already knows, and pay it several times more than the scaffolded version.
metadata:
  internal: true
---

# Opt-In Hard Mode, Priced Higher

## Concept

Scaffolds — hints, autocomplete, multiple choice, visible answers, templates — make a task easier and the resulting capability weaker. The user practices recognizing rather than producing. The obvious fix, raising the baseline difficulty for everyone, fails: the identical constraint that is productive for a user who chose it reads as the product being broken to a user who did not. Imposed difficulty is a defect; accepted difficulty is training.

So the unassisted version has to be a **transform the user applies to a task they already understand** — same content, supports removed, taken at the moment they have capacity for it. And because the harder version costs more effort for the same visible output, it has to be paid more, or nobody picks it. The size of the premium is the whole design: a small bonus reads as a rounding error and the scaffolded path stays dominant.

## What Duolingo does

Source: blog.duolingo.com/ways-to-practice-in-duolingo (Duolingo blog, 2025-12-16; accessed 2026-09-22)

- **Legendary Levels** re-run an already-completed node with harder exercises and **no hints**; the node turns gold on completion.
- The pricing is the mechanism: a plain review of a completed node earns **5 XP**; the Legendary lesson on the **same node** earns **40 XP** — an **8x premium** purely for removing the supports.
- The same body of content has several doorways with different reward shapes: timed formats (Side Quests, Match Madness) and a mistakes-only practice lane in the Practice Hub.

Source: blog.duolingo.com/sneaky-pronunciation-practice (Duolingo blog, 2023-06-28; accessed 2026-09-22)

- The dictation microphone lets a learner voluntarily upgrade a low-pressure typing exercise into a **speaking** one. Duolingo notes the spoken version is harder — it carries time pressure and demands faster retrieval — and frames that added difficulty as the point, not a side effect. It is a per-instance toggle on a task the user already knows how to do.

Source: blog.duolingo.com/review-exercises-help-measure-learner-recall (Duolingo blog, 2021-12-02; accessed 2026-09-22)

- Only the easiest tier of each unit was required to advance, and learners who did the optional next tier were **significantly more likely to recall that content later**.
- **The tension.** That is also the failure: if the depth is optional and merely available, most users stop at the mandatory tier and forget. Optional is not a strategy on its own — it only works when the harder tier is visible, legible and paid well enough to compete with the easy one. And a large enough premium starts selecting for users who want the reward rather than the capability, which is a different failure.

## The transferable pattern

Ship difficulty as a user-applied transform with a price attached.

1. **Enumerate your scaffolds.** Autocomplete, suggested options, a visible reference, a retry with the answer shown, a template. Each one is a support, and each one has an unassisted counterpart you are not currently offering.
2. **Make the hard version a toggle on a known task, not a new task.** The user should already understand what is being asked; the only change is that the help is gone.
3. **Price the premium large enough to notice.** Several times the baseline reward, not a few percent. If the easy path is still the efficient way to accumulate whatever your product counts, the hard path is decoration.
4. **Keep the scaffolded path fully legitimate.** It serves newcomers and low-capacity days. The hard mode is an addition, never a replacement.
5. **Make the depth visible from the easy tier.** A user who cannot see the rung above will never reach for it. See [[users-will-grind-what-they-already-know]].

## Apply to your product

- List every hint, suggestion and autocomplete in your core flow. Which of them could become optional, and what would the unassisted version look like?
- What is your reward currency, and what multiple would make the harder path the rational choice for a committed user? Is your current bonus anywhere near that?
- Is your harder tier discoverable from inside the easy one, or does a user have to already know it exists?

## See also

[[let-users-pick-the-rung]] · [[users-will-grind-what-they-already-know]] · [[train-above-the-real-load]] · [[../duo-progression-design/references/make-the-scaffold-removable-by-the-user]] · [[../duo-gamification/references/xp-system]]
