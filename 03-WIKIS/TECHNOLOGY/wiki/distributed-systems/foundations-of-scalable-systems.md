---
domain: tech
type: reference
tags: [subject/distributed-systems]
timeline: later
status: wiki-only
---

# Foundations of Scalable Systems (Ian Gorton)

**Summary**: Source tracker for Ian Gorton's *Foundations of Scalable Systems: Designing Distributed Architectures* (O'Reilly, 2022) — a technical reference on distributed systems architecture: scalability principles, services, caching, messaging, serverless, microservices, distributed databases, and event/stream processing.

**Sources**: Foundations of Scalable Systems.pdf

**Last updated**: 2026-06-17

---

## About this source

340 pages, 16 chapters across 4 parts. Unlike *The Goal* (narrative) or *Python Crash Course* (tutorial), this is a dense technical reference closer to a graduate course — concepts are explained directly with diagrams, real benchmark data, and short code examples (mostly Java) rather than discovered through a story. Ingestion here tracks closely to chapters, similar to how the Django material was split.

## Structure and ingestion status

| Part | Chapters | Topic | Status |
|---|---|---|---|
| I. The Basics | 1–4 | Scalability principles, distributed systems essentials, concurrency | **Ingested** — see [[scalability-fundamentals]], [[distributed-systems-architecture-patterns]], [[distributed-systems-essentials]], [[concurrency-fundamentals]] |
| II. Scalable Systems | 5–9 | Application services, caching, messaging, serverless, microservices | **Ingested** — see [[application-services]], [[distributed-caching]], [[asynchronous-messaging]], [[serverless-processing]], [[microservices]] |
| III. Scalable Distributed Databases | 10–13 | Relational/NoSQL scaling, CAP theorem, consistency models, Redis/MongoDB/DynamoDB | **Ingested** — see [[scalable-database-fundamentals]], [[eventual-consistency]], [[strong-consistency]], [[distributed-database-implementations]] |
| IV. Event and Stream Processing | 14–16 | Kafka, stream processing (Flink), production concerns (automation, observability) | **Ingested** — see [[scalable-event-driven-processing]], [[stream-processing-systems]], [[final-tips-for-success]] |

**Book complete.** All 16 chapters across all 4 parts have been ingested.

## Connects to

- [[scalability-fundamentals]], [[distributed-systems-architecture-patterns]], [[distributed-systems-essentials]], [[concurrency-fundamentals]] — Part I pages.
- [[application-services]], [[distributed-caching]], [[asynchronous-messaging]], [[serverless-processing]], [[microservices]] — Part II pages.
- [[scalable-database-fundamentals]], [[eventual-consistency]], [[strong-consistency]], [[distributed-database-implementations]] — Part III pages.
- [[scalable-event-driven-processing]], [[stream-processing-systems]], [[final-tips-for-success]] — Part IV pages.
- [[theory-of-constraints]] — this book is, in large part, Theory of Constraints applied to software systems: load balancers and caches are literal exploit/elevate mechanisms for a system's constrained resource. Each Part I page cross-links the specific TOC connection.
- [[django-deployment]] — this book picks up architecturally where a single Platform.sh deployment leaves off: scaling beyond one server.
