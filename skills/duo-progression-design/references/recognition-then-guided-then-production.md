---
name: duo-progression-design-recognition-then-guided-then-production
summary: Within one session, move from picking the right answer to producing it unaided; ending where you started wastes the session.
metadata:
  internal: true
---

# Recognition, Then Guided, Then Production

## Concept

Recognition and recall are different operations with very different costs. Picking the right answer from four options gets the user to a correct representation cheaply; producing it from nothing is what actually consolidates it. Pick one and you lose: pure recognition builds a capability that evaporates the moment real performance is demanded, pure production loses everyone who was not already able. So do not choose between them — order them inside a single session. Prime with recognition, support the middle with a worked example, end with unaided production. The hard retrieval then happens at the point where the user has already been set up to succeed at it.

## What Duolingo does

Source: blog.duolingo.com/language-rules-learning-grammar-on-duolingo (Duolingo blog, 2020-10-02; accessed 2026-09-22)

- In Grammar Lessons, **early exercises have you tap the correct verb ending from a list of options; later in the same lesson you type the ending yourself**. Duolingo names this scaffolding and ties it explicitly to holding the difficulty at "not too hard, but also not too easy."
- The middle stage is a fully worked instance. In Duolingo Math, a harder application of ratios is introduced with **a step-by-step walkthrough of that exact problem type before the learner practises alone**; order of operations is built up in steps rather than stated as a rule. The 7th-grade course spans ratios and proportions, two-step equations and inequalities, negative-number operations, circles and angle relationships, and probability including non-uniform and compound events (blog.duolingo.com/7th-grade-math (Duolingo blog, 2026-07-14; accessed 2026-09-22)).
- Components are separated before they are combined, and accuracy comes before speed: practise two verb groups apart, then together; start with slower self-paced practice before building up to real-time practice (blog.duolingo.com/grammar-practice-tips (Duolingo blog, 2022-05-17; accessed 2026-09-22)).
- The low-pressure production mode is offered before the real-time one. Duolingo frames writing as the safe counterpart to speaking — both require retrieval, but writing "gives you the time to think carefully about what you want to say" and to go back and edit, described as "a safe space to help you train your brain for situations where you need to speak" (blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-writing-skills (Duolingo blog, 2026-07-02; accessed 2026-09-22)).
- At the production end, Duolingo makes **"only use what you already know" the crucial first rule** of its 5-step fluency routine, staging practice from isolated known items to short phrases to narrating your surroundings, with a separate later step for noting what was missing. Acquiring new material and making existing material automatic are different exercises, and running them together degrades both (blog.duolingo.com/learn-to-think-in-new-language (Duolingo blog, 2024-05-28; accessed 2026-09-22)).

## The transferable pattern

Structure a single session as three stages, not one:

1. **Recognition.** The user selects, sorts, or identifies. Cheap, high success rate, establishes the correct representation. This is priming, not learning — do not stop here.
2. **Guided production.** One fully worked instance showing the *decision sequence*, not just the rule, followed immediately by the user doing the next one with the support still visible. A demonstration plus practice is not the same thing as instructions plus practice.
3. **Unaided production.** The support comes off and the user produces from memory. This is where the session's value is.

Two ordering constraints that fall out of it. Separate components before combining them: a user who fails a combined task cannot tell which part failed, so the failure teaches nothing. And add time pressure last, so speed is built on a correct representation rather than automating a wrong one.

One rule for the production stage: forbid reaching for new material. Looking something up mid-attempt breaks the traversal and re-routes the user through the very detour the exercise exists to eliminate. Constrain them to what they already have, and collect the gaps afterwards as input to the next session.

## Apply to your product

- Does your core session end on the same operation it started on? If so, the user is leaving with recognition they will not be able to retrieve.
- Where in your flow does the user get a worked example that shows the decision sequence rather than the finished answer?
- At what point do you add speed or time pressure, and is the underlying representation correct by then?

## See also

[[do-the-real-thing-badly-on-day-one]] · [[scaffold-and-fade-on-a-schedule]] · [[the-crutch-that-makes-you-cheap-to-build]] · [[train-the-shared-bottleneck-where-it-is-cheapest]]
