---
domain: tech
type: concept
tags: [subject/storage-engines]
timeline: later
status: wiki-only
---

# Storage Engines: B-Trees and LSM-Trees

**Summary**: How databases actually store and retrieve data on disk — the
two dominant families of storage engine (log-structured/LSM-trees and
page-oriented B-trees), how each is built up from first principles (a
2-line Bash key-value store, then hash indexes, then sorted files), and
the concrete performance trade-offs (write amplification, read latency,
fragmentation) that explain why a database "feels" fast or slow for a
given workload.

**Sources**: designingDataIntensiveApplications.pdf (Kleppmann, *Designing
Data-Intensive Applications*, O'Reilly 2017), Chapter 3, "Data Structures
That Power Your Database" (pp. 69–90)

**Last updated**: 2026-07-13

---

## Starting from the simplest possible database

A key-value store can be built from two Bash functions: `db_set` appends
`key,value` to a file; `db_get` greps the file for the last matching line.
Writes are fast (appending is the cheapest possible disk operation) but
reads are O(n) — every lookup scans the whole file. This is the seed every
real storage engine grows from: an append-only **log**, plus an **index**
(extra metadata that trades write overhead for fast lookups) (source:
designingDataIntensiveApplications.pdf). Every index speeds up some
reads and slows down every write — there is no free index, which is why
databases require indexes to be chosen deliberately rather than applied
to everything by default.

## Hash indexes (Bitcask)

The simplest real index: an in-memory hash map from key → byte offset in
an append-only log. This is literally what Bitcask (Riak's default engine)
does — fast reads and writes, as long as every key fits in RAM (values can
exceed RAM; only the offset index must fit). To avoid growing forever, the
log is broken into size-bounded segments, and old segments are
periodically **compacted** (keep only the most recent value per key) and
merged in a background thread. Limitations: the hash table must fit in
memory, and range queries are impossible — you cannot scan "all keys
between kitty00000 and kitty99999" without checking every key individually
(source: designingDataIntensiveApplications.pdf).

## SSTables and LSM-Trees

The fix for both limitations: require segment files to be **sorted by
key** (a Sorted String Table, or SSTable). This buys three things a hash
index can't: (1) merging segments becomes a simple mergesort-style
streaming pass, even when files exceed available memory; (2) the
in-memory index no longer needs every key — it can be **sparse** (one
entry per few KB is enough, since you can jump to the nearest known offset
and scan a short distance); (3) records can be grouped into compressed
blocks, since a read already scans a range.

Constructing a sorted file from arbitrary-order writes: keep an
in-memory sorted structure (a **memtable**, typically a red-black tree);
once it exceeds a size threshold, flush it to disk as a new SSTable
segment; serve reads by checking the memtable first, then each on-disk
segment newest-to-oldest; run background merge/compaction. A separate
on-disk write-ahead log protects against losing the memtable's contents
on crash. This is the actual algorithm behind LevelDB, RocksDB, Cassandra,
and HBase — the general technique (a cascade of sorted files, merged in
the background) is called a **Log-Structured Merge-Tree (LSM-tree)**
(source: designingDataIntensiveApplications.pdf). Real implementations add
Bloom filters (fast "definitely not present" checks, since a lookup for a
nonexistent key otherwise has to check every segment) and choose between
size-tiered compaction (HBase) or leveled compaction (LevelDB, RocksDB;
Cassandra supports both).

## B-Trees

The far more common index in practice — the standard in almost every
relational database since 1970. Unlike log-structured indexes (variable-size
segments, append-only), B-trees break the database into fixed-size
**pages** (traditionally 4 KB, matching how disks are physically
addressed), organized as a tree: a root page routes to child pages by key
range, down to **leaf pages** holding the actual values. Branching factor
is typically several hundred, so most databases fit in a 3–4 level tree —
a 4-level tree with branching factor 500 can address up to 256 TB (source:
designingDataIntensiveApplications.pdf).

Unlike LSM-trees, a B-tree **overwrites pages in place** — updating a key
means finding its leaf page and rewriting that page on disk; references
from parent pages stay valid. Inserting past a page's capacity triggers a
**page split**, which must also update the parent — a multi-page write
that's dangerous on crash (an orphan page is possible if the database
dies mid-split). The standard fix: a **write-ahead log (WAL)** — every
modification is appended to a WAL before it touches the actual tree pages,
so a crash can always replay the WAL to restore consistency. Concurrent
access requires **latches** (lightweight locks) protecting the tree
structure itself, since in-place overwrites can leave the tree briefly
inconsistent mid-update.

## Comparing B-Trees and LSM-Trees

No universal winner — this is a genuine, workload-dependent trade-off, not
a "pick the newer one" decision:

| | LSM-trees | B-trees |
|---|---|---|
| Writes | Faster — sequential writes, lower write amplification in many configs | Slower — every write touches the WAL *and* a page (and possibly split-triggered rewrites of multiple pages) |
| Reads | Slower — may need to check memtable + several SSTables at different compaction stages | Faster and more predictable — one direct path down the tree |
| Storage footprint | Smaller — periodic rewriting removes fragmentation; compresses well | Larger — page splits and partial-page updates leave unused space (fragmentation) |
| Concurrency/transactions | Multiple copies of the same key can exist across segments simultaneously | Each key exists in exactly one place — makes range locks straightforward to attach directly to the tree, which is why B-trees remain attractive for databases wanting strong transactional semantics (see [[transaction-isolation-levels-and-concurrency-control]]) |
| Tail latency | Compaction can occasionally stall a request needing the disk — higher-percentile latency spikes | More predictable under load |

**Write amplification** — one logical write causing multiple physical disk
writes (WAL + page, or repeated SSTable rewrites during compaction) — is
the single number that best explains why a storage engine's write
throughput ceiling sits where it does, and it's specifically why SSD
lifespan (limited overwrite cycles per block) is a real storage-engine
design constraint, not just a hardware afterthought (source:
designingDataIntensiveApplications.pdf).

## Other Indexing Structures (brief)

- **Secondary indexes** (non-unique keys) are built the same way as
  primary indexes, just with either a list of matching row IDs per key or
  a uniqueness suffix appended to the key.
- **Heap files vs. clustered indexes**: a secondary index can either point
  to a separate location where the full row lives (a heap file — avoids
  duplicating data across multiple indexes) or store the row data directly
  in the index itself (a clustered index — faster reads, no extra hop, at
  the cost of write overhead and duplication if there are multiple
  indexes). MySQL's InnoDB always clusters on the primary key; a
  **covering index** is the middle ground, storing a few extra columns
  inline so common queries never need the extra hop.
- **Multi-column and multi-dimensional indexes**: a single B-tree or
  LSM-tree can't efficiently answer "latitude in this range AND longitude
  in this range" simultaneously — that needs specialized structures like
  R-trees (used by PostGIS) or a space-filling curve that folds multiple
  dimensions into one sortable key.
- **In-memory databases** (Redis, VoltDB, Memcached): their speed doesn't
  come from skipping disk reads — a well-cached disk-based engine rarely
  hits disk either, since the OS caches recently used blocks. The real
  gain is avoiding the overhead of encoding in-memory structures into a
  disk-writable format at all.

## Connects to

- [[transaction-isolation-levels-and-concurrency-control]] — B-trees'
  each-key-exists-once property is what makes row-level locking for
  transaction isolation straightforward to implement directly on the
  index.
- [[foundations-of-scalable-systems]] — the sibling source (Gorton) covers
  scaling databases (partitioning, replication, CAP) but not how a single
  node actually stores data on disk; this page fills that specific,
  previously-uncovered gap.
- [[scalable-database-fundamentals]] — the higher-level "why NoSQL, what
  are the data model families" discussion this page's storage-mechanics
  detail sits underneath.

## North Star Connection

Foundational systems knowledge, not an immediate build need — same
"ahead of where Chris actually is" caution this wiki's July 7 alignment
pass already flagged for `distributed-systems/` generally. Genuinely
useful once any project needs to reason about *why* a chosen database
(Postgres, SQLite, Redis, DynamoDB) behaves the way it does under a
specific read/write pattern, rather than treating database choice as a
brand decision.
