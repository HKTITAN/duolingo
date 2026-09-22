---
name: duo-inclusive-access-let-the-user-own-the-turn-boundary
summary: Silence-threshold turn detection cuts off exactly the hesitant users a conversational feature exists to serve — give them explicit control of when their turn ends.
metadata:
  internal: true
---

# Let the User Own the Turn Boundary

## Concept

Automatic turn detection in a conversational interface usually works by waiting for silence. That design assumes the pause means *I am finished*. For a confident, fluent user it usually does. For a slow, uncertain or non-fluent user — the exact person the feature was built to help — a pause means *I am thinking*, and the system interrupts them mid-sentence.

The damage compounds. First the user learns to rush, which makes their output worse and the interaction more stressful. Then they learn to avoid the feature entirely, and you lose the population whose need justified building it. A push-to-talk style control fixes this by converting an unpredictable, system-owned time limit into space the user owns. That is generally what makes a stressful interaction attemptable at all: not removing the difficulty, but removing the ambush.

## What Duolingo does

Source: blog.duolingo.com/product-highlights (Duolingo blog, 2025-12-10; accessed 2026-09-22)

- Duolingo added **Push-To-Talk** to Video Call with Lily, framed as giving learners more breathing room to respond and stopping Lily from interrupting them mid-sentence.
- Alongside it, two audience-specific moves: **captions** and **post-call actionable feedback** for beginners, and **longer, more steerable calls** for advanced learners. The same feature is tuned differently by confidence level rather than shipped as one setting.
- Reach at the time of the post: Video Call extended to **Android** across **8 languages**.
- Note the direction of the fix. The interaction was not made shorter or easier; the unpredictable part of it was handed to the user. The difficulty stayed where it was.
- Tension worth naming: the calls are gamified with an **XP goal that is reached faster with longer responses**. That is a nudge toward verbosity, not toward the most useful thing to say. An access improvement and an engagement incentive were shipped into the same surface, and they pull in different directions.

## The transferable pattern

Anywhere your product decides that a user's input is finished, ask who owns that decision and what happens when the system gets it wrong. Timeouts, auto-advance, auto-submit, silence detection, idle logout, "are you still there" — each is a system-owned boundary, and each one misfires against slower users in a way that reads to them as being cut off rather than as a bug.

The population this hurts is invisible in aggregate metrics, because the people it hurts most stop using the feature and therefore stop generating events in it. A completion rate that looks healthy can be the average of a fluent group who never trip the threshold and an absent group who left.

Give the boundary to the user wherever the cost of doing so is bounded. The point is not extra time; it is *predictable* time, because an unpredictable limit forces people to spend attention monitoring the clock instead of on the task. Then check what you have attached to the interaction: an incentive that rewards length, speed or volume will bend behaviour toward that metric and can undo the calm the control was supposed to create.

## Apply to your product

- Where does your product decide the user is done? What is the failure mode for someone who is slower than your threshold, and would they read it as their fault?
- Can you hand that boundary to the user without unbounded cost? If not, can you at least make the remaining limit visible and predictable?
- What reward is attached to that interaction, and what behaviour does it actually maximise — the useful one, or a proxy?

## See also

[[working-memory-is-already-spent-elsewhere]] · [[a-slow-decomposed-version-is-not-the-answer-key]] · [[../duo-gamification/SKILL]]
