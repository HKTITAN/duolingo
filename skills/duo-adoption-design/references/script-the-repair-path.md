---
name: duo-adoption-design-script-the-repair-path
summary: Products teach the happy path and skip recovery; supply the exact words for predictable friction points, with the condition under which the script should be abandoned.
metadata:
  internal: true
---

# Script the Repair Path

## Concept

Curricula, onboarding flows and help centres are all built around the intended sequence, so failure states are under-documented relative to how often they happen and how much they cost. A user who can complete the task but cannot recover from a small failure is stranded at exactly the moment they most needed the product to have prepared them — which is worse than never having started. The cost of a common mistake is mostly the paralysis it causes, not the mistake. Supply the exact move, in advance, for the moment it will be unaffordable to invent one.

## What Duolingo does

- A Duolingo engineer describes finishing the **entire Polish course** — a user since **2013**, studying daily for months before a **2019** trip — and being competent enough to buy a kiełbasa in a village shop. Then it fell on the ground, and he had no idea how to say "mine fell on the ground, may I have another?" He stopped and looked up "spadła" and "ziemię" in a paper pocket dictionary.
- The course had covered the transaction and skipped the repair.
- For the predictable friction of getting answered in English, Duolingo supplies exact prepared lines in **both registers** — informal "Lass uns doch lieber Deutsch sprechen", formal "Ich möchte mein Deutsch üben. Könnten wir bitte auf Deutsch sprechen?"
- Tension, and Duolingo states it rather than hiding it: the script comes with an **override condition**. Holding the line is wrong when explaining symptoms to a doctor, talking to police, discussing allergies, or holding up a supermarket queue. Safety-critical or queue-blocking situations mean give in.
- For the most common recoverable error in email, the guidance is a canned line rather than advice: "Made a mistake in an email? Don't panic! Just send a corrected version and write **'Please disregard the previous email'** at the beginning." The same guide supplies ready-made constructions for other awkward moments, including "I'm looking forward to your reply," described as a way "to create a gentle sense of urgency."

Source: blog.duolingo.com/learning-polish-family-reunion (Duolingo blog, 2026-06-01; accessed 2026-09-22)

Source: blog.duolingo.com/people-switch-to-english-when-i-want-to-practice (Duolingo blog, 2024-08-20; accessed 2026-09-22)

Source: blog.duolingo.com/tips-for-emails-in-english (Duolingo blog, 2024-10-02; accessed 2026-09-22)

## The transferable pattern

Audit for the repair path, not just the happy path. The question is not "can the user do this?" but "what does the user do when this goes wrong in the ordinary way?"

The script has to be exact. General encouragement arrives in real time, under pressure, when the user has no capacity to compose anything — so they take the path of least resistance and abandon the goal. A pre-authorised phrase or a pre-authorised sequence removes the composition cost at the moment it is unaffordable, and removes the judgement call entirely.

Three properties of a good repair script:

1. **It is verbatim.** Copyable, sendable, clickable. Not a description of what to do.
2. **It comes in more than one register** where the situation has social stakes — the wording that works with a peer is not the wording that works with an authority.
3. **It carries its own override condition.** Name the cases where the scripted move is the wrong move. A script without limits gets applied in the emergency it was never meant for, and that failure is much more expensive than the one it prevented.

Publish the recovery for your single most common user error. That one artifact usually outperforms a whole help section.

## Apply to your product

- What is the most common way your users' work goes wrong, and what exactly do you tell them to do — in words they can use, not principles they must apply?
- Where does your onboarding stop? Does it end at "task completed," or does it cover the first ordinary failure after that?
- For each script you supply, when is following it the wrong call — and do you say so alongside the script?

## See also

[[every-context-gated-step-needs-a-skip-and-a-fallback]] · [[social-features-die-in-empty-boxes-and-one-way-relationships]] · [[../duo-product/references/intuitive-by-default]]
