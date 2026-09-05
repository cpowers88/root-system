---
type: concept
stage: 09
status: draft
source_refs: ["Automate the Boring Stuff Ch.19 (Keeping Time, Scheduling Tasks)", "Automate the Boring Stuff Ch.20 (Sending Emails, light mention)"]
prerequisites: ["organizing-files-at-scale", "csv-and-json", "decomposition-and-pseudocode"]
tags: [automation, scheduling, decision-rule]
timeline: reference
---

# Concept: Designing an Automation Script

## Plain-English Meaning

This isn't new syntax — it's the decision process for turning a repetitive chore into a script: identify the repeated manual steps, decide what triggers the script (a schedule, a file appearing, running it by hand), and decompose it the same way Stage 7 taught, but now with files/folders/structured data as the building blocks.

## What Problem This Solves

The whole point of "automation" isn't any single new piece of syntax — it's recognizing a real chore that's boring/repetitive/error-prone by hand, and applying everything from Stages 1-8 to replace it with a script.

## When To Use It

Whenever a task involves doing the same steps repeatedly on files, spreadsheets, or structured data — sorting downloads, generating a weekly report, renaming a batch of files consistently.

## When Not To Use It

A one-time task that will genuinely never repeat usually isn't worth automating — the time spent writing and testing the script might exceed just doing it once by hand. Automate things you (or someone) will do more than a couple of times.

## Code Shape

```text
1. Identify the repeated manual chore precisely (what exactly do you do, every time?)
2. Decompose it into steps (Stage 7's process, applied here)
3. Identify what data it reads (files? CSV? a folder listing?) and what it produces
4. Build incrementally, testing each step against real (or sample) data
5. Decide how it should be triggered: run manually, or check Automate the Boring Stuff Ch.19 for basic scheduling
```

## Tiny Working Example

```python
# Chore: "Every week I manually count how many .txt files are in my notes folder"
import os

txt_count = 0
for filename in os.listdir("notes"):
    if filename.endswith(".txt"):
        txt_count += 1
print(f"{txt_count} text files found.")
```

## Beginner Mistakes

- Trying to automate something too vague ("organize my computer") instead of one precise, repeated chore.
- Skipping testing on sample/throwaway data before running an automation script against real files — file-moving and file-deleting mistakes are hard to undo.
- Reaching for complex scheduling (cron jobs, Task Scheduler) before the script itself reliably works when run manually.

## Physical-World Anchor

Setting up a recurring chore chart versus doing the chore from memory each time — the chart (script) only helps once it accurately reflects the actual steps.

## Required Vocabulary

- [[glossary/automation-script]]
- [[glossary/scheduling]]

## Related Code Patterns

- [[code-patterns/organize-files-by-extension]]
- [[code-patterns/read-csv-and-process]]

## Drill

- [[drills/stage-09-automation-practice]]

## Explain-Back Questions

1. What makes a chore a good candidate for automation, versus not worth automating?
2. Why should an automation script be tested on sample data before running it on real files?
3. Describe a repeated chore from your own life (school, hobbies, anything) and sketch how you'd decompose it into an automation script.

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Ch.19, "Keeping Time, Scheduling Tasks, and Launching Programs" — light conceptual mention of scheduling only, not deep implementation)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.20 — mentioned only as an example of "what automation can grow into," parked for deeper use per `wiki/parking-lot.md`)
