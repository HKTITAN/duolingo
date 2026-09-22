---
name: duo-measurement-validity-measure-willingness-alongside-capability
summary: For anything users avoid out of fear, willingness to attempt is the gating variable and it moves independently of skill.
metadata:
  internal: true
---

# Measure Willingness Alongside Capability

## Concept

Some behaviours are gated by nerve rather than ability. A user who can do the thing but will not attempt it produces no outcome at all, and a capability-only metric cannot see that — it will show the feature working while the number you actually care about stays flat. Willingness is a separate variable with its own trajectory, and on avoidance-shaped behaviours it is usually the binding constraint. Measuring only the half that is easy to score is how a team ships a demonstrably effective feature into a market that never uses it.

## What Duolingo does

Source: blog.duolingo.com/video-call-research-report (Duolingo blog, 2026-03-30; accessed 2026-09-22)

- Speaking is the skill learners most avoid — the fear of being heard making mistakes keeps able learners silent. So Duolingo's study of its Video Call feature reported **two outcomes, not one**.
- The cohort was English speakers learning Spanish at **Duolingo Score 45–55** — a deliberately narrow band, so that neither outcome could be explained by mixing beginners with advanced learners.
- Learners who did video calls with the Lily character showed **both** greater measured speaking improvement **and** higher self-reported confidence than learners who did regular lessons only. Reporting the pair is the point — capability alone would have left the actual mechanism of the feature undemonstrated.
- The tension, which applies to any self-report: confidence measured right after using a new, novel, attention-grabbing feature is inflated by the novelty and by the obvious demand characteristic of being asked. A confidence delta on its own is weak evidence. It is strong evidence when it moves together with a capability delta measured on a separate instrument, and it is a warning sign when the two diverge.

## The transferable pattern

- **Identify whether your outcome is gated by ability or by nerve.** Anything a user can silently decline — raising an objection, publishing, submitting, asking for help, running the irreversible operation, showing work to a colleague — is gated by nerve, and the ability metric will overstate your effect.
- **Report both, always as a pair.** Willingness alone is a mood reading. Capability alone assumes everyone who can, will. The informative quantity is whether they move together.
- **Treat divergence as the finding.** Capability up and willingness flat means you built a better tool nobody will pick up. Willingness up and capability flat means you built confidence without competence, which is worse than either — users will attempt things they cannot do and absorb the failure as evidence against themselves.
- **Anchor self-report with a behavioural proxy.** Attempt rate, retry-after-failure rate, and time-to-first-attempt cost nothing to instrument, are not subject to the demand effect, and give you something to check the survey against.
- **Ask about willingness before the session, not after it.** A rating collected immediately after a pleasant interaction measures the interaction. One collected at the start of the next session measures what actually carried over.
- **Hold the cohort narrow enough that neither outcome can be explained by composition.** A confidence gain that is really a skill-mix difference is indistinguishable from a real one unless the band was fixed up front.

## Apply to your product

- Which action in your product do users decline rather than fail at — and do you currently measure the declining at all, or only the succeeding?
- If you shipped a feature that made people 20% better at something they are afraid to attempt, would any metric on your dashboard move?
- What behavioural proxy for willingness could you instrument this week without asking anyone a question?

## See also

[[publish-the-component-where-you-lose]] · [[clean-cohort-buys-attribution-costs-generality]] · [[../duo-experimentation/references/outcome-not-engagement]]
