---
name: duo-backend-architecture-hold-the-lock-only-over-shared-work
summary: Lock duration, not transaction rate, is usually what is killing you — move network calls and computation outside the critical section.
metadata:
  internal: true
---

# Hold The Lock Only Over Shared Work

## Concept

Contention is hold time multiplied by request rate. You rarely control the rate; you almost always control the hold time. The common failure is a critical section that opens, then does everything — network calls, computation, lookups, business logic — and only at the very end touches the shared resource it was protecting. Worse, once the store spends meaningful time just tracking who holds what, lock bookkeeping crowds out real work and the system degrades faster than traffic grows. The fix is to shrink the section to the write itself: read without a lock, do all the thinking outside, and at write time verify that nothing you read has changed.

## What Duolingo does

Source: blog.duolingo.com/optimistic-locking (Duolingo blog, 2025-12-22; accessed 2026-09-22)

- Duolingo's notification scheduler locked a user's row and then, still holding the lock, made network calls for user details such as streak length — **over half of a transaction that could take up to ten seconds**.
- They moved to optimistic locking: read unlocked, build the new schedule, compare a **version ID** at write time, retry if it moved. Every network call now happens outside the critical section.
- Transactions to update reminders fell from **~16ms to under 1ms**. Notification delays of **over 20 minutes** were eliminated. The change saved **over $100K/year** in database resources, at a volume of **hundreds of millions of notifications per day**.
- **The tension they measured first.** Optimistic locking *raised* commit load, because it cannot batch transactions, and it introduces wasted work from retries. Overall load still fell and retries turned out to be rare — but both were real costs, and both were quantified before the switch.
- **The business case was a nickname.** The team routinely sat watching metrics during peak traffic on Saturday mornings around 10 a.m. Eastern, ready to intervene. They called it "watching the Saturday morning cartoons." A recurring ritual with a name is a standing bug report — the labor absorbs the defect so completely that it never appears in incident counts.

## The transferable pattern

1. **Measure hold time, not lock count.** The question is not how many transactions you run; it is how many milliseconds each one keeps others waiting.
2. **Nothing inside the critical section may touch the network.** A remote call inside a lock couples your contention to somebody else's latency and somebody else's outage.
3. **Move from pessimistic to optimistic where writes rarely collide.** Read freely, compute freely, then commit conditionally on a version stamp and retry on conflict. This is a bet that collisions are rare — so measure the retry rate rather than assuming it.
4. **Price the ritual.** If people manually babysit the system on a predictable schedule, that recurrence is proof the failure is structural, not random, and the hours are the funding argument for fixing it.
5. **Expect the load to move, not vanish.** Removing held time usually shifts cost elsewhere — more individual commits, retried work, extra round trips. Find where it lands and confirm the total actually fell.

## Apply to your product

- In your longest-running transaction, what fraction of the held time is spent on work that does not touch the shared resource at all?
- Do you know your write-conflict rate on the rows you contend for — measured, not estimated? If not, that number is the precondition for going optimistic.
- What does your team do by hand, on a schedule, to keep a system upright — and has anyone ever converted those hours into a cost?

## See also

[[instrument-the-failure-mode-you-traded-into]] · [[delete-dependencies-from-the-request-path]] · [[../duo-culture/SKILL]]
