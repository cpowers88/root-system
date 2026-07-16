---
tags:
  - phase-all
  - risk
---

# Risks & Failure Modes

> What actually kills this business at each stage, the early warning signs, and the standing countermeasures.

## Purpose
Catalog the realistic ways this business fails — commercial, delivery, technical, and personal — with detection signals and countermeasures, so problems get caught as metrics instead of as crises.

## Key Idea
This business rarely dies from competition or technology; it dies from **self-inflicted operating failures**: inconsistent selling, underpricing, unreliable delivery, founder bottlenecking, and drift away from the [[north-star-alignment|North Star]]. Every failure mode below has a leading indicator. The countermeasure system is simple: put the indicators in the weekly/monthly review and act on the *first* miss, not the third.

## Tier 1 — The Killers (Most Businesses Die Here)

### 1. The feast/famine pipeline
**Pattern:** sell → get busy delivering → stop selling → finish → empty pipeline → panic-discounting.
**Signal:** any week with zero outreach touches; pipeline coverage < 2× next-quarter target.
**Countermeasure:** the non-negotiable weekly sales minimums in the [[sales-system|Sales System]], enforced hardest when busiest.

### 2. Chronic underpricing
**Pattern:** nervous quotes → bad-fit clients → no margin for improvement → resentment and burnout.
**Signal:** close rate >80% on proposals; effective hourly on projects below your floor; dread when the client emails.
**Countermeasure:** the rate card and rules in [[pricing-models|Pricing Models]]; log actual hours vs. price on every engagement.

### 3. Delivery without proof or retainers
**Pattern:** projects delivered, everyone happy, nothing captured — no baseline, no case study, no retainer offer. The business stays a treadmill.
**Signal:** projects "closed" with no before/after numbers; retainer conversion <40%.
**Countermeasure:** baselines at kickoff and the handoff checklist in the [[fulfillment-system|Fulfillment System]] — case study and retainer conversation are mandatory line items.

### 4. Silent automation failure
**Pattern:** a client automation breaks quietly; leads or invoices vanish for days; trust is destroyed retroactively — worst single event in this business.
**Signal:** any client system without failure alerts; you learning about breakage *from the client*.
**Countermeasure:** error handling and monitoring as first-class build requirements ([[workflow-automation-pathway|Workflow Automation]]); centralized alerting ([[tool-stack|Tool Stack]]); parallel runs before cutover.

## Tier 2 — The Cripplers (Survivable, Expensive)

### 5. Scope creep and unscoped projects
**Signal:** projects sold without an audit; "while you're in there" work absorbed silently; delivery hours >150% of estimate.
**Countermeasure:** sell projects from audit findings ([[service-offer-ladder|Service Offer Ladder]]); written change requests, always priced ([[fulfillment-system|Fulfillment System]]).

### 6. Bad-fit clients
**Pattern:** the price-shopper, the chaos business with no documented process, the "make us an AI strategy" client, the one who won't give access or decisions.
**Why it happens:** an exciting-looking opportunity (a big logo, a big check) triggers the same motivated-reasoning failure Gawande documents in professional investors — Pabrai calls it "going into greed mode": you skip due diligence you'd normally run, not because you don't know better, but because the deal feels too good to slow down for.
**Signal:** client fails the [[north-star-alignment|alignment filter]] or the [[market-map|Market Map]] profile; slow payment on the audit (predicts everything after); you notice yourself excited enough to skip a step you'd normally insist on.
**Countermeasure:** the audit is the filter — behavior during a $2,500 engagement predicts behavior during a $25K one. Decline the project when the audit reveals a bad client, not just a bad process. Keep a short, written pre-engagement checklist (5–9 items, tied to specific past misjudgments — Pabrai-style) and run it explicitly on every prospect that feels exciting, precisely because that's the state most likely to make you skip it.

### 7. Client concentration
**Signal:** any client >25% of revenue (early) or >10% (scaled).
**Countermeasure:** track it; keep selling even when one client could fill your calendar; price big-client work to fund diversification.

### 8. Automating a broken process
**Pattern:** the client's workflow is chaos, and automating it just produces faster, more confident chaos — with your name on it.
**Why it happens:** build pressure ("just automate what we do") beats diagnosis; redesign feels like scope.
**Signal:** no documented current state; staff describe three different versions of the same process; exceptions outnumber the happy path.
**Countermeasure:** process redesign and SOP buildout precede automation ([[service-offer-ladder|Service Offer Ladder]] Rung 2); the [[smb-ai-audit-method|audit's flow map]] is the prerequisite, not a formality.
**Recovery:** stop the build, sell the redesign phase honestly, resume on a documented process.

### 9. Replacing workers without preserving knowledge
**Pattern:** client cuts staff the moment automation lands; the veteran's undocumented exception-handling walks out the door; the system fails on every case she used to catch invisibly.
**Why it happens:** owners see headcount as the ROI; nobody prices the tribal knowledge.
**Signal:** owner talks about "who we can let go" before go-live; no knowledge-capture step in the plan.
**Countermeasure:** [[human-role-redesign|role redesign]] and knowledge-capture interviews before any staffing change; sell capacity, not cuts.
**Recovery:** emergency knowledge-capture with remaining staff; rebuild the exception rules from the failure log; reset owner expectations in writing.

### 10. Adoption failure
**Pattern:** the system works; the staff don't use it; renewal dies quietly.
**Signal:** usage/adoption metrics falling after handoff; no named internal owner on the client side.
**Countermeasure:** owner mandate secured pre-project ([[crm-and-sales-ops-pathway|CRM pathway]] delivery notes); training and 30-day check-in built into every handoff; adoption reported to the owner.
**Third-party corroboration (added 2026-07-12):** WEF's Future of Jobs Report 2025 names organizational resistance to change as employers' #2-cited transformation barrier (46%) globally, second only to skills gaps and ahead of regulatory concerns (39%) — this isn't a Chris-specific risk, it's the documented #2 reason AI initiatives fail industry-wide.

## Tier 3 — Technical & External Risks

### 11. AI output failure in production
**Pattern:** extraction/classification/drafting errors reach a client's customer or books.
**Countermeasure:** human-in-the-loop by design, confidence thresholds, validation layers, and never promising 100% ([[document-automation-pathway|Document Automation]]); acceptance-test suites for assistants ([[internal-ai-assistants-pathway|Internal Assistants]]).

### 12. Data and security incidents
**Pattern:** client credentials or sensitive data mishandled — potentially fatal to reputation in a referral-driven business.
**Countermeasure:** password manager with per-client vaults from day one, client-owned accounts, minimal data retention, a written data-handling answer before clients ask ([[tool-stack|Tool Stack]]); liability terms in the MSA and appropriate insurance early.

### 13. Platform/API churn
**Pattern:** a tool you depend on changes pricing, API, or dies.
**Countermeasure:** this is retainer *content*, not an existential threat — if it's monitored and you fix it fast, churn events strengthen the relationship. Abstract LLM providers; avoid single-vendor lock-in on anything critical.

### 14. Commoditization of basic automation
**Pattern:** simple zap-building goes to $0 as tools get easier and AI builds automations itself.
**Countermeasure:** the moat was never the build — it's diagnosis, integration judgment, reliability engineering, and accountability ([[north-star-alignment|North Star]]). Keep climbing the [[service-offer-ladder|offer ladder]]; cheaper tools mean *your* delivery cost falls too.

## Tier 4 — Founder Risks

### 15. Builder's procrastination
**Pattern:** perfecting internal tools and learning new tech as a socially acceptable way to avoid selling.
**Signal:** week with more tooling hours than client/pipeline hours (early stage).
**Countermeasure:** the [[first-30-days|First 30 Days]] outreach deadlines; sales minimums as the first metric reviewed.

### 16. Founder bottleneck & burnout
**Pattern:** everything routes through you; quality holds but nothing scales; then quality breaks too.
**Signal:** founder delivery hours not falling quarter-over-quarter after year 1; vacation impossible.
**Countermeasure:** the documented → delegated discipline of the [[three-year-plan|Three-Year Plan]]; playbook hours scheduled weekly from month 1.

### 17. Shiny-object drift
**Pattern:** new offer, new market, new tool every quarter; nothing compounds.
**Countermeasure:** one new offer per quarter maximum ([[one-year-plan|One-Year Plan]]); the alignment filter; the [[what-not-to-do|What NOT To Do]] list reviewed when tempted.

## Practical Actions
- Build the review cadence now: **weekly** (outreach count, pipeline coverage), **monthly** (margin per engagement, retainer conversion, client concentration, founder delivery hours), **quarterly** (recurring share, NRR, this page re-read).
- Write the MSA with liability limits and data terms before client #3; get professional liability + cyber insurance before the first document-automation or data-heavy client.
- Pre-commit countermeasures in writing — deciding *now* what you'll do when close rates hit 80% beats negotiating with yourself later.

## Beginner Version
Watch four numbers only: weekly outreach touches, proposal close rate, retainer conversion, and "does every client system have failure alerts?" Those four catch failure modes 1–4 — the killers — and the rest can wait.

## Intermediate Version
The weekly/monthly/quarterly review cadence runs on real data, every Tier 1–2 risk has its leading indicator on your own dashboard, the MSA and insurance are in place, and gate coverage ("does every client system have failure alerts and a named reviewer?") is checked at every handoff — the point where risk management stops being a document and becomes operations.

## Advanced Version
The full indicator set lives on the ops dashboard; each Tier 1–2 risk has a named owner; incident post-mortems (delivery misses, security events, churn) feed the playbooks; and an annual pre-mortem ("it's next December and we're down 40% — what happened?") is run with the leadership team.

## Revenue Connection
Risk management here isn't defensive overhead — every countermeasure is a margin or LTV mechanism: pipeline discipline smooths revenue, pricing rules protect margin, monitoring protects retainers, and adoption work protects renewals. The firms that reach the [[ten-year-scale-plan|ten-year outcomes]] aren't the ones that grew fastest; they're the ones that didn't stop.

## Human-Agent Management Connection
Half this catalog is structurally prevented by the human-agent layer: [[quality-control-and-risk-gates|gates]] prevent #4 and #11, [[human-role-redesign|role redesign]] prevents #9 and #10, and the [[agent-manager-job-design|auditor role]] catches drift before it becomes an incident. The thesis isn't just strategy — it's the risk-control architecture.

## Related Pages
- [[company-operating-system-and-founder-judgment|Company Operating System and Founder Judgment]] — decision, resilience, metric, and bias countermeasures as the firm grows
- [[what-not-to-do|What NOT To Do]] — the strategic complement to this operational list
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]] — the engineering countermeasures
- [[sales-system|Sales System]] — countermeasure to the #1 killer
- [[fulfillment-system|Fulfillment System]] — countermeasure to delivery risks
- [[pricing-models|Pricing Models]] — countermeasure to margin risks
