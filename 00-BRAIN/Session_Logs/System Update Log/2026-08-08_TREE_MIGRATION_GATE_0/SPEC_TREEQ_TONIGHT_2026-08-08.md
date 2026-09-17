---
type: report
timeline: now
status: ready-to-build
tags: [tree, codex, treeq, nightly-prep]
created: 2026-08-08
owner: Codex
---

# Spec — `treeq tonight`

**For Codex to build.** Kernel work, so it sits in Codex's area under the
collision rule. All data it depends on now exists in the two registered wikis.

## Why this is the priority

Chris named the gap on 2026-08-08: *"things that I didn't do was look for what to
read to be ready for the next day… I will need readings to be prepared for
classes, likely multiple subjects nightly."*

That is the daily driver. `treeq wiki <ID>` is used once a week. **This is used
every night**, and it answers the one question no agent can answer alone — it
requires joining the meeting schedule, the semester map, the current frontier,
the lead rule, and the source page map across two wikis by date arithmetic.
Ripgrep cannot touch it.

It is also the answer to improvement item **I5, adoption.** A router that gets
opened nightly is a router that survives the semester.

## The week it has to serve

| Night | Prepares | Subjects |
|---|---|---|
| Sun | Mon | **PHYS 09:10 + CSE 16:10** — heaviest |
| Mon | Tue | TCOM |
| Tue | Wed | **PHYS + CSE** |
| Wed | Thu | TCOM |
| Thu | Fri | PHYS + breakout |
| Fri / Sat | — | no class next day; return consolidation or nothing |

## Data contract — all of it already exists

| Field | Where | Status |
|---|---|---|
| `meets:` — list of `'Label: Days, HH:MM-HH:MM'` | wiki charter | **Live** in `PHYS2211.md` and `CSE1321.md` |
| Week → topic → chapter table | `<ID>-semester.md` | **Live** in both |
| `learner_frontier`, `proof_gate` | `<ID>-state.md` | **Live** in both |
| Chapter → printed pages → PDF pages → file | `.ROOT\03-WIKIS\PHYSICS\wiki\textbook-page-map.md` | **Built 2026-08-08, verified** |
| `confidence` / unverified flags | proposal I2 | Not yet — degrade gracefully |

`meets:` passes `check` today because unknown frontmatter keys are permitted.
**Add it to `LIST_FIELDS`** so it is type-checked as a list of strings.

Semester tables are currently Markdown for humans. Two options: parse the table,
or add a machine block. **Recommendation: parse the table.** A second copy of the
schedule in YAML is a competing authority, and that is Law 1.

## Algorithm

```text
treeq tonight [--date YYYY-MM-DD] [--json]

1. target = --date or (today + 1 day)
2. For each registered wiki with `meets:`:
     does it meet on target's weekday?  if no, skip
3. For each meeting wiki:
     a. resolve the semester week containing target from <ID>-semester.md
     b. read the row: what class covers that week
     c. apply the lead rule -> what Chris studies
     d. map chapters -> printed and PDF page ranges
     e. pull proof_gate from <ID>-state.md
     f. collect any unverified/derived markers on the rows used
4. Order output by class start time, earliest first
5. Emit
```

### The lead rule is per wiki, not global

PHYS2211 studies week N+1 during week N. **CSE1321 does not** — Chris is roughly
seven weeks ahead there, and its semester map says Weeks 1–6 are review with the
surplus going to Physics. Read the rule from the wiki, never assume one week.

## Output — human by default

`--json` for machines. The default must fit one screen; see I5. **If the packet
costs more to read than the file it replaces, it will not be used.**

```text
TONIGHT — Sun Aug 23  ->  prepares Mon Aug 24

PHYS 2211   09:10   class: Wk 1 — Intro, 1D motion (Ch 1-2)
  Study     Wk 2 — Vectors, 2D motion
  Read      Ch 3-4 · printed pp. 52-93 · PDF pp. 82-123
            raw/textbook/Physics book-0001-0100.pdf
            (Ch 4 continues into ...0101-0200.pdf)
  Proof     Decompose one non-axis vector cold; explain x/y independence
  !         Section 54 exam dates unverified — D2L opens Aug 23

CSE 1321    16:10   class: Wk 1 — Module 0
  Study     review only — you are ~7 weeks ahead
  Do        Syllabus & Policy Quizzes (graded)
  Note      No study block here. Surplus goes to PHYS 2211.

2 subjects · 1 requires real study
```

Note the last line. **A count of what actually needs work** is what makes the
output trustworthy on a heavy night — it distinguishes two real subjects from one
real subject plus a formality.

## Edge cases, all required

| Case | Behavior |
|---|---|
| No class tomorrow | Exit 0, say so, suggest the open proof gate from each wiki. Never invent work. |
| Target outside the semester | Exit 0, name the preparation-phase item for that date if one exists, else say the semester has not started. |
| A wiki meets but its semester map has no row for that week | **Exit nonzero and name the wiki.** A silent skip is how a subject gets missed. |
| A chapter is not in the page map | Emit the chapter without page numbers and flag it. Do not guess. |
| Chapter spans two PDF files | Name both. Four active-path chapters do this: 4, 7, 10, 17. |
| Rows used are derived, not verified | Surface the flag inline, as in the `!` line above. |

## Acceptance tests

1. `--date 2026-08-24` returns **both** PHYS2211 and CSE1321, PHYS first by time.
2. `--date 2026-08-25` returns neither (Tuesday: TCOM only, not yet registered)
   and exits 0 with the no-class message.
3. PHYS output carries the correct chapter **and both page numberings** for that
   week, matching `textbook-page-map.md`.
4. CSE output for any date before Oct 5 states the review posture and does not
   request a study block.
5. The proof gate appears without the invocation mentioning proof.
6. Removing a `meets:` field drops that wiki from all output and `check` still
   passes — the feature degrades, it does not crash.
7. Deterministic: same date, same output, byte for byte.

## Must not

- Must not read `journal/private/`.
- Must not write anything. Read-only command.
- Must not invent a reading when the map has no entry.
- Must not answer a physics or programming question. It assembles.
- Must not require network access.

## Companion: counting the work

Chris: *"it also needs to be counted morning or night."*

No new machinery. `<ID>-state.md` gains a session table — date, start, duration,
what was worked, artifact, outcome. **The frontier moves on evidence, never on
the clock.** `SYSTEM.md`'s acceptance suite already requires exactly this: *"real
work at any hour counted from evidence rather than a fixed clock assumption."*

A later `treeq worked` could append it, but hand-editing the table is enough for
V1 and avoids a write path in a read-only tool.

## Two adoptions from COG-second-brain

Reviewed 2026-08-08 at Chris's request. It converged independently on
Markdown-canonical, deterministic retrieval, no embeddings, no vendor lock-in,
and `last_verified` + confidence stamping — that last is improvement item I2,
invented separately. Useful corroboration.

**Adopt 1 — tiered progressive enrichment.** COG gates page depth on demand:
stub, then moderate, then full as a topic is actually reached. **This replaces
improvement item I1.** I1 measured waste after it was built; this prevents
building it. It is the direct structural fix for `.ROOT`'s largest failure — 18
stage packets and ~250 physics pages generated against a Stage 4 frontier, with
`learning-path.md` admitting in its own words that *"generated content is not
studied content."*

**Adopt 2 — the verification harness.** *"The worker never grades its own
homework; verifiers observe the artifact, not the worker's summary."* Today
supplied two cases: a report stated the validator warns on `00-turnk` while
running it printed no warning, and the B1–B6 completion report was accurate —
but only confirmable by executing it. Make it a rule: **completion is verified by
running the artifact, never by reading the report.**

Do not adopt COG's numbered `00-inbox`/`01-daily` folders — that is `.ROOT`'s own
failure 6.3, a numbering scheme that encodes nothing. Do not adopt its 33-skill
surface; Law 10.

## Build order

1. `meets:` into `LIST_FIELDS`.
2. Semester-table parser.
3. `tonight` with human output and `--json`.
4. Page-map lookup, sourced from `textbook-page-map.md`.
5. Acceptance tests 1–7.

**Ship before August 22.** After that the semester outranks the system, and a
nightly-prep command that arrives in September has missed the two weeks it was
built for.

---

*Prepared by Claude Code, 2026-08-08. Data verified, not inferred. No authority;
Chris decides.*
