---
type: research
tags: [ai-automation, claude-code, prompting, patterns]
source: raw/CLAUDE_FILES/PROMPT_LIBRARY.md (official Claude Code docs, 1,389-line prompt-card dataset; inventoried but never actually read in the July 11 CASTLE-era ingest — read in full in this pass)
---

# Claude Code Prompt Library — Reusable Prompt Patterns

**Official prompt library (52 copy-paste prompt cards), read in full for the
first time in this pass.** Not a set of one-off examples worth transcribing —
the value is the *structure* the cards share and six named principles for what
makes a prompt reusable, both directly applicable to how `.ROOT` itself writes
its own recurring-task instructions (skills, HAT files, session-close prompts).

## One-paragraph summary

The library organizes 52 prompts across a five-stage SDLC axis (discover → design
→ build → ship → operate) and 15 task categories (Understand, Plan, Prototype,
Implement, Test, Debug, Refactor, Review, Git, Release, Incident, Automate, Data,
Onboard, Steer), each tagged by which non-engineering roles it also serves (pm,
design, docs, marketing, data, ops, security). Every card is a **template with
named slots** (`{path}`, `{feature}`, `{target}`) rather than a fixed string —
the reusability comes from parameterization, not the literal wording. The
closing "What makes these prompts work" section names six patterns that explain
*why* the templates are effective, independent of any single card.

## The card structure (the reusable part)

Each entry is a small structured record, not prose:

```text
id, sdlc-stage, category, roles: [], prompt: '...with {slots}',
slots: { key: 'example value' }, src: (which source doc it traces to)
```

- **Template + example, not instruction alone.** Every slotted prompt ships
  with a concrete filled-in example (`{path}` → `src/scheduler/queue.ts`), so
  the reader sees both the abstract pattern and a working instance in the same
  breath.
- **Role-tagged, not engineering-only.** Roles beyond `pm` appear throughout:
  `design`, `docs`, `marketing`, `data`, `ops`, `security` — e.g. a `design`-tagged
  card is "implement this design, then screenshot the result, compare it to the
  original, and fix any differences" (paste-a-mockup-in workflow), and a
  `marketing`-tagged card exists for content/analytics tasks. The library treats
  Claude Code as a cross-functional tool, not solely a coding tool.
- **Traceable provenance.** Every card names its source doc (`best-practices`,
  `workflows`, `teams`) — each card is a distilled instance of a rule documented
  elsewhere, not a standalone invention.

## Six patterns for what makes a prompt work (the durable content)

1. **Describe the outcome, not the steps.** `"add rate limiting to the public
   API and make sure existing tests still pass"` — works without naming a file,
   because Claude finds the files itself.
2. **Give it a way to check its own work.** Ask for run/test/compare/verify in
   the same prompt so Claude iterates instead of stopping after one attempt —
   `"write the migration, run it against the dev database, and confirm the
   schema matches"`.
3. **Point at a reference.** Name an existing file/test/pattern to match, so
   new work is consistent with what already exists — `"add a settings page
   that follows the same layout as the profile page"`.
4. **State the measurable target.** For performance/coverage goals, give the
   metric and threshold so "done" is unambiguous — `"get the bundle size under
   200KB and show me what you removed"`.
5. **Give it the artifact, not a description of it.** Paste errors/logs/
   screenshots directly, or `@`-reference a file — `"why is the build failing?
   @build.log"`.
6. **Say how you want the answer.** Name format, length, or audience so the
   output fits its actual use — e.g. request an HTML page with a diagram
   instead of prose, or set an output style as the standing default.

## Candidate `.ROOT` mappings (ideas, not commitments)

Three card types map to real recurring `.ROOT` tasks closely enough to be worth
naming as future skill/prompt candidates:

- **`capture-what-to-remember`** ("Claude knows what it had to figure out this
  session and proposes CLAUDE.md entries so the next session starts with that
  context") — directly parallels `.ROOT`'s session-close ritual and DAILY/HANDOFF
  discipline. A slotted version of this card is a plausible addition to the
  `session-close` skill: end-of-session, ask explicitly what should be captured
  before it's lost, rather than relying on the session to remember to log it.
- **`turn-a-meeting-into`** ("read {input} and write up the action items, then
  create a {tracker} ticket for each with acceptance criteria") — the same
  template shape fits routing a weekly/monthly castle review or a wiki-lint
  finding batch into concrete next actions, with "tracker" swapped for
  `SYSTEM_FLAGS` or a `NOW.md` update instead of Linear/Jira.
- **`connect-a-tool-with`** (MCP) — "connect the source once instead of pasting
  data every session" — conceptually validates why `.ROOT` treats MCP servers
  (Gmail, Drive, Notion, etc.) as standing connections rather than one-off pastes;
  no action needed, just confirms the existing practice.

None of these are drafted as skills — flagging them here per this wiki's
research-and-propose charter; promotion to an actual skill file needs a real
`wiki/proposals/` entry and Chris's review, same as any other governance-adjacent
change.

## Why this matters for this wiki / `.ROOT`

- **The six patterns are a reusable prompting checklist**, applicable the next
  time `.ROOT` writes a skill file, HAT file, or CASTLE brief — "does this
  instruction describe the outcome, give a self-check, point at a reference,
  state a measurable target, supply the artifact, and specify the answer
  format?" is a fast five-second audit for any instruction file, not just chat
  prompts.
- **The slotted-template structure is the same shape `.ROOT` already uses**
  informally in section operating files (a pattern + a worked example) — this
  page is external validation of that convention, similar to how
  [[mcp-landscape-architecture-and-patterns]] validated the router pattern.
- The role-tagging (pm/design/docs/marketing/data/ops/security) is a reminder
  that Claude Code's own vendor documentation treats it as a cross-functional
  tool — relevant context if a future client conversation needs the "this
  isn't just for developers" framing.

---
*Processed July 12, 2026. Source in `raw/CLAUDE_FILES/` (immutable).*
