---
type: framework
timeline: reference
status: wiki-only
source_role: primary
use_cases: [audit, system-evaluation, software-delivery]
tags: [evaluation, failure-analysis, organizational-learning]
---

# Information-System Evaluation Lifecycle and Failure Levels

## Decision

Evaluate a system at four different moments. Testing only the finished technical
artifact misses whether the project should exist, whether it is drifting during
construction, whether it creates value in use, and what the organization should
learn when it fails.

| Evaluation | Check moment | Primary decision | Minimum evidence |
|---|---|---|---|
| **Strategic** | Before commitment | Start, reject, or prioritize? | problem, alternatives, expected costs/benefits, stakeholder outcome, go/no-go criterion |
| **Formative** | During design and construction | Continue, change, reduce scope, or stop? | working increment, acceptance evidence, new risk/cost information, objective comparison |
| **Summative** | After a representative period of real use | Keep, modify, expand, or retire? | adoption, functionality, usability, utility, realized cost/benefit, unintended effects |
| **Post-mortem** | After abandonment or material failure | What practice must change? | chronology, contributing conditions, failed assumptions/controls, lessons and owner |

Strategic evaluation supplies the baseline that summative evaluation later
returns to. If the expected benefit, cost, user, or workflow outcome was never
written before implementation, post-implementation claims become easy to move.

Formative evaluation is also the defense against escalation of commitment. Prior
investment is not evidence that more investment is justified. Define stop or
rescope conditions before negative evidence arrives, then compare the live
trajectory against them.

## Failure Matrix

Classify failure on two axes before proposing a remedy.

### When it failed

- **Development failure:** the system or a material part is abandoned before
  implementation.
- **Use failure:** the system is abandoned, heavily reworked, resisted, or fails
  to produce the required outcome after implementation.

### Where it failed

| Level | Typical evidence | Response owner |
|---|---|---|
| **Technical** | crashes, incorrect output, unavailable service, security or integration failure | engineering/operations |
| **Project** | uncontrolled scope, time/cost overrun, missing acceptance evidence, weak coordination | project/product owner |
| **Organizational** | low adoption, work transferred elsewhere, stakeholder resistance, no operational benefit | workflow/process owner |
| **Environmental** | regulation, labor relationship, market, dependency, or external platform changed | sponsor/strategy owner |

A technically healthy system can still be an organizational failure. Conversely,
a useful organizational response can survive a partial technical or project
failure after a bounded redesign. Diagnose the level rather than treating every
failure as a coding defect.

## Applied Evaluation Card

Use this at each gate:

```text
System/workflow:
Evaluation type:
Decision owner:
Stakeholder groups:
Original problem and baseline:
Expected functionality:
Expected usability/context of use:
Expected workflow utility or net benefit:
Current evidence:
Technical/project/organizational/environmental risks:
Continue / change / stop decision:
Next check moment and evidence:
```

Pair the card with the
[[../user-experience/user-experience-structure-skeleton-surface-and-validation|Three-Layer Worth Test]]
so functionality, usability, and utility stay separate. Use
[[software-testing-levels-and-techniques|software testing]] for technical
verification, [[user-centered-system-design-principles-and-tradeoffs|user-centered
system design]] for observed use and recovery, and
[[workflow-observation-method|workflow observation]] for organizational impact.

## Independence and Learning

The people who designed a system are poorly positioned to be its only summative
evaluators. Use an independent reviewer when the decision is consequential or
judgment-heavy. A post-mortem must be learning-oriented rather than punitive;
otherwise participants hide the information needed to improve the system.

Record product and process separately:

- Did the delivered system produce the required result?
- Did the development and implementation process expose risk early enough?
- Which assumption, control, or decision rule should change before the next
  project?

## Source and Limits

Primary source: Paul Beynon-Davies, *Business Information Systems*, 2nd ed.
(2013), Chapter 9, physical PDF pp. 328-342 (book pp. 289-303), reviewed
2026-07-27 from
`03-WIKIS/TECHNOLOGY/raw/Business Information Systems 2nd Ed. Textbook.pdf`.

The evaluation sequence and failure taxonomy are durable. Period-specific
Internet-access examples, named government procurement programs, statistics,
and technology claims were not retained as current evidence.

## Related Pages

- [[../user-experience/user-experience-structure-skeleton-surface-and-validation|UX Validation and Three-Layer Worth Test]]
- [[software-testing-levels-and-techniques|Software Testing Levels and Techniques]]
- [[../devops/just-culture-and-blameless-postmortems|Just Culture and Blameless Postmortems]]
- [[../goal-aligned-technology-gap-audit-2026-07-16|Goal-Aligned Technology Gap Audit]]
- [[user-centered-system-design-principles-and-tradeoffs|User-Centered System Design]]
- [[workflow-observation-method|Workflow Observation Method]]
