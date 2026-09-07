---
type: flags
timeline: now
status: active
tags: [governance]
updated: 2026-09-06
---

# SYSTEM_FLAGS — Live Safety and Improvement Register

Load for file-writing, system, review, security, backup, migration, or known-risk work. `SYSTEM_FLAGS_DETAIL.md` holds forensics; closed flags live in the monthly ledgers.

## Live prohibitions

1. **Preserve raw evidence.** Never deduplicate `raw` by hash and never write, rename, move, or delete inside any `raw\` folder. Duplicate names and empty captures may be the only evidence of source loss. Chris alone places files there.
2. **Protect private material.** Never read or write `88-JOURNAL\`. A child process can bypass application file rules, so every command and delegated boundary must preserve this rule explicitly.
3. **Treat bulk controls honestly.** The Claude Bash gate does not cover PowerShell and does not constrain every spawned process. Bulk work requires copy-first plus `00-BRAIN\scripts\safe_shell.sh`; never describe presence of a rule as measured enforcement.
4. **Keep universal methods reachable.** Situational procedures may load conditionally; a method or prohibition needed every time stays in the live branch that uses it.
5. **Protect conflict copies.** `(1)`-suffixed files under `raw`, archives, or inbox are not automatically debris. Inspect provenance before any archive proposal.

## Priority

| Priority | Required response |
|---|---|
| HIGH | Repair in the session raised; do not close with it unresolved. |
| MEDIUM | Address at the next relevant review. |
| LOW | Address at monthly review or when its owning system is already open. |

## Open flags

| # | Priority | Subject | Owner and next check |
|---|---|---|---|
| 105 | LOW | Drive holds a stale second `.ROOT` tree, making restoration ambiguous. | Chris: compare only after a real restore test, then choose archive/delete deliberately. |
| 101 | LOW | Claude's bulk matcher parses some command payload/prose as executable shape and also blocks read-only work. | Chris/Codex when `.claude` changes: fix payload blanking first; do not widen the script allowlist as a substitute. |
| 97 | MEDIUM | Five raw sources need recovery and the clipper can lose captures. | Chris: re-clip only after the clipper is fixed or retired. Monthly review. |
| 96 | MEDIUM | Spawned processes can bypass journal/raw tool guards. | Re-measure controls at any `.claude` change and monthly; preserve prohibition 2. |
| 93 | MEDIUM | HIGH-before-close remains prose rather than enforced behavior. | Design and review a warning/block mechanism before implementation. |
| 16 | LOW | Physics right-hand rule needs a physical anchor before torque instruction. | PHYSICS: Oct 12–18 learning window, using hands and a real wrench/breaker bar. |
| 69 | LOW | Byte-identical AIAS raw capture has an approved archive disposition AI cannot execute. | Chris moves it; AI leaves raw untouched. |

No HIGH flag is currently open. Full evidence, prior probes, and ownership history are in `SYSTEM_FLAGS_DETAIL.md`. Closed records: `Session_Logs\Closed Flags\CLOSED_FLAGS_2026-08.md` and `CLOSED_FLAGS_2026-09.md`.

## September runtime ruling

Flag #91 re-raised HIGH on September 6 because the September 5 TUTOR/VALUE decision failed to propagate through multiple live interfaces—the second propagation miss under its standing consequence. It closed the same session through the approved runtime rewrite, archive preservation, semantic reconciliation, boot validation, wiki lint, and CASTLE freshness checks. The 14-day runtime review measures usefulness, not whether the HIGH conflict remains open.
