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

- Five tabs at the bottom of every screen: Learn (the path), Leagues, Quests, Profile, and a fifth slot that can vary (Stories, Music, etc., depending on user).
- Each tab has a recognizable character or icon — users learn the layout in the first session.
- The bar persists across all primary flows; it's not hidden inside a hamburger menu.
- Tab changes have small calibrated motion ([[juicy-motion]]) — quick enough to not delay, animated enough to feel alive.

## The transferable pattern

Three rules:

1. **Stability beats flexibility.** The bar should look the same on day 1 and day 1000. Personalization is fine inside tabs, not in the tab structure.
2. **Five is the cap.** More than five tabs and recognition fails. If you need more, you have a hierarchy problem, not a tab-count problem.
3. **Icons need to be recognizable.** Generic icons are recognizable as nothing. Distinctive icons (especially character-driven) become muscle memory.

Anti-patterns:
- Hamburger menus on consumer products. Hides primary navigation; well-known to reduce engagement of the menu items.
- Tabs that change based on user state. Users lose their muscle memory; navigation becomes a puzzle.

## Apply to your product

- Does your product have a stable primary navigation? Could a long-term user describe it from memory?
- If you have a hamburger menu, is it because you genuinely have too many top-level destinations, or because the navigation hierarchy hasn't been done?
- Are your nav icons recognizable, or are they generic?

## See also

[[../duo-product/references/intuitive-by-default]] · [[../duo-gamification/references/progression-design]] · [[character-system]]
