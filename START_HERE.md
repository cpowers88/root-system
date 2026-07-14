---
type: map
tags: [reference]
---

# START HERE — The Whole System on One Screen
### For Chris Powers, aka theinternet. Updated July 11, 2026 (North Star + school relocation sync). If anything here confuses you, that's a bug — tell the AI.

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
| 🗼 `...projectSuccess` | **Watch the horizon.** The radar (trends, industry moves, opportunities). Swept weekly; feeds the castle gate. |
| 🧠 `00-BRAIN` | See/change how the AI operates. `AGENT.md` is the universal OS every engine boots from; lane files (`CLAUDE.md` / `CODEX.md` / `ATLAS.md`) define engine behavior; `HATS\` holds the roles; 🏰 `CASTLE` (the command center — phases, skills, proof projects) lives here too, plus maps, flags, session logs. |
| ⭐ `01-NORTH_STAR` | Read the star. `NORTH_STAR.md` (the controlling document — identity, ratchet, engine, tracks), skill gaps, weekly/monthly reviews. |
| 📚 `02-LIBRARY` | Grab reference by domain. Also `.PROJECTS` (build docs), `00-SCHOOL` (course files), and `.raw ARCHIVE` (sources). |
| ⚒️ `03-WIKIS` | Work the seven knowledge hubs: `SYSTEMS` (system dynamics + ISYE spine) · `PYTHON` (Python/CS stages) · `EDUCATION` (general KSU support — TCOM/ECON/ENGR) · `PHYSICS` (physics stages) · `BUSINESS` (offers, pricing, audit method, market research) · `TECHNOLOGY` (tech-adoption roadmap + applied technical reference) · `AI_AUTOMATION_SYSTEMS` (AI/agent research + `.ROOT` self-evolution proposals). Each has a `HOW_TO_USE.md` inside. |
| 💼 `05-BUSINESS` | The money system: audit templates, field notes, case studies, pricing, proposals. Real client artifacts land here. |
| 📥 `77-INBOX` | Dump quick captures. Cleared every weekly review. |
| 🗄️ `99-ARCHIVE` | Find anything retired. Nothing is ever deleted. |

Private inside the live vault: `88-JOURNAL` — no AI ever reads it.

---

## How Any AI Enters This System

Every agent, every model, same path — this is wired, not hoped for:

```
C:\Users\chris\.ROOT\CLAUDE.md (router, auto-loads)
  → C:\Users\chris\.ROOT\00-BRAIN\AGENT.md    (universal OS: star, school status, file safety, when to stop)
  → lane file: CLAUDE.md / CODEX.md / ATLAS.md   (engine behavior)
  → CHRIS_CORE.md                 (who you are, how you work)
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
| 🟢 Green | `BUSINESS` · 🟣 Purple `PYTHON` · 🟨 Gold `EDUCATION` · 💠 Cyan `PHYSICS` · 🟦 Indigo `TECHNOLOGY` · 🩷 Rose `AI_AUTOMATION_SYSTEMS` · 🟫 Tan `SYSTEMS` |
| 🩷 Magenta | `02-LIBRARY\00-SCHOOL` · 🌲 Dark green `05-BUSINESS` · ⚪ White `NOW.md` |

Exact hex values are machine-canon in `00-BRAIN\COLOR_MAP.yaml` (edit that
file, then run `00-BRAIN\scripts\build_graph_colors.py` — never hand-edit
`graph.json`). Palette approved by Chris July 8, 2026.

### 🎯 Finding "what's next" — tag filters, not a second graph

Sequential ("what do I touch next") navigation now happens by filtering the
single graph's search box by tag, instead of opening a separate colored
graph per wiki:

| Filter | Tags | Means |
|---|---|---|
| `tag:#now` | `priority/now` · current stages · `phase-1` | **Do / learn / use this now** |
| `tag:#next` | `priority/next` · next stages · `phase-2` | **Next up** — on deck |
| `tag:#later` | `priority/later` · later stages · `phase-3` | **Later** — waiting its turn |
| `tag:#parked` | parked-advanced · `phase-4` | **Parked** — deliberately not now |
| — | `phase-5` | **Horizon** — years out |
| `tag:#reference` | `phase-all` · glossaries, templates | **Always-on reference** |

Combine with a path filter to stay inside one wiki, e.g.
`path:"03-WIKIS/PYTHON" tag:#now`. Clear a stage → the AI moves the timeline
tag forward → your live edge moves with you, same idea as before, just
filtered instead of separately colored.

**Under the hood:** every file carries `type:` + one timeline tag + topic
tags (the full standard lives in `00-BRAIN\WHERE_IT_GOES.md → Tag
Standard`). Filter any view by tag: `tag:#now`, `tag:#business`, `tag:#school`.

---

## The Loop That Compounds

```
Morning     → castle refreshes NOW.md from yesterday's DAILY + handoffs — one priority, do it
Daily rep   → tracker / SQL / course work
Every task  → AI appends a 4-line block to the day's report (00-BRAIN\Session_Logs\DAILY_…)
Night       → Day Summary consolidates the blocks, then each AI used today writes its handoff (1–2/day)
Sources     → feed books/docs directly to the relevant 03-WIKIS hub — each refines its own domain
Business    → refined knowledge → BUSINESS templates → 05-BUSINESS client assets
Horizon     → weekly Watchtower sweep — signals route through the castle gate
Sunday      → weekly review + Engine Question (01-NORTH_STAR\Weekly Reviews)
Monthly     → weak-link check + every wiki's timeline tags move forward
Quarterly   → THE RATCHET — floors that fell early get raised
```

School is the spine; course files live at `02-LIBRARY\00-SCHOOL`, while the matching wikis run the study path. The castle keeps the order. The wikis compound
the knowledge, each in its own domain. The business wiki turns it into offers. 05-BUSINESS
turns offers into money. The watchtower keeps you ahead. The ratchet
makes sure the target never stops moving. **October 8, 2031 — floor, not finish line.**

---

## Rules of the Realm (human version)

1. One file, one home. Not sure? → `77-INBOX`; the weekly review files it.
2. Nothing gets deleted — it gets archived.
3. `88-JOURNAL` is yours alone.
4. Oct 5 – Nov 11, 2026 is a high-load school window. AI warns once if optional work threatens fixed commitments, recommends the smallest safe scope, then follows Chris's decision.
5. The skeleton is frozen. Content grows inside sections — we don't re-root.
6. Targets normally move at quarterlies. Chris may authorize a mid-cycle change after an impact review; AI does not move targets autonomously.

---
*AI entry: `C:\Users\chris\.ROOT\CLAUDE.md` or `AGENTS.md` -> `00-BRAIN\AGENT.md` -> surface profile (`CLAUDE.md` / `CODEX.md` / `ATLAS.md`) -> CHRIS_CORE.md. The star: `01-NORTH_STAR\NORTH_STAR.md`. G: is cloud backup only.*
