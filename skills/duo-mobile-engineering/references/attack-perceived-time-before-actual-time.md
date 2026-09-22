---
name: duo-mobile-engineering-attack-perceived-time-before-actual-time
summary: When a blocking operation is genuinely unavoidable, render the screen you were going to show next and do the work behind it.
metadata:
  internal: true
---

# Attack Perceived Time Before Actual Time

## Concept

The cost the user pays is the felt wait, not the elapsed milliseconds. Those two numbers can be decoupled, and decoupling them is usually far cheaper than removing the blocking work — which may be genuinely unavoidable, or may require a backend rewrite you cannot fund this quarter.

A spinner is the worst possible thing to show, because a spinner is an explicit admission that nothing is happening. Content is better, and the best content is the thing you were always going to show next. Duolingo's own analogy is the elevator door-close button: it frequently does nothing, and pressing it still makes the wait tolerable.

This is not a trick played on the user, as long as the underlying work really does complete and failures really do surface. It is a reordering: the moment of acknowledgment moves to the tap, and the machinery runs behind something worth looking at.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- At session end the app made a **blocking call to submit data and fetch all end-of-session screens**, showing a **full-screen spinner** while it ran.
- The change: show the **"Session Complete!" screen with fireworks immediately on tap**, and submit the data and prepare the following screens behind it. The blocking work was not removed — it was hidden behind content the user wanted anyway.
- Measured result: **60%+ reduction in perceived session end latency**, plus a **significant increase in DAUs and total sessions completed**.
- Duolingo explicitly frames this as the cheap move relative to actually removing the block, and puts it in the same programme as the conversion guardrail described in [[optimize-against-conversion-not-milliseconds]].

The tension: this technique buys you the option of *never* fixing the underlying latency, and that option is easy to exercise forever. It also complicates error handling — the user has already been told they succeeded, so a failure behind the celebration has to be recovered rather than reported. Neither cost is a reason to skip it; both are reasons to keep the real latency on a dashboard after you have hidden it.

## The transferable pattern

- **Separate the two numbers explicitly.** Actual duration and perceived duration are different metrics with different fixes. Track both, or you will keep spending engineering on the one that is harder and matters less.
- **Ask what you were going to show next anyway.** Confirmation, summary, celebration, the next form step — rendering it immediately costs nothing and occupies attention with something the user values.
- **Prefer optimistic acknowledgment to indeterminate progress.** An indeterminate spinner conveys no information and reads as a stall. A determinate one at least conveys motion.
- **Budget for the unhappy path first.** If the hidden work can fail, decide now how the user learns about it, because the confirmation already shipped.

## Apply to your product

- Where in your product does a user tap something and then look at a spinner? What screen were you going to show them one second later, and why are they not seeing it now?
- If the hidden work fails, how does the user find out — and is that recovery path designed, or is it a toast nobody has read?
- Which of your latency complaints are actually about waiting without information rather than about waiting?

## See also

[[optimize-against-conversion-not-milliseconds]] · [[defer-everything-the-first-screen-doesnt-need]] · [[../duo-gamification/references/celebration-moments]]
