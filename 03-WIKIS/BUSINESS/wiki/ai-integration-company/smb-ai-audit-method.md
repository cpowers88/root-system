---
tags:
  - phase-2
  - pathway
  - audit
  - delivery
  - human-agent
---

# SMB AI Audit Method

> The paid diagnostic that opens every client relationship: how to run it, what to deliver, and how it converts into projects. This is the core operating page of the business.

## At a Glance
- **Core claim:** the audit is a paid sales process disguised as consulting (and real consulting disguised as a sales process) — it must produce a real work-redesign diagnosis whether or not a project follows.
- **When to use it:** before and during every client audit engagement — Step 1 scoping through Step 6 delivery.
- **Decision/action it supports:** what to charge, what to interview for, how to classify findings, and how to price the follow-on project.
- **Key risk:** running it free, or running it as a sales pitch instead of real diagnostic work — both kill conversion and credibility (see Risks / Failure Modes).

## Purpose
Document the repeatable method for auditing an SMB's operations — so every audit produces the same quality of diagnosis, the same deliverable, and the same conversion opportunity, regardless of who runs it.

## Key Idea
The audit is a **paid sales process disguised as consulting — and real consulting disguised as a sales process.** The client pays $1,500–$5,000 to have their operations mapped, their waste quantified in dollars, and a prioritized fix-list produced. You get paid to build the exact document that sells the implementation. Both sides win even if no project follows.

The audit's deeper product is a **work redesign**: it doesn't just find automatable tasks, it classifies every piece of work through the [[human-agent-operating-model|Human-Agent Operating Model]] and shows the owner what their business looks like when AI does first-pass production and their people manage the system ([[progressive-operating-thesis|Progressive Operating Thesis]]).

Charging for it is non-negotiable: free audits attract non-buyers, get ignored, and position you as a salesperson instead of an engineer.

### Who You're Actually Auditing (added 2026-07-12, CES-WP-26-25 pp.24-27)
The Census Bureau's latent-class analysis of 117,000 firms (Nov 2025–Jan 2026) sorts AI-using businesses into five archetypes — useful for calibrating expectations before Step 1, since most prospects are NOT the blank slate they think they are:
- **Minimalist Adopters (37% of AI users)** — low-intensity use scattered thinly across functions. The modal prospect.
- **Marketing Specialists (31%)** — AI concentrated in sales/marketing only, everything else untouched.
- **Institutional-Administrative Integrators (15%)** — back-office/admin functions only.
- **Technical Strategists (12%)** — deeper but narrow technical use.
- **Comprehensive Adopters (only 4%)** — genuinely broad, cross-functional use.

**57% of all AI-using firms use it in 3 or fewer of 15 business functions.** The practical read: almost every prospect has already dabbled somewhere (usually marketing or admin) and calls themselves "not an AI user" — the audit's job in Step 1–2 isn't discovering whether they use AI, it's discovering *which thin slice* they're already in and mapping the other 12+ functions that are still fully manual. Set the framing early: "you're not starting from zero, you're a Minimalist/Marketing-Specialist adopter — we're mapping where the other 80% of the business still is."

## The Method (6 Steps, 1–2 Weeks)

### Step 1 — Intake & Scoping (Day 1)
Pre-audit questionnaire: org chart, software list, top 3 frustrations, rough volumes (leads/month, invoices/month, etc.). Sign scope: which departments/processes are in-bounds.

### Step 2 — Business Flow Map (Days 2–4)
Map how work enters, moves through, and exits the business. Interview the owner plus 2–4 frontline staff (30–45 min each); watch at least one process performed live — what people *say* they do and what they *do* always differ. Use the [[negotiation-toolkit|Negotiation Toolkit]]'s Mirroring and Calibrated Questions throughout these interviews — they're built for exactly this: keeping a source talking and surfacing what they'd otherwise leave out. The questions that expose the map:
- Where do leads come from, and who touches one first?
- Where is information stored — and where is it re-typed?
- What happens after the customer says yes?
- Where do jobs stall, and who notices?
- What gets copied between systems?
- What does the owner manually check every day?

For each core process capture: trigger → steps → tools → handoffs → time per instance → volume → failure points.

Whenever possible, run this as a group conversation — owner, office staff, and field crew together, not sequential one-on-ones — and let them compare notes on the same process in the same room. No single role in an SMB has full visibility into how work actually flows; contradictions between what the owner thinks happens and what a frontline employee actually does are themselves findings, and they surface fastest when the team hears each other's answers, not just yours.

**Walk it twice, on paper.** This is [[lean-methodology|Value Stream Mapping]]'s field method: walk the physical flow once with no data collection — just observe how work and information actually move, where things pile up. Walk it a second time collecting real numbers by hand (time per step, batch size, how often work sits waiting) — never from a printout or a system report. Map it with pencil and paper, in the work area itself, not from a desk.

**Construction-specific: check the Procore (or equivalent) instance before the interviews.** Procore is the dominant construction-management platform, and a contractor's instance is a pre-built data source for this whole step: RFIs, submittals, change orders, daily logs (labor hours, weather, equipment, deliveries), budgets and commitments, timecards, inspections, punch lists, photos, and correspondence — with 90+ API endpoints and a reporting/analytics layer on top. Three audit uses: (1) **real volumes and timestamps** for the Step 4 waste math (how long RFIs actually sit, change-order turnaround, log completion rates) instead of interview estimates; (2) **the double-entry finding** — the classic construction waste pattern is data typed into Procore *and* QuickBooks *and* a spreadsheet, and the instance proves it; (3) **the unused-data finding** — most contractors capture far more in daily logs and financials than anyone ever reports on, which is a ready-made [[data-and-dashboard-pathway|dashboard]] recommendation. Per the BTOS numbers in [[market-map|Market Map]], even AI-adopting contractors have near-zero AI in quality management and supply chain — the functions this data already covers. Free platform training: learn.procore.com (see [[skill-roadmap|Skill Roadmap]], Layer 1). A fourth audit use: the **App Marketplace integration check** — Procore's partner marketplace spans accounting/ERP sync, embedded Power BI, document migration, takeoff/estimating, SMS field-data bots, 3D site capture, time & attendance, tool tracking, jobsite cameras, and iPaaS connectors (Boomi). Asking "which of these does your stack already integrate, and which gaps are you re-typing across by hand?" turns the marketplace category list into a ready-made double-entry checklist (source: Procore integration roundup clipping, `raw\`, intake July 2026).

**Construction-specific: the bid-closing interview (added 2026-07-12, residential estimating textbook, `raw/`).** For a GC or custom builder, the highest-waste moment is often bid closing, not day-to-day operations — worth its own line of questioning: in the final hours before a bid deadline, subtrade prices traditionally arrive by phone/fax/email under time pressure; larger bids need several people just to answer phones and log incoming numbers; each phone-in price gets hand-transcribed onto a paper "bid form" (trade, bidder, price, tax treatment, conditions, time received) before being rolled into the summary bid. NAHB has named "inaccurate/inefficient estimating procedure" as home-building's #1 financial-control problem. Ask directly: *"Walk me through your last bid closing — how many subtrade prices came in by phone or text in the final two hours, and who transcribes those by hand onto the summary?"* Sanity-check the specific channel (phone/fax/text/email) with the client since this varies by shop in 2026, but the underlying pattern — time-pressured manual transcription feeding a bid summary — is the automation target regardless of medium.

### Step 3 — Task Inventory (Days 4–6)
Classify every recurring task from the flow map into six buckets — this classification *is* the future-state design:
- **Human-only** — judgment, relationships, accountability ([[human-agent-operating-model|operating model]] category 1)
- **AI-first** — repeatable cognitive production: drafting, extracting, classifying, summarizing
- **Human-review** — AI produces, a named human validates via a [[quality-control-and-risk-gates|gate]]
- **Automatable** — deterministic, no AI needed (integrations, syncs, notifications)
- **Delegatable** — belongs with cheaper labor or a vendor, not software
- **Eliminate entirely** — work nobody would miss (the most satisfying finding in any audit)

### Step 4 — Waste Diagnosis & Revenue Leakage (Days 6–8)
Two lenses on the same inventory. **Cost waste:** waiting, rework, manual copy/paste, duplicate entry, missing information, unclear ownership, forgotten tasks, unused data, poor visibility. Use the lean [[lean-methodology|seven wastes]] taxonomy (overproduction, waiting, transportation, unnecessary processing, inventory, unnecessary motion, correction — translated to office/field terms) as the naming checklist so findings read as specific, nameable categories rather than a vague impression. Watch specifically for a **"monument"** — any tool, system, or piece of equipment too large or rigid to adapt, forcing batch-style work: a client who over-invested in software or hardware that doesn't match their actual job flow is a common, easy-to-miss finding, and recommending more automation on top of a monument makes the waste worse, not better. For each: annual cost = `(minutes per instance × instances per year × loaded hourly rate) + error/rework cost`. Example: manual quote assembly at 40 min × 600 quotes/yr × $45/hr ≈ **$18,000/yr**, before counting quotes lost to slow turnaround.

**Revenue leakage:** slow lead response, poor follow-up, bad estimates, missed change orders, unbilled work, incomplete documentation, underused CRM, owner bottlenecks. These usually dwarf the cost waste and they're what moves owners — "you're losing ~$80K/yr in leads nobody calls back" outsells "save $15K in admin time" every time ([[crm-and-sales-ops-pathway|CRM & Sales Ops]]).

Conservative numbers only — credibility is the product.

**Diagnose ignorance vs. ineptitude before recommending a fix.** Two different failure modes produce the same symptom (a process that isn't working), and they call for opposite fixes. **Ignorance**: the client genuinely doesn't know a better way exists — the fix is training or a new tool. **Ineptitude**: the client knows the better way and doesn't do it consistently — the fix is a checklist or process discipline, not more training (throwing training at an ineptitude problem doesn't fix it; it's the mistake medicine made for decades). Misdiagnosing which one you're looking at wastes the client's money and your credibility — always ask "does this team know a better way, or do they know it and skip it under pressure?" before writing the recommendation.

**Find the constraint before diagnosing waste everywhere.** Goldratt's Theory of Constraints (*The Goal*) is the discipline underneath this whole step: a business is a chain of dependent processes, and at any moment its total output is capped by exactly one constraint — a resource, policy, or market condition whose capacity is at or below the demand on it. Improving anything else first is wasted motion ("an hour saved at a non-bottleneck is a mirage"). Practically, this means Step 4 isn't "list every inefficiency" — it's "find the one process stage where work actually piles up or stalls, and start there." In the flow map, that's the stage where jobs sit longest, where the owner personally intervenes most often, or where the queue is visibly longest. Everything else is secondary until that stage is fixed.

## Applying the Five Focusing Steps to a Client Engagement

TOC's Five Focusing Steps are a reusable prioritization sequence for both diagnosing (Step 4) and sequencing the roadmap (Step 6):

1. **Identify the constraint** — find the one stage in the flow map with capacity at or below the demand on it (the worst bottleneck), not a list of everywhere efficiency could be marginally better. Use the client's own data (CRM exports, timestamps, volumes) to point at it, not a guess.
2. **Exploit it** — before recommending any paid build, check whether the constrained stage is wasting its own capacity on things a free policy fix would solve: idle time waiting on upstream input, low-value work that could be reassigned, rework caused by upstream defects. Cheap fixes here should ship before anything gets scoped as a paid project.
3. **Subordinate everything else to it** — the rest of the roadmap should be sequenced around what the bottleneck stage can actually absorb, not around what's easiest to build. A slick automation upstream of the real constraint doesn't move total throughput; it just moves the pile-up earlier in the process.
4. **Elevate it** — only once Steps 2–3 are exhausted does it make sense to recommend real investment (a new tool, added headcount, a build) at the constrained stage specifically.
5. **Repeat — and watch for inertia** — once the constraint moves (it always does), the old fix becomes dead weight if left in place. This is the strongest argument for [[retainer-model|retainer]] work over one-and-done projects: an audit finds today's constraint; it doesn't mean the business is "fixed." Quarterly re-audits (see Advanced Version below) exist specifically to re-run Step 1 against a system that has already changed.

### Step 5 — Human-Agent Redesign & Solution Mapping (Days 8–10)
For each priority workflow, design the future state explicitly:
- **What AI does first** (the first-pass production)
- **What the human reviews** and through which [[quality-control-and-risk-gates|gate]]
- **What gets escalated**, to whom, within what time
- **What gets logged** for traceability
- **Which rule/prompt/SOP gets updated** when the AI is wrong — and who owns that update ([[agent-manager-job-design|role design]])
- **What metric proves improvement**
- **Who owns the workflow today and what their role becomes** ([[human-role-redesign|Human Role Redesign]])

Match each design to a delivery pathway: [[workflow-automation-pathway|workflow automation]], [[crm-and-sales-ops-pathway|CRM/sales ops]], [[document-automation-pathway|document automation]], [[data-and-dashboard-pathway|dashboards]], [[internal-ai-assistants-pathway|internal assistants]].

### Step 6 — Priority Scoring, Report & Roadmap (Days 10–14)
Score each opportunity on: revenue impact, time saved, ease of implementation, risk level, data availability, human-review burden, and retainer potential. Rank by payback — but rank the constraint stage's fixes first regardless of score. A high-scoring fix to a non-bottleneck stage is the "mirage" TOC warns about: it looks productive in the report but doesn't move the client's actual total throughput until the real constraint is addressed.

Deliverable (10–20 pages):
1. Executive summary — total quantified annual waste + leakage (the headline number)
2. Business flow map of current state
3. Task inventory with the six-bucket classification
4. Findings table: problem → annual cost → recommended fix → who reviews it → payback
5. Prioritized roadmap: Phase 1 quick wins, Phase 2 core systems, Phase 3 optimization
6. **Phase 1 proposal with price** — the audit's last page is the next sale's first page

Present live, never just email it. Walk the owner from headline waste number to Phase 1 proposal in one meeting.

## Why It Matters
- It solves the cold-start problem: strangers won't buy $20K projects, but they will buy a $2,500 diagnosis of a pain they already feel.
- It kills scope-creep at the source: projects sold from audit findings have defined baselines and agreed priorities.
- It is the most defensible thing you do: anyone can buy automation tools; almost nobody can walk into a business and find the money. See [[north-star-alignment|North Star Alignment]].

## Practical Actions
- Build the three templates once: intake questionnaire, interview guide, report skeleton ([[templates/template-library|templates]] has ready versions). Add the task-inventory classification column and redesign fields to the report skeleton.
- Rehearse the waste-math on your own workflows or a friend's business before the first paid audit.
- Track conversion: audits delivered → Phase 1 projects sold. Target 50–70%. Below 40% means the findings aren't quantified sharply enough or the roadmap isn't prioritized by payback.

## Beginner Version
Price: $1,500–$2,500. Scope: one department (usually sales/admin — fastest wins live there). First one or two audits may be discounted for a case-study agreement — discounted, never free. Expect 20–30 hours each early on; that's tuition. A $500–$1,500 **starter diagnostic** (half-day walkthrough + opportunity list, no full inventory) is a legitimate low-friction entry for the very first clients — see [[pricing-models|Pricing Models]].

## Intermediate Version
Price: $2,500–$5,000 with the full six-step method and human-agent redesign as standard. Delivery time falls to 15–20 hours through templates and reusable process libraries. The task inventory and redesign sections become your signature deliverable — the thing no cheap automator's "free consultation" can imitate.

## Advanced Version
Price: $3,500–$7,500+ with fixed 2-week turnaround. Delivery: 10–15 hours using vertical-specific templates ([[market-map|Market Map]] verticals get pre-built process libraries and classification inventories). Junior consultants run discovery; you review findings and present. Quarterly **re-audits** become a retainer deliverable — see [[retainer-model|Retainer Model]].

## Revenue Connection
Direct: $1.5K–$7.5K per audit at high margin. Indirect (the real value): each audit generates a warm, pre-scoped project pipeline worth 5–20× the audit fee, plus the baseline metrics that later become [[case-study-template|case studies]]. Audit volume is the single best leading indicator of next-quarter revenue.

## Human-Agent Management Connection
The audit is where the [[progressive-operating-thesis|thesis]] first touches a client: Step 3's inventory applies the [[human-agent-operating-model|operating model]], Step 5 designs the gates and the new roles, and the report names which employees become [[agent-manager-job-design|operators, agent managers, and knowledge maintainers]]. Selling the audit is selling the redesign of work.

## Risks / Failure Modes
- **Findings without dollars:** qualitative observations don't convert. Every finding carries an annual cost or it doesn't ship.
- **Roadmap without gates or owners:** recommending automation with no review design or named human owner sets up the implementation to fail — and signals amateurism to sophisticated buyers.
- **Free or underpriced audits:** attract non-buyers and reprice your expertise at zero ([[what-not-to-do|What NOT To Do]]).
- **Scope sprawl:** auditing the whole company at beginner speed burns 60 hours. Hold the signed scope.

## Related Pages
- [[customer-discovery-and-evidence|Customer Discovery and Evidence]] — protects discovery from compliments, hypotheticals, and solution-leading questions
- [[enterprise-ai-opportunity-and-adoption|Enterprise AI Opportunity and Adoption]] — cross-industry opportunity patterns and readiness diagnostic
- [[ai-economics-and-decision-workflows|AI Economics and Decision Workflows]] — decomposes prediction, judgment, action, outcome, and feedback before automation
- [[strategic-diagnosis-and-coherent-action|Strategic Diagnosis and Coherent Action]] — converts the symptom list into a decisive diagnosis and coherent roadmap
- [[theory-of-constraints|Theory of Constraints]] — the full framework (throughput/inventory/operational-expense measurements, cost-world vs. throughput-world, the asymmetry rule) behind the constraint-first diagnosis logic above
- [[owner-dependency-diagnostic|Owner-Dependency Diagnostic]] — the *why is this business stuck* complement: root-cause, growth-stage, and target-state diagnostics to run alongside this method
- [[consulting-methodology|Consulting Methodology]] — the contracting, discovery-interview, and feedback-meeting mechanics behind Steps 1, 2, and 6
- [[creative-problem-solving-and-facilitation-toolkit|Creative Problem Solving and Facilitation Toolkit]] — use only after findings are evidenced, when stakeholders need a structured route from diagnosis to options and a test
- [[negotiation-toolkit|Negotiation Toolkit]] — discovery-interview technique (Step 2) and reading real buy-in in the findings presentation (Step 6)
- [[service-offer-ladder|Service Offer Ladder]] — where the audit sits in the stack
- [[human-agent-operating-model|Human-Agent Operating Model]] — the classification engine of Step 3
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]] — the gate designs of Step 5
- [[sales-system|Sales System]] — booking audit engagements
- [[pricing-models|Pricing Models]] — audit pricing logic
- [[fulfillment-system|Fulfillment System]] — delivering what the audit sells
