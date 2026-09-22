---
name: duo-timely-data-publishing-point-your-tool-at-a-public-dataset
summary: Run an internal measurement tool over a public, topical dataset — near-zero cost, and a demonstration rather than an assertion.
metadata:
  internal: true
---

# Point Your Tool at a Public Dataset

## Concept

Most companies with a serious internal measurement tool describe it in a whitepaper nobody reads. The alternative costs almost nothing, because both inputs already exist: the tool is built and the dataset is public. Run the one over the other and publish the output. What makes this different from an ad is that the reader is not asked to believe a claim about the instrument — they are handed its judgments about a subject they already know well, and they check it themselves. Agreement validates the tool far more strongly than any accuracy figure you could quote, and disagreement is a conversation about your methodology, which is also a conversation about your product.

## What Duolingo does

Source: blog.duolingo.com/who-has-the-best-words-a-linguistic-analysis-of-the-democratic-debates (Duolingo blog, 2019-12-19; accessed 2026-09-22)

- The **CEFR Checker** was built by ML engineers for an internal job — grading the difficulty of Duolingo's own course content and Stories so material lands at the right level.
- Duolingo pointed it at the **public transcripts of the 2019 Democratic primary debates**, scoring each candidate's word choice and tracking how it shifted **debate to debate across 6 debates**.
- Output is on the **CEFR A1–C scale**, with **C1 and C2 collapsed into a single "C" tier** by the tool — a real limitation of the instrument, stated rather than hidden.
- The topical subject does the distribution work. The instrument does the credibility work. Neither required new research spend.

The choice of dataset is what makes it land. A candidate transcript is something readers have strong independent opinions about, so every score is immediately testable against their own judgment. A dataset the audience has no feel for would have produced numbers nobody could evaluate, which is a whitepaper with extra steps.

**The cost.** The moment you score named people, the piece stops being about the tool unless you actively steer it back. That is a real risk, and it has its own discipline — see [[say-what-your-score-does-not-mean]].

## The transferable pattern

Four conditions make this play work:

1. **The instrument must already exist for an internal reason.** Building one for the publicity inverts the economics and produces a tool tuned for the demo.
2. **The dataset must be public and current.** Public so nobody has to trust your extract; current so the piece has a reason to exist this week.
3. **The audience must have priors about the subject.** The value is that they can grade your grader. Pick something they argue about.
4. **State the instrument's limits in the same piece.** Where it collapses categories, what it cannot distinguish, what resolution it actually has. This reads as confidence and forecloses the obvious attack.

The general form is a demonstration instead of an assertion. You are not saying the tool is good; you are letting the reader audit it on material they already understand, and letting the topicality carry the distribution.

## Apply to your product

- What do you measure internally that nobody outside has a way to measure, and what public corpus could you run it over this month?
- Which subject would your target buyer have strong independent opinions about, so they can check your output rather than take your word?
- What does your instrument get wrong or blur together, and are you willing to print that in the same post?

## See also

[[say-what-your-score-does-not-mean]] · [[attach-to-a-format-already-circulating]] · [[../duo-measurement-validity/SKILL]]
