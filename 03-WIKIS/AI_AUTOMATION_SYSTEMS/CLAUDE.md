---
type: os
tags: [ai-automation]
created: 2026-07-08
status: live
timeline: reference
---

# CLAUDE.md — AI & Automation Systems Wiki OS

## Purpose

Two research jobs, one wiki:

1. **AI tooling and agent-pattern research generally** — what's out there,
   agent architectures, prompt/automation techniques, MCP servers, workflow
   patterns worth knowing.
2. **Self-evolution research on `.ROOT` itself** — this system. Study how
   `.ROOT` operates, notice friction or drift, and draft improvement
   proposals.

The controlling question:

> What AI/automation pattern is worth knowing, and does `.ROOT` itself need to
> change to use it well?

Both jobs serve the same direction. The Technology track needs a practitioner
who knows what AI/automation patterns are worth building into real work. The
Advisor-Builder business needs someone who can enter an unfamiliar operation,
identify where AI creates measurable value, and implement the right system.
This wiki is where that knowledge accumulates before it becomes client-facing
capability — and where `.ROOT` improves through its own use.

## Current State

`wiki/index.md` — live inventory of every research page and proposal, with
status markers. `wiki/log.md` — recent session activity and intake summary.
Open these two before starting any research session; do not estimate coverage
from page names or file counts here — they drift.

## Division of Labor — Read This First

This wiki **researches and proposes**. `00-BRAIN\CASTLE` **reviews, maintains,
and keeps things legible** — the same eyes-not-hands split already used for
the Watchtower (`...projectSuccess`) and the castle's profit-skill gate.

Concretely:

- This wiki may draft a proposal for a governance-file change (e.g., a better
  session-boot pattern, a new tag convention, a hook idea).
- This wiki does **not** unilaterally rewrite `00-BRAIN` governance files
  (`AGENT.md`, `WHERE_IT_GOES.md`, hats, etc.).
- Stable, repeated findings hand off to the existing review cadence already
  defined in `AGENT.md` (handoff → weekly → monthly → quarterly) for actual
  promotion into core files. Chris approves structural/governance changes,
  same as everywhere else in the system.

## System Boundary

- `03-WIKIS\TECHNOLOGY` is the sibling wiki for the broader tech-adoption
  roadmap (tool categories generally, not AI-specific). This wiki is the
  narrower AI/agent/automation slice, plus the self-evolution charter that
  TECHNOLOGY doesn't carry. TECHNOLOGY's `ai-and-llm/` subfolder is closed
  inherited reference (July 9, 2026) — new AI/LLM/agent research routes
  HERE, not there.
- `03-WIKIS\TECHNOLOGY` and `03-WIKIS\PYTHON` hold applied technical reference
  (Python, SQL, APIs, automation tooling already in active use — inherited
  from FORGE's retirement, July 7, 2026) — this wiki is landscape research
  and system-improvement proposals, not applied technique.
- `02-LIBRARY\REF-AI-AUTOMATION\` holds existing prompt libraries and
  Obsidian-automation notes (`LLM_WIKI_PATTERN_karpathy.md`,
  `PROMPTS for AIchat\`, etc.) — this wiki may draw on that material as a
  source but nothing there was moved; it stays a `02-LIBRARY` reference
  domain per `WHERE_IT_GOES.md`.

## Folder Structure

```text
raw/          # AI/automation articles, tool docs, pattern references — immutable
wiki/
  index.md
  log.md
  proposals/    # drafted improvement proposals for .ROOT, pending castle/Chris review
```

Build out further structure only as research accumulates — do not pre-build
empty category folders.

## Shared Wiki Rules

The shared layer for all `03-WIKIS` hubs — raw/ immutability, large-source
chunking, session start/close minimums, update-over-create, contradiction
flagging, recency markers, and the lint pass — lives in
`00-BRAIN\AGENT.md § Wiki Shared Layer`. One copy, zero drift. This file
carries only this wiki's own rules.

## Proposal Format

Every proposal in `wiki/proposals/` must state: the friction or drift observed,
the specific file(s) it would touch, the proposed change, why it's better than
the status quo, and its risk/blast radius — plus a **Post-Change Check**:
expected behavior after the change, evidence that would show improvement **or
regression**, and a `check_at` date tied to real usage (not calendar
convenience). At the check date, record the observed **Outcome** with an
evidence link and a **keep / modify / revert Verdict**. An applied proposal
with no recorded outcome is not yet proven (added 2026-07-15; all previously
approved proposals were retrofitted the same day). Proposals are drafts — they
become real only when Chris (or the castle's review cadence) approves them into
the target file.

## Watchtower Handoff

External AI/agent changes stay researched here and reach
`...projectSuccess\radar.md` only when verified and material. Internal `.ROOT`
friction follows the proposal/SYSTEM_FLAGS path instead. Every promoted signal must
name its evidence page, affected strategy assumption/system choice, consequence or
bounded test, and review trigger.

## Final Operating Principle

Research and propose, never unilaterally govern. This wiki's value is noticing
what the rest of the system can't see about itself — but Chris and the
existing review cadence still decide what becomes permanent.

