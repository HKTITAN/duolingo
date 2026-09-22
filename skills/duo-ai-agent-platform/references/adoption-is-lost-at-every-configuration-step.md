---
name: duo-ai-agent-platform-adoption-is-lost-at-every-configuration-step
summary: Each setup step between a person and a capability filters most of them out — move the capability into the surface they already sit in instead of perfecting the setup guide.
metadata:
  internal: true
---

# Adoption Is Lost at Every Configuration Step

## Concept

Every configuration step between a user and a capability removes most of the remaining users. This is brutal in a way teams consistently underestimate, because setup cost is paid up front, before any value has been experienced — so it is weighed against zero evidence of benefit.

Most people do not want to configure anything. They want an answer. Which means the move that raises adoption is usually not a better setup experience; it is relocating the capability into a surface the person is already sitting in, where setup cost is zero and the ceiling becomes the size of that surface's audience.

The same arithmetic applies to knowledge that is scattered across tools, and to logic that lives in code but is owned by people who cannot edit code. In both cases the cost is invisible because it is paid in small amounts by many people, continuously.

## What Duolingo does

Source: blog.duolingo.com/aislackbot (Duolingo blog, 2026-05-20; accessed 2026-09-22)

Internal AI tooling went through three stages, and only the third worked:

1. **Hand-editing a local config file** — used by a handful of engineers.
2. **A one-click centralized config generator page** — polished, and still, in the team's own words, too much.
3. **A chat app requiring no setup at all** — reached **~300 weekly active users, roughly 30% of the company**, with a response upvote rate that stabilized around **80%**. It monitors **20+ help desk channels** across an organization running hundreds of microservices for 130M+ monthly active users. Adding a new capability means deploying a new integration server, with no change to the app's core logic.

**Tension.** The intermediate step is the lesson. A polished one-click setup page still failed on adoption, and the team says plainly that even one click was too much. Improving the setup experience was not the answer — eliminating it was. That is an uncomfortable finding, because "make onboarding smoother" is the fix every team reaches for first.

Two adjacent cases:

- **One search box over many tools.** Duolingo built and open-sourced a federated search tool covering up to **22 data sources** in roughly **3,000 lines of TypeScript**, with fewer than **100 lines on average to add a source** and a single container command to run it, used internally for nearly a year before release (blog.duolingo.com/open-sourcing-metasearch-our-one-tool-to-search-them-all (Duolingo blog, 2021-03-17; accessed 2026-09-22)).
- **Logic non-engineers keep asking you to change.** Duolingo generates content at scale, but the generation logic often lives in a code file, so a writer who wants a tweak has to ask an engineer. The post frames this as an unresolved dilemma — small changes that add up cumulatively versus a heavy one-time cost to build a self-serve pipeline (blog.duolingo.com/life-at-duolingo-julie-wang (Duolingo blog, 2023-09-15; accessed 2026-09-22)). The honest position is that it is a real tradeoff, not an obvious win.

## The transferable pattern

1. **Count the steps** between a new user and their first result. Each one is a filter, and the early ones cut hardest because no value has been delivered yet.
2. **Ask where the user already is** — which surface they have open all day — and put the capability there, rather than asking them to adopt a new one.
3. **Annualize invisible costs before dismissing them.** A five-minute favour asked fifty times a year by twelve people is a headcount question wearing a disguise. It stays invisible because it has no line item and the one-time build does.
4. **Include the waiting.** The person who has to ask also waits, and that latency appears in neither estimate.

## Apply to your product

- How many steps stand between a new user and their first useful result, and which of them exists for your convenience rather than theirs?
- Which surface do your users already have open all day, and what would it take to deliver your capability inside it?
- What recurring small request lands on your team weekly? Multiply it by a year, then compare honestly against the one-time cost of making it self-serve.

## See also

[[distribute-the-prompt-not-the-person]] · [[standardize-the-integration-surface]] · [[../duo-product/references/intuitive-by-default]]
