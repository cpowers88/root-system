---
type: map
timeline: reference
reference_priority: core
tags: []
---

# START HERE — The Whole System on One Screen
### For Chris Powers, aka theinternet. Updated July 15, 2026 (root-entry + metadata reconciliation). If anything here confuses you, that's a bug — tell the AI.

---

## Your Morning

Open **`NOW.md`** — it's right next to this file. One page: today's
priority, this week's reps, countdowns. That's the whole ritual.
The castle maintains it; if the date is stale, tell the AI.

---

## The Map

| Open… | When you want to… |
|---|---|
| 📄 `NOW.md` | **Start your day.** One screen, one priority. |
| 📘 [ROOT_OPERATING_MANUAL.md](ROOT_OPERATING_MANUAL.md) | **Learn how to operate.** Use the proof loops, ownership rules, and closeout pattern after this map. |
| 🗼 [WATCHTOWER.md](...projectSuccess/WATCHTOWER.md) | **Watch material external change.** Evidence stays in its wiki; qualifying signals enter the two-file radar, then CASTLE gates any test. |
| 🧠 `00-BRAIN` | See/change how the AI operates. `AGENT.md` is the universal OS every engine boots from; surface profiles (`CLAUDE.md` / `CODEX.md` / `ATLAS.md`) describe strengths and access; `HATS\` holds optional modes; 🏰 `CASTLE` (the command center — phases, skills, proof projects) lives here too, plus maps, flags, session logs. |
| ⭐ `01-NORTH_STAR` | **Read the durable star.** Load `CURRENT_STRATEGY.md` only for the active business vehicle, and the prep plan only for pre-semester sequencing. |
| 📚 `02-LIBRARY` | Grab reference by domain (`REF-…` folders). Also `.PROJECTS` (build docs), `00-SCHOOL` (course files), and `.raw ARCHIVE` (sources). `README.md` inside disambiguates the business/physics look-alikes. |
| ⚒️ `03-WIKIS` | Work the eight knowledge hubs: `SYSTEMS` (system dynamics + ISYE spine) · `PYTHON` (Python/CS stages) · `EDUCATION` (general KSU support — TCOM/ECON/ENGR) · `PHYSICS` (physics stages) · `BUSINESS` (offers, pricing, audit method, market research) · `TECHNOLOGY` (tech-adoption roadmap + applied technical reference) · `AI_AUTOMATION_SYSTEMS` (AI/agent research + `.ROOT` self-evolution proposals) · `REVENUE_LAB` (digital revenue evidence and tests). Each has a `HOW_TO_USE.md` inside. |
| 💼 `05-BUSINESS` | The money system: reusable templates, pricing, sanitized field lessons, and capability assets (case-study and proposal folders are ready and fill with real engagements — see its `README.md`). Active client-specific work stays in a separate client workspace outside `.ROOT`. |
| 📥 `77-INBOX` | Manual files dropped from outside `.ROOT`. Cleared every weekly review. |
| ✂️ `Clippings` | Automatic Obsidian web-clipping intake at the vault root. Cleared every weekly review. |
| 🗄️ `99-ARCHIVE` | Find anything retired. Nothing is ever deleted. |

Private inside the live vault: `88-JOURNAL` — no AI ever reads it.

---

## How Any AI Enters This System

Every agent, every model, same path — this is wired, not hoped for:

```
C:\Users\chris\.ROOT\CLAUDE.md or AGENTS.md (surface boot pointer)
  → C:\Users\chris\.ROOT\00-BRAIN\AGENT.md    (universal OS: star, school status, file safety, when to stop)
  → surface profile: CLAUDE.md / CODEX.md / ATLAS.md   (strengths + access notes)
  → CHRIS_CORE.md                 (who you are, how you work)
  → 01-NORTH_STAR\NORTH_STAR.md  (durable direction — every session)
  → current strategy / prep plan / Watchtower only when that question is active
  → optional HATS\ mode           (Operator / Educator / subject hat, if useful)
  → the section's own operating file
  → work. close clean. refresh NOW.md if the picture changed.
```

---

## The Color Language — One Vault, One Map (canonical definition)

`.ROOT` is one Obsidian vault with one graph.

### 🗺️ Open `.ROOT` as a vault = THE MAP (categorical)
Every section, and every wiki inside `03-WIKIS`, has its own color. One
glance = the shape of the whole system. Archives, old session logs, and the
inbox are filtered out of this graph.

| Color | Section |
|---|---|
| 🔴 Red | `00-BRAIN` — governance + AI operations |
| 🟤 Light brown | `00-BRAIN\CASTLE` — the command center |
| 🟡 Amber | `01-NORTH_STAR` — the star + reviews |
| 💜 Blue-violet | `...projectSuccess` — the watchtower |
| 🟠 Orange | `02-LIBRARY` — reference + projects + school file home |
| 🟢 Green | `BUSINESS` · 🟣 Purple `PYTHON` · 🟨 Gold `EDUCATION` · 💠 Cyan `PHYSICS` · 🟦 Indigo `TECHNOLOGY` · 🩷 Rose `AI_AUTOMATION_SYSTEMS` · 🟫 Tan `SYSTEMS` · 🟩 Teal `REVENUE_LAB` |
| 🩷 Magenta | `02-LIBRARY\00-SCHOOL` · 🌲 Dark green `05-BUSINESS` · ⚪ White `NOW.md` |

Exact hex values are machine-canon in `00-BRAIN\COLOR_MAP.yaml` (edit that
file, then run `00-BRAIN\scripts\build_graph_colors.py` — never hand-edit
`graph.json`). Palette approved by Chris July 8, 2026.

### 🎯 Finding "what's next" — property filters, not a second graph

Sequential ("what do I touch next") navigation now happens by filtering the
single graph's search box by property, instead of opening a separate colored
graph per wiki:

| Filter | Property | Means |
|---|---|---|
| `[timeline:now]` | `timeline: now` | **Do / learn / use this now** |
| `[timeline:next]` | `timeline: next` | **Next up** — on deck |
| `[timeline:later]` | `timeline: later` | **Later** — waiting its turn |
| `[timeline:parked]` | `timeline: parked` | **Parked** — deliberately inactive |
| `[timeline:reference]` | `timeline: reference` | **Use when needed** |
| `[timeline:log]` | `timeline: log` | **History** — not an action queue |

Combine with a path filter to stay inside one wiki, e.g.
`path:"03-WIKIS/PYTHON" [timeline:now]`. Static position is separate:
`[stage:2]` or `[stage:phase-1]`. Artifact condition uses `[status:active]`;
reference usefulness uses `[reference_priority:core]`. Topic discovery still
uses tags, such as `tag:#business`.

**Under the hood:** every new or updated file carries `type:` + one `timeline:`
property + topic tags. Optional `stage:`, `status:`, and `reference_priority:`
properties answer different questions. The full transition standard lives in
`00-BRAIN\WHERE_IT_GOES.md → Metadata Standard`.

---

## The Loop That Compounds

```
Morning     → castle refreshes NOW.md from yesterday's DAILY + handoffs — one priority, do it
Daily rep   → tracker / SQL / course work
Every task  → AI appends a 4-line block to the day's report (00-BRAIN\Session_Logs\DAILY_…)
Night       → Day Summary consolidates the blocks, then each AI used today writes its handoff (1–2/day)
Sources     → feed books/docs directly to the relevant 03-WIKIS hub — each refines its own domain
Business    → refined knowledge → BUSINESS templates → reusable/sanitized 05-BUSINESS assets
Horizon     → evidence home → qualifying Watchtower signal → castle gate → bounded test
Sunday      → weekly review + Engine Question (01-NORTH_STAR\Weekly Reviews)
Monthly     → weak-link check + each wiki's timeline/stage properties are reviewed
Quarterly   → THE RATCHET — outcomes review the vehicle; earned floors get raised
```

School is the spine; course files live at `02-LIBRARY\00-SCHOOL`, while the matching
wikis run the study path. CASTLE keeps the order. The wikis compound knowledge;
business work turns verified capability into value; `05-BUSINESS` preserves reusable
assets. The Watchtower keeps the system aware without steering it. The Ratchet lets
evidence improve the vehicle while the destination stays clear. **October 8, 2031 —
floor, not finish line.**

---

## Rules of the Realm (human version)

1. One file, one home. Manual unknowns → `77-INBOX`; automatic web clips → root `Clippings`; the weekly review files both.
2. Nothing gets deleted — it gets archived.
3. `88-JOURNAL` is yours alone.
4. Oct 5 – Nov 11, 2026 is a high-load school window. AI warns once if optional work threatens fixed commitments, recommends the smallest safe scope, then follows Chris's decision.
5. The skeleton is frozen. Content grows inside sections — we don't re-root.
6. Targets normally move at quarterlies. Chris may authorize a mid-cycle change after an impact review; AI does not move targets autonomously.

---
*AI entry: `C:\Users\chris\.ROOT\CLAUDE.md` or `AGENTS.md` -> `00-BRAIN\AGENT.md` -> surface profile (`CLAUDE.md` / `CODEX.md` / `ATLAS.md`) -> CHRIS_CORE.md. The star: `01-NORTH_STAR\NORTH_STAR.md`. G: is cloud backup only.*
