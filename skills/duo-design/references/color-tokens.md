---
name: duo-design-color-tokens
summary: Role-and-value split — a token names what color does, not what it looks like; the brand can evolve without rewriting screens.
metadata:
  internal: true
---

# Color Tokens

## Concept

A color token system has two layers:

- **Primitive tokens** — the actual colors (`green-500`, `red-400`, `gray-100`).
- **Role tokens** — what each color does (`feedback-success`, `feedback-error`, `text-primary`).

Components reference *role* tokens, never primitive ones. The result: the brand can evolve (swap green for teal) without touching every screen, and accessibility audits become tractable (you can audit roles, not occurrences).

## What Duolingo does

- The design system uses role-named tokens — feedback states, surface tiers, character-associated palettes — rather than literal color names in components.
- Brand evolutions over the years (subtle palette refinements) ship without breaking screens, because the role tokens hold the contract.
- Dark mode and accessibility variants are alternate value layers behind the same role names.

## The transferable pattern

Three rules:

1. **Components reference roles, not primitives.** A button knows it wants `feedback-success`, not `green-500`. The mapping is centralized.
2. **Token names describe purpose, not appearance.** `surface-elevated` outlasts `gray-50`. The first survives a redesign; the second doesn't.
3. **Themes live behind tokens.** Dark mode, high-contrast mode, brand-evolution mode — all are alternate values of the same role names.

Anti-pattern: tokens named for color values (`brand-blue-500`). The first redesign breaks every consumer.

A useful test: rename one of your primitive tokens (e.g. `green` → `teal`). Does anything in your product break? If yes, you have role-leakage.

## Apply to your product

- Do your design tokens describe role or appearance? When you read a component, can you tell what the color *does* without seeing it?
- Could you ship a brand color refresh without touching component code?
- Are accessibility variants a separate set of tokens or alternate values of the same tokens?

## See also

[[type-system]] · [[accessibility-default]] · [[../duo-product/references/polish]]
