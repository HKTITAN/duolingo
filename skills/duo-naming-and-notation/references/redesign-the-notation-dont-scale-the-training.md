---
name: duo-naming-and-notation-redesign-the-notation-dont-scale-the-training
summary: When adoption is blocked by the cost of learning your notation, change the notation — training cost is paid per user forever, design cost is paid once by you.
metadata:
  internal: true
---

# Redesign the Notation, Don't Scale the Training

## Concept

When people cannot use your system until they have been trained on it, there are two places to spend: on more training, or on a cheaper notation. Training cost is paid per user, forever, and it scales linearly with adoption. Notation cost is paid once, by you. So if mastery genuinely requires specialist study, the ceiling on adoption is the size of the specialist class, and no volume of documentation, onboarding or enablement moves that ceiling — it only makes the climb slightly less steep for the people who were already going to climb it.

The second half of this is who should do the redesign. The obvious answer — the resident expert — is usually the wrong one.

## What Duolingo does

- Korean was written with Chinese **hanja**, which required years of Classical Chinese study, so literacy stayed confined to "elites, Buddhist priests, and government officials." Scribes had to overload characters to mean either their Chinese sense **or** just a Korean sound, which made texts ambiguous — the training cost and the ambiguity cost compounded each other.
- King Sejong's answer was not more schools. It was a replacement notation "that anyone could learn without extensive education in Chinese": Hangeul, **commissioned 1443, presented 1446** in *Hunminjŏngŭm* ("The Correct Sounds for Instructing the People"), still marked annually on **October 9**.
- The redesign had an unplanned second payoff: because the new notation recorded sounds directly, scholars now have "essentially perfect knowledge" of how the language was pronounced. A well-designed notation fixes the historical record as a side effect. Source: blog.duolingo.com/history-of-korean-language (Duolingo blog, 2022-08-22; accessed 2026-09-22)
- On who designs well: **Sequoyah**, who could read and write no language at all and spoke only Cherokee, produced a syllabary that took Cherokee literacy to **nearly 100% within 20 years** and directly inspired Canadian Aboriginal Syllabics. **Adlam** was created in **1989** by two Guinean brothers, Ibrahima and Abdoulaye Barry, aged **10 and 14**. The conclusion drawn: "you don't need years of formal linguistic training in order to make an immense contribution." Source: blog.duolingo.com/evolution-of-writing-systems (Duolingo blog, 2025-06-24; accessed 2026-09-22)
- **The tension:** Hangeul shipped with characters that later fell out of use (ᆞ, ᄫ, ᅀ). Even a deliberately designed replacement carries dead surface that has to be pruned later. A redesign is not a one-time payment; it is a smaller recurring one.

## The transferable pattern

If your onboarding keeps getting longer and adoption keeps not moving, stop treating that as an education problem.

1. **Measure the ceiling, not the funnel.** Ask how many people could ever be trained to the required level. If that number is smaller than your target, no funnel optimisation reaches the target.
2. **Price the two options honestly.** Training = hours per person, times every person, forever, plus re-training on every turnover. Redesign = one bounded project plus a migration. The second usually wins earlier than people expect, and loses only when the population is small and stable.
3. **Hand the redesign to a fluent user, not to the expert who built the current one.** An expert optimises for descriptive completeness and internal consistency. A fluent insider optimises for the distinctions that actually get made and drops the ones nobody uses — which is dramatically cheaper to learn, and adoption is bounded by learning cost, not by expressiveness.
4. **Budget for pruning.** Your v2 will ship with elements that turn out to be unused. Plan a deprecation pass rather than pretending the redesign is final.

The failure mode this guards against is a system whose difficulty has become a source of professional identity. The people best placed to fix it are the ones least motivated to.

## Apply to your product

- What is the smallest population that can use your system unaided today, and is your growth target larger than that number? If it is, which is cheaper: another training program, or a second interface with fewer concepts in it?
- Who in your user base is fluent but has no formal stake in the current design? What would they cut?
- Which parts of your current notation exist because they are correct, rather than because someone needs the distinction?

## See also

[[motivated-form-and-one-symbol-one-thing]] · [[name-the-category-for-what-it-does]] · [[../duo-product/references/intuitive-by-default]]
