---
name: duo-ai-agent-platform-every-producer-needs-a-janitor
summary: An automated producer needs an automated janitor with a retry cap, a staleness deadline and a cooldown, or the system re-attempts its own failures forever.
metadata:
  internal: true
---

# Every Producer Needs a Janitor

## Concept

An automated producer creates items. Some of those items will never succeed. Without a second process whose only job is to clean up, the failures accumulate in the same queue as the successes and quietly poison it.

The janitor needs three explicit give-up rules: a **retry cap**, a **staleness deadline**, and a **cooldown** that stops the producer from immediately regenerating what was just abandoned. The cooldown is the one people forget, and it is the one that matters most — without shared state between producer and janitor, closing a doomed item is not a decision, it is a loop.

Note the asymmetry: give-up rules are not uniform. Some failure modes are worth an immediate retry from a clean state; others are worth a month of silence. The janitor's value is in telling them apart.

## What Duolingo does

Source: blog.duolingo.com/ai-ios-unit-test-generation-pipeline (Duolingo blog, 2026-06-24; accessed 2026-09-22)

A PR lifecycle workflow runs **hourly** over every open generated PR and applies a decision tree:

- **Merge conflict** → close immediately, with **no cooldown**, since regenerating from a clean main branch will work.
- **Open more than 14 days** → close, with a **30-day cooldown** on that file.
- **CI green and no reviewer** → assign a reviewer via `git blame` and enable auto-merge.
- **CI red past 5 retries** → close, with a **30-day cooldown**.
- **CI red under the cap** → trigger a fix-CI agent and let it try again.

State lives in per-file and per-PR JSON records in object storage, deliberately chosen over a database — the producer reads the same records the janitor writes, which is what makes a cooldown mean anything. In the most recent batch, **13.6% failed**, the vast majority from lint violations, with **two lint rules alone causing 62%** of those failures.

**Tension.** That dominant failure mode is a consequence of an infrastructure choice, not of model quality — because the workers run on Linux, the agent cannot compile or lint the platform-specific code it writes before opening the PR. The janitor is cleaning up after a gap in the producer's environment. Worth naming, because the tempting fix is a better prompt, and the real fix is giving the producer the ability to check its own work.

## The transferable pattern

For any process that automatically creates work items, write down the give-up rules before you turn it on:

1. **Retry cap** — the number of attempts after which this item is declared dead.
2. **Staleness deadline** — the age at which an item is closed regardless of state, because an untouched item is consuming attention, not earning it.
3. **Cooldown** — how long before the producer is allowed to recreate the same item. Zero is a valid answer for failures that were environmental, and only for those.
4. **Shared state** — one record both processes read and write. Without it the cooldown does not exist, no matter what the policy document says.

Then read the failure distribution. If a small number of causes dominate, the answer is usually to give the producer the ability to detect them before it publishes — not to make the janitor smarter.

## Apply to your product

- What does your system do with an item that has failed five times? If the answer is "try again", you do not have a give-up rule, you have a loop.
- Where does the state that says "we already gave up on this" live, and can the producer actually read it?
- In your current failure log, what share comes from the top two causes, and could the producer check for those itself before publishing?

## See also

[[model-an-agent-run-as-a-durable-workflow]] · [[verification-becomes-the-bottleneck]] · [[constrain-the-blast-radius-at-the-platform-layer]] · [[../duo-experimentation/references/kill-criteria]]
