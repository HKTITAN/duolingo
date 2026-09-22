---
name: duolingo-sources
summary: What this pack was actually built from, what was deliberately left out, and where Duolingo has changed its mind — read before treating any claim here as current.
metadata:
  internal: true
---

# Sources — provenance and its limits

## Concept

A distilled pack is only as trustworthy as its account of what it read. This file exists so a reader can check the pack's homework and know where it stops. Everything below is measured, not estimated.

## What Duolingo does

Duolingo publishes its methodology alongside its numbers — the efficacy research framework names its study design and its limits before reporting results, and the metric posts state which figure is a *proxy* rather than the real thing. Source: `blog.duolingo.com/duolingo-efficacy-research-framework (Duolingo blog, 2022-10-17; accessed 2026-09-22)` and `blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)`. This pack copies that habit.

## The transferable pattern

### The corpus

| | |
|---|---|
| Source | `blog.duolingo.com`, via the published sitemap |
| Posts in sitemap | 2,679 |
| English posts | 842 |
| Posts actually read | 750 |
| Words read | ~559,000 |
| Claims extracted | 992, from 536 distinct posts |
| Claims carrying hard numbers | 610 |
| Claims recording a tension or tradeoff | 351 |

Also drawn on: the Duolingo Handbook (`handbook.duolingo.com`) for the operating principles, which the eight original skills were built from.

### What was deliberately left out

- **92 English posts** — pure grammar and vocabulary explainers ("what are demonstratives", "5 ways to say hello"). No transferable product wisdom. Read the titles, skipped the bodies.
- **1,837 localized posts** (es, de, pt, ja, fr, ko). Spot-checked for unique content: a handful of English originals now redirect to a locale path (the Duolingo Max / GPT-4 launch among them), but every major concept — Max, Birdbrain, Energy, Friends Quests, CEFR, Duolingo Score, Video Call — appears in 11 to 73 English posts. English coverage is sufficient; the localized set is translation, not new material.
- **`design.duolingo.com`** as a design-system source. It 301-redirects to `blog.duolingo.com/hub/design/`, a four-post curated hub. It is not a live token or component reference and must not be cited as one.

### Where Duolingo has changed its mind

Treat anything in this pack describing a current Duolingo *system* as dated. The patterns transfer; the implementations move.

- **Hearts → Energy.** The failure currency was redesigned. A node describing hearts is describing a retired system.
- **Tree → Path.** The whole navigation model changed, and with it what "progress" looks like.
- **Shorter lessons.** Duolingo tried them expecting more sessions, and it *hurt* their learning metric. Published as a failed hypothesis — one of the more useful things on the blog.
- **The AI-first shift.** Content generation economics changed what the company builds and how fast.

### What this pack cannot tell you

- **Effect sizes for most claims.** The blog reports direction ("positive impact") far more often than magnitude. Where a number exists it is quoted; where it doesn't, the claim is directional and should be treated that way.
- **What didn't work.** Publication bias is severe. Duolingo publishes its wins and a small number of instructive failures. The base rate of failed experiments behind any shipped feature is invisible here.
- **Anything after the crawl date.** This pack is a snapshot, not a feed.

## Apply to your product

- When you distill someone else's public material, can a reader tell what you read and what you skipped? If not, they cannot calibrate how much to trust you.
- Which claims in your own documentation describe a system that has since changed — and what would make that visible to the next reader?

## See also

[[translate]] · [[map]] · [[overlaps]]
