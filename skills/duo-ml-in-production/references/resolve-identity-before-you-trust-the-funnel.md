---
name: duo-ml-in-production-resolve-identity-before-you-trust-the-funnel
summary: Without cross-device and cross-account identity resolution, a returning user counts as an acquisition and your funnel is wrong in both directions at once.
metadata:
  internal: true
---

# Resolve Identity Before You Trust the Funnel

## Concept

Retention and acquisition are computed from the same join key. Retention asks whether this identity came back; acquisition asks whether this identity is new. So when the key fragments — a user reinstalls, switches devices, signs in with a different provider, or starts anonymous and registers later — both numbers break at once, and they break in opposite directions. Churn is overstated, because the person appears to have left. Acquisition is overstated, because a stranger appears to have arrived.

That is the dangerous part. The two errors partially cancel in the top-line total, so the dashboard everyone watches looks fine while every segment underneath it is wrong. Identity resolution is not a data-hygiene chore you do later; it is the precondition for any of your behavioral numbers meaning what their names say.

## What Duolingo does

Source: blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)

- Duolingo's engineering team built an **"aliasing" process** that resolves a person's activity across multiple accounts into one identity.
- **Data Science only works with post-aliasing data.** Aliasing is not an optional enrichment applied by whoever remembers — it is upstream of the analytics surface, so there is no path to the raw fragmented view.
- The **Growth Model** — the framework the company uses to decompose daily active users into new, current, reactivated, and resurrected states — is computed on top of the aliased data. Every state transition in that decomposition depends on the join key being right, since "reactivated" and "new" are distinguished by nothing else.

## The transferable pattern

Treat identity resolution as infrastructure that sits between raw events and every metric, not as a transformation applied per analysis. The architectural rule is that the fragmented identity should be unavailable downstream. If analysts can reach the pre-resolution table, some analyses will use it, and you will end up with two sets of numbers that disagree for reasons nobody can reconstruct six months later.

Before you believe any cohort or funnel number, enumerate the ways one person can generate two identifiers in your system: a fresh install, a second device, a different sign-in provider, an anonymous session that later registers, a workspace invitation to an address they already use. Each one is a mechanism that converts a returning user into a new one.

Then notice which metrics are *most* corrupted. The top-line total absorbs the error and looks stable. The damage concentrates in exactly the numbers used to make decisions: cohort retention curves, cost per acquisition, and any claim about reactivation. A reactivation program measured on fragmented identity is measuring its own inability to recognize people.

The cost is honest: resolution is probabilistic at the edges, it is a standing pipeline with an owner, and it must be versioned, because re-resolving history changes numbers that were already reported. Say when the resolution logic last changed whenever you present a trend that crosses that date.

## Apply to your product

- List every way one person in your product can end up with two identifiers. Which of those are you currently resolving?
- Can an analyst on your team query the pre-resolution events, and if so, which of your published numbers were computed that way?
- Which decision have you made recently that would flip if your "new user" count were meaningfully lower and your churn meaningfully lower too?

## See also

[[ship-coverage-as-the-progress-metric]] · [[../duo-production-reliability/references/sampled-tracing-versus-request-identity]] · [[../duo-growth/SKILL]]
