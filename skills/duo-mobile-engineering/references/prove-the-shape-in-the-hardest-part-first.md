---
name: duo-mobile-engineering-prove-the-shape-in-the-hardest-part-first
summary: Build the first version as a bare end-to-end skeleton with placeholders, and implement a new architecture once in the most complex part of the system before writing the migration guide.
metadata:
  internal: true
---

# Prove the Shape in the Hardest Part First

## Concept

The instinct for a large feature is to build the smallest shippable slice of the final thing — one complete vertical, done properly. The alternative is to walk the entire path end to end with nothing in it: every screen, every handoff, every state transition, all placeholders. The second is better for one reason. Structural bugs — races, cache-keying errors, ownership confusion — are easy to triage when the code contains only the logic required to do that one job. Each layer of feature complexity added on top of a wrong foundation makes the same fix an order of magnitude more expensive.

The same logic inverts for architecture adoption. Proving a new pattern on an easy case proves nothing: the gaps and missing primitives only surface under real complexity. Do it once in the worst part of the system, with three people, before thirty people start.

## What Duolingo does

Source: blog.duolingo.com/duolingo-stories-the-journey-to-android (Duolingo blog, 2020-02-21; accessed 2026-09-22)

- The first Android build of Stories had **no challenges, no audio, no illustrations, and full placeholders** — just enough to walk a story start to finish.
- Internal testing on that skeleton exposed **a race condition and a cache that was not indexed by user**, so resource management was restructured before any complexity landed on top of it.
- Shipped as an experiment: **3% increase in users actively learning, 4.6% more time spent learning** versus control.
- The tension is stated plainly against the operating principle *Prioritize ruthlessly*: the team felt the pull to take the easy way out, and deliberately kept MVVM, documentation and readable code during the fast prototype phase — otherwise "Stories would have become a feature built on top of layers and layers of crutches."

Source: blog.duolingo.com/duolingo-android-reboot-2021 (Duolingo blog, 2021-10-27; accessed 2026-09-22)

- Before the wider migration, a small group **"tackled the monkey"** by implementing the new repository + MVVM architecture in a **sufficiently complex Activity first**. That exercise produced reusable primitives and exposed gaps they had initially overlooked — and only then did they write thorough architecture and migration documentation.

Source: blog.duolingo.com/life-at-duolingo-julie-wang (Duolingo blog, 2023-09-15; accessed 2026-09-22)

- The standing questions at every architectural decision: what assumptions are we making, what upcoming features could challenge those assumptions, and **are there features we have put off for years because of technical complexity that careful design choices could now make feasible**. The named scaling constraint is **100+ courses**: adding an exercise type to one is straightforward, doing it across all requires content work, coordinators, new tooling and more backend infrastructure.

## The transferable pattern

- **Skeleton before slice.** Walk the whole path with placeholders. You are buying early exposure of structural defects while restructuring is still cheap.
- **A prototype is not permission to abandon structure.** The speed comes from omitting features, not from omitting the layering and the docs. Crutches installed during the fast phase are load-bearing forever.
- **Pilot a new pattern on your worst case, then write the guide.** Documentation written from the easy case is a description of a pattern that has never been tested.
- **Price architecture against the work you have deferred, not only what you have shipped.** The true cost of a design is the set of capabilities that silently became infeasible — and those never surface in a roadmap review, because nobody proposes them any more. Audit that graveyard deliberately.

## Apply to your product

- Could you walk your next big feature end to end tomorrow with every step stubbed? What would that skeleton tell you that a finished first slice would not?
- Which part of your system is the ugliest, and would your proposed new pattern actually survive there?
- What have you quietly not built for two years because "the architecture makes it hard"? That list is your real design brief.

## See also

[[mandate-new-code-first-backfill-on-evidence]] · [[a-fixed-window-beats-a-trickle]] · [[../duo-product/references/ship-it]]
