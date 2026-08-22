---
type: template
timeline: next
status: draft
reference_priority: core
tags: [business, apqc, client, technology, audit]
---

# Workflow and Technology Stack Evidence Template

## Metadata

**Asset Name:** Workflow and Technology Stack Evidence Template  
**File Name:** `APQC_13_1_WORKFLOW_TECHNOLOGY_STACK_EVIDENCE_TEMPLATE.md`  
**Primary APQC Process:** 13.1 Manage Business Processes (13.1.2 Design and model processes)  
**Secondary APQC Process:** Cross-functional; use the APQC area that owns the workflow under study  
**Asset Type:** template / decision aid / report section  
**Technical Tags:** workflow mapping / technology stack / data / integration / automation / AI / measurement  
**Business Use Case:** Document what technology a business uses in one workflow, what each component is supposed to do, how well the stack performs, and the smallest justified improvement  
**Maturity:** draft  
**Source or Origin:** `00-BRAIN\Session_Logs\BUSINESS_WORKFLOW_AND_TECHNOLOGY_STACK_RESEARCH_REPORT_2026-07-18.md`  
**Owner:** Chris Powers  
**Last Reviewed:** July 18, 2026  
**Index Row Added:** yes

> Copy this file for each internal practice case or authorized client engagement.
> Never fill the master directly. Active client-specific/private copies live in the
> authorized client workspace outside `.ROOT`.

---

## 1. Research Decision

**Business/industry:**  
**NAICS sector/subsector:**  
**Geography:**  
**Business size band:**  
**Revenue/maturity band:**  
**Workflow selected:**  
**Decision this research must support:**  
**Why this workflow matters now:**  
**Scope boundary:**  
**Explicit non-goals:**  

### Governing question

> Given this workflow failure, what is the smallest technology architecture that
> fixes it at this business's current maturity level, and what evidence would justify
> moving to a more advanced layer?

## 2. Evidence Source Ledger

| Source | Publisher/owner | Evidence role | Population/sample | Reference period | Geography/industry detail | Measures used | Main limitation/bias | Freshness/recheck date | Link/file |
|---|---|---|---|---|---|---|---|---|---|
| Census BTOS core | U.S. Census Bureau | National business conditions | U.S. employer businesses excluding farms |  | Sector/subsector, state, MSA, size | Performance, revenue, demand, employment, prices | Aggregate/self-report; biweekly volatility | Re-pull before external use |  |
| Census BTOS AI Supplement | U.S. Census Bureau | AI adoption/function/task baseline |  | Nov. 2025-Feb. 2026 collection | Industry, geography, firm size | Current/future use, functions, tasks, investment, effects | Wording changes limit comparisons with 2024 | Annual supplement/recheck |  |
| Jobber HSER 2026 Q1 | Jobber | Home-service operating benchmark | Cohort of U.S. Jobber users | Q1 2026 | Green, Cleaning, Contracting, Construction | Revenue, new work, invoice size, digital payments | Proprietary platform cohort; not whole market | Quarterly |  |
| Jobber 2026 Trends | Jobber/Conjointly | Owner practices and technology sentiment | 1,050 U.S. home-service owners | Dec. 2025 survey | Trade, revenue, maturity, performance cohorts | Pricing, leads, quoting, challenges, AI use | Self-report/vendor publication; ±3 points at 90% confidence | Annual/recheck |  |
|  |  |  |  |  |  |  |  |  |  |

## 3. Business and Operating Context

| Dimension | Evidence | Current condition | Confidence | Why it matters to this workflow |
|---|---|---|---|---|
| Demand/new work |  |  |  |  |
| Revenue/margins |  |  |  |  |
| Labor/capacity |  |  |  |  |
| Input costs |  |  |  |  |
| Technology adoption |  |  |  |  |
| AI adoption/use |  |  |  |  |
| Business maturity |  |  |  |  |

## 4. Workflow Definition

**Trigger:**  
**Case/object being followed:**  
**Customer/user:**  
**Start event:**  
**End event:**  
**Decision owner:**  
**Primary outcome:**  
**Failure outcome:**  
**Volume/frequency:**  

| Step | Actor | Input | Action/decision | System/tool | State created or changed | Output/handoff | Wait/rework/exception | Evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |

### Workflow diagnosis

**Symptom:**  
**Waste:**  
**Root-cause hypothesis:**  
**Constraint:**  
**Falsifying evidence:**  
**Economic consequence:**  

## 5. Current Technology Stack Inventory

| Tool/system | Category | Workflow step | Job it is supposed to do | Actual users | Source of truth? | Information stored | Inputs/outputs | Integration method | Manual workaround | Failure mode | Owner/support | Monthly/annual cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | yes/no/partial |  |  | native/API/file/manual |  |  |  |  |

### State and boundary checks

| Fact/state | Authoritative system | Who may change it? | Copies/shadow systems | Conflict rule | Backup/recovery | Evidence quality |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 6. How Well the Stack Works

Use a separate row for each claim. Do not score the entire stack with one opinion.

### Evidence levels

| Level | Meaning |
|---:|---|
| 0 | Unknown or vendor assertion |
| 1 | Owner/worker opinion |
| 2 | Direct observation or artifact trace |
| 3 | Reconciled operating data |
| 4 | Before/after intervention measurement |
| 5 | Repeated or comparison-backed result |

| Tool/system or handoff | Intended outcome | Adoption/usage measure | Workflow coverage | Time/cost/quality result | User friction | Reliability/control result | Evidence level | Confidence | Verdict |
|---|---|---|---|---|---|---|---:|---|---|
|  |  |  |  |  |  |  |  | low/medium/high | effective/partial/ineffective/unknown |

### Minimum outcome measures

| Metric | Definition | Baseline | Current | Target | Data source | Owner | Review date |
|---|---|---:|---:|---:|---|---|---|
| Lead/cycle time |  |  |  |  |  |  |  |
| First-pass completeness/accuracy |  |  |  |  |  |  |  |
| Rework/exception rate |  |  |  |  |  |  |  |
| Manual touches/double entry |  |  |  |  |  |  |  |
| Revenue/cash-flow consequence |  |  |  |  |  |  |  |
| User adoption |  |  |  |  |  |  |  |

## 7. Market Pattern vs. Business Reality

| Claim | Aggregate/industry evidence | Observed business evidence | Agreement, difference, or unknown | Implication/test |
|---|---|---|---|---|
|  |  |  |  |  |

Do not use an industry average to overwrite direct evidence from the business. Use
the difference to form a question: business-specific variation may be the finding.

## 8. Recommendation Ladder

| Rung | Candidate response | Existing capability available? | Expected value | Cost/effort | Risk/maintenance | Evidence for/against | Verdict |
|---:|---|---|---|---|---|---|---|
| 1 | Eliminate the step |  |  |  |  |  |  |
| 2 | Simplify the workflow |  |  |  |  |  |  |
| 3 | Use what they own |  |  |  |  |  |  |
| 4 | Configure off-the-shelf |  |  |  |  |  |  |
| 5 | Integrate existing systems |  |  |  |  |  |  |
| 6 | Build light |  |  |  |  |  |  |
| 7 | Build real/custom |  |  |  |  |  |  |

## 9. Proposed Future-State Stack

| Layer | Keep/change/add/remove | Component or category | Why it earns a place | State/data owned | Interface/contract | Human role/control | Failure/recovery | Exit path |
|---|---|---|---|---|---|---|---|---|
| Observe/capture |  |  |  |  |  |  |  |  |
| Source of truth |  |  |  |  |  |  |  |  |
| Integration |  |  |  |  |  |  |  |  |
| Decision/reporting |  |  |  |  |  |  |  |  |
| Custom application |  |  |  |  |  |  |  |  |
| AI feature |  |  |  |  |  |  |  |  |
| Operations/security |  |  |  |  |  |  |  |  |

## 10. Smallest Provable Slice

**Proposed intervention:**  
**Assumption being tested:**  
**Named owner:**  
**Time/cost ceiling:**  
**Data required:**  
**Human approval/control:**  
**Acceptance check:**  
**Stop condition:**  
**Rollback/exit:**  
**Review trigger/date:**  

## 11. Return Packet

**1. Outcome:** What became true?  
**2. Evidence:** What supports the finding?  
**3. Artifact:** What reusable output was produced?  
**4. Capability:** What can Chris now do that was not previously proven?  
**5. Next exact action:** What single action follows?  

## 12. Internal Validation and Packaging

**Practice case used:**  
**What worked:**  
**What broke or confused the user:**  
**Fields added/removed after use:**  
**Privacy check complete:** yes / no  
**Ready for external client instance:** yes / no  
**Maturity after test:** idea / draft / tested internally / client-ready / deployed  

### Next test

Complete one internal copy using the sanitized July 18 construction
change-order-to-cash evidence. Success means the template produces a bounded stack
decision without confusing national/industry evidence with observed workflow proof.

