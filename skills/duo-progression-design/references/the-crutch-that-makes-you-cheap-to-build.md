---
name: duo-progression-design-the-crutch-that-makes-you-cheap-to-build
summary: The scaffold that makes content cheap to generate and answers cheap to grade is often the one preventing the skill from forming.
metadata:
  internal: true
---

# The Crutch That Makes You Cheap to Build

## Concept

Some scaffolds are not there for the user. They are there because they make the product tractable. Route every interaction through a familiar intermediate representation and correctness becomes trivially checkable, content becomes trivially generatable, and the whole system scales. That is exactly why it gets built — and exactly why the user never forms the direct connection the product exists to teach. They get very good at the intermediate step. Under real conditions the intermediate step is not available, and the performance collapses. The crutch is a business-model decision wearing a pedagogy costume, and it should be named as one.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-teaches-english (Duolingo blog, 2024-08-07; accessed 2026-09-22)

- Duolingo's B1/B2 English content teaches English **entirely in English, with no translation exercises at all** — the crutch that had underpinned the product was removed at the top of the ladder. Scale of the rebuild: **nearly 200 new units across 20+ English courses**, covering CEFR B1 and B2 across four sections (5 and 6 for B1, 7 and 8 for B2). English is the number one language studied in **119 countries**.
- **Duolingo concedes the motive in the same post.** Translations are "convenient" for checking comprehension and make developing content with technology "efficient and scalable." The crutch was load-bearing for the company, not just for the user.
- Removing it cost real work. New monolingual exercise types had to be invented — definitions given in English, dialogue completion, cloze passages — because the cheap correctness check was gone.
- The safety net stays as an **opt-in hint**: learners can still tap for a translation in their own language. Removed as the default path, kept as an escape hatch.
- The same move at the beginner end: immersion exercises answerable **only in the target language**, with meaning carried by images and surrounding context, so the user builds a direct meaning-to-form link instead of a form-to-translation-to-meaning chain. Duolingo concedes this is "trickier to design" — the cost moves onto content design, which now needs context clues and images for every item (blog.duolingo.com/new-immersion-exercises-maximize-your-language-learning (Duolingo blog, 2021-04-27; accessed 2026-09-22)).

## The transferable pattern

Ask one uncomfortable question about every scaffold in your product: *would we have built this if it were expensive?* If the honest answer is no, it is a production convenience, and production conveniences have a way of becoming the thing the user actually learns.

The diagnostic is whether the practice task can be completed by routing through the user's existing mental model. If it can, the brain takes that route every time, and what gets reinforced is the detour — leaving the direct path weak, slow and effortful under load. Examples of the shape: a tool that always shows the generated equivalent beside the raw form; a workflow where the answer can be found by pattern-matching the template instead of reasoning about the case; a review step that can be passed by checking the summary rather than the artifact.

The fix is not deletion:

1. **Design at least one exercise the crutch cannot solve.** One is enough to reveal whether the skill exists.
2. **Move the crutch from default to on-demand hint.** The safety net survives; the default path changes.
3. **Budget for the replacement.** Removing the cheap correctness check means inventing a new way to tell right from wrong, and that is engineering work, not a copy change.
4. **Remove it at the top of the ladder first.** Advanced users have the most to lose from it and the most tolerance for the harder version.

## Apply to your product

- Which scaffold in your product exists because it makes content cheap to author or answers cheap to grade? Would you have shipped it otherwise?
- Can your core practice task be completed without exercising the target skill? Design one task where the shortcut is unavailable and watch what happens.
- If you removed the crutch from your most advanced tier, what new way of checking correctness would you have to build — and what would that cost?

## See also

[[scaffold-and-fade-on-a-schedule]] · [[make-the-scaffold-removable-by-the-user]] · [[recognition-then-guided-then-production]] · [[../duo-product/references/raise-the-bar]]
