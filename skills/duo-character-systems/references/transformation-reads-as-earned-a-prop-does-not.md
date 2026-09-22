---
name: duo-character-systems-transformation-reads-as-earned-a-prop-does-not
summary: Mark a milestone by transforming the thing the user identifies with, not by handing it an accessory — a change of state reads as earned, a prop reads as decoration.
metadata:
  internal: true
---

# Transformation Reads as Earned, a Prop Does Not

## Concept

There are two ways to mark a milestone visually. You can give the user's avatar, badge or mascot something — a trophy, a number, a balloon — or you can change what it is. These feel similar in a spec and land completely differently. A prop is something handed over, and it could have been handed to anyone; it decorates the achievement without asserting anything about the person. A transformation implies the milestone changed you, which is precisely the feeling the milestone is supposed to produce.

## What Duolingo does

Source: blog.duolingo.com/streak-milestone-design-animation (Duolingo blog, 2022-01-21; accessed 2026-09-22)

- Duolingo's earlier streak-milestone artwork showed Duo **holding number balloons** — the prop approach, where the number is carried rather than embodied.
- The redesign replaced it with Duo **physically transforming into a flaming phoenix** on milestone days. The mascot does not receive the milestone; it becomes something else because of it.
- The team framed this internally as treating milestones **like power-ups in a video game**. That grammar does two jobs without any copy: it says the state is a reward, and it says the state is temporary and repeatable, so the user knows another one is reachable.
- Milestones are placed on a fixed ladder — **1 week, 1 month, 50, 100, 365 days and beyond** — not at every increment.
- Tension: transformation is far more expensive per milestone than a prop. A prop can be swapped by changing one layer; a transformation is new artwork and new animation each time. The fixed ladder is not only a motivation design, it is what makes the production cost survivable.

## The transferable pattern

When you mark an achievement, ask what the user identifies with in your product — their avatar, their workspace, their profile, their progress counter, the object they have been building — and change *that* rather than attaching something beside it.

Three design consequences follow:

- **Borrow a convention the user already reads.** The power-up idiom communicates reward, impermanence and repeatability with no text at all. Any widely recognized idiom will do the same work; inventing a private one means explaining it.
- **Make the transformation temporary and recurring.** A permanent change is consumed once and then becomes the baseline. A state the user enters, enjoys and exits leaves something to come back for, and it lets you reuse the moment on a ladder.
- **Space the ladder to fit production cost.** Every rung is a distinct piece of work, so the ladder has to be short enough that each rung is actually good. A long ladder of cheap, near-identical rungs is the prop approach wearing a costume.

The honest tradeoff: if you cannot afford to build a distinct state for each rung, a well-made prop system beats a transformation system executed at half quality. Choose by budget, not by ambition.

## Apply to your product

- What does the user in your product actually identify with, and have you ever changed it — or do you only ever add things next to it?
- Which of your achievement states are permanent? Would any of them do more work as something the user enters, keeps for a while, and can reach again?
- How many distinct milestone states can you build at full quality this year? Set the ladder to that number and no more.

## See also

[[animate-the-confirmation-moment]] · [[test-the-central-metaphor-for-legibility]] · [[../duo-retention/SKILL]]
