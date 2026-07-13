---
type: report
tags: [reference, governance, validation, instruction-design]
created: 2026-07-12
status: changes-requested
---

# ROOT Operating Instructions — Codex Validation

## Verdict

**CHANGES REQUESTED — not yet validated for final release.**

The architecture and most execution work are strong. Automated structure checks pass, `START_HERE.md` shows no execution-time modification, the new master manual is well organized, and the pointer/stage/title corrections landed. Two semantic contradictions in user-facing instructions must be fixed before approval.

## Findings

### P1 — AI_AUTOMATION_SYSTEMS guide falsely says the populated hub is empty

**File:** `G:\My Drive\.ROOT\03-WIKIS\AI_AUTOMATION_SYSTEMS\HOW_TO_USE.md`

**Current text:** line 36 says, “No research or proposals filed yet as of July 12, 2026.” Line 13 also says to use the index “once research accumulates.”

**Evidence:** `wiki\index.md` lines 12–17 says the hub is operational, records six research batches, two approved/promoted self-evolution proposals, and fully processed raw. Lines 21–99 list the research pages; lines 101–113 list the completed proposals.

**Risk:** This is the exact class of current-state drift the new human instruction system is meant to prevent. A user or AI following the guide would ignore a mature evidence base and may recreate work.

**Required correction:** Make `wiki/index.md` the immediate start page. Replace Current State with durable wording such as: operational research hub; multiple research batches ingested; two proposal-to-promotion loops completed; use the index for live inventory and the log for recent activity. Avoid fragile exact page counts.

**Validation:** `rg -n -i "once research accumulates|no research or proposals" 03-WIKIS/AI_AUTOMATION_SYSTEMS/HOW_TO_USE.md` returns no hits, and the guide agrees with the index.

### P1 — Capability Library proof-before-entry rule contradicts its live maturity system

**File:** `G:\My Drive\.ROOT\05-BUSINESS\06-Capability Library\README.md`

**Current text:** lines 16–24 define `idea -> proof -> reusable asset`; line 21 says ideas do not enter the folder unproven.

**Contradicting live authorities/evidence:**

- `CAPABILITY_LIBRARY_INDEX.md` lines 19–20 explicitly define `idea` as captured/unshaped and `draft` as structured/not tested.
- Its line 13 contains `APQC_13_1_WORKFLOW_OBSERVATION_MAP.md` at maturity `draft`, with testing as the next action.
- The asset itself says `draft` at line 17 and “Not yet run” at line 66.
- `FIRST_RUN_CHECKLIST.md` lines 18–31 explicitly creates, indexes, then decides the test and sets maturity honestly.

**Risk:** The user now has two incompatible operating models: proof before asset entry versus draft asset entry followed by testing. The new manual repeats “package only after proof,” so the contradiction propagates into the master instruction layer.

**Required decision and correction:** Preserve the already-coherent maturity ladder and first-run workflow unless Chris explicitly wants to redesign it. Recommended pipeline:

```text
reusable idea -> draft asset -> internal test/proof -> client-ready asset
              -> client instance -> deployment feedback
```

Permit `idea`/`draft` entries when they satisfy the four Entry Rules, have a named test, and state maturity honestly. Require proof before advancing to `tested internally` or `client-ready`, not before entering the library. Align both the README and `ROOT_OPERATING_MANUAL.md` language.

**Validation:** README, manual, checklist, index maturity definitions, and first asset describe the same gate and sequence.

### P2 — SYSTEMS AI operating file retains three stale page-count claims

**File:** `G:\My Drive\.ROOT\03-WIKIS\SYSTEMS\CLAUDE.md`

**Current text:** lines 35, 47, and 59 say 41 pages. The human guide says 78.

**Risk:** Low immediate user impact, but it leaves the AI-facing folder instructions inconsistent with the new human guide and live index. Exact manual counts will drift again.

**Required correction:** Replace exact counts with durable language: inherited FORGE corpus plus later direct ingests; flat structure currently retained; source-family note without a page number.

**Validation:** no live `41 pages` hits remain in SYSTEMS operating files.

### P2 — CASTLE guide metadata still claims July 6

**File:** `G:\My Drive\.ROOT\00-BRAIN\CASTLE\HOW_TO_USE.md`

**Current text:** lines 60–61 say last updated July 6/created during unification, although the file received material July 12 operating-contract changes.

**Risk:** Weakens recency trust in the master instruction network.

**Required correction:** Change Last Updated to July 12 and identify the operating-contract normalization.

## Passed Checks

- New `ROOT_OPERATING_MANUAL.md` exists at the `.ROOT` root and has the required ten-section structure.
- It points to `START_HERE.md` for the map and `WHERE_IT_GOES.md` for placement instead of copying those authorities.
- `START_HERE.md` timestamp predates execution; Claude's DAILY records identical SHA-256 before/after. Codex could not reconstruct the unavailable pre-execution hash independently, but found no evidence of modification.
- Root `AGENTS.md` now points to `00-BRAIN\CODEX.md`.
- CASTLE mission copy was replaced with a canonical North Star pointer.
- CASTLE and PHYSICS both report Stage 3 / Vectors.
- PYTHON index title is corrected.
- Seven wiki guides contain the normalized operating headings.
- Boot-chain validator: **PASS**, 29 boot files, 999 live pages.
- Strict wiki lint: **PASS**, 0 blockers, 0 review debt, 714 expected/classified findings.
- Frontmatter audit completed with the established legacy finding set; no execution-specific new finding was identified.
- Recent protected-path scan found no `raw\`, `99-ARCHIVE\`, or private-path modifications attributable to the instruction execution window.

## Scope Note

The first Capability Library asset was created in an earlier same-day pass, not by the instruction brief. This validation does not reject that asset. It rejects the newly introduced instructions that contradict the asset's valid `draft` maturity and the established first-run checklist.

## Correction Brief

Execution owner: Claude Code.

1. Fix AI_AUTOMATION_SYSTEMS `HOW_TO_USE.md` against its live index.
2. Align the Capability Library README and root manual to the existing draft-before-proof maturity workflow.
3. Remove stale exact counts from SYSTEMS `CLAUDE.md`.
4. Correct CASTLE `HOW_TO_USE.md` Last Updated metadata.
5. Append the relevant wiki/CASTLE logs and DAILY.
6. Re-run boot validation, strict wiki lint, frontmatter audit, and the finding-specific greps above.

No new files, folders, doctrine, capability assets, or structural changes are required.

## Single Next Action

Send this validation report to Claude Code for the four-file correction pass, then return to Codex for a short revalidation.
