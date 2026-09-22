---
name: duo-experiment-velocity-curate-the-report-per-experiment-type
summary: A per-type report template with a curated metric list plus standing guardrails makes relevance a design-time decision instead of a read-time one.
metadata:
  internal: true
---

# Curate the Report per Experiment Type

## Concept

The instinct at scale is to put every metric you track into every experiment report, on the theory that more numbers are more rigorous. The opposite happens. A report with two hundred metrics is unreadable, so the reader scans until something moved — which means the decision about which numbers matter is made after seeing them, and that is exactly the decision that has to be made before seeing them. The fix is not discipline at read time; it is a template per class of experiment, carrying the short list of metrics that class is supposed to move, plus the universal metrics that apply to everything. Relevance becomes a design-time decision made once for a whole category, and the guardrails become non-negotiable rather than a thing a motivated owner can omit.

## What Duolingo does

Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

- Duolingo's experiments service defines **report templates**. Each template carries a curated list of metrics relevant to that class of experiment, plus the universal metrics that always apply, and the owner picks a template during setup — before any data exists.
- The templates exist because of volume. With **a few hundred experiments running simultaneously**, the binding problem stopped being running tests and became gathering and synthesising results across them, which an everything-metric report makes impossible.
- The guardrail veto is shown with a case where it cost real money. Duolingo ran a promotion that let offline users tap into locked lessons and then see an upsell for its subscription. **Purchase rate rose sharply** — and retention and daily active users **fell**, because the promotion discouraged people from using the app offline at all. They shut it down and iterated rather than shipping it and monitoring.
- The post states the cost rather than hiding it — the experiment was successful from a revenue standpoint and was killed anyway. That only holds if leadership pre-committed to the guardrail, because after the revenue number lands there is always an argument for keeping it.
- Template thinking extends to the arms. When Leaderboards were added to desktop they collided with the existing Friends feature, since both compared progress. Rather than an on/off test, the experiment ran two branches — Friends kept in the sidebar alongside Leaderboards, and Friends moved to the profile page — so the readout answered where the old thing goes, not merely whether the new thing wins.

## The transferable pattern

- **Write the template per class of change, not per test.** Checkout changes, notification changes and onboarding changes each have a small set of metrics they are supposed to move. Fix that list once and every test in the class inherits it.
- **Pick the template before the data exists.** Choosing at setup is what converts "which number matters" from a negotiation into a fact of the report.
- **Standing guardrails belong in every template and may veto a win.** A change that moves the target metric by cannibalising something the target cannot see is the default failure mode of single-metric optimisation, and the owner has no incentive to go looking for it.
- **Pre-commit the veto at the leadership level.** A guardrail that is only enforced when the result is cheap is not a guardrail. Agree before the test that a specific decline overrides a specific win.
- **Keep the list short enough to read in full.** If nobody reads to the bottom, the metrics at the bottom are decoration that makes the report feel thorough.
- **When a change collides with something that exists, make the arms be the resolutions.** An on/off test confounds the value of the new thing with the damage from the collision, so a loss tells you nothing about which one was at fault.

## Apply to your product

- Take your last experiment readout. How many metrics were on it, how many did anyone look at, and who decided which ones counted — the template or the reader?
- What are the two or three metrics that must not decline no matter what a test wins, and has anyone with authority agreed in writing that they override a win?
- Which of your planned changes overlaps with a feature that already exists, and could the arms be the ways of resolving that overlap instead of on and off?

## See also

[[experiments-as-shared-infrastructure]] · [[build-tools-that-can-embarrass-you]] · [[../duo-experimentation/references/guardrail-metrics]] · [[../duo-experimentation/references/metric-selection]]
