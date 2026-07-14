---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/transactions]
---

# Transaction Isolation Levels: Dirty Reads, Snapshot Isolation, and Write Skew

**Summary**: What ACID transactions actually guarantee (and why "consistency"
doesn't really belong in the acronym), the weak isolation levels every
mainstream database actually runs by default (read committed, snapshot
isolation), the specific race conditions each one does and doesn't
prevent (dirty reads/writes, read skew, lost updates, write skew,
phantoms), and why "just use an ACID database" doesn't automatically
solve any of this. Companion page [[serializability-2pl-and-serializable-snapshot-isolation]]
covers the strong-isolation techniques that prevent everything on this
page's list.

**Sources**: designingDataIntensiveApplications.pdf (Kleppmann, *Designing
Data-Intensive Applications*, O'Reilly 2017), Chapter 7, "Transactions" —
"The Meaning of ACID" through "Write Skew and Phantoms" (pp. 221–251)

**Last updated**: 2026-07-13

---

## What a transaction actually buys you

A transaction groups several reads/writes into one logical unit: either
the whole thing commits, or it aborts and the application can safely
retry without worrying about partial failure. That's the entire point —
transactions exist to simplify the application's error-handling model,
not because they're a law of nature. Not every application needs them,
and weakening or abandoning transactional guarantees is a legitimate
trade-off for performance or availability, not automatically a mistake
(source: designingDataIntensiveApplications.pdf).

## ACID, more carefully than the acronym suggests

- **Atomicity** — not about concurrency (that's isolation). It's about
  faults mid-transaction: if a fault occurs partway through a multi-write
  transaction, the database discards everything written so far. "Abortability"
  would have been the more accurate word.
- **Consistency** — an application-specific notion of "the data is in a
  good state" (e.g., accounting debits/credits balance). This is **not**
  something the database can enforce in general — it's the application's
  responsibility to write transactions that preserve its own invariants.
  Kleppmann's own verdict: "the letter C doesn't really belong in ACID" —
  atomicity, isolation, and durability are database properties; consistency
  is an application property that merely relies on the other three.
- **Isolation** — concurrently running transactions can't see each other's
  half-finished work. The gold-standard formalization is **serializability**:
  the result is as if transactions ran one at a time, even though they
  actually overlapped. Rarely used in practice, though, because it carries
  a real performance cost — most databases run a weaker isolation level by
  default (see below).
- **Durability** — once committed, data survives crashes. In practice this
  is always a risk-reduction bundle (disk + replication + backups), never
  an absolute guarantee — correlated faults (power loss hitting every
  replica, SSD firmware bugs, silent disk corruption) can defeat any single
  durability mechanism (source: designingDataIntensiveApplications.pdf).

**Single-object vs. multi-object**: atomicity/isolation for a single key
is basically universal (every storage engine provides it via a log +
per-object lock). Multi-object transactions — needed whenever denormalized
data or secondary indexes must stay in sync across more than one record —
are the part many distributed/NoSQL databases dropped for scalability
reasons. That drop is a real trade-off, not a free upgrade.

## Read Committed — the common default

The baseline isolation level (default in Oracle, PostgreSQL, SQL Server,
and most others). Two guarantees only: **no dirty reads** (you never see
another transaction's uncommitted writes) and **no dirty writes** (you
never overwrite another transaction's uncommitted writes — the second
writer waits for the first to commit/abort). Implemented via row-level
locks for writes; reads are usually implemented by keeping both the old
committed value and the new uncommitted value, and serving readers the old
value until commit — not by taking a read lock, because that would let one
slow write stall every reader (source: designingDataIntensiveApplications.pdf).

**What read committed does *not* prevent**: the lost-update race (two
concurrent counter increments, Alice's and Bob's writes both succeed but
one silently clobbers the other) and **read skew** — Alice checks two bank
account balances mid-transfer and sees $900 total instead of $1,000,
because she read account 1 before the transfer and account 2 after it.
Read skew is "acceptable" under read committed because each value she saw
really was committed at the time — but it makes read committed unsafe for
backups and analytic/integrity-check queries that scan large parts of the
database over time.

## Snapshot Isolation — the fix for read skew

Each transaction reads from a consistent snapshot: the state of the
database as of when the transaction started, regardless of what commits
afterward. Implemented via **multi-version concurrency control (MVCC)** —
the database keeps multiple committed versions of each object side by
side, and a set of visibility rules (ignore writes from transactions still
in-progress at your start time; ignore writes from transactions that
started after you; ignore aborted writes) determines what your transaction
sees. Key performance property: **readers never block writers, and writers
never block readers** — a sharp contrast with the locking approach
[[serializability-2pl-and-serializable-snapshot-isolation]] covers (source:
designingDataIntensiveApplications.pdf).

**Naming trap worth knowing**: Oracle calls this isolation level
"serializable" (it isn't — see the companion page); PostgreSQL and MySQL
call it "repeatable read" (per the SQL standard's much older, ambiguous
definition, predating snapshot isolation's invention) — "nobody really
knows what repeatable read means" across vendors, per Kleppmann's own
assessment. Always verify what a specific database's isolation-level name
actually implements rather than trusting the label.

## Preventing lost updates

Snapshot isolation alone doesn't solve the lost-update read-modify-write
race. Four real fixes, in order of preference:

1. **Atomic operations** (`UPDATE counters SET value = value + 1`) —
   best when the operation can be expressed this way; usually implemented
   with an exclusive lock held for the duration ("cursor stability").
2. **Explicit locking** (`SELECT ... FOR UPDATE`) — needed when the update
   logic can't be expressed as a single atomic operation (e.g., a
   multiplayer game's move-validation logic).
3. **Automatic detection** — some databases (PostgreSQL's repeatable read,
   Oracle's serializable, SQL Server's snapshot isolation) detect a lost
   update at commit time and abort the offending transaction; notably
   **MySQL/InnoDB's repeatable read does not** — a real, easy-to-miss gap
   between vendors claiming the same isolation-level name.
4. **Compare-and-set** — `UPDATE ... WHERE id = X AND content = 'old value'`
   — only safe if the database doesn't evaluate the `WHERE` clause against
   a stale snapshot; verify this per-database before relying on it.

## Write Skew and Phantoms — the subtler failure mode

Neither a dirty write nor a lost update (different transactions update
*different* objects), but still a genuine race: two transactions each read
some shared precondition, both see it as satisfied, and both then write in
a way that — combined — violates the invariant neither one violated alone.
The canonical example: a hospital requires ≥1 doctor on call per shift;
Alice and Bob are both on call and both feeling sick; both transactions
check "are there ≥2 doctors on call?", both see 2, both go off call, and
now the invariant (≥1 on call) is silently broken — even though neither
transaction did anything wrong in isolation (source:
designingDataIntensiveApplications.pdf).

**Other real instances of the same pattern**: double-booking a meeting
room (check for conflicts, then insert — snapshot isolation doesn't stop a
concurrent conflicting insert), two figures moved to the same board
position in a multiplayer game, double-spending (two concurrent debits
that individually look fine but together overdraw an account). A
**phantom** is the specific mechanism underneath most of these: a write in
one transaction changes the result set of another transaction's search
query, and since the query originally returned *zero rows*, there's
nothing for `SELECT FOR UPDATE` to attach a lock to — you can't lock a row
that doesn't exist yet.

**Mitigations, none fully general**: a unique constraint solves the
username-claiming case cleanly; explicitly locking the rows a decision
actually depends on helps the doctor/on-call case; **materializing
conflicts** (pre-creating dummy lock rows — e.g., one row per room per
15-minute slot — purely so there's something to attach a lock to) works
but is "ugly" and a last resort per Kleppmann's own framing. The only
mechanism that prevents *all* of these automatically is true serializable
isolation — see [[serializability-2pl-and-serializable-snapshot-isolation]].

## Connects to

- [[serializability-2pl-and-serializable-snapshot-isolation]] — the
  companion page: how databases actually deliver the stronger guarantee
  this page's whole catalog of race conditions requires.
- [[storage-engines-btrees-and-lsm-trees]] — B-trees' each-key-exists-once
  property is what makes attaching row-level locks for isolation
  straightforward; LSM-trees' multiple-copies-across-segments shape makes
  it harder, which is part of why B-trees remain the default choice for
  transactionally-heavy databases.
- [[strong-consistency]] — this page's isolation levels are the
  *single-node* concurrency-control story; that page covers the
  *distributed* consensus/2PC story for transactions spanning multiple
  nodes — related but genuinely distinct problems, not duplicates of each
  other.

## North Star Connection

This is core, load-bearing software-engineering knowledge with zero prior
coverage in this wiki — unlike most of `distributed-systems/`, this isn't
"ahead of where Chris is." Any application with a database and more than
one concurrent user runs into some subset of this page's race conditions,
whether or not the developer knows the vocabulary for it. Directly
relevant the moment a Flask app (see [[../web-frameworks/flask-web-development]])
needs correctness guarantees under concurrent requests, not just working
demo code.
