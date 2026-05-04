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

- Projects have explicit success criteria at start; failure to meet them is a stop signal, not a permission to keep going.
- Sunsetting a feature is treated as legitimate work, not a failure to be hidden.
- Cumulative cost matters: a feature shipped years ago that drags maintenance and complexity is a candidate for cutting, even if it's not "broken."
- The decision to kill is owned and made — it's not allowed to drift to no decision.

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

[[ship-it]] · [[ruthless-prioritization]] · [[take-the-long-view]] · [[../duo-experimentation/references/kill-criteria]]
