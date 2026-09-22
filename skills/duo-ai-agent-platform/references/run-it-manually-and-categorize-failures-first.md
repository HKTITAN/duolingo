---
name: duo-ai-agent-platform-run-it-manually-and-categorize-failures-first
summary: Weeks of manual runs with every failure categorized is a free structural audit — some failures are prompt bugs, and some are real defects your own people route around silently.
metadata:
  internal: true
---

# Run It Manually and Categorize Failures First

## Concept

The instinct after a promising demo is to wire it into a pipeline. Do the boring thing instead — run it by hand for weeks and write down what went wrong every single time, sorted into categories.

Two things come out of that log, and the second is worth more than the first. Some failures are your instructions being wrong, which you fix in the prompt. The rest are real defects in the system being worked on, and you would never have found them otherwise, because a human practitioner routes around structural friction unconsciously and never files a ticket about it. An automated worker cannot. It fails loudly at exactly the places your design makes work hard, which turns its error log into a ranked list of what to fix.

That list benefits everyone who touches the system, not only the automation you were building.

## What Duolingo does

Source: blog.duolingo.com/ai-ios-unit-test-generation-pipeline (Duolingo blog, 2026-06-24; accessed 2026-09-22)

- Before automating anything, the team spent weeks running the coding agent locally and analysing every CI result, in batches.
- **Batch 1 — 17 PRs, 8 merged (47%). Batch 2 — 40 PRs, 19 merged (48%).** Roughly half failing, twice, is what the honest starting point looks like.
- The recurring failure modes were categorized rather than patched one by one — mock type mismatch, Swift 6 `Sendable` conformance, mixing two test frameworks in one file, access-control errors, and missing `try`/`throws`.
- The top category was a structural defect, not a prompt bug. Several repository classes took a concrete client type instead of the protocol, which made injecting a mock impossible. Duolingo migrated the codebase to the protocol and added a linter rule so it could not recur.

**Tension — the audit outran the automation.** The post is explicit that these fixes improved CI pass rates for everyone, not just the pipeline. The most valuable output of the experiment was a map of where the architecture resisted testing, which had been invisible for years because every engineer had quietly worked around it. Had the team skipped the manual phase and gone straight to a pipeline, they would have tuned prompts against a defect instead of finding it.

## The transferable pattern

Treat the manual phase as a measurement instrument, not as a delay:

1. **Run it by hand, in batches, for weeks.** Batches make the success rate comparable over time; a continuous trickle does not.
2. **Categorize every failure** into "the instruction was wrong" versus "the system made this hard". Keep the counts. The second bucket is the audit.
3. **Fix the second bucket structurally**, and add an enforcement mechanism so the defect cannot come back after you stop looking.
4. **Publish the failure taxonomy** to the team that owns the system. Written down, it is a prioritized backlog with evidence attached; in your head, it is an anecdote.

A ~50% success rate on the first batches is not a reason to stop. It is the number you are trying to move, and you cannot move it until you know which half of it is yours.

## Apply to your product

- Where in your system does work reliably get harder, that nobody has ever filed as a bug because everyone learned the workaround?
- If you ran your intended automation by hand fifty times, who would keep the log, and in what categories?
- What would it take to turn the top failure category into an enforced rule rather than a piece of tribal knowledge?

## See also

[[verification-becomes-the-bottleneck]] · [[every-producer-needs-a-janitor]] · [[../duo-culture/references/candor-what-not-who]]
