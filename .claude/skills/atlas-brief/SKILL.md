---
name: atlas-brief
description: Generate a paste-ready ATLAS/ChatGPT context brief from the live system state (NOW.md + latest DAILY + the decision at hand). Use when Chris wants ATLAS to pressure-test a decision, architecture change, or Codex brief.
---

# ATLAS Brief Generator

ATLAS cannot read `.ROOT`. Claude generates the paste-in brief from
the template in `00-BRAIN\ATLAS.md § Part 2` — never from memory.

## Steps

1. Read `00-BRAIN\ATLAS.md` (role definition + the exact template).
2. Fill the bracketed fields from live sources:
   - **Current phase** → `.ROOT\NOW.md` (priority, countdowns) +
     `00-BRAIN\CASTLE\wiki\current-position.md` (phase/baseline)
   - **Current system state** → today's
     `00-BRAIN\Session_Logs\DAILY_YYYY-MM-DD.md` + the specific
     decision/change Chris wants challenged (ask one question if the
     decision itself is unclear — that field cannot be guessed)
3. Keep every fixed section of the template verbatim (identity, North
   Star, four-engine split, "your job is to challenge, not confirm").
4. Output the finished brief in ONE fenced code block, ready to paste
   into ChatGPT. Nothing else around it except a one-line reminder.
5. Log one DAILY line: "ATLAS brief generated for [topic]."

## After the ATLAS session

When Chris pastes ATLAS's answer back: significant findings → DAILY
block; architecture-level findings → SYSTEM_FLAGS.md entry or a
reviewed doctrine proposal (per ATLAS.md Part 1). ATLAS output always
feeds back through Claude — it never edits the vault.
