---
name: duo-localization-reading-direction-is-a-component-problem
summary: Right-to-left support lives in paging and gesture components, not in strings; budget for building the primitive yourself.
metadata:
  internal: true
---

# Reading Direction Is a Component Problem

## Concept

Translating every string and shipping is the cheap half of supporting a right-to-left market. Direction is also encoded in components — which way a pager advances, which way a swipe means forward, which end of a row is the start. If a container does not flip, the copy can be perfect while "next" moves the wrong way. The mismatch is felt on every single interaction, in the primary navigation, by users who have no workaround. And the component you need is often the one your platform never fixed, so treat it as engineering work with its own budget, not as a translation ticket.

## What Duolingo does

Source: blog.duolingo.com/flipping-duolingo-filling-a-gap-in-support-for-right-to-left-languages (Duolingo blog, 2016-09-13; accessed 2026-09-22)

- Android had supported RTL layouts since Jelly Bean, but the widely used ViewPager component never was updated — the feature request sat open for **3+ years**.
- Duolingo needed it for the English-for-Arabic-speakers launch and the component sat on the app's main screen, so a partial flip was not survivable. They built their own pager, RtlViewPager, and released it as their **first open-source project**.
- The market they were building for is large and the payoff was concrete: roughly **650 million native speakers of RTL languages**, and ICEF reporting that Arabic-speaking employees with English skills earn up to **3x** those without in some MENA areas.
- The fix shipped as a reusable primitive rather than a patch inside one screen, which is why it could carry the app's main navigation and be handed to everyone else with the same gap.

## The transferable pattern

- **Audit containers, not copy.** List every component whose behaviour encodes a direction — pagers, carousels, swipe actions, progress indicators, sliders, back gestures, anything with a "next". Each one is a separate piece of work; the string file is not.
- **Assume the platform will not rescue you.** A years-old open request is the normal case, not bad luck. When the primitive you need does not exist, the choice is to build and own it or to not enter the market — pretending a half-flipped screen is acceptable picks the second option without admitting it.
- **Fix it at the primitive, not the screen.** A per-screen workaround has to be re-done by every team that touches it and silently regresses. A replaced component fixes the screens you have not built yet.
- **This is a bimodal defect.** Partial directional support is not partial credit — a user who swipes forward and goes backward is blocked, not inconvenienced. Ship it whole or delay the market.
- Open-sourcing the primitive is a cheap by-product once you have paid for it, and it puts maintenance pressure on more than your own team.

## Apply to your product

- Which components in your product encode direction in their behaviour rather than their styling, and which of them carry primary navigation?
- If a mirrored build shipped tomorrow, what breaks silently — in a way QA reading translated text would not notice?
- Who on the team owns the replacement primitive, and is that work on a roadmap or hidden inside a localization ticket?

## See also

[[layout-overrides-your-content-policy]] · [[localize-to-a-consumption-budget]] · [[../duo-product/SKILL]]
