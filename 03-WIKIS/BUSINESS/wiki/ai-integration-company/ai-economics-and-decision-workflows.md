---
type: reference
timeline: reference
tags:
  - phase-1
  - ai-economics
  - workflow-design
  - audit
---

# AI Economics and Decision Workflows

> AI lowers the cost of prediction. Business value appears only when that
> prediction changes a decision, action, workflow, or strategy enough to exceed
> the cost and risk of using it.

## Purpose

Give the audit a precise way to separate AI capability from economic value.
Instead of asking "where can AI help?", decompose the decision and identify
which uncertain input, judgment, action, and feedback loop matter.

## Key Idea

A decision contains inputs, prediction, judgment about payoffs, an action, an
outcome, and feedback. Cheaper or better prediction may increase the value of
complements such as data, human judgment, integration, and action capacity while
reducing the value of a formerly scarce forecasting skill.

## Decision Anatomy

| Element | Audit question | Typical owner |
|---|---|---|
| Input | What facts are available at decision time? | System/data owner |
| Prediction | What unknown outcome must be estimated? | Model or analyst |
| Judgment | What are the costs and benefits of each possible outcome? | Accountable human |
| Action | What happens after the estimate? | Workflow operator |
| Outcome | What actually happened? | Process/customer |
| Feedback | How does the result improve the next decision? | Workflow/model owner |

Prediction is not judgment. A probability of late payment does not determine
whether to deny terms, contact the customer, change the deposit, or accept the
risk. The accountable human or approved business rule supplies the payoff logic.

## Workflow Redesign Method

1. Map the complete workflow, not only the predictive task.
2. Identify the decisions that create delay, error, cost, or lost revenue.
3. Decompose each decision using the table above.
4. Estimate the value of improved prediction at realistic accuracy levels.
5. Identify complements: data capture, integration, human judgment, training,
   monitoring, exception queues, and action capacity.
6. Redesign upstream and downstream steps; local prediction gains often move the
   bottleneck rather than improving the total flow.
7. Start with assistance or triage, measure outcomes, then consider higher
   autonomy only when the gate evidence supports it.

## Strategic Test

Most AI uses improve a task incrementally. A strategic effect requires a large
enough reduction in uncertainty to change the operating model: which customers
can be served, when action happens, what inventory is needed, who makes the
decision, or what the company can promise.

Use three questions:

- What decision becomes possible or materially different?
- Which complements become more valuable or scarce?
- Does the new prediction change the constraint or merely optimize a nonconstraint?

## Practical Actions

- Add the decision anatomy to candidate AI findings in the
  [[smb-ai-audit-method|SMB AI Audit Method]].
- Require a baseline for prediction quality and the business outcome; do not use
  model accuracy alone as ROI.
- Price integration, judgment design, gates, and feedback operations as part of
  the implementation rather than treating the model as the whole project.

## Beginner Version

Find one recurring decision, write its six elements, and identify which element
actually causes the business loss. Do not build a model unless prediction is the
limiting element.

## Intermediate Version

Redesign the end-to-end workflow around improved prediction and instrument the
outcome/feedback loop. Review false positives and false negatives in dollars.

## Advanced Version

Use a portfolio of decision workflows to identify shared data assets,
complementary capabilities, strategic operating-model changes, and new market
boundaries.

## Revenue Connection

The method converts vague AI interest into scoped diagnostic and redesign work.
It also makes hidden implementation value visible: data readiness, integration,
judgment capture, exception operations, monitoring, and continuous improvement.

## Human-Agent Management Connection

AI owns bounded prediction or first-pass analysis. Humans own payoff judgments,
high-consequence decisions, exceptions, accountability, and changes to the
decision policy.

## Risks / Failure Modes

- Automating a prediction that does not change an action.
- Treating prediction confidence as permission to remove judgment.
- Improving a local decision while moving congestion downstream.
- Ignoring false-positive/false-negative asymmetry.
- Assuming adoption is irrational before checking local economics and complements.

## Source Coverage

Source: `raw/PredictionMachines.pdf` (275 PDF pages), reviewed in complete
decision/workflow chunks.

| PDF range | Source chunk | Disposition |
|---|---|---|
| 1-68 | Prediction economics (introduction through Ch. 6) | Ingested into prediction/complement logic |
| 69-121 | Decision making (Ch. 7-11) | Ingested into decision anatomy and autonomy boundary |
| 122-150 | Tools, workflows, and job redesign (Ch. 12-14) | Ingested into workflow redesign method |
| 151-208 | Strategy, learning, and risk (Ch. 15-18) | Ingested into strategic test and risk controls |
| 209-275 | Society, notes, and back matter | Societal discussion deferred outside the active business method; provenance retained |

## Related Pages

- [[enterprise-ai-opportunity-and-adoption|Enterprise AI Opportunity and Adoption]]
- [[smb-ai-audit-method|SMB AI Audit Method]]
- [[human-agent-operating-model|Human-Agent Operating Model]]
- [[quality-control-and-risk-gates|Quality Control & Risk Gates]]
- [[theory-of-constraints|Theory of Constraints]]

