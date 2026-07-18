---
type: source-summary
timeline: reference
reference_priority: supporting
tier: 1
source-role: support
tags: [source, ai-tooling]
---

# Claude Code Official Docs Pack (July 2026)

**Author / Organization**: Anthropic (official product documentation) + 1 customer case study
**Source type**: official docs (20 md files) | article (1) | report PDF (1, unparsed)
**URL or Drive location**: `00-BRAIN\CASTLE\raw\books\CLAUDE_FILES\` (raw, immutable) — canonical upstream: code.claude.com/docs
**Date accessed**: July 11, 2026 (Chris-directed castle ingest)
**Reliability tier**: 1 (vendor's own docs about its own tool — authoritative for mechanics; marketing-toned where it praises itself)

## Core Argument (3 sentences max)

The context window is the binding constraint of agentic AI sessions: everything always-loaded (CLAUDE.md files, memory, flags) taxes every request, and adherence *drops* as instruction files grow — "bloated CLAUDE.md files cause Claude to ignore your actual instructions."
The prescribed architecture is three tiers: a thin always-on layer (target **under 200 lines per file**; per-line test: *would removing this cause mistakes?*), an on-demand layer (skills / path-scoped rules / subagents) that loads only when relevant, and a deterministic layer (hooks, permission rules) for anything that must hold 100% of the time — because .md instructions are advisory, never enforcement.
Specificity is a virtue, not a cost ("run `npm test` before committing" beats "test your changes"); *volume* and *always-on loading* are what get punished.

## Claims This Source Supports

| Claim | Phase / skill it supports |
|---|---|
| Always-loaded instruction files should stay <200 lines; prune with "would removing this cause mistakes?" | .ROOT system maintenance (castle Wiki Sweep); Phase 1+ AI-operations skill |
| Rules that must never break (private folders, raw/ immutability) belong in hooks / permission deny rules, not prose | .ROOT governance hardening (Chris decision) |
| On-demand loading (skills, rules with `paths:`, subagents for research) is the escape valve for growing systems — HATS and section operating files already follow this pattern | validates .ROOT boot-chain architecture |
| Subdirectory CLAUDE.md files auto-load **in full** when files there are read — every hub CLAUDE.md is a per-session tax on work in that hub | wiki CLAUDE.md size budgets |
| History belongs in logs read tail-first, never in always-read live files | SYSTEM_FLAGS / NOW.md hygiene |
| Give the agent a verifiable check (test, script, diff) instead of watching it; demand evidence, not assertions | Phase 3 workflow-systems skill; tracker/dev workflow |
| Explore → plan → implement → commit; interview-then-spec for big features; fresh session per spec | AI-first build workflow (Phases 1–4) |
| Writer/Reviewer split sessions, adversarial review subagents, `claude -p` fan-out for batch work | Phase 3+ automation capability; future client delivery |
| CLAUDE.md = advisory context delivered as a user message, not system prompt — write it like code, prune it when behavior drifts | all instruction-file authoring |

## What to Ignore in This Source

- Enterprise/CI surface docs (GitHub Actions, GitLab, Enterprise Server, Slack, JetBrains, VS Code details) — inventory only; no current .ROOT use case. Revisit at Phase 3+ if client delivery needs CI automation.
- Thomson Reuters piece is a vendor marketing case study (treat as Tier 3): useful only as client-conversation vocabulary ("verification capacity," domain-expert-in-the-loop).
- Feature minutiae version-pinned to mid-2026 builds (exact token caps, flag names) — recheck upstream docs before relying on them; recency marker applies (claims current as of July 2026).

## Coverage note (honest accounting)

Read in full: Best_Practices, STORE_INSTRUCTIONS_AND_MEMORIES, EXPLORE_CLAUDE_CONTEXT_WINDOW, HOW_CLAUDE_CODE_WORKS, Extend_Claude_Code. Read in part: PROMPT_CACHING, COMMON_WORKFLOWS, MANAGE_SESSIONS, PERMISSION_MODES, Thomson Reuters article. Inventoried only: CLI/IDE/CI integration docs, PROMPT_LIBRARY, SECURITY_GUIDANCE_PLUGIN, CODE_REVIEW. **Unparsed:** `Anthropic-enterprise-ebook-digital.pdf` (queued; route per big-source rule if ever needed). **Raw defect:** `EXPLORE_THE_.CLAUDE_DIRECTORY.md` is byte-identical to `HOW_CLAUDE_CODE_WORKS.md` (MD5 match) — mis-saved duplicate, flagged (SYSTEM_FLAGS #63), Chris's call per raw immutability.

## Applied

This ingest drove the July 11, 2026 system self-review:
`99-ARCHIVE\ARCHIVED_2026-07-12_SESSION_LOG_CLAUDE_DOCS_SYSTEM_REVIEW_2026-07-11.md`
(verdict: architecture sound, history-creep in always-read files was the real bloat;
SYSTEM_FLAGS closed-table archived the same session).

## Entered in [[source-map]]: yes
