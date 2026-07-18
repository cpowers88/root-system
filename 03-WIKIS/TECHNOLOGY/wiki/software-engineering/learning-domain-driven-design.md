---
domain: technology
type: source-summary
timeline: reference
status: wiki-only
tags: [domain/technology, source-role/primary, use-case/tech-stack, subject/ddd, subject/software-engineering]
---

# Learning Domain-Driven Design - Source Summary and Navigation Hub

**Source:** `raw/LearningDomainDrivenDesign.pdf`, Vlad Khononov, *Learning
Domain-Driven Design* (446 PDF pages).

## Why It Matters

Domain-driven design connects software structure to business strategy. It is
most useful when business rules, terminology, ownership, and change are complex;
it is not a reason to install microservices or elaborate patterns in a simple
application. For Chris, its immediate value is better workflow discovery and a
shared business language. Its advanced implementation patterns remain lookup
material until a real build needs them.

## Retrieval Map

- [[domain-driven-strategic-design-and-bounded-contexts|Strategic Design and Bounded Contexts]] - business domains, subdomain investment, ubiquitous language, boundaries, and context maps.
- [[domain-driven-business-logic-and-architecture-patterns|Business Logic and Architecture Patterns]] - transaction script through event sourcing, layered architecture, ports and adapters, and CQRS.
- [[domain-driven-integration-and-reliable-messaging|Integration and Reliable Messaging]] - sync/async integration, outbox, saga, process manager, and event contracts.
- [[domain-driven-evolution-eventstorming-and-distributed-boundaries|Evolution, EventStorming, and Distributed Boundaries]] - heuristics, design evolution, workshops, brownfield adoption, microservices, event-driven design, and data mesh.

## Complete Chunk Ledger

The PDF has a nonstandard tagged text layer that emits Chapter 2 before the
front matter during whole-file extraction. Physical/rendered page checks were
used for the ledger; Chapter 2 was recovered from that tagged section and placed
with Part I rather than treated as a separate or missing source.

| PDF range | Book content | Disposition |
|---|---|---|
| 1-38 | Cover, publication material, foreword, preface, navigation, introduction; tagged Chapter 2 text | Front matter summarized here; Chapter 2 ingested with strategic design |
| 39-91 | Part I, Chapters 1-4: domains, ubiquitous language, bounded contexts, context maps | Ingested into strategic-design page |
| 92-203 | Part II, Chapters 5-9: business-logic, architecture, and communication patterns | Ingested into business-logic and integration pages |
| 204-269 | Part III, Chapters 10-13: heuristics, evolving design, EventStorming, brownfield DDD | Ingested into evolution/workshops page |
| 270-380 | Part IV, Chapters 14-16; conclusion and applied case study | Microservices, event-driven architecture, data mesh, and case lessons ingested into evolution/integration pages |
| 381-446 | References and index | Reviewed for source closure; lookup only |

## Use Gate

Use the strategic page during discovery and software scoping. Pull tactical or
distributed patterns only after the business model and consistency requirements
are known. Prefer the simplest pattern that implements the actual rules.

## Related Pages

- [[personas-scenarios-and-user-stories|Personas, Scenarios, and User Stories]]
- [[reliable-programming-techniques|Reliable Programming Techniques]]
- [[../distributed-systems/microservices|Microservices]]
- [[../distributed-systems/asynchronous-messaging|Asynchronous Messaging]]
