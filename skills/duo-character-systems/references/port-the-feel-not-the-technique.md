---
name: duo-character-systems-port-the-feel-not-the-technique
summary: Recognition runs on surface cues, so the technically correct rendering in a new medium reads as a different brand; re-import the old cues deliberately and price the pipeline.
metadata:
  internal: true
---

# Port the Feel, Not the Technique

## Concept

When an identity moves into a new medium — 2D into 3D, static into motion, human-produced into generated — the default output of the new medium is technically correct and wrong. Recognition runs on a small set of surface cues such as flatness, contour and silhouette, not on the underlying construction. A faithful model of a flat character satisfies the modeler and fails the viewer, because the smooth shading that makes it correct is exactly the cue that says "not that character." Deliberately re-importing the old medium's cues is not a regression. It is what preserves identity across the port.

## What Duolingo does

Source: blog.duolingo.com/duolingo-art-intern-animation-case-study (Duolingo blog, 2023-02-24; accessed 2026-09-22)

- Bringing the character Zari into 3D, the generic CG look with smooth shading made her **read as clay** — the model was right and the character was gone.
- The fix re-imported the 2D cues: **toon shaders** to define 3D volume in a cel-shaded way, plus **graphic lines that appear where colours overlap** so limbs stay readable when they cross.
- The experiment was scoped to **one character**, chosen for the right mix of design complexity, 3D appeal and popularity, rather than porting the whole cast at once.
- The pipeline cost is the headline number. A **six-week** timeline through modeling, texturing, rigging and lighting; Zari's rig carries **145 controls**, built so artists with no 3D experience could drive it; the final roughly **10-second animation required 253 rendered frames at 24fps**.

Source: blog.duolingo.com/duolingo-english-test-interactive-skills (Duolingo blog, 2023-05-01; accessed 2026-09-22)

- For generated delivery, Duolingo uses text-to-speech for all spoken test content, and argues consistency as a **fairness** property rather than a cost saving: generated voices "make for a consistent listening experience for test takers, eliminating any unfairness or variation that might come from using human voices." Any variation in how a prompt is delivered becomes unmeasured variance in the score, and it lands unevenly.
- They also used machine learning and computer vision to generate **visemes** — the distinct mouth shapes for specific speech sounds — for animated characters, citing research that combining auditory and visual cues helps people understand what is being said. That animation is doing perceptual work, not aesthetic work.
- Tension: a 145-control rig and 253 frames for ten seconds is the true unit cost, and it recurs. Generated pipelines trade artistic range and per-take nuance for consistency and scale, which is the right trade for scored or high-volume content and the wrong one where performance is the product.

## The transferable pattern

Before porting an identity into a new medium, write down the three or four surface cues your audience actually recognizes it by. Those are usually blunt properties — flat versus shaded, outlined versus not, hard edges versus soft, a specific silhouette. Then treat the new medium's defaults as a hypothesis to be overridden rather than a standard to be met, and add the cues back explicitly.

Two operational rules:

- **Scope the first port to one subject**, picked for a mix of complexity, appeal and familiarity. You are proving a pipeline, not shipping a library, and the first one tells you what the next twenty cost.
- **Budget it as a pipeline build, not an asset.** Rigs, shaders and generation models are infrastructure with ongoing cost. Where you adopt a generated pipeline, name what you are buying — usually consistency, which is a fairness property when every user must be judged on the same basis — and name what you are giving up, which is per-instance nuance.

## Apply to your product

- What are the three surface cues your users would name if asked how they recognize your product at a glance? Would the default output of the new tool preserve any of them?
- If you ported one thing into a new medium as a proof, which one would teach you the most about the cost of the rest?
- Where in your product does variation in how something is presented turn into unfairness between users, and would a consistent generated delivery be an improvement rather than a compromise?

## See also

[[silhouette-first-and-reproducible-from-primitives]] · [[shared-construction-not-shared-subject]] · [[animate-the-confirmation-moment]]
