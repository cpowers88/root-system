---
type: reference
tags:
  - capability
  - tools
stage: phase-1
timeline: reference
---

# Tool Stack

> The standard software toolkit: what to master, what to run the business on, and the rules for adding anything new.

## Purpose
Standardize the tools used for delivery and internal operations, so skills compound, builds are consistent and maintainable, and every new client doesn't mean a new learning curve.

## Key Idea
**Depth in a boring stack beats breadth in a shiny one.** Clients don't pay for tool knowledge; they pay for outcomes delivered reliably — and reliability comes from using instruments you know cold. Pick one tool per job, master it, and add new tools only through a deliberate evaluation gate. Tool names below will age; the *categories and selection rules* are the durable content.

## Delivery Stack (What You Build Client Systems With)

| Category | Primary pick | Notes / alternates |
|---|---|---|
| Integration/automation platform | **Make** (visual, cheap, fast) | **n8n** as the second platform: self-hostable, better for complex logic and data-control-sensitive clients. Zapier only when a client already lives in it. |
| Custom code layer | **Python** (or JS) + serverless/cloud functions | For what no-code can't do: complex transforms, custom APIs, heavy document processing |
| Agentic delivery environment | **Claude Code** | The delivery multiplier for the whole custom-code layer — per-client configs, code generation with review gates. Full playbook: [[claude-code-leverage]] |
| LLM APIs | **Claude API** (primary), OpenAI as alternate | Structured outputs, vision for document extraction; abstract the provider so you can switch — see [[skill-roadmap|claude-api patterns in Skill Roadmap layer 2]] |
| Document extraction | LLM vision + a dedicated OCR/extraction service as needed | Choose per document type by accuracy testing, not marketing ([[document-automation-pathway|Document Automation]]) |
| CRM (to implement for clients) | **HubSpot** (free tier → paid) | **Pipedrive** for simpler sales-only clients; respect strong vertical CRMs (ServiceTitan, Jobber, Clio) — integrate, don't replace ([[crm-and-sales-ops-pathway|CRM pathway]]) |
| Databases / storage | **Airtable** (client-friendly) + **Postgres** (real workloads) | Airtable doubles as lightweight client UI |
| BI / dashboards | **Looker Studio** (free, good enough early) | Metabase or Power BI when clients need more; warehouse (e.g., BigQuery) only at real data volume ([[data-and-dashboard-pathway|Dashboard pathway]]) |
| Forms & intake | Jotform / Fillout / Tally | Whichever integrates cleanest with the client's stack |
| E-sign & documents | Client's existing tool where possible | PandaDoc/DocuSign otherwise |

## Internal Stack (What You Run the Company On)
- **CRM & pipeline:** the same CRM you implement for clients — you must live in what you sell
- **Proposals & contracts:** template library + e-sign
- **Project delivery:** a simple PM board (Notion/ClickUp/Linear) with the standard [[fulfillment-system|fulfillment lifecycle]] as its template
- **Documentation:** this wiki pattern — one source of truth for playbooks, client system inventories, and SOPs
- **Password/credential management:** a proper password manager with per-client vaults, from day one — non-negotiable
- **Monitoring:** centralized error/failure alerting across all client automations into one triage channel ([[retainer-model|Retainer Model]] depends on this)
- **Bookkeeping:** QuickBooks/Xero + a real accountant early
- **Time/effort logging:** lightweight, but real — margin per engagement is unknowable without it ([[pricing-models|Pricing Models]])

**Human-review requirement by category:** any tool producing customer-facing or financial output (LLM APIs, document extraction, AI-drafted anything) ships behind a [[quality-control-and-risk-gates|review gate]]; pure plumbing (integration platforms, storage, forms) needs monitoring but not human review; dashboards need data-quality reconciliation rather than approval. Deciding the review requirement is part of choosing the tool.

## Tool Selection Rules
1. **One primary tool per category.** A second is allowed only with a written reason (e.g., n8n for self-host requirements).
2. **New tools pass an evaluation gate:** solves a problem the current stack can't; tested on an internal project first; someone owns learning it; documented before first client use.
3. **Client-owned accounts always.** Systems run in the client's name and billing; you hold admin access. This is ethics *and* good business — hostage-taking destroys referrals; see [[fulfillment-system|Fulfillment System]].
4. **Bias to boring.** Prefer the tool with 5 years of stability over this month's launch. You are selling reliability.
5. **Pass through client-specific software costs** — itemized on invoices, never absorbed.

## Practical Actions
- Set up the internal stack this month — CRM, password manager, PM board, bookkeeping — before client volume makes it painful.
- Build your automation-platform mastery project: an internal pipeline connecting your forms → CRM → invoicing → monitoring. Practice and demo in one.
- Start the "evaluation list" for tools that tempt you; review quarterly instead of impulsively.

## Evaluation List
*Tools that tempt — reviewed quarterly, not adopted on impulse (per the Practical Actions rule above).*

| Tool | Tempted by | Category it would compete with | Status |
|---|---|---|---|
| Power Automate | Free access via school M365 tenant (July 2026); parallels the automation skill already being built in the MCP Bootcamp; relevant if an Advisor-Builder prospect already lives in Microsoft rather than Make/n8n | Integration/automation platform | Watching — not adopted, no client need yet |
| Power BI | Free access via school M365 tenant (July 2026); already named as the Looker Studio alternate above | BI / dashboards | Watching — not adopted, Looker Studio remains primary |

## Beginner Version
Minimum viable stack: Make + HubSpot free + Airtable + Looker Studio + Claude API + a password manager + QuickBooks. Under ~$150/mo total. Master these seven before touching anything else.

## Intermediate Version
The beginner seven mastered and producing, plus: n8n for logic the visual platform can't hold, a real monitoring/alerting channel across all client builds, per-client Claude Code configurations ([[claude-code-leverage]]), and the evaluation gate actually enforced — new tools tested internally before any client sees them.

## Advanced Version
Add: self-hosted n8n for enterprise-ish clients, a proper warehouse + modeled BI layer, internal monitoring dashboard across all retainer clients, template/component libraries per pathway, and a documented internal platform ("how we build") that new hires learn from — the stack itself becomes an asset with resale value in the [[ten-year-scale-plan|Ten-Year Scale Plan]].

## Revenue Connection
Stack discipline shows up directly in margin: mastered tools cut delivery hours per project by 30–50%, monitoring automation is what makes 70%+ retainer margins possible, and standardized builds are what let hires deliver profitably. Tool sprawl, by contrast, is a silent tax on every engagement.

## Human-Agent Management Connection
Tools are where the [[human-agent-operating-model|operating model]] gets physical: review queues, approval interfaces, exception dashboards, and logs are all *tool choices*, and a stack that makes reviewing painful produces rubber-stamping no matter how good the [[quality-control-and-risk-gates|gate design]] is. Pick tools your client's [[agent-manager-job-design|operators]] will actually enjoy working in — the laziest-user test applies to gates too.

## Risks / Failure Modes
- **Tool sprawl** — a silent tax on every engagement; the one-primary-per-category rule exists for margin, not tidiness.
- **Vendor dependency** — never let one platform hold the whole practice hostage; abstract LLM providers and keep the second automation platform warm.
- **Shiny-tool procurement as procrastination** — the evaluation list and quarterly review convert impulse into process ([[what-not-to-do|What NOT To Do]]).

## Related Pages
- [[skill-roadmap|Skill Roadmap]] — the order to learn the stack in
- [[fulfillment-system|Fulfillment System]] — the stack in use
- [[workflow-automation-pathway|Workflow Automation Pathway]] — primary consumer of the delivery stack
- [[what-not-to-do|What NOT To Do]] — tool-collecting as a failure mode
