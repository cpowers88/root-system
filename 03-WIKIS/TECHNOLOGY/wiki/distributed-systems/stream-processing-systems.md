---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/event-streaming]
---

# Stream Processing Systems (Apache Flink)

**Summary**: Why some use cases can't wait for batch ETL cycles, the Lambda/Kappa architectural answers to that problem, the general anatomy of a stream-processing dataflow, and a concrete walkthrough of Apache Flink's parallelism model and checkpoint-based fault tolerance.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 15)

**Last updated**: 2026-06-17

---

## Batch vs. stream: a latency trade-off, not a strict replacement

**Batch processing** (ETL — accumulate data, periodically load and transform it) is reliable and handles essentially unbounded volume, but the freshness lag (minutes to hours) is fine for a real-estate listing and unacceptable for credit-card fraud detection, where "real time" can mean sub-second decisions (source: Foundations of Scalable Systems.pdf). **Stream processing** trades some of batch's volume/complexity headroom for that low latency, processing events (or small "microbatches") as they arrive rather than waiting for a full batch window.

The **Lambda architecture** (batch layer for completeness + a speed layer for low-latency approximate results + a serving layer merging both) was the original hybrid answer to "I need both." The book notes it's lost ground to the **Kappa architecture** — storing everything in an immutable log (Kafka, per [[scalable-event-driven-processing]]) and treating *all* processing, batch or real-time, as just different consumers reading that same log at different paces. This matters as a design heuristic: rather than building two separate pipelines (batch and speed), a persistent log lets you reprocess history and react to new events through the same mechanism.

## Generic stream-processing anatomy

Data flows from **sources** (a Kafka topic, files in S3) through a **directed acyclic graph (DAG)** of processing nodes performing transforms/aggregations, to **sinks** (a database, another queue) — hence "dataflow systems" (source: Foundations of Scalable Systems.pdf). Two flavors of node logic:

- **Stateless** — transform each event independently (e.g., reshape a wearable device's raw reading into several typed outputs). No memory needed between events.
- **Stateful** — must remember context across events (the running count of bus positions in the last 30 seconds, a fraud-detection model's current parameters, hourly per-item sales totals). This is where the real engineering complexity lives, because that in-memory state has to survive node failures somehow.

## Apache Flink: parallelism and fault tolerance

Flink programs compile down to a logical DAG, then get mapped onto physical cluster resources. Two levers control how much parallel hardware a given operation gets: per-operator `.setParallelism(N)`, or a program-wide default via the execution environment (source: Foundations of Scalable Systems.pdf). Each cluster node runs a **task manager** with a configurable number of **task slots** (commonly one per CPU core) — the unit Flink actually schedules parallel work onto.

**Windowing** is how stateful aggregation gets bounded in an otherwise-unbounded stream: a **sliding window** (e.g., "10-minute window, sliding every 5 minutes") produces overlapping, periodically-refreshed aggregates; a **tumbling window** uses non-overlapping, distinct boundaries where every event belongs to exactly one window.

**Fault tolerance via checkpointing**: Flink periodically injects **barrier** events into the source stream that flow in strict order alongside real data. When a stateful operator sees a barrier on all its inputs, it persists its current state (to RocksDB by default) and forwards the barrier downstream — once a barrier reaches every sink, that's a complete, consistent checkpoint representing "fully processed everything up through source offset N" (source: Foundations of Scalable Systems.pdf). On failure, Flink redeploys the whole application, restores every operator from its last complete checkpoint, and resumes the source from offset N+1. This is conceptually the same "log + periodic snapshot" durability pattern as VoltDB's command log ([[strong-consistency]]) and Redis's AOF+snapshot combination ([[distributed-database-implementations]]) — replay-from-a-known-point is the recurring answer to "how do you recover in-memory state after a crash" throughout this entire book.

The trade-off is explicit: checkpointing small state costs little; checkpointing large managed state can materially reduce throughput — another instance of the book's running theme that durability is never free, only tunable.

## Connects to

- [[scalable-event-driven-processing]] — Kafka topics are the most common data source for Flink/Storm-style stream processors; the Kappa architecture treats them as the single source of truth for all processing.
- [[strong-consistency]] / [[distributed-database-implementations]] — checkpoint-and-replay is the same fault-recovery pattern used by VoltDB's command log and Redis's AOF, applied to in-flight stream state instead of database state.
- [[application-services]] — batching events before sending (Kafka producers, here Flink's window aggregation) is the same throughput-via-batching trade-off as HTTP payload compression.
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
