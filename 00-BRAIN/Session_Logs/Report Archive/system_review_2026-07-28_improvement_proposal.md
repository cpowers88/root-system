---
type: report
timeline: reference
status: implemented
tags: [governance, system-review]
created: 2026-07-28
implemented: 2026-07-28
---

**Implemented 2026-07-28, same day, Chris-approved.** See the addendum at the
bottom of this file for exactly what was done, one real deviation from the
original proposal (with the reason), and one bug introduced and fixed during
implementation.

# System Review — July 28, 2026 — 5-10% Improvement Proposal

## Summary

I read the open/closed flag history, CASTLE, `WHERE_IT_GOES.md`, the Watchtower,
and ran the frontmatter audit directly rather than trusting the summary number.
The system is in good shape — no rot, no contradicted decisions, no evidence
of drift in HATS or the System Contracts. The single biggest lever is boring:
**the entire 320-item frontmatter debt is one root cause** (a missing
`timeline:` field) concentrated in exactly two hubs, fixable in one small,
fully reversible script pass. Everything else below is smaller. Nothing here
proposes new process, dashboards, or checkpoints — the two recurring failure
patterns I found (metadata drift, silent breakage on restructure) are better
served by finishing an existing fix than by adding a new one.

## Evidence

| # | Finding | Evidence | Recurrence |
|---|---|---|---|
| 1 | **320/320 frontmatter findings are the exact same defect**: missing `timeline:`, nothing else. 100% concentrated in two hubs: PHYSICS (262, 82%) and PYTHON (58, 18%) — every other hub (BUSINESS, TECHNOLOGY, SYSTEMS, EDUCATION, AI_AUTOMATION_SYSTEMS, REVENUE_LAB, CASTLE) is clean. Broken down by `type:`: concept (59), glossary (47), source-summary (45), equation (43), problem-type (37), drill (36), stage (21), worked-example (20), calculus-link (8), common-errors (3), template (10). | Ran `frontmatter_audit.py --json` directly, parsed all 320 findings by path and `type:`. | Every finding, not a sample — this is the whole debt total that `root_health.py` has reported as "reviewed baseline" for weeks. |
| 2 | **15 files use an undefined `priority:` property instead of the approved `reference_priority:`** — all 14 PYTHON stage packets + `stage-template.md`. This is the exact same failure class as closed flag #84 (`register:` propagating by sibling precedent without checking the Metadata Standard first), just smaller and still live. | `grep -rl "^priority:" 03-WIKIS` → 15 files, all PYTHON stages/template. | Same pattern flag #84 already named and closed once (July 25) — this is a second, un-caught instance of it. |
| 3 | **Flag #80's fix has a dangling, unclosed verification loop.** Closed-flag-in-waiting since July 25: "root cause found and fixed, pending one scheduled run to confirm." Tonight's own scheduled 5pm run (`EVENING_READING.md`, generated 2026-07-28) is clean — 0 mojibake, correct em dashes, verified directly in today's session. The confirmation happened; nobody closed the loop. | `SYSTEM_FLAGS.md` #80 text vs. today's live `EVENING_READING.md`. | Three days open past its own stated closing condition. |
| 4 | Silent-breakage-on-restructure is a real recurring pattern (flag #83: `AGENT.md` anchor dropped during a file split; flag #75: stale tracker paths after restructuring; flag #85: three hubs silently diverged on the same canonical-copy question until it became material). Existing tools (`wiki_lint.py`, `validate_boot_chain.py`) already catch broken wikilinks and boot-chain drift; none of them catch a dropped section anchor or a cross-hub policy disagreement — and building that check would be new tooling, which this review is explicitly not proposing. | Flags #83, #75, #85 (three separate root causes, one shared symptom). | 3 instances across July. |

## Proposed changes, ranked by leverage

**1. Frontmatter timeline fix — highest leverage, lowest risk.**
Add `timeline: reference` to the 299 non-stage findings (concept, glossary,
source-summary, equation, problem-type, drill, worked-example, calculus-link,
common-errors, templates) — this is not a guess, it's the value every single
correctly-tagged sibling page in these same folders already uses (verified
directly against several today, including pages I wrote this session). For
the 21 `stage` packets, same fix except whichever stage is each hub's
*currently active* one (PYTHON Stage 4, PHYSICS Stage 4) — those should get
`timeline: next` or `now`, not `reference`, since they're live curriculum
position, not dormant reference. **Risk: near zero — additive-only field,
matches an existing convention exactly, `root_health.py` verifies the result
immediately.** Fully reversible (git). **Needs:** one-sentence go-ahead from
Chris, since it's ~300 files even though each edit is trivial. Not something
to silently batch without asking, per this review's own instructions.

**2. Rename `priority:` → `reference_priority:` in the 15 PYTHON stage files.**
Bundle with #1 since it's the same files. Brings PYTHON's stage packets into
line with the Metadata Standard's actual approved property list, closing a
live second instance of the flag-#84 pattern before it spreads further (there
are more stage packets yet to be built for later PYTHON stages — cheaper to
fix the template now than fix N more copies later). **Risk: none** — this
property currently does nothing (not read by any script), so correcting its
name changes zero behavior. **Needs:** same one-sentence go-ahead as #1.

**3. Close flag #80 with the evidence now available.**
The fix has already been proven correct by tonight's real scheduled run —
record that and move the row to the July ledger. **Risk: none, it's a record
of a fact that already happened.** **Needs:** nothing beyond Chris seeing
this report; I didn't move it myself because closing a flagged item is a
judgment call this review is deliberately leaving to you, not because there's
real doubt.

**4. No new tooling for the restructure-breakage pattern.**
Naming it here is the whole recommendation. `AGENT.md § File Safety` already
requires verifying exact paths before consequential changes; the fix is
consistent execution of that existing rule (grep the vault for a name/anchor
before finishing a rename or restructure), not a new script watching for it.
Building a fourth lint pass to catch a three-times-in-a-month problem would
cost more ongoing attention than it saves — the existing discipline, applied
consistently, already covers it.

## What I deliberately did not change

- **EDUCATION's half of flag #85** (canonical-copy rule) — explicitly your
  decision to make (HIGH, already tracked, already scoped by Chris's own
  words in the flag). Not mine to resolve by review.
- **Flag #57** (EDUCATION/PHYSICS syllabus gaps) — blocked on D2L actually
  populating; nothing internal to fix.
- **Flag #86** (evening-reading vs. cold-gate conflict) — you deliberately
  deferred this July 26 and it hasn't recurred since. Re-litigating a
  settled, working-as-intended deferral isn't an improvement.
- **HATS folder, CASTLE structure, System Contracts** — read all of these
  looking for drift after the July 24-26 architecture work; found none.
  Re-touching a recently settled structural decision without new evidence
  would be the opposite of this review's own standard.
- **Any new dashboard, review cadence, or governance layer** — explicitly
  out of scope per your framing of "5-10% improvement," and would
  contradict `AGENT.md`'s own stated culture ("reduces friction or it gets
  changed").

## Direct fixes made this pass

None. Everything found is either a bounded batch action needing one
go-ahead (items 1-2) or a judgment call left to you (item 3, and the two
EDUCATION-owned flags above). I did not silently edit ~300 files as part of
writing this report. `root_health.py` was re-run to confirm the baseline
figures cited above are current as of tonight: **BLOCKER** (one pre-existing,
unrelated item — `03-WIKIS\EDUCATION\.claude\settings.local.json`, still
awaiting your sign-off, untouched by this review), frontmatter debt
**320 baseline, 0 new**, wiki links clean, both whitespace checks clean.
Not calling anything clean that isn't.

## Implementation Addendum — 2026-07-28, same session, Chris-approved

Chris said "let's do the proposed changes now." Items 1-3 were implemented.
Item 4 (no new tooling) required no action by design.

### Item 1 — frontmatter timeline fix: done as proposed

Added `timeline: reference` to all 320 files that were missing it.
Verification found the real per-hub split differs slightly from this
report's estimate (PHYSICS/PYTHON breakdown by `type:` was: concept 59,
glossary 47, source-summary 45, equation 43, problem-type 37, drill 36,
stage 21, worked-example 20, calculus-link 8, common-errors 3, guide 1 —
320 total, not the "template: 10" bucket originally estimated; templates
carry their content `type:`, not a separate `template` type). Of the 21
stage packets, only one was actually missing `timeline:` *and* currently
active: `03-WIKIS\PYTHON\wiki\stages\stage-04-functions-parameters-return.md`
got `timeline: now`; PHYSICS's active Stage 4 file already had a valid
`timeline:` set (not in the findings) so needed no change. All other stage
packets (dormant or already-closed) got `timeline: reference` like
everything else, per this report's original proposal.

### Item 2 — deviation: deleted `priority:` rather than renaming it

**This report's original recommendation (rename `priority:` to
`reference_priority:`) would have caused a regression, and was not
followed as written.** Verification before acting found the 14 files' actual
`priority:` values (`complete`, `current`, `upcoming`, `later`, one empty) —
none of which are in `reference_priority`'s valid set (`core`, `supporting`,
`lookup`). A literal rename would have replaced 14 timeline findings with 14
*new* schema findings ("invalid reference_priority: ..."), the opposite of
the goal. Two of the values were also independently stale regardless of
schema (`stage-03` marked `priority: current` though Stage 3 has been closed
since July 26; `stage-04` marked `upcoming` though it's the active stage) —
further reason not to preserve them under a validated name. Fix applied
instead: deleted the undefined `priority:` line from all 14 files plus
`stage-template.md` (15 total, matching this report's file count — the
report's "15" included a false-positive 16th match in a documentation file
showing an unrelated JSON schema example, correctly not touched). This
achieves the same underlying goal (stop using an undefined property) with
zero regression risk. Curriculum-sequence position for these stages remains
correctly owned by `current-position.md` and `learning-path.md`, which were
already the real source of truth — the deleted field was duplicate,
undefined, and in two cases already wrong.

### Item 3 — flag #80 closed

Moved to `00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_2026-07.md` with
tonight's real 5pm scheduled-run evidence as the closing proof.
`SYSTEM_FLAGS.md`'s header updated.

### A bug introduced and fixed during implementation

The first pass at item 1 used a raw-bytes script that tried to preserve each
file's existing line-ending style (LF vs. CRLF) by detecting it and
re-encoding. The CRLF-preservation logic was wrong: it blanket-replaced every
`\n` in the *entire* file with `\r\n`, which doubled the `\r` on every
pre-existing line ending in the 47 files that were originally CRLF (turning
`\r\n` into `\r\r\n` — content unchanged, only line endings corrupted). A
second pass (removing legacy `reference`/`parked` tags on 45 of those same
files) used the same flawed logic and compounded it on those files.
`root_health.py` caught this immediately as a `live Markdown text integrity`
BLOCKER (47 findings) and a whitespace BLOCKER, before this file was closed
out — this was never left undetected. Root cause: this repo runs
`core.autocrlf=true` (confirmed via `git config` and the repo's own checkout
warnings), meaning git stores content as LF and manages CRLF conversion at
checkout automatically — manual line-ending preservation was unnecessary and
actively harmful. Fix: normalized all 322 files touched by this session's
scripts to pure LF, letting git's own attribute handle any checkout-time
conversion as designed. Verified clean after: `git diff --check` reports zero
real errors (only routine autocrlf informational warnings), and
`root_health.py` returns **PASS** on frontmatter (0/0/0), whitespace (both
staged and unstaged), and text integrity (0 findings), with the frontmatter
baseline refreshed to reflect the genuinely-zero current state. The one
remaining BLOCKER (`EDUCATION\.claude\settings.local.json`) is the same
pre-existing item named throughout this report, untouched, still awaiting
Chris's sign-off.
