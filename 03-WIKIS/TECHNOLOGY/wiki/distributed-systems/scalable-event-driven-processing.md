---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/event-streaming]
---

# Scalable Event-Driven Processing (Apache Kafka)

**Summary**: How event-driven architectures differ from ordinary message queues by keeping a permanent, replayable log instead of destroying messages on consumption — and how Apache Kafka implements this at scale via topic partitioning, consumer groups, and leader-follower replication.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 14)

**Last updated**: 2026-06-17

---

## Events vs. ordinary messages

An **event** records that something happened (a package scan, a license expiring) and is published with no expectation of how — or whether — anything reacts to it; this is what gives event-driven architecture its loose coupling (source: Foundations of Scalable Systems.pdf). The structural difference from the queues covered in [[asynchronous-messaging]] is what happens *after* consumption:

- A traditional message broker (RabbitMQ, ActiveMQ) uses **destructive consumer semantics** — once read, the message is gone.
- Kafka treats the topic as an **append-only, immutable log** with nondestructive reads — consumers just track an offset/index into the log, and the broker keeps every event until a retention policy (time-based TTL, or **compacted topics** that keep only the latest value per key) removes it (source: Foundations of Scalable Systems.pdf).

This single design choice unlocks three capabilities that destructive queues can't offer: **new consumers can be added at any time and replay the entire history**, not just future events; **existing processing logic can be fixed or enhanced and rerun against the full log** to recompute results; and **a crashed service can rebuild its state by replaying the log from scratch**, the same role a database transaction log plays for crash recovery.

## Kafka's architecture: "dumb broker, smart clients"

The broker's job is narrow and fast: append events durably, manage partitioning/replication, and serve reads by offset. **Producers**, not the broker, decide which partition an event goes to — this keeps the broker simple and pushes intelligence to the edges (source: Foundations of Scalable Systems.pdf). Producers batch events locally (flushed by size or time threshold, `linger.ms`) before sending — fewer, larger network round trips, the same batching-for-throughput trade-off seen with HTTP payload compression in [[application-services]]. Delivery guarantees are tunable via `acks` (0 = fire-and-forget, can lose events; 1 = acknowledged once persisted, can duplicate on retry) and `enable.idempotence` (broker deduplicates — the same idempotency-key pattern from [[distributed-systems-essentials]] and [[asynchronous-messaging]], implemented natively).

## Scalability: topic partitioning

A topic is split into partitions distributed across brokers — producers write to, and consumers read from, different partitions in parallel, giving horizontal scalability for both sides. **Ordering is only guaranteed within a single partition**, not across the whole topic — events with the same key (e.g., the same `liftID`) always hash to the same partition and stay strictly ordered relative to each other, but there's no total order across different keys (source: Foundations of Scalable Systems.pdf). This is a real design constraint, not an implementation detail: applications have to be built around "ordered within a key, unordered across keys."

**Consumer groups** let multiple consumers split a topic's partitions between them (max one consumer per partition per group at a time) — fewer consumers than partitions means some consumers handle multiple partitions; more consumers than partitions means some sit idle. Adding/removing a consumer or partition triggers a **rebalance**, coordinated by a broker-side group coordinator and executed by an elected consumer-group leader, designed to reassign as few partitions as possible to minimize processing disruption.

## Availability: replication and ISR

Each partition replicates across N brokers in a leader-follower setup; producers/consumers only talk to the leader, and followers pull from it like consumers. The **in-sync replica (ISR) list** tracks which followers are actually caught up; only ISR members are eligible for leader election on failure. Setting `acks=all` plus a `min.insync.replicas` value lets you tune exactly how many replicas must confirm a write before it's acknowledged — the same explicit latency-vs-durability dial as the `W` parameter in [[eventual-consistency]] (source: Foundations of Scalable Systems.pdf).

## Connects to

- [[asynchronous-messaging]] — the destructive-queue model this chapter explicitly contrasts Kafka against; the data-safety/availability trade-offs (acks, replication) are the same shape, different mechanism.
- [[distributed-systems-essentials]] / [[eventual-consistency]] — idempotency keys and tunable write-durability dials reappear here as native Kafka configuration.
- [[microservices]] — event logs are the most common substrate for choreographed (peer-to-peer) microservice workflows, and for keeping duplicated data consistent across services without synchronous coupling.
- [[stream-processing-systems]] — Kafka topics are the most common data source feeding the stream processors covered next.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
