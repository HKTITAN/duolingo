---
name: duo-freemium-monetization
description: Decide where the paid line sits when your free tier is also your distribution engine — what to charge for, what to never charge for, and when an upsell costs more than it earns. Covers friction-removal pricing versus core-value paywalls, metering a premium asset by dose instead of locking it, using subscribers to validate a feature before releasing it free, raising the ceiling for users who exhausted you, shared-seat plans without eligibility checks, renaming a tier without reading as a price increase, timing the ask to an intention the user already formed, and turning owned reference content into an instrumented conversion surface. Use when someone asks what should be free versus paid, how to design a paywall, why the upgrade screen is not converting, whether to ship a feature as premium first, how to price a family or team plan, or how to monetize without killing growth.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Freemium Monetization

Where to draw the paid line when the free tier is the thing that grows you.

Duolingo became the top-grossing app in Education on both stores while giving away
every course. That is not generosity and it is not an accident — it is a specific
set of decisions about which layer of the product carries the price, which segments
should never see an upgrade screen at all, and what has to be true structurally for
a free-core commitment to survive a bad quarter. This skill is those decisions, with
the numbers attached and the tradeoffs left in.

Duolingo is the case study. Your product is the target — nothing here assumes you are
selling education, and none of it assumes your free tier is a demo.

## Where the line goes

- [[references/charge-for-friction-removal-not-core-value]] — sell friction removal and optional amplification; never sell access to the thing you exist to deliver.
- [[references/a-paying-minority-funds-a-complete-free-tier]] — a small paying minority can fund everyone else, but only if the free tier is genuinely complete rather than crippled.
- [[references/give-the-free-tier-an-owner-with-standing]] — the commitment holds only if a non-revenue function has real decision power and a first-order metric.
- [[references/unpaid-supply-expires-when-you-monetize-it]] — volunteer production is a legitimate cold start that stops being legitimate the day you earn from the output.

## When the upsell costs more than it earns

- [[references/the-upsell-you-delete-is-growth-you-keep]] — in a segment that does not recognize your payment model, the upgrade screen reads as a wall and kills the user.
- [[references/remove-the-incidental-barrier-not-the-standard]] — cutting cost, travel and scheduling expands the qualified pool because those barriers never measured ability.

## How to shape the offer

- [[references/meter-by-dose-instead-of-locking-the-door]] — give free users the real premium asset briefly and countably; the meter running out is the pitch.
- [[references/paywall-for-evidence-not-forever]] — launch uncertain features to subscribers, then release what proves out and owe yourself a replacement.
- [[references/raise-the-ceiling-for-users-who-finished-you]] — your most engaged cohort is the one with nowhere left to go, and it costs nothing to reacquire.
- [[references/drop-eligibility-checks-on-shared-seat-plans]] — a group plan is a referral engine; every verification rule is friction on your own acquisition.

## How to package and time the ask

- [[references/rebrand-the-package-not-the-price]] — change one variable, answer the suspicion item by item, and pick a name that survives translation.
- [[references/time-the-ask-to-an-intention-already-formed]] — arrive as the instrument of a decision the user already made, so the offer only has to clear price.
- [[references/reference-content-as-a-conversion-surface]] — build owned reference pages as a lattice and route each page's call-to-action to the audience it attracted.

## Boundaries

This skill covers where the paid line sits and how the offer is shaped. It does not
cover which market or product line to enter, and it does not cover how to measure
conversion health — route those to the strategy and metrics skills rather than
stretching a pricing argument to carry them.

Pixel-level craft — easing curves, contrast ratios, token values, component props —
is out of scope for this entire pack. Describe intent and rationale; route the
implementation to a design-engineering skill.

## Sibling skills

- [[../duo-growth/SKILL]] — viral loops, brand as acquisition, and the distribution the free tier buys.
- [[../duo-product/SKILL]] — taking the long view, shipping, and raising the bar on what the free core delivers.
- [[../duo-experimentation/SKILL]] — the A/B discipline behind every number quoted here.
- [[../duo-inclusive-access/SKILL]] — reach as a design constraint rather than a marketing outcome.

## Sources

Every node cites a dated post on blog.duolingo.com, verified against
`scripts/sources.json` — the bibliography of 842 crawled English posts. Substance is
inlined in the nodes; the URLs are provenance, not pointers.
