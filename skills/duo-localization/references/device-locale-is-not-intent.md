---
name: duo-localization-device-locale-is-not-intent
summary: Device language is a bad proxy for what a user wants, and popularity rankings mostly measure what you made available.
metadata:
  internal: true
---

# Device Locale Is Not Intent

## Concept

Most of what you think you know about demand in a new market is an artifact of a default you shipped. Device language is set once — often by the retailer, often out of aspiration — so it describes a phone, not a person. And a popularity ranking only ranks the options you put on the shelf in a form users could actually take. Before you read either signal as preference, check what your own defaults made possible.

## What Duolingo does

Source: blog.duolingo.com/language-learning-for-the-next-billion-duolingo-in-india (Duolingo blog, 2020-09-24; accessed 2026-09-22)

- **Over 95% of English learners in India had phones set to English.** The signal inverted: the people most likely to want the English course were exactly the population the locale-based default hid it from.
- Because the global-default Play Store listing followed device language, it never mentioned learning English — in a market where **half of existing India learners were studying English**.
- Duolingo shipped a custom India store listing focused on learning English, and ran an experiment surfacing the English-for-Hindi-speakers course at the top of the course list regardless of phone language. The reordering produced **+2% daily active users**.

Source: blog.duolingo.com/2025-duolingo-language-report (Duolingo blog, 2025-12-01; accessed 2026-09-22)

- In 2025 Japanese climbed to the **4th** most-studied language globally, passing German, and Korean to **6th**, passing Italian — the same year those courses first became available directly from speakers' own languages instead of only from English, Japanese and Chinese.
- That year Duolingo launched **148 new courses for speakers of 20+ languages**, reaching 280+ courses across 40+ languages. The ranking moved because supply moved.

Source: blog.duolingo.com/korean-course-updates (Duolingo blog, 2026-07-07; accessed 2026-09-22)

- The Korean rebuild went from **3 source languages to 27**, making **over 9 million more users eligible** for content that already existed and had **1.9 million** existing learners. The same release raised the ceiling to B2 and added transliterations users can toggle mid-lesson.

## The transferable pattern

- **Never infer intent from a device setting.** Pull the actual joint distribution — setting against observed behaviour — for each market before you let a locale drive a store listing, a default, or an ordering.
- **Override in both places.** A market-specific listing gets the right people to install; in-product ordering decides what they see first. Fixing one and not the other leaves the funnel broken in the middle.
- **Read rankings as a map of your distribution.** When a category jumps, ask what you changed about eligibility before you write the trend memo. Preference that had no way to register is not new preference.
- **Widen access to what you already own before funding new content.** Removing an inherited prerequisite — one entry locale, one region, one plan — has no incremental creation cost and compounds against every unit you already built.

Note the boundary. This is about defaults inside your product. Barriers a third party controls — carrier costs, procurement, app-store policy — are a distribution problem, not a localization one.

## Apply to your product

- Which of your defaults is currently deciding what a new user in a foreign market sees first, and what evidence backs it beyond the device setting?
- If you plotted your top-selling items per market against which items were actually purchasable there, how much of the ranking survives?
- What already-built part of your product is gated behind one entry locale, region or prerequisite, and what would eligibility look like without it?

## See also

[[a-winning-message-is-valid-only-where-it-won]] · [[localize-into-the-register-people-speak]] · [[../duo-growth/SKILL]]
