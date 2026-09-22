---
name: duo-localization-rewrite-rather-than-default-the-assumption
summary: When a translation forces you to assert something about the user, rephrase around it instead of picking a default.
metadata:
  internal: true
---

# Rewrite Rather Than Default the Assumption

## Concept

Some languages will not let you write a neutral sentence. Greet the user and the grammar demands you commit to a fact about them — their gender, their number, their formality relationship to you — that you do not have and do not need. Picking a default feels like a small call, but a default is still an assertion, and in high-frequency interface copy it is wrong for a large share of users on every impression. The better move is usually not to choose a side but to rewrite the sentence so the question never arises, using words that are already neutral in that language rather than inventing new ones.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-keeps-its-spanish-localization-inclusive-2 (Duolingo blog, 2021-07-13; accessed 2026-09-22)

- The Spanish localization team replaces the gendered welcome pair (*bienvenido/bienvenida*) with a rephrasing — *te damos la bienvenida*, "we welcome you" — that sidesteps the choice entirely instead of defaulting to the masculine form.
- Achievement names are translated into forms that work for anyone. "Legendary" ships as *Leyenda* (legend, a noun with no gender marking) rather than the gendered *Legendario*.
- They lean on epicenes — words already neutral in the language, such as *estudiante*, *persona* and *especialista* — rather than coining new endings. Native neutral vocabulary reads as natural; invented forms read as a political statement, which changes what the string is doing.
- The scale is why the rounding error matters: **500+ million learners** at the time of writing, seeing these strings on repeat.

Tension, stated in the post: "you can't always win them all." Design and spacing constraints forced them to keep masculine forms for *Filósofo* (Philosopher), *Fotogénico* (Photogenic) and *Vencedor* (Conqueror). And where the neutral rephrasing will not fit the screen, they fall back to a shorter, weaker greeting — *hola* — which is neutral and on-tone but loses the meaning of welcoming someone.

## The transferable pattern

- **Rephrase before you default.** Whenever a target language forces a commitment you cannot back with data, restructure the sentence — change the subject, address the user directly, switch to a noun that carries no marking. This costs nothing at runtime and asks the user for no extra data.
- **Do not collect a field just to fix a string.** Asking every user for an attribute you have no other use for is a worse trade than a rewrite, and it moves a copy problem into your data model permanently.
- **Prefer existing neutral vocabulary to invented forms.** The same intent, expressed with words that were already ordinary, reads as writing; expressed with a coinage, it reads as a stance and changes the register of your whole interface.
- **Weight the fix by frequency.** A string on the first screen of every session deserves a rewrite; a string in a rarely-opened settings pane does not need to block the release.
- **Accept partial coverage in public.** Some strings will not have a neutral form that fits. Name them, keep the list, and be honest that the fallback lost something rather than pretending the constraint does not exist.

## Apply to your product

- Which of your most-shown strings force an assertion about the user in any locale you ship, and could each be rewritten to address them directly instead?
- Are you holding any user attribute purely to render copy correctly — and would a rewrite let you delete that field?
- Where you have already had to accept a default, is that decision written down anywhere a future translator can find it?

## See also

[[layout-overrides-your-content-policy]] · [[localize-into-the-register-people-speak]] · [[../duo-voice/SKILL]]
