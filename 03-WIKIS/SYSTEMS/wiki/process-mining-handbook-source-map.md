---
domain: systems
type: source-summary
timeline: reference
status: active
reference_priority: core
tags: [systems, process-mining, source-coverage, audit, automation]
---

# Process Mining Handbook - Source Map and Retrieval Router

**Summary**: The 2022 *Process Mining Handbook* is a 17-chapter summer-school
reference spanning discovery, conformance, event-log engineering, enhancement,
responsibility, industry adoption, auditing, automation, and value realization.
This map records the disposition of every chapter. Eight chapters with direct
SYSTEMS and Advisor-Builder value were read in full and consolidated into four
retrieval pages; the remaining chapters are routed to existing coverage or held
as triggered technical/domain reference.

**Source**: `Process Mining Handbook.pdf` (Wil M. P. van der Aalst and Josep
Carmona, eds., Springer LNBIP 448, 2022, 503 physical PDF pages, CC BY 4.0).
Added to immutable `raw/` on 2026-07-17.

**Last updated**: 2026-07-18

## Complete Chapter Disposition

| Part / chapter | Printed pages | Disposition |
|---|---:|---|
| Introduction - 1. Process Mining: A 360 Degree Overview | 3-34 | Existing conceptual coverage in [[process-mining-manifesto-principles-and-challenges]] and [[pm4py-process-mining-in-python]]; use this chapter for a current-in-book overview, not a duplicate page. |
| Process Discovery - 2. Foundations of Process Discovery | 37-75 | Technical reference. Existing working-level discovery coverage lives in [[pm4py-process-mining-in-python]]; reopen when choosing or explaining a discovery algorithm. |
| 3. Advanced Process Discovery Techniques | 76-107 | Technical reference for region-based discovery, Split Miner, and log-skeleton methods; activate only when basic Inductive/DFG discovery is insufficient. |
| 4. Declarative Process Specifications | 108-152 | Technical reference for DECLARE-style constraints, discovery, monitoring, and reasoning; activate for flexible/compliance-heavy processes where procedural flow is the wrong representation. |
| Conformance Checking - 5. Foundations, Milestones and Challenges | 155-190 | **Read in full** (physical pp. 162-197) -> [[conformance-checking-and-kpi-driven-process-improvement]]. |
| Data Preprocessing - 6. Foundations of Process Event Data | 193-211 | Supporting reference. Minimum event schema and XES semantics are already in [[xes-standard-for-event-logs]]; Chapter 7 supplies the practical engineering layer. Activate for uncertain events or deeper data-quality mechanics. |
| 7. Practitioner Adoption, Event Log Engineering and Data Challenges | 212-240 | **Read in full** (physical pp. 218-246) -> [[process-mining-engagement-and-value-realization]]. |
| Enhancement - 8. Foundations of Process Enhancement | 243-273 | **Read in full** (physical pp. 248-278) -> [[conformance-checking-and-kpi-driven-process-improvement]]. |
| 9. Event Knowledge Graphs | 274-319 | Triggered technical reference for multiple interacting objects/case notions. Activate when flattening orders, items, deliveries, invoices, or resources into one case would create false behavior. |
| 10. Predictive Process Monitoring | 320-348 | Triggered reference for predicting running-case outcomes or remaining time; activate only after reliable event extraction and retrospective conformance are proven. |
| Assorted Topics - 11. Streaming Process Mining | 349-372 | Triggered reference for unbounded event streams and low-latency monitoring; not needed for the first batch/CSV proof. |
| 12. Responsible Process Mining | 373-401 | **Read in full** (physical pp. 377-405) -> [[responsible-process-mining-fact-gate]]. |
| Industrial Applications - 13. From Process Discovery to Process Execution | 405-415 | **Read in full** (physical pp. 407-417) -> [[process-mining-engagement-and-value-realization]]. Vendor/market claims are a 2022 snapshot. |
| 14. Using Process Mining in Healthcare | 416-444 | Domain reference. Activate for a healthcare-specific process question; do not generalize its clinical data and stakeholder constraints to ordinary operations. |
| 15. Process Mining for Financial Auditing | 445-467 | **Read in full** (physical pp. 447-469) -> [[process-mining-audit-and-automation-opportunity]]. Audit standards cited are historical and require current verification before professional reliance. |
| 16. Robotic Process Mining | 468-491 | **Read in full** (physical pp. 470-493) -> [[process-mining-audit-and-automation-opportunity]]. Product examples are a 2022 snapshot; the selection logic is the durable contribution. |
| Closing - 17. Scaling Process Mining to Turn Insights into Actions | 495-502 | **Read in full** (physical pp. 495-502) -> [[process-mining-engagement-and-value-realization]]. |
| Author Index | 503 | Reference back matter; no synthesis target. |

## What the Selective Ingest Adds

The pre-existing cluster already explained discovery, XES, PM4Py, BPMN, and the
Manifesto. The handbook closes four different gaps:

1. How to scope and engineer an event log from real operational systems.
2. How conformance evidence becomes a controlled process-improvement decision.
3. How fairness, accuracy, confidentiality, and transparency constrain the work.
4. How audit findings can identify automation candidates without treating every
   repetitive click path as safe to automate.

## Activation Order

For a first real process-mining job, use the retrieval order below:

1. [[process-mining-manifesto-principles-and-challenges]] - determine whether the
   question and event data support mining.
2. [[process-mining-engagement-and-value-realization]] - scope the engagement and
   build the event-data pipeline.
3. [[pm4py-process-mining-in-python]] - execute discovery/conformance in Python.
4. [[conformance-checking-and-kpi-driven-process-improvement]] - classify and
   interpret deviations before recommending change.
5. [[responsible-process-mining-fact-gate]] - review people, data, model, and
   disclosure risks.
6. [[process-mining-audit-and-automation-opportunity]] - convert verified findings
   into audit evidence or bounded automation candidates.

## Limits

This is selective conceptual ingestion, not a transcription of all formulas,
algorithm proofs, figures, examples, or citations. The raw PDF remains the authority
for technical implementation detail. Product, adoption, market-growth, regulatory,
and professional-standard claims are anchored to 2022 and must be reverified when
used for a current decision.

