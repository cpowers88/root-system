---
type: research
tags: [ai-automation, openai, cli, sdk, agent-builder, tooling]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, relocated from CASTLE July 12, 2026) — SDKs and CLI, OpenAI CLI, Node reference
---

# OpenAI Developer Tooling — SDKs, the `openai` CLI, and Agent Builder

**Official OpenAI documentation, read in full July 12, 2026.** Companion to
[[openai-responses-api-state-and-streaming]], which covers the Responses
API's mechanics; this page covers how developers actually reach that API —
SDK install paths, the shell-native `openai` CLI (a genuinely reusable
batch-scripting pattern), and Agent Builder's node vocabulary (deprecated,
inventory-only).

## One-paragraph summary

OpenAI's own SDK/CLI guidance draws an explicit line matching `.ROOT`'s own
subagent-vs-scripted-tool instinct: **use the CLI for repeatable API work
you want to inspect and rerun** (batch extraction, file transforms,
deliberate model selection) **and subagents for work that still needs
judgment** (exploring code, comparing hypotheses, debugging, reviewing
changes) — stated explicitly as "CLI vs subagents for Codex," confirming
this pack's tooling guidance is written with Codex's own operating model in
mind, not just generic API consumers. The `openai` CLI's `--transform`
(GJSON path extraction) plus `--format` pattern is the single most reusable
concrete artifact in this chunk. Agent Builder — a separate visual workflow
canvas — is being deprecated (shutdown November 30, 2026) and is recorded
here for completeness, not as something worth learning now.

## `Node reference` is mislabeled — filename defect

**Flagging, not silently fixing** (raw/ is immutable): the file named
`Node reference  OpenAI API.md` is not a Node.js/JavaScript SDK reference —
its actual content is the **Agent Builder node catalog** (a visual
workflow-canvas tool, unrelated to the Node.js runtime). Same class of
defect as `CLI_USE.md` in the Claude Code pack turning out to be "computer
use," not CLI usage (see [[claude-code-integration-surface-and-platform]])
— worth knowing if either raw file is ever searched by filename rather than
content.

## SDK install path — thin and unremarkable

Official first-party SDKs: Node/TypeScript (`npm install openai`), with the
Agents SDK as a separate package for code-first orchestration (handoffs,
tools, guardrails, tracing, sandboxing) layered on top of direct API calls
— the guide explicitly frames Agents SDK as "when you need X" rather than
a universal default, mirroring Claude Code's own extension-trigger-table
philosophy (see [[claude-code-workflows-and-sessions]]). Azure maintains
compatible libraries for .NET/JS/Java/Go; a long tail of community SDKs
(Rust, Kotlin, Swift, PHP, Elixir, Scala, Dart, Clojure, Delphi, Unity,
Unreal) exist unverified by OpenAI — "use at your own risk," stated
plainly.

## The `openai` CLI — the reusable pattern

Installed via Homebrew or `go install`; reads `OPENAI_API_KEY` from the
environment (or `OPENAI_ADMIN_KEY` for Admin endpoints, `OPENAI_BASE_URL`
to redirect to a compatible host). Structure worth internalizing:

- **`--format`**: `auto`, `json`, `jsonl`, `pretty`, `raw`, `yaml`, `explore`
  — controls how the full response object prints.
- **`--transform`**: a **GJSON path** applied to the response before
  printing — e.g. `output.#(type=="message").content.0.text` selects just
  the assistant's text, skipping past reasoning/tool-call items that
  aren't at a fixed array index. This is the load-bearing pattern: because
  Responses output is a typed, heterogeneous array (not a guaranteed
  `output[0]`), every worked example in this doc selects by `type` rather
  than by position.
- **YAML heredocs for anything multiline or structured** (prompts, tool
  definitions, file references) — flags alone risk the parser
  misinterpreting a prompt containing `:` or `{}` as YAML syntax rather
  than literal text. The documented workaround is piping a
  programmatically-built YAML body into the command via `printf`/`sed`
  rather than fighting flag-escaping.
- **Batch pattern, verbatim from the source**: loop over local files,
  call `openai responses create` with a JSON-schema-constrained
  `--text.format` per file, transform to extract the structured array, and
  append one JSON object per record to a growing `.jsonl` file via `jq`.
  This is a complete, working recipe for "extract structured data from many
  local documents into one line-delimited file" — directly parallel in
  *shape* (not implementation) to how this wiki's own forked research
  ingests batch through parallel Claude Code agents rather than a shell
  loop.
- **Other command families**: `openai files create` (upload, capture
  `file_id` via `--transform id`), `openai images generate`/`edit`
  (base64-encode-then-decode pattern, since native `--output` support for
  images doesn't exist yet), `openai audio:speech create` / `audio:transcriptions
  create` (TTS and transcription, with a response-format table for
  plain text vs. subtitles vs. word-timestamps vs. speaker-diarized
  output), and `openai admin:organization:*` for provisioning
  projects/service-accounts/API keys programmatically (explicitly flagged:
  "be careful about giving unvetted actors access to admin keys").

## Agent Builder node reference — deprecated, inventory only

A visual workflow canvas (nodes + connections), **scheduled to shut down
November 30, 2026** — ChatKit survives the deprecation, Agent Builder does
not. Node families for reference only, no action implied:

- **Core**: Start (defines workflow inputs, exposes `input_as_text`),
  Agent (instructions/tools/model config — the guide recommends keeping
  each agent narrowly scoped rather than one do-everything agent), Note
  (non-functional documentation).
- **Tools**: File search (vector-store retrieval), Guardrails (pass/fail
  input monitors for PII/jailbreaks/hallucination — the guide recommends
  ending the workflow or looping back with a safety reminder on failure,
  not silently continuing), MCP (third-party tool/service connections).
- **Logic**: If/else and While, both driven by Common Expression Language
  (CEL) conditions; Human approval (defers to an end-user before a
  consequential step — the guide's worked example is literally "draft an
  email, pause for approval, then send via an MCP Gmail node," the same
  draft-then-gate shape as the Responses API's `interruptions`/`state`
  pattern documented in [[openai-responses-api-state-and-streaming]]).
- **Data**: Transform (reshape output types/shapes between nodes), Set
  state (global workflow variables).

## Why this matters for this wiki / `.ROOT`

- **The CLI batch-extraction pattern is the one concretely reusable idea
  here**, independent of the Agent Builder deprecation or SDK inventory.
  If `.ROOT` or a Capability Library asset ever needs to run the same
  structured-extraction prompt across many local files (e.g., batch-tagging
  a folder of client field notes, or extracting structured findings from
  a folder of raw research captures), the `--transform` + YAML-heredoc +
  `jq`-append-to-JSONL shape is a complete, tested recipe to adapt —
  whether via the actual `openai` CLI or as a design pattern reimplemented
  against Claude's own `claude -p --output-format json` batch mode (see
  [[claude-code-workflows-and-sessions]], which documents the Claude-side
  equivalent).
- **"CLI vs subagents for Codex" is external validation of a distinction
  `.ROOT` already draws informally**: use a scripted, rerunnable tool for
  mechanical repeatable work, use an agent (subagent/fork) when the task
  needs judgment. Worth citing directly if this wiki ever formalizes its
  own extension-trigger heuristic further.
- **No action item from Agent Builder** — it's being deprecated inside the
  year, and `.ROOT` was never a user of it. Recorded for completeness only,
  matching this pack's honest "no current use case" disposition elsewhere
  (see [[claude-code-integration-surface-and-platform]]).
- Companion page: [[openai-responses-api-state-and-streaming]] covers the
  API mechanics this tooling surface calls into.

---
*Processed July 12, 2026. Source in `raw/OPEN_AI-CHATGPT_CODEX_FILES/` (immutable).*
