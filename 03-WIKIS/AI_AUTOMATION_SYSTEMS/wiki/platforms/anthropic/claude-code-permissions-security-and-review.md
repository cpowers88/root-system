---
type: research
timeline: reference
tags: [ai-automation, claude-code, permissions, security, code-review]
source: raw/CLAUDE_FILES/ — PERMISSION_MODES.md, SECURITY_GUIDANCE_PLUGIN.md, CODE_REVIEW.md (official Claude Code docs, re-ingested July 12, 2026 after the folder moved from `00-BRAIN\CASTLE\raw\books\CLAUDE_FILES\` to its correct home here)
---

# Claude Code — Permission Modes, Security Guidance, and Code Review

**Official Claude Code documentation, three pages read in full for the first time
in this pass** (the CASTLE-era ingest on July 11 only skimmed these). Covers the
permission-mode mechanics behind `.ROOT`'s hardened `.claude/settings.local.json`,
and two review layers `.ROOT` has not yet evaluated: the `security-guidance`
plugin and the `REVIEW.md` mechanic behind PR-based Code Review.

## One-paragraph summary

Permission modes set a baseline (Manual/`default` reviews every action; `acceptEdits`,
`plan`, `auto`, `dontAsk`, `bypassPermissions` trade oversight for throughput), and
**deny rules and explicit ask rules apply in every mode without exception, including
`bypassPermissions`** — the one guarantee that doesn't depend on which mode a session
happens to be in. `.ROOT`'s current Manual-mode + deny-rule hardening is exactly the
pattern the docs recommend for "hard guarantees" (verbal boundaries stated in
conversation are *not* durable — they're lost on context compaction; only a deny
rule holds). Two adjacent capabilities were never actually read before: the
`security-guidance` plugin (automatic, hook-based, three-layer code review that
fires *during* a session, not after) and the `REVIEW.md` file (a repo-root override
that retunes what the PR-based Code Review service flags, separate from `CLAUDE.md`).

## Permission modes — the six-way table

| Mode | What runs without asking | Best for |
|---|---|---|
| `default` (labeled **Manual**) | Reads only | Sensitive work — `.ROOT`'s current mode |
| `acceptEdits` | Reads, file edits, common filesystem commands | Iterating on reviewed code |
| `plan` | Reads only; Claude researches and proposes, doesn't edit | Exploring before changing |
| `auto` | Everything, gated by a background classifier model | Long tasks, fewer prompts |
| `dontAsk` | Only pre-approved tools; denies everything else | Locked-down CI/scripts |
| `bypassPermissions` | Everything, no checks | Isolated containers/VMs only |

## Protected paths — a mechanic worth knowing precisely

Writes to a fixed set of paths are **never auto-approved in any mode except
`bypassPermissions`** — this is a separate, harder layer than ordinary permission
rules:

- Protected directories: `.git`, `.config/git`, `.vscode`, `.idea`, `.husky`,
  `.cargo`, `.devcontainer`, `.yarn`, `.mvn`, `.claude` (except `.claude/worktrees`).
- Protected files: `.gitconfig`, shell rc files, `.npmrc`/`.yarnrc`, `.mcp.json`,
  `.claude.json`, and several more.
- **An explicit `permissions.allow` rule does not pre-approve a protected-path
  write.** The safety check runs *before* Claude Code evaluates allow rules, so
  something like `Edit(.claude/**)` in settings has no effect on this table. In
  modes that prompt, the prompt for a `.claude/` write offers a one-session
  "allow Claude to edit its own settings" option — approving later `.claude/`
  writes for the rest of that session only.

This is a structural reason `.claude/settings.local.json` can't be silently
self-escalated by an allow rule, independent of the deny-rule hardening `.ROOT`
already did — a second, vendor-enforced backstop on top of the first.

## `auto` mode — not currently relevant, but the boundary mechanic is

`.ROOT` doesn't use `auto` mode, but one fact matters regardless of mode: **a
boundary you state in conversation** ("don't push", "wait until I review") is
read by the classifier from the live transcript on each check — **it is not
stored as a rule**, and is lost if context compaction removes the message that
stated it. The docs are explicit: *"For a hard guarantee, add a deny rule
instead."* This directly validates why `.ROOT`'s permission hardening used
deny rules rather than relying on session-stated boundaries.

## The `security-guidance` plugin — genuinely new capability, not yet evaluated

Not the same thing as the `/security-review` skill `.ROOT` already has (that's
on-demand, one pass). This plugin, once installed, runs **automatically** at
three points, each a different depth:

1. **On each file edit** — a zero-cost, no-model-call pattern match (regex/substring)
   for risky calls: `eval(`, `os.system`, `pickle`, `.innerHTML =`,
   `dangerouslySetInnerHTML`, edits under `.github/workflows/`. Fires once per
   pattern per file per session.
2. **At the end of each turn** — a background Claude call (Opus 4.7 by default)
   diffs everything the turn changed and reviews for authorization bypass, IDOR,
   injection, SSRF, weak crypto. Runs in the background so it doesn't delay the
   reply; findings re-prompt Claude to fix them same-session. Capped at 30 files
   per turn, fires at most three times in a row.
3. **On each commit/push Claude makes** — a deeper agentic review (reads callers,
   sanitizers, related files) that only fires on commits/pushes run through
   Claude's own Bash tool (not on commits from the user's own shell, including
   the `!` escape). Capped at 20 reviews/rolling hour.

Requirements: Claude Code CLI ≥2.1.144, Python 3.8+ on PATH, and **a git
repository** — the end-of-turn and commit reviews skip silently outside one; the
per-edit pattern check works anywhere. None of the three layers block a write or
commit — findings are advisory, surfaced back to the writing Claude as
instructions to fix, not a gate. Extension points: `.claude/claude-security-guidance.md`
(freeform threat-model prose, 8 KB cap across user/project/project-local scopes)
and `.claude/security-patterns.yaml` (up to 50 custom regex/substring rules).

## `REVIEW.md` — the PR-review-tuning file, distinct from `CLAUDE.md`

Only relevant once `.ROOT` has a git-backed proof project with real PRs, but the
mechanic is precise enough to be worth recording now rather than re-deriving
later:

- `CLAUDE.md` violations found during a PR review are automatically demoted to
  **nit-level** findings — and, notably, **this runs bidirectionally**: if a PR's
  code change makes a `CLAUDE.md` claim stale, Code Review flags that the docs
  need updating too. This is the same failure class as the Codex validation
  pass `.ROOT` just ran (`ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md`
  — guides describing stale current-state) — Anthropic's own review product
  treats stale-doc drift as a first-class finding type, which is external
  validation that this is a known, recurring failure mode worth a standing check,
  not a one-off.
- `REVIEW.md` sits at the repo root and is injected **verbatim, as the
  highest-priority instruction block**, into every agent in the review pipeline
  — it overrides default review guidance, not just supplements it. Unlike
  `CLAUDE.md`, its `@`-import syntax is not expanded; only what's literally in
  the file applies. What it's built to tune: severity calibration (redefine what
  counts as 🔴 Important for this repo), a nit-count cap, skip rules (paths/
  categories to never flag — generated code, lockfiles), repo-specific
  always-check rules, a citation/evidence bar for findings, and re-review
  convergence behavior (suppress new nits after the first pass).
- PR-based Code Review itself is Team/Enterprise-plan only and not available
  under Zero Data Retention — not something a solo Claude Code user gets access
  to. The **locally-run `/code-review` command** (already in `.ROOT`'s skill set)
  is the free, always-available equivalent: same severity model conceptually,
  runs against the current branch's diff, supports `--comment` and `--fix`, and
  `/code-review ultra --fix` now runs the deeper cloud ultrareview and applies
  its findings back to the working tree.

## Why this matters for this wiki / `.ROOT`

- **Validates, doesn't change, the current permission posture.** `.ROOT`'s
  Manual-mode + deny-rule setup already IS the pattern this documentation
  recommends for hard guarantees; `auto`/`bypassPermissions` remain correctly
  unused. No action needed here — this is a confirmation, not a gap.
- **The protected-path backstop is worth knowing exists**, independent of
  `.ROOT`'s own deny rules — a second layer that specifically stops `.claude/`
  self-escalation via allow-rule drift, which the earlier CASTLE ingest didn't
  surface.
- **`security-guidance` is a candidate self-evolution proposal, not yet drafted.**
  It only becomes relevant once Claude Code is writing real code in
  `02-LIBRARY\.PROJECTS` with a git repo behind it — worth a proposal at that
  point, not before. Needs Python3 + pip + network access on first run, which is
  a real setup cost to weigh.
- **The `CLAUDE.md`-staleness-as-review-finding pattern is directly relevant
  to `.ROOT`'s own governance-file discipline** — Anthropic's product treats
  "code changed, docs didn't" as a standing check on every PR. `.ROOT` currently
  catches this kind of drift only via ad hoc audits (like the July 12 Codex
  validation pass). Worth a proposal: could the wiki-lint pass or a session-close
  step do a lighter version of this — flag when a page's claims contradict what
  a recent edit just changed?
- **`REVIEW.md` and the Capability Library** — if a Capability Library asset
  ever formalizes review calibration for client codebases (a plausible
  `APQC_[process]_CODE_REVIEW_CALIBRATION.md` asset down the line), this page
  is the source to build it from.
- Companion pages: [[claude-code-context-and-instruction-economics]] covers
  the same advisory-vs-deterministic split from the memory/caching side
  (hooks vs. CLAUDE.md as a request, not a guarantee); [[claude-code-prompt-library-patterns]]
  covers the six-pattern prompting checklist this page's `REVIEW.md`/
  `security-guidance` findings don't touch.

---
*Processed July 12, 2026. Source in `raw/CLAUDE_FILES/` (immutable).*
