---
name: duo-inclusive-access-escape-hatches-at-the-granularity-of-the-blocked-modality
summary: Put the opt-out at the level of the blocked capability, not the session, and build it into completion rules rather than the renderer.
metadata:
  internal: true
---

# Escape Hatches at the Granularity of the Blocked Modality

## Concept

When an entire input or output channel is inaccessible to a slice of your users, making content that depends on it mandatory does not make those users practise it. It makes the product unusable and they leave. The fix is an escape hatch sized to the blockage: not "quit this session", not "restyle this screen", but "skip this *kind* of task" — for now, or permanently — without losing progress or the habit you have built with them.

The hard part is where the hatch lives. A presentation-layer accommodation assumes everyone can still perform the underlying task and only needs it presented differently. When the barrier *is* the task, the opt-out has to exist in the completion rules — what counts as finished, what unlocks the next thing — rather than being bolted onto the renderer.

## What Duolingo does

Source: blog.duolingo.com/learning-with-hearing-aids (Duolingo blog, 2026-01-20; accessed 2026-09-22)

- The WHO estimate Duolingo cites for scale: **1.5 billion people, nearly 20% of the global population**, live with hearing loss.
- Four graduated hatches for audio content, not one:
  1. **"Can't listen now"** skips all listening exercises inside that single lesson.
  2. DuoRadio lessons offer **"Do this later"** and are never required to progress.
  3. A **settings toggle** disables listening exercises entirely, across the product.
  4. The Practice Hub offers a **listening-only lesson** for when the user does want to work on exactly that.
- None of the four costs progress or the streak.
- Tension: a user who disables a modality is opting out of a skill they came to build. Duolingo re-prompts them to re-enable listening if they enter the listening-only practice — the opt-out is honoured, but it is not treated as a permanent verdict on the person.

Source: blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-listening-skills (Duolingo blog, 2026-05-05; accessed 2026-09-22)

- Learners with hearing impairment can reduce or entirely skip listening-based exercises **without blocking course progress**, and listening and speaking exercises each have their own on/off setting. The accommodation sits in what the curriculum requires, not in how a screen is drawn.

## The transferable pattern

Inventory your product by the capability each task demands of the person — seeing, hearing, speaking, fine motor control, sustained attention, a quiet room, a fast connection. Wherever one of those is load-bearing for a whole class of task, that class needs its own exit, and the exit needs three properties: it is reversible, it is available at more than one grain (this instance, and always), and it costs the user nothing they have accumulated.

Then check where the exit is implemented. If turning it on only changes what renders while the completion requirement stays put, you have built a decoration. The structural version changes what "done" means. Offer a way back too — a dedicated place where the skipped capability is the whole point — so opting out is a state the user controls rather than a door that locks behind them.

## Apply to your product

- Which of your required steps depends on one specific human capability? What happens today to a user who does not have it — do they stall, or do they exit?
- Is your accommodation a change of appearance or a change of rules? Trace one: does the progress gate still check the thing you claim to have waived?
- If a user turns a whole category off, how do they turn it back on later when their situation changes — and does anything in your product ever ask?

## See also

[[route-around-the-block-dont-only-remove-the-step]] · [[scaffolding-belongs-on-a-user-controlled-switch]] · [[../duo-design/references/accessibility-default]]
