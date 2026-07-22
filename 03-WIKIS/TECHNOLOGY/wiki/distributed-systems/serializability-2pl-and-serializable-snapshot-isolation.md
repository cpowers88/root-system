---
domain: tech
type: concept
tags: [subject/transactions]
timeline: later
status: wiki-only
---

# Serializability: Actual Serial Execution, Two-Phase Locking, and SSI

**Summary**: The three real techniques databases use to deliver true
serializable isolation — the only isolation level that automatically
prevents every race condition covered in [[transaction-isolation-levels-and-concurrency-control]]
(dirty reads/writes, lost updates, write skew, phantoms) — and why each
one trades away something (throughput, latency predictability, or
retry overhead under contention) to get there.

**Sources**: designingDataIntensiveApplications.pdf (Kleppmann, *Designing
Data-Intensive Applications*, O'Reilly 2017), Chapter 7, "Serializability"
(pp. 251–266)

**Last updated**: 2026-07-13

---

## Why this is a separate page from weak isolation levels

Every isolation level covered in [[transaction-isolation-levels-and-concurrency-control]]
is a *deliberate* compromise — it prevents some race conditions and not
others, and it's genuinely hard to know from application code alone which
race conditions a given piece of code is actually vulnerable to. Since the
1970s, the research answer has been consistent: **use serializable
isolation** — it guarantees the result is as if transactions ran one at a
time, full stop, no exceptions to track. The open question has always been
performance, not correctness (source: designingDataIntensiveApplications.pdf).

## 1. Actual Serial Execution

The most literal fix: remove concurrency entirely, run one transaction at
a time on a single thread. By definition this is serializable — there's
no interleaving to reason about. Counterintuitively this only became
practical around 2007, for two reasons: RAM got cheap enough to hold
entire active datasets in memory (removing disk-wait time from the
critical path), and database designers noticed that OLTP transactions are
usually short with few reads/writes — long analytic queries can run
separately under snapshot isolation instead. Used in VoltDB/H-Store,
Redis, and Datomic (source: designingDataIntensiveApplications.pdf).

**The catch**: interactive, multi-round-trip transactions (query, wait for
app logic, query again) would make single-threaded execution painfully
slow — the database would spend most of its time idle, waiting on network
round-trips. The fix is **stored procedures**: the entire transaction is
submitted to the database ahead of time as one unit, so it can execute at
memory speed with zero network waiting in the middle. Modern
implementations use real languages (VoltDB: Java/Groovy; Datomic:
Java/Clojure; Redis: Lua) rather than the old vendor-specific stored-procedure
languages (PL/SQL, T-SQL) that gave stored procedures their bad reputation.

**Scaling limit**: throughput is capped at one CPU core unless the dataset
partitions cleanly, with each transaction touching only one partition.
VoltDB reports ~1,000 cross-partition writes/second — orders of magnitude
below single-partition throughput, and that ceiling doesn't rise by adding
machines. Whether this approach fits a given application depends heavily
on whether its data actually partitions cleanly (simple key-value: usually
yes; heavy secondary-index use: usually no).

## 2. Two-Phase Locking (2PL)

For roughly 30 years, the only widely used serializability mechanism.
**Not the same thing as two-phase commit (2PC)** despite the similar
name — 2PC is a distributed-transaction coordination protocol (see
[[strong-consistency]]), 2PL is a single-node concurrency-control scheme.

The core rule, stronger than read-committed's write-only locking: readers
block writers *and* writers block readers, in both directions. If
transaction A has read an object, transaction B can't write it until A
finishes; if A has written an object, B can't even read it until A
finishes. This directly contradicts snapshot isolation's mantra ("readers
never block writers, writers never block readers") — that's the single
clearest way to remember which mechanism you're dealing with (source:
designingDataIntensiveApplications.pdf).

Mechanically: a shared/exclusive lock per object. Shared locks stack (many
concurrent readers); an exclusive lock blocks everyone else entirely. "Two-phase"
refers to lock *lifetime*: phase one acquires locks as the transaction
runs, phase two releases them all at commit/abort — never before. This
inevitably produces **deadlocks** (A waiting on a lock B holds while B
waits on a lock A holds); the database detects these and aborts one side
for retry.

**The performance cost, and why it's real**: unlike weak isolation levels,
2PL has no bound on how long a transaction might wait, since traditional
databases don't limit transaction duration. One slow or lock-heavy
transaction can stall a whole queue of others — 2PL databases are known
for unstable, high-percentile-latency behavior under contention, which is
a genuine operability problem, not just a benchmark number.

**Predicate locks and the phantom problem**: ordinary object locks can't
prevent phantoms (a write that changes what a *future* search query would
return), because there's no existing row to attach a lock to. The
conceptual fix is a **predicate lock** — a lock on "all objects matching
this condition," including ones that don't exist yet. These don't perform
well in practice (checking every active predicate lock against every write
is expensive), so real 2PL databases use **index-range locks** instead — a
deliberately coarser approximation (e.g., lock the whole `room_id = 123`
index range rather than the precise time-window predicate) that trades
some unnecessary lock contention for much lower checking overhead. If no
suitable index exists, the fallback is a lock on the entire table — safe,
but bad for concurrency.

## 3. Serializable Snapshot Isolation (SSI)

First described in 2008, and the newest of the three — PostgreSQL's
`serializable` level since 9.1, and FoundationDB uses a similar algorithm.
The pitch: full serializability with only a small performance penalty over
plain snapshot isolation, potentially resolving the "correct vs. fast"
trade-off the other two techniques force (source:
designingDataIntensiveApplications.pdf).

**Pessimistic vs. optimistic, the framing that explains why SSI is
different**: 2PL is *pessimistic* — assume conflicts will happen and block
proactively (like mutex-based multi-threaded programming). Serial
execution is pessimistic to the extreme — one giant lock on everything.
SSI is *optimistic* — let transactions run freely against a consistent
snapshot, and only check for conflicts at commit time; if isolation was
actually violated, abort and retry. Optimistic concurrency control
performs *worse* than pessimistic under high contention (heavy retry
overhead can make an already-loaded system worse), but *better* when spare
capacity exists and contention is low — this is a genuine workload-dependent
trade-off, not a strict improvement.

**The core mechanism**: SSI builds on ordinary snapshot isolation (see
[[transaction-isolation-levels-and-concurrency-control]]) and adds conflict
detection for the exact "decision based on an outdated premise" pattern
that causes write skew — a transaction reads some fact, decides to act on
it, and by commit time that fact may no longer hold. Rather than blocking
proactively like 2PL, SSI tracks these premise-dependencies and aborts (at
commit) any transaction whose premise turned out to have been invalidated
by a concurrent write.

## Choosing among the three — no universal answer

| Technique | Best fit | Cost |
|---|---|---|
| Actual serial execution | Small, fast transactions; dataset fits in memory; partitions cleanly | Hard cap at one core per partition; cross-partition transactions are drastically slower |
| Two-phase locking (2PL) | Mature, widely available (MySQL/InnoDB, SQL Server); needed where SSI/serial aren't options | Unstable tail latency under contention; deadlocks require retry logic |
| Serializable Snapshot Isolation (SSI) | Low-to-moderate contention workloads wanting full correctness without 2PL's blocking cost | Newer, still proving itself in practice; retry storms possible under high contention |

The unifying lesson, consistent with [[transaction-isolation-levels-and-concurrency-control]]'s
closing point: there is no free lunch between "prevents every race
condition" and "fast under all workloads." The right choice depends on
actual contention levels and transaction shape, which is exactly the kind
of thing that needs measuring under realistic load rather than assumed —
the same discipline [[distributed-database-implementations]] already
recommends for choosing a database generally.

## Connects to

- [[transaction-isolation-levels-and-concurrency-control]] — the race
  conditions (dirty reads/writes, lost updates, write skew, phantoms) this
  page's three techniques exist to eliminate entirely.
- [[strong-consistency]] — 2PC (distributed atomic commit) is a different
  mechanism from 2PL (single-node locking) despite the similar name;
  that page covers 2PC and Raft-based consensus for transactions spanning
  multiple nodes, a genuinely separate problem from single-node
  serializability.
- [[storage-engines-btrees-and-lsm-trees]] — B-trees' one-copy-per-key
  property is what makes attaching 2PL's index-range locks directly to
  the storage engine practical.

## North Star Connection

Completes the transactions/concurrency-control gap this wiki had zero
prior coverage of. Directly useful the moment any client-facing tool
(see [[../web-frameworks/flask-web-development]]) needs to reason
concretely about "what happens if two users click submit at the same
time" rather than hoping the database's default isolation level happens
to be safe enough.
