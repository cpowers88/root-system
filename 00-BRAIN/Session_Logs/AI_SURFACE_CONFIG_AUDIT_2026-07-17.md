---
type: report
timeline: now
tags: [governance, claude, codex, configuration, audit]
created: 2026-07-17
status: mostly-implemented
---

# AI Surface Configuration Audit — Claude Code & Codex — July 17, 2026

**Scope:** Every `.claude` and `.codex` configuration location on this machine, matched
against (a) each other, (b) the `.ROOT` boot-chain governance files, and (c) the vendor
documentation held in `03-WIKIS\AI_AUTOMATION_SYSTEMS\` (raw + wiki). Findings below were
gathered report-only, then Chris approved the batch same-session ("go... nothing exactly
locked, but does need permission to go places") and 9 of 13 action-plan items were
implemented same session — see §6 for per-item status. Two items remain genuinely open
(§7 questions 5 and 7); two more are gated on Chris capturing follow-up docs (item 7's
remainder, item 8).

---

## 1. Executive Summary

The Claude Code side is in **good shape and closely matches the pattern the official
docs recommend** (Manual mode + deny rules = the documented "hard guarantee" posture).
Main issues are hygiene: three different deny-path syntaxes across three settings files
(they cannot all be resolving as intended), a permission allowlist polluted by one-off
auto-accreted grep entries, a stale `G:\My Drive\.claude` leftover, and a sandbox block
whose effect on native Windows needs verification.

The Codex side has **one significant hole and one open mechanical question**:

1. **`C:\Users\chris\.codex\AGENTS.md` is empty (0 bytes).** Codex loads this file in
   every session, everywhere on the machine. Right now it contributes nothing — the
   machine-wide hard boundaries (88-JOURNAL private, raw immutable) exist for Codex only
   as in-repo prose it reads *after* opening `.ROOT`, and not at all outside `.ROOT`.
2. ~~**It is unverified whether Codex actually loads `.ROOT\.codex\config.toml`.**~~
   **RESOLVED July 17 (same day):** Chris captured the official Codex config docs into
   raw. "Config basics" states project overrides via `.codex\config.toml` **are loaded,
   but only when the project is trusted** — and `c:\users\chris\.root` holds
   `trust_level = "trusted"` in the global config. `.ROOT`'s `sandbox_mode`/
   `approval_policy`/`network_access` lines are live config, not dead letters.

The wiki evidence base is **strong for Claude Code and thin-to-absent for Codex CLI
configuration**: 22 official Claude Code docs in raw with two excellent distilled pages,
versus an OpenAI folder that is API/platform documentation (Agents SDK, ChatKit, GPT
Actions) with essentially nothing on the Codex app's `config.toml`, `AGENTS.md`
discovery, sandbox modes, or approval policies. Codex-side recommendations below are
therefore grounded in model knowledge, not vault evidence — closing that raw gap is
itself a recommendation.

---

## 2. Inventory — What Actually Loads From Where

### Claude Code (this machine, working in `.ROOT`)

| Layer | File | Status |
|---|---|---|
| User settings | `C:\Users\chris\.claude\settings.json` | Live. Deny rules (journal/raw/destructive), Manual mode, bypass+auto disabled, model `claude-fable-5[1m]`, dark theme, notifications on |
| User local | `C:\Users\chris\.claude\settings.local.json` | Live. Allow list — partly curated, partly auto-accreted junk (see §3) |
| User memory | `C:\Users\chris\.claude\CLAUDE.md` | **Does not exist** (intentional — governance lives in the boot chain; noted for completeness) |
| Auto memory | `C:\Users\chris\.claude\projects\C--Users-chris--ROOT\memory\` | Live and in use |
| Project settings | `C:\Users\chris\.ROOT\.claude\settings.json` | Live. Deny + ask lists, sandbox block, network allowlist |
| Project local | `C:\Users\chris\.ROOT\.claude\settings.local.json` | Live. Curated allow list (validation scripts, WebFetch domains, Google Calendar MCP, `Skill(run)`) |
| Template | `C:\Users\chris\.ROOT\.claude\user-settings-policy.template.json` | Reference copy of intended user settings (mild drift — lacks `model`) |
| Backup | `C:\Users\chris\.claude\settings.pre-phase1-2026-07-15.json` | Pre-hardening backup, archive candidate |
| Instructions | `.ROOT\CLAUDE.md` → `00-BRAIN\AGENT.md` → `00-BRAIN\CLAUDE.md` → chain | Pointer-only root file — exactly the pattern the docs validate (subagents re-pay root CLAUDE.md cost, so pointer-only is right) |
| Skills | `.ROOT\.claude\skills\` (5 skills) | Generated mirror of `00-BRAIN\SKILLS\`, matches `.agents\skills\` mirror |
| **Stray** | `G:\My Drive\.claude\settings.local.json` | **Leftover from the G: vault era.** Contains a full old-style policy (allow/ask/deny/sandbox) with `.ROOT/`-prefixed paths. Only loads if a session starts under `G:\My Drive`; confusion risk, no current function |

### Codex (this machine)

| Layer | File | Status |
|---|---|---|
| Global config | `C:\Users\chris\.codex\config.toml` | Live, largely **app-managed** (desktop): model `gpt-5.6-sol` @ medium reasoning, plugins, MCP servers, `[windows] sandbox = "unelevated"`, per-project `trust_level = "trusted"` entries — including `c:\users\chris\.root` **and four stale G:-era paths** |
| Global instructions | `C:\Users\chris\.codex\AGENTS.md` | **Empty (0 bytes)** — loaded every session, contributes nothing |
| Rules | `C:\Users\chris\.codex\rules\default.rules` | App-managed default sandbox rules (32 KB) |
| Skills | `C:\Users\chris\.codex\skills\.system\` | Vendor system skills only; no `.ROOT` shared-skill mirror exists for Codex global |
| Project config | `C:\Users\chris\.ROOT\.codex\config.toml` | `sandbox_mode = "workspace-write"`, `approval_policy = "on-request"`, `network_access = false` — **loading unverified** (see Finding C2) |
| Project instructions | `C:\Users\chris\.ROOT\AGENTS.md` | Pointer to boot chain (`AGENT.md` → `CODEX.md` → …) — correct, this *is* read by Codex |

Cross-check worth stating explicitly (confirmed by the raw docs): **Claude Code does not
read `AGENTS.md`, and Codex does not read `CLAUDE.md`.** `.ROOT`'s twin-pointer design
(root `CLAUDE.md` + root `AGENTS.md`, both pointing at the same `AGENT.md` boot chain)
handles this correctly. The similarly named `00-BRAIN\AGENT.md` (singular) is `.ROOT`'s
own universal OS file, not either vendor's mechanism — naming is fine, just never
mistake them for the same thing.

---

## 3. Claude Code — Rule-by-Rule Match

### Deny rules (the protection that matters most)

| Rule intent | User `settings.json` | Project `settings.json` | Stray G: file | Boot-chain authority |
|---|---|---|---|---|
| 88-JOURNAL never read/written | `~/.ROOT/88-JOURNAL/**` | `/88-JOURNAL/**` | `/.ROOT/88-JOURNAL/**` | AGENT.md File Safety #8 |
| raw/ never edited/written | `~/.ROOT/**/raw/**` | `/**/raw/**` | `/**/raw/**` | AGENT.md File Safety #9 |
| No `rm`/`rmdir` | ✔ | ✔ | ✔ | AGENT.md archive-don't-delete |
| No `git reset --hard` / `git clean` | ✔ | ✔ | ✔ | same |
| No `Remove-Item`/`Clear-Content` | ✔ | ✔ | ✔ | same |
| Bypass + Auto modes disabled | ✔ | ✔ | ✔ | AGENT.md human-in-the-loop |

**Finding CL1 — CORRECTED July 17 (evening), original finding was wrong.**
Original claim: three deny-path syntaxes across three settings files were
inconsistent and needed standardizing onto `~/.ROOT/...`. **That was a
misread.** `00-BRAIN\scripts\validate_boot_chain.py` deliberately requires
**different** spellings at different scopes: project-scope
`.ROOT\.claude\settings.json` must use project-relative
`/88-JOURNAL/**`/`/**/raw/**`, while user-scope files (`~/.claude/settings.json`
and `.ROOT\.claude\user-settings-policy.template.json`) must use
home-anchored `~/.ROOT/...`. This is documented in the validator itself:
*"Claude safety is split deliberately: user scope = launch-independent,
non-negotiable deny/mode baseline; project scope = reviewable .ROOT policy."*
Acting on the original finding "standardized" the project file onto the
user-scope spelling, which **broke the validator and produced a root-health
BLOCKER** — caught by Codex the same evening (SYSTEM_FLAGS #76, closed same
session). Reverted; `validate_boot_chain.py` now passes clean. The only
genuinely stray spelling was the archived G: file's `/.ROOT/88-JOURNAL/...`,
which is moot — that file is now in `99-ARCHIVE`. **No further action on
this finding** — the two-spelling split is correct as originally written and
should not be touched again without re-reading the validator first.

**Finding CL2 — allowlist pollution in user `settings.local.json`.** Alongside four
deliberate entries (`git *`, `python *`, and the two named validation scripts) sit four
enormous auto-accreted `Bash(grep ...)` entries with 8-deep backslash escaping — one-off
session approvals that got saved as permanent rules. They are dead weight, will never
match again, and make the file unreadable. Also note `Bash(git *)` includes `git push`
and `Bash(python *)` includes any script on the machine — both broad. Given AGENT.md's
human-approval rule for consequential actions, `git *` is defensible (deny rules still
block the destructive subset), but it's a deliberate-choice item, not an accident to
preserve. **Action:** delete the four grep entries; consciously confirm or narrow
`git *` / `python *`.

**Finding CL3 — sandbox block may be inert on native Windows.** Project settings enable
`sandbox.enabled: true` with filesystem denyRead/denyWrite and a network allowlist of two
Anthropic doc domains. Claude Code's OS sandbox is documented for macOS/Linux; on native
win32 the effective protection is the permission-rule layer, not this block. The
`denyWrite` list also duplicates what the `/**/raw/**` deny rule already covers, and its
`./`-relative paths silently depend on the session CWD. Not harmful — but we should not
*believe* we have sandbox guarantees we may not have. **Action:** verify (run a session
and check whether the sandbox reports active), then either keep the block documented as
"forward-looking, inert on Windows" or trim it.

**Finding CL4 — housekeeping.** (a) `settings.pre-phase1-2026-07-15.json` → archive to
`99-ARCHIVE` per convention. (b) `G:\My Drive\.claude\` → delete or archive; G: is
backup-only and this file predates the C: migration. (c)
`user-settings-policy.template.json` lacks the `model` line the live user file now has —
sync the template when other changes land.

### What the docs say we're doing right (no action)

- **Manual mode + deny rules** is verbatim the documented "hard guarantee" pattern;
  verbal boundaries don't survive compaction, deny rules apply in every mode including
  bypass. (`wiki\claude-code-permissions-security-and-review.md`)
- **Protected-path backstop:** `.claude/` writes are never auto-approved regardless of
  allow rules — vendor-enforced second layer against settings self-escalation.
- **Pointer-only root `CLAUDE.md`:** every subagent re-pays root CLAUDE.md cost, so the
  pointer design multiplies its savings across forks.
- **<200-line always-loaded files** as a quality lever, already .ROOT doctrine.
- **Skills mirrors** (`.claude\skills\` = `.agents\skills\` = canonical `00-BRAIN\SKILLS\`)
  are in sync — 5 skills each.

### Not yet used, worth knowing (candidates, not gaps)

- **`.claude/rules/` path-scoped rules** — per-hub `CLAUDE.md` files already achieve the
  same context economy; only revisit if one folder needs type-specific rules.
- **HTML comments in governance files** are stripped before context injection — free
  human-only "why this rule exists" annotations. Immediately usable, zero risk.
- **`security-guidance` plugin** — already flagged in the wiki as a proposal candidate
  *once* real code projects run in `.ROOT` with git; not before.
- **Hooks** — AGENT.md's extension table already gates these ("hook only after
  evaluation"); nothing currently justifies one.

---

## 4. Codex — Rule-by-Rule Match

### What protects the vault when Codex works in `.ROOT`

| Protection | Claude Code has | Codex has |
|---|---|---|
| Journal/raw write-block | Deny rules, two layers | **Nothing mechanical** — only prose in `AGENT.md` File Safety, loaded via the AGENTS.md pointer |
| Destructive-command block | Deny rules | Approval prompts (`approval_policy = "on-request"` — *if* the project config loads; otherwise whatever the app's trust level grants) |
| Network restraint | Sandbox allowlist (2 domains) | `network_access = false` in workspace-write (same caveat) |
| Machine-wide instructions | n/a (`~/.claude/CLAUDE.md` absent by design) | `~/.codex/AGENTS.md` **empty** |

**Finding C1 — empty global `AGENTS.md` is the single best Codex improvement available
(HIGH value, 10 lines of text).** Codex has no deny-rule vocabulary for paths; its file
safety inside `.ROOT` is entirely instruction-borne. Those instructions currently load
only through the repo pointer — a Codex session started *outside* `.ROOT` (Documents,
Desktop, a client repo) has zero knowledge of the journal/raw boundaries and could be
handed a path into the vault. Proposed content (draft, for approval):

```markdown
# Global Codex Instructions — chris @ this machine
- `C:\Users\chris\.ROOT` is a governed vault. When working in it, follow its
  root `AGENTS.md` boot chain before acting.
- Machine-wide hard stops, in any directory: never read or write
  `C:\Users\chris\.ROOT\88-JOURNAL\`; never modify any file under a `raw\`
  folder inside `.ROOT`; never delete — archive instead.
- Prefer reading live files over remembered maps; verify paths before writing.
```

Keep it under ~15 lines — it loads into every Codex session on the machine, so the same
context-economy discipline as root `CLAUDE.md` applies.

**Finding C2 — RESOLVED July 17.** Official docs (now in
`raw\OPEN_AI-CHATGPT_CODEX_FILES\Config basics.md`) confirm Codex loads project
`.codex\config.toml` layers **when the project is trusted**; `.ROOT` is trusted, so its
`sandbox_mode = "workspace-write"`, `approval_policy = "on-request"`, and
`network_access = false` are in effect. Note the coupling this creates: the project
config's protection *depends on* the trust grant in the global file — one more reason
to keep the trust list pruned (Finding C3).

**Finding C3 — stale trust grants in global `config.toml`.** Seven directories hold
`trust_level = "trusted"`, including four G:-era/experiment paths (`g:\my drive\.root`,
`g:\my drive`, `g:\my drive\test_gemini`, `codexsandboxtest`). `g:\my drive` trusts the
*entire* backup drive. Harmless day-to-day, but trust grants are exactly the thing to
keep minimal. **Action:** prune to `c:\users\chris\.root` (+ any active client dirs).

**Finding C4 — no Codex mirror of shared skills.** `sync_shared_skills.py` feeds
`.claude\skills\` and `.agents\skills\`. If `.agents\skills\` is the intended
Codex-discovery mirror, confirm Codex actually discovers them there; if Codex needs
`~/.codex/skills\` or a different location, extend the sync script (small change, real
capability gain — session-close, root-health etc. become invocable from Codex).

**Finding C5 — optional tuning.** Model is `gpt-5.6-sol` @ `medium` reasoning. For the
audit/validation work Codex does in `.ROOT`, `high` reasoning effort is worth an A/B on
one real audit task before changing the default. App-managed sections (plugins, MCP
servers, marketplaces) look healthy; leave them alone.

**Finding C6 (added evening of July 17, from the doc ingest) — `approvals_reviewer =
"auto_review"` in the global config routes Codex approval prompts to an AI guardian
agent, not to Chris.** The docs are explicit: auto-review substitutes a reviewer agent
for the user on exactly the actions consequential enough to prompt (sandbox escalations,
network requests, side-effecting tool calls). That is in direct tension with `AGENT.md`'s
"consequential actions remain human-approved" rule — and it was invisible until the
official docs were read. Chris decision needed: set `user` for doctrine alignment, or
record auto-review as a documented, bounded exception. `/approve` retries a guardian
denial once either way.

**Finding C7 (added same ingest) — Codex has deterministic guard mechanisms the audit
believed it lacked.** (a) **Named permission profiles** (beta): `[permissions.<name>]`
filesystem rules per path/glob valued `read`/`write`/`deny` — a custom profile can make
`raw\` read-only and `88-JOURNAL\` read-denied, mechanically, replacing the
filesystem-attribute workaround as the idiomatic option (selected via
`default_permissions`; replaces `sandbox_mode`, don't combine). (b) **Execpolicy
`.rules` files**: prefix rules with `allow`/`prompt`/`forbidden` decisions — Codex's
equivalent of Claude's command deny rules (e.g. forbid `Remove-Item`, `git reset
--hard`). (c) **Lifecycle hooks** (`PreToolUse` etc.), trust-gated. Also confirmed:
`.git\`, `.codex\`, and `.agents\` are vendor-protected read-only inside the
workspace-write sandbox — Codex cannot silently edit its own project config or the
skills mirror. Full mechanics: `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\codex-app-configuration-and-security.md`.
Prerequisite before implementing: capture the dedicated Permissions/Rules/Hooks doc
pages into raw.

**Finding C8 (same ingest) — Windows sandbox mode.** Docs recommend `[windows]
sandbox = "elevated"`; this machine runs `"unelevated"`. The in-session
`/setup-default-sandbox` command performs the elevated upgrade (needs admin once).

### One deterministic guard that would protect against *every* surface

Windows read-only attributes on raw files (`attrib +R` recursively on each `raw\`
folder) block accidental writes from Claude, Codex, ATLAS-driven scripts, and Chris's
own slips alike — at the filesystem level, no AI instruction involved. Cost: Chris (or a
small helper script) clears/re-sets the bit when legitimately adding raw material. This
is the only mechanism on the table that gives Codex a *mechanical* raw-immutability
guarantee today. Worth a proposal through the normal review path.

---

## 5. Wiki Evidence Base — Coverage Assessment

**Claude side: strong.** 22 official docs in `raw\CLAUDE_FILES\`, distilled into
`claude-code-permissions-security-and-review.md`, `claude-code-context-and-instruction-economics.md`,
`claude-code-workflows-and-sessions.md`, `claude-code-integration-surface-and-platform.md`,
`claude-code-prompt-library-patterns.md`. The permission and context-economics pages are
current (July 12 ingest) and directly grounded every Claude-side judgment in this audit.

**Codex side: the config surface is uncovered.** `raw\OPEN_AI-CHATGPT_CODEX_FILES\`
(~100 files) is OpenAI *platform* documentation — Agents SDK, ChatKit, GPT Actions,
fine-tuning, Responses API. Grep across the whole folder finds **no** documentation of
the Codex app's `config.toml` reference, `AGENTS.md` discovery order, sandbox modes, or
approval policies (one incidental `AGENTS.md` mention in `Sandbox Agents OpenAI API.md`).
The wiki pages (`openai-sdks-cli-and-agent-builder.md`, `shift-to-agentic-ai-codex.md`)
inherit the same gap.

**Consequence:** every Codex-side claim in §4 rests on model knowledge, not vault
evidence — the exact situation `.ROOT`'s evidence-first doctrine exists to avoid.
**Action:** Chris captures the official Codex configuration docs (config reference,
AGENTS.md, sandbox & approvals pages) into raw (raw is Chris-write-only), then a normal
wiki ingest produces a `codex-app-configuration.md` page. That page then becomes the
authority for re-verifying Findings C1–C4.

---

## 6. Recommended Action Plan (priority order)

| # | Action | Surface | Effort | Value | Gate |
|---|---|---|---|---|---|
| 1 | ~~Write global `~/.codex/AGENTS.md`~~ **DONE July 17** — 12-line file written (governed-vault pointer, 88-JOURNAL/raw hard stops, consequential-action ask rule) | Codex | — | Resolved | — |
| 2 | ~~Verify `.ROOT\.codex\config.toml` loads~~ **DONE July 17** — docs confirm project config loads for trusted projects; `.ROOT` is trusted | Codex | — | Resolved | — |
| 3 | ~~Fix deny-path syntax~~ **REVERSED then RE-RESOLVED July 17** — original fix was wrong (see corrected Finding CL1); it broke `validate_boot_chain.py` and caused a root-health BLOCKER (SYSTEM_FLAGS #76). Reverted to the validator-required project-relative spelling; validator now PASSes clean. No further action — the two-spelling split was correct all along | Claude | — | Resolved (self-corrected) | — |
| 4 | ~~Clean user `settings.local.json`~~ **DONE July 17** — 4 junk grep entries removed; `git *`/`python *` kept broad per Chris ("nothing locked, but needs permission to go places"), with `Bash(git push*)` moved to `ask` as the one outbound/consequential exception | Claude | — | Resolved | — |
| 5 | ~~Prune Codex trust levels~~ **DONE July 17** — 4 stale G:-era entries removed; kept `c:\users\chris\.root` plus two other real local dirs the app had added since the audit (a Documents\Codex session dir and bare `c:\users\chris`) | Codex | — | Resolved | — |
| 6 | ~~Delete/archive `G:\My Drive\.claude\`~~ **DONE July 17** — moved to `99-ARCHIVE\ARCHIVED_2026-07-17_GDRIVE_claude_settings\`. ~~Archive `settings.pre-phase1` backup~~ **DONE** — moved to `99-ARCHIVE\ARCHIVED_2026-07-17_claude_user_settings_pre-phase1.json`. ~~Sync template~~ **DONE** — `model` line added to `user-settings-policy.template.json` | Both | — | Resolved | — |
| 7 | ~~Capture Codex config docs → wiki ingest~~ **DONE July 17 (both halves)** — 5 docs in raw, all read in full, compiled into `wiki\codex-app-configuration-and-security.md`. Follow-up capture queued: Permissions, Hooks, Rules, AGENTS.md, Sandboxing pages | Wiki | — | Resolved | Follow-up capture: Chris |
| 8 | Mechanical raw/journal guard for Codex — **upgraded by the ingest**: prefer a custom permission profile (raw `read`, journal `deny`) and/or execpolicy `.rules` forbidding destructive commands over the filesystem-attribute workaround. Pilot + verify with `codex sandbox windows -P <profile>` (beta feature) | Codex | Proposal + pilot | MED-HIGH | Normal proposal path, after follow-up doc capture |
| 9 | Skills-mirror parity for Codex — **start with `/import`** (migrates Claude Code config/skills), then extend `sync_shared_skills.py` only if needed | Codex | 15–30 min | MED | After #7 follow-up |
| 12 | ~~Decide `approvals_reviewer`~~ **DONE July 17** — switched to `"user"` in `~/.codex/config.toml`; Chris reviews Codex approval prompts again, aligned with AGENT.md doctrine | Codex | — | Resolved | — |
| 13 | Upgrade Windows sandbox `unelevated` → `elevated` via `/setup-default-sandbox` (Finding C8; docs' recommendation; needs admin once) | Codex | 10 min | MED | Chris runs it (interactive, admin prompt) |
| 10 | Verify Windows sandbox status; document or trim the sandbox block | Claude | 10 min | LOW-MED (accuracy of self-knowledge) | Verify first |
| 11 | Optional: A/B `high` reasoning effort for Codex audit tasks | Codex | One task | LOW | Chris preference |

**What deliberately stays as-is:** Manual mode, disabled bypass/auto, two-layer deny
overlap, pointer-only root `CLAUDE.md`/`AGENTS.md`, the boot chain itself, curated
project allowlist, skills sync system, app-managed Codex sections, absence of
`~/.claude/CLAUDE.md` (the boot chain is the governance channel; a user-level memory
file would create a second, unversioned instruction source).

---

## 7. Open Questions for Chris

1. ~~Approve the global `~/.codex/AGENTS.md` draft wording?~~ **Resolved July 17:**
   Chris said go; written as drafted.
2. ~~Keep `Bash(git *)` broad, or narrow to exclude `git push`?~~ **Resolved July 17:**
   Chris's stated principle — "nothing exactly locked, but needs permission to go
   places" — kept `git *`/`python *` broad for local work and moved `git push*` to
   `ask` as the one outbound/consequential exception. Same shape now governs both
   the Claude allowlist and the Codex `approvals_reviewer` decision (#6 below).
3. ~~G: stray `.claude` — delete outright, or copy into `99-ARCHIVE` first?~~ **Resolved July 17:** Chris said remove it; moved to `99-ARCHIVE\ARCHIVED_2026-07-17_GDRIVE_claude_settings\`.
4. ~~Willing to capture the Codex config doc set into raw?~~ **Resolved July 17:**
   captured and sorted into `raw\OPEN_AI-CHATGPT_CODEX_FILES\`.
5. **STILL OPEN** — Interest in the mechanical raw/journal guard for Codex (#8 — now
   a permission profile / execpolicy rules per Finding C7, superseding the
   read-only-attribute idea), or is instruction-level immutability considered
   sufficient? Blocked on the follow-up doc capture (item 7's remainder).
6. ~~`approvals_reviewer`: switch to `user`?~~ **Resolved July 17:** yes — switched to
   `"user"` in `~/.codex/config.toml`.
7. **STILL OPEN** — Run `/setup-default-sandbox` to move the Windows sandbox to
   `elevated`? (Finding C8 / item 13) — interactive, needs Chris to run it directly.

---

*Audit performed from outside a live `.ROOT` work session ("from the outside"), report
placed in Session_Logs per request; DAILY_2026-07-17.md deliberately not amended.*
