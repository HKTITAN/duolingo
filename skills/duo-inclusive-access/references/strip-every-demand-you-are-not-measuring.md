---
name: duo-inclusive-access-strip-every-demand-you-are-not-measuring
summary: Every incidental requirement gets scored alongside the real skill; difficulty of content and difficulty of experience are separate dials.
metadata:
  internal: true
---

# Strip Every Demand You Are Not Measuring

## Concept

Whatever your product attaches to a task gets measured along with the task. Travel to a location, three uninterrupted hours of concentration, a long scroll, unexplained jargon — none of those are the competence you care about, but every one of them shapes who succeeds. The measurement name for this is *construct-irrelevant variance*: score differences caused by something other than the ability under test. It makes your result less valid and it systematically penalises people whose incidental constraints differ from yours.

The companion mistake is conflating two independent dials. Difficulty of the *content* and difficulty of the *experience* move separately. Lowering the second is not lowering the bar — stress from the interface, the logistics or the duration adds noise to performance without adding signal about the thing you are trying to observe.

## What Duolingo does

Source: blog.duolingo.com/inclusive-testing-technology (Duolingo blog, 2022-01-27; accessed 2026-09-22)

- Traditional English proficiency exams run roughly **3 hours, in person, with limited breaks**. The Duolingo English Test removed the test-centre visit entirely, shortened the exam with computer adaptive testing so it stays rigorous without the three-hour concentration demand, and uses a deliberately plain interface — minimal scrolling, large type — to cut visual and working-memory load.
- Sizing the stake: **26% of Americans, 1 in 4, have a disability**.
- Tension, stated in the post itself: design alone is not sufficient. Even a well-designed test stays inaccessible for some people, so Duolingo still runs a human accommodations team. Interface work reduces the queue; it does not empty it.

Source: blog.duolingo.com/is-the-duolingo-english-test-hard (Duolingo blog, 2021-06-14; accessed 2026-09-22)

- The two dials are an explicit design principle — the content is meant to be challenging, taking it is not. Test-takers sit the exam whenever and wherever they are comfortable rather than at a scheduled centre.

Source: blog.duolingo.com/businesses-use-duolingo (Duolingo blog, 2025-11-26; accessed 2026-09-22)

- **5–10 minute sessions** are what business customers name as the reason frontline staff — restaurant back-of-house, bus operators, paramedics, rail operators — can participate at all, against formal classes nobody can attend. Access to contiguous free time is unequally distributed and correlates with seniority, so a format needing a booked hour filters on calendar rather than on motivation.
- One bartaco employee went from dishwasher to line cook **within seven months** of starting in October 2024.

## The transferable pattern

Write down every demand your task makes on the person beyond the thing you are actually assessing or teaching: where they must be, what hardware they need, how long a block of attention it takes, how much reading, how much unexplained terminology. For each one ask a blunt question — *am I grading this?* If the answer is no, it is noise you are attributing to the person, and it is not distributed evenly.

Then separate the two dials out loud, because your team will fight you on this. Keeping the substance hard while making the wrapper effortless is not a softening; it is what makes the outcome mean what you claim it means. Short, self-contained units are the cheapest version of this move: anything that fits in a gap depends on intent rather than on schedule control.

## Apply to your product

- List every prerequisite to complete your core task once. For each, can you name what it measures that you care about — or is it there because it was convenient to build?
- Does your product need a contiguous block of time? Who on your user list does not control their own calendar, and what happens to them?
- If someone on your team says "making it easier makes it worthless", which dial are they actually defending — the content or the wrapper?

## See also

[[a-precondition-produces-a-zero-not-a-smaller-number]] · [[working-memory-is-already-spent-elsewhere]] · [[audit-fairness-against-the-delivery-context]]
