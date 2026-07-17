---
type: report
timeline: now
tags: [governance, codex, configuration, audit, skills]
created: 2026-07-17
status: draft-for-review
---

# Codex Instruction and Skill Optimization Audit — July 17, 2026

**Scope:** Codex's effective instruction/configuration stack on this machine,
with emphasis on `C:\Users\chris\.codex`, `.ROOT` discovery, the recurring
"2%" skills warning, and alignment with `01-NORTH_STAR\NORTH_STAR.md` and the
`.ROOT` Capability Contract. This is a report-only audit. No Codex settings,
plugins, rules, trust grants, skills, or governance files were changed.

**Evidence used:** live filesystem state; the current session's surfaced
capabilities; `.ROOT` governance; Claude's same-day
`AI_SURFACE_CONFIG_AUDIT_2026-07-17.md`; and a fresh July 17 fetch of the
official Codex manual through the installed OpenAI documentation helper. The
manual's relevant source pages are [Build skills](https://learn.chatgpt.com/docs/build-skills),
[Plugins](https://learn.chatgpt.com/docs/plugins),
[Configuration](https://learn.chatgpt.com/docs/config-file/config-basic), and
[`AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

---

## 1. Executive Verdict

The `.ROOT` governance design is fundamentally sound. The failure is at the
entry boundary, not in the North Star or the boot-chain architecture.

Two conditions are interacting:

1. **This Codex session started at `C:\Users\chris`, one directory above
   `.ROOT`.** Codex walks upward from the current working directory to discover
   project configuration and instructions; it does not walk down into child
   folders. Therefore this session did **not** automatically load:
   - `C:\Users\chris\.ROOT\AGENTS.md`;
   - `C:\Users\chris\.ROOT\.codex\config.toml`; or
   - the five repo skills under `C:\Users\chris\.ROOT\.agents\skills`.

   Those files became active only because Chris explicitly named `.ROOT` and
   Codex manually read them during this audit. A normal chat started from the
   home folder has no automatic `.ROOT` orientation.

2. **The current runtime advertises 102 installed skills before any `.ROOT`
   repo skills are added.** Ninety-seven come from enabled plugins and five are
   Codex system skills. Vercel alone contributes 47 skills; Figma contributes
   11. The active plugin skills contain at least 26,764 characters of one-line
   descriptions and about 1.10 MB of full `SKILL.md` content on disk.

The recurring "2%" message is therefore explained exactly. Official Codex
behavior caps the initial skill list at **2% of the model context window**, or
**8,000 characters when the context size is unknown**. Codex shortens
descriptions first and may omit some skills from the initial list, then shows a
warning. This does **not** mean full skill instructions are cut to 2%, and it
does not mean the model has permanently lost those capabilities. When a skill
is explicitly selected or successfully matched, Codex reads the full
`SKILL.md`.

**Best path forward:** open `.ROOT` as the Codex project, then curate plugins
to a small always-on working set and turn specialized bundles on only when the
task needs them. After that, install a tiny global `~/.codex/AGENTS.md` safety
router and prune obsolete trust/rule entries. Do not copy the North Star or the
full `.ROOT` operating system into global Codex instructions.

---

## 2. What Is Actually Instructing Codex

Codex receives multiple layers. They should not be treated as one file.

| Precedence / scope | Source | Current effect |
|---|---|---|
| OpenAI runtime policy | Product system/developer instructions, tool contracts, permission profile, environment | Always active; not authored in `.codex` and not a `.ROOT` file |
| User-wide config | `C:\Users\chris\.codex\config.toml` | Active in every local Codex session |
| User-wide guidance | `C:\Users\chris\.codex\AGENTS.md` | Active but empty (0 bytes), so it contributes no guidance |
| User-wide command rules | `C:\Users\chris\.codex\rules\default.rules` | 132 allow rules; enforcement/approval memory, not prose governance |
| Installed systems/plugins | `.codex\skills\.system` and `.codex\plugins\cache` | Supplies the current 102-skill discovery catalog plus tools/connectors from enabled plugins |
| Project config | `[project root]\.codex\config.toml` | Loads only when the session is inside a trusted project and the file lies on the upward discovery path |
| Project guidance | `[project root]\AGENTS.md` plus closer nested `AGENTS.md` files | Loads only for the selected project/path; closer guidance wins |
| Repo skills | `.agents\skills` from CWD upward to repo root | Available only when the session is launched inside that repo/path |
| Task prompt and files read during work | Chris's request plus manually loaded `.ROOT` files | Active for this thread; does not repair future session discovery |

### What loaded automatically in this session

Because the CWD was `C:\Users\chris`:

- global `.codex\config.toml` — yes;
- global `.codex\AGENTS.md` — yes, but empty;
- installed plugin/system skills — yes, 102 surfaced;
- `.ROOT\AGENTS.md` — no automatic discovery;
- `.ROOT\.codex\config.toml` — no automatic discovery;
- `.ROOT\.agents\skills` — no automatic discovery;
- `.ROOT` North Star/governance — no, until manually read for this request.

### What loads when `.ROOT` is opened correctly

When Codex's project/CWD is `C:\Users\chris\.ROOT`:

- `.ROOT\AGENTS.md` becomes the repo instruction pointer;
- `.ROOT\.codex\config.toml` becomes an active trusted project layer;
- `.ROOT\.agents\skills` becomes a repo skill source;
- the pointer instructs Codex to read `00-BRAIN\AGENT.md`, the Codex profile,
  `CHRIS_CORE.md`, `SYSTEM_FLAGS.md`, and `NORTH_STAR.md`, followed only by
  task-relevant companions.

This is the intended `.ROOT` architecture. The operating defect is choosing the
parent folder as the project, not the pointer design.

---

## 3. The 2% Skill Warning — Exact Diagnosis

The official manual states that Codex uses progressive disclosure:

- the initial prompt receives each skill's name, description, and path;
- that initial catalog is capped at 2% of context (or 8,000 characters when
  context size is unknown);
- descriptions are shortened first;
- some skills can be omitted from the initial catalog when the set is large;
- the full `SKILL.md` is read only after a skill is selected.

### Current active catalog

| Source | Skills | Measured one-line description characters | Full skill bytes on disk |
|---|---:|---:|---:|
| Vercel | 47 | 10,533 | 553,755 |
| Figma | 11 | 5,188 | 193,719 |
| Google Calendar | 5 | 1,441 | 16,999 |
| Google Drive | 5 | 2,296 | 59,855 |
| OpenAI Developers | 5 | 1,826 | 57,531 |
| GitHub | 4 | 1,126 | 16,229 |
| Airtable + Canva + Gmail | 8 | 1,821 | 35,289 |
| Browser/Sites/Visualize | 4 | 885 | 50,643 |
| Document/PDF/Presentation/Spreadsheet/Template runtime | 6 | 1,435 | 107,255 |
| Linear + Notion | 2 | 213 | 6,408 |
| **Enabled plugin subtotal** | **97** | **26,764** | **1,097,683** |
| Codex system skills | **5** | additional | additional |
| **Current session total** | **102** | **well above the discovery budget** | — |

The descriptions alone are more than three times the 8,000-character fallback
budget before names, paths, formatting, or the five system skills are counted.
Vercel by itself exceeds that fallback budget.

### What the warning does and does not mean

**It means:** implicit skill matching is degraded because Codex sees shortened
descriptions or an incomplete initial list.

**It does not mean:** only 2% of each skill is available, the full skill files
are truncated after selection, reasoning effort is capped, or plugins have been
deleted.

### Why `.ROOT` skills appeared missing

The five `.ROOT` skills—`atlas-brief`, `graph-colors`, `profit-gate`,
`root-health`, and `session-close`—exist in the correct official repo discovery
location: `.ROOT\.agents\skills`. They were absent from this session's available
skills list because the session started above the repo, not because the sync
mirror is wrong.

Do **not** copy those five skills to `C:\Users\chris\.agents\skills` as a quick
fix. Official behavior does not merge duplicate names, so a future session
inside `.ROOT` could show both user and repo copies and create version drift.
Opening the correct project solves discovery without duplication.

---

## 4. Global `.codex` Configuration Audit

### `config.toml`

| Setting/group | Live value | Assessment |
|---|---|---|
| Model | `gpt-5.6-sol` | App-managed/private-looking model slug; current session accepts it. Do not hand-normalize without a product reason. |
| Reasoning | `medium` | Sensible default. Raise per task/UI for deep audits rather than making every session expensive. |
| Approval reviewer | `auto_review` | Active human-in-the-loop backstop through automatic policy review; aligned with `.ROOT`. |
| Service tier | `default` | No issue. |
| Windows sandbox | `unelevated` | Appropriate local baseline; project permission profile still determines effective writable roots. |
| `features.js_repl` | `false` | Disables that optional capability. No `.ROOT` conflict. |
| OpenAI docs MCP | configured | Useful and directly closed the Codex-documentation gap in this audit. Keep. |
| Node/browser runtime block | app-generated | Required by installed browser/runtime tooling. Do not manually optimize. |
| Desktop preferences | steps/commands detail, ambient suggestions, queued follow-ups, remote awake | UX settings, not `.ROOT` governance. |
| Plugin enablement | artifact plugins explicitly enabled; curated plugin state surfaced at runtime | Main contributor to skill-catalog pressure. Manage through Plugins, not by editing cache files. |
| Shell environment policy | browser/runtime values | App-generated. Not a North Star instruction source. |

### Trust grants

Nine paths are currently trusted:

- the live `C:\Users\chris\.ROOT` vault;
- **the entire `C:\Users\chris` home directory**;
- four G:/legacy paths;
- `codexsandboxtest`;
- two dated/experimental Codex folders.

The home-directory grant is new relative to Claude's earlier same-day count
and is broader than `.ROOT` needs. Trust determines whether project-level
`.codex` configuration is honored; it should be deliberately narrow.

**Recommendation:** retain `.ROOT` and any genuinely active code/client repos;
remove the home-root, G:-era, sandbox-test, and dated experiment grants after
confirming none is active. This is a config change and requires Chris approval.

### Global `AGENTS.md`

The file exists and is empty. Claude's earlier audit was right that a small
global safety router is valuable, but it should not contain `.ROOT`'s North
Star or boot chain in full.

Recommended draft (for approval):

```markdown
# Global Codex Guidance — Chris's machine

- `C:\Users\chris\.ROOT` is a governed vault. For any task that reads or
  changes it, open/use that folder as the project and follow its root
  `AGENTS.md` before acting.
- Never read or write `C:\Users\chris\.ROOT\88-JOURNAL\`.
- Never modify a `raw\` file inside `.ROOT` unless Chris explicitly authorizes
  that exact exception. Archive approved replacements; do not delete history.
- Verify live paths and files before writing; do not rely on remembered maps.
```

This gives outside-the-vault sessions a safety tripwire without duplicating
`AGENT.md`, `NORTH_STAR.md`, `CHRIS_CORE.md`, or changing governance authority.

### `rules\default.rules`

The file contains 132 allow rules, zero deny rules, and 59 exact PowerShell
command approvals. Many point to retired `.AI_OS`, old `00-NORTH STAR` paths,
or one-time audit commands. One exact historical rule includes a validated
`Remove-Item` operation. These rules are approval memory, not the skill-list
prompt, so they are **not** causing the 2% warning.

They are still configuration debt:

- stale rules make the approval boundary hard to review;
- exact one-off commands provide little reusable value;
- legacy paths preserve a false picture of the live system;
- an allow-only file is not a mechanical journal/raw deny layer.

**Recommendation:** review and retire stale entries through the supported
rules/permissions surface. Keep only narrow, repeatable commands. Do not solve
this by adding broad `python`, `pwsh`, or `git` prefixes.

### Files intentionally excluded from instruction analysis

`auth.json`, credential/key stores, history, session JSONL, SQLite databases,
model caches, temporary runtime files, and app logs are state or secrets—not
durable instructions. They were not treated as governance, and credentials were
not inspected or reproduced. Plugin cache contents were measured/read only to
identify installed capability weight; cache files should never be hand-edited.

---

## 5. `.ROOT` Project Configuration and Governance Alignment

### Project config loading is now confirmed

Claude's Finding C2 can be closed as a documentation uncertainty. Current
official Codex documentation explicitly supports trusted project
`.codex/config.toml` layers and says Codex walks from project root to CWD,
loading every such layer. The closest layer wins.

Therefore `.ROOT\.codex\config.toml` is valid and will apply when `.ROOT` is
opened as a trusted project:

```toml
sandbox_mode = "workspace-write"
approval_policy = "on-request"

[sandbox_workspace_write]
network_access = false
```

It did not apply to this home-folder session because it is below, not above,
the current CWD. The config file is not dead; the project selection was wrong.

### Instruction-economy assessment

The intended always/read-every-session `.ROOT` chain is approximately:

| File | Lines | Approx. tokens (characters/4) |
|---|---:|---:|
| root `AGENTS.md` pointer | 16 | 178 |
| `00-BRAIN\AGENT.md` | 176 | 3,161 |
| `00-BRAIN\CODEX.md` | 46 | 740 |
| `00-BRAIN\CHRIS_CORE.md` | 127 | 1,300 |
| `00-BRAIN\SYSTEM_FLAGS.md` | 58 | 1,077 |
| `01-NORTH_STAR\NORTH_STAR.md` | 138 | 1,725 |
| **Core orientation total** | — | **about 8,181** |

For this architecture audit, the task-triggered Capability Contract adds about
3,173 tokens. That is legitimate progressive loading.

The core chain is not the source of the 2% skill warning. It is somewhat rich,
but it remains purposeful, bounded, and under the system's own 200-line
always-loaded-file guideline. Do not perform a blind compression pass. Remove
only proven duplication or volatile facts that belong elsewhere.

### One real alignment defect: volatile stage facts in `CHRIS_CORE.md`

`CHRIS_CORE.md` says live learning is Physics Stage 3 and Python Stage 2, while
`NOW.md` says Physics Stage 4 and Python Stage 3. Because `CHRIS_CORE.md` loads
every session, this creates an immediate conflict inside the orientation chain.

**Recommendation:** remove exact live stage numbers from `CHRIS_CORE.md` and
point to `NOW.md` plus the owning wiki current-position pages. The person file
should hold durable learning traits and life constraints; volatile frontier
status belongs to the live owner. This is a governance edit and should be
implemented only after Chris approves the wording.

### North Star fit

The recommended configuration supports the North Star better than the current
state because it:

- reduces ceremony at session start;
- makes the live vault, not the home directory, the working boundary;
- restores discoverability of `.ROOT`'s own proof/health/session skills;
- preserves human approval for consequential actions;
- keeps specialized capability available on demand instead of paying for all
  possible workflows in every prompt;
- favors a thin global harness and task-specific progressive disclosure;
- keeps product cache/config mechanics separate from `.ROOT` governance.

---

## 6. Recommended Operating Model

### Tier 1 — Always available

Keep the smallest set that supports ordinary `.ROOT` work:

- Codex system skills;
- the five repo-local `.ROOT` skills (discovered by opening `.ROOT`);
- core document/PDF/spreadsheet/presentation artifact plugins actually used;
- browser/sites/visualize only if they are part of regular weekly work;
- the OpenAI docs MCP server.

### Tier 2 — Daily connectors, only if genuinely frequent

Google Drive, Calendar, Gmail, and GitHub can remain enabled if Chris uses them
often enough to justify their discovery cost. Connector authentication and
plugin availability are separate; disabling a plugin does not automatically
revoke the underlying service connection.

### Tier 3 — Task-switched specialist bundles

Default these off and enable them for the sessions that need them:

- Vercel (47 skills);
- Figma (11 skills);
- Canva, Airtable, Linear, and Notion;
- OpenAI Developers when the session is not building with OpenAI APIs;
- any design/deployment stack not active in the current quarter.

Official supported control paths:

- desktop app: Plugins → Installed → turn a plugin off/on;
- Codex CLI: `/plugins`, then Space on an installed plugin;
- surgical persistent skill disable:

```toml
[[skills.config]]
path = "C:/absolute/path/to/SKILL.md"
enabled = false
```

Prefer plugin-level toggles for plugin bundles. Per-skill cache paths include
plugin versions and are likely to change on updates, so dozens of
`[[skills.config]]` entries against cache paths would create brittle config.

### Target, not dogma

The correct acceptance target is not an arbitrary number of skills. It is:

1. a fresh `.ROOT` session shows all five `.ROOT` skills;
2. the 2% warning is absent, or accepted deliberately for a connector-heavy
   session;
3. the task-relevant specialist skill can be invoked explicitly;
4. ordinary `.ROOT` prompts choose the right skill without Chris restating the
   workflow;
5. no required North Star capability was removed—only moved to on-demand.

---

## 7. Prioritized Change Plan

| Priority | Change | Why | Approval / validation |
|---|---|---|---|
| P0 | Start `.ROOT` work with `C:\Users\chris\.ROOT` selected as the project/CWD | Restores project config, root `AGENTS.md`, repo skills, and a narrow workspace boundary | No file change; fresh-session check |
| P0 | Turn off Vercel and Figma by default unless the active task needs them | Removes 58 skills and 15,721 measured description characters—the largest discovery pressure | Chris chooses plugin baseline; restart/new chat |
| P1 | Curate remaining plugins toward a normal-session working set | Reduces implicit-skill degradation and warning noise | Toggle, then measure warning and available list |
| P1 | Write the minimal global `.codex\AGENTS.md` router above | Protects `.ROOT` when Codex starts elsewhere without duplicating governance | Chris approves exact wording; fresh outside-vault test |
| P1 | Prune trust grants, especially `C:\Users\chris` and G:/experimental paths | Restores least privilege and makes project config intent legible | Chris confirms active repos; inspect config diff |
| P2 | Remove volatile Python/Physics stage numbers from `CHRIS_CORE.md` | Eliminates an always-loaded contradiction with `NOW.md` | Governance approval; boot-chain validation |
| P2 | Review `default.rules` and retire legacy/one-off allows | Improves permission auditability; unrelated to 2% warning | Preserve before-state; supported rules UI/file review |
| P2 | Ingest current Codex configuration/skills/plugin docs into AIAS | Closes the durable wiki evidence gap identified by Claude | Chris adds/captures raw; normal wiki ingest |
| P3 | Evaluate mechanical raw/journal filesystem protection | Codex prose remains the main vault-specific safety layer | Separate proposal; test Windows behavior first |

### Recommended implementation sequence

1. **No-edit experiment:** close this chat, select/open
   `C:\Users\chris\.ROOT` as the project, start a fresh session, and verify
   root guidance plus the five `.ROOT` skills are visible.
2. **Plugin experiment:** turn off Vercel first; if warning remains, also turn
   off Figma and other inactive specialist bundles. Start a new session after
   each coherent toggle set.
3. **Record the winning baseline:** note enabled plugins and the observed skill
   count/warning state in the implementation log.
4. **Governance/config edits:** only after Chris accepts this report, patch the
   global router, trust list, and volatile `CHRIS_CORE` line as one reviewed
   change set.
5. **Validate:** fresh `.ROOT` and fresh outside-`.ROOT` sessions, boot-chain
   validator, shared-skill sync check, config inspection, and a real invocation
   of `root-health` or `session-close`.

---

## 8. Acceptance Test

A configuration pass is complete only when a fresh session proves all of the
following:

- project/CWD reports `C:\Users\chris\.ROOT`;
- `.ROOT\.codex\config.toml` is effective (`workspace-write`, `on-request`,
  sandbox network off);
- `.ROOT\AGENTS.md` is automatically present as project guidance;
- `$root-health`, `$session-close`, `$graph-colors`, `$profit-gate`, and
  `$atlas-brief` appear in skill discovery/selection;
- normal skill catalog does not show the 2% warning, or the warning is a
  conscious tradeoff for a named connector-heavy session;
- explicit invocation of a specialist skill still reads the full skill;
- an outside-vault session recognizes `.ROOT` as governed and refuses journal
  access before touching it;
- `CHRIS_CORE.md` no longer contradicts the live owner on learning stage;
- no G:/backup path or entire-home trust grant remains without a live reason;
- no cache, auth, session, SQLite, or plugin package file was hand-edited.

---

## 9. Final Recommendation in One Sentence

**Make `.ROOT` the selected project, not a child of the selected project; keep
`.ROOT` governance repo-local and progressive; use a tiny global safety router;
and treat the plugin catalog as a toolbelt to switch by job, not 102 tools that
must hang on the belt every session.**

---

## Return Packet

1. **Outcome:** exact Codex instruction/configuration stack mapped; the 2%
   warning and missing `.ROOT` skills diagnosed; prioritized remedy defined.
2. **Evidence link:** this report plus
   `AI_SURFACE_CONFIG_AUDIT_2026-07-17.md` and the live config/governance files.
3. **Capability/status movement:** none yet—report-only; implementation awaits
   Chris's review.
4. **Reusable-asset candidate:** no; this is internal machine/vault governance.
5. **System-learning candidate:** yes—the repeatable lesson is that project-root
   selection controls both instruction and repo-skill discovery, while the 2%
   warning measures only the initial skill catalog.

*Prepared by Codex from live state on July 17, 2026. No settings changed.*
