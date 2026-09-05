---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/ddd, subject/integration, subject/messaging]
source_role: primary
use_cases: [tech-stack]
---

# Domain-Driven Integration and Reliable Messaging

## Integration Is a Business Contract

Contexts should exchange the minimum stable information needed for collaboration.
Do not expose internal domain objects or private event histories as public
contracts. Translate at boundaries when another context uses a different model.

## Communication Choices

| Need | Default pattern | Main tradeoff |
|---|---|---|
| Immediate answer or validation | Synchronous request/response | Runtime coupling and cascading failure risk |
| Notify that something happened | Asynchronous event | Delivery, ordering, duplication, and eventual consistency |
| Reliable state change plus publication | Transactional outbox | Extra relay/storage operations |
| Linear cross-context reaction with compensation | Saga | Harder failure reasoning; not atomic across contexts |
| Branching, stateful, long-running business process | Process manager | Central process state and lifecycle must be owned |

## Reliable Publication

Writing business state and publishing a message as unrelated operations creates
a dual-write failure: the database can commit while the message fails, or the
message can publish before the transaction rolls back. The outbox pattern writes
the state change and outbound message in one local transaction, then a relay
publishes the message. Consumers still need idempotency because delivery may be
at least once.

Assume:

- networks and servers fail;
- messages can be duplicated, delayed, or reordered;
- consumers retry;
- schemas and business meanings evolve;
- replay can produce unexpected load or side effects.

Include stable message identity, versioning, ordering information when needed,
deduplication, observable failure queues, and a recovery procedure.

## Saga Versus Process Manager

A saga maps events to commands across a relatively simple flow and may issue
compensating actions when later steps fail. Compensation is a business action,
not a database rollback.

A process manager owns the state and decision logic for a multi-step process. If
the coordinator contains branching rules and must remember where each instance
is, it is probably a process manager rather than a simple saga.

Do not use either pattern to hide an aggregate that was split incorrectly. Rules
requiring immediate strong consistency may belong inside one aggregate/context.

## Public Events Versus Internal Events

Event sourcing records fine-grained internal state transitions. Event-driven
architecture integrates components through public events. Internal domain events
can expose implementation details and create brittle consumers; publish a stable
event in the context's published language instead.

## Advisor-Builder Application

For SMB integration work, default to native integrations, simple APIs, or a
controlled automation platform. Pull these patterns only when a real multi-system
workflow needs reliable recovery or long-running coordination. A 40-step brittle
automation without ownership and failure handling is a distributed system even
if it was built in a visual tool.

Minimum integration design record:

```text
Producer and owner:
Consumer and owner:
Business event/command:
Contract and version:
Delivery guarantee:
Idempotency key:
Ordering requirement:
Retry and dead-letter behavior:
Compensation/recovery owner:
Monitoring signal:
```

## Source Coverage

Primary source: `raw/LearningDomainDrivenDesign.pdf`, PDF pages 181-203
(Chapter 9) and 294-312 (Chapter 15). See
[[learning-domain-driven-design|source hub]].

## Related Pages

- [[domain-driven-strategic-design-and-bounded-contexts|Strategic Design and Bounded Contexts]]
- [[../distributed-systems/asynchronous-messaging|Asynchronous Messaging]]
- [[../distributed-systems/scalable-event-driven-processing|Scalable Event-Driven Processing]]
- [[../devops/production-telemetry-and-monitoring-architecture|Production Telemetry and Monitoring]]
