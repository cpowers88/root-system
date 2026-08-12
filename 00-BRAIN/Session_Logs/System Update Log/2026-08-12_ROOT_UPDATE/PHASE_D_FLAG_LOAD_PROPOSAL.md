---
type: report
timeline: now
register: system-review
status: proposed
tags: [update, phase-d, flags, instruction-layer, load]
created: 2026-08-12
---

# Phase D proposal — take the flag register out of the boot load

**Status: PROPOSED. Nothing has been moved.** Chris's decision required.
Originated by Chris, 2026-08-12: *"what if we just lost the flags there, and the larger
facts if needed in separate file."*

## The measurement

Always-load is **6,803 words**. `SYSTEM_FLAGS.md` is **2,091 of them — 31%**, and it is the
only component that grows without bound. It gained ~158 words on 2026-08-12 alone from
that day's own flag work.

Of those 2,091: **1,668 are the seven open-flag table rows** (80%). The remaining 423 are
the header, the PAUSE banner, § The Rule, and the closed-flags pointer.

| Flag | Words |
|---|---|
| #96 | 590 |
| #97 | 351 |
| #94 | 235 |
| #57 | 175 |
| #69 | 127 |
| #93 | 100 |
| #16 | 90 |

## The finding that shapes the fix

**Only three of the seven flags forbid an action.** The other four are work items that a
session cannot act on at boot anyway.

### Boot-time prohibitions — these must survive in the always-load

| # | The constraint, in full |
|---|---|
| **97** | **DO NOT DEDUPE `raw\` ON HASH.** Five sources survive only as filenames; a hash-based cleanup destroys the only record of what is missing. AI may not write under `raw\` at all. |
| **96** | **The bulk-work gate covers `Bash`, NOT `PowerShell`.** Windows bulk work is governed by discipline alone. A spawned child can write `88-JOURNAL` and every `raw\`. Never describe the gate as covering "bulk work." |
| **94** | **Methods moved behind a conditional load stop being applied.** Situational procedures may move; methods used every time may not. (This is the guardrail for Phase D itself.) |

That is ~120 words against the current 1,176 those three flags occupy.

### Not boot-time — move out of the load entirely

| # | Why it is not a boot constraint | Where it belongs |
|---|---|---|
| 57 | A dated calendar trigger, and **`NOW.md` already carries the Aug 17 date** in its Fixed and Dated table. Loading it twice buys nothing. | `04-SCHOOL\SYLLABUS_STATUS.md` (already the owner) |
| 16 | A teaching to-do for the next physics session touching vector products. | the PHYSICS teaching queue |
| 69 | A chore only Chris can execute — AI cannot pass the `raw\` guard. | Chris's action list |
| 93 | Build backlog; needs Codex hook-mechanics design before anyone implements. | the work register |

## Proposed shape

- **`SYSTEM_FLAGS.md`** keeps: the PAUSE banner, § The Rule, the *Last updated* line, the
  three prohibitions above in full imperative form, and a one-line index of every other
  open flag (number, one-phrase subject, severity, pointer). Target: **~700 words, down
  from 2,091.**
- **`SYSTEM_FLAGS_DETAIL.md`** (new, not loaded) takes the full forensic entries — the
  measurement history, what was tried, which probe was wrong, provenance disputes.
- Closed flags continue to `CLOSED_FLAGS_YYYY-MM.md` exactly as today. **This proposal
  extends a pattern this vault already runs; it does not invent one.**

**Net effect on every future session: ~1,390 fewer words, ~20% of the entire always-load,
with every live prohibition still present.**

## Risks, stated plainly

1. **The imperative must survive the trim.** If #97's line loses "DO NOT DEDUPE ON HASH,"
   a cleanup pass destroys evidence — the precise outcome the flag exists to prevent. The
   summary line must carry the prohibition itself, never a pointer to it. This is the one
   way this change can go badly wrong.
2. **Detail one click away is detail some sessions will not open.** Flag #96 records that
   a session claimed to have filed a flag and had not. That kind of provenance note is
   what stops a settled question being re-litigated. Mitigation: the index line names the
   pointer explicitly, and any session *working* a flag must open the detail.
3. **This is a governance change.** It alters what every future session reads. Requires
   Chris's approval, and per `AGENT.md` § System Evolution Authority it wants a named
   check date.

## Contradiction found while measuring — fix it in the same pass

`AGENT.md` disagrees with itself about when this file loads:

- **L134** (Session Start Protocol step 3): "Check `SYSTEM_FLAGS.md` for the active task."
- **L153** (File Safety 7): "required context for **system, file-write, and review** sessions."
- **The file's own header:** "Check at every session start."

Two of those say always; one says situational. Whatever Chris rules on this proposal, the
three lines should be made to agree — an ambiguity in the load rule is how a file ends up
loaded by default forever without anyone deciding it should be.

## Verification if approved

1. `validate_boot_chain.py` — must stay PASS; `SYSTEM_FLAGS.md` is in `BOOT_FILES`.
2. `root_health.py` — must stay exit 0.
3. Re-measure the always-load and record the new figure in `UPDATE_PLAN.md`.
4. **Behavioural check, not just structural:** open a fresh session and confirm it can
   state all three prohibitions without opening the detail file.
5. Named check date, per System Evolution Authority.
