---
name: duo-adoption-design-structure-the-session-and-let-them-ask-for-the-explanation
summary: Give an open-ended session a narrator that opens, steers and closes it, and make explanation opt-in per instance — offered on correct answers too.
metadata:
  internal: true
---

# Structure the Session, and Let Them Ask for the Explanation

## Concept

Open-ended generation has no natural ending, so users quit rather than finish — and a quit registers as failure even when the time was well spent. The cure is a voice outside the interaction that sets the scene, states what this session is for, pushes it back on track, and ties it off. The mirror-image error is forced explanation: a system that explains every result slows down the users who already understood and trains everyone to dismiss the panel. Structure should be imposed; explanation should be requested.

## What Duolingo does

- Roleplay includes **a narrator alongside the learner and the character** — a non-participant voice. It sets the scene, communicates the learning objective, interjects with new information mid-session, steers the conversation back to the objective, and ties it off at the end.
- The narrator is what makes an unbounded AI conversation feel bite-sized and finished rather than abandoned.
- On explanation: **Explain My Answer** appears as a **button inside both** the green "Correct!" and the red "Incorrect" result popups. Duolingo frames it as **"More control: Choose whether you want feedback on a mistake."** Offering it on correct answers matters — a right answer arrived at by a guess is the most fragile state a user can be in, and it is invisible unless they can ask.
- The same structural trick shows up in the podcast work. The French season on "traditions iconiques" opens by attacking the audience's own model — "But how well do any of us really know France?" — and builds each episode around an unresolved struggle, ending sections on the open question: "Will he succeed? Or will his beloved Grasse become a faded, jasmine-scented memory?"
- Format borrowing supplies the same machinery cheaply: Duolingo chose true crime for its first serialized podcast season because it is among the most popular podcast genres and lends itself to bingeable serialized storytelling, then followed with **"The Rebel Thief," six parts, published November 2021**, aimed at intermediate learners (app Unit 5 and above).
- Tension: borrowing a genre is not free. That season forced a new capability — historical fiction with voice actors, an original score, and a historian on staff — because they had only ever produced stories with living people.

Source: blog.duolingo.com/chatbot-language-practice (Duolingo blog, 2024-03-20; accessed 2026-09-22)

Source: blog.duolingo.com/explain-my-answer-now-free (Duolingo blog, 2026-01-01; accessed 2026-09-22)

Source: blog.duolingo.com/french-traditions-duolingo-podcast (Duolingo blog, 2022-05-24; accessed 2026-09-22)

Source: blog.duolingo.com/duolingo-french-podcast-the-rebel-thief (Duolingo blog, 2021-11-09; accessed 2026-09-22)

## The transferable pattern

For any open-ended surface — a generated conversation, a sandbox, a freeform workspace — add a non-participant voice that does four jobs: states the objective at the start, interjects when the session drifts, steers back, and declares the session complete. The completion signal is the point. Users return to things they finished.

Two amplifiers:

- **An unresolved outcome pulls harder than a well-explained one.** Wrap the work in something with an open loop, and prefer material that argues with what the audience already believes; agreement gets skimmed.
- **Borrow a structure your audience already knows how to want.** You inherit its pacing and shape instead of discovering them. Budget for the new capability the borrowed form demands.

And make explanation a tap, per instance, available on success as well as failure. Automatic explanation costs the confident their flow and teaches everyone to close the panel; requested explanation is read.

## Apply to your product

- Where does your product leave a session with no ending? Who tells the user it is done, and that it counted?
- What is the objective of your most open-ended surface, and is it said out loud at the start or assumed?
- Do you explain results automatically? What would change if explanation were one tap, offered equally when the user got it right?

## See also

[[turn-the-session-into-three-named-buckets]] · [[ship-a-coached-variant-of-the-thing-people-avoid]] · [[../duo-voice/SKILL]]
