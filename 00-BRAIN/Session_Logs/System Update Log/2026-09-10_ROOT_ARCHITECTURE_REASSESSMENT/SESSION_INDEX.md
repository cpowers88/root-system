---
type: report
timeline: log
status: research-complete-plan-proposed-pending-live-test
tags: [system-design, runtime, knowledge-management, ai-automation]
created: 2026-09-10
updated: 2026-09-10
check_at: 2026-09-20
---

# `.ROOT` Architecture Reassessment and Karpathy LLM-Wiki Repository Scan

## Living system landscape

The broader capability map, platform-family taxonomy, 29-candidate comparison,
evaluation scorecard, research protocol, research waves, and proposed boundary between
the future active system and `.ROOT` are maintained in
[`PERSONAL_AI_SYSTEM_LANDSCAPE.md`](PERSONAL_AI_SYSTEM_LANDSCAPE.md).

It is an evidence-organizing research artifact, not a platform selection or install
plan. Its central working boundary is that `.ROOT` may research and propose profitable
applications of demonstrated capability, but only the human can promote a proposal
into the active system.

## Full greenfield plan

The purpose, evidence review, source verification, architecture decision, concrete
minimal structure, learning-to-profit loops, growth controls, staged pilot, scorecard,
and `.ROOT` transition policy are documented in
[`GREENFIELD_LEARNING_TO_PROFIT_SYSTEM_PLAN.md`](GREENFIELD_LEARNING_TO_PROFIT_SYSTEM_PLAN.md).

Its decision is to pilot a physically separate, file-first action spine with a small
Karpathy-style library while preserving `.ROOT` intact as a reference and learning
platform. No implementation, installation, migration, or `.ROOT` structural change was
authorized or performed by the plan.

## Outcome

This work now has two separate tracks. The current `.ROOT` session is a control test of
the existing runtime with no folder changes. The repository search is for a possible
greenfield successor built small from the beginning; it is not a search for packages to
install into `.ROOT`.

The first live `.ROOT` observation is already negative: initial loading feels slow and
clunky. The final task outcome is not yet recorded, so this does not by itself settle the
architecture decision. It does directly challenge the runtime's promise of low-friction
orientation and must not be explained away by technical health results.

The operator also cannot yet comprehend the whole structure, what every part does, or
whether the system grew around real needs versus early assumptions. Human
comprehensibility is a required property of an operating system. Passing lint, routing
correctly for an agent, or preserving useful research cannot substitute for it.

The working decision is therefore:

> **Continue the unchanged `.ROOT` control test far enough to measure its useful output,
> while independently designing a small greenfield candidate from current Karpathy-style
> repositories. Do not install, migrate, or bulk-copy knowledge yet.**

The most promising future architecture is a two-layer system:

1. a small, human-comprehensible active core for current commitments, projects, areas,
   and proven procedures;
2. `.ROOT` as the durable research, evidence, history, and reference platform.

`.ROOT` may still earn both roles. The Claude session begun September 10 is measuring
that possibility. The repository scan below is evaluated solely as input to the new
system design.

## Why the decision changed

The September 10 optimization report concluded that `.ROOT` should keep its
macro-architecture and improve retrieval observability, diagnostic tests, and recovery.
That conclusion was sound from the evidence then available, but it treated agent routing
and evidence integrity as the primary acceptance criteria.

The operator then supplied a more fundamental constraint: `.ROOT` may have grown large
before the operator understood enough to choose its architecture, and the complete
system is not presently comprehensible as a whole. The first Claude test also began with
slow, clunky loading. These are direct operating observations. They mean “keep” must
become an option to prove, not the default.

This does not imply that the accumulated material is bad. It separates two questions
that had been coupled:

- Is `.ROOT` a valuable reference and research platform? **Probably yes.**
- Is `.ROOT` the best daily human operating interface? **Unproven.**

The distinction protects the useful knowledge while allowing a genuinely small system
to be tested without a forced migration.

## Architecture options now under consideration

| Option | Benefit | Main risk | Current position |
|---|---|---|---|
| Repair `.ROOT` in place | Preserves owners, evidence, safeguards, and history | Inherited complexity can keep shaping every proposed fix | Test now; no presumption of success |
| Replace `.ROOT` immediately | Maximum initial clarity | Loses working safeguards and invites an untested rebuild | Reject now |
| Small active core with `.ROOT` as reference | Clean, reversible learning while preserving prior knowledge | Duplicate truth if ownership boundaries are vague | Recommended next pilot if salvage test fails or human comprehension remains poor |

A future small core should be able to fit on one screen:

```text
HOME.md       whole-system map, purpose, and current orientation
NOW/          current commitments and immediate next actions only
PROJECTS/     bounded outcomes with completion conditions
AREAS/        continuing responsibilities
PLAYBOOKS/    procedures that have proved useful in real work
INBOX/        temporary undecided inputs
ARCHIVE/      inactive completed material
```

Research and source material would remain in `.ROOT`. The active layer would link to it
when needed and would not re-ingest the vault. Only information demanded by real work
would be promoted into the small core.

This is a proposal shape, not an approved build. Moving active ownership would be a
consequential system change and requires a separate impact review and explicit approval.

## Karpathy's actual LLM-Wiki pattern

Andrej Karpathy's original April 2026 idea file is deliberately not a product or fixed
folder taxonomy. It describes a pattern to instantiate with an agent according to the
domain and operator's preferences.

The [original gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
defines three layers:

1. **Raw sources:** curated and immutable; the LLM reads but never modifies them.
2. **Wiki:** LLM-generated Markdown summaries, entities, concepts, comparisons, and
   synthesis; the LLM maintains this layer.
3. **Schema:** `CLAUDE.md`, `AGENTS.md`, or equivalent instructions defining structure,
   conventions, and ingest/query/maintenance workflows.

Its core operations are ingest, query, and lint. It recommends `index.md` for content
navigation and `log.md` for chronological evolution. Karpathy reports that an index can
work at moderate scale—around one hundred sources and hundreds of pages—before a search
engine becomes necessary. He personally prefers one-source-at-a-time ingestion with
human involvement and explicitly says the exact directory structure and tools should be
developed collaboratively for the operator's domain.

`.ROOT` already implements most of this pattern:

- immutable `raw` evidence;
- maintained Markdown wikis;
- indexes and append-only logs;
- section schemas and operating files;
- agent instruction files and skills;
- query-first use of maintained pages, followed by evidence when needed;
- lint, contradiction, frontmatter, and ownership checks.

The difference is scope. `.ROOT` is not only an LLM wiki. It is simultaneously a
personal operating system, school environment, strategy layer, business workspace,
research collection, instruction runtime, evidence refinery, and historical record.
The current architecture question is whether those functions need one visible human
surface even if they share one underlying reference system.

## Current repository landscape — September 10, 2026

The ecosystem has expanded rapidly. The
[Awesome LLM Wiki](https://github.com/gavischneider/awesome-llm-wiki) catalog now spans
blueprints, applications, compilers, skills, ingestion utilities, MCP servers, templates,
reference vaults, and research. Repository popularity and commit counts below are only
rough activity signals; they do not prove quality, safety, or fit.

### Greenfield shortlist

| Repository | Current shape | Visible activity signal | Most useful lesson | Greenfield use |
|---|---|---:|---|---|
| [ddenzu/karpathy-llm-wiki-second-brain](https://github.com/ddenzu/karpathy-llm-wiki-second-brain) | Public template with only `raw/`, `wiki/`, index, log, schema, and commands; uses Work, Learning, Thinking, and Decisions as index axes rather than folder trees | Early public template | Keep folders minimal and let one visible map carry the conceptual structure | **Best structural starting reference** |
| [jackwener/llm-wiki](https://github.com/jackwener/llm-wiki) | TypeScript CLI; tiny `AGENTS.md`/`CLAUDE.md`; four focused skills; Markdown, sources, schema, log; BM25 with optional vector search | 100 stars, 9 forks, 30 commits | Keep boot files small and move ingest/query/lint/research into on-demand skills | **Best agent-operation reference** |
| [pawel-cell/llm-wiki-agent](https://github.com/pawel-cell/llm-wiki-agent) | Minimal `sources/`, `wiki/`, and one instruction file | 14 stars, 1 fork | Establish the minimum viable system before adding abstractions | **Best simplicity control** |
| [tyroneross/ai-operating-system-quickstart](https://github.com/tyroneross/ai-operating-system-quickstart) | File-based personal/work templates with raw, wiki, brain, system, outputs, simple local search, and privacy checks | 0 stars, 4 commits | Shows how active work and Karpathy-style reference pages can coexist without a service stack | **Closest full greenfield template, but too opinionated to copy whole** |
| [lawyer112/personal-os-wiki](https://github.com/lawyer112/personal-os-wiki) | Separate Personal OS, Personal Wiki, and Agent Guide; tasks, reviews, and evidence backed by web apps and PostgreSQL | 7 stars, 1 fork, 59 commits; early release | Explicitly separates execution state, knowledge, and agent protocol | **Best conceptual two-layer reference; far too complex to start from** |
| [frankchu91/mindbase-llm-wiki](https://github.com/frankchu91/mindbase-llm-wiki) | Local web UI and MCP server; Ollama support; proposed wiki edits shown for approval before write | 99 stars, 13 forks, 84 commits; early access | Human review should be a visible product surface, not a hidden agent promise | **Best interface and approval reference** |
| [microsoft/llmwiki](https://github.com/microsoft/llmwiki) | Microsoft VS Code extension with raw/wiki/schema layers, sidebar views, backlinks, Copilot-powered ingestion, MCP, and lint | Microsoft repository; 9 forks at review | Human browsing and agent operations can share a visible editor interface | **Study UI; reject Copilot/VS Code dependency as the foundation** |
| [ChavesLiu/second-brain-skill](https://github.com/ChavesLiu/second-brain-skill) | Karpathy pattern packaged as a Claude/ChatGPT skill with natural-language commands | 43 stars, 9 forks, 6 commits | A knowledge system can be invoked as a focused capability instead of dominating every session | **Useful skill-interface reference** |
| [TacoTakumi/agent-wiki](https://github.com/TacoTakumi/agent-wiki) | One shared Markdown vault exposed through CLI and skills; optional network service | 11 stars, 260 commits | A reference vault can serve separate projects without becoming each project's active workspace | **Possible future reference interface** |
| [Labhund/llm-wiki](https://github.com/Labhund/llm-wiki) | Markdown plus search manifest, viewports, MCP, attributed Git sessions, background quality agents | 27 stars, 2 forks, 522 commits | Retrieval traces, page slicing, and Git-attributed writes are valuable at scale | **Advanced pattern library only** |
| [Ekgardt/llm-wiki](https://github.com/Ekgardt/llm-wiki) | Cross-agent MCP memory, lifecycle adapters, session capture, background compilation, citation verification | 3 stars, 1 fork | Verify-before-write and evidence generations address memory drift | **Verification reference; exclude auto-injection initially** |
| [NDOTO-G/doc.html](https://github.com/ndoto-g/doc.html) | Single-document format with in-band manifest, section sizes, stable addresses, and hashes | 0 stars, 16 commits | “Give the model a map, not a pile”; make selective loading and integrity visible | **Borrow the manifest idea; retain Markdown** |

### Other current branches of the ecosystem

The broader catalog contains several families that should not be conflated:

- **Minimal templates and schemas:** folders plus agent instructions, with little or no
  runtime code. These are best for learning the operator's natural structure.
- **Skills and plugins:** ingest, query, lint, or research procedures installed into
  Claude Code, Codex, Cursor, or other agents. These can keep permanent boot context
  small.
- **Local applications:** web or desktop interfaces that make proposed changes,
  backlinks, and sources visible. MindBase is the clearest current example for the
  human-review problem.
- **Wiki compilers:** CLIs and watchers that parse mixed files, generate pages, build
  indexes, and run lints. These are useful when manual file retrieval repeatedly fails.
- **Agent-memory platforms:** session capture, ambient writeback, automatic
  consolidation, graphs, and multi-agent MCP surfaces. These solve a different problem
  and create the highest drift and complexity risk.
- **Integrity and interchange formats:** OKF bundles, manifest-driven documents, source
  hashes, and rebuildable projections. These are useful components, not necessarily an
  operating system.

## What the repositories imply for the new system

### 1. The clean start should begin with a schema, not a platform

The original gist, the minimal templates, and the more mature skill-based CLI support
the same sequence: define purpose, preserve sources, create a small map, and add tools
only after actual retrieval friction. A greenfield pilot should therefore start as
files and a concise agent contract. Installing an application first would let the
application's ontology shape the system before the operator learns what is needed.

### 2. Human comprehension needs its own interface

MindBase's strongest idea is not its local model or web server. It is the ingest review
surface: the system shows takeaways and a checklist of proposed wiki edits before
writing. The new system should begin with a compact human-facing map and visible change
preview, even if both are plain Markdown at first.

### 3. Active work and durable knowledge are different products

Personal OS + Personal Wiki makes the distinction explicit: execution state says what
is unfinished and who owns it; the wiki preserves durable evidence and knowledge; the
agent guide defines behavior. Agent Wiki separately shows that one reference vault can
serve many projects. The new system should borrow that separation without adopting the
PostgreSQL, Docker, API, heartbeat, or multi-service machinery.

### 4. Advanced maintenance should arrive last

Labhund and Ekgardt contain sophisticated ideas—viewports, manifests, cited queries,
verification agents, session capture, and background compilation. They also recreate
the complexity being escaped. Their techniques should be borrowed only in response to
measured failures. They are not suitable foundations for a system whose first
requirement is that its operator comprehend the whole structure.

### 5. No repository should be adopted wholesale

No reviewed repository proves that its agent-generated structure remains correct and
comprehensible for a one-person, multi-domain system over years. Most are young, some
are explicitly early access, and repository activity is not outcome evidence. The new
system should be a small synthesis built for this operator, not a renamed clone.

## Greenfield design direction from the repository scan

The strongest starting combination is:

- **Karpathy's three-layer truth model:** immutable sources, maintained knowledge,
  concise schema.
- **ddenzu's map-first structure:** Work, Learning, Thinking, and Decisions as visible
  index views rather than deep folder hierarchies.
- **jackwener's operation split:** ingest, query, lint, and research as focused skills
  loaded on demand.
- **Personal OS + Personal Wiki's boundary:** active execution state is not the same
  thing as durable knowledge.
- **MindBase's human gate:** show proposed knowledge changes before applying them.
- **NDOTO-G's navigation principle:** give the reader a small map and load only selected
  sections.

An initial filesystem should stay close to this size:

```text
START.md               complete map and plain-language explanation
ACTIVE/
  NOW.md               current commitments and next actions
  PROJECTS/            only projects currently being executed
  AREAS.md             continuing responsibilities and constraints
KNOWLEDGE/
  INDEX.md             Work · Learning · Thinking · Decisions views
  pages/               durable maintained knowledge only
SOURCES/
  inbox/               material intentionally selected for possible use
  processed/           immutable sources already compiled
OUTPUTS/                useful deliverables; not canonical until promoted
ARCHIVE/                inactive material
AGENTS.md               short cross-agent pointer and hard boundaries
CLAUDE.md               short pointer for Claude
skills/                 ingest, query, lint, research; added only as needed
```

This is a research conclusion, not an authorized build. Before creating it, the
structure should be reduced further if every item cannot be explained from `START.md`
in two minutes. No `.ROOT` files should be copied into it at initialization. The first
content should come from a real task, followed by only the reference material that task
actually demands.

## Separate `.ROOT` control test

The Claude session already under way is a test of `.ROOT` without folder changes. It is
not a pilot of any repository above. The first observation is **slow and clunky initial
loading**. Continue only far enough to learn whether that loading eventually buys a
meaningfully better result.

To preserve the remaining value of the test:

1. Do not change folders or runtime instructions during the task.
2. Let Claude complete the work far enough to produce a useful result, unless loading
   never resolves into action.
3. Observe, without coaching where possible:
   - what it reads before acting;
   - approximate time or turns before the first useful action;
   - whether it finds the correct owner;
   - whether it repeats loading later in the same task;
   - whether it asks useful versus procedural questions;
   - whether it reconstructs settled work;
   - whether it produces the requested output;
   - whether the operator understands what the system is doing.
4. After the task, ask Claude to read this update and the runtime rewrite report, then
   write a retrospective named `CLAUDE_TEST_RESULT.md` in this directory. The
   retrospective should identify the first failing transition, if any, and recommend
   keep, modify, or revert without changing system files.

The test is about both participants. A session can route correctly and still fail if the
operator cannot understand or trust the path it took.

## September 20 decision rule

| Evidence | Decision |
|---|---|
| Claude routes correctly, useful work clearly repays loading cost, and the operator can explain the system | Salvage `.ROOT`; make only small interface or routing changes |
| Claude routes correctly but the operator still cannot comprehend the system | Preserve `.ROOT` as reference; pilot a small active core |
| Loading remains slow or repetitive, but the failure is isolated to one repairable boot transition | Modify the smallest route or owner and retest |
| Agent failures and human burden remain broad after bounded repair | Begin the clean active-core pilot; keep `.ROOT` intact as reference |

No pass condition allows technical correctness to overrule persistent human
incomprehensibility.

## Current boundaries

- No governance, active owner, folder structure, or runtime file changed in this review.
- No external repository was cloned, installed, executed, or granted access.
- `88-JOURNAL` and every `raw` directory remained untouched.
- The September 6 runtime remains on probation through September 20.
- The `.ROOT` test and greenfield repository research are separate evidence tracks.
- Slow and clunky initial Claude loading is recorded as the first live test observation;
  the task's final usefulness is still pending.
- A likely future change is acknowledged, but its shape remains evidence-gated.
- The earlier comprehensive evidence review remains at
  `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\system-evolution\root-optimization-research-2026.md`.
- The runtime change under test remains documented at
  `00-BRAIN\Session_Logs\System Update Log\2026-09-06_ROOT_RUNTIME_REWRITE\SESSION_INDEX.md`.

## Next exact action

Finish the current unchanged Claude task far enough to compare loading cost with useful
output. Then have Claude read this packet and record `CLAUDE_TEST_RESULT.md` here. The
greenfield design remains research-only until that control result is captured.
