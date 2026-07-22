---
tags:
  - strategy
  - human-agent
  - delivery
stage: phase-3
timeline: reference
---

# Agent Manager Job Design

> The five roles of the new job layer — what each one does daily, the skills it needs, how it protects quality and grows capacity, and how to sell the design to clients.

## Purpose
Specify the jobs created when AI takes over first-pass production — the concrete role designs you hand to clients (and eventually staff in your own firm), so "humans move up" is a set of job descriptions instead of a slogan.

## Key Idea
AI integration doesn't remove the need for people; it changes what the people are *for*. Five roles cover the new layer. In a 10-person SMB these are hats worn part-time by existing staff (a person might wear three); in a 100-person company they become titles. Either way, **a system with no named humans in these roles is a system that will decay** — which is why role design ships with every build.

## The Five Roles

### 1. AI Workflow Operator
- **Purpose:** run the daily AI-assisted workflows and keep the work flowing.
- **Responsibilities:** work the review queues, approve/correct AI outputs, handle the day's exceptions, confirm the morning's automations ran.
- **Skills:** the underlying business process cold; judgment about "normal vs. weird"; basic comfort with the tools' review interfaces.
- **Example daily tasks:** clear the quote-approval queue by 10am; resolve 3 flagged invoice mismatches; re-run a failed sync after fixing the source record.
- **Protects quality by:** being the human gate on category-3 work ([[human-agent-operating-model|operating model]]) — nothing customer-facing ships unreviewed.
- **Increases capacity by:** one operator supervising the throughput that previously took 3–4 producers.
- **How to sell it:** "Your admin stops typing quotes and starts approving them — same person, 4× the volume, fewer errors."

### 2. Agent Manager
- **Purpose:** own a *group* of AI workflows as systems — performance, exceptions, and improvement.
- **Responsibilities:** monitor workflow metrics (throughput, error rate, exception rate), triage what operators escalate, update prompts/rules/SOPs when patterns of error appear, decide what escalates to the engineer (you).
- **Skills:** systems thinking; pattern recognition across errors; enough prompt/rule literacy to make safe changes; knowing what *not* to touch.
- **Example daily tasks:** review yesterday's exception log; adjust the lead-classification rule that's been mis-tagging commercial jobs; write up a recurring failure for the monthly retainer call.
- **Protects quality by:** catching drift early — the role that notices "the AI has been slightly wrong about X all week" before the owner does.
- **Increases capacity by:** making workflows improve continuously instead of degrading; each rule fix permanently reduces exception volume.
- **How to sell it:** "Someone on your team owns the system's performance the way a foreman owns a crew — and we train them."

### 3. Knowledge-Base Maintainer
- **Purpose:** keep the company's documented knowledge — SOPs, policies, templates, pricing rules, client preferences — current, because every AI output is only as good as this layer.
- **Responsibilities:** update documents when the business changes; retire stale content; capture new exceptions into SOPs; own the "single source of truth."
- **Skills:** writing clearly; organization; the institutional memory (this role is where the veteran admin's knowledge becomes an asset — see [[human-role-redesign|Human Role Redesign]]).
- **Example daily tasks:** update the pricing SOP after the vendor cost change; add the new service area to the intake rules; archive the outdated warranty policy the assistant keeps citing.
- **Protects quality by:** preventing the most common assistant failure — confidently serving outdated policy ([[internal-ai-assistants-pathway|Internal Assistants]]).
- **Increases capacity by:** making knowledge reusable — new hires onboard from the knowledge base instead of shadowing someone for six months.
- **How to sell it:** "Right now your operation lives in Sharon's head. This role gets it into a system — and makes Sharon more valuable, not less."

### 4. AI Quality Auditor
- **Purpose:** independent sampling and verification — trust, but verify, on a schedule.
- **Responsibilities:** sample AI outputs weekly (including ones that passed review), track error rates over time, verify customer-facing materials, test edge cases after any prompt/model change, maintain the risk log.
- **Skills:** skepticism; attention to detail; basic metrics literacy; independence from the operator role (never audit your own queue).
- **Example daily tasks:** pull 10 random sent quotes and check math and terms; re-run last month's acceptance tests after the model update; log the two near-misses into the risk register.
- **Protects quality by:** catching what review gates miss — calibration drift, rubber-stamping, silent failure classes. See [[quality-control-and-risk-gates|Quality Control & Risk Gates]].
- **Increases capacity by:** earning gate relaxation — documented accuracy history is what justifies moving work from human-review toward straight-through processing.
- **How to sell it:** "A few hours a week of sampling is the insurance policy that lets the automation run at full speed the rest of the time."

### 5. Process Designer
- **Purpose:** the improvement engine — map workflows, find bottlenecks, spec the next automation.
- **Responsibilities:** maintain current-state process maps; identify the next constraint after each fix; write automation specs; measure before/after on every change.
- **Skills:** process mapping; waste analysis; the [[smb-ai-audit-method|audit method]] applied internally; enough technical literacy to write a buildable spec.
- **Example daily tasks:** map why closeout packets still take 3 days; spec the change-order workflow for next quarter's build; report the month's throughput deltas.
- **Protects quality by:** ensuring changes are designed, not improvised — every workflow change gets a spec, a gate design, and a metric.
- **Increases capacity by:** compounding — this role turns the operating loop into a flywheel where every quarter's system is measurably better.
- **How to sell it:** at SMB scale, this role is usually *you on retainer* — which is precisely the pitch: "you don't need to hire a process engineer; you need one embedded a few hours a month." ([[retainer-model|Retainer Model]], Partner tier.)

## Why It Matters
- **The market is independently converging on these exact roles.** Deloitte's State of AI in the Enterprise (Jan 2026, n=3,235 — intake July 2026, `raw/`) reports leading organizations creating "AI operations managers, human-AI interaction specialists, quality stewards" — the enterprise names for roles 1, 2, and 4 on this page — while **84% of companies have not redesigned jobs around AI at all** and only 21% have mature governance for autonomous agents. A telecom AI executive in the same report: *"You're going to give existing workers force multipliers… they're going to be watching these agents, making sure the metrics are right, and being there when they hit a human-in-the-loop gate."* This page is that job layer, specified for SMBs — designed before the market has a standard playbook for it.
- **The WEF's own task-shift data says the same thing a different way** (Future of Jobs Report 2025, intake 2026-07-12, `raw/`): the global work split is shifting from 47% human / 22% tech / 30% combined today toward a near-even ~33/33/34 split by 2030 — but **82% of that shift is pure automation, only 19% is human-machine collaboration**. Read correctly, that's not "AI takes the human share" — it's that most of what's automating was already low-judgment production work; the collaboration slice (this page's five roles) is the smaller but *durable* layer that doesn't automate away next. Industry variance matters for pitching: Insurance and Telecom show >95% automation-driven shift (production-heavy, few of these roles needed), while Healthcare and Government run ~50% augmentation-driven (judgment-heavy, this page's roles are central) — calibrate which of the five roles to emphasize by how automation-vs-augmentation-heavy the client's industry runs.
- **It converts the scariest objection into the strongest selling point** — the answer to "what about my people?" is five better job descriptions.
- **It makes systems durable.** Every named role is a failure mode prevented: no operator → queues rot; no manager → drift; no maintainer → stale knowledge; no auditor → silent failure; no designer → stagnation.
- **It's your own org chart too.** Your firm's hires ([[three-year-plan|Three-Year Plan]]) grow into these same roles internally — delivery engineers are operators/managers of your build agents; your playbooks are the knowledge base.

## Practical Actions
- Turn each role above into a one-page role card template (purpose / daily tasks / escalation rules / time budget) — deliverables for implementation handoffs.
- In audits, note which existing employee is the natural fit for each hat; owners love hearing their people named into the future state.
- Price role training explicitly: a "staff enablement" line in every implementation over ~$10K.

## Beginner Version
You wear all five hats for your own business and for early client systems (that's what the first [[retainer-model|retainer tier]] really is). Learn what each role's work actually feels like — that experience is what makes the role cards credible later.

## Intermediate Version
Client staff take the Operator and Knowledge-Maintainer hats with your training; you keep Agent Manager, Auditor, and Designer inside the retainer. The retainer's monthly report explicitly shows each role's outputs (exceptions handled, rules updated, samples audited, improvements shipped).

## Advanced Version
Full role transfer as clients mature: their team runs Operator through Auditor with your quarterly oversight, and you keep Process Designer at the Partner tier. Internally, your own firm staffs these roles across the client portfolio — one agent manager covering 10 clients' workflows is the unit of scale in the [[three-year-plan|Three-Year Plan]].

## Revenue Connection
Role design creates three revenue lines that pure automation can't: **training** (per-implementation), **staffed roles inside retainers** (you *are* the agent manager/auditor for most SMBs — recurring, high margin), and **role-transfer consulting** for larger clients. It also hardens all other revenue: systems with named humans in these roles don't churn.

## Human-Agent Management Connection
This page defines the management layer itself. The [[human-agent-operating-model|operating model]] says which work is supervised; [[human-role-redesign|Human Role Redesign]] moves people into these seats; [[quality-control-and-risk-gates|Quality Control & Risk Gates]] gives the Operator and Auditor their tools.

## Risks / Failure Modes
- **Roles designed but never staffed:** the client nods, assigns nobody, and calls you when it breaks. Prevention: named person per role card before go-live, in the SOW.
- **One person wearing conflicting hats:** operator auditing their own queue defeats the audit. Keep at least those two hats on different heads (or make the auditor *you*).
- **Role inflation at SMB scale:** proposing five job descriptions to a 6-person company reads as consulting theater — present hats, not headcount.

## Related Pages
- [[human-role-redesign|Human Role Redesign]] — the transition into these roles
- [[human-agent-operating-model|Human-Agent Operating Model]] — the work these roles supervise
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]] — the tools of the Operator and Auditor
- [[retainer-model|Retainer Model]] — where you staff these roles for clients
