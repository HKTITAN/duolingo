---
name: duo-product-kill-criteria-product
summary: The rules for stopping a project, not just an experiment.
metadata:
  internal: true
---

# Kill Criteria (Product)

## Concept

The experimentation skill has its own [[../duo-experimentation/references/kill-criteria]]. This is the bigger sibling: the rules for stopping a *project*. Most teams have rules for starting projects (planning, prioritization) and almost none for stopping them. The handbook's *Ship It* explicitly names this gap: *"We ruthlessly prioritize projects with the highest impact and quickly cut what isn't working."*

## What Duolingo does

Source: blog.duolingo.com/duolingo-energy (Duolingo blog, 2025-07-03; accessed 2026-09-22)

- **A core system that isn't "broken" can still be cut.** Hearts had been the free-tier mistake economy for years. Duolingo replaced it with Energy because the data said beginners were **2x more likely to run out of hearts mid-lesson** — discouraging exactly the users least able to absorb it. The stated reason was not a bug; it was "not the most effective way to support learning."
- **Killing a project you already designed for counts too.** The Friend Streak team had deliberately designed the UI to scale past 5 slots, then ran a data science exercise on retention and uptake per additional slot to forecast whether "the juice was worth the squeeze." It wasn't: the population with large active friend groups was small, and users at 5 streaks were already well-retaining. They shipped the cap and did not run the expansion tests (blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)).
- **Content gets killed at commissioning, not in production.** A partner pitched a Spanish story about a journalist investigating unsolved murders; Duolingo's country marketing manager in Mexico argued it down on two grounds — too complex for the intermediate level, and it didn't feel like Duolingo. They went back to the drawing board mid-pandemic and took a bank-heist story instead (blog.duolingo.com/true-crime-meets-spanish-learning (Duolingo blog, 2020-12-03; accessed 2026-09-22)).
- The decision to kill is owned and made — it's not allowed to drift to no decision.

The pattern across all three: the stop decision is made against a **pre-stated user outcome** (does this help people learn, does this move the invite step, does this fit the level and the tone), not against sunk cost or against whether anything is visibly failing.

## The transferable pattern

Three rules:

1. **Pre-commit to success criteria.** What does "this project worked" look like? Write it before you start.
2. **Stopping is a positive act.** Reframe "we're killing this" as "we're freeing the team's attention for higher-leverage work."
3. **Sunset has a process.** Removing a feature has its own work — communications, migration, deprecation. Plan for it; don't pretend you can leave it running forever for free.

The hardest part is cultural. Most orgs have implicit rules that punish stopping: it looks like failure, the original sponsor loses face, the team that built it feels disrespected. *Ship It* requires inverting these: stopping should look like leadership, not weakness.

## Apply to your product

- What's a project still alive that the data says should be cut? Why hasn't it been?
- Does your team have a defined sunset process, or is feature removal ad-hoc?
- Is "we cut it" something a leader would say with pride or with apology in your org?

## See also

[[ship-it]] · [[ruthless-prioritization]] · [[scope-floor-for-v1]] · [[take-the-long-view]] · [[../duo-experimentation/references/kill-criteria]]
