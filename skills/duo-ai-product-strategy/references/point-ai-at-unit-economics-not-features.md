---
name: duo-ai-product-strategy-point-ai-at-unit-economics-not-features
summary: A feature built with AI gets copied in a quarter; a cost structure rebuilt with AI does not. Aim at steps, authoring and grading.
metadata:
  internal: true
---

# Point AI at Unit Economics, Not Features

## Concept

The easiest thing to do with a capable model is add a surface — a chat panel, a summarize button, an assistant. Those are visible, demoable, and copyable by any competitor within a quarter, because they cost about what you paid.

The durable use is different and less photogenic. Point the model at whatever makes the incumbent expensive and slow, until your cost per delivered unit is structurally below theirs. A rival can ship your feature next month; they cannot ship your cost structure without rebuilding their operation. Three levers usually carry the weight: how many steps the user must complete, who authors the content, and who evaluates the output.

## What Duolingo does

Source: blog.duolingo.com/ai-improves-education (Duolingo blog, 2023-03-30; accessed 2026-09-22)

- The Duolingo English Test does what a traditional in-person paper-based test does in **half the time and less than half the cost**. Those two numbers are the whole strategy, and each comes from a distinct lever.
- **Fewer steps** — computer-adaptive testing selects each item to maximize information gained, so the session converges on a score in far fewer questions than a fixed-form exam needs.
- **No per-item authoring cost** — items are generated automatically rather than written by expert item writers one at a time.
- **No per-submission grading cost** — scoring is automated, which is also what removes the week-plus human marking queue.
- Accessibility rides on the same rebuild — secure at-home proctoring, so the test travels to the user instead of the reverse.
- This is not a recent bolt-on. AI had been running in the product since the DET's start, **nearly seven years as of March 2023**. GPT-3 was in production from **2021**, upgraded to **GPT-4** in **2023**.

**Tension.** A cost advantage built this way is not self-justifying. Removing human graders is exactly the move that makes an institutional buyer doubt the result, so the economics only bank if the trust work in [[attack-the-incumbents-physical-bottleneck]] happens alongside them. Cheaper and faster with no credible warrant is a product nobody in a high-consequence market is allowed to buy.

## The transferable pattern

Write down what one delivered unit of your product costs you today, split into steps the user performs, content someone authors, and output someone evaluates. Then ask of each line whether a model removes the cost or merely decorates it.

- **Steps.** Can selection be adaptive, so each step is chosen to resolve the most remaining uncertainty rather than to cover a fixed script? Fewer steps is a user-visible win and a cost win at once.
- **Authoring.** Is anyone paid per delivered item? That line scales linearly with catalog size and is the one generation actually kills.
- **Evaluation.** Is a human looking at every submission? That line scales linearly with usage, which is the worst shape a cost can have.

The test for whether you aimed correctly — can you now price where the incumbent structurally cannot follow without dismantling their own operation? If the answer is no, you built a feature. Beware the mirror failure too — a lever that only converts cost into a quality drop your users can feel is not an economics win, it is a downgrade with a spreadsheet attached.

## Apply to your product

- Which line in your cost per delivered unit grows with usage, and which grows with catalog size? Those are the two you can actually attack.
- If your model work succeeded completely, what price could you charge — and what would your incumbent have to shut down to match it?
- Which of your current AI plans would a competitor be able to copy in a quarter, and what would you build instead if copying had to take them three years?

## See also

[[spend-the-automation-budget-on-the-gate]] · [[attack-the-incumbents-physical-bottleneck]]
