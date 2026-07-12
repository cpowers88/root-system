---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/concurrency]
---

# Concurrency Fundamentals

**Summary**: Why concurrent execution matters even on a single core (I/O wait), the two classic failure modes of concurrent code (race conditions and deadlocks) and how to avoid each, thread lifecycle, the producer-consumer pattern, thread pools, and barrier synchronization.

**Sources**: Foundations of Scalable Systems.pdf (Chapter 4)

**Last updated**: 2026-06-17

---

## Why concurrency exists at all

Even on a single CPU core, a program spends huge amounts of time waiting on I/O (a disk read taking ~10ms is "an eternity" relative to millions of instructions/second a CPU can execute). Structuring software as multiple concurrent activities lets the OS schedule other work while one task waits — this is true even before multicore hardware existed, and multicore chips (common since 2001) just let truly independent threads run physically simultaneously (source: Foundations of Scalable Systems.pdf). **Threads** are the primary mechanism for this in most mainstream languages, though the underlying model differs: Go uses CSP/channels, Erlang uses the actor model (no shared state, message-passing), Node.js uses a single-threaded event loop that delegates I/O — different syntax, same underlying tension between concurrency and correctness.

## Race conditions

A **race condition** occurs when multiple threads update shared state and the result depends on unpredictable interleaving of their execution. The book's illustrative example: 50,000 threads each incrementing a shared counter by 1 produces a final count *less than* 50,000, because an increment isn't atomic at the machine level — it's load, increment, store as three separate steps, and two threads can interleave those steps and silently lose an update (source: Foundations of Scalable Systems.pdf).

The fix is identifying and protecting **critical sections** — code that touches shared state and must execute atomically. In Java this is the `synchronized` keyword, which serializes access via a per-object monitor lock so only one thread executes the critical section at a time. The general principle (applicable regardless of language): **keep critical sections as small as possible** — the more code is serialized, the worse Amdahl's law bites your scalability (see [[distributed-systems-architecture-patterns]]).

## Deadlocks

A **deadlock** is when two or more threads are each waiting on a resource the other holds, and neither can ever proceed. Classic illustration: the **dining philosophers problem** — five philosophers sharing five chopsticks, each needing both their left and right chopstick to eat. If all reach for their left chopstick simultaneously, none can ever get a right one — permanent circular wait (source: Foundations of Scalable Systems.pdf).

The general fix for circular-wait deadlocks is imposing a **consistent acquisition order** on shared resources — e.g., have one philosopher (or thread) acquire resources in the opposite order from everyone else, breaking the cycle. This generalizes directly to database row-locking deadlocks: two transactions that lock tables in opposite order can deadlock exactly the same way the philosophers do.

## Thread states and coordination

Threads cycle through **Created → Runnable → Blocked → Terminated**. A scheduler (priority-based in Java) decides which runnable thread executes on each core; threads block on locks, I/O, or explicit waits.

The **producer-consumer pattern** is the canonical thread-coordination problem: producers add items to a shared bounded buffer, consumers remove them, and both need to block (not busy-poll) when the buffer is full or empty respectively — busy-waiting/polling wastes CPU resources continually checking a condition. Java's `BlockingQueue` abstracts this entirely, removing the need to hand-write `wait()`/`notify()` signaling logic (source: Foundations of Scalable Systems.pdf).

## Thread pools

Creating a new thread per task is wasteful — each consumes real memory (~1MB stack) and context-switch overhead. A **thread pool** preallocates a fixed set of worker threads and queues excess work until a thread frees up (Java's `ExecutorService`). This is the same resource-discipline idea as connection pooling or the database read-replica pooling discussed elsewhere in the book — bound your concurrency to what your resources can actually support, queue the rest.

## Barrier synchronization

Sometimes you need the opposite of producer-consumer's continuous flow: all threads must reach a point before *any* of them continues — e.g., parallel image-processing segments that all need to finish before the combined image is considered done. Java's `CountDownLatch` implements this: initialize with a count, each thread calls `countDown()` on completion, and any thread calling `await()` blocks until the count hits zero (source: Foundations of Scalable Systems.pdf).

## Thread-safe collections

Standard Java collections (`ArrayList`, `HashMap`, etc.) are deliberately **not** thread-safe by default, for single-threaded performance — using them across threads without explicit synchronization risks corruption. `Collections.synchronizedList()`-style wrappers fix correctness but serialize *all* access (locking the whole collection per operation). The `java.util.concurrent` package's `ConcurrentHashMap` does better via **sharding** — locking only the affected segment, not the whole map — trading off strict consistency (iterators are "weakly consistent," not guaranteed to reflect concurrent updates) for much better concurrent throughput (source: Foundations of Scalable Systems.pdf). This consistency-vs-performance trade-off recurs at much larger scale in distributed databases (deferred to Part III of the book).

## Connects to

- [[distributed-systems-architecture-patterns]] — Amdahl's law, which directly explains why minimizing critical-section size (this page) matters for horizontal scalability.
- [[distributed-systems-essentials]] — partial failures and idempotence are the distributed-systems analogue of race conditions: both are about correctness under unpredictable interleaving/timing, just across machines instead of within one.
- [[theory-of-constraints]] — a thread pool is a literal, mechanical instance of "balance flow, not capacity": bounding concurrent work to a fixed pool and queueing the rest is exactly what a constraint-aware scheduling policy does in [[theory-of-constraints#The Five Focusing Steps|TOC Step 3 — Subordinate everything else]].
- [[foundations-of-scalable-systems]] — source tracker for the whole book.
