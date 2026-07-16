---
type: research
tags: [ai-automation, claude-code, integrations, ci-cd, platform-landscape]
source: raw/CLAUDE_FILES/ (Anthropic Claude Code official docs, moved from CASTLE July 12, 2026) — CLI_USE.md, VSCODE_CLAUDE.md, JETBRAIN.md, GITHUB_ACTIONS.md, GITHUB_ENTERPRISE_SERVER.md, GITLAB_CI-CD.md, CLAUDE_CODE_IN_SLACK.md, OVERVIEW-Platform-and-Intergrations.md, "Working at the frontier" (Thomson Reuters case study); the formerly unparsed Anthropic enterprise ebook was recovered separately on 2026-07-15 — see [[enterprise-ai-adoption-and-production-roadmap]]
---

# Claude Code Integration Surface — CI/CD, IDE, Slack, and Platform Landscape

**Official Claude Code docs, inventoried July 11 (CASTLE ingest) and read in
full here July 12, 2026.** This is the lowest information-density chunk of
the pack: it catalogs *where else* Claude Code runs and *what it plugs
into* — none of it has a live `.ROOT` use case today. Recorded here as an
inventory so a future session doesn't have to re-derive "does `.ROOT` need
GitHub Actions" from scratch; it can just check this page.

## One-paragraph summary

Claude Code is one engine exposed through six surfaces (CLI, Desktop,
VS Code, JetBrains, web, mobile) and wired into five external integration
points (Chrome, GitHub Actions, GitLab CI/CD, automated Code Review, Slack)
plus MCP for everything else. The IDE extensions (VS Code, JetBrains) add
inline diffs, selection-context sharing, and checkpoints/rewind on top of
the same CLI; the CI integrations (GitHub Actions, GitLab CI/CD, GitHub
Enterprise Server) turn `@claude` mentions into automated PRs/MRs running
under a `CLAUDE.md`-guided agent in a sandboxed job; Slack routes `@Claude`
mentions to cloud Claude Code sessions and is itself being retired in favor
of "Claude Tag." None of this applies to `.ROOT` today — it is a Google
Drive vault with no git-hosted repo, no CI pipeline, no team Slack — but
the shape is worth knowing for the day a proof project (`02-LIBRARY\.PROJECTS`)
goes to GitHub.

## Platform surfaces (from OVERVIEW-Platform-and-Intergrations.md)

| Platform | Best for | Notable capability |
|---|---|---|
| CLI | terminal workflows, scripting, remote servers | full feature set, Agent SDK, computer use (macOS Pro/Max) |
| Desktop | visual review, parallel sessions | diff viewer, computer use, Dispatch |
| VS Code | working inside VS Code | inline diffs, integrated terminal, checkpoints |
| JetBrains | IntelliJ/PyCharm/WebStorm/etc. | diff viewer, selection sharing, terminal session |
| Web (claude.ai/code) | long-running/unattended tasks | Anthropic-managed cloud, keeps running after disconnect |
| Mobile | starting/monitoring tasks away from the machine | Remote Control, Dispatch to Desktop |

Config, project memory, and MCP servers are shared across the local
surfaces — the same `.claude/settings.json` and `CLAUDE.md` govern CLI,
VS Code, and JetBrains sessions on one machine. This is a direct match for
how `.ROOT` already treats `CLAUDE.md`/`AGENT.md` as portable governance
regardless of which Claude surface opens the vault.

## IDE extensions — VS Code and JetBrains

Both extensions are thin graphical wrappers around the same CLI engine, not
a separate product:

- **VS Code**: bundles its own private CLI copy for the chat panel (a
  separate standalone CLI install is still needed for `claude` in the
  integrated terminal). Adds a built-in local MCP server named `ide`
  (hidden from `/mcp`) that lets the CLI open diffs in VS Code's native
  viewer, read the current selection for `@`-mentions, and execute Jupyter
  notebook cells — the latter always requires an interactive confirmation
  and cannot run silently. Supports **checkpoints**: fork the conversation
  from any message, rewind code to that point, or both.
- **JetBrains**: does *not* bundle its own CLI — it runs the machine's
  installed `claude` in the IDE's integrated terminal and layers on diff
  viewing, selection-context sharing, and diagnostic sharing (lint/syntax
  errors auto-shared). `acceptEdits` mode is flagged as riskier here because
  Claude could modify IDE config files the JetBrains IDE auto-executes.
- Both: a `Read` deny rule on a file path (e.g. `.env`) blocks that file's
  content from being silently shared as selection/open-file context — the
  IDE integration doesn't bypass permission config.

## CI/CD integrations — GitHub Actions, GitHub Enterprise Server, GitLab CI/CD

All three follow the same shape: an `@claude` (or `@Claude`) mention in an
issue/PR/MR triggers a sandboxed job that reads the repo's `CLAUDE.md`,
does the work, and opens a PR/MR for human review — never pushes directly
to a protected branch.

- **GitHub Actions**: `/install-github-app` does guided setup (installer +
  workflow + secret). v1.0 unifies the old beta's scattered inputs
  (`mode`, `direct_prompt`, `max_turns`, etc.) into two: `prompt` and
  `claude_args` (raw CLI flags passthrough). Supports Amazon Bedrock and
  Google Cloud's Agent Platform via OIDC/Workload Identity Federation (no
  static cloud keys). A distinct "Code Review" feature (separate doc, not
  read in this chunk) posts automatic reviews on every PR without a
  trigger phrase.
- **GitHub Enterprise Server (GHES)**: an org Owner connects the GHES
  instance once (generates a GitHub App manifest); after that, developers
  get web sessions, Code Review, and Claude Security with zero per-repo
  setup. One real gap: the **GitHub MCP server does not work with GHES** —
  the documented workaround is the `gh` CLI (`gh auth login --hostname
  github.example.com`).
- **GitLab CI/CD** (GitLab-maintained integration, beta): a single
  `.gitlab-ci.yml` job plus a masked `ANTHROPIC_API_KEY` CI/CD variable.
  Same provider abstraction (Claude API / Bedrock / Vertex) via OIDC.
  Cost-optimization advice mirrors the other CI docs: specific `@claude`
  commands, `--max-turns` caps, job timeouts, and concurrency limits to
  avoid runaway/parallel job costs.

Common thread across all three: `CLAUDE.md` at the repo root is the single
lever for steering CI-triggered Claude, same role it plays for interactive
sessions — validates that `.ROOT`'s CLAUDE.md-as-governance pattern is the
vendor-intended one, not a local invention.

## Chat integration — Slack (being retired)

Claude Code in Slack routes `@Claude` mentions with detected coding intent
to a cloud Claude Code session; progress posts back to the thread; a
"Create PR" button closes the loop. Two facts worth remembering if this
ever becomes relevant: **it's already being replaced by "Claude Tag"** for
Team/Enterprise workspaces (same app, org-shared identity, admin-configured
access — nothing to reinstall), and it is **GitHub-only**, one PR per
session, channel-only (no DMs). Not a `.ROOT` use case — no team Slack
workspace exists in this system.

## Computer use, mislabeled in this pack as "CLI_USE.md"

**Filename defect**: `CLI_USE.md`'s actual content is *computer use*
(screen/GUI control — clicking, typing, screenshotting native apps), not
CLI usage instructions. Worth knowing if this page or the raw file is ever
searched by filename. Computer use itself: a built-in MCP server
(`computer-use`, off by default, macOS-only, Pro/Max plan, research
preview) that lets Claude open apps, click, type, and screenshot — reserved
as the *last-resort* tool (Claude tries MCP server → Bash → Chrome →
computer use, in that order). Holds a machine-wide lock until the session
exits; per-app approval; terminal excluded from screenshots so on-screen
text can't feed prompt injection back through the terminal. No `.ROOT` use
case (Windows machine; feature is macOS-only), but the **tool-priority
order** (structured tool > shell > browser > screen control, cheapest/most
precise first) is a reusable heuristic for any agent-tool vetting work this
wiki already does (see [[agent-vetting-worked-examples]]).

## Case study: Thomson Reuters ("Working at the frontier")

**Tier 3 — vendor blog, customer-story format, treat as marketing, not
evidence.** ⚠️ **Metadata defect**: the source file's frontmatter has
`published: 2001-07-08`, almost certainly a typo for `2026-07-08` (the
`created:` field two lines below correctly reads `2026-07-11`) — flagged,
not silently corrected, since raw/ is immutable.

What's usable despite the tier — vocabulary and a trust framework directly
reusable in Chris's own `05-BUSINESS` audit/client conversations:

- **"Fiduciary-Grade AI"** — Thomson Reuters' own term for AI that is
  grounded in authoritative content, shaped by domain expertise, and
  embedded in a workflow so outputs are transparent, verifiable, and
  defensible. A named articulation of exactly the **verification-capacity
  gap** this wiki has now confirmed independently four times (see
  [[agentic-ai-industry-adoption-barriers]], [[work-trend-index-2024-2026]],
  [[generative-ai-for-software-development-pereira]], [[ai-index-2026]]) —
  a fifth independent confirmation, this time from a vendor case study
  rather than a neutral source, so weight it accordingly.
- **Four requirements a professional-grade AI system has to meet**, per
  their CTO: (1) checks its own citations before presenting findings, (2)
  holds steady across long chains of tool calls, (3) brings a human into
  the work product, not just the final answer, (4) frees time for work
  that was previously out of reach, not just speeds up existing work. This
  is a usable four-point checklist when a client audit asks "how do I know
  an AI tool is actually good enough for this."
- **ROI framing**: "if you try to optimize too much for the rate-of-return
  calculation, you miss the forest for the trees" — the cultural/mindset
  shift precedes the cost-per-task tuning, in their telling. Useful
  talking point for a skeptical client, but note this is the vendor's own
  customer talking about the vendor's own product — treat as a persuasion
  device, not a finding.

## Enterprise ebook block closed (2026-07-15)

`Anthropic-enterprise-ebook-digital.pdf` is now fully processed. `pdftotext`
became available and the 35-page guide was reviewed in five chunks. Its
durable adoption, pilot, evaluation, rollout, and LLMOps material now lives in
[[enterprise-ai-adoption-and-production-roadmap]]. Product-generation details
and vendor customer claims remain clearly tiered there rather than folded into
this platform inventory.

## Why this matters for this wiki / `.ROOT`

Mostly: it doesn't, yet — and that's the honest finding, not a gap to
paper over. `.ROOT` has no CI/CD pipeline, no GitHub Actions or GitLab CI
usage, no team Slack, and runs on Windows (ruling out computer use). Two
things are worth carrying forward anyway:

- **The `CLAUDE.md`-as-steering-lever pattern is vendor-universal**, not
  just a `.ROOT` convention — every CI surface (Actions, GHES, GitLab) uses
  the repo-root `CLAUDE.md` the same way `.ROOT` uses its own. Confirms the
  architecture rather than changing it.
- **Revisit trigger**: if a `02-LIBRARY\.PROJECTS` build ever goes to
  GitHub with real CI, GitHub Actions' `/install-github-app` quick-setup
  and the Code Review companion feature (not read in this chunk) are the
  first things to read properly — this page is inventory-depth, not
  implementation-depth, for that scenario.
- The Thomson Reuters four-point professional-grade-AI checklist is
  usable now, independent of the CI/CD material, in `05-BUSINESS` client
  conversations about AI tool vetting.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
