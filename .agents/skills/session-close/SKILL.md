---
name: session-close
description: Run the .ROOT session-close ritual — DAILY block append, wiki log updates, NOW.md refresh check, handoff decision. Use at the end of any meaningful work session, or when Chris says "close the session", "wrap up", or "have to run".
---

# Session Close — .ROOT Ritual

Execute the close sequence from AGENT.md § Report Chain + CASTLE
OPERATIONS.md § Session Close. Read those two sections if not already
loaded this session.

## Steps

1. **DAILY block** — append a 4-line block to today's
   `00-BRAIN\Session_Logs\DAILY_YYYY-MM-DD.md` (create from
   `DAILY_TEMPLATE.md` if missing). Format per template: time/role —
   what was done, files touched, next action.
2. **Wiki close** — if any wiki was touched: append its `wiki/log.md`,
   update its `index.md` if pages changed, update
   `current-position.md` if progress moved.
3. **NOW.md check** — if the session changed today's picture (priority
   done, project status moved, new countdown), refresh `.ROOT\NOW.md`
   (castle-owned): date header, single priority, statuses, countdowns.
   A stale NOW.md is a broken castle.
4. **Backstop** — if yesterday's DAILY has no Day Summary, write it
   now (the castle backstops missed consolidation).
5. **Handoff decision** — write a handoff to `Session_Logs`
   (`HANDOFF_MMDD_WHO.md`) ONLY if: day end with meaningful work,
   Chris said "have to run", or another AI continues same-day work.
   Skip on quick-answer days.
6. **Close line** — state in one sentence what changed and the single
   next action.

## Rules

- Append-only on DAILY files. Never rewrite earlier blocks.
- Mid-day handoff only on "have to run" / same-day AI switch.
- If a HIGH flag was raised this session, it must be fixed or
  explicitly handed to Chris before closing (SYSTEM_FLAGS.md rule).
