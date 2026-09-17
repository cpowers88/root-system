---
type: model
tags:
  - strategy
  - human-agent
  - delivery
stage: phase-1
timeline: reference
---

# Human-Agent Operating Model

> The four-category work classification used in every audit and every build: human-only, AI-first, human-review, and system-improvement work.

## Purpose
Give the [[progressive-operating-thesis|progressive thesis]] a working tool: a repeatable way to classify any task in any business into one of four categories, so audits produce consistent future-state designs and builds always know where the human sits.

## Key Idea
Every piece of work in an SMB belongs to one of four categories. The audit classifies; the build enforces; the retainer maintains the boundaries as the business and the models change.

### 1. Human-Only Work (AI assists, never owns)
- Customer trust and relationship management
- Final approval of customer-facing work
- Legal, financial, safety, ethical, or employment decisions
- Negotiation and conflict resolution
- Strategic prioritization and field judgment
- Complex exception handling
- Accountability for final outcomes

AI may summarize, draft, or prepare here — it must not decide. Selling this boundary explicitly is what makes owners trust the rest of the design.

### 2. AI-First Work (AI produces, by default)
- Drafting emails and follow-ups
- Summarizing calls, meetings, and documents
- Extracting data from PDFs, forms, emails, and spreadsheets
- Classifying leads, tasks, tickets, and requests
- Creating checklists, reports, and SOP drafts
- Searching company knowledge bases
- Preparing proposal and quote drafts
- Comparing quotes, invoices, or vendor documents
- Identifying missing information
- Producing dashboard summaries

### 3. Human-Review Work (AI produces, human validates)
- Estimates and proposals
- Customer messages
- Intake summaries
- Invoice exceptions
- CRM updates
- Compliance checklists
- Job closeout packets
- Daily management reports
- Escalation queues

The design goal: the human reviews **exceptions and approvals**, not the whole workflow. If staff redo the AI's work manually, the gate is miscalibrated — see [[quality-control-and-risk-gates|Quality Control & Risk Gates]].

### 4. System-Improvement Work (the new job layer)
Agent manager, AI workflow operator, knowledge-base maintainer, AI quality auditor, prompt/process designer, automation maintainer, data-hygiene operator, customer exception handler, internal systems trainer. Full role designs: [[agent-manager-job-design|Agent Manager Job Design]].

## Why It Matters
- **It makes audits decisive.** "Where can we use AI?" is unanswerable; "which category does each task belong to?" is a checklist. The [[smb-ai-audit-method|audit's task inventory]] is this model applied.
- **It scopes builds correctly.** Most blown AI projects put category-1 work into category-2 pipelines (AI deciding things it shouldn't) or category-2 work behind category-3 friction (humans re-checking what needs no checking).
- **It's the staffing answer.** Category 4 is where displaced hours go — the explicit answer to "what happens to my people?" See [[human-role-redesign|Human Role Redesign]].

## Practical Actions
- Turn the four categories into a column in your audit task-inventory spreadsheet; every mapped task gets classified (plus two more buckets: *delegatable* and *eliminate entirely* — some work needs neither humans nor AI).
- For every category-3 workflow you design, define: what AI does first, what the human reviews, what escalates, what gets logged, which rule/prompt/SOP gets updated when it's wrong, and what metric proves improvement.
- Re-classify quarterly on retainer accounts: model improvements move borderline tasks from category 3 toward category 2 — that migration is retainer value delivered.

## Beginner Version
Use the model on your own operation and one practice audit. Expect to over-assign work to "human-only" at first — most operators do. The corrective question: "is this judgment, or is it just familiar?"

## Intermediate Version
The classification is a standard audit deliverable with volumes and costs attached: each category-2/3 task carries hours/week, error cost, and a gate design. Future-state process maps show the category boundaries visually — owners immediately understand a map that shows "AI does this, Maria approves here."

## Advanced Version
Per-vertical classification libraries: for HVAC, for law offices, for property management — pre-built inventories of which tasks fall where, refined across dozens of audits. This library is proprietary IP ([[ten-year-scale-plan|Ten-Year Scale Plan]]) and what lets junior consultants produce senior-quality future-state designs.

## Revenue Connection
Category 2 and 3 work is where the quantified savings live (the [[smb-ai-audit-method|audit math]]); category 4 roles create the training and ongoing-management services in the [[retainer-model|retainer]]; and the category boundaries themselves are what you're paid to keep calibrated as models improve — recurring engineering work that never runs out.

## Human-Agent Management Connection
This page is the framework the whole connection layer is built on: it defines *where* agents work, *where* humans work, and *where* the new management jobs sit. Apply it through the [[smb-ai-audit-method|audit]], enforce it through [[quality-control-and-risk-gates|gates]], staff it through [[agent-manager-job-design|role design]].

## Risks / Failure Modes
- **Misclassification up:** putting judgment work in AI's hands — the failure that reaches a client's customer or books. Gates and the human-only list exist to prevent it.
- **Misclassification down:** keeping trivially automatable work human out of caution — leaves the ROI unrealized and the proposal weak.
- **Static classification:** the boundaries move as models and the business change; an unmaintained model quietly becomes wrong in both directions. That's a retainer deliverable, not a one-time artifact.

## Related Pages
- [[progressive-operating-thesis|Progressive Operating Thesis]] — why this model exists
- [[smb-ai-audit-method|SMB AI Audit Method]] — where classification happens
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]] — enforcing category 3
- [[agent-manager-job-design|Agent Manager Job Design]] — staffing category 4
- [[human-role-redesign|Human Role Redesign]] — the transition plan for client staff
