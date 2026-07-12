---
tags:
  - phase-4
  - pathway
  - data
---

# Data & Dashboard Pathway

> Business intelligence for owners flying blind: KPIs, reporting, and decision visibility built on the systems you've integrated.

## Purpose
Define the data, reporting, and dashboard service line — how to turn a client's scattered operational data into the numbers the owner actually runs the business on.

## Key Idea
Most SMB owners cannot answer basic questions about their own business — true job profitability, lead-source ROI, cash position next month, technician utilization — because the data lives in five disconnected systems and a drawer of spreadsheets. This pathway builds the **pipe → warehouse → dashboard** layer that answers those questions automatically, plus AI-assisted narrative reporting on top. It is the natural second or third sale after integration work, because integration is what makes the data reachable.

## Why It Matters
- **Owners are personally addicted to it.** Automation helps their staff; dashboards help *them*. Nothing renews a retainer like the owner checking your dashboard every morning.
- **It reveals the next project.** Visible bottlenecks and leaks become the roadmap for further automation work — this pathway is a pipeline generator for the others.
- **Strong engineering fit:** data modeling, ETL, and metric definition reward systems discipline and punish improvisation. See [[skill-roadmap|Skill Roadmap]].

## What Gets Sold (Typical Builds)
- **Owner's KPI dashboard:** the 8–12 numbers that run the business (sales, pipeline, cash, jobs, utilization) auto-refreshed daily
- **Job/project profitability reporting:** quoted vs. actual cost per job — often the single most valuable number a trades or manufacturing client has ever seen
- **Sales & marketing attribution:** lead source → close rate → revenue, closing the loop on the [[crm-and-sales-ops-pathway|CRM work]]
- **Cash flow visibility:** AR aging, payment velocity, projected position
- **AI-assisted reporting:** dashboards feeding drafted weekly/monthly narrative summaries ("what changed and why") delivered to the owner's inbox
- **Data cleanup & consolidation:** the unglamorous prerequisite — deduplication, standardization, connecting systems — sold honestly as Phase 1

## Delivery Notes (What Makes This Pathway Different)
- **Metric definitions are the hard part, not the charts.** "Gross margin per job" means three different things to the owner, the bookkeeper, and the foreman. Get definitions signed off in writing before building.
- **Garbage in kills you.** If source data is unreliable, the dashboard will be wrong in ways the owner *will* notice, and it will burn trust. Audit data quality first; quote cleanup as its own phase.
- **Fewer numbers, more trust.** A 10-metric dashboard that's always right beats a 60-metric wall. Start with the owner's top 5 questions.

## Pricing
- Owner KPI dashboard (2–3 sources): **$5,000–$12,000** build
- Full BI layer (warehouse + multi-source + several dashboards): **$15,000–$40,000**
- Ongoing: data pipelines break when source systems change — a **$500–$2,500/mo** monitoring/maintenance component is legitimate and necessary. See [[pricing-models|Pricing Models]].

## Practical Actions
- Standardize one BI toolchain (see [[tool-stack|Tool Stack]]) and build a demo dashboard on realistic fake trades-company data for sales calls.
- Add a "questions you can't currently answer" section to every [[smb-ai-audit-method|audit]] — it plants this pathway's seed.
- Practice the metric-definition interview: for any KPI, force the answers to "exact formula? source fields? who owns accuracy?"

## Beginner Version
One dashboard, 2–3 data sources, off-the-shelf connectors, top-5 owner questions only. Looker Studio or similar keeps costs near zero. Deliver alongside an automation project rather than standalone.

## Intermediate Version
Owner KPI dashboards plus AI-drafted narrative reporting ("what changed and why") as the standard package: dashboards auto-refresh, the AI drafts the weekly summary, and either you or a client-side reviewer approves it before it hits the owner's inbox. Metric definitions signed off in writing before every build; data-cleanup quoted honestly as Phase 1.

## Advanced Version
Proper lightweight warehouse per client, modeled metrics layer, anomaly alerts ("margin on job type X dropped 9% this month"), AI narrative reporting, and quarterly business reviews where you walk the owner through their numbers — which is also where next-phase projects get sold.

## Revenue Connection
Mid-to-high tickets, near-automatic maintenance retainers, and the strongest client-retention effect of any pathway: the owner who runs their Monday meeting off your dashboard does not churn. Also the engine of expansion revenue, since every visible problem becomes a proposal.

## Human-Agent Management Connection
Dashboards are the **management-visibility layer of the operating loop** — they're how owners supervise AI-assisted operations without micromanaging them: exception counts, straight-through rates, queue ages, and workflow throughput all belong on the owner's dashboard next to sales and cash ([[progressive-operating-thesis|Progressive Operating Thesis]]). AI-drafted narrative reports are category-3 work — drafted first-pass, human-approved — and the [[agent-manager-job-design|agent manager's]] weekly numbers come from here.

## Risks / Failure Modes
- **Wrong numbers** — one metric the owner catches being wrong burns the whole dashboard's trust; audit data quality first, reconcile continuously.
- **Metric-definition drift** — "margin" meaning different things to different people turns the dashboard into an argument generator; signed definitions before building.
- **Vanity walls** — 60 metrics nobody acts on; start from the owner's top 5 questions and stop.

## Related Pages
- [[crm-and-sales-ops-pathway|CRM & Sales Ops Pathway]] — the pipeline data feeding attribution
- [[document-automation-pathway|Document Automation Pathway]] — extracted data worth reporting on
- [[retainer-model|Retainer Model]] — monitoring and QBRs as retainer deliverables
- [[tool-stack|Tool Stack]] — the BI toolchain
