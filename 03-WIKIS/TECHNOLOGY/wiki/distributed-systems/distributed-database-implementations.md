---
domain: tech
type: concept
tags: [subject/distributed-databases]
timeline: later
status: wiki-only
---

# Distributed Database Implementations: Redis, MongoDB, DynamoDB

**Summary**: How three widely-deployed distributed databases apply the concepts from the rest of Part III in practice — each making different, deliberate trade-offs on the performance/consistency/availability spectrum despite superficially similar architectures.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 13)

**Last updated**: 2026-06-17

---

## The chapter's core warning

"All databases are scalable, but some are more scalable than others." Marketing claims about scalability and consistency need verification against the actual implementation details — superficially similar databases can behave very differently under the same workload, and the only way to know is to dig into specifics (or, as the book repeatedly points out, check the [Jepsen](https://jepsen.io) consistency-testing reports) (source: Foundations of Scalable Systems.pdf).

## Redis: performance over safety

A key-value, in-memory data structure store (strings, lists, sets/sorted sets, hashes), single-threaded by design for simplicity and to avoid locking overhead. Durability is opt-in and explicitly a performance trade-off: periodic disk snapshots, an append-only command log (written by default every second — meaning up to a second of writes can be lost on crash), or both for maximum safety at a real throughput cost (source: Foundations of Scalable Systems.pdf).

- **Scaling**: Redis Cluster shards across up to 1,000 nodes using 16,384 fixed hash slots; a notable constraint is that **multi-key transactions only work if all keys hash to the same slot** — a real data-modeling limitation, not a tuning knob.
- **Consistency**: eventually consistent by default (async replication to replicas); an optional `WAIT N timeout` command can force the primary to wait for N replica acknowledgments, trading latency for safety per-request.
- **Bottom line**: excellent throughput if your data model fits Redis's limited structures and you can tolerate occasional data loss — not a recommended system-of-record if data loss is unacceptable.

## MongoDB: developer ergonomics, matured into a real distributed platform

A document database (JSON/BSON) that eliminates the object-relational mapping layer entirely — store your business objects close to how your application already represents them. Schemaless (schema-on-read) by default, with single-document writes always atomic — which is why heavy denormalization into nested documents was, for years, the *only* practical way to get transaction-like guarantees, before native multi-document ACID transactions arrived in v4.0 (source: Foundations of Scalable Systems.pdf).

- **Scaling**: sharding (hash- or range-based) plus a stateless `mongos` query router layer that clients always talk through; an automatic cluster balancer redistributes "chunks" (64MB units) to avoid hotspots as data grows unevenly.
- **Consistency**: tunable via **write concerns** (e.g., `majority` — wait for quorum durability) and **read preferences** (route reads to primary for consistency, or to the nearest/any replica for lower latency at the cost of staleness) — the same N/W/R-style dial as [[eventual-consistency]], just under different names.
- **Bottom line**: the most flexible of the three for general-purpose application development; performance and safety are both genuinely tunable per use case rather than fixed architectural choices.

## DynamoDB: fully managed, pay-per-operation

A managed AWS key-value/document store descended directly from the original Dynamo paper (the same paper that originated sloppy quorums and hinted handoff, covered in [[eventual-consistency]]). The defining trait is **operational simplicity in exchange for cost structure complexity** — you pay per GB stored *and* per read/write operation, with two capacity modes (on-demand for spiky/unpredictable load, provisioned for predictable load with autoscaling between configured limits) (source: Foundations of Scalable Systems.pdf).

- **Scaling**: automatic partition rebalancing ("adaptive capacity") — but a well-known failure mode is **hot keys**: since provisioned capacity is divided per-table across partitions, a small number of disproportionately-accessed keys can exhaust their partition's slice of capacity even while the table overall has spare capacity elsewhere.
- **Consistency**: eventually consistent reads by default; an explicit `ConsistentRead: true` flag forces a leader read (at higher cost). **Global tables** (multi-region replication) are multi-leader, meaning concurrent writes in different regions can conflict — resolved via last-writer-wins, with the same silent-data-loss risk flagged in [[eventual-consistency]]. Both strongly-consistent reads and ACID transactions are explicitly **scoped to a single region** — global tables don't extend those guarantees globally.
- **Bottom line**: the right choice when you're already deep in the AWS ecosystem and want to trade direct infrastructure control for managed operations — but the hot-key and region-scoped-consistency caveats are easy to miss until they bite in production.

## The general lesson

All three databases implement the *same* underlying concepts from [[scalable-database-fundamentals]], [[eventual-consistency]], and [[strong-consistency]] — sharding, replication, tunable consistency, conflict resolution — but make genuinely different default choices and expose different knobs. **Evaluating a database for a specific use case means understanding which knobs exist and what they actually cost**, not trusting a vendor's "scalable and consistent" marketing copy at face value. The book's recommended practice — a proof-of-technology prototype under realistic load before committing — is the database-specific instance of the same measure-don't-assume discipline that ran through [[scalability-fundamentals]] and [[serverless-processing]].

## Connects to

- [[scalable-database-fundamentals]] — the data models and sharding strategies all three databases implement concretely.
- [[eventual-consistency]] — tunable consistency (write concerns, `ConsistentRead`, `WAIT`), sloppy quorums, and last-writer-wins all show up here as real product features, not just theory.
- [[strong-consistency]] — MongoDB and DynamoDB's ACID transaction support both use 2PC under the hood, exactly as described there.
- [[foundations-of-scalable-systems]] — source tracker for the whole book; this closes out Part III.
- think-python-debugging-and-algorithm-analysis — the LinearMap→BetterMap→HashMap build-up there (bucket by hash, resize and rehash as load grows) is the single-machine version of the same hash-based sharding logic these databases use to distribute across many nodes.
