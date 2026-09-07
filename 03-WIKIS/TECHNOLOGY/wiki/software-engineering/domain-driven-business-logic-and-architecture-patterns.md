---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/ddd, subject/software-architecture]
source_role: primary
use_cases: [tech-stack]
---

# Domain-Driven Business Logic and Architecture Patterns

## Choose Complexity to Match the Domain

DDD does not prescribe one implementation pattern. It provides a progression;
the right choice is the least complicated pattern that preserves the business
rules and expected evolution.

| Pattern | Best fit | Main caution |
|---|---|---|
| Transaction script | Simple procedural operation with limited rules | Logic duplicates and tangles as rules interact |
| Active record | Simple rules centered on a data record and CRUD lifecycle | Persistence concerns dominate complex behavior |
| Domain model | Complex rules, invariants, state transitions, and interacting concepts | Requires disciplined boundaries and domain expertise |
| Event-sourced domain model | Complex temporal rules where complete state history and auditability are essential | Operational, modeling, migration, and tooling cost are high |

Do not use a domain model because the business matters; use it because the
business logic is complex. Supporting subdomains often need only transaction
scripts or active records. Core subdomains more often justify a domain model.

## Domain Model Building Blocks

- **Value object:** defined by its attributes rather than identity; should be immutable and validate its own values.
- **Entity:** has identity and continuity across state changes.
- **Aggregate:** consistency and transaction boundary around entities/value objects, accessed through one aggregate root.
- **Invariant:** business rule that must remain true after every operation.
- **Domain service:** domain logic that does not naturally belong to one entity or value object.
- **Domain event:** business-significant fact that already occurred.

Keep aggregates small. Only data inside an aggregate can be assumed strongly
consistent; coordination beyond it is normally eventually consistent. If a rule
must be atomic, that is evidence the boundary may be wrong.

## Architecture Patterns

### Layered architecture

Separates presentation, application/service orchestration, business logic, and
infrastructure. It works when dependency direction protects the domain rather
than letting database and UI concerns leak inward.

### Ports and adapters

Places application/domain logic behind ports and connects databases, APIs, UIs,
and tests through adapters. It is useful when external technology changes or
testability should not distort the business model.

### CQRS

Command-Query Responsibility Segregation uses different models for changing
state and reading it. It helps when the write model is optimized for enforcing
complex rules while users need multiple query projections. It is not required
for ordinary CRUD and adds synchronization and operational complexity.

Event sourcing and CQRS are distinct. Event sourcing stores state transitions;
CQRS separates read and write models. They can be combined but neither implies
the other.

## Selection Sequence

1. Classify the subdomain and its expected change.
2. List invariants, state transitions, concurrency needs, and history needs.
3. Start with transaction script or active record if rules are simple.
4. Move to a domain model when behavior and invariants outgrow record-centric code.
5. Add ports/adapters when external dependencies threaten the model or testing.
6. Add CQRS only when one model cannot serve both rule enforcement and queries cleanly.
7. Choose event sourcing only when temporal history is central enough to repay its cost.

## Evolution Rule

Design decisions should change when the business changes. A transaction script
can evolve into active record, then domain model, then event-sourced domain model;
the reverse simplification is also valid. Refactor around observed complexity,
not an imagined future architecture.

## Source Coverage

Primary source: `raw/LearningDomainDrivenDesign.pdf`, PDF pages 92-180
(Part II, Chapters 5-8), with evolution rules reinforced by pages 204-229
(Chapters 10-11). See [[learning-domain-driven-design|source hub]].

## Related Pages

- [[domain-driven-strategic-design-and-bounded-contexts|Strategic Design and Bounded Contexts]]
- [[reliable-programming-techniques|Reliable Programming Techniques]]
- [[../distributed-systems/transaction-isolation-levels-and-concurrency-control|Transaction Isolation and Concurrency Control]]
