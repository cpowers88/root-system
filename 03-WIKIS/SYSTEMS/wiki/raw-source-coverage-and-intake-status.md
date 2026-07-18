---
type: reference
timeline: reference
status: active
reference_priority: core
tags: [systems, source-coverage, intake, governance]
---

# SYSTEMS Raw-Source Coverage and Intake Status

**Summary**: This is the disposition ledger for every substantive file currently
in `03-WIKIS/SYSTEMS/raw/`. A source is either closed through named retrieval
coverage, intentionally excluded, covered in the owning BUSINESS wiki, or parked
behind a concrete activation trigger. Presence in `raw/` alone never means that a
source was reviewed.

**Last audited**: 2026-07-18 - 27 substantive raw files; the July 17 Process
Mining Handbook intake is now dispositioned.

## Closed in SYSTEMS

| Raw source | Disposition |
|---|---|
| `1905.06169v1.pdf` | Full paper represented in [[pm4py-process-mining-in-python]]. |
| `2404.06035v1.pdf` | Full PM4Py.LLM paper represented in [[pm4py-process-mining-in-python]]. |
| `2606.04350v2.pdf` | Full PM4Py-UCM paper represented in [[pm4py-process-mining-in-python]]. |
| `About XES - IEEE Task Force on Process Mining.md` | Represented in [[xes-standard-for-event-logs]]. |
| `IEEE XES Standard - IEEE Task Force on Process Mining.md` | Represented in [[xes-standard-for-event-logs]]. |
| `IEEE-Process-Mining-Manifesto-2011.pdf` | Represented in [[process-mining-manifesto-principles-and-challenges]]. |
| `Process Mining Handbook.pdf` (503 physical pp.) | Selectively compiled at full-chapter depth on 2026-07-18. Chapters 5, 7, 8, 12, 13, 15, 16, and 17 were read in full and consolidated into [[conformance-checking-and-kpi-driven-process-improvement]], [[process-mining-engagement-and-value-realization]], [[responsible-process-mining-fact-gate]], and [[process-mining-audit-and-automation-opportunity]]. Every other chapter has a named existing-coverage or triggered-reference disposition in [[process-mining-handbook-source-map]]. |
| `BPMN_1-133.pdf`, `BPMN_134-266.pdf`, `BPMN_267-399.pdf`, and `BPMN_400-532.pdf` | Four immutable chunks of one specification; modeling core ingested and formal machinery classified for lookup in [[bpmn-2-0-specification]]. Detailed range disposition is in [[log]]. |
| `BusinessDynamics.pdf` | Closed at conceptual retrieval depth. Inherited chapter coverage plus the corrected Chapter 9-16 and Chapter 21 dispositions are recorded in [[log]] and routed across the system-dynamics and Sterman case-study sections of [[index]]. |
| `factoryPhysics.pdf` | Closed at conceptual retrieval depth. Earlier chapter coverage plus the corrected Chapter 9-19 dispositions are recorded in [[log]] and routed across the Factory Physics, variability, control, and supply-chain sections of [[index]]. |
| `IntroductiontoOpersationsResearch.pdf` | Closed through the four coordinated OR passes recorded in [[log]], with named inclusions, conceptual-only sections, and reasoned exclusions. Retrieval pages occupy the OR, optimization, inventory, forecasting, and project-practice sections of [[index]]. |
| `K013989_Introduction to APQC&#039;s Process Classification Framework (PCF).pdf` | Full explainer represented in [[apqc-process-classification-framework]]. |
| `K013990_Applying the PCF for Business Value.pdf` | Full explainer represented in [[apqc-process-classification-framework]]. |
| `K013991_Understanding the Elements of APQC&#039;s Process Classification Framework (PCF).pdf` | Full explainer represented in [[apqc-process-classification-framework]]. |
| `suppyChainScience.pdf` | All Chapters 0-9 have named-page or covered-by dispositions. The corrected Chapter 5-9 closure is recorded in [[log]]. |
| `The-Design-of-Everyday-Things-Norman-2002.pdf` | Complete conceptual ingest routed by [[design-of-everyday-things-source-map]]. |
| `Value Stream Mapping Overview.md` | Represented in [[value-stream-mapping-method-and-lean-guidelines]]. |

## Covered in the Owning BUSINESS Wiki

These sources do not warrant duplicate SYSTEMS pages. Their operating concepts
remain discoverable here through adjacent Factory Physics and VSM pages.

| Raw source | Disposition |
|---|---|
| `leanmanufacturing.pdf` | MSE507 *Learning to See* workshop condensation; covered by `03-WIKIS/BUSINESS/wiki/ai-integration-company/lean-methodology.md`. |
| `leanthinking.pdf` | Womack and Jones *Lean Thinking* outline; covered by `03-WIKIS/BUSINESS/wiki/ai-integration-company/lean-methodology.md`. |
| `Theory of Constraints of Eliyahu M. Goldratt.md` | Introductory TOC Institute clipping; covered more rigorously by `03-WIKIS/BUSINESS/wiki/ai-integration-company/theory-of-constraints.md`. Its unsupported tool-name mentions do not justify a separate page. |

## Intentionally Excluded from Synthesis

| Raw source | Reason |
|---|---|
| `The OMG® Specifications Catalog.md` | Catalog/index of specifications, not teaching content. Retained only as a lookup aid. |

## Parked with Activation Triggers

Parked means **not source-complete**. These files are not an active backlog and
should not be reopened merely because they remain in the immutable raw folder.

| Raw source | Current disposition | Activation trigger |
|---|---|---|
| `AlgorithmstoLiveBy.pdf` | Broad decision-science source added 2026-07-16; no ingest attempted. Existing OR pages already cover several adjacent mechanics. | Open only for a concrete stopping, scheduling, sorting, caching, or explore/exploit decision that exposes a retrieval gap. |
| `Mike Rother - Learning to See Version 1.2 (kanban)_value stream lean.pdf` | Image-heavy canonical VSM workbook; topic-level coverage exists in [[value-stream-mapping-method-and-lean-guidelines]], but the book itself has not received visual chunk review. | Activate when building a real current-state/future-state client map, a VSM template, or a visual worked example where workbook-specific symbols and examples matter. |
| `TLS.pdf` | Three-page Pirasteh/Farah article comparing TOC, lean, and Six Sigma; reviewed only for identity and scope, not ingested. Its high-level comparison overlaps existing TOC, lean, quality, and Factory Physics coverage. | Activate when a real improvement program requires an explicit TOC-versus-lean-versus-Six-Sigma method-selection framework. |

`desktop.ini` is an operating-system metadata file, not a knowledge source, and is
excluded from intake accounting.

## Reopening Rule

When an activation trigger fires, compare the requested decision against existing
pages first. Ingest only the smallest complete visual, chapter, or section chunk
that supplies a genuine retrieval delta, and record the new disposition in this
ledger and [[log]].
