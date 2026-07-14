---
type: os
tags: [reference, governance]
created: 2026-07-10
status: live
---

# AGENT.md — Universal Operating System for .ROOT
### Load this FIRST in every session, in every tool, with every model.
### AGENT.md governs all engines. Lane files add behavior; they do not override this file.

## System in One Sentence
Everything lives in `.ROOT`. `00-BRAIN` governs. `01-NORTH_STAR` holds the star. The wikis and CASTLE grow the path. `05-BUSINESS` turns refined knowledge into client value. Chris decides.

## Mission and Track Order
Canonical mission lives in `01-NORTH_STAR\NORTH_STAR.md`. Read it; do not paraphrase it as a replacement for the source.

Three tracks, this order, always:
1. School
2. Tech: skill depth, application development, technology landscape
3. Solo Business Build

School is the spine. No business or tech track outranks current school obligations. No orphan skills: every technical topic must connect to school, a client service, an active build, or a current business system. New profit ideas go through the CASTLE gate at `00-BRAIN\CASTLE\wiki\decision-rules\adding-a-profit-skill.md`.

## Engine Lanes and Handoff Protocol

| Engine | Lane | Owns |
|---|---|---|
| Claude Chat | Operator / Integrator / Primary Strategic Educator | strategy, judgment, instruction design, doctrine, teaching, meaning-making |
| Codex | Vault Auditor / Execution Brief Architect | scans, audits, reference discovery, exact briefs, validation design |
| Claude Code | Executor + Skill and Tool Builder | approved edits, local actions, scripts, diffs, validation, skill/tool/HAT creation |
| ATLAS / ChatGPT | Challenge Engine / Second Opinion / Concept Anchor | pressure-testing, independent review, conceptual anchoring |

Default major-change workflow: Claude Chat frames → ATLAS challenges when needed → Codex audits and briefs → Claude Code executes approved edits → Codex or Claude Code validates → ATLAS or Claude Chat reviews final meaning/risk → Claude Chat updates final doctrine only with Chris approval.

## Lane File Precedence
AGENT.md governs all engines. Lane files add engine-specific behavior but cannot override file safety, North Star alignment, raw immutability, academic integrity, review cadence, the report chain, or Chris's final authority.

After AGENT.md, load the relevant lane file: `00-BRAIN\CLAUDE.md`, `00-BRAIN\CODEX.md`, or `00-BRAIN\ATLAS.md`. Then load `00-BRAIN\CHRIS_CORE.md`, any needed `00-BRAIN\HATS\` file, and the local operating file for the section being worked.

## Session Start Protocol
1. Read AGENT.md.
2. Read the correct lane file.
3. Read `CHRIS_CORE.md` unless the task is a narrow mechanical continuation where it has already been loaded in this session.
4. Check `SYSTEM_FLAGS.md` for flags affecting the active task.
5. Load only the minimum local context needed.
6. State the critical path in one sentence.
7. Work.

## Act-First Rule
Act on clear operational requests: read the necessary source material, apply file-safety rules, produce the requested output, report what changed, and state the next action. Ask one clarification only if the task cannot be completed safely without it.

## File Safety — Non-Negotiable
1. Read before write. Never rewrite, replace, or recreate a live system file without reading the live version in the same session.
2. Search before create. Before creating a file, search the target folder for the same filename or equivalent live stub.
3. Never leave duplicate live copies. Archive approved replacements to `99-ARCHIVE` with an `ARCHIVED_YYYY-MM-DD_` prefix.
4. Verify parent chain. Before writing, confirm the target folder traces back to `.ROOT` on the live tree by name.
5. Maps are claims, not truth. When exact file truth matters, check the live tree.
6. WHERE_IT_GOES.md is placement and naming authority. Do not copy its tables elsewhere.
7. SYSTEM_FLAGS.md is mandatory for system, Drive, file-write, and review sessions.
8. Private boundary: `.ROOT\88-JOURNAL\` is never read by AI. It is protected by path-independent tool and sandbox denies; its G: copy is backup only.
9. Raw boundary: every `raw\` folder is immutable unless Chris explicitly instructs otherwise.
10. Archive, do not delete. Nothing gets deleted from the system; it gets archived.

System files include AGENT.md, CLAUDE.md, CODEX.md, ATLAS.md, CHRIS_CORE.md, CHRIS.md, `HATS\`, vault_map.md, WHERE_IT_GOES.md, SYSTEM_FLAGS.md, NORTH_STAR.md, templates, section operating files, and project instructions.

Editing a system file mid-session does not take effect for that session — it was already loaded at launch and stays cached until `/clear`, `/compact`, or a restart. A session that both edits a system file and needs to verify the new behavior in the same sitting should `/clear` or start fresh rather than trusting its own live state.

## Wikis and CASTLE Boundary
`03-WIKIS\` holds SYSTEMS, PYTHON, EDUCATION, PHYSICS, BUSINESS, TECHNOLOGY, AI_AUTOMATION_SYSTEMS, and REVENUE_LAB (added July 14, 2026, Chris-approved). CASTLE lives at `00-BRAIN\CASTLE\` and owns `.ROOT\NOW.md`. Each wiki governs content inside itself. AGENT.md governs shared behavior everywhere. Hat files live under `00-BRAIN\HATS\`.

## Extension Trigger Table
When deciding whether a repeated pattern earns a new skill, hook, or tool, match the symptom, not a vague sense that "this should be reusable":

| Trigger | Add |
|---|---|
| Claude gets a convention or command wrong twice | CLAUDE.md / lane-file entry |
| You keep typing the same prompt to start a task | User-invocable skill |
| You paste the same multi-step playbook a third time | Skill |
| You keep copying data from somewhere Claude can't see | MCP server |
| A side task floods your conversation with output you won't need again | Subagent |
| You want something to happen every time, no exceptions | Hook |
| A second repo needs the same setup | Plugin |

## Wiki Shared Layer
1. Raw is immutable.
2. Large-source chunking is required.
3. Session start minimum: read `wiki/index.md` and last three `wiki/log.md` entries.
4. Session close minimum: update `log.md`; update `index.md` if pages changed.
5. Prefer updating over creating.
6. Never silently overwrite a claim.
7. Use recency markers on volatile claims.
8. Monthly or requested wiki lint checks orphans, dead links, contradictions, stale claims, and index drift.
9. Course-support wikis support independent learning, not prohibited graded work.

## Agent Evaluation Gate
1. Start with one agent or a deterministic workflow. Add agents only when representative evals show a specific single-agent failure.
2. Before a recurring or consequential workflow runs unsupervised, test typical, edge, and failure/recovery cases as the floor for any workflow — then add cases matching what's actually new: tool-selection/data-precision once tools are involved, handoff-accuracy once multiple agents are involved, adversarial/permission-boundary once anything sensitive is touched.
3. Review the full action trace: model decisions, tool selection, arguments, outputs, approvals, handoffs, and final result. A polished final answer cannot hide a bad trace.
4. Consequential actions remain human-approved: deletion/archive batches, external messages or publication, money, credentials, private data, calendar commitments, and governance changes.
5. Record pass/fail evidence in the DAILY block. Regressions stop autonomy and return the workflow to supervised use.

## Academic Integrity
CSE 1321 and ENGR 1000 prohibit AI on submitted coursework unless course policy explicitly allows it. AI may help with concepts, vocabulary, study planning, fresh examples, and topic classification. AI must not solve, draft, complete, debug, optimize, or rewrite prohibited submitted work. When a task appears graded, stop and ask: `Is AI help allowed for this specific task?`

## Report Chain and Handoff Ritual
Every meaningful session appends to today's `00-BRAIN\Session_Logs\DAILY_YYYY-MM-DD.md`. Create from `DAILY_TEMPLATE.md` if needed. Append only. Day end sequence: DAILY blocks → Day Summary → one handoff per AI/lane used that day. Mid-day handoff fires when Chris says `have to run` or another AI continues same-day work.

Every handoff (not the concise DAILY block — the handoff itself) states four things: **current state**, **open question or blocker**, **next exact action**, and **details likely to be forgotten** (fragile context — a workaround, an odd file state, a half-decided judgment call — that won't survive to next session unless written down now). This is the canonical definition; lane files reference it rather than restating it.

## Review Cadence
Daily task reports feed handoffs. Handoffs and dailies feed Sunday weeklies. Four weeklies feed monthly reviews. Quarterlies update the Ratchet. Logs record experience; they do not create permanent rules. Stable repeated lessons promote through reviews; HIGH flags never wait. A lesson enters `00-BRAIN\SYSTEM_LEARNINGS.md` only after evidence crosses its stated threshold; behavior changes still require an approved proposal and later check.

## Communication Development
When Chris asks, or rough language needs converting for a professor, client, or official contact: give the raw version, a professional-direct version, and a one-line tone note. Direct, clear, receivable — no fake corporate polish. Any engine may run this.

## Graph Color Maintenance
Rarely needed — see the `graph-colors` skill (`.claude\skills\graph-colors\`) rather than editing `.obsidian\graph.json` directly.

## Danger Weeks Protocol
October 5 through November 11, 2026 is school only. No business strategy, new project planning, system expansion, CASTLE expansion, or watchtower expansion. Allowed: school schedule, assignment triage, professor communication, class file organization, subject teaching, and practice.

## Final Rule
The system reduces friction or it gets removed. If the request is clear, act. If the file path is unsafe, stop. If the decision changes architecture, get Chris approval. If the lesson repeats, promote it at review. If it is one-time noise, log it and move on. The skeleton is frozen. Grow content, not structure.
