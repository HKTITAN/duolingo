---
name: duo-streak-mechanics-scheduled-pause-at-the-known-dip
summary: Ship a sanctioned pause timed to land where your own usage data already dips; permission to skip raises long-run usage.
metadata:
  internal: true
---

# Scheduled Pause at the Known Dip

## Concept

Every product has a predictable trough — a day of the week, a season, a stage in the customer's calendar when usage falls for reasons that have nothing to do with your product. An unforgiving chain converts that trough into mass breakage: the same people lose their accumulated investment on the same day, every cycle, and a good share of them never restart.

The move is to find the dip in data you already have and ship a sanctioned pause aimed at it. Not slack the user has to ration — a pause that is explicitly allowed, timed, and understood. It carries the sunk investment across the gap instead of destroying it.

## What Duolingo does

Source: blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals (Duolingo blog, 2017-05-10; accessed 2026-09-22)

- Duolingo's usage peaks midweek and falls at weekends — **weekend daily actives run 5-10% below midweek**. The pause was designed against that measured shape.
- The **Weekend Amulet** A/B test offered an equippable store item every Friday that preserved the streak across an unused weekend. Learners offered it were **4% more likely to return a week later** and **5% less likely to lose their streak**. Treat this as an experiment result from 2017, not a description of the current app.
- The post calls the finding counterintuitive, and pairs it with a second one that cuts against session-maximising instincts — learners who **binge** lessons are **much more likely to abandon** the app than learners who pace themselves. The mechanic that maximises short-run session count is not the one that maximises survival.
- **The extreme case.** During the 2022 invasion of Ukraine, learners there wrote in worried about their streaks while still finding ways to keep going; Duolingo **froze streaks for all learners in Ukraine** (blog.duolingo.com/duolingo-statement-ukraine (Duolingo blog, 2022-03-14; accessed 2026-09-22)). When a defined group physically cannot comply, suspending the clock for them is the only version of the mechanic that is not cruel.

## The transferable pattern

- The dip is already in your data. Look at your own activity by day-of-week, by month, by account lifecycle stage, and place the pause where the trough is rather than where it feels generous.
- A pause is not the same instrument as a recovery token. The token covers a random bad day the user did not see coming; the pause covers a structural gap you both know is coming. Products with a strong seasonal shape usually need both.
- Build a **segment-level suspend** you can trigger operationally, for outages, disasters, or any period where a group of users cannot act. A commitment device that punishes people who physically cannot comply turns your best motivator into a reason to leave.
- Watch the opposite failure. A mechanic that rewards cramming can inflate your activity chart while lowering survival, so keep a pacing or burnout guardrail on any streak experiment.

## Apply to your product

- Plot your activity by day of week and by month — where is your reliable trough, and what share of chain breaks happen inside it?
- What would a sanctioned, pre-announced pause look like for that window, and would you rather users take it or silently break?
- Can you suspend the counter for a named segment tomorrow without a code change, if an outage or an external event makes compliance impossible?

## See also

[[scarce-recovery-token]] · [[trivial-floor-protects-the-chain-not-the-outcome]] · [[../duo-retention/references/churn-diagnostics]] · [[../duo-experimentation/references/guardrail-metrics]]
