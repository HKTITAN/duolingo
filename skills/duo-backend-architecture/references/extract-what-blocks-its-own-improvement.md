---
name: duo-backend-architecture-extract-what-blocks-its-own-improvement
summary: If changing one subsystem requires redeploying nearly everything, it will never be improved — extract it first and the optimization follows.
metadata:
  internal: true
---

# Extract What Blocks Its Own Improvement

## Concept

Deployment coupling is a tax on every experiment. If touching one subsystem means redeploying nearly everything, the expected value of trying anything against it falls below the cost of trying, and the component ossifies — not because it is hard, but because nobody will bother. Extraction does not make that code faster. It makes iteration cheap enough that someone will make it faster, and cheap enough to survive breaking it on a Friday. The same logic governs the language or framework you extract it into: pick for how legible the system becomes, not for how quickly a newcomer can pick up the syntax.

## What Duolingo does

Source: blog.duolingo.com/how-i-saved-duolingo-40000year-in-my-summer-internship (Duolingo blog, 2017-09-30; accessed 2026-09-22)

- Challenge statistics were embedded in Duolingo's core mass of code, so deploying **any** change to them required deploying **almost everything**. Moving them into a specialized separate service let the team modify it independently.
- The safety this bought is the point: the intern **broke the service twice** during the experimentation period, **reverted to the monolith code path for a weekend**, and restarted on Monday. The ability to fall back is what made the breakage survivable — extraction without a revert path is just a smaller blast radius for the same fear.

On choosing what to extract into, Duolingo ported its lesson-generation engine from Python to Scala despite Scala's reputation for a steep learning curve. The reasoning: onboarding time is the sum of learning the tool plus learning the system, and in a genuinely complex system the second term dwarfs the first — so pick the tool that makes the system's logic legible and accept the steeper tool. Static typing also shortened the deploy-find-bug-fix loop that dynamic typing had forced. **The costs they name:** library documentation was missing or scattered, integrations with the surrounding ecosystem often did not support the new language's native constructs, the rewrite **halted new feature development for months**, and they concede it was still too early to say whether the rewrite would actually reduce future technical debt (blog.duolingo.com/rewriting-duolingos-engine-in-scala (Duolingo blog, 2017-01-31; accessed 2026-09-22)).

## The transferable pattern

1. **Find the components nobody has improved in two years and ask why.** The answer is usually deployment coupling, review burden or test-suite runtime — not difficulty. Those are the extraction candidates.
2. **Extract for iteration cost, not for purity.** The justification is "this will let us try five things a week instead of one a quarter," which is measurable, unlike architectural elegance.
3. **Keep the old path alive during the experimental window.** A fast revert to the previous implementation is what converts a risky rewrite into an ordinary week. Extraction plus a flag to fall back is the complete pattern.
4. **Choose the tool by comparing two learning curves.** How hard is the tool to learn, against how hard the domain already is? Where the domain dominates, optimize the tool for readability and maintainability and accept the steeper ramp. Where the domain is simple, the fear of onboarding cost is correct.
5. **Price the freeze.** A rewrite that stops feature work for months is a real product cost, and the debt reduction it promises is a hypothesis, not a result. Say both out loud when proposing it.
6. **Check the surrounding ecosystem, not just the tool.** A well-chosen runtime with thin documentation and integrations that do not support its native constructs will cost you in places the language comparison never mentioned.

## Apply to your product

- Which part of your system requires redeploying the most unrelated code to change, and when was it last improved?
- If you extracted it, could you revert to the old implementation in minutes — and if not, is the extraction actually safer than the status quo?
- For your next significant rewrite, which is steeper: the learning curve of the tool you are considering, or of the domain a new engineer must learn regardless?

## See also

[[delete-dependencies-from-the-request-path]] · [[pitch-migrations-in-the-sponsors-currency]] · [[../duo-culture/SKILL]]
