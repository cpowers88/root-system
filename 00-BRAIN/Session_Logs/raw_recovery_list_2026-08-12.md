---
type: report
timeline: now
register: system-review
status: active
tags: [flag-97, raw, data-loss, recovery, clipper]
created: 2026-08-12
---

# `raw\` Recovery List — flag #97, council step 1

**Read-only reconciliation of all 9 `raw\` queues. Nothing was moved, renamed, or
deleted.** 264 `.md` files hashed and compared filename-against-frontmatter.

> **Do not dedupe on hash.** The filenames below are the only surviving record of
> what is missing. Deleting the duplicates makes the loss permanent and invisible.
> This list exists so that a cleanup pass has somewhere to look first.

## A. Sources that were never captured — 5 files, re-clip these

Each file's **body** belongs to a different article. The **filename** is the only
evidence the intended source was ever queued.

| Filename (the only record) | What the file actually contains |
|---|---|
| `SYSTEMS\raw\13  Project management.md` | NIH Data Management policy |
| `SYSTEMS\raw\Data Management for Researchers Three Tales.md` | NIH Data Management policy |
| `SYSTEMS\raw\Eight Principles of Good Data Management.md` | NIH Data Management policy |
| `SYSTEMS\raw\aimos2021 - Rose O'Dea The next 10 years.md` | *What's Wrong with Social Science* |
| `SYSTEMS\raw\Why Trust Science.md` | *What's Wrong with Social Science* |

**Content that DID survive**, and needs exactly one home each:

- *NOT-OD-21-013: Final NIH Policy for Data Management and Sharing* —
  `https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html` — currently
  in 4 files, correctly named in `NOT-OD-21-013 Final NIH Policy for Data Management and Sharing.md`
- *What's Wrong with Social Science and How to Fix It* (Alvaro de Menard, 2020-09-11) —
  `https://www.fantasticanachronism.com/p/whats-wrong-with-social-science-and-how-to-fix-it` —
  currently in 3 files, correctly named in
  `What's Wrong with Social Science and How to Fix It Reflections After Reading 2578 Papers.md`

**Root cause** (council, 2026-08-11): the clipper pre-fills the note name from
whichever tab was active when the popup opened, then re-extracts content at save
time. Clipping several tabs quickly yields a name and a body from different pages.
**Fix or retire the clipper before pointing it at anything else.**

## B. Placeholder or truncated names — 4 files, rename not recovery

Content exists; the filename or title is junk. No data is lost.

| File | Frontmatter title |
|---|---|
| `AI_AUTOMATION_SYSTEMS\raw\Conversation.md` | `New notebook` |
| `TECHNOLOGY\raw\co.md` | `Edit CSV - Visual Studio Marketplace` |
| `TECHNOLOGY\raw\Mixture of SMB wedges and enterprise stacks.md` | `TEMP*conversation grok*TEMP` |
| `TECHNOLOGY\raw\readthis.md` | `Tech stack roadmap for workflow/AI systems integration (unsourced chat export)` |

## C. Benign — no action

- `loopany part 1 / part 3 / part 4 / CLAUDE.md / INSTALL_FOR_AGENTS.md` (5 files) —
  deliberate multi-part split of one repo; shared title is correct.
- `Second brain obsidian.md`, `LLM WIKI.md` — shortened filenames for very long repo
  titles. Intentional.
- 5 × identical `README.md` under `PHYSICS\raw\*\` — folder scaffolding, not content.

## D. Unverifiable by this method — 37 files

37 raw `.md` carry **no frontmatter `title:`**, so filename-against-title cannot be
checked. Not evidence of loss; simply outside what this pass can see. Lower priority
than section A.

## Method, and what it would have missed

264 files MD5-hashed; 3 byte-identical groups found (x5 benign, x4, x3). Filenames
were then normalised and compared against frontmatter titles by word overlap.

**The name-comparison heuristic under-reported.** `Data Management for Researchers
Three Tales.md` and `Eight Principles of Good Data Management.md` both scored *above*
the mismatch threshold, because they share the words "Data Management" with the NIH
article that overwrote them. Only the hash comparison caught those two. Either check
alone would have missed part of the loss — recorded here so a future pass does not
run just one of them and call the queue clean.

## Status

Council step 1 (`COUNCIL_RECONCILED_VERDICT.md`) is **complete as specified**:
filename-vs-frontmatter reconciled across all nine queues, recovery list produced
outside `raw\`, nothing deleted. Re-clipping the 5 sources in section A is Chris's
call and is not blocked by anything.
