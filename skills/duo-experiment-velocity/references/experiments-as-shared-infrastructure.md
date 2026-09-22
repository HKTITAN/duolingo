---
name: duo-experiment-velocity-experiments-as-shared-infrastructure
summary: Template setup, eligibility, hypothesis and nightly analysis into one internal service so learning rate scales with traffic instead of headcount.
metadata:
  internal: true
---

# Experiments as Shared Infrastructure

## Concept

Most teams treat each experiment as a small project — someone wires up the split, someone else defines eligibility, an analyst writes a bespoke query, and the readout arrives as a deck. That is a fixed cost paid again per test, and it is why a team that genuinely believes in testing still runs three tests a quarter. The alternative is to build the experiment as a product surface once — a form, a standard eligibility model, a required hypothesis, a report template, automated nightly analysis — and let every team run tests through it. The per-test cost collapses to the part that is actually specific to the test, and the rate at which the organisation learns becomes a function of how much traffic it has rather than how many analysts.

## What Duolingo does

Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

- Duolingo built a company-wide internal experiments service with a UI that walks the owner through naming the experiment, defining the arms, setting eligibility, stating a hypothesis, and picking a report template. The service then auto-generates a statistical report **every night for every running experiment** — nobody queues behind an analyst for a readout.
- Volume that the shared service produced: **over 2,000 experiments in its first three years**, with **a few hundred running simultaneously** in a given week, and **750+ A/B tests per quarter as of 2025**.
- The stated tension is a consequence of the win. Once hundreds run at once, the hard problem stops being running tests and becomes gathering and synthesising data points across all of them — which is exactly what forced the per-type report template design (see [[curate-the-report-per-experiment-type]]).
- The shared substrate is also institutional memory. Past experiment data is visible to everyone, and PMs form and test a hypothesis for anything from a copy change to an entirely new section of the app, so decisions get argued from what was already tried rather than from seniority (blog.duolingo.com/why-i-interned-at-duolingo-rebecca-hu-product-management-intern (Duolingo blog, 2022-08-26; accessed 2026-09-22)).
- The thing that erodes the substrate is branching. Duolingo calls market-specific customisation *forking the app* and reserves it for cases that are necessary or a big enough win, such as WeChat login in China. Its Asia teams instead ran local research and market-level analysis, translated findings into experiments tested in one country, and rolled out worldwide when the result held — **doubling the fraction of its learners from Asia over three years**. The cost of a fork, the post says, is not the initial build; it is a slow, hard-to-notice drag on all future development and testing, plus silent breakage when priorities move (blog.duolingo.com/lessons-from-asia-turning-local-research-into-global-experiments (Duolingo blog, 2021-02-02; accessed 2026-09-22)).

## The transferable pattern

- **Pay the fixed cost once.** Assignment, eligibility, exposure logging, significance math and the readout are the same for every test you will ever run. Anything rebuilt per test is a tax on curiosity.
- **Make the analysis automatic and scheduled, not requested.** A readout that someone has to ask for arrives late and only for the tests someone cares about. A nightly report for every live test means a bad result surfaces before anyone is invested in it.
- **Force the hypothesis into the setup form.** It costs the owner one sentence and is the only cheap moment to capture it — after the numbers land, the hypothesis is unfalsifiable by construction.
- **Treat the archive as the product.** Universal read access to past results is what converts a pile of one-off tests into something a new hire can query instead of re-running.
- **Budget for synthesis before you need it.** High volume relocates the bottleneck to reading across results. Plan the aggregation layer as part of the platform, not as a later cleanup.
- **Price a segment-specific fork in future test throughput, not build days.** Every permanent branch multiplies the surface that each later experiment must be defined and validated against, and that drag is invisible on the quarter you approve it.

## Apply to your product

- How many hours of engineering and analyst time does your next experiment cost before it starts collecting data, and which of those hours would be identical for the test after it?
- If someone joined your team tomorrow, could they find out what you already tested in this area without asking a person?
- Which of your permanent per-customer or per-region branches would you approve again if the cost were stated as a percentage slowdown on every future test?

## See also

[[marginal-cost-decides-which-ideas-get-tested]] · [[curate-the-report-per-experiment-type]] · [[../duo-experimentation/references/experiment-cadence]] · [[../duo-localization/SKILL]]
