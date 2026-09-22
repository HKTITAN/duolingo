---
name: duo-memory-and-decay-delay-the-retry-and-weight-the-queue
summary: An immediately re-served item is answered from working memory and teaches nothing; hold the retry, and order the queue on recency and error together.
metadata:
  internal: true
---

# Delay the Retry, Weight the Queue

## Concept

Two scheduling decisions sit right next to each other and are usually both made badly.

The first is **when to retry a failed item**. The intuitive answer — show it again right now, while the correction is fresh — is the one that destroys the signal. An item re-served seconds after its correction is answered out of working memory. The user passes, the product records a success, and no long-term retrieval ever occurred. The retry looks like it worked; it measured the buffer, not the memory.

The second is **what to pull next**. Interval alone assumes every item decays at the same rate, which is exactly the assumption an error disproves. A wrong answer is direct evidence that this item's trace is weaker than its age implies. Recency and accuracy are two independent signals, and a queue that uses only one of them is discarding half its information.

## What Duolingo does

Source: blog.duolingo.com/spaced-repetition-for-learning (Duolingo blog, 2023-12-26; accessed 2026-09-22)

- Mistakes made during a lesson are re-served **at the end of the lesson**, not in place — described explicitly as taking advantage of "a little spaced repetition." Even a few minutes of intervening work is enough to force a real retrieval instead of a buffer read.
- Practice-lesson selection uses spaced repetition **along with accuracy**. The learner-facing version of the rule is stated directly: review things you got wrong sooner, and wait longer to review concepts you got right.
- The same error is scheduled more than once at more than one horizon. Duolingo tracks each learner's mistakes, resurfaces them at the end of the lesson, and then **weights that topic more heavily in later personalized practice** — so a failure buys both a near-term retry and a long-term priority bump (blog.duolingo.com/mistakes-in-spanish-for-learners (Duolingo blog, 2023-11-06; accessed 2026-09-22)).
- Aggregate error data feeds a separate lane: the same post is built from the **top 5 mistakes English speakers make in Spanish**, and the app shows a quick tip for the most common ones. Population errors drive content; personal errors drive scheduling.

**The tension.** Delaying the retry costs you the moment of maximum user attention. The user cared about that mistake when it happened; by the end of the session they may have moved on, and some will quit before the retry arrives. A delayed retry that never happens is worth nothing, so the delay has to fit inside a session the user reliably finishes — which is an argument for short sessions, not long ones.

## The transferable pattern

1. **Put a gap between a correction and its test.** Any gap filled with other work beats no gap. End-of-session is a cheap, reliable place to put it.
2. **Distrust a pass that follows immediately from a reveal.** Instrument it separately from a cold pass; they are different events and averaging them inflates your numbers.
3. **Order the queue on at least two signals** — time since last exposure *and* observed performance. An item failed yesterday outranks an item passed three weeks ago.
4. **Give a failure two lives.** One near-term retry to confirm the correction landed, one long-horizon priority bump to confirm it survived.
5. **Separate the population signal from the personal one.** Common failures tell you what to fix in the product or explain better. This user's failures tell you what to show this user next. Do not let one impersonate the other.

## Apply to your product

- When a user gets something wrong, how long until you ask again? If the answer is "immediately," what are you actually measuring?
- Does your resurfacing queue know how the user performed, or only when they last saw the item?
- What is your session completion rate? If it is low, an end-of-session retry is mostly a retry that never runs.

## See also

[[own-errors-are-the-highest-value-practice-set]] · [[per-item-half-life-not-a-fixed-ladder]] · [[retrieval-not-re-exposure]]
