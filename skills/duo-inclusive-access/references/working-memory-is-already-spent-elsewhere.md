---
name: duo-inclusive-access-working-memory-is-already-spent-elsewhere
summary: Treat working memory as a fixed budget the user is already spending on self-monitoring and on tracking your interface — reducing extraneous load is a direct multiplier on what lands.
metadata:
  internal: true
---

# Working Memory Is Already Spent Elsewhere

## Concept

Working memory is a fixed budget, and you are not the first claim on it. Before your content arrives, some of it is already committed — to self-monitoring, to masking behaviour the person has learned to suppress in public, to remembering which mode your interface is in, which panel they came from, and what that unlabelled icon did last time. Whatever goes to those is subtracted from the task.

This reframes load reduction. Cutting extraneous demand is not a comfort feature or a politeness; it is a direct multiplier on how much of the intended content actually lands. It also reframes where to look first. The biggest single reclaim is often not in your interface at all — it is in the conditions the person is using it under, which means the highest-leverage move can be a setting or a permission rather than a feature.

## What Duolingo does

Source: blog.duolingo.com/adhd-study-tricks (Duolingo blog, 2022-03-15; accessed 2026-09-22)

- Duolingo's guidance starts from the observation that people with ADHD have **fewer working-memory resources**, and that a share of those resources is already going to hiding ADHD characteristics — not being too loud, not bouncing their legs, not sitting in a chair the way that is comfortable rather than the way that looks normal.
- So the **first** recommendation is not a feature. It is a space where the person can stop suppressing, which frees the budget for the task itself. Everything else in the list is downstream of that reclaim.

Source: blog.duolingo.com/inclusive-testing-technology (Duolingo blog, 2022-01-27; accessed 2026-09-22)

- The same logic drives the interface choices in the Duolingo English Test — minimal scrolling and large type, explicitly to reduce visual and working-memory load — and the use of computer adaptive testing to replace a roughly **3-hour** sustained-concentration demand with a shorter one that is no less rigorous.

## The transferable pattern

Audit what your product asks people to *hold* rather than what it asks them to do. State they must remember across screens, a mode with no visible indicator, values they must carry from one step to the next, jargon they must silently decode, a layout that shifts under them — each of these is a withdrawal from a budget that was already partly spent. None of it shows up in a feature list, and all of it shows up in completion rates.

Two rules follow. Put state on the screen instead of in the person's head; a visible breadcrumb, a persistent summary or a labelled mode costs pixels and buys attention. And when you are designing for people under additional load, ask what their *context* is charging them before you ask what your interface is charging them — an option that lets someone stop performing for their environment can return more capacity than any amount of interface tightening.

## Apply to your product

- Walk one core flow and write down every value or piece of state the user has to carry in their head. Which could be on screen instead?
- Where does your product change mode without saying so? How would a distracted user find out which mode they are in?
- What is your users' environment already charging them while they use you, and is there a setting that would let them stop paying it?

## See also

[[strip-every-demand-you-are-not-measuring]] · [[let-the-user-own-the-turn-boundary]] · [[../duo-design/references/accessibility-default]]
