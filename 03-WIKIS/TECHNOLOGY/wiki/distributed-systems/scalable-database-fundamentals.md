---
domain: tech
type: concept
tags: [subject/distributed-databases]
timeline: later
status: wiki-only
---

# Scalable Database Fundamentals

**Summary**: How relational databases scale (up, then via read replicas, then via partitioning) and where that approach strains; why NoSQL emerged with simpler, denormalized "model the queries, not the domain" data models; the four NoSQL data model families; sharding strategies; leader-follower vs. leaderless replication; and the CAP theorem as the master trade-off underlying everything in distributed databases.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 10)

**Last updated**: 2026-06-17

---

## Scaling relational databases

Three escalating strategies, each solving the limits of the one before:

1. **Scale up** — bigger single machine. No application changes, but cost grows faster than capacity, you still have one node (a single point of failure), and eventually you hit a ceiling.
2. **Scale out: read replicas** — a primary handles writes; one or more secondaries hold asynchronously-replicated copies and serve reads. Excellent for read-heavy workloads, and reads survive a primary outage. The cost: secondaries lag behind the primary by some replication delay, creating a window where reads can return **stale data** (source: Foundations of Scalable Systems.pdf).
3. **Scale out: partitioning (sharding)** — split a table across multiple nodes, either **horizontally** (rows distributed by a partitioning strategy, e.g. region) or **vertically** (columns split, e.g. static vs. dynamic fields). This is where relational databases start fighting their own design: **SQL joins across partitions require shuffling data between nodes**, which is expensive and hard to optimize automatically — the strategies that help (replicate small reference tables everywhere; join on the partition key; filter aggressively before joining) all amount to deliberately avoiding the general case (source: Foundations of Scalable Systems.pdf).

**Oracle RAC** is cited as the high-end "shared-everything" answer — multiple database engines clustered against one shared storage array (a SAN), giving horizontal compute scaling without the partitioning/join problem, at the cost of expensive specialized hardware and the SAN itself becoming a potential bottleneck.

## Why NoSQL emerged

A confluence of cheap commodity hardware, unstructured/rapidly-evolving data, and the need for internet-scale availability made the "one-size-fits-all" relational model a poor fit for many new use cases (source: Foundations of Scalable Systems.pdf). The core NoSQL characteristics: simplified, easily-evolved data models; proprietary query languages with little or no join support; and native horizontal scaling on commodity hardware.

**The fundamental modeling shift**: relational design normalizes around the *problem domain* (one canonical entry per fact, joined as needed) — NoSQL design denormalizes around the *solution domain*, i.e., the actual access patterns the application needs. In practice this means **a table per use case**, with data deliberately duplicated across tables so a single query never needs a join. The book's example: instead of normalized `SnowSportPerson`/`Resort`/`Visit`/`Weather` tables joined at query time, you create one `VisitDay` object that already contains everything a "show my visit history" query needs. The trade-off: **reads get faster, writes get more complex** (updating a resort's name now means updating every duplicated copy), and you take on responsibility for keeping duplicates consistent.

## Four NoSQL data model families

- **Key-value** (Redis, Oracle NoSQL) — a hash map; the value is opaque to the database.
- **Document** (MongoDB, Couchbase) — value is structured (typically JSON), so individual fields can be indexed and queried.
- **Wide column** (Cassandra, Bigtable) — a two-dimensional hash map; rows in the same collection can have different columns.
- **Graph** (Neo4j, Amazon Neptune) — relationships are first-class, enabling traversal algorithms; conceptually closest to relational, and notably **harder to shard** than the other three because partitioning a graph without constantly crossing node boundaries for traversals is a genuinely unsolved general problem (source: Foundations of Scalable Systems.pdf).

All four are typically **schemaless** (schema-on-read) — no upfront format definition, which eases evolution but pushes structure-discovery responsibility onto the application.

## Sharding mechanics

A **shard/partition key** determines which node owns a given object. Three approaches: **hash-based** (even distribution, but can't easily query ranges), **value-based** (e.g., shard by country — keeps related data together but risks uneven "hot" partitions), **range-based** (e.g., by zip code range — supports range queries but also risks hotspots) (source: Foundations of Scalable Systems.pdf). Sharding solves capacity but reintroduces the availability problem from single-node databases at the partition level — solved the same way as everywhere else in this book: **replication**.

## Replication architectures

- **Leader-follower** — one replica is authoritative for writes; followers are read-only and can be load-balanced for read scaling.
- **Leaderless** — any replica can accept a write and becomes the coordinator for propagating it; generally more write-scalable, at the cost of needing conflict resolution when two replicas are written to concurrently (the subject of [[eventual-consistency]]).

## The CAP theorem

Eric Brewer's CAP theorem is the single sentence that explains *why* every distributed database design in this Part makes the trade-offs it does: **when a network partition occurs, a database can guarantee either consistency (CP) or availability (AP), not both** (source: Foundations of Scalable Systems.pdf). If replicas of an updated object are split across both sides of a partition, the database must either refuse the update (consistency, at the cost of availability) or apply it to whichever side is reachable (availability, at the cost of temporary inconsistency). Note this isn't an everyday operational choice — it's specifically what happens *during* a partition; most of the time, with no partition, a system can be both. The CP/AP label is a useful shorthand but, as later chapters show, most real databases let you tune this per-request rather than picking one mode globally.

## Connects to

- [[eventual-consistency]] — what happens on the "available" (AP) side of the CAP trade-off: how systems that accept inconsistency manage and eventually resolve it.
- [[strong-consistency]] — what happens on the "consistent" (CP) side: the consensus algorithms that make strict consistency possible despite partitions.
- [[distributed-database-implementations]] — concrete products (Redis, MongoDB, DynamoDB) built on these data models and replication strategies.
- [[theory-of-constraints]] — CAP is itself a constraint statement: you cannot simultaneously maximize consistency and availability under partition, so a system design has to explicitly choose which one to subordinate to the other for a given use case.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
- think-python-iteration-strings-wordplay — "debugging by bisection" (halve the search space, check the midpoint, repeat) is the same logarithmic-search logic underneath sharding and ordered-index lookups, just applied to finding a bug in a line range instead of a record in a dataset.
- think-python-debugging-and-algorithm-analysis — Big-O's worst-case/order-of-growth framing is the formal vocabulary behind this page's "some databases are more scalable than others" warning; both insist on judging a design by how it degrades at large scale, not by small-scale behavior.
