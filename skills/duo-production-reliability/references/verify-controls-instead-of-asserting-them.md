---
name: duo-production-reliability-verify-controls-instead-of-asserting-them
summary: Run internal functions as advisors who continuously test whether their controls actually work, and pay outsiders to attack with full source and privileged access rather than black-box.
metadata:
  internal: true
---

# Verify controls instead of asserting them

## Concept

Two habits make an internal function — security, platform, compliance, legal — into something teams route around. The first is being a gatekeeper: if the function's job is to approve, teams learn to hide risk and to arrive late, which destroys the information the function needs to be useful. The second is asserting controls rather than testing them, which means the only thing that ever proves a control wrong is a real incident, purchased with real damage. The alternative is an advisor who pushes accountability to the team closest to the problem and then continuously tests whether the controls do what everyone claims, letting the failures set the next quarter's work. And when you buy outside testing, buy findings rather than a grade.

## What Duolingo does

Sources: blog.duolingo.com/life-at-duolingo-matt-brandman (Duolingo blog, 2023-05-26; accessed 2026-09-22) and blog.duolingo.com/duolingo-english-test-security (Duolingo blog, 2021-09-02; accessed 2026-09-22)

- Duolingo's security team runs **hypothesis-driven security**: orchestrating systems and tests to confirm controls work as intended, then using the outcomes to direct new work — closing observability gaps and provable-security gaps that the tests expose.
- They **dogfood their own controls**, and ship both user-facing and developer-facing work rather than only policy. The stated aim is that teams **feel comfortable and safe engaging with us**, which is the operational definition of advisor rather than gatekeeper.
- The forcing constraint is scale of change: Duolingo ships **hundreds of changes every quarter**. No approval-based function can sit in front of that without becoming either a rubber stamp or a bottleneck.
- For external testing they gave penetration testers **the desktop app, high-privilege backend accounts, and the actual source code for both**, for **six weeks** of attacks on authentication, session management, data protection, and client and server code — and committed to repeating it regularly.
- Numbers: **6 weeks** of full-knowledge testing; **only minor vulnerabilities found, all resolved within a month**.
- Why full-knowledge rather than black-box: a black-box tester who fails has told you only that they failed in the time allotted. Handing over source and privileged access buys you findings instead of a grade.
- Tension, stated plainly: **no assessment company can claim to be unhackable**. The goal is reducing risk, not eliminating it, and they note it is almost impossible to anticipate every threat. The advisor model also requires accepting churn — the team is explicit that it **cannot be afraid to pivot or throw out projects that were relevant yesterday**.

## The transferable pattern

1. **Advise, do not approve.** Push accountability to the team closest to the problem. A function that gates gets routed around and stops seeing the risk it exists to manage.
2. **Earn disclosure.** Honest early conversations are the function's main input. Anything that makes teams reluctant to come to you is a direct loss of information.
3. **Test your own controls continuously.** Treat "this control works" as a hypothesis with an experiment attached, not as a statement in a document.
4. **Let proven gaps set priorities.** Work chosen from test failures beats work chosen by whoever argued most persuasively in planning.
5. **Buy findings, not grades, from outside testers.** Give them source, credentials and privileged access. Blind testing measures the tester's luck as much as your exposure.
6. **Publish the limits.** Saying you cannot be certain is what makes the rest of your claims credible, and it keeps people from treating a passed test as a guarantee.
7. **Accept the churn.** Adversaries and systems move, so some of this quarter's work will be obsolete before it ships. Sunk-cost attachment is the failure mode here.

## Apply to your product

- Does your security, platform or compliance function approve things or advise on them? Ask a team whether they tell that function about risk early or late.
- Pick one control you believe is in place. What test would prove it works today, and when did anyone last run it?
- If you commission external testing, are you giving them enough access to find real problems — or buying a report that says they did not get in?

## See also

[[continuous-qa-for-always-on-systems]] · [[long-incidents-need-a-different-playbook]] · [[../duo-culture/SKILL]]
