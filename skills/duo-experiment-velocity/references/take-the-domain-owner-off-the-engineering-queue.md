---
name: duo-experiment-velocity-take-the-domain-owner-off-the-engineering-queue
summary: Put variants in a tool the content owner operates directly and a whole class of experiment stops competing for engineering time.
metadata:
  internal: true
---

# Take the Domain Owner Off the Engineering Queue

## Concept

Some experiments need an engineer because the change is genuinely technical. Many need an engineer only because of where the change happens to live in the codebase. Text is the clearest case — a person who owns the words cannot change the words, so every wording test must be specified, scheduled, built, reviewed and released by someone whose scarcest skill is irrelevant to the decision being made. The result is not that wording tests get delayed; it is that they are never proposed, because everyone has internalised the queue. The fix is not a faster queue. It is removing engineers from the critical path for that entire class of experiment, by giving the domain owner a tool that writes the variants directly into the system that serves them.

## What Duolingo does

Source: blog.duolingo.com/copy-testing-experiments (Duolingo blog, 2022-01-14; accessed 2026-09-22)

- Duolingo built **Expurrimenter** inside CopyCAT, its existing translation tool, so the people who own the words define the variants themselves rather than filing a request against an engineering backlog.
- The volume change was immediate and large. **Within the first three months of Expurrimenter, Duolingo more than doubled its all-time volume of copy tests** — not doubled the quarter, doubled the total ever run.
- The tool operates against copy localised into **22 primary languages**, so a single test is defined once and resolves per language instead of being rebuilt per market.
- The honest cost is the part teams skip when they retell this story. The cheap tool was only possible after an expensive plumbing project — Duolingo had to programmatically revamp its localisation infrastructure end to end, from how copy is referenced in code through to how localisation experiments run in the app. The self-serve surface was the last step, not the first.
- The complementary constraint lives in the readout, not the tool. High-volume, low-cost tests of small changes only stay meaningful if each one still carries a hypothesis and lands in a standard report — see [[curate-the-report-per-experiment-type]].

## The transferable pattern

- **Name the class, not the request.** The win is not "make this one change easier." It is identifying a category of experiment — text, thresholds, ordering, pricing tiers, eligibility rules, notification timing — where the person with the judgement is not the person with commit access.
- **Ask who decides and who types.** Wherever those are different people, you have a queue, and the queue is suppressing tests that were never written down as ideas.
- **Extend the tool the owner already lives in.** Duolingo put the experiment surface inside the tool its content people already used daily. A separate experimentation console for non-engineers becomes a thing they need training for, which recreates the queue with extra steps.
- **Expect to pay for the plumbing first.** If the values are hardcoded, scattered, or referenced inconsistently, the self-serve layer cannot exist until that is centralised. Budget the unglamorous refactor as the actual project.
- **Set the blast radius in the tool.** Self-serve means someone will eventually ship a bad variant to production. Cap exposure, require the same guardrails as any other test, and make rollback a button rather than a deploy.
- **Volume is the success metric, and it will look suspicious.** A tenfold jump in tests of small changes is the tool working, not people wasting time — judge it on decisions made, not on hit rate.

## Apply to your product

- Which category of change in your product requires an engineer purely because of where the value is stored, not because the change is technical?
- Who currently owns the judgement for that category, what tool do they already open every day, and could the variant live there?
- What centralisation work stands between you and that tool, and would you still call the tool cheap if you priced that work into it?

## See also

[[marginal-cost-decides-which-ideas-get-tested]] · [[self-serve-adoption-is-the-tooling-metric]] · [[../duo-localization/SKILL]]
