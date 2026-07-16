---
domain: systems
type: method
timeline: reference
status: active
reference_priority: core
tags: [systems, operations-research, modeling, implementation, audit]
---

# Operations Research Study Lifecycle

**Summary**: Operations research is an end-to-end decision practice, not just
mathematical optimization. A successful study moves from a vague operational
problem through evidence, formulation, testing, a maintained decision system,
implementation, and continuing feedback.

**Source**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman,
Introduction to Operations Research), Chapter 2, "Overview of the Operations
Research Modeling Approach" (printed pp. 10-24; physical PDF pp. 41-55),
reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## The Six Overlapping Phases

| Phase | Required outcome | Common failure |
|---|---|---|
| 1. Define the problem and gather data | Agreed objectives, system boundary, constraints, alternatives, decision owners, and usable evidence | Solving the stated symptom or a local department's problem instead of the organization's real problem |
| 2. Formulate a mathematical model | A deliberately simplified representation linking decisions to consequences | Treating the first formulation as the one right model or hiding judgment behind notation |
| 3. Derive solutions | A computer-based procedure that finds and compares feasible courses of action | Reporting "optimal" without saying it is optimal only relative to the model and its assumptions |
| 4. Test and refine | Evidence that the model predicts relevant differences between alternatives well enough for the decision | Equating historical fit with validity or testing only with the data used to build the model |
| 5. Prepare ongoing application | A documented operating system containing data interfaces, model, solution procedure, postoptimality analysis, reports, ownership, and maintenance | Delivering a one-time answer that future users cannot run, interpret, or update |
| 6. Implement | The recommendation translated into operating procedures, training, phased adoption, monitoring, and revision | Assuming technical completion creates benefits without management and user ownership |

The phases overlap and loop. A failed test may require new data, a revised problem
definition, or a different formulation. Implementation feedback may expose a changed
constraint and reopen the model.

## Phase 1: Find the Real Problem

Practical OR problems arrive vague and politically shaped. Before calculating:

- Identify who makes the decision, who performs the work, and who bears the effect.
- Define the objective from the whole organization's perspective; local objectives
  can create system-wide suboptimization.
- Separate hard constraints from policies, habits, and negotiable preferences.
- Map interactions with the rest of the system and choose an explicit time horizon.
- Gather the data the decision requires, then assess fitness, lineage, recency, and bias.

Data work is often a large share of the study. Needed data may be missing, stale,
stored in the wrong form, or based on judgment; in other cases the problem is too
much unfiltered data. Collection, cleaning, reconciliation, and estimation are part
of the model, not clerical preparation outside it.

## Phase 2: Formulate for Insight and Use

There is no single correct model. Build a succession of better models, beginning
with the simplest version capable of exposing the decision structure.

A formulation should make explicit:

- decision variables—the choices management can control;
- objective measure—the result being improved;
- constraints—the resource, policy, service, risk, and logical limits;
- parameters and evidence—the quantities treated as inputs;
- relationships and assumptions—how choices are expected to create outcomes;
- scope and omissions—what the model deliberately leaves outside.

The mathematical model is an aid to judgment. Its value is not complexity but its
ability to represent the important tradeoffs clearly enough to guide action.

## Phase 3: Derive More Than One Answer

An optimum is only optimal for the model as written. Practical success may call for
a satisficing solution when data, computation, time, usability, or organizational
constraints make exact optimization a poor target.

The solution phase should produce:

- the recommended course of action;
- useful alternatives and their tradeoffs;
- postoptimality and what-if analysis;
- sensitive assumptions and thresholds;
- consequences of changing priorities or constraints;
- an explanation in the language of management and operations.

The practical standard is not "the mathematical best answer." It is a better guide
to action than the available alternatives.

## Phase 4: Test What Matters

Treat model testing like debugging a large program: assume the first version contains
important flaws and search for them.

1. Have a person who did not formulate the model review the whole problem and model.
2. Recheck the problem definition, boundary, and omitted interactions.
3. Verify dimensional consistency and calculation logic.
4. Vary parameters and decision variables, including extreme values.
5. Compare behavior with expert knowledge and observed system behavior.
6. Use retrospective data to compare model-guided alternatives with actual practice.
7. Recognize the limit of retrospective tests: the same history may have shaped the
   formulation, and the future may not resemble the past.
8. When feasible, test against new data not available during formulation.
9. Include future users in preimplementation testing and use their feedback to revise
   the system.
10. Document the validation process for later reviewers and diagnosis.

Exact reproduction of every historical value is not the goal. The key criterion is
whether the model predicts the relative effects of alternative actions accurately
enough to support the decision.

## Phase 5: Build the Ongoing Decision System

Repeated use requires more than preserving an equation or spreadsheet. Package:

- current input sources and data interfaces;
- the model and versioned assumptions;
- the solution procedure and postoptimality analysis;
- management-facing interpretation and reports;
- operating procedures and action authorities;
- maintenance ownership, change triggers, and review cadence;
- reproducibility instructions and test evidence.

The system should support managerial judgment rather than conceal or replace it.
Personnel changes and changing conditions should not make the analysis unusable.

## Phase 6: Implement and Keep Learning

Benefits appear only when the system changes operating behavior. The study team and
operating management share responsibility for translating model results into workable
procedures, explaining the logic, training affected people, and monitoring early use.

Implementation is stronger when management and future users have participated from
the beginning. Phase changes in gradually when risk or adoption cost is high, collect
feedback, and revise when assumptions no longer hold. Reproducibility is an ethical
obligation, especially where recommendations affect many people or contested policy.

## Audit Translation

For an operational audit, the lifecycle becomes a traceable chain:

1. **Problem**: What recurring decision or failure is being improved?
2. **Evidence**: What data and frontline knowledge support the diagnosis?
3. **Model**: What variables, constraints, assumptions, and tradeoffs represent it?
4. **Proof**: Can an independent reviewer reproduce and challenge the recommendation?
5. **Operating system**: Who runs it, with what inputs, triggers, and maintenance?
6. **Adoption**: What changes in procedure, behavior, and authority make it real?
7. **Feedback**: What result or assumption change causes review?

This prevents an audit from ending at analysis. The deliverable must survive contact
with the operating system and remain useful after the analyst leaves.

## Connects to

[[model-validation-and-testing-practice]],
[[modeling-process-and-client-ethics]],
[[the-art-of-spreadsheet-modeling]],
[[sensitivity-analysis-and-postoptimality]],
[[strategic-objectives-hierarchy-and-efficient-frontiers]], and
[[designing-for-human-error-and-recovery]].

## Use / Retrieval Notes

**Use when**: Scoping an analytical engagement, converting a model into a maintained
client tool, or diagnosing why a technically sound recommendation was not adopted.

**Proof**: The engagement record traces the recommendation from an agreed problem
and evidence through independent testing, operating ownership, implementation, and
post-deployment review.
