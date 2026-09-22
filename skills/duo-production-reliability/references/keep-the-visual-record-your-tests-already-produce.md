---
name: duo-production-reliability-keep-the-visual-record-your-tests-already-produce
summary: Your test suite already drives the product into every state on every device and locale, so store the screenshots, make them filterable, and put a one-click report next to each.
metadata:
  internal: true
---

# Keep the visual record your tests already produce

## Concept

The expensive part of seeing your product in every state is already paid for. Automated end-to-end tests drive the interface into thousands of states, across every device, size and locale you support, on every release. Then almost every team throws the frames away, keeping a pass or fail bit. What is missing is not capture but retrieval: storage, and filter axes matching how people actually ask the question. A reviewer wants one screen across every locale. A designer wants one locale across every device. Once those axes exist, an archive becomes a tool — and if a report button sits next to each frame, pre-filled with the exact state shown, the distance from noticing a defect to filing it goes to zero.

## What Duolingo does

Source: blog.duolingo.com/birds-eye-a-powerful-tool-for-exploring-app-screenshots (Duolingo blog, 2021-06-29; accessed 2026-09-22)

- **Bird's Eye** started as a **hackathon demo** and became an internal web app that indexes screenshots from end-to-end UI tests by **journey, interface language, app version, and device** — including **animated GIFs for transitions**, not only static frames.
- Implementation is deliberately cheap: **a Python script builds a manifest**, and the front end does **fast client-side filtering** (using Tamper and PourOver). No search infrastructure, no service to operate.
- Numbers: weekly releases across iOS, Android and Web; tests run in **23 languages on 11 devices and browsers**; **5,000+ screenshots per weekly release and 60,000+ in total**; **about 40 internal users per release**. **Localization team productivity increased 3.5x.**
- The 3.5x is the point. The gain came from retrieval, not from new testing. The same suite, the same runs, the same screenshots — only now someone can pull one screen across 23 locales in seconds instead of installing builds.
- Duolingo extended it to run on **GitHub pull requests**, moving the artifact from "something you can consult" to "something that shows up in review."
- Tension: this is a coverage map, not a correctness check. It shows what the automated journeys reach. States your tests never enter are simply absent, and an archive can create false confidence about exactly those gaps.

## The transferable pattern

1. **Stop discarding the byproduct.** If your pipeline renders the interface to produce a pass or fail, the rendered frames are an asset you are already paying for.
2. **Choose filter axes from the questions people ask.** Locale, device, version, journey, state. The axes are what convert a bucket of files into a tool; a flat folder of timestamped images is worth nothing.
3. **Capture transitions, not just end states.** Many defects only exist mid-animation or mid-load, and a static frame will never show them.
4. **Attach the report action to the artifact.** A frame with a one-click, pre-filled report next to it collapses noticing and filing into a single step.
5. **Put it in the review flow.** An archive someone must remember to visit gets visited during launches. One that posts on a pull request gets used every day.
6. **Build it small.** A manifest file and client-side filtering carried this at 60,000 images. Reach for infrastructure when you have outgrown that, not before.

## Apply to your product

- What visual or structural output does your CI generate and then delete? Would keeping a release's worth of it cost anything meaningful?
- Which review task in your team currently requires someone to build and install the product by hand just to look at one screen?
- If you kept those artifacts, what three filters would people need on day one — and who would be the first user?

## See also

[[make-reporting-free-and-aggregate-every-channel]] · [[gate-the-release-on-internal-telemetry]] · [[../duo-design/SKILL]]
