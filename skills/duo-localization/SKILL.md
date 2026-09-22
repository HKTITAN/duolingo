---
name: duo-localization
description: Ship your product to people who do not share your language, script, reading direction, demographics or fluency with software — and decide which markets that opens. Covers writing into the register users actually speak instead of the formally correct one, why device locale is a bad proxy for intent, right-to-left as a component problem rather than a string problem, why a copy win in one market does not port, sidestepping grammatical defaults that assert things about the user, how layout silently reverts your content decisions, translating to a consumption budget, and giving local teams authority to diverge from the source text. Use when someone asks how do we launch in another country, should we just translate this, why is conversion worse in this market, does our app work in Arabic or Hebrew, why did our winning experiment fail abroad, or who should own translated copy.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Localization — Map of Content

Translation is the cheapest and least important part of shipping to a market that is not yours. The expensive parts are structural: components that encode a reading direction, containers sized for your source string, defaults that decide who sees what, and copy that works through connotation rather than meaning. Most localization failures are not mistranslations — they are correct strings inside a product that still assumes your user.

Two ideas run through all of it. First, **comprehension beats correctness** — the goal is the user reaching the next screen, not a string a reviewer would approve. Second, **the market you learned your product in taught you things that are not true elsewhere**, so every default, every winning test and every cohort assumption is suspect until re-checked locally.

Scan the descriptions, follow only the `[[wikilinks]]` you need.

## Write for the person who is actually reading

- [[references/localize-into-the-register-people-speak]] — ship the words users say, including loanwords; review every screen against your least software-fluent user; open by inventorying what they already know.
- [[references/rewrite-rather-than-default-the-assumption]] — when grammar forces you to assert something about the user, rephrase around it rather than picking a default, and prefer already-neutral words to invented ones.
- [[references/localize-to-a-consumption-budget]] — the constraint is the consumer's processing rate, so rank information by importance and preserve intent rather than words.

## The product, not the strings

- [[references/reading-direction-is-a-component-problem]] — pagers, swipes and orderings encode direction; the platform primitive you need may never have been fixed, so budget to build it.
- [[references/layout-overrides-your-content-policy]] — containers sized for the source string quietly revert your content decisions, and a denser script can buy explanation that a longer one cannot.

## Read your own market signals with suspicion

- [[references/device-locale-is-not-intent]] — device language describes a phone, not a person; popularity rankings mostly measure what you put on the shelf.
- [[references/a-winning-message-is-valid-only-where-it-won]] — persuasion, cohort shape and even where your audience lives are local facts; re-test before rolling a localized win out.

## Who owns the words

- [[references/local-teams-own-expressive-copy-and-full-editions]] — give regional teams authority to diverge from the source for names, campaigns and story, and publish flagship material complete in-language.

## Boundary

This skill covers what has to change inside the product once you are in a market. Barriers a third party controls — carrier data costs, accreditation, institutional procurement, app-store policy — are a distribution problem and belong elsewhere. Accessibility and the requirements that exclude people regardless of locale live in [[../duo-inclusive-access/SKILL]]. And pixel craft — easing values, contrast ratios, token values, component props — is out of scope for this whole pack; route it per [[../duolingo/references/design-handoff]].

## Sibling skills

- [[../duo-voice/SKILL]] — the brand voice that expressive copy has to carry into each market.
- [[../duo-experimentation/SKILL]] — how to re-test a localized win without fooling yourself, including what a null result is worth.
- [[../duo-inclusive-access/SKILL]] — the requirements that filter people out on circumstance rather than ability.
- [[../duo-growth/SKILL]] — choosing which market to open, and what earned media a localized launch buys.

## Sources

Distilled from 15 posts on blog.duolingo.com dated 2016-09-13 to 2026-07-07, all cited inline and dated in each node; slugs are verified against `scripts/sources.json`.
