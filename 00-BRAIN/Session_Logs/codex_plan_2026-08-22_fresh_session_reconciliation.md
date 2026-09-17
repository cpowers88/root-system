---
type: plan
timeline: next
status: pending
tags: [governance, school, fall-2026, reconciliation]
created: 2026-08-22
review_trigger: fresh-single-agent-session
---

# Fresh-Session Reconciliation Plan — ENGR, TCOM, Integrity Gate 0

## Status and authority

This is a transfer plan, not authorization to edit the target files. Chris authorized
the handoff and preservation of the exact plan on 2026-08-22. The next session must
re-establish the live filesystem baseline and present one reconciled impact plan before
applying school, governance, archive, commit, or push changes.

The canonical literal edit source is:

`00-BRAIN\Session_Logs\claude_report_2026-08-22_engr_corpus_diff_and_tcom_filenames.md`

Its **EDIT SET — for Codex, held for approval** is authoritative. Copy its FIND,
REPLACE, ADD, table, and filename strings directly. Do not retype, normalize, smarten
quotes, collapse spaces, change capitalization, or remove `.docx`.

SHA-256 at transfer:

`F75DBC71A37E031FD06EE2BC72D5F25FD348C4AB9354511FD10FD7B9275522B5`

If that hash changes, re-read the complete report and reconcile the change before using
any literal. A changed hash is a stop signal, not permission to apply the older copy.

## Why the fresh session is mandatory

Chris moved and deleted files from a `raw\` folder and added syllabus copies under
`04-SCHOOL` while Claude and Codex reviews were active. New ENGR files and two Claude
reports also appeared during Codex's review. The prior counts and path inventories are
therefore evidence snapshots, not a safe write baseline.

The next session runs with one agent in `.ROOT`. No second review or editor runs in
parallel during reconciliation or implementation.

## Hard boundaries

- Never read or write `88-JOURNAL\`.
- Do not create, edit, move, rename, archive, restore, or delete anything under any
  `raw\` folder. Chris made the reported raw changes; AI records and routes around them.
- Never delete. Any approved retirement is an archive move with references reconciled.
- Do not restore a deleted raw file automatically, even if Git can recover it.
- Do not treat similarly named syllabi as duplicates. Verify course, section, source,
  version, pagination where relevant, and intended authority from the school copies.
- Do not commit or push without Chris's separate explicit approval.
- Do not apply a FIND/REPLACE against a previously loaded copy. Re-read the target
  immediately before patching and require the literal FIND text to match.

## Transfer fingerprints

These hashes identify the target versions visible when the handoff was written. They are
staleness detectors, not a requirement to restore an older version.

| SHA-256 | File |
|---|---|
| `E52FC3CC780D0231D27B60AC9E8E0B3399B2CAEDFA160D1DE5518FC8510DA8CE` | `04-SCHOOL\SEMESTER_MAP.md` |
| `64B48566EE9CF6AE01390C15241542831BDA309D838C0E34E72807D439A7856C` | `04-SCHOOL\miss-log.md` |
| `7514EC89BFA8FCA1AB6A2746C6FC36D3EEBF6B7F973B1BDAC591068148A5303C` | `00-BRAIN\SYSTEM_FLAGS.md` |
| `1DC6A625DA36A24E2D6524ABD87A3D23680905840D9E2E93101BC85579261003` | `NOW.md` |

## Exact execution order

### Gate A — stabilize and reconcile, read-only

1. Load `AGENTS.md` and the full governed boot chain, then the operating files for
   `04-SCHOOL`, CASTLE, and any wiki whose references are affected.
2. Inspect live Git status, staged and unstaged diffs, untracked paths, and recent path
   history. Identify added, moved, deleted, and duplicated syllabus paths without reading
   or modifying raw content.
3. Reconcile the three new ENGR web-section captures in `04-SCHOOL\05-ENGR` and the
   user-reported duplicate course syllabi. Classify each as exact-section authority,
   neighboring-section evidence, duplicate, or superseded reference. Do not infer from
   filename alone.
4. Trace live references to every relocated syllabus path. Produce the exact stale-link
   and owner-impact list before proposing edits.
5. Re-run root health, CASTLE freshness, boot validation, and the relevant path checks.
   Record every blocker and each check's non-evaluated scope honestly.
6. Re-read both Claude reports and this plan. Recompute the hashes above. If any target
   changed, rebase the edit set against the live text and show Chris the difference.

### Gate B — school truth corrections, approval required

Apply items 1–7 from the canonical Claude ENGR/TCOM report exactly:

1. Correct the ENGR corpus description and departmental-template inference in
   `04-SCHOOL\SEMESTER_MAP.md`.
2. Re-aim ENGR ingestion from a nonexistent syllabus calendar to D2L dates, meeting
   format, and attendance-quiz mechanics.
3. Add Chris's recycled-syllabus week-structure ruling.
4. Replace the invented TCOM filename pattern with the four literal `.docx` filenames
   and the separate email subject-line literal.
5. Correct `LastnameLastnameLastname` to `LastNameLastNameLastName` in the Week 14 row.
6. Reconcile miss-log row 1 to four filenames plus one email subject line, schedule the
   cold spaced rep for Aug 24–25, and record the fourth aid-defect instance.
7. Reword flag #57 rather than re-running it: the syllabus-date search was mis-aimed;
   ENGR D2L date ingestion remains open for Aug 24.

Also reconcile `NOW.md` item 2 against miss-log row 2 at the Sunday review; the miss log
owns the re-aimed rep.

### Gate C — Integrity Gate 0, separate approval scope

After the school-source and relocation baseline is stable, reconcile and seek approval
for the previously proposed integrity work:

- normalize the three ENGR capture headers;
- repair `frontmatter_audit.py` so `register:` vocabulary and applicability are measured;
- remove the verified register leaks only after the fixed instrument exposes them;
- repair CASTLE's human semester router;
- retain platform-discovered `AGENTS.md` and `CLAUDE.md`, and archive only the redundant
  CASTLE `CODEX.md` if Chris approves;
- harden CASTLE freshness and boot-check fail-open/coverage paths before wiring new gates;
- defer the 1,000-file `type:` taxonomy and a new `study-close` skill until evidence and
  a separately approved design exist.

### Gate D — semester hardening

Only after Gates A–C have passed: implement the Excel `TODAY` execution surface and the
bounded semester-hardening changes. CASTLE remains the decision/control layer; course and
school owners remain truth; the workbook remains a human checklist/view.

## Acceptance criteria

- Every Claude literal in the applied ENGR/TCOM edit set is byte-faithful, including
  capitalization, double spaces, punctuation, and all four `.docx` extensions.
- No AI write occurs under `raw\`; no deletion occurs anywhere.
- Every relocated syllabus reference resolves to the intended live owner or is explicitly
  archived/reworded under Chris's approval.
- The three ENGR captures no longer create frontmatter regressions.
- Focused negative tests prove each repaired checker detects the failure it claims.
- Boot validation, CASTLE freshness, root health, link/path checks, and staged plus
  unstaged whitespace checks report their exact state.
- Final diff contains only approved files and no normalized TCOM literals.
- Commit and push remain unperformed until separately approved.

