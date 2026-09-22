---
name: duo-freemium-monetization-drop-eligibility-checks-on-shared-seat-plans
summary: A shared-seat plan is a referral engine disguised as a pricing tier; every eligibility rule is friction applied to your own acquisition.
metadata:
  internal: true
---

# Drop Eligibility Checks on Shared-Seat Plans

## Concept

A group plan looks like a pricing tier. It is actually a distribution mechanism where an existing paying customer does your acquisition work, chooses the recipients, and vouches for you personally. Every eligibility rule you attach — same household, same surname, same address — is friction applied at the precise moment that customer is trying to hand you new activated accounts. Worse, the rules block the highest-value cases first, because friends, colleagues and roommates are exactly the relationships where the referral is most likely and the shared-address test most likely to fail. And the revenue you are protecting is revenue you were never going to collect from those people individually.

## What Duolingo does

Source: blog.duolingo.com/plus-family-plan (Duolingo blog, 2021-08-30; accessed 2026-09-22)

- The Duolingo Family Plan gives **six full accounts under one annual fee, paid by one manager** — the payer plus up to five invitees, each with a complete separate account rather than a limited guest profile.
- There is **no requirement that members share a household or a surname**. The post names the eligible population as "family, friends, friendly neighbor, even your neighborhood bear" — deliberately absurd, and unambiguous about the policy.
- Invitations go out over **any messaging channel** the manager already uses, rather than through a closed in-product invite system.
- There is a **direct-add path for people sharing a device** — for example children without their own phone — so the plan does not assume one person equals one handset.
- The framing is explicitly positioned against services that do restrict membership, with friends, neighbours and colleagues called out as counting (blog.duolingo.com/friends-social-features (Duolingo blog, 2023-06-06; accessed 2026-09-22)).
- **The tension.** Unenforced eligibility does leak revenue — some of those five seats would have been individual subscriptions. The bet is that seats inside a real social group reinforce each other's usage, and that the retention and word of mouth from an activated group beats the incremental subscriptions you forgo. That bet is worth checking against your own data rather than assuming.

## The transferable pattern

Before you write an eligibility rule, answer three questions.

**What abuse are you actually suffering?** Not the abuse you can imagine. If you cannot measure it today, the rule is protecting against a hypothetical and costing you real seats.

**Is the rule enforceable?** Address and surname checks are trivially defeated by anyone motivated, so they filter honest users and pass dishonest ones — the worst possible selectivity.

**What does each additional seat do for you?** If an extra seat is an activated account inside a group that will reinforce each other's usage, it is worth more than the fee you would have charged that person alone. If it is a passive license with no engagement, the calculus changes and a cap matters more than a rule.

Cap the number of seats, since that is enforceable and legible. Do not police who they are.

## Apply to your product

- What eligibility rules does your group or team plan enforce, and what measured abuse motivated each one?
- What is the retention difference between a lone account and an account inside an active group of yours? If you do not know, that number decides this policy.
- Where does your invite flow live? If it only works inside your product, you are excluding the channels people actually use to vouch for things.

## See also

[[rebrand-the-package-not-the-price]] · [[a-paying-minority-funds-a-complete-free-tier]] · [[../duo-growth/SKILL]] · [[../duo-retention/SKILL]]
