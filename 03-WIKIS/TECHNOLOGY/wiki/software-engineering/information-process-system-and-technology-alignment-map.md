---
type: framework
timeline: reference
status: wiki-only
source_role: primary
use_cases: [audit, architecture, integration, system-planning]
tags: [information-architecture, process-mapping, interoperability]
---

# Information, Process, System, and Technology Alignment Map

## Decision

Plan from the work and information outward:

```text
organizational purpose
  -> processes and actors
  -> information classes and flows
  -> information systems
  -> technology, standards, skills, and operations
```

Starting with products or vendors reverses the dependency chain. Technology
exists to support systems; systems exist to provide information for processes;
processes exist to create an organizational outcome.

## Four Linked Views

### 1. Process model

List the important activity systems and their processes, including human work,
manual controls, exceptions, and external actors. Do not limit the model to
computerized steps.

### 2. Information model

List the durable information classes the organization uses and the important
relationships between them. Examples include customer, project, estimate,
change order, invoice, employee, asset, and approval.

This is a conceptual model, not a list of files or database tables. "Customer"
is an information class; `customers_final_v3.xlsx` is one current
representation.

### 3. Process/information matrix

Cross processes against information classes:

| Process | Customer | Project | Estimate | Change order | Invoice |
|---|---|---|---|---|---|
| Qualify lead | uses/updates | creates | - | - | - |
| Prepare estimate | uses | uses | creates | - | - |
| Approve change | uses | uses | references | creates | - |
| Bill completed work | uses | uses | - | uses | creates |

Use the matrix to find:

- information with no clear owner;
- the same information recreated in several processes;
- processes operating without required information;
- incompatible names, identifiers, formats, or definitions;
- clusters that should share an application or database;
- integration boundaries where information crosses systems;
- manual systems that are operationally important but absent from the formal
  technology inventory.

### 4. System and technology portfolio

Map every current system - manual and computerized - to the processes and
information it supports. Then distinguish:

- correction or maintenance of an existing system;
- enhancement of an existing system;
- integration between existing systems;
- replacement or new system;
- infrastructure or standards work;
- bounded research needed before a decision.

Only after this map exists should the technology layer specify hardware,
software, data formats, communication methods, knowledge, skills, security,
support, maintenance, and recovery.

## Current and Future States

Maintain two views:

- **Current portfolio:** what supports the work now, including spreadsheets,
  paper, email, text messages, personal memory, and unofficial workarounds.
- **Future portfolio:** the smallest justified corrections, integrations,
  retirements, or additions needed to support the intended process.

Every future system must point to a process and information requirement. Every
current system must have a disposition: retain, configure, integrate, repair,
replace, or retire. A technology experiment remains research until its trigger,
decision, and evaluation gate are named.

### Choose the development shape deliberately

Separate two decisions that are often collapsed:

| Decision | Option | Primary advantage | Primary obligation |
|---|---|---|---|
| Product | bespoke build | close fit to distinctive work | fund scarce development and maintenance capability |
| Product | package/configuration | faster access to established capability | expose where the organization must adapt to the package |
| Sequence | staged/linear | clearer dependencies, authorization, and control | manage the cost of changing early decisions |
| Sequence | iterative | earlier user evidence, prototypes, and risk reduction | bound time, scope, and learning because resource demand is less predictable |

A package does not remove analysis, design, implementation, or evaluation. It
changes the design question from only "How should the technology fit the work?"
to also "Which parts of the work should adapt to the package, and at what
operational cost?" Record every material process compromise, customization,
integration, retained manual control, and exit dependency.

Use staged control where dependencies and irreversible commitments dominate.
Use iteration where requirements, usability, or the context of use remain
uncertain. A hybrid is normal: authorize in stages while learning through small
prototypes inside each stage.

## Alignment and Governance Check

The strategy should reduce fragmentation, redundancy, inconsistency, and
uncontrolled variation while improving interoperability. Standardization is not
an end in itself; it is justified when shared identifiers, formats, controls, or
interfaces reduce operational failure.

Use four operating checks:

1. **Plan and organize:** tie technology work to the organizational outcome.
2. **Acquire and implement:** define requirements and introduce change safely.
3. **Deliver and support:** operate, train, maintain, and recover.
4. **Monitor and evaluate:** verify continued fit, value, risk, and compliance.

Pair this map with
[[information-system-evaluation-lifecycle-and-failure-levels|the evaluation
lifecycle]] so current and future portfolios are tested before commitment,
during implementation, and after real use.

### Operating ownership

Every portfolio also needs named ownership for six different functions:

| Function | Owns |
|---|---|
| **Planning** | future information, system, and technology direction |
| **Management** | implementation of future plans and control of the current portfolio |
| **Project management** | scope, resources, coordination, evidence, and delivery |
| **Development** | analysis, design, construction, testing, and implementation |
| **Maintenance** | corrective, adaptive, and improvement work after delivery |
| **Operations** | availability, continuity, support, monitoring, and routine use |

Buying or building a system funds only part of this chain. A recommendation is
incomplete until it names who will operate, support, maintain, evaluate, and
eventually modify or retire it.

## Delivery and Service-Control Loop

Treat delivery and operation as one governed lifecycle:

```text
business justification
  -> named product or service
  -> bounded delivery stage
  -> accepted work package
  -> supported operating service
  -> measured use, incidents, cost, and benefit
  -> improve, replace, or retire
```

### Control delivery by products and stages

Define the product or service to be accepted before decomposing it into tasks.
For each stage:

1. name the deliverable, acceptance evidence, owner, dependencies, effort, and
   risk;
2. authorize a bounded work package rather than releasing an unlimited project;
3. monitor progress and quality against explicit tolerances;
4. escalate exceptions that exceed the delivery owner's authority;
5. at the boundary, update the plan, risk record, and business case before
   authorizing the next stage;
6. close formally, release resources, record follow-on actions, and evaluate
   the delivered result.

The business case is therefore a living control, not a document that merely
opens the project. Continued funding depends on whether the expected outcome
still justifies the remaining cost and risk.

### Operate technology as a service portfolio

Translate infrastructure and applications into services a user can request and
an owner can measure. Each service record should include:

| Control | Minimum evidence |
|---|---|
| Definition | user, supported activity, functional and non-functional promise |
| Request | entry point, required information, authorization, target response |
| Support | service owner, support route, escalation, operating hours |
| Incident | restore service, communicate status, record impact and resolution |
| Problem | investigate recurring causes and prevent recurrence |
| Change and release | approve, test, deploy, verify, and reverse safely |
| Service level | availability, response, recovery, capacity, and quality measures |
| Continuity | backup, recovery, dependency, and disaster-response evidence |
| Cost | acquisition plus operation, support, maintenance, security, and retirement |
| Improvement | review trend, user impact, benefit, and next corrective action |

An incident restores service; a problem investigation removes or controls the
cause. Treating those as the same activity creates repeat outages. Likewise, a
purchase price is not the system cost: the portfolio decision must include the
total cost of ownership across development or acquisition, operation, support,
maintenance, security, recovery, and decommissioning.

### Prove technical and work-system readiness

Implementation changes two coupled systems:

| Readiness | Evidence |
|---|---|
| Technical | hardware/service, software, integration, migrated data, security, capacity, recovery, and acceptance tests |
| Work system | roles, authority, procedures, staffing, training, documentation, support, controls, and stakeholder acceptance |

Choose conversion deliberately:

- **Direct:** old system stops as the new one starts; fastest, with concentrated
  failure and recovery risk.
- **Parallel:** both run for a bounded comparison period; stronger verification,
  with duplicate work and reconciliation cost.
- **Phased/hybrid:** components, locations, or user groups move in controlled
  increments; spreads risk but creates temporary interfaces and mixed-state
  complexity.

The conversion record must name cutover criteria, rollback conditions,
reconciliation ownership, the maximum mixed-state period, and who authorizes
completion.

### Fund maintenance as portfolio work

Classify post-delivery changes so maintenance capacity remains visible:

| Class | Purpose |
|---|---|
| Corrective | repair a previously unidentified defect |
| Adaptive | restore fit after an environmental, regulatory, dependency, or workflow change |
| Perfective | improve functionality, usability, performance, or service value |
| Preventive | improve maintainability, resilience, security, documentation, or future change safety |

Configuration management keeps requirements, designs, code/configuration,
tests, documentation, deployed versions, and environment state synchronized.
Every material change should identify the affected configuration, approval,
verification, deployment, rollback, and documentation update. A system without
an explicit maintenance owner and configuration record is not operationally
finished.

## Applied Audit Packet

For one bounded workflow, return:

1. actual process map;
2. information-class list and ownership;
3. process/information matrix;
4. current system/tool inventory;
5. fragmentation, duplication, inconsistency, and integration findings;
6. smallest future-state change;
7. named owner, proof, and evaluation moment.

The field evidence comes from [[workflow-observation-method|the Workflow
Observation Method]]. Material and information-flow structure can be extended
with [[value-stream-mapping-method-and-lean-guidelines|Value-Stream Mapping]].
Strategic selection remains governed by
[[strategic-diagnosis-and-coherent-action|Strategic Diagnosis and Coherent
Action]].

## Source and Limits

Primary source: Paul Beynon-Davies, *Business Information Systems*, 2nd ed.
(2013), Chapter 10 physical PDF pp. 361-373 (book pp. 322-334), Chapter 11
physical PDF pp. 374-403 (book pp. 335-364), and Chapter 12 physical PDF
pp. 404-435 (book pp. 365-396), reviewed 2026-07-27 from
`03-WIKIS/TECHNOLOGY/raw/Business Information Systems 2nd Ed. Textbook.pdf`.

Retained the process/information matrix, current/future system portfolio,
information/system/technology separation, durable plan-implement-support-
evaluate control pattern, six operating-ownership functions, product/stage
delivery controls, service-portfolio operating loop, dual readiness check,
conversion choices, maintenance classes, and configuration-control record.
COBIT, PRINCE2, ITIL, and ISO version details; package/vendor examples; method
histories; channel examples; organizational structures; industry history;
regulatory references; environmental statistics; and period-specific
technology details require current primary-source verification before
operational use.

## Related Pages

- [[information-system-evaluation-lifecycle-and-failure-levels|Information-System Evaluation Lifecycle and Failure Levels]]
- [[domain-driven-strategic-design-and-bounded-contexts|DDD Strategic Design and Bounded Contexts]]
- [[application-services|Application Services]]
- [[workflow-observation-method|Workflow Observation Method]]
- [[value-stream-mapping-method-and-lean-guidelines|Value-Stream Mapping]]
- [[strategic-diagnosis-and-coherent-action|Strategic Diagnosis and Coherent Action]]
