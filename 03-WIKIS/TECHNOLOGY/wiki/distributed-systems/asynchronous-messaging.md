---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/messaging]
---

# Asynchronous Messaging

**Summary**: How message queues decouple producers from consumers for better responsiveness and independent scaling, the data-safety vs. performance and availability vs. performance trade-offs every messaging system forces, and three recurring patterns — competing consumers, exactly-once processing, and poison message handling — illustrated with RabbitMQ.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 7)

**Last updated**: 2026-06-17

---

## Why asynchronous messaging

Synchronous request/response (the default assumed everywhere else in the book) requires the client to wait for a result. Many operations don't need that — the book's analogy: returning a package at a shipping store doesn't require waiting in the store for the vendor's confirmation. **Producers send a message and move on ("fire and forget"); consumers retrieve and process it independently** (source: Foundations of Scalable Systems.pdf). This is the generalized, named version of the queueing pattern already introduced for "increasing responsiveness" in [[distributed-systems-architecture-patterns]].

Core vocabulary: **message queues** (FIFO stores), **producers** (send), **consumers** (retrieve — exactly one consumer gets each message from a plain queue), **message broker** (manages the queues). Consumers retrieve via **pull** (polling — wasteful, busy-waits) or **push** (broker invokes a callback when a message arrives — far more efficient, the recommended default) (source: Foundations of Scalable Systems.pdf).

## Persistence and publish-subscribe

- **Message persistence**: in-memory-only queues are fast but lose everything on a broker crash. **Persistent (durable) queues** write to disk before acknowledging a send — trading latency for **data safety**.
- **Publish-subscribe**: when a message needs to go to *multiple* interested parties (not just one consumer), the queue becomes a **topic**, and every active subscriber gets a copy. This decouples publishers from subscribers entirely — new subscribers can be added with zero changes to the publisher — and is the foundational pattern for event-driven architectures (revisited for microservices in [[microservices]] and for streaming systems later in the book).
- **Message replication**: brokers replicate queues/topics across a **leader-follower** cluster so a single broker failure doesn't take down the whole system — the follower is a hot standby that takes over (failover) transparently to clients.

## RabbitMQ as a concrete example

RabbitMQ routes messages through **exchanges** using a **routing key** and **bindings**: a **direct** exchange delivers by exact routing-key match, a **topic** exchange by pattern match (flexible pub-sub), a **fanout** exchange broadcasts to every bound queue regardless of routing key (source: Foundations of Scalable Systems.pdf). Practically: RabbitMQ connections are heavyweight (multi-round-trip to establish) so they're long-lived; lightweight **channels** multiplex over one connection but aren't thread-safe, so multithreaded clients need either a channel-per-thread model or a pooled channel pool (the same resource-pooling discipline as thread pools in [[concurrency-fundamentals]] and DB connection pools in [[application-services]]).

## Two unavoidable trade-offs

- **Data safety vs. performance**: guaranteed delivery requires publisher confirms (broker acknowledges receipt), persistent queues/messages (written to disk), and manual consumer acknowledgments (only removed from the queue once actually processed, not just delivered). Each adds latency. Get all three for a purchasing system where lost messages cost money; skip them for, say, a best-effort chat app where an occasional dropped message barely matters (source: Foundations of Scalable Systems.pdf).
- **Availability vs. performance**: broker replication (RabbitMQ's mirrored or quorum queues) protects against a single broker failure, but all publisher/consumer traffic still flows through one leader — replication buys availability, not extra throughput. Quorum queues use a **Raft**-based consensus algorithm for replication and leader election (Raft is covered in depth later in the book's distributed-database chapters).

## Three recurring messaging patterns

- **Competing consumers** — run multiple consumer instances against the same queue to scale out message processing horizontally. Push delivery round-robins fairly; pull delivery naturally load-balances itself (a consumer on more cores simply pulls and processes more). This pattern gives availability (a failed consumer's unacknowledged messages go to another), automatic failure handling, and dynamic scaling — directly the messaging-system version of horizontal scaling from [[application-services]].
- **Exactly-once processing** — duplicates can originate from either side: a publisher retrying after a lost acknowledgment, or a broker redelivering to a consumer that crashed before acknowledging. The fix mirrors [[distributed-systems-essentials]]'s idempotency-key pattern exactly: producers attach a unique ID per logical message so the broker can dedupe; consumers track which message IDs they've already processed.
- **Poison messages** — a message that can never be successfully processed (malformed payload, stale foreign-key reference) will otherwise be redelivered forever, consuming capacity and potentially crashing consumers repeatedly. The fix is a **redelivery limit**: after N failed attempts (commonly 3–5), the message is automatically routed to a **dead-letter queue** for manual diagnosis instead of looping indefinitely (source: Foundations of Scalable Systems.pdf).

## Connects to

- [[distributed-systems-architecture-patterns]] — the original "increasing responsiveness with queueing" example this chapter generalizes into a full pattern catalog.
- [[distributed-systems-essentials]] — idempotency keys, the direct ancestor of exactly-once message processing.
- [[concurrency-fundamentals]] / [[application-services]] — channel pooling and competing consumers both reuse the same bounded-resource-pool discipline as thread and connection pools.
- [[theory-of-constraints#The Five Focusing Steps|TOC Step 3 — Subordinate everything else]] — a queue is the purest implementation of "pace work to what the constrained resource can absorb": producers never have to wait for consumers, and consumers process at their own sustainable rate.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
