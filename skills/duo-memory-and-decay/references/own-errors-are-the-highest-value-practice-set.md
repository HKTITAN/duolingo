---
name: duo-memory-and-decay-own-errors-are-the-highest-value-practice-set
summary: A session assembled from this person's recorded failures spends every slot at their frontier; a population-average review set wastes most of them.
metadata:
  internal: true
---

# Own Errors Are the Highest-Value Practice Set

## Concept

A mistake marks the exact boundary between what a user has and has not mastered. That makes their own error history the highest-information practice set you own — every item in it is, by construction, something they could not do.

Compare the alternative. A shared review set built from population averages re-tests things most individuals already hold. Two users who completed identical content have different residual weaknesses, so a common set wastes most of its slots. Selecting by personal error history concentrates every slot inside that person's frontier.

There is a second effect that is not about information at all. Having erred on something primes attention to that pattern when it reappears. And labelling the item as known-weak changes its meaning: the difficulty is expected and system-flagged rather than evidence that the user is failing.

## What Duolingo does

Source: blog.duolingo.com/keeping-you-at-the-frontier-of-learning-with-adaptive-lessons (Duolingo blog, 2020-05-26; accessed 2026-09-22)

- **Mistakes practice** sessions are assembled from the exact errors a learner made across the whole course, reachable from the hearts menu, and framed to the learner as evidence they are at their frontier rather than as failure.
- Personalized practice is embedded directly in the path, not parked in a separate review area. The app tracks what each learner is struggling with and builds a session from their weakest items, marking exercises **"WEAK WORD" in orange**. Everyone sees something different (blog.duolingo.com/right-level-of-difficulty (Duolingo blog, 2024-04-02; accessed 2026-09-22)).
- The low-tech version of the same loop, published as a protocol for language-exchange partners: keep a running log of failures as they happen — the moment the other person did not understand, the sentence that stalled halfway. Then in the session, pick **one logged item**, have the partner fix it, write down or record the response, practise at home, and **use the new sentence in a conversation within that week** (blog.duolingo.com/3-tips-to-level-up-your-next-language-exchange (Duolingo blog, 2024-02-28; accessed 2026-09-22)).

**The tension.** An error-only set is relentless — by design it never shows the user anything they can do. That is efficient and demoralizing at the same time, which is why the labelling and framing are load-bearing rather than cosmetic. It is also fragile in a cold start: a user with no error history has no set, and one with a bad first week can be handed a session that is nothing but their worst moments.

## The transferable pattern

Failures are near-free to capture at the moment they occur and very expensive to reconstruct later. Most products throw them away.

1. **Persist every failure as a first-class record**, attached to the user and the item, not just as a transient error state.
2. **Make "work through my own failures" an entry point**, not a filter buried in settings. The log is the feature.
3. **Label the item in the interface.** Telling the user this one is flagged as weak reframes difficulty as expected, and makes the personalization visible instead of spooky.
4. **Spend scarce expensive attention only on logged items.** Where a human expert, a support call or a review meeting is in the loop, the log converts unstructured time into targeted throughput — otherwise the agenda defaults to whatever the expert felt like covering.
5. **Close with a forced use.** A correction that is only written down is a note. Require one real use inside a bounded window and it becomes retrieval in context.
6. **Dilute deliberately.** Mix in items the user reliably gets right. The efficiency argument says never do this; the completion rate says otherwise.

## Apply to your product

- Do you store your users' failures, or only their successes? If someone asked for "everything I got wrong this month," could you produce it?
- Where does a scarce expert currently spend time on an agenda nobody derived from data? What would that hour look like driven by a failure log?
- After you show a user a correction, what forces them to use it once? If nothing does, you have delivered information, not practice.

## See also

[[delay-the-retry-and-weight-the-queue]] · [[three-conditions-for-practice-to-pay]] · [[../duo-retention/references/churn-diagnostics]]
