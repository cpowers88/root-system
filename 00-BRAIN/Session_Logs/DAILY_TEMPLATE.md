---
type: template
tags: [reference, governance]
---

# DAILY — YYYY-MM-DD
### One file per day: `DAILY_YYYY-MM-DD.md` → `00-BRAIN\Session_Logs\`
### Every session appends. Never rewrite earlier blocks — append only, like the castle log.
### Why it exists: task-level truth feeds the Day Summary → weekly review → evolution loop. A day with work but no DAILY file is a broken report chain.

---

## Task Blocks

Append one block **when the session starts a task, switches task/section, and at session close**.
Four lines. If it takes more than a minute to write, it's too long.

```
### HH:MM — [Hat] — [section: task]
- Did: [one line — what actually happened]
- Files: [files touched, or "none"]
- Result: shipped / partial / blocked / decision-needed
- Next: [one line — the single next action for this task]
```

Rules:
- **Switch = block.** Moving from PYTHON wiki to PHYSICS wiki mid-session = close the
  first task with a block, open the next. Three tasks = three or more blocks.
- **Blocked is a result, not a failure.** Name what blocks it — that line is what the
  Day Summary and weekly review hunt for.
- A DAILY block does not replace a handoff. Handoffs still fire per AGENT.md when
  continuity matters; the DAILY block is the lightweight always-on layer beneath them.

---

## Day Summary

Appended once by the day's **last session** — or by the next morning's NOW.md refresh
if the last session missed it. Consolidate the blocks above; do not re-narrate them.

**Day-end order (Chris's rule, July 9, 2026):** Day Summary first, THEN each AI/hat
used today writes its end-of-day handoff (`HANDOFF_MMDD_WHO.md`, one per AI — usually
1–2 per day). The handoff never repeats these blocks; it carries state, terms, review,
and the message to the other AI.

```
## Day Summary — YYYY-MM-DD
- Moved: [what actually advanced today, 1-3 lines]
- Blocked: [anything still stuck, or "nothing"]
- Drift check: [did today's work point at the North Star? one honest line]
- Tomorrow: [the single priority — this line seeds NOW.md]
- Feeds weekly: [anything the Sunday review must see, or "routine"]
```

---
*Template. Live files: `DAILY_YYYY-MM-DD.md` beside this file. Naming authority: WHERE_IT_GOES.md.*
*Wired into session close: AGENT.md + CASTLE\OPERATIONS.md (July 9, 2026).*

