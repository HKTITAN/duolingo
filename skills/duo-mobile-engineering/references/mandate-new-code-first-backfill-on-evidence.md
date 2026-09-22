---
name: duo-mobile-engineering-mandate-new-code-first-backfill-on-evidence
summary: Stage a migration in two commitments — all new code on the new stack with no promise about old code, then decide backfilling on evidence — and split conversion PRs so reviewers only judge the human part.
metadata:
  internal: true
---

# Mandate New Code First, Backfill on Evidence

## Concept

A migration decision is really two decisions with wildly different risk profiles, and teams habitually make them as one. The first — *all new code uses the new stack* — stops the debt growing, generates in-house experience at close to zero opportunity cost, and is cheap to reverse. The second — *we will convert everything existing* — is expensive, slow and hard to reverse.

Making them together means the expensive decision gets made with the enthusiasm that started the project. Making them separately means it gets made months later with data the first phase produced.

Then there is the review problem. A mechanical conversion diff is mostly machine-produced noise that is safe by construction, with a handful of lines that require real judgment buried inside it. Mixed together, review becomes either unaffordable or a rubber stamp.

## What Duolingo does

Source: blog.duolingo.com/migrating-duolingos-android-app-to-100-kotlin (Duolingo blog, 2020-04-06; accessed 2026-09-22)

- In early 2018 the Android developers **unanimously adopted a policy of writing all new code in Kotlin while explicitly not committing to migrating existing Java**. The full migration to 100% Kotlin followed and **took two years**, after five years of Java.
- The evidence the first phase produced: converting a Java file cut its line count **~30% on average and up to 90%**; codebase LOC had been growing **46% year over year before Kotlin and was flat for the two years after, despite 2x the contributors**; developer-happiness NPS rose **129 points**; they counted **100+ historical commits fixing NullPointerExceptions** that the new type system makes structurally impossible.
- The review recipe: **one source file per pull request, minimum three commits** — run the IDE autoconverter (not reviewed carefully), fix compilation errors, then refactor to idiomatic style and satisfy the linters. Reviewers spend their attention on the third commit.
- **Two risks were named upfront and not dismissed**: the migration might not be worth its opportunity cost in developer time, and the new language might be obsoleted by improvements backported to the old one — the CoffeeScript outcome.

Source: blog.duolingo.com/life-at-duolingo-julie-wang (Duolingo blog, 2023-09-15; accessed 2026-09-22)

- Cleanup that is nobody's job never happens, because it loses every head-to-head against a feature with a named owner and a launch date. Duolingo runs a **Client Architecture team whose sole responsibility is the stability and testability of client repos**, including deleting legacy code. Over roughly **two years the Objective-C in the oldest parts of the iOS app was almost entirely removed**.

## The transferable pattern

1. **Split the reversible decision from the irreversible one and take only the first now.** "Everything new goes here; we promise nothing about what exists" is a real commitment that costs almost nothing and buys you experience plus a stopped bleed.
2. **Decide the backfill on numbers the first phase generated** — defect classes eliminated, code volume, contributor sentiment, onboarding time — not on the momentum that started it.
3. **Name the ways this could be a mistake, in writing, at the start.** Opportunity cost and technology obsolescence are the two standard ones. A migration that cannot articulate its own failure modes is an enthusiasm.
4. **Separate machine churn from human judgment at the commit level.** One unit per change, one commit for the tool's output, one to make it build, one for the judgment calls. Review the last one.
5. **Fund cleanup as a standing mandate, not as heroism.** Diffuse, deferred benefits versus a concrete present cost loses every prioritization argument; the only fix is to remove it from that competition.

## Apply to your product

- What is the smallest version of your migration that you could commit to on Monday and reverse in a week if it went badly?
- What evidence would you need, six months in, to justify converting the rest — and are you collecting it now?
- Who on your team is measured on removing things? If the answer is nobody, your legacy will outlive every plan to delete it.

## See also

[[prove-the-shape-in-the-hardest-part-first]] · [[a-fixed-window-beats-a-trickle]] · [[../duo-product/references/ruthless-prioritization]]
