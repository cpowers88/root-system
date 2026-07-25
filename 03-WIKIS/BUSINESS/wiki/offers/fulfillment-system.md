---
type: reference
tags:
  - commercial
  - delivery
stage: phase-3
timeline: reference
---

# Fulfillment System

> How work gets delivered: the 14-step engagement sequence, quality bar, documentation discipline, and the habits that protect margin and reputation.

## Purpose
Define the standard way every engagement is delivered — audit, project, or retainer — so quality is consistent, margins are protected, scope stays controlled, and (eventually) delivery can be done by people who aren't you.

## Key Idea
Fulfillment is where this business is won or lost. Sales gets you one project; **reliable delivery gets you the retainer, the case study, and the referral** — the three assets that compound. The system rests on four disciplines: fixed scope in writing, engineering-grade reliability (error handling, testing, monitoring — [[quality-control-and-risk-gates|Quality Control & Risk Gates]]), documentation as a deliverable, and a measured before/after on every project.

## Why It Matters
- SMB owners have been burned by tech vendors before; **boring reliability is your differentiation**.
- Scope creep and rework are the two biggest margin killers in services; both are fulfillment-process failures, not client failures.
- Nothing in the [[three-year-plan|Three-Year Plan]] works if delivery lives only in your head. Every project delivered "your way, documented" is a brick in the sellable company; every heroic improvisation is not.

## The 14-Step Engagement Sequence
The full arc from first call to retainer. Steps 1–5 are the [[smb-ai-audit-method|audit]] (sold and priced separately); steps 6–14 are the implementation project the audit sells. Every step produces a written output — the output *is* the progress.

| # | Step | Output produced | Your responsibility | Client's responsibility |
|---|---|---|---|---|
| 1 | Intake call | Scoped audit agreement, questionnaire returned | Qualify fit, set scope, price the audit | Honest answers, decision-maker present |
| 2 | Workflow audit | Interview notes, live-observation notes | Run the [[smb-ai-audit-method|audit method]] | Staff access, systems access |
| 3 | Current-state process map | Business flow map ([[smb-ai-audit-method|audit step 2]]) | Map reality, not the org chart's fiction | Confirm the map matches reality |
| 4 | Waste & revenue-leakage diagnosis | Quantified findings table | Conservative dollar math | Validate volumes and rates |
| 5 | Future-state human-agent design | Redesign per workflow: AI first-pass, [[quality-control-and-risk-gates|gates]], [[human-role-redesign|role cards]] | Design the loop, name the metrics | Agree on who owns each new role |
| 6 | Implementation plan | Signed SOW: deliverables, exclusions, baselines, timeline | Fixed scope, "not included" list, success metrics with **baselines captured now** | Sign-off, named internal owner |
| 7 | Tool selection | Stack decision per [[tool-stack|Tool Stack]] rules | Choose boring, client-owned tools; itemize pass-through costs | Approve subscriptions in their name |
| 8 | Build prototype | Working build in sandbox against real sample data | Error handling, retry logic, logging from day one | Provide real historical data |
| 9 | Human review gates | Gate design implemented and tested ([[quality-control-and-risk-gates|the 7 gate types]]) | Acceptance tests written and passing | Nominate reviewers; work the queues in testing |
| 10 | Staff training | Role cards delivered, 2–5 min screen recordings, live session | Train to the role, not the tool ([[human-role-redesign|Human Role Redesign]]) | Attendance mandated by the owner |
| 11 | Launch | Cutover after 1–2 week parallel run | Cutover only at demonstrated accuracy; monitoring live | Run the old process in parallel until sign-off |
| 12 | Measurement period | Before/after metrics vs. step-6 baselines | Honest measurement, 30-day check-in | Keep using the system; report friction |
| 13 | Optimization cycle | Rule/prompt/SOP updates from real exceptions | Calibrate gates, fix the top exception patterns | Log exceptions instead of working around them |
| 14 | Retainer handoff | Signed [[retainer-model|retainer]] + [[05-BUSINESS/03-Case Studies/CASE_STUDY_TEMPLATE|case study]] + handoff package | "Who keeps this running — your team or ours?" | Choose a tier; approve the case study |

**Failure modes by phase:** steps 1–5 fail by skipping the dollars (findings without costs don't convert); steps 6–9 fail by silent scope absorption and missing baselines; steps 10–12 fail by adoption neglect (the system works, nobody uses it); steps 13–14 fail by simply not being done — the beginner classically ships step 11 and walks away, leaving the retainer and the case study on the table.

**Revenue at each phase:** steps 1–5 are paid audit revenue; step 6 closes the project (50% deposit); step 11 collects the balance; step 14 starts the recurring line. The sequence is a revenue instrument, not just a delivery checklist.

## Scope Control
- All change requests in writing, priced (even if the price is $0 — a written "$0 this time" trains the client that changes have cost).
- The "while you're in there, could you also..." reply: *"Absolutely — that's a great candidate for Phase 2. Let me quote it so we keep this phase on schedule."*
- If discovery reveals the scope was wrong (their systems are messier than represented): pause and re-scope immediately, never absorb silently.

## Retainer Fulfillment (Ongoing Work)
- Automated monitoring on everything built; alerts to a single triage inbox/channel
- Monthly per-client checklist: alerts reviewed, fixes logged, enhancement hours applied, gate calibration updated, report sent ([[retainer-model|Retainer Model]] has the report format)
- Track actual hours per retainer client monthly; re-tier when consumption exceeds tier

## Practical Actions
- Create the core templates now: scope doc, client system inventory, handoff package checklist, weekly update format, role card, gate checklist.
- Start a personal **delivery playbook**: after every project write down what you'd repeat and what you'd never do again. This document becomes your training manual at hire #1.
- Capture baseline metrics at step 6 without exception — the habit that makes case studies possible.
- Weekly 15-minute client update (written or call) during any build — silence is where client anxiety and scope drift both grow.

## Beginner Version
One project at a time, delivered fully through all 14 steps — including steps 12–14, which beginners always skip and always regret. Slow and complete beats fast and fragile; your first five clients are your reputation.

## Intermediate Version
The sequence runs from templates: every step has its document, the gate checklist is a ship-blocker, and steps 2–4 take half the hours they used to. You can run two engagements in parallel because the system, not memory, tracks where each one stands. Client-owned accounts, credentials in a password manager with per-client vaults — always.

## Advanced Version
Delivery team with defined roles (builder, reviewer, client lead), the playbook as onboarding curriculum, QA review before anything ships, capacity planning against the sales pipeline, and delivery margin per engagement reported monthly. You review the numbers and the hard problems; the system delivers the work.

## Revenue Connection
Fulfillment quality sets three numbers that dominate long-run revenue: retainer conversion (target 60%+), referral rate, and rework cost. A mediocre seller with excellent delivery builds a compounding client base; the reverse builds a treadmill with a burn-out date.

## Human-Agent Management Connection
Steps 5, 9, 10, and 13 are the human-agent layer made operational: future-state design applies the [[human-agent-operating-model|operating model]], gates get built and staffed ([[quality-control-and-risk-gates|Quality Control & Risk Gates]]), staff get trained into their [[agent-manager-job-design|new roles]], and the optimization cycle runs the [[progressive-operating-thesis|improvement loop]]. Skipping them delivers automation; including them delivers a redesigned operation — the difference between a project and a client for life.

## Risks / Failure Modes
- **Baselines skipped at step 6** — no before/after, no case study, no proof. Non-negotiable.
- **Silent scope absorption** — margins die in undocumented "small favors." Written change requests always.
- **Launch-and-leave** — steps 12–14 skipped under pressure of the next sale; the compounding assets (retainer, case study, referral) all live in those steps.
- **Hero delivery** — improvised, undocumented work that only you can maintain caps the firm at your calendar. See the full catalog in [[risks-and-failure-modes|Risks & Failure Modes]].

## Related Pages
- [[smb-ai-audit-method|SMB AI Audit Method]] — steps 1–5 in full
- [[consulting-methodology|Consulting Methodology]] — the engagement mechanics (contracting, discovery, feedback, implementation) underneath every step of this sequence
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]] — step 9's architecture
- [[human-role-redesign|Human Role Redesign]] — steps 5 and 10's people work
- [[retainer-model|Retainer Model]] — step 14's destination
- [[tool-stack|Tool Stack]] — the standard build environment
- [[05-BUSINESS/03-Case Studies/CASE_STUDY_TEMPLATE|Case Study Template]] — harvesting proof at handoff
