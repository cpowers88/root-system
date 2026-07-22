---
tags:
  - strategy
  - human-agent
  - risk
  - delivery
stage: phase-3
timeline: reference
---

# Quality Control & Risk Gates

> The engineering discipline that makes AI safe to put in a revenue path: gate patterns, confidence routing, sampling, and escalation — designed into every build, sold as the differentiator.

## Purpose
Specify the standard quality-control architecture for every AI-assisted workflow you ship: which gate types exist, where each belongs, how gates are calibrated over time, and why "our systems have engineered review gates" is a core sales claim rather than overhead.

## Key Idea
AI output is a **component with a known, nonzero failure rate**. Engineering around an unreliable component is a solved discipline — validation, redundancy, monitoring, escalation — and applying it to AI workflows is what separates you from every hobbyist automator. The gate is not friction; the gate is the product. A client isn't buying "AI does your quotes"; they're buying "quotes go out 10× faster *and nothing wrong ever reaches a customer*."

**Shadow AI is already inside most prospects before you arrive (added 2026-07-12, CES-WP-26-25 pp.19-21):** Census microdata on 117,000 firms found **36% of firms where employees use AI show no formal firm-level adoption policy at all** — bottom-up, ungoverned AI use invisible to ownership (vs. 19% with formal adoption but no actual worker use — the opposite failure, adopted-on-paper-only). Practical implication for Step 1–2 of the [[smb-ai-audit-method|audit]]: don't ask "do you use AI" and take a "no" at face value — ask what individual employees already do with ChatGPT/Copilot/etc. on their own, because in over a third of shops the honest owner answer and the actual-use answer are two different things. That gap is itself a risk-gate finding: **ungoverned employee AI use with no validation, logging, or escalation path is the single most common quality-control failure mode you'll find on day one**, not a hypothetical to design against.

## The Standard Gate Types

### 1. Validation gates (deterministic, automatic)
Hard checks that don't need judgment: totals reconcile, dates parse, required fields present, vendor exists in the master list, values within plausible ranges. **Every AI output passes deterministic validation before any human sees it** — humans are too expensive for checking arithmetic.

### 2. Confidence routing
High-confidence outputs flow through; low-confidence route to a review queue. Confidence comes from the model where usable, plus your own proxies (document quality, field completeness, agreement between two extraction passes). Sell it honestly: "95% straight-through, 5% to your team's queue" ([[document-automation-pathway|Document Automation]]).

### 3. Human approval gates
Category-3 work ([[human-agent-operating-model|Human-Agent Operating Model]]): a named human approves before anything customer-facing, financial, or irreversible executes. The design bar: **approval takes seconds, correction is easy, and volume is low enough to stay real** — an overloaded approval queue becomes a rubber stamp within a month.

### 4. Exception & escalation paths
Every workflow defines: what counts as an exception, where it queues, who handles it ([[agent-manager-job-design|Operator → Agent Manager → you]]), and the maximum time it can sit. An exception with no owner is a silent failure with a delay timer.

### 5. Sampling audits
Scheduled random sampling of *passed* outputs by someone who isn't the approver ([[agent-manager-job-design|AI Quality Auditor]]). This is what catches rubber-stamping, calibration drift, and new failure classes after model or prompt changes.

### 6. Logging & traceability
Every AI action logged: input, output, confidence, gate decisions, who approved. Non-negotiable for debugging, for the client's trust, and for the accuracy history that later justifies relaxing gates.

### 7. Acceptance tests & change control
A test set (15–25 real cases with known-correct answers) per workflow, run before go-live and **after every prompt, rule, or model change**. Prompt changes are deployments; treat them with deployment discipline.

## Checklist Design Discipline (Gawande, *The Checklist Manifesto*)
Every gate above is, mechanically, a checklist — and most fail the same way generic checklists fail: too long, untested, or built on paper instead of with the people who'll run it. Four rules, borrowed from aviation/surgical checklist design and validated at scale by the WHO Safe Surgery Checklist trial (36% fewer major complications, 47% fewer deaths, across eight hospitals):
- **Define the pause point precisely.** Not "review before sending" — the exact moment: before the invoice posts, before the email sends, before the record locks.
- **Choose DO-CONFIRM or READ-DO.** Most gates here are DO-CONFIRM — the AI does the work, a human pauses and confirms it's right — because it preserves the model's flexibility while still catching gaps. Use READ-DO only where step *order* itself is the risk (a multi-stage approval sequence).
- **Keep it to killer items — 5 to 9 checks, cut ruthlessly.** A gate checklist that takes a reviewer more than 60–90 seconds gets rubber-stamped, which is the exact rubber-stamping failure mode this page already warns about above. Include only checks that are both genuinely dangerous to skip and actually liable to be skipped — not a comprehensive re-verification of everything the AI did.
- **Test it with the actual people who'll use it before trusting it.** A gate checklist designed on paper and never dry-run with the real approver fails the same way Gawande's own first surgical checklist did: ambiguous wording, wrong timing, an annoyed team. Revise after a real trial run, not before.

This also gives a diagnostic for *why* a gate is failing: is the reviewer missing knowledge (**ignorance** — needs training), or do they know what to check and skip it anyway under time pressure or excitement about closing the queue (**ineptitude** — needs a shorter, better-designed checklist, not more training)? Most gate failures in a mature system are ineptitude, not ignorance — throwing more training at a rubber-stamping problem doesn't fix it.

## Diagnosing a Failed Engagement: The Gap Model (added 2026-07-12, *Principles of Marketing* Ch.12, pp.514-517)
When a client relationship sours — not a single AI output failure but the whole engagement feeling wrong — this five-gap model names *where* the breakdown actually happened, which fix applies:
1. **Discovery gap:** what the client actually needs vs. what Chris understood during the audit. Fix: better discovery questioning (the [[negotiation-toolkit|Negotiation Toolkit]]'s Calibrated Questions), not more engineering.
2. **Scoping gap:** the correct understanding vs. what actually got written into the SOW. Fix: [[fulfillment-system|scoping discipline]], not blame on either side.
3. **Delivery gap:** the written spec vs. what was actually built. This is the one the gate architecture above targets directly.
4. **Promise gap:** what was delivered vs. what sales promised during the close. Fix: the "never oversell" discipline in [[sales-system|Sales System]] — this gap is a sales-conversation failure, not a delivery failure, even though it surfaces as client anger at delivery.
5. **Perception gap:** what was actually delivered vs. what the client *perceives* they got — sometimes the work is right and the client experience of it (communication cadence, how results were framed) is what's actually broken.
Practical use: in a post-mortem or a cooling client relationship, name which gap it is before reaching for a fix — engineering a better gate (#3) does nothing for a #1 or #4 failure, and misdiagnosing which gap failed is itself a common way remediation attempts fail twice.

## Gate Placement by Risk
Calibrate gates to blast radius, not to anxiety:

| Blast radius | Examples | Gate level |
|---|---|---|
| Irreversible / external / financial | payments, contracts, filings, customer commitments | Human approval always + validation + logging |
| External but correctable | emails, quotes, follow-ups | Approval early → confidence routing as accuracy proves out |
| Internal, visible | CRM updates, reports, summaries | Validation + sampling; approval only for anomalies |
| Internal, low-stakes | drafts, search, classifications feeding a human anyway | Validation + logging only |

Over-gating low-stakes work destroys the ROI and trains staff to ignore queues; under-gating high-stakes work destroys the client. Both are calibration failures.

## The Calibration Loop
Gates are not set-and-forget — relaxing them safely *is* the ongoing engineering:
1. Launch with deliberately heavy review.
2. Accumulate accuracy data (logging + sampling).
3. Where the data supports it, move work down a gate level; document the decision.
4. After any model/prompt/process change, re-run acceptance tests and temporarily re-tighten.

This loop is a standing [[retainer-model|retainer deliverable]]: measurable, reportable ("straight-through rate rose from 71% to 93% this quarter"), and impossible for the client to do without you.

## Why It Matters
- **Human validation is a measured top differentiator, not a preference.** McKinsey's Nov 2025 Global Survey on AI (n=1,993 — intake July 2026, `raw/`) found that having **defined processes for when model outputs need human validation** is among the practices that most distinguish AI high performers from everyone else — and that inaccuracy is the #1 AI risk organizations both experience consequences from (~one-third of respondents) and work to mitigate. Deloitte (Jan 2026) adds the gap this page fills: 74% of companies plan agentic AI within two years, but only 21% have mature governance for autonomous agents — "AI agents are scaling faster than the guardrails," and "governance is the difference between scaling successfully and stalling out." Cite both in proposals: the gate architecture is what the winners measurably do.
- **Silent failure is the worst event in this business** ([[risks-and-failure-modes|Risks & Failure Modes]] #4); gates plus monitoring are its structural prevention.
- **It's the defensible skill.** Anyone can call an API. Designing the validation, routing, and audit architecture around it is engineering — the part that survives tool commoditization ([[north-star-alignment|North Star]]).
- **It closes deals with the cautious buyer.** The owner who's heard AI horror stories is your best prospect once you show the gate architecture — you're the vendor who takes their risk seriously.

## Practical Actions
- Write your standard gate checklist (the 7 types above) into the build phase of the [[fulfillment-system|Fulfillment System]]; no workflow ships without a completed gate design.
- Add a one-page "how we protect you" gate diagram to your proposal template — it visibly differentiates against cheap automators.
- Build the acceptance-test habit on your own systems first: test set, run log, change discipline.

## Beginner Version
Minimum viable gates on every early build: deterministic validation, one human approval on anything customer-facing, failure alerts, and a log. That alone puts you ahead of most of the market. Add confidence routing and formal sampling once volumes justify them.

## Intermediate Version
Full seven-type architecture on every engagement, gate designs documented in the SOW, acceptance tests run at go-live, and the calibration loop reported monthly inside retainers. Client staff trained on their queues via [[human-role-redesign|role cards]].

## Advanced Version
A firm-level QC platform: centralized exception dashboards across all clients, standardized accuracy metrics per workflow type, gate-pattern libraries per vertical, and change-control policy enforced by tooling. Your gate architecture becomes documented IP — part of what an acquirer buys ([[ten-year-scale-plan|Ten-Year Scale Plan]]).

## Revenue Connection
Gates raise close rates (they answer the risk objection), justify premium pricing (engineering vs. zaps), create the calibration loop that anchors [[retainer-model|retainer]] value, and prevent the trust-destroying incident that would vaporize a referral-driven pipeline. QC isn't a cost center; it's the moat.

## Human-Agent Management Connection
Gates are where humans and agents physically meet: approval queues and exception paths are the daily workplace of the [[agent-manager-job-design|Operator and Agent Manager]], sampling is the Auditor's tool, and the calibration loop is the improvement work of the [[progressive-operating-thesis|operating loop]].

## Risks / Failure Modes
- **Rubber-stamping:** approval queues too big or too dull get clicked through. Detection: sampling audits; prevention: keep human gates low-volume and consequential.
- **Gate theater:** gates in the diagram but not the build ("we'll add validation later"). Prevention: gate checklist completion is a ship-blocker.
- **Un-versioned prompt changes:** someone tweaks a prompt, accuracy silently shifts. Prevention: change control + acceptance tests, no exceptions.
- **Over-gating:** every task human-reviewed, no ROI, client concludes AI "doesn't work." Prevention: the blast-radius table, applied honestly.

## Related Pages
- [[human-agent-operating-model|Human-Agent Operating Model]] — which work needs which gate
- [[agent-manager-job-design|Agent Manager Job Design]] — who staffs the gates
- [[risks-and-failure-modes|Risks & Failure Modes]] — the failures gates prevent
- [[fulfillment-system|Fulfillment System]] — where gate design lands in delivery
- [[retainer-model|Retainer Model]] — the calibration loop as recurring revenue
- [[smb-ai-audit-method|SMB AI Audit Method]] — the ignorance-vs-ineptitude diagnostic applied to a client's whole process, not just one gate
