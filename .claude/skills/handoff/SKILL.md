---
name: handoff
description: Write a `.ROOT` handoff document (current state, open question/blocker, next exact action, details likely to be forgotten). Use for a meaningful day end, a same-day AI-surface switch, or "have to run."
---

# Write a `.ROOT` Handoff

1. Read the handoff rule in `00-BRAIN\AGENT.md` (Report Chain and Handoff
   Ritual) first — it is the canonical spec; this skill only executes it.
2. Confirm a trigger actually applies: meaningful day end, another AI surface
   continuing the work same-day, or "have to run." Not every session gets a
   handoff — only these three.
3. Do not restate the day's factual record. Point to
   `00-BRAIN\Session_Logs\DAILY_YYYY-MM-DD.md` (task blocks + Day Summary)
   instead of duplicating it.
4. Write exactly four fields:
   - **Current state** — concrete enough that a fresh agent doesn't have to
     re-derive it.
   - **Open question/blocker** — what's stuck and why, with the evidence
     needed to act on it immediately (error text, flag number, exact file).
   - **Next exact action** — the single next move, not a menu of options.
   - **Details likely to be forgotten** — anything a fresh agent would
     otherwise silently drop or re-verify from scratch (intentional
     exclusions, in-progress-not-abandoned items, explicitly skipped steps).
5. Save as `00-BRAIN\Session_Logs\HANDOFF_MMDD_WHO.md` (numeric MMDD, not a
   month name). One handoff per AI surface used that day.
6. Frontmatter: `type: handoff`, `timeline: log`, topic tags only if useful.
7. Close with `*Written by:*` and `*Next session priority:*` — one sentence
   naming the single most important next thing.
