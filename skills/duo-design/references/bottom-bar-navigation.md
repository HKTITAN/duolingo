---
name: duo-design-bottom-bar-navigation
summary: A small, stable set of tabs at the bottom of every screen; doesn't move, doesn't change, doesn't surprise.
metadata:
  internal: true
---

# Bottom-Bar Navigation

## Concept

A bottom navigation bar with a small fixed set of tabs (typically four to six) is the most retention-friendly navigation pattern for a habit product. The user has muscle memory for where each thing lives; the bar doesn't move, doesn't reshuffle, doesn't shrink to make room. The cost is that you can only have a small number of top-level destinations — which is a feature.

## What Duolingo does

Source: blog.duolingo.com/learning-asian-language-duolingo (Duolingo blog, 2021-12-16; accessed 2026-09-22) and blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)

- A five-tab bar pinned to the bottom of every screen. A 2021 walkthrough of the Japanese course enumerates it left to right: home (three circles), characters, profile (a face), leagues (a shield), shop (a treasure chest).
- Each tab is a distinct pictogram rather than a generic glyph, and Duolingo's own help copy navigates by shape — "tap the barbell icon in the bottom menu," "click the bell icon at the bottom of your screen," the chest icon for Quests. That instruction only works because the silhouettes are memorable.
- The bar survived the November 2022 home-screen redesign intact. The skill tree became a linear path and Stories lost their own tab and moved into the path, but the bottom bar stayed the navigation contract — it absorbed the change instead of participating in it.
- In the 2026 core-tabs refresh, all four extreme design directions changed headers, color, and layout while the bottom navigation icons stayed fixed across every variation (blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)).

**Where Duolingo breaks its own rule.** The tab set is not actually constant. The characters tab appears only in Japanese and Korean courses; the English Sounds tab (mouth icon) only in the English course (blog.duolingo.com/duolingo-english-sounds-tab (Duolingo blog, 2024-11-20; accessed 2026-09-22)); Practice Hub arrived as a Super-subscriber tab. So the honest version of the rule is that tab *positions* and the core slots are fixed, while the last slot is a deliberate variable — not that the bar never changes.

## The transferable pattern

Three rules:

1. **Stability beats flexibility.** The bar should look the same on day 1 and day 1000. Personalization is fine inside tabs, not in the tab structure.
2. **Five is the cap.** More than five tabs and recognition fails. If you need more, you have a hierarchy problem, not a tab-count problem.
3. **Icons need to be recognizable.** Generic icons are recognizable as nothing. Distinctive icons (especially character-driven) become muscle memory.

Anti-patterns:
- Hamburger menus on consumer products. Hides primary navigation; well-known to reduce engagement of the menu items.
- Tabs that move. Duolingo varies *which* feature occupies its variable slot, but never reorders the fixed ones — muscle memory is built on position, not on membership. Reshuffling positions is the thing that turns navigation into a puzzle.

## Apply to your product

- Does your product have a stable primary navigation? Could a long-term user describe it from memory?
- If you have a hamburger menu, is it because you genuinely have too many top-level destinations, or because the navigation hierarchy hasn't been done?
- Are your nav icons recognizable, or are they generic?

## See also

[[../duo-product/references/intuitive-by-default]] · [[../duo-gamification/references/progression-design]] · [[character-system]]
