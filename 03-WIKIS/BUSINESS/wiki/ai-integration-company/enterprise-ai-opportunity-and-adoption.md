---
type: reference
timeline: reference
tags:
  - phase-1
  - market-research
  - ai-adoption
  - audit
---

# Enterprise AI Opportunity and Adoption

> A cross-industry pattern map for finding valuable AI work and diagnosing why
> deployment stalls. It is an audit lens, not a catalog of products to sell.

## Purpose

Translate enterprise use cases and transformation research into questions Chris
can use with SMBs without copying enterprise architecture, budgets, or hype.

## Key Idea

High-value AI opportunities repeat across industries because business functions
repeat. The strongest opportunities combine a measurable workflow, usable data,
a human owner, an exception path, and a business outcome. Adoption fails when a
company buys models or pilots without changing the surrounding process,
responsibility, data, and management system.

## Cross-Industry Opportunity Patterns

| Pattern | Typical work | Audit evidence | Required gate |
|---|---|---|---|
| Intake and triage | Leads, claims, cases, requests, permits, tickets | Queue volume, response delay, misrouting | Confidence threshold and escalation owner |
| Document production | Proposals, contracts, appeals, reports, marketing | Draft hours, rework, missing fields | Source validation and final approval |
| Customer or employee assistance | Support, knowledge retrieval, guided service | Search time, repeat questions, abandonment | Retrieval citations and human handoff |
| Forecasting and planning | Demand, staffing, liquidity, maintenance, inventory | Forecast error, stockouts, overtime, downtime | Monitoring, override, and drift review |
| Pricing and commercial optimization | Pricing, promotions, bundles, next-best action | Margin leakage, stale pricing, inconsistent offers | Approval limits and fairness review |
| Risk, anomaly, and quality detection | Fraud, defects, safety, cyber, compliance | Missed incidents, review burden, false positives | Independent sampling and appeal path |
| Scheduling and resource allocation | Crews, assets, routes, labs, field work | Wait time, utilization, rescheduling | Constraint rules and dispatcher override |
| Software and technical work | Code, tests, specifications, RFP responses | Cycle time, defects, review backlog | Tests, security review, and accountable owner |
| Research and decision preparation | Market, policy, clinical, engineering, finance | Analyst hours, evidence fragmentation | Provenance, uncertainty, and expert judgment |

The pattern is more durable than the industry example. A health-care claims use
case and a construction change-order use case may share the same document,
classification, exception, and approval architecture.

## AI-Fueled Operating Diagnostic

Assess seven layers before recommending a build:

1. **Outcome:** What economic or service result must move?
2. **Workflow:** Which end-to-end process produces that result, and where is the
   constraint?
3. **Use-case portfolio:** Which few cases combine value, feasibility, and safe
   adoption instead of creating scattered pilots?
4. **Data and technology:** Is the needed data accessible, governed, timely, and
   connected to production systems?
5. **People and roles:** Who owns the outcome, reviews exceptions, maintains
   knowledge, and improves the workflow?
6. **Delivery capability:** Can the company deploy, monitor, measure, and update
   the system after launch?
7. **Governance:** Are privacy, security, fairness, reliability, transparency,
   and accountability controls proportional to the consequence?

## SMB Translation

- Start with one workflow and one baseline, not an enterprise AI strategy.
- Use existing client-owned systems and data before proposing a platform rebuild.
- Prefer assistance and human-review work before autonomous action.
- Make the internal workflow owner visible before implementation.
- Measure adoption and business outcome together. A working model that staff
  bypass is not a successful deployment.
- Treat enterprise examples as possibility evidence only. They do not prove ROI,
  feasibility, legality, or customer fit in a specific SMB.

## Practical Actions

- Add the opportunity-pattern table to audit preparation; use it after mapping
  reality, never as a leading checklist that forces AI into the process.
- Score each candidate on outcome value, workflow readiness, data readiness,
  gate burden, adoption ownership, and measurement quality.
- Build the future-state map through the [[human-agent-operating-model|Human-Agent
  Operating Model]] and [[quality-control-and-risk-gates|Quality Control & Risk
  Gates]].

## Beginner Version

Use the pattern map to notice opportunities, then require observation, volumes,
cost, and a named owner before recommending one.

## Intermediate Version

Maintain a use-case portfolio per client and sequence shared prerequisites. One
clean data or integration improvement should unlock several measured workflows.

## Advanced Version

Build vertical pattern libraries with benchmarks, gate designs, adoption roles,
and proven economics from delivered engagements.

## Revenue Connection

The map improves audit depth and creates expansion paths without selling random
tools. The adoption diagnostic also exposes sellable work around data readiness,
workflow redesign, training, governance, and ongoing monitoring.

## Human-Agent Management Connection

Every opportunity must name what AI produces, what a human judges, what escalates,
and who improves the rules. Enterprise transformation evidence supports the
[[progressive-operating-thesis|Progressive Operating Thesis]]: value comes from
redesigning work around AI, not distributing access to a tool.

## Risks / Failure Modes

- Treating an industry use-case catalog as proof of demand.
- Starting with autonomous agents where reviewable assistance would work.
- Building isolated pilots with no production owner or measurement plan.
- Copying enterprise architecture into an SMB before the workflow earns it.
- Confusing model performance with business performance.

## Source Coverage

### *The AI Dossier*

Source: `raw/The AI Dossier.pdf` (190 PDF pages). All 86 use cases were reviewed
by industry chunk and normalized into the reusable patterns above; individual
vendor-style narratives were not duplicated.

| PDF range | Industry chunk | Disposition |
|---|---|---|
| 1-4 | Framework and contents | Ingested into pattern/gate method |
| 5-38 | Consumer | Ingested into pricing, inventory, service, marketing, planning, and supply-chain patterns |
| 39-64 | Energy, Resources and Industrials | Ingested into maintenance, safety, field, logistics, design, and planning patterns |
| 65-94 | Financial Services | Ingested into risk, intelligence, personalization, data, cyber, and service patterns |
| 95-124 | Government and Public Services | Ingested into intake, permitting, policy, contracts, planning, and multilingual-service patterns |
| 125-154 | Life Sciences and Health Care | Ingested into research, administration, inventory, claims, quality, and decision-support patterns |
| 155-190 | Technology, Media and Telecommunications | Ingested into technical sales, software, support, content, testing, and knowledge patterns |

### *All-In on AI*

Source: `raw/All in on AI_how smart companies win with ai.pdf` (221 PDF pages),
reviewed chapter-by-chapter.

| PDF range | Source chunk | Disposition |
|---|---|---|
| 1-13 | Front matter and introduction | Ingested into operating premise |
| 14-32 | Ch. 1: AI-fueled organizations | Ingested into outcome/workflow standard |
| 33-50 | Ch. 2: Human side | Ingested into roles, adoption, and training |
| 51-77 | Ch. 3: Strategy | Ingested into portfolio and strategic alignment |
| 78-98 | Ch. 4: Technology and data | Ingested into readiness diagnostic |
| 99-123 | Ch. 5: Capabilities | Ingested into delivery/management capability |
| 124-158 | Ch. 6: Industry use cases | Cross-checked against Dossier patterns; no duplicate catalog |
| 159-193 | Ch. 7: Becoming AI fueled | Ingested into transformation sequence |
| 194-221 | Notes, sources, and index | Retained as provenance; no standalone wiki content |

## Related Pages

- [[ai-economics-and-decision-workflows|AI Economics and Decision Workflows]]
- [[market-map|Market Map]]
- [[smb-ai-audit-method|SMB AI Audit Method]]
- [[progressive-operating-thesis|Progressive Operating Thesis]]
- [[human-agent-operating-model|Human-Agent Operating Model]]
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]]
