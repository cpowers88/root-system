---
type: ops
tags: [reference, governance]
---

# OPERATIONS.md — How AI Sessions Run the Castle
### Approved by Chris: July 6, 2026 (Pass-2 update same day: castle lives at `00-BRAIN\CASTLE`; NOW.md lives at `.ROOT\NOW.md` but the castle owns it. July 9, 2026, Chris-approved: daily report system added to Session Close)
### One brain, one map: governance lives in `00-BRAIN`. Direction lives here.

---

## Session Boot Order

Any AI session working in `CASTLE` loads, in this order:

1. `C:\Users\chris\.ROOT\00-BRAIN\AGENT.md` — universal OS: shared rules, file safety, session close
2. `C:\Users\chris\.ROOT\00-BRAIN\CLAUDE.md` — lane file (optional HATS\ mode if useful)
3. `wiki/index.md` — what exists in the castle
4. Last 3 entries of `wiki/log.md` — what happened recently
5. `wiki/north-star-roadmap.md` — the current pathway state

Then state in one sentence what the session will do.

## What the Castle Is

The **command center**: the master pathway from Chris's current position to the
North Star (October 8, 2031 — canonical target and identity: `01-NORTH_STAR\NORTH_STAR.md`,
not restated here). It answers, at all times:

> What skill comes next, in what order, why does it matter,
> what source proves it, and what project proves Chris can use it?

## What the Castle Is Not

- Not the behavioral OS — that is `00-BRAIN`. Do not duplicate governance here.
- Not the knowledge refinery — each `03-WIKIS` hub runs its own deep source ingests per its own `CLAUDE.md` (FORGE, the prior single refinery, retired July 7, 2026).
- Not the business-model wiki — that is `03-WIKIS\BUSINESS`. The castle links to it.
- Not a course wiki — `03-WIKIS\PYTHON` and `03-WIKIS\PHYSICS` own Track 1 execution;
  `03-WIKIS\EDUCATION` owns general KSU support (TCOM/ECON/ENGR).
- Not the landscape-research or self-evolution layer — `03-WIKIS\TECHNOLOGY` and
  `03-WIKIS\AI_AUTOMATION_SYSTEMS` research and propose; the castle reviews and
  maintains (see Wiki Sweep below).
- Not a journal, project tracker, or file dump.

The castle REFERENCES the other systems. It never absorbs them.

## Autonomy Level — FULL OPERATOR (set by Chris, July 6, 2026)

AI sessions act without asking inside the castle: update maps, statuses, logs,
phase progress, source registrations, and flag drift proactively. Approval is
required only for: structural changes (new folders, renamed/deleted pages),
opening a new phase, changes to OPERATIONS.md itself, and ANY file outside
`CASTLE`. Report what changed at session close — always.

## Standing Rules

1. **NORTH_STAR.md is the controlling document.** Castle pages reconcile to it,
   never against it. Conflicts get flagged to Chris, not silently resolved.
2. **No orphan skills.** Every skill page must name the phase it serves, the
   service it unlocks, and the proof project that demonstrates it. New profit-skill
   ideas pass through [[adding-a-profit-skill]] before getting a page.
3. **Source tiers rule.** Tier 1–2 sources determine the roadmap. Tier 4 (Reddit,
   YouTube opinion, hype) may only raise questions. Every source lands in
   [[source-map]] with tier, claim supported, and role.
4. **File safety per AGENT.md.** Never modify `raw/`. Never reorganize files
   outside the castle without explicit approval. Archive, don't delete.
5. **Depth before sprawl.** Do not open a new phase/skill/project page while an
   existing one in the same area is a stub. Update `index.md` and `log.md` every
   session that changes files.
6. **Danger weeks (Oct 5 – Nov 11, 2026): school only.** Castle sessions during
   that window are limited to logging and Track 1 support. No new planning.
7. **Chris decides what's permanent.** The castle proposes; Chris approves
   promotions to `.ROOT` and any structural change.
8. **Calendar-encoded capacity.** Castle's schedulable pool = blocks labeled "CASTLE"
   on the **North Star Calendar** (Google Calendar, separate from the primary account
   calendar). Fill CASTLE blocks with whatever the active phase/project needs, no
   separate improvised blocks. Confirmed capacity (verified July 7, 2026): ~24-26
   hours/week of CASTLE-tagged blocks, plus up to ~10 hours/week of float time that
   may absorb overflow but is not guaranteed. Float is not dedicated time — never
   schedule against it directly. CASTLE tags currently run only through Aug 22, 2026 —
   extend into the Fall semester template before classes start or this capacity line
   goes stale (tracked: SYSTEM_FLAGS #51). Clean ceiling:
   26–30 hours/week.

## Wiki Sweep — Seven Hubs (added July 7, 2026 wiki unification; FORGE retired same day, replaced by SYSTEMS)

`03-WIKIS` holds seven hubs: SYSTEMS, PYTHON, EDUCATION, PHYSICS, BUSINESS,
TECHNOLOGY, AI_AUTOMATION_SYSTEMS. The castle's standing job
on top of its roadmap role:

- **Weekly sweep** (alongside the existing Watchtower sweep): read each wiki's
  `log.md` and summarize what moved.
- Maintain `00-BRAIN\vault_map.md` and `.ROOT\.obsidian\graph.json`'s color groups
  so the map stays an accurate, readable picture of the whole tree.
- Flag drift into `SYSTEM_FLAGS.md`: a wiki's `index.md` going stale, a wiki
  growing without matching log activity, orphan pages.
- **Monthly lint** (`AGENT.md § Wiki Shared Layer` rule 8, added July 9, 2026):
  the sweep's deeper tier — dead wikilinks, contradictions between pages, stale
  claims, index-vs-live-tree mismatch — runs at the monthly review or on Chris's
  call. Weekly sweep = light check; lint = deep check; both land findings in
  `SYSTEM_FLAGS.md`.

**Division of labor:** `AI_AUTOMATION_SYSTEMS` researches AI tooling, agent
patterns, and proposes `.ROOT` self-improvements; the castle reviews,
maintains, and keeps things legible. The castle does not do that wiki's
primary research — same eyes-not-hands split already used for the Watchtower.
Stable, repeated proposals from that wiki pass through the review cadence
in `AGENT.md` before landing in `00-BRAIN` governance files.

## Weekly Inbox Routing Checklist

Run this alongside the weekly CASTLE sweep for `.ROOT\77-INBOX` and any approved capture folder.

1. Scan the inbox for raw clippings, quick notes, unsorted ideas, and observations.
2. Capture filter: keep only what is useful, surprising, or tied to an open question — otherwise let it pass. Anti-hoarding heuristic for personal clippings only; consequential/technical/legal/audit sources still get full-source capture in wiki `raw/` regardless of this filter.
3. Route only files with clear homes under `WHERE_IT_GOES.md`.
4. Leave ambiguous files in place and add a `SYSTEM_FLAGS.md` entry instead of guessing.
5. Confirm raw school material stays in the school/course system and is not converted into a business asset unless Chris explicitly asks for the conversion.
6. Confirm reusable client-facing assets include APQC process, asset type, business use case, technical tags, maturity, source/context, and next action.
7. Confirm `05-BUSINESS\06-Capability Library` holds only reusable client-facing assets, not wiki notes or general reference.
8. Confirm no fake client-retainer folders were created before a real client, named prospect, or approved sandbox exercise.

## Session Close

Before ending any session that changed files:
- **Refresh `.ROOT\NOW.md`** — date, today's priority, project status, countdowns.
  NOW.md sits at the .ROOT root so it's the first thing Chris sees; the castle
  owns and maintains it. A stale NOW.md is a broken castle.
- **Append task blocks to today's `00-BRAIN\Session_Logs\DAILY_YYYY-MM-DD.md`**
  (per AGENT.md report-as-you-go, added July 9, 2026). When the castle
  refreshes NOW.md in the morning, it also writes the **previous day's Day
  Summary** if the last session missed it — the castle backstops the daily
  consolidation the same way it backstops NOW.md.
- Update `wiki/index.md` if pages were added/renamed
- Append to `wiki/log.md`: date, what changed, next action
- State the single next action for the following session
- For project or meaningful learning sessions, use the full handoff (`AGENT.md § Report Chain and Handoff Ritual`) instead of just the next action — DAILY blocks stay concise regardless.
