---
type: report
timeline: log
status: proposed
tags: [castle, governance, claude-review, slice-a1]
---

# CASTLE Slice A1 — Claude Independent Review and Implementation Instructions

**Date:** July 19, 2026 (late evening)
**Author:** Claude Code (Fable 5), Operator mode
**Reviews:** `CASTLE_SLICE_A1_CODEX_PROPOSAL_FOR_CLAUDE_REVIEW_2026-07-19.md`
**Status:** review complete; three modifications required; implementation instructions included. Nothing implemented — Chris approves the final wording first.

---

## Verdict Summary

**Slice A1 is sound and safe to implement as one commit after three modifications.**
Codex's four replacements do what they claim: they remove every retired-contract
phrase from the entrance layer, complete the inventory, and convert both routers
to pointer-based orientation. I verified every filename in the proposed index
against the live tree (all 30 entries resolve), confirmed the proposed `CLAUDE.md`
frontmatter matches the live file's existing `type: pointer` (no new metadata
type introduced), and confirmed the path claims. The defects are two broken
retrieval suggestions, one validation step that would false-fail on the
append-only log, and one missing route that matters to Chris's stated priority.

## Per-File Verdicts (required table)

| Target | Verdict | Live evidence | Exact modification, if any |
|---|---|---|---|
| `HOW_TO_USE.md` | **MODIFY** | (a) Proposed search `tag:#castle` matches exactly one CASTLE file (`CODEX.md` — verified by grep across all CASTLE frontmatter); `type:map` / `type:proof-project` lack the bracket property syntax every other live page uses (`[timeline:now]` etc.), so all three suggested searches are dead on arrival. (b) The old router's `WHERE_IT_GOES.md` route is dropped, and no route exists for the technology-landscape question — the exact question Chris named tonight as his core interest. | Mods 1 and 2 below |
| `wiki\README.md` | **KEEP as written** | Both "daily authority"/"daily priority" claims removed; `..\` relative paths resolve from `wiki\`; property-filter syntax correct; no schedule prescription ("When beginning active work" describes Chris's choice, not a mandate). | none |
| `CLAUDE.md` | **KEEP as written** | Frontmatter matches live file (`type: pointer` already exists — verified); four-step chain matches AGENT.md's Session Start Protocol order (profile then CHRIS_CORE); no rules duplicated into the pointer. | none |
| `wiki\index.md` | **KEEP as written** | All 30 listed entries verified against the live tree (5 phases, 2 skills, 2 source summaries, 7 templates, root files, core maps). Removing the Planned section is correct: `phase-map.md` still lists phases 5–10 as planned rows and OPERATIONS Rule 5 owns the creation guard, so no discovery or protection is lost. Stale "Current Command-Center State" removal is the fix my July 19 review demanded. | none |

## Required Modifications

### Mod 1 — `HOW_TO_USE.md` § Retrieve: replace the dead searches

Replace:

```markdown
Useful Obsidian searches:

- `tag:#castle`
- `path:"00-BRAIN/CASTLE"`
- `type:map`
- `type:proof-project`
```

with:

```markdown
Useful Obsidian property searches:

- `path:"00-BRAIN/CASTLE/wiki" [timeline:reference] [reference_priority:core]` — core maps
- `path:"00-BRAIN/CASTLE/wiki" [timeline:now]` — current CASTLE pages
- `path:"00-BRAIN/CASTLE" [type:proof-project]` — proof projects
```

Rationale: matches the live frontmatter (CASTLE pages do not carry a `castle`
tag) and the bracket syntax the README's Find a Layer section already uses —
one search idiom across both routers.

### Mod 2 — `HOW_TO_USE.md` § Ask the Right Owner: add two rows

```markdown
| What technology fits this workflow problem? | `02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` — 12 categories + Recommendation Ladder |
| Where does an artifact go? | `00-BRAIN\WHERE_IT_GOES.md` |
```

Rationale: the second restores a route the old router had and Chris actually
uses. The first is new and deliberate: Chris stated tonight (July 19) that his
controlling interest is how technology and workflow fit together and what
applications companies are using. The entrance router should answer that
question in one hop; today it answers pricing and phases but not this. Path
verified against `source-map.md`'s registration.

### Mod 3 — Post-approval validation step 2: exclude the append-only log

The proposed grep ("zero live hits under `00-BRAIN\CASTLE`") **false-fails
today**: `wiki\log.md` contains `FULL OPERATOR` (×4) and `daily authority` (×2)
in historical entries — verified by grep at lines 470, 960, 1171, 1177,
1211–1212. The log is append-only; editing history to satisfy a grep would
violate its own rule. Replace step 2 with:

```
rg -n "FULL OPERATOR|daily authority|Every session that changes files|Refresh NOW.md. — after any" "00-BRAIN/CASTLE" --glob "!wiki/log.md"
```

Expected result: zero hits. Historical hits inside `wiki\log.md` are correct
and remain untouched.

## Answers to the Five Required Questions

1. **Safe as one coherent commit?** Yes, with Mods 1–3 applied. Four files, no
   dependency ordering, no frontmatter type changes, no structural changes.
   Keep the commit pure: session-log/DAILY files from this review commit
   separately.
2. **Fully synchronizes the entrances?** Yes. After A1, zero *live instruction
   or router* text under `00-BRAIN\CASTLE` contradicts the July 19
   `OPERATIONS.md`; the only remaining retired-contract phrases sit in the
   append-only log, where they belong. The remaining conflicts (roadmap,
   source-map, skill-map, current-position) are A2 scope by design, and none
   of them is an *entrance* — a cold session reaches them only after passing
   through now-correct routers.
3. **Narrowing or over-abstraction?** No narrowing — no market, tool, or offer
   language appears in any of the four files. One under-service found and fixed
   by Mod 2: the router had no route for the technology-landscape question,
   which is the practical technology/workflow goal Chris just named as primary.
4. **Entrance conflicts outside the four files?** None controlling. `CODEX.md`
   verified clean (already OPERATIONS-consistent, correct boot pointer).
   `OPERATIONS.md` untouched by design. Nothing should join A1.
5. **Exact validation:** the procedure below, steps 5–7.

Codex's seven challenge notes, briefly: thin-router test **pass** — the
five-field paraphrase in "From Decision to Proof" is two sentences with an
explicit pointer to the formal definitions; acceptable for a Chris-facing
router, and it is the one spot the July 26 sweep should re-check for drift.
Authority, Chris-owned-time, and boundary tests **pass** in all four files.
Path test **fail as proposed** (Mod 1), **pass after**. Index test: removal
correct (evidence in table). Compression test: nothing further worth cutting —
the files are already near minimum viable orientation.

## Implementation Instructions (run after Chris's one-line approval)

**Estimated time:** 30–40 minutes including validation. Any capable surface may
execute; steps assume Claude Code or Codex with local access.

1. **Precondition — clean baseline.** `git status`: confirm no unrelated
   pending edits. Commit any session-log/DAILY changes from this review first,
   separately. (Codex reports Slice A0 committed and pushed — confirm
   `NORTH_STAR.md` shows no pending diff.)
2. **Archive predecessors** (file-safety rule 3, matching the OPERATIONS
   precedent): copy all four live files to
   `99-ARCHIVE\ARCHIVED_2026-07-19_CASTLE_HOW_TO_USE.md`,
   `..._CASTLE_WIKI_README.md`, `..._CASTLE_CLAUDE_POINTER.md`,
   `..._CASTLE_WIKI_INDEX.md`. Cheap, uniform, zero ambiguity.
3. **Apply the four exact replacements** from the Codex packet, with Mod 1 and
   Mod 2 folded into `HOW_TO_USE.md`. Read each live target immediately before
   writing (concurrent-session guard). Full-file replacements; do not merge.
4. **Diff check:** `git diff --stat` shows exactly four modified files plus the
   four new archive files; nothing else.
5. **Phrase check (Mod 3 version):** run the scoped `rg` command above —
   expected zero hits.
6. **Link resolution:** confirm every `[[wikilink]]` and path in the new
   `index.md` resolves (the wiki lint covers wikilinks; spot-check the seven
   template paths and three external pointers).
7. **Gates:** `python 00-BRAIN\scripts\frontmatter_audit.py --baseline
   00-BRAIN\scripts\frontmatter_baseline.json` — zero new findings; then
   `python 00-BRAIN\scripts\root_health.py` — PASS WITH DEBT, zero new debt.
8. **Close:** append `wiki\log.md` (CASTLE state changed) and the DAILY block;
   update `NOW.md`'s `.ROOT` row only to mark A1 done (one phrase, no
   restructure). Single commit, suggested message:
   `CASTLE Slice A1: synchronize entrance files to July 19 OPERATIONS contract`.
9. **Check date:** July 26 governance sweep re-runs step 5's grep and confirms
   the "From Decision to Proof" paraphrase still matches OPERATIONS.

## Return Packet

1. **Outcome:** Slice A1 reviewed against live files; verdict MODIFY-then-
   proceed — three required modifications (dead searches, two missing routes,
   log-scoped validation), all four replacements otherwise approved as drafted.
2. **Evidence:** this report; grep verifications of tag frontmatter, phrase
   locations (including the six historical log hits that forced Mod 3), live
   `CLAUDE.md` frontmatter, and all 30 index entries against the live tree.
3. **Capability/status movement:** none — review only. A1 is implementation-
   ready pending Chris's approval of the modified wording.
4. **Reusable-asset candidate:** no.
5. **System-learning candidate:** validation greps over folders containing
   append-only history must scope the history out — second occurrence of this
   class this week (stale counts, now grep targets). Promote at July 26 only if
   the sweep agrees.

---
*Chris's next action: one line — "A1 approved with Claude's mods" (or edits) —
then any surface executes steps 1–9.*
