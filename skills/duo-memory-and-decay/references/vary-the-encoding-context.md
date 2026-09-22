---
name: duo-memory-and-decay-vary-the-encoding-context
summary: A capability rehearsed in one context is retrievable only in that context; varying surfaces, voices and settings builds multiple retrieval routes to the same knowledge.
metadata:
  internal: true
---

# Vary the Encoding Context

## Concept

The brain encodes the surrounding circumstances along with the thing itself. A capability rehearsed only on the couch at 9pm, in one format, presented one way, is reliably retrievable on the couch at 9pm in that format. Everywhere else it is patchy.

Two related failures follow. First, **surface binding**: shown one clean canonical example, the user encodes its accidental properties alongside the essential ones and has no way to tell which is which. Only when the same underlying distinction survives across many different surfaces does it become isolable. Second, **route poverty**: repeating the same item in the same format builds one retrieval route, cued by that format. Encountering the same objective across three different formats builds three.

The design move is to vary aggressively on the dimensions that do not matter, so the dimension that does matter is the only thing left in common.

## What Duolingo does

Source: blog.duolingo.com/why-are-conversations-in-other-languages-so-hard (Duolingo blog, 2024-09-03; accessed 2026-09-22)

- Duolingo advises mixing surfaces deliberately — switching exercise types in-app, podcasts on a walk, side quests and Match Madness, reading the blog in the target language — explicitly to maximize the transferability of the learning to other contexts.
- Rather than one narrator, Duolingo built distinct custom TTS voices for **nine characters across English, Spanish, French, German and Japanese**, on the stated reasoning that out in the world learners interact with people of different ages, genders and backgrounds (blog.duolingo.com/character-voices (Duolingo blog, 2021-08-23; accessed 2026-09-22)).
- The tone lessons make the variation explicit: a grid of **4 speakers each pronouncing the same 8 tone-minimal-pair words** (妈/麻/马/骂, 汤/糖, 吻/问), so the same distinction is heard across four vocal ranges (blog.duolingo.com/chinese-tones (Duolingo blog, 2026-04-28; accessed 2026-09-22)).
- Curriculum designers define a communication goal once and hit it from several surfaces: the Spanish phrase *no hay por qué* appears in a translation exercise, in a dialogue exercise, and again inside an in-story website ad — **one objective, three surfaces** (blog.duolingo.com/duolingo-advanced-stories (Duolingo blog, 2022-10-19; accessed 2026-09-22)).

**The tension, and it is a direct contradiction inside Duolingo's own advice.** For learners studying two similar languages at once, Duolingo recommends the opposite — deliberately *fixing* separate time-and-place contexts per language (one in the kitchen in the morning, the other on the couch after dinner) to prevent interference. Context variability aids transfer; context separation prevents confusion. Which one you need depends entirely on whether your risk is failure to generalize or failure to discriminate, and applying the wrong one makes the actual problem worse.

## The transferable pattern

1. **Vary the irrelevant, hold the essential.** List which properties of your practice item are accidental and randomize them. Whatever survives every variation is what the user will encode.
2. **Define the objective once, deliver it from three surfaces.** Three encounters in three formats beat three encounters in one, at the same cost.
3. **Rehearse in the conditions of real use**, including the awkward ones — noisy, rushed, on a small screen, without the reference open.
4. **Diagnose before you choose.** Are your users failing to apply the thing in new situations, or confusing two similar things with each other? Variability fixes the first and worsens the second. Separation fixes the second and worsens the first.
5. **Do not mistake cosmetic variety for contextual variety.** Different colors on the same template is one context.

## Apply to your product

- What does every one of your practice or review items have in common that the real situation will not supply?
- Can you name one objective in your product and three genuinely different surfaces that could each deliver it?
- Is your users' failure mode generalization or discrimination? Your answer decides whether you should be varying context or fixing it.

## See also

[[retrieval-not-re-exposure]] · [[three-conditions-for-practice-to-pay]] · [[../duo-design/SKILL]]
