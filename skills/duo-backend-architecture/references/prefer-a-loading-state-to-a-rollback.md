---
name: duo-backend-architecture-prefer-a-loading-state-to-a-rollback
summary: Check whether a plain loading state is acceptable before adopting optimistic UI — the complexity avoided is larger than the latency saved.
metadata:
  internal: true
---

# Prefer A Loading State To A Rollback

## Concept

Optimistic updates look like a pure latency win, so teams reach for them before asking the cheaper question: would a spinner have been fine? The thing prediction actually costs is duplication — both of state and of business logic — across client and server. The duplicated state is annoying; the duplicated *logic* is what compounds. A rule that starts as "add one" grows into real product logic with edge cases, and from then on it must be kept in sync across two implementations, every shipped app version, and every live experiment, forever. The speed win is paid for once. The divergence tax is paid every release. And there is no reusable rollback pattern waiting downstream to rescue you.

## What Duolingo does

Source: blog.duolingo.com/frontend-prediction (Duolingo blog, 2026-04-15; accessed 2026-09-22)

- Duolingo has shipped **all three rollback strategies** — never roll back, immediate rollback surfaced elsewhere in the interface, and deferred rollback on app restart — and reports **no clear winner**. Each carries its own jarring user moment or its own debugging cost.
- Their guidance is to **first ask whether waiting is acceptable**, and to treat prediction as a **per-feature decision tied to product context**, not a platform-wide architecture choice.
- **The honest counterweight, which is most of the post.** Prediction also buys real things: offline support, resilience to flaky networks, and decoupling from backend latency and from strict-consistency guarantees that get harder to hold as a system scales. The benefits are genuine — which is precisely why the costs get underestimated.
- Duolingo did not conclude "don't predict." It predicts a great deal. The conclusion is that the decision is per value and the default should be the simpler one.

## The transferable pattern

Run this order of questions before writing any optimistic path:

1. **Would a loading state be acceptable here?** If the wait is short, the action is deliberate, and the user is not mid-flow, the answer is usually yes. Take it and stop.
2. **What logic would have to exist in two places?** If the answer is "increment a number," the duplication is cheap. If it is "apply the current promotion rules," you are about to fork your product logic across two runtimes and every installed version.
3. **Which rollback policy will this value use, and who chose it?** Never correcting quietly leaves wrong data. Correcting immediately flickers. Correcting at restart means the user saw wrong data all session. Pick deliberately, per value.
4. **What else is prediction buying?** Offline capability and tolerance of unreliable networks may justify the machinery on their own. If they are not on your requirements list, latency alone is a thin reason.
5. **Re-ask per feature.** This is not an architectural stance to adopt once. It is a judgment made each time, against that feature's stakes.

## Apply to your product

- Which of your optimistic updates exist because the wait was genuinely unacceptable, and which exist because optimistic felt more sophisticated?
- For your most complex predicted action, how much business logic now lives in both client and server — and what happens when only one of them is updated?
- Do you need offline or flaky-network tolerance at all? If not, what is prediction actually buying you beyond a few hundred milliseconds?

## See also

[[predict-only-what-users-dont-care-about]] · [[duplication-can-beat-the-abstraction]] · [[../duo-product/SKILL]]
