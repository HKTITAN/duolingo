---
name: duo-memory-and-decay-three-conditions-for-practice-to-pay
summary: Practice earns its cost only if it targets the unmastered, requires active retrieval, and returns feedback immediately; drop one and you are burning the user's time.
metadata:
  internal: true
---

# Three Conditions for Practice to Pay

## Concept

Practice is not automatically valuable. It is valuable when three conditions hold together, and they form a chain — the chain is only as strong as the missing link.

1. **It targets something not yet mastered.** Re-doing what the user already has produces no learning signal and no information for your model. It feels productive to the user, which is exactly the problem.
2. **It requires active retrieval rather than review.** Applying the rule, not reading about it. Re-reading generates fluency, which the user mistakes for mastery.
3. **Feedback returns immediately.** Feedback is what lets an error be corrected before it is consolidated. Delayed feedback arrives after the wrong version has already been stored.

Drop any one and the session is a cost with no return, and — worse — a cost the user experiences as progress.

## What Duolingo does

Source: blog.duolingo.com/grammar-practice-tips (Duolingo blog, 2022-05-17; accessed 2026-09-22)

- Duolingo's curriculum team publishes **five practice principles** framed as applying to anything, not just language: target what is not yet mastered; keep it active by applying the rule rather than reading about it; get feedback on each attempt; practise concepts **separately first and together second**; and practise **slowly first, faster later**.
- The product implements them structurally: lessons focus on one grammar topic and give many examples of one part of a pattern, and each exercise is marked correct or not **as soon as it is finished** rather than at the end.
- A fourth, cheaper mechanism sits alongside these: have the user **teach someone else one small thing**. Duolingo scripts it for friends and family as "Can you teach me how to say thank you in the language you're learning?" and describes the effect as helping learners organize what they know, notice things they would like to know, and lock new information into memory (blog.duolingo.com/how-to-support-a-language-learner (Duolingo blog, 2026-01-06; accessed 2026-09-22)).
- Explaining works because it forces retrieval **plus reorganization** — selecting, ordering and simplifying — which exposes the gaps that recognition-based practice hides. The status flip is a second, independent effect: being briefly the expert is a confidence input your product cannot supply by praising the user.

**The tension.** All three conditions push toward difficulty, and difficulty is the enemy of completion. A session that is entirely unmastered material, entirely unaided, with instant correction on every attempt, is the most efficient session you can build and one many users will abandon. Efficiency per minute and minutes spent are in direct conflict here, and the right answer is a mix, not a maximum.

## The transferable pattern

1. **Score every practice surface against all three conditions.** Most fail on the first: they re-serve content the user has demonstrably mastered because that content is what exists.
2. **Feedback latency is a design number.** Per-attempt beats per-session beats per-week, by a lot. If your feedback arrives after the user has left, it is documentation.
3. **Isolate before you combine, and slow down before you speed up.** Compound tasks hide which component failed, from the user and from you.
4. **Add a teach-it surface.** Asking a user to explain one small thing to someone else is close to free to build and does work that no additional round of drilling does.
5. **Do not maximize any one condition.** Deliberately mix in some already-mastered material to keep the session survivable. The optimum is not the extreme.

## Apply to your product

- Take your main practice or review surface: which of the three conditions does it actually satisfy? Be strict about condition one.
- What is your feedback latency per attempt, measured — not intended?
- Is there any place in your product where a user explains something to another person? If not, what is the smallest version of that you could ship?

## See also

[[retrieval-not-re-exposure]] · [[own-errors-are-the-highest-value-practice-set]] · [[../duo-gamification/references/anti-grind]]
