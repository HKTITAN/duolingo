---
name: duo-perceived-progress-rate-of-change-beats-absolute-position
summary: Motivation tracks how fast the number is moving, not where it sits; a tier wide enough to mean something is wide enough to look frozen.
metadata:
  internal: true
---

# Rate of Change Beats Absolute Position

## Concept

People do not judge their progress by where they are. They judge it by whether the marker moved since last time. A coarse tier — bronze/silver/gold, beginner/intermediate/advanced, plan level — is legible precisely because each band covers a lot of ground, and that is the same property that makes it sit still for months at a time. During those months the user is working and the interface is telling them nothing has happened.

That flat stretch is not evenly distributed across the lifecycle. It lands in the middle, which is exactly the interval where people quit. The fix is not to narrow the tiers until they are meaningless; it is to ship a fine-grained scalar alongside the coarse tier, with the next increment visible.

## What Duolingo does

Source: blog.duolingo.com/duolingo-score (Duolingo blog, 2024-10-23; accessed 2026-09-22)

- Duolingo shipped the **Duolingo Score**, a **0-160 scalar** displayed next to the course flag, with a **progress bar showing distance to the next point**. Launched in 2024 for Spanish, French and English learners, and unlocked only **after the learner completes Unit 1** — there is no score to stare at before there is data to compute it from.
- **Most advanced courses top out around 120**, the end of the CEFR B2 band. The scale is deliberately not normalised to 100, and the ceiling is not the top of the scale.
- The stated reason for building it is the granularity problem itself. Duolingo frames the score against CEFR levels, which "cover a broad range of material (sometimes multiple sections of your course!)" — a band a learner can occupy through many weeks of real work without the label ever changing.
- The score does **not replace the tier**. It is shown next to the coarse standard, so the user gets a number that moves every session and a label that means something to other people.

**The tension.** A number that moves every session will keep moving through stretches where felt capability is flat, which buys motion at the cost of accuracy. See [[a-portable-number-in-can-do-terms]] for what that divergence costs and how to talk about it.

## The transferable pattern

- Your status tiers are for communication. Your scalar is for motivation. They are different instruments and you generally need both — do not make one do the other's job.
- The design test for a progress display is not "is this accurate?" but "does this move within one session of ordinary use?" If the answer is no, the user's effort is going into a black box.
- Show the **delta and the next increment**, not only the current value. A bar to the next point converts an abstract quantity into a near target.
- Withhold the scalar until you have enough signal to make it non-random. An early number that jumps around teaches users the metric is noise, and that lesson does not wear off.
- Pick a ceiling that reflects your actual content, not a round number. A scale most users can max out stops working the moment they do.

## Apply to your product

- Open your product as a two-month-old account. What on the screen is numerically different from yesterday, and would the user notice without being told?
- What is the longest period a committed user can spend without any visible marker changing, and how does that interval line up with your churn curve?
- If you added a fine-grained score tomorrow, what would it be computed from — and would it still move on a day when the user did the smallest real unit of work?

## See also

[[a-portable-number-in-can-do-terms]] · [[shorten-the-unit-of-completion]] · [[../duo-gamification/references/xp-system]] · [[../duo-progression-design/references/borrow-an-external-standard-as-the-spine]]
