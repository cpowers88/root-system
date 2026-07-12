---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/consistency]
---

# Eventual Consistency

**Summary**: How databases that favor availability over strict consistency (the "AP" side of CAP) manage the resulting staleness — the inconsistency window, read-your-own-writes guarantees, tunable consistency via N/W/R, quorum reads/writes, anti-entropy replica repair, and the mechanisms (last-writer-wins, version vectors, CRDTs) for resolving conflicting concurrent updates without silently losing data.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 11)

**Last updated**: 2026-06-17

---

## The inconsistency window

When an update is applied to one replica and propagated asynchronously to others, there's a period — the **inconsistency window** — during which different replicas hold different values for the same object. Its duration grows with the number of replicas, network/operational issues, and geographic distance between replicas (source: Foundations of Scalable Systems.pdf). The book is blunt that you can't bound this window in advance — it's a fact of life for any asynchronously-replicated system, not a bug to be fixed.

**Read-your-own-writes (RYOWs)** is the specific, very visible failure mode this causes: a client updates an object, then immediately reads it back and sees the *old* value because the read hit a replica that hasn't caught up yet. The fix in leader-follower systems is simple — route a client's follow-up read to the leader (which always has the latest value) — but it requires the application or driver to know to do this (source: Foundations of Scalable Systems.pdf).

## Tunable consistency: N, W, R

Most eventually-consistent databases let you tune the consistency/performance trade-off per request using three parameters:

- **N** — total replicas.
- **W** — replicas that must confirm a write before it's acknowledged.
- **R** — replicas read from before returning a value.

`W = N` (wait for every replica) gives **immediate consistency** for that write — but slower writes, and the write fails entirely if any replica is unreachable. `W = 1` gives fast, available writes but an inconsistency window. The book is explicit that **immediate consistency (W=N) is not the same as strong consistency** — concurrent reads mid-update can still see different values until convergence (see [[strong-consistency]] for the actual stronger guarantee) (source: Foundations of Scalable Systems.pdf).

**Quorum reads/writes** (`W = R = (N/2)+1`) sit in the useful middle: because the set of replicas written to and the set read from must overlap by at least one node, a quorum read is guaranteed to see the latest quorum-confirmed write. The trade-off: both reads and writes fail outright if a quorum of nodes isn't reachable.

**Sloppy quorums + hinted handoff** (used in DynamoDB, Cassandra, Riak, Voldemort) relax this further for availability: if a write can't reach a quorum of *home* nodes, it's temporarily stashed on any reachable node and handed off to the correct home node once it recovers. This increases write availability but means a quorum read can still occasionally see a stale value, because the read's R nodes may not include the one currently holding the handoff (source: Foundations of Scalable Systems.pdf).

## Replica repair (anti-entropy)

Distributed replicas drift apart over time from network failures, crashes, or bugs — a process the book likens to thermodynamic entropy. Two repair strategies:

- **Active (read) repair** — triggered on read: the coordinator compares replica values (often via cheap hash comparison, a "digest read") and pushes the latest value to any stale replica it notices.
- **Passive repair** — a background process using a **Merkle tree** (a hash tree where each parent node hashes its children) to efficiently compare entire collections between replicas without transferring all the data — only mismatched branches need to be walked down to find the actually-stale objects (source: Foundations of Scalable Systems.pdf). This runs during low load specifically because building Merkle trees is CPU/memory intensive.

## Resolving concurrent write conflicts

In a leaderless system, two clients can update the same key on different replicas at the same time. Someone has to decide the final value:

- **Last writer wins (LWW)** — use timestamps, keep the latest. Simple, but **silently loses updates** — and since clocks drift across machines (see [[distributed-systems-essentials]]), "latest" is often not even meaningfully true. The book's mitigation: only safe to rely on LWW if every write creates a new immutable object with a unique key, never mutates in place.
- **Version vectors** — each object carries a version per replica. A write must present the version it read; if it doesn't match the current version, that's a detected conflict (not a silent loss) — the database can store both conflicting versions as "siblings" and push resolution to the client (e.g., Riak), or reject the write and force a re-read. This is built on **logical clocks** (Lamport's happens-before relation) rather than physical timestamps, since logical clocks can correctly distinguish "definitely earlier," "definitely later," and "genuinely concurrent — no valid order exists" (source: Foundations of Scalable Systems.pdf).
- **CRDTs (conflict-free replicated data types)** — data structures (counters, sets, maps, lists) specifically designed so that concurrent updates from any replica, applied in any order, **always converge to the same final value** — no application-level conflict handling needed at all. Supported by Redis, Cosmos DB, and Riak among others.

## Connects to

- [[scalable-database-fundamentals]] — the CAP/AP trade-off this entire chapter is the practical implementation of.
- [[strong-consistency]] — the alternative (CP) approach this chapter's techniques are explicitly *not* providing; immediate consistency (W=N) is a deliberately weaker guarantee than what's covered there.
- [[distributed-systems-essentials]] — clock drift (why LWW is unreliable) and the Two Generals' Problem / consensus impossibility this chapter's mechanisms are working around in practice.
- [[theory-of-constraints#The Five Focusing Steps|TOC Step 3 — Subordinate everything else]] — tunable consistency (N/W/R) is a literal dial for trading latency against guarantees per use case, exactly the kind of deliberate, conscious trade-off the Five Focusing Steps ask you to make rather than defaulting to one extreme everywhere.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
