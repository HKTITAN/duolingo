---
name: duolingo
description: Route a product, habit, learning, growth, brand, team, or engineering question to the right Duolingo skill — and say which one and why.
---

# /duolingo

Load `skills/duolingo/SKILL.md` and follow it in order. Do not summarize the router — execute it.

1. Run the **Gate** table first, top to bottom. First match wins; if one fires, take it and stop.
2. Otherwise classify the **posture** (Diagnose / Build / Decide / Critique / Explain) — this decides the shape of the answer — then the **material** row.
3. Name **one or two** skills, one line each on why, then actually run them. Never load four.
4. Before answering, apply `skills/duolingo/references/translate.md`: the user is not building Duolingo, so the answer has to end in *their* product.
5. Cite the node path you used.

If the user passed an argument, treat it as the question. If they passed nothing, ask what they're working on — one short question, not a menu.

Design, UI, motion, layout, type and colour questions leave this pack: follow `skills/duolingo/references/design-handoff.md`.
