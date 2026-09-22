---
name: duo-mobile-engineering-generate-the-boilerplate-instead-of-relaxing-the-standard
summary: When an architecture standard raises boilerplate and the team pushes back, fix the boilerplate with compile-time generation — and prefer representations that fail at compile time.
metadata:
  internal: true
---

# Generate the Boilerplate Instead of Relaxing the Standard

## Concept

When a standard raises the cost of every new unit of code, the team will push back, and the pushback is usually correct on the facts. The repeated code often cannot be collapsed into a generic, because the varying part is an implementation detail you are deliberately refusing to expose to callers. So the choice looks binary: keep the standard and pay the typing, or relax the standard and lose the consistency.

There is a third option. Generate the repetition at compile time. That moves it into one tested place, so a change to the pattern propagates everywhere at once and per-instance typos become impossible — you buy back the ergonomics the standard cost you without giving up what it bought.

The same instinct applies one level down, to how you represent failure and concurrency. A representation that makes the bad case visible to the compiler removes a class of bug instead of catching instances of it.

## What Duolingo does

Source: blog.duolingo.com/ios-mvvm-swift-macros (Duolingo blog, 2025-07-10; accessed 2026-09-22)

- Duolingo's iOS Client Architecture team standardized on MVVM, hit boilerplate complaints, **tried helper functions and shared utilities first**, and only then wrote Swift Macros that generate whole data-source implementations off a key-definition.
- **Over 4,300 lines of macro-generated code** in the iOS codebase as of that post, rising since July 2024.
- Named costs: macro-generated code is **not searchable in the IDE**, it adds a learning curve, and the post explicitly says to **exhaust helpers and classes first**. The macro dependency also added **10–20 seconds to clean builds** until they stopped importing it through the package manager.

Source: blog.duolingo.com/real-world-swift (Duolingo blog, 2015-01-07; accessed 2026-09-22)

- Duolingo Test Center was built Swift-only using `Optional<T>` for absence and a hand-defined `Result<T>` throughout networking, I/O and parsing, deliberately avoiding exceptions, force-unwrapping and implicitly unwrapped optionals.
- **~0.2% crash rate over ~2.5 months live**; **~10,634 lines, one developer, ~3 months to 1.0**. Tellingly, the **#1 crash group (~30% of crashes) came from an external Objective-C library and 4 of the top 5 came from Objective-C**, and the 7th most common crash was a platform method throwing an undocumented exception.
- The cost was real and they published it: **no reliable debugger or code completion, frequent IDE crashes, incomprehensible compiler errors, ~14-second iteration time versus 2–3 seconds** for the older app, and language churn forcing fixes on compiler upgrades. They said they would choose it again.

Source: blog.duolingo.com/a-good-read-building-duolingo-abc-for-android (Duolingo blog, 2022-10-06; accessed 2026-09-22)

- Narration assembled from multiple audio files, some paired with simultaneous visual cues, moved from nested callbacks to structured concurrency — suspending functions for sequence, `async` + `awaitAll` for the simultaneous pairs. Callbacks can express "then" but have no vocabulary for "together," so a guarantee like *both of these must finish before the next step* is unexpressible.

## The transferable pattern

- **Treat a boilerplate complaint as a tooling bug, not a discipline problem.** If the standard is right and the typing is the objection, remove the typing.
- **Exhaust the cheap abstractions first.** Shared helpers, base classes, a lint rule. Generation is powerful and costs discoverability — generated code that your search tools cannot find is a real tax on the next person.
- **Encode absence and failure in the type, not in a convention.** "This may be missing" and "this may fail, and here is why" belong where the compiler enforces them; you move detection from production to the keyboard.
- **Reach for structured concurrency the moment two things must happen simultaneously.** Nesting handles sequence at the cost of readability and offers nothing for simultaneity.
- **Publish the costs alongside the win.** The accounts above name slower builds, worse tooling and lost searchability. A team that only hears the benefit will adopt it in the wrong place.

## Apply to your product

- What standard is your team quietly working around, and is the objection about the rule or about the typing it demands?
- Which of your runtime failure modes could be moved to compile time by changing how the value is represented rather than by adding another check?
- Where are you choreographing several async operations with callbacks, and is there a "these must both complete" constraint you currently cannot express?

## See also

[[treat-the-build-loop-as-a-shipped-feature]] · [[mandate-new-code-first-backfill-on-evidence]] · [[prove-the-shape-in-the-hardest-part-first]]
