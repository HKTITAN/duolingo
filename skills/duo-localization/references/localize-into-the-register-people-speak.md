---
name: duo-localization-localize-into-the-register-people-speak
summary: Ship the words users actually say, checked against your least software-fluent user, not the formally correct translation.
metadata:
  internal: true
---

# Localize Into the Register People Speak

## Concept

A technically correct word your users do not actually use costs them a parse, and in onboarding every parse is a chance to drop out. In many markets the vocabulary people genuinely use for software and for your domain is borrowed from another language, so the "proper" translation is the harder one — a formally flawless string can be less comprehensible to a native speaker than a loanword written in their own script. The target is comprehension, not correctness, because comprehension is what gets the user to the next screen.

## What Duolingo does

Source: blog.duolingo.com/language-learning-for-the-next-billion-duolingo-in-india (Duolingo blog, 2020-09-24; accessed 2026-09-22)

- User research found the Hindi interface was too hard for native Hindi speakers. The in-app currency carried a formal Hindi word (transliterated *mani*) while users called the thing a "coin" or a "diamond".
- Duolingo replaced Hindi terms in onboarding with the English words users already said — "language", "level" — written in Roman script.
- The swap produced a **+1% increase in onboarding completion**. The strings got less correct and the funnel got wider.

Source: blog.duolingo.com/product-principles (Duolingo blog, 2024-02-21; accessed 2026-09-22)

- Product teams run a standing check against the typical global user — someone who may have owned an Android phone for a month — asking whether that person will understand the main action button and the on-screen copy, and whether a feature name survives translation.
- **About half the time**, teams find they have to correct toward the international, older, or low-tech-literacy audience. The check is not a rubber stamp; it changes the design in roughly one review out of two.

Source: blog.duolingo.com/latin-alive-and-ready-to-be-learned (Duolingo blog, 2019-08-28; accessed 2026-09-22)

- The Latin launch post opens on what the reader already owns rather than what they must acquire — why a tooth specialist is a "dentist" and not a "toothist", and the e.g., i.e., etc., *carpe diem* and "Re:" the reader uses every day.

## The transferable pattern

Three moves, in order of how cheap they are:

1. **Ship the register, not the dictionary.** Find out what users call the objects in your product — in interviews, in support tickets, in their reviews — and use that, including borrowed words. A reviewer optimising for formal correctness will flag it; the funnel is the tiebreaker.
2. **Review every screen against the least capable user you serve, not the median and never yourself.** Reach is set by the hardest case. Two questions cover most of it: will they know what this button does, and does this name survive translation?
3. **Open by inventorying what they already hold.** People decide whether to start from their estimate of the distance to competence. Showing them they are already partway there revises the estimate without changing the work.

The cost is real — your product's vocabulary drifts from the official terminology of the domain, and you will defend that choice repeatedly.

## Apply to your product

- Take your three highest-traffic screens. Which noun on each is a word your team invented or translated, rather than a word you have heard a user say out loud?
- Who is the least software-fluent person who can still succeed with your product, and when did anyone last put a screen in front of them?
- What does a new user already know that maps onto your domain, and does your first screen mention any of it?

## See also

[[localize-to-a-consumption-budget]] · [[layout-overrides-your-content-policy]] · [[../duo-inclusive-access/SKILL]]
