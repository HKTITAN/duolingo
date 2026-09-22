---
name: duo-backend-architecture-move-the-ui-definition-to-the-server
summary: When the release cycle caps how many experiments you can run, ship the interface as a server-sent config plus a per-user data model.
metadata:
  internal: true
---

# Move The UI Definition To The Server

## Concept

The binding constraint on how fast a team learns is usually not the supply of ideas — it is the cost of one iteration. If every interface change has to ride a binary release, each idea costs a week or more, doubled by implementing it once per platform, and a post-release bug costs another full cycle. Moving the interface definition itself server-side — layout, styling, conditions, interaction handlers, all delivered in a response — collapses that loop to a deploy. It also ends version fragmentation, where the population is split across several different interfaces at once. What you are buying is iteration rate; what you are paying is that you now own and version an interface framework.

## What Duolingo does

Source: blog.duolingo.com/server-driven-ui (Duolingo blog, 2024-11-08; accessed 2026-09-22)

- Duolingo built a server-driven UI system, starting with the in-app shop. A single backend response (`SDUIResponse`) carries **screens, components, a stylesheet, actions, conditions and a data model** — granular enough to control both layout and interactivity.
- **12 components** were exposed in the API. In the first year they ran **18 experiments** through the system, **including a full shop redesign with zero client changes**.
- The prior baseline: **one week minimum** for any interface change to reach users, plus **another week** for any post-release fix.
- **The payload is split in two layers.** The **UI config** (screens, components, stylesheet) is the same for everyone and changes rarely. The **data model** holds per-user values — asset images, localized strings, prices, and the backend values that conditions evaluate against — and is cached locally so an action can mutate a displayed value without a new round trip. One split buys localization, local updates and versioning at the same time.
- **The cost.** This is an interface library you now own, version and support. Duolingo's own takeaways stress designing for scalability and versioning from the outset — front-loaded design work before the first screen ships.

Scope note: this node is about where the interface *definition* lives and how it is transported. Visual craft — motion, tokens, component styling — belongs to [[../duo-design/SKILL]].

## The transferable pattern

1. **Diagnose the constraint before adopting the machinery.** Server-driven interfaces pay off when release cadence is what caps your experiment count. If you ship continuously to the web already, you have most of the benefit and none of the cost.
2. **Split the payload by change rate, not by screen.** A rarely-changing, everyone-identical configuration layer and a constantly-changing, per-user value layer. Fusing them forces you to send every locale to every user and to re-fetch an entire screen to change one number.
3. **Make conditions data-driven.** If the config declares which value a branch reads, and the data model supplies it, product logic moves without a release.
4. **Budget the versioning design up front.** The framework's hardest problem is not rendering; it is what happens when a client is older than the config. See [[version-clients-by-last-good-config]].
5. **Start on one surface.** A commerce or settings screen with high experiment volume and low visual ambition is the right first target.

## Apply to your product

- How many interface experiments per quarter do you run, and is that number set by ideas or by release mechanics?
- Which single screen absorbs the most iteration, and what would it take to describe it as data your server sends?
- If you split your payload into configuration and per-user values today, which of the two would change ten times more often?

## See also

[[version-clients-by-last-good-config]] · [[split-data-by-sharing-pattern]] · [[../duo-experimentation/SKILL]]
