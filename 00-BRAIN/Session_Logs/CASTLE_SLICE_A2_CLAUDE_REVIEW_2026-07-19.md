---
type: report
timeline: now
status: proposed
tags: [castle, governance, claude-review, slice-a2]
---

# CASTLE Slice A2 — Claude Review: A1 Verification + A2 Challenge and Implementation Order

**Date:** July 19, 2026 (night)
**Author:** Claude Code (Fable 5), Operator hat (Technology Engineer available, not needed)
**Reviews:** commit `18d8f0c` (Slice A1 as implemented) and
`CASTLE_SLICE_A2_CODEX_SYSTEM_REVIEW_AND_PROPOSAL_2026-07-19.md`
**Status:** A1 verified CLOSED. A2 verdict: KEEP scope, MODIFY four things. Nothing implemented — Chris approves the modified wording first.

---

## Part 0 — Slice A1 As Committed: VERIFIED CLOSED

Commit `18d8f0c` checked against the 9-step procedure:

- **All four replacements landed with both my modifications applied** — the
  working property searches and both new router rows (technology-landscape,
  WHERE_IT_GOES) are live in `HOW_TO_USE.md`.
- **Scoped phrase grep: clean.** `FULL OPERATOR` / `daily authority` /
  `Every session that changes files` return zero hits under `00-BRAIN\CASTLE`
  outside the append-only log (whose six historical hits are correct).
- **All four predecessors archived on disk.** They are absent from the commit
  because `99-ARCHIVE/` is git-ignored by design (`.gitignore` line 9) — this
  is correct existing behavior, not a skipped step. Worth remembering: archive
  files have no git backup; the D-drive snapshot is their only second copy.
- **Minor, harmless:** the commit bundles the two review reports, DAILY, log,
  and the `NOW.md` row with the four target files rather than committing docs
  separately. Diff is still readable; no action needed.
- Acceptance tests 1 (cold AI loads CHRIS_CORE — now visible in the pointer),
  2 (no live instruction assigns time), and the README authority fix all pass.

**A1 is done and correct.** The July 26 sweep re-check stands.

---

## Part 1 — A2 Proposal: Overall Verdict

**KEEP the four-file scope and the target-state direction; MODIFY four
things before Chris approves wording.** Codex's live findings are accurate —
they match my own July 19 line-cited review, and its new additions (the
active-capability register, the tier-rule reword, the Rule-4 framing) are
correct diagnoses. But the register as drafted would create the exact defect
class A2 exists to eliminate, one status change over-corrects, two active rows
silently vanish, and the Standing Priority Frame needs an authority anchor.

## Per-File Verdicts (required return 1)

| Target | Verdict | Live evidence |
|---|---|---|
| `north-star-roadmap.md` | **MODIFY (one addition)** | All findings confirmed earlier today (lines 49, 66, 74–97, 101–102). The Standing Priority Frame is better than my two-line pointer — it is undated and stable — but it paraphrases the North Star's priority hierarchy, creating a second statement of priorities that must track the first. Mod 1 anchors it. |
| `source-map.md` | **KEEP structure; row dispositions decided in Mod 4** | Self-contradiction (header vs. lines 68–72), volatile counts (lines 29–45), and the "Tier 1–2 sources determine the roadmap" over-claim (line 9) all previously confirmed. The four-section rebuild, Registration Gate, and confidence reword are right as drafted. |
| `skill-map.md` | **MODIFY (Mods 2 and 3)** | Scheduling block (lines 34–45) and "no zero-commit days" (line 116) confirmed. The register is genuinely required by OPERATIONS Rule 4 — the current tables have no owner, next-rep, or value-path fields. But as drafted it double-homes every active capability. |
| `current-position.md` | **KEEP as proposed** | Minute-level drill state, counts, and the duplicated weak-link question all previously confirmed. The proposed monthly-baseline shape, owner-aware status lines, and Owner Pointers close are correct. August 1 reconciliation date correct. |

## Required Modifications

### Mod 1 — Roadmap: anchor the Standing Priority Frame

Append one line to the frame:

```markdown
This frame inherits the North Star priority hierarchy; it adds no authority and
changes only when `NORTH_STAR.md` changes.
```

Rationale: without the anchor, the roadmap becomes a second place priorities
are *defined* rather than *reflected* — the same consumer-drift pattern A0–A2
exist to end.

### Mod 2 — Skill-map register: one home per capability (the critical one)

Add this rule directly above the register:

```markdown
An active capability lives in this register only. The eight category tables
hold horizon capabilities — statuses `not-started` and `later` — and mark an
activated row with "→ register" instead of carrying a duplicate status.
```

And apply it: the ~10 active rows move out of the category tables (replaced by
"→ register" markers), so no capability ever has two status cells.

Rationale: today's Data Studio defect — the very evidence Codex cites — exists
*because* the same fact lived in two places (`skill-map.md` said not-started,
`current-position.md` said verified). The register as drafted would put Python,
SQL, data visualization, and seven others in two tables inside one file.
Acceptance test 7 cannot be durably true without single-homing.

### Mod 3 — Register contents: two corrections

**(a) Agentic delivery stays `working` — reject the demotion.** Codex demotes
it to `building` for lacking "measured delivery proof." That conflates
promotion evidence with current-state evidence. On the map's own ladder,
`working` means real-workflow use and `proven` requires the evidence artifact:
the tracker V1 shipped July 8 through agentic delivery, and it has been the
daily production method across the scanner, Bootcamp scaffolding, and this
governance program. That is `working` by definition. What is genuinely missing
is the *proven* gate. Exact row:

| Capability | State | Owner | Next real rep | Proof that moves state | Enabled outcome / likely value path |
|---|---|---|---|---|---|
| Agentic delivery | working | approved projects + AI system | measure one real assisted delivery end-to-end | time/quality evidence + Chris explain-back → proven | delivery leverage and reusable methods |

**(b) Decide the two silently-dropped rows explicitly.** The category tables
carry `Waste identification — building` and `Time management under load —
building`; the register omits both without disposition, making it lossy.
Apply Codex's own evidence-calibration principle consistently:

- **Waste identification → horizon** (`not-started`, note: "BUSINESS wiki
  ingested; activates with the first live observation"). Its only evidence is
  reading — the same standard Codex applied to agentic delivery actually
  applies here.
- **Time management under load → remove as a capability row.** The pace model
  is a standing constraint owned by the North Star and phase-map, not a
  capability with a next rep and proof artifact. Keep it as the one-line
  constraint note in the Professional category.

### Mod 4 — Source-map row dispositions (required return / Codex question 4)

Rows that **truly shape roadmap decisions — keep** (claims trimmed of counts):

- The seven spine rows (retitle the section "Authority Spine — pointers, not
  evidence" so the register stays honest about what they are).
- Docs packs (both drove system/landscape decisions and have CASTLE summaries).
- CS50P (spine of the Python path).
- Mark Spain, NAR 2025, ATTOM 2025, GA Bar FAO 23-1 + GREC, Clio 2025 — each
  one demonstrably shaped a gate outcome (OPP-20260716-01/-02) or a strategy
  assumption (S-02/S-03). These are exactly what the Registration Gate is for.
- Internal support rows that back a named phase claim (audit/delivery
  templates, field notes, Revenue Lab scorecard, pre-semester plan), with the
  PYTHON/PHYSICS row stripped to "staged school-readiness paths with mastery
  gates; positions live in the owners' current-position files."

Rows that are **domain-only — remove from CASTLE, note in the owning hub if
not already there:**

- Luke Barousse SQL course → PYTHON wiki (practice resource, shapes no
  roadmap choice).
- MIT OCW Operations Management → SYSTEMS/school owners (same).
- iSixSigma/ASQ and ConstructionDive/AGC → BUSINESS evidence home /
  Watchtower (vocabulary and market texture; they informed no gate or
  assumption on record).

Parked Source Pools section: keep — stable and useful.

## Answers to Codex's Seven Questions

1. **Four-file boundary smallest coherent?** Yes — verified empirically: the
   opportunity-queue greps clean for scheduling/authority language, phase pages
   are Slice B, entrances are done. Nothing missing, nothing extra.
2. **Register required by Rule 4?** Yes — no more compact form meets the five
   named fields, because the current tables structurally lack three of them.
   But it is only *safe* with Mod 2's single-home rule; otherwise it
   manufactures the next Data Studio.
3. **Roadmap concrete enough?** Yes. The 2031 date, income floor, degree,
   phase windows, and milestone table all survive; day-level concreteness now
   correctly lives in `NOW.md` and the register's next-rep column.
4. Answered in Mod 4.
5. **Weakens the destination?** No. Destination, degree, floor, and the
   technology/workflow priority (frame item 2 names it explicitly — matching
   Chris's stated controlling interest) are all retained or strengthened.
6. **SKILL_GAP_ANALYSIS into A2?** No — concur with Codex. It is an owner
   file; editing it inside a CASTLE consumer pass would blur the ownership
   line A2 is drawing. August 1 is its review. The "smallest recurring real
   rep sized to declared capacity" rewording is good — queue it for that
   review.
7. **Missing controlling conflicts?** None found (see 1).

## Implementation Order and Validation (required return 5)

Single commit, ~60–75 minutes, any capable surface, after Chris's one-line
approval of the wording as modified. Order (dependency-logical):

1. **Preconditions:** commit this review's session-log/DAILY changes
   separately first; `git status` otherwise clean.
2. **Archive** the four predecessors to
   `99-ARCHIVE\ARCHIVED_2026-07-19_CASTLE_WIKI_<NAME>.md` (on-disk only —
   `99-ARCHIVE/` is git-ignored by design; do not force-add).
3. **`source-map.md`** — four-section rebuild + Registration Gate + Mod 4
   dispositions (self-contained; nothing depends on it).
4. **`skill-map.md`** — Working Output block, register with Mods 2–3,
   category tables converted to horizon + "→ register" markers, "no
   zero-commit days" deleted.
5. **`current-position.md`** — monthly-baseline rewrite as proposed; status
   lines must quote the register's states verbatim (single source).
6. **`north-star-roadmap.md`** — track-1 rewording, Standing Priority Frame +
   Mod 1 anchor, governing question swap, 2028 outcome-category line,
   evidence-guardrail swap.
7. **Deterministic checks:**
   - Phrase grep (expect zero hits):
     `"What Matters RIGHT NOW"|becomes a sellable service|no zero-commit days|Skill Block Format|suggested calendar block|determine the roadmap|98 pages|51-page` —
     scope `00-BRAIN\CASTLE`, `--glob "!wiki/log.md"`.
   - Single-home check: no capability name appears with a status cell in both
     the register and a category table.
   - Status agreement: register vs. `current-position.md` vs. owner
     current-position files (Python Stage 3 building, Physics Stage 4 next,
     data visualization building, SQL building, field observation building).
   - `python 00-BRAIN\scripts\frontmatter_audit.py --baseline
     00-BRAIN\scripts\frontmatter_baseline.json` — zero new findings.
   - `python 00-BRAIN\scripts\root_health.py` — PASS WITH DEBT, zero new debt.
8. **Close:** CASTLE log append; DAILY block; `NOW.md` `.ROOT` row updated to
   "A2 installed" only. Suggested commit message:
   `CASTLE Slice A2: core maps to reference-grade — register, one-rule source gate, monthly baseline`.
9. **Check dates:** July 26 sweep re-runs the phrase grep and single-home
   check; August 1 monthly review is the register's first live maintenance rep
   and the SKILL_GAP_ANALYSIS rewording decision.

**Acceptance-test amendment:** add to Codex's list —
*13. No capability appears in both an active register row and a category-table
status row (single-home check passes).*

## Return Packet

1. **Outcome:** A1 verified CLOSED as committed (mods applied, grep clean,
   archives on disk, git-ignore explains their commit absence). A2 verdict:
   KEEP scope and direction, MODIFY four things — priority-frame anchor,
   register single-home rule, two register-content corrections (agentic
   delivery stays working; waste-ID and time-management explicitly
   dispositioned), and source-map row dispositions decided.
2. **Evidence:** this report; commit `18d8f0c` stat and live-file greps;
   `.gitignore:9`; opportunity-queue clean grep; all A2 line citations
   cross-checked against my July 19 first-run review of the same files.
3. **Capability/status movement:** none — review only. A2 is
   implementation-ready pending Chris's approval of the modified wording.
4. **Reusable-asset candidate:** no.
5. **System-learning candidate:** double-homed facts are the root cause behind
   every drift instance found this week (Data Studio status, index dashboard,
   roadmap RIGHT-NOW, source-map counts). "One fact, one home, pointers
   elsewhere" is accumulating evidence across four instances; promote to
   `SYSTEM_LEARNINGS.md` at the July 26 sweep if A1/A2 hold.

---
*Chris's next action: one line — "A2 approved with Claude's mods" (or edits) —
then any surface executes steps 1–9.*
