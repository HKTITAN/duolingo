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

Source: blog.duolingo.com/shape-language-duolingos-art-style (Duolingo blog, 2020-07-02; accessed 2026-09-22) and blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

- Duolingo has already shipped one full palette inversion: from "static, hard-edged shapes on a light gray background" and muted colors to vibrant colors and rounded buttons on a white background, in a 2018 UI redesign that followed the art style over from Duolingo KIDS. A change of that size is exactly the event a role-token layer exists to absorb.
- Color is treated as load-bearing meaning, not decoration: "with the right colors and composition, the objects we need to illustrate can be clearly communicated with very few cleverly placed vector shapes," and artwork is framed in white negative space so it stays legible on a small screen.
- The 2026 core-tabs refresh built "a framework for all our design elements that could scale across tabs" — header sizes graded by each tab's *purpose*, with title position held constant — rather than one color-and-header rule applied uniformly.
- The named primitive/role token architecture itself is Handbook material (handbook.duolingo.com); the public blog does not document it. Do not cite design.duolingo.com for tokens — that URL redirects to a four-post blog hub, not a live design system.

**The number that makes palette decisions expensive.** Assets are 32% of the Duolingo app binary, and when the team audited the worst offenders, the outliers all had gradients or blurs, which explode in size when exported as PDF vectors (blog.duolingo.com/emerge-tool-app-size (Duolingo blog, 2023-07-14; accessed 2026-09-22)). A flat palette is not only a style position; gradients have a shipping weight.

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
