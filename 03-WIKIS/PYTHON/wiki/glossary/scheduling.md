---
type: glossary-entry
stage: 09
status: draft
aliases: []
related_terms: ["automation-script"]
timeline: reference
---

# Scheduling

## Plain-English Definition

Setting up a script to run automatically at certain times or intervals, without someone manually starting it each time.

## What Problem It Helps Solve

Some automation only matters if it actually runs without anyone remembering to trigger it — a daily report, a weekly cleanup.

## When Chris Will See It

A light mention here — full scheduling tools (cron, Task Scheduler) are beyond Stage 9's depth; the concept is worth knowing exists, not drilled deeply yet.

## Code Example

```text
(Conceptual only at this stage — actual scheduling uses OS tools
 like Windows Task Scheduler or cron, run outside the Python script itself.)
```

## Common Confusion

Scheduling is usually handled *outside* the Python script (by the operating system), not by code that "waits" inside the script itself — a script that just sleeps in a loop isn't true scheduling and will stop the moment the program is closed.

## Physical-World Anchor

An alarm clock that goes off automatically each morning, versus relying on someone to manually check the time and decide to start the day.

## Related Terms

- [[glossary/automation-script]]

## Flashcard Q/A

**Front:** Is scheduling usually handled inside the Python script itself, or by the operating system?

**Back:** Usually by the operating system (cron, Task Scheduler) — the script itself just needs to work correctly when triggered.
