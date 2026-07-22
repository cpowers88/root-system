---
domain: tech
type: concept
tags: [subject/consistency]
timeline: later
status: wiki-only
---

# Strong Consistency

**Summary**: The "CP" side of CAP — how distributed databases deliver single-machine-like consistency guarantees (serializability + linearizability) despite being partitioned and replicated, via two-phase commit for distributed transactions and consensus algorithms (Raft, Paxos) for replica agreement, illustrated with VoltDB and Google Cloud Spanner.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 12)

**Last updated**: 2026-06-17

---

## Why bother with strong consistency

Eventually consistent systems ([[eventual-consistency]]) push real complexity onto application code — handling stale reads, resolving conflicts, reasoning about an inconsistency window. Strongly consistent databases trade some performance/availability headroom to **eliminate that complexity entirely**: once an update is confirmed, every subsequent read by every client sees it, and concurrent updates behave as if strictly ordered (source: Foundations of Scalable Systems.pdf). Google's own framing of this trade-off (from the Spanner paper) is worth keeping as a design heuristic: it's better for engineers to deal with performance problems from *overusing* transactions than to constantly code around the absence of them.

Two distinct things both get called "strong consistency," worth keeping separate:

- **Transactional consistency (serializability)** — the "C" in ACID: concurrent transactions behave as if executed in some sequential order.
- **Replica consistency (linearizability)** — all clients see the most recent write to a single object, ordered by real (wall-clock) time.

**Strong consistency** in this chapter means both combined — the strongest practically achievable guarantee.

## Distributed transactions and two-phase commit

A transaction spanning multiple partitions/nodes needs every participant to agree on commit-or-abort. **Two-phase commit (2PC)**: a coordinator drives a **prepare phase** (every participant locks its data and confirms it *can* commit) then a **resolve phase** (if all said yes, commit; if any said no or didn't answer, abort everyone) (source: Foundations of Scalable Systems.pdf).

2PC's critical weakness: **coordinator failure**. If the coordinator dies after participants have voted to commit but before they're told the outcome, those participants must **block indefinitely**, holding locks, until the coordinator recovers and checks its transaction log. This is a direct availability cost — and under load, exactly the kind of blocked-thread situation that triggers the cascading failures described in [[microservices]].

## Distributed consensus: Raft

The fix for 2PC's single-coordinator fragility is replicating the coordinator role itself via a **consensus algorithm** — Raft is the book's worked example, chosen explicitly for being simpler to reason about than Paxos:

- One node is **leader**; it accepts all writes, assigns them an order, and replicates them to **followers** via periodic `AppendEntries` messages (which double as heartbeats).
- An update is **committed** once a **majority** of nodes (a quorum) have durably logged it — not all of them, which is what lets the system tolerate a minority of slow/unreachable followers.
- **Leader election**: each follower runs a randomized election timer; if it expires without a heartbeat, that follower becomes a candidate, increments a **term** counter, and requests votes. A candidate only wins with a majority, and critically, **a follower won't vote for a candidate whose log is behind its own** — this guarantees the new leader has every previously-committed entry (source: Foundations of Scalable Systems.pdf).

This is 2PC's coordinator-failure problem, solved generally: if a leader dies, a new one is elected from whichever followers have the most up-to-date log, and the system keeps making progress as long as a quorum is alive.

## Two real implementations, two different strategies

- **VoltDB** — each table partition is bound to a single CPU core running requests strictly single-threaded, which sidesteps locking entirely for single-partition transactions (no concurrent access to interleave = no isolation problem to solve). Multi-partition transactions fall back to 2PC across cores, at higher cost. Being in-memory, it layers command logging + periodic snapshots for durability — a real-time trade-off between data-loss-window size and write throughput (source: Foundations of Scalable Systems.pdf).
- **Google Cloud Spanner** — globally distributed, using Paxos for replica consensus within each shard and 2PC (riding on top of Paxos-replicated coordinators, so coordinator failure no longer blocks) across shards. Its standout innovation is **TrueTime**: GPS- and atomic-clock-synchronized clocks across Google's data centers with a known, bounded clock skew (~7ms). Spanner uses this bound to implement a **commit-wait** period — holding a transaction's locks an extra few milliseconds past its commit timestamp specifically so no other transaction can possibly commit with an *earlier* wall-clock-ordered timestamp that contradicts it (source: Foundations of Scalable Systems.pdf). This is what makes Spanner's consistency genuinely tied to real elapsed time, not just logical ordering — and explains why open-source Spanner-inspired databases (CockroachDB, YugabyteDB) that lack custom atomic-clock hardware necessarily offer weaker guarantees.

## Connects to

- [[eventual-consistency]] — the alternative (AP) approach this chapter's mechanisms trade availability/performance to avoid.
- [[scalable-database-fundamentals]] — the CAP theorem framing that explains why this entire chapter exists as a *choice*, not a universal best practice.
- [[distributed-systems-essentials]] — the Two Generals' Problem and FLP impossibility theorem this chapter's consensus algorithms are the practical, bounded-time answer to; also the clock-drift problem TrueTime specifically engineers around.
- [[microservices]] — 2PC's coordinator-blocking failure mode is the database-level version of the cascading-failure problem solved at the service level by circuit breakers and timeouts.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
