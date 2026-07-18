---
name: session-close
description: Run `.ROOT` session close, including the DAILY append, wiki/CASTLE log updates, cockpit freshness check, and handoff decision. Use when meaningful work ends or Chris says to close, wrap up, switch AI, or leave.
---

# Close a `.ROOT` Session

1. Read the close rules in `00-BRAIN\AGENT.md` and
   `00-BRAIN\CASTLE\OPERATIONS.md`.
2. Append a concise block to today's DAILY: outcome, evidence/files, decision or
   fragile detail, and next exact action. Create from the template if absent.
3. If a wiki changed, append its log and update index/current-position only when
   reality moved.
4. Refresh `NOW.md` only when the live picture changed: date, starting action,
   fixed school item, technology rep, business/system item, soft boundary,
   status, or countdown.
5. Backstop a missing prior-day Day Summary when required.
6. Write a four-field handoff only for meaningful day end, same-day AI switch,
   or “have to run.”
7. After governance, system-script, settings, metadata-policy, or shared-skill
   changes, run `python 00-BRAIN\scripts\root_health.py`. Stop on `BLOCKER` and
   report reviewed debt without calling it clean. Ordinary learning sessions do
   not require this system-wide gate — unless the session created any new `.md`
   file anywhere in `.ROOT`; a new file requires frontmatter at creation
   (`WHERE_IT_GOES.md` Metadata Standard), so a session that created one runs
   the gate before close and resolves any new frontmatter finding it raised.
   (Added July 18, 2026 after the second new-file frontmatter regression in
   three days; check at the July 26 governance-drift weekly sweep.)
8. State the outcome and next exact action.

DAILY files are append-only. Resolve or explicitly hand off every HIGH flag.
