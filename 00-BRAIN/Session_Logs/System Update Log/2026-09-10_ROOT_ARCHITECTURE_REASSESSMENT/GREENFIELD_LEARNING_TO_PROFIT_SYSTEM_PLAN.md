---
type: report
timeline: reference
status: proposed
tags: [system-design, learning, business, knowledge-management, ai-automation]
created: 2026-09-10
updated: 2026-09-10
check_at: 2026-09-20
---

# Greenfield Learning-to-Profit System Plan

## Executive decision

The best route is to design and pilot a new, physically separate, very small daily
system while preserving `.ROOT` intact as a reference platform, research library,
governance case study, and source of lessons. The new system should not be a second
attempt at an all-encompassing personal operating system. It should be an action spine
that grows only when real school, skill, or business work proves that another component
is needed.

The recommended architecture combines two complementary ideas:

1. **An action layer organized around bounded projects and the next useful action.**
   This borrows the actionability of PARA without adopting a large subject taxonomy.
2. **A Karpathy-style reference layer containing immutable sources, an AI-maintained
   wiki, and a concise operating schema.** This layer supports research and accumulated
   understanding but does not own unfinished work.

Obsidian is recommended as an optional human interface over ordinary Markdown files,
not as the system's database or governing architecture. No LLM-wiki plugin, vector
database, background memory process, bulk ingest, or automated reorganization should
be installed during the first pilot.

This decision is deliberately reversible. `.ROOT` is not deleted, moved, or mass
migrated. The new system earns responsibility one real workflow at a time.

## Purpose

The system exists to help a systems-engineering student become more capable and convert
that capability into valuable, eventually highly profitable work. It must connect four
things that are often kept separate:

- academic obligations and systems-engineering knowledge;
- programming and computer-usage skill development;
- artifacts that demonstrate useful capability;
- customer evidence, offers, delivery, and revenue.

The system succeeds when it helps produce better grades, stronger technical skill,
finished artifacts, validated business opportunities, satisfied users or customers,
and revenue. A cleaner folder tree, a larger wiki, or a more impressive graph is not an
outcome by itself.

Kennesaw State's Industrial and Systems Engineering department describes its domain as
solving problems, integrating multifunctional systems, optimizing processes, and
meeting quality, cost, and output goals. The current degree offers Industrial and
Systems Engineering concentrations and several related graduate pathways. That is an
excellent match for a system centered on real processes, measurements, and economic
outcomes rather than note accumulation. See the [KSU department overview](https://campus.kennesaw.edu/colleges-departments/spceet/academics/industrial-systems-engineering/index.php)
and [2026–2027 advising page](https://campus.kennesaw.edu/current-students/academics/academic-advising/explore-majors/industrial-systems-engineering.php).

## Problem statement

`.ROOT` accumulated many useful ideas, safeguards, research collections, operating
files, and agent instructions before its operator had enough experience to decide which
parts were genuinely necessary. The result is a system that can be technically healthy
yet still feel slow, clunky, and difficult to comprehend as a whole.

The central failure was not ambition. It was allowing anticipated future needs to
create present structure. That produced several coupled problems:

- the system became an object of continual redesign instead of a tool used to finish
  work;
- permanent structure was created before repeated behavior revealed natural owners;
- agent context, human navigation, durable knowledge, active commitments, and
  automation were combined into one visible surface;
- system sophistication became easier to measure than learning, delivery, or profit;
- accumulated material created migration anxiety and made a clean experiment feel
  costly.

The new design must therefore optimize for **comprehensibility, action, evidence, and
reversibility before completeness**.

## Research conclusions

### Karpathy's proposal is a knowledge architecture, not a personal operating system

The [original LLM-Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
defines three layers: immutable raw sources, an LLM-maintained Markdown wiki, and a
schema that teaches an agent how to ingest, query, and lint the wiki. It recommends an
index for content navigation and an append-only log for chronology. Karpathy reports
that a simple index works at moderate scale—roughly one hundred sources and hundreds of
pages—and personally prefers one-source-at-a-time ingest with human involvement.

The most important line for this decision is that the design is intentionally abstract:
directory structure, schema, page formats, and tools are optional and should fit the
domain and operator. Copying a repository wholesale would contradict that principle.

The Karpathy pattern is valuable for the new system's **library**, but it does not by
itself decide what to work on, how to learn a skill, how to validate an opportunity, or
how unfinished work should be owned.

### Structured files can help retrieval, but they do not maintain themselves reliably

Recent research supports structured, tool-navigable knowledge while warning against
assuming that organization automatically improves answers. A 2026
[filesystem-memory study](https://arxiv.org/abs/2607.26637) found that organized stores
roughly halved retrieval cost at large scale, but organization degraded for all but the
strongest management agent and did not itself improve answer quality. Tool choice
shaped the store as strongly as model choice.

[LongMemEval-V2](https://arxiv.org/abs/2605.12493) found that a coding agent gathering
evidence from files outperformed its strongest RAG baseline on environment-memory
questions, but incurred high latency. That result closely matches the current `.ROOT`
experience: files can preserve important operational context and still feel expensive
to load.

The [Retrieval-as-Reasoning LLM-Wiki paper](https://arxiv.org/abs/2605.25480) shows that
structured pages, bidirectional links, and iterative search/read/link-following can
outperform several graph and RAG baselines on multi-hop benchmarks. This supports a
maintained reference layer. It does not establish that a large personal operating
system should be loaded into every session.

[WiCER](https://arxiv.org/abs/2605.07068) demonstrates the main knowledge-compilation
risk: blind summarization can drop critical facts catastrophically. Diagnostic probes
and iterative refinement recovered much of the loss. Therefore, an AI-written wiki
must remain a derived layer with source citations, explicit uncertainty, and tests for
important claims—not a replacement for evidence.

### Established folder methods each solve only part of the problem

| Method | What it does well | Where it fails this use case | Decision |
|---|---|---|---|
| [PARA](https://fortelabs.com/blog/para/) | Organizes by actionability: Projects, Areas, Resources, Archives; keeps active outcomes close | Does not define provenance, AI ownership, learning verification, or customer validation | Borrow the project/resource/archive boundary |
| [Johnny.Decimal](https://johnnydecimal.com/documentation/introduction) | Stable locations, limited choices, spatial memory, master index | A detailed numbering taxonomy created too early can harden guesses into permanent structure | Consider stable top-level numbers only after the pilot proves the categories |
| [Zettelkasten](https://zettelkasten.de/overview/) | Atomic ideas, explicit links, structural notes, synthesis through writing | Can turn learning into note-production and fragment context; categories intentionally remain emergent | Borrow links and map notes; do not require atomic notes |
| [CODE / Second Brain](https://fortelabs.com/blog/basboverview/) | Capture, Organize, Distill, Express connects information to output | Capture can outrun expression and recreate a collection problem | Adopt “capture selectively” and make expression mandatory |
| [Karpathy LLM-Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Clear source/wiki/schema ownership and cumulative synthesis | It is a research-memory pattern, not a commitment or business-execution system | Use inside the library only |
| Obsidian | Local folder as vault, links, backlinks, graph, human browsing | Plugins and graph views can become a substitute for deciding owners and completing work | Use as a viewer/editor, initially with core features only |
| Vector database / RAG | Useful search accelerator for large corpora | Hidden chunking, index drift, extra infrastructure, and no human-comprehensible source of truth | Add only if measured search failures justify it |

PARA's own rationale is particularly relevant: if the organizational system is as
complex as life, maintaining it consumes the attention needed to live that life. Its
project-first approach is the correct execution spine, but its four folders should not
be copied mechanically.

Learning also needs an operation, not just storage. The U.S. Department of Education's
[study-learning practice guide](https://ies.ed.gov/ncee/wwc/practiceguide/1) supports
spacing, interleaving worked examples with problem solving, active retrieval, and deep
explanatory questions. The system should record attempts, errors, feedback, and
demonstrated performance—not merely class notes or AI summaries.

Profit requires external evidence. The National Science Foundation's
[I-Corps program](https://www.nsf.gov/funding/initiatives/i-corps) uses experiential
education and customer discovery to reduce commercialization risk. Its national
training asks teams to interview potential customers and stakeholders to test
product-market fit and inform the business model. The proposed system uses the same
principle at smaller scale: observed pain and customer behavior outrank internally
generated business ideas.

## Verification of the supplied repositories

The supplied list contained useful leads, but several claims needed correction.

| Supplied item | Verified current state | Design lesson |
|---|---|---|
| [GD4AI/obsidian-llm-wiki](https://github.com/GD4AI/obsidian-llm-wiki) | Active Obsidian plugin; the official listing reports roughly 46,000 downloads. The repository exposes ingest, query, lint, graph retrieval, source protection, multiple providers, and a headless CLI | Strong future interface experiment; too much behavior to make the initial foundation |
| [green-dalii/obsidian-llm-wiki](https://github.com/green-dalii/obsidian-llm-wiki) | Redirects to `GD4AI/obsidian-llm-wiki`; it is not a separate implementation | Count it once |
| [Obsidian Karpathy plugin listing](https://community.obsidian.md/plugins/karpathywiki) | Current official community listing for the GD4AI plugin | Useful evidence that the plugin is installable and used; not evidence of long-term personal-system fit |
| [Obsidian LLM Wiki by enduserlab](https://community.obsidian.md/plugins/llm-wiki) | Archived and no longer available after version 0.1.0 and one release | Do not use as a foundation; the earlier “production-grade alternative” description was overstated |
| [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | Claude Code template with L1 always-loaded memory and L2 on-demand wiki; 16 commits at review | Borrow the hot/cold context boundary and two-stage index routing; reject the eight-namespace starter schema and never store credentials in always-loaded Markdown memory |
| [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Original conceptual blueprint and active comment ecosystem | Treat it as a pattern catalogue, not a product specification |

The GD4AI plugin is currently the strongest ready-made Obsidian implementation in the
supplied set. It deliberately creates entity and concept pages, performs maintenance,
and can ingest folders and multiple files. Those strengths are exactly why it should
wait: the first pilot needs to reveal the natural shape of the system before software
begins manufacturing pages and relationships.

The MehmetGoekce repository contributes one excellent idea: a tiny hot layer loaded in
every session and a larger cold layer queried on demand. Its proposed L1 contains ten to
twenty files, however, which is already too large for this greenfield experiment, and
its suggestion to keep credentials in memory should not be adopted. Secrets belong in
an operating-system credential store or provider-managed secret mechanism, never in
ordinary personal-system Markdown.

## Architecture decision record

### Decision drivers

The system must:

1. be explainable from one page in under two minutes;
2. lead to the next useful action without a long orientation ritual;
3. keep active commitments separate from reference knowledge;
4. support school, skill development, and business without building three systems;
5. preserve source evidence and show when AI-written knowledge is derived or uncertain;
6. work with Claude, Codex, future agents, and ordinary human tools;
7. grow only in response to repeated, observed friction;
8. make system maintenance cheaper than the work it enables;
9. remain local, portable, readable, and versionable;
10. preserve `.ROOT` without forcing a bulk migration.

### Options

| Option | Strength | Failure mode | Decision |
|---|---|---|---|
| Continue repairing `.ROOT` as the only system | Retains current owners, history, and safeguards | Continues optimizing inherited complexity; current human comprehension and loading are poor | Keep as the control test, not the default future |
| Clone an LLM-wiki repository | Fast visible setup | Imports another designer's ontology and automation before needs are understood | Reject |
| Adopt the GD4AI Obsidian plugin immediately | Polished ingest/query/lint UI | Automated page growth could recreate the exact problem under a cleaner interface | Defer to a later sandbox test |
| Move to SaaS or a vector-first system | Fast search and convenient interfaces | Lock-in, opaque derived state, weak human map, and additional services | Reject as source of truth |
| Build a minimal local action spine plus derived library | Maximum comprehension, reversibility, and fit; keeps evidence visible | Requires discipline against adding structure and creates temporary dual-system risk | **Choose** |

### Chosen design

Create a separate local Git repository containing ordinary Markdown. Open it in
Obsidian if the visual interface helps, but keep it fully usable in File Explorer, an
editor, Claude, and Codex. Begin with this maximum structure:

```text
NEW-SYSTEM/
├── HOME.md                 whole-system map, purpose, boundaries
├── NOW.md                  current focus and next useful actions
├── INBOX/                  temporary captures awaiting a decision
├── PROJECTS/               bounded outcomes; one owner per commitment
├── LIBRARY/
│   ├── INDEX.md            compact map of maintained knowledge
│   ├── sources/            human-curated, immutable evidence
│   └── wiki/               AI-drafted, human-reviewable knowledge
├── SYSTEM/
│   ├── SPEC.md             non-loaded design and ownership reference
│   ├── METRICS.md          pilot observations and acceptance results
│   └── CHANGELOG.md        structural decisions and reversals
├── ARCHIVE/                inactive work; nothing is deleted
├── AGENTS.md               short universal rules and routing pointer
└── CLAUDE.md               short Claude pointer; no duplicated rulebook
```

This tree is a ceiling, not a launch checklist. `PROJECTS/`, `LIBRARY/`, and `SYSTEM/`
may begin nearly empty. No School, Business, Programming, People, Ideas, Tools, or
Research subfolder is created until real contents fail to route cleanly at least three
times.

School, skill, and business are **project kinds**, not permanent top-level silos. The
same project format can represent “pass the next exam,” “build a Python automation,” or
“test whether local businesses will pay for the automation.” This lets a skill flow
across contexts without copying its truth into three owners.

### Consequences

The benefit is a complete system that remains visible and explainable. The cost is that
some material will initially remain in `.ROOT` and must be queried or linked manually.
That cost is intentional: it prevents migration from becoming the next system-building
project.

The new repository and `.ROOT` must never become equal active authorities. During the
pilot, `.ROOT` retains current commitments that have not been explicitly transferred.
Each transferred commitment records a single cutover note. After a successful cutover,
the old owner is marked historical or linked to the new owner; it is not silently
maintained in both places.

## Operating model

### The action path

```text
Need, assignment, or observed pain
              |
              v
        NOW.md chooses focus
              |
              v
   one PROJECT with one outcome
        /         |          \
       v          v           v
   learn       build       test outside
       \          |           /
        \         v          /
         evidence and result
              |
       +------+------+
       |             |
       v             v
 useful output   durable lesson
 / customer      with source link
       |             |
       v             v
 PROJECT closes  LIBRARY updates
```

The library never determines the day's work. `NOW.md` and the selected project do.
Knowledge is retrieved because the project needs it; knowledge collection does not
manufacture projects merely to justify itself.

### Minimal project contract

Every active project needs only one owner note at first:

```markdown
# Project name

- kind: school | skill | business | personal
- outcome: observable end state
- why-now: reason this deserves attention
- done-when: objective completion condition
- next-action: one physical or digital action
- evidence: links to attempts, feedback, results, or customer behavior
- library-links: only references actually used
```

Additional folders or documents are added inside a project only when the work produces
them. Empty scaffolding is prohibited.

### Learning loop

For a school or programming skill project:

1. Define the performance to demonstrate, not the notes to collect.
2. Attempt a problem or small build before asking AI for the complete solution when
   safe and appropriate.
3. Use AI to explain, generate variants, review reasoning, and expose misconceptions.
4. Perform a closed-book retrieval or cold rebuild.
5. Record the miss, feedback, correction, and next repetition.
6. Produce a useful artifact: solved model, script, analysis, diagram, tutorial, or
   process improvement.
7. Ask whether the artifact solves a real person's costly problem. If yes, open a
   business-test project rather than merely tagging it “profitable.”

The library stores the durable explanation after competence has been tested. It does
not confuse an AI-generated explanation with learned capability.

### Profit loop

For a business project:

1. Start from observed recurring friction, delay, error, risk, or cost.
2. Identify a narrow user and the current workaround.
3. Conduct conversations or observations before building substantial software.
4. State a falsifiable value hypothesis: whose problem, what measurable improvement,
   and what behavior would show willingness to pay.
5. Deliver the smallest manual, spreadsheet, script, or automation that tests the
   hypothesis.
6. Measure time saved, errors reduced, throughput increased, risk lowered, or money
   made.
7. Ask for commitment: access, introduction, pilot, letter of intent, or payment.
8. Convert repeated delivery into a playbook or product only after the evidence repeats.

This loop makes profit a result of validated usefulness rather than a property assigned
to an idea in a planning file.

### Knowledge ingest

The human chooses each source. The default is one source at a time.

1. Place the source in `LIBRARY/sources/` only when a current project or recurring
   question justifies it.
2. AI extracts proposed takeaways with citations and identifies affected wiki pages.
3. The human accepts, edits, or rejects the proposed changes.
4. AI writes only to `LIBRARY/wiki/`, updates `INDEX.md`, and appends a short change
   record.
5. Important claims retain source, date, confidence, and scope.
6. A query reads `INDEX.md`, then the smallest relevant pages, then original sources if
   the decision is consequential or the wiki is uncertain.

No bulk import from `.ROOT` is allowed. A `.ROOT` item is promoted only because a live
project needed it and the item proved useful enough to deserve a new owner.

### AI authority

| Action | Human | AI |
|---|---|---|
| Choose goals, commitments, and sources | Owns | Advises |
| Decide today's focus | Owns | Recommends from visible evidence |
| Draft project work and artifacts | Directs/reviews | Executes within project scope |
| Update active next actions | Approves or explicitly delegates | May update only the active project |
| Draft wiki pages and links | Reviews important changes | Maintains derived knowledge |
| Change folder structure or governing rules | Explicitly approves | Proposes with evidence only |
| Contact people, spend money, publish, or use credentials | Explicitly approves | Never assumes authority |
| Reorganize or prune automatically | Prohibited during pilot | Prohibited during pilot |

The always-loaded AI contract should contain only non-negotiable safety boundaries, the
purpose, and the route from `HOME.md` to `NOW.md` to one project. Detailed workflows
become on-demand skills only after they repeat. OpenAI's
[AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and
Anthropic's [Claude Code memory guidance](https://code.claude.com/docs/en/memory) both
support scoped or imported instructions rather than one expanding universal file.

## Growth constitution

The following rules prevent another premature expansion:

1. **No speculative folders.** Add a folder only after three recorded routing failures
   that one clear container would solve.
2. **No speculative automation.** Automate only after a task has repeated at least five
   times, its stable steps are understood, and expected time or error savings are
   recorded.
3. **No rule without a failure.** Every new governing rule names the event it prevents,
   its owner, its test, and when it can be retired.
4. **No bulk ingestion.** One source at a time until measured demand proves a bounded
   batch is safer and more useful.
5. **No invisible durable writes.** AI-generated knowledge changes are reviewed or
   clearly marked unreviewed.
6. **No duplicate active owner.** Links may be many; the authoritative unfinished
   commitment is one file.
7. **No maintenance without a beneficiary.** System work must name the school,
   capability, delivery, or business result it enables.
8. **System work stays below ten percent of working time** across a normal month unless
   the system itself is a paid deliverable or explicit course project.
9. **Archive instead of delete.** Reversibility outranks neatness.
10. **A prettier interface does not justify a dependency.** Add software only after a
    specific measured failure and a rollback plan.

## Adoption plan

### Stage 0 — Preserve the control

Finish the current unchanged Claude `.ROOT` task far enough to record whether its
useful output repays the slow and clunky loading. Do not alter `.ROOT` structure during
that test. Record the first failing transition and final usefulness.

**Exit evidence:** `CLAUDE_TEST_RESULT.md` exists in the current reassessment packet and
states keep, modify, or revert with observations.

### Stage 1 — Build the minimum candidate

After explicit approval, create the separate repository with `HOME.md`, `NOW.md`, one
real project, the empty library boundary, a short cross-agent rule file, and Git history.
Do not install any plugin. Do not migrate material.

**Exit evidence:** the whole system can be explained from `HOME.md`; one real task can
begin after reading no more than `HOME.md`, `NOW.md`, and its project note.

### Stage 2 — Ten-session fit test

Use the candidate for ten real work sessions. At least one session must involve school,
one a programming/computer-use build, and one a business or opportunity test. Log only
orientation time, files read before action, useful output, routing corrections, and
maintenance time.

**Exit evidence:** at least eight of ten sessions route without structural correction,
the operator can explain every top-level item, and maintenance remains below ten
percent of working time.

### Stage 3 — First knowledge loop

Ingest only sources needed by those sessions. Create the first wiki page from a source,
review it, query it later, and verify the answer against evidence. Test whether an index
alone is sufficient.

**Exit evidence:** one-source ingest, one cited query, and one contradiction or missing-
fact check can be completed without opaque automation.

### Stage 4 — Thirty-day execution pilot

Run the system long enough to close projects, not just open them. Require at least one
closed school outcome, one demonstrable skill artifact, and one externally tested
business hypothesis. A paid result is desirable but not required this early; credible
customer behavior is required for a business claim.

**Exit evidence:** the system produces outcomes in all three lanes and does not require
a structural rewrite.

### Stage 5 — Controlled cutover

If the candidate passes, transfer daily ownership one area at a time. Write explicit
cutover notes and leave `.ROOT` as historical/reference authority for material not
transferred. If the candidate does not outperform `.ROOT`, archive the experiment and
use its findings to make the smallest `.ROOT` repair.

**Exit evidence:** every active commitment has exactly one owner, and no permanent dual
maintenance remains.

### Stage 6 — Optional tooling

Only after the file-only system passes should tooling be evaluated:

1. Obsidian core features as the normal human interface;
2. a tiny on-demand ingest/query/lint skill;
3. the GD4AI plugin in a disposable vault containing copies of three to five nonprivate
   sources;
4. plain-text search or BM25 after index retrieval fails repeatedly;
5. embeddings, MCP services, or background agents only after simpler search is measured
   and inadequate.

No experiment receives direct write access to `.ROOT` or the candidate's canonical
library until its write set and rollback behavior are understood.

## Acceptance scorecard

| Property | Pass threshold | Failure response |
|---|---|---|
| Human comprehension | Explain every top-level item and ownership boundary in under two minutes | Remove or combine components |
| Agent orientation | Begin useful work after at most three authoritative reads: `HOME`, `NOW`, project | Shorten pointers; remove universal context |
| Routing | At least 80% of ten pilot sessions need no owner correction | Fix one boundary; do not add a subsystem |
| Maintenance burden | Under 10% of working time in a normal month | Freeze changes and revert the last addition |
| Learning | Cold attempt or retrieval evidence exists for important skills | Add practice, not more notes |
| Production | Every active project has an observable done condition and useful output | Rewrite or close the project |
| Business validity | Business claims cite customer behavior or measured operational value | Return to discovery; stop feature building |
| Knowledge integrity | Important wiki claims cite immutable sources and distinguish unreviewed content | Quarantine or correct the page |
| Portability | Core system remains readable without Obsidian or any AI provider | Export or remove the dependency |
| Growth discipline | Every structural addition cites repeated failure and a rollback | Reject the addition |

No technical health check can override persistent human incomprehensibility. No elegant
knowledge system can override a lack of useful output.

## Repository component decisions

| Component or idea | Use now | Test later | Reject for initial system |
|---|:---:|:---:|:---:|
| Plain Markdown + Git | Yes |  |  |
| Obsidian core editor, links, backlinks | Optional |  |  |
| Karpathy immutable-source / maintained-wiki boundary | Yes |  |  |
| Map-first `INDEX.md` | Yes |  |  |
| One-source-at-a-time, human-reviewed ingest | Yes |  |  |
| Hot/cold context split from MehmetGoekce | Yes, reduced |  |  |
| Focused ingest/query/lint skills |  | Yes |  |
| GD4AI plugin |  | Separate sandbox |  |
| PageRank, graph ranking, or vector search |  | After measured retrieval failure |  |
| Automated entity/concept page creation |  | After stable ontology emerges | Yes |
| Eight predefined knowledge namespaces |  |  | Yes |
| Credentials in L1 or Markdown memory |  |  | Yes |
| Background session capture and automatic compilation |  |  | Yes |
| Bulk `.ROOT` import |  |  | Yes |
| SaaS or database as canonical source of truth |  |  | Yes |

## Risks and controls

### System-building becomes the work again

Control: ten-session and thirty-day stages are scored by closed work, skill evidence,
external tests, and maintenance ratio. New structure needs a recorded failure.

### The new system and `.ROOT` become duplicate realities

Control: one authoritative active owner, explicit cutover notes, links instead of
copies, and a defined end to dual-running.

### AI does the learning instead of supporting learning

Control: important learning projects require cold attempts, retrieval, error records,
and feedback before knowledge is promoted as demonstrated capability.

### AI-generated wiki pages become confidently wrong

Control: immutable sources, citations, review state, confidence/scope, source checks for
consequential decisions, and diagnostic questions after compilation.

### Capture again outruns use

Control: a source needs a current project or recurring question; `INBOX/` is temporary;
unprocessed accumulation is a failure signal, not a success metric.

### Profit ambition rewards premature product building

Control: customer discovery and measurable operational benefit come before substantial
automation. Skill artifacts may be valuable learning outcomes without being treated as
businesses.

### A plugin quietly becomes the platform

Control: all canonical content remains ordinary files; plugin trials use disposable
copies; the system must pass its portability test after any adoption.

## What `.ROOT` becomes

`.ROOT` is not a failed system to erase. It becomes three valuable things:

1. **Reference layer:** prior research, evidence, history, and material not yet needed in
   the new active system.
2. **Learning laboratory:** concrete examples of what helped, what created friction, and
   what happens when governance, automation, and taxonomy arrive too early.
3. **Recovery source:** if a candidate loses an important safeguard or context, the
   original reasoning can be recovered without pretending the entire former runtime
   should be restored.

`.ROOT` should be read on demand, not automatically treated as the daily control plane.
Its value is protected precisely by removing the pressure for it to be every tool at
once.

## Final recommendation

Proceed with the small greenfield candidate after the current `.ROOT` control result is
recorded and explicit build approval is given. Do not clone any reviewed repository.
Do not install the GD4AI plugin yet. Do not redesign `.ROOT` before the candidate
produces comparative evidence.

The target is not “the perfect second brain.” It is a minimal learning-to-profit
feedback system:

> **Choose one real outcome → learn what it requires → build and test something useful →
> preserve the evidence and lesson → let repeated success earn the next layer of
> structure.**

## Next exact action

Complete the unchanged Claude `.ROOT` task and capture its result. Then review this plan
against that result. If approved, create only the Stage 1 skeleton and run the first
real project before adding any repository code, plugin, migrated knowledge, or new
folder category.

## Sources

### Primary concept and implementations

- [Andrej Karpathy — LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [GD4AI — Karpathy LLM Wiki Plugin for Obsidian](https://github.com/GD4AI/obsidian-llm-wiki)
- [Obsidian community listing — Karpathy LLM Wiki](https://community.obsidian.md/plugins/karpathywiki)
- [Obsidian community listing — archived LLM Wiki](https://community.obsidian.md/plugins/llm-wiki)
- [MehmetGoekce — LLM Wiki](https://github.com/MehmetGoekce/llm-wiki)
- [Gavi Schneider — Awesome LLM Wiki](https://github.com/gavischneider/awesome-llm-wiki)
- [ddenzu — Karpathy LLM Wiki Second Brain](https://github.com/ddenzu/karpathy-llm-wiki-second-brain)
- [jackwener — LLM Wiki CLI](https://github.com/jackwener/llm-wiki)
- [frankchu91 — MindBase LLM Wiki](https://github.com/frankchu91/mindbase-llm-wiki)
- [Microsoft — LLMWiki](https://github.com/microsoft/llmwiki)

### Knowledge, memory, and learning evidence

- [Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki](https://arxiv.org/abs/2605.25480)
- [Filesystem-Based Memory for LLM Agents](https://arxiv.org/abs/2607.26637)
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)
- [WiCER: Wiki-memory Compile, Evaluate, Refine](https://arxiv.org/abs/2605.07068)
- [U.S. Department of Education — Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/practiceguide/1)
- [NSF I-Corps](https://www.nsf.gov/funding/initiatives/i-corps)

### Organization and platform references

- [Forte Labs — PARA](https://fortelabs.com/blog/para/)
- [Forte Labs — Building a Second Brain and CODE](https://fortelabs.com/blog/basboverview/)
- [Johnny.Decimal introduction](https://johnnydecimal.com/documentation/introduction)
- [Zettelkasten Method overview](https://zettelkasten.de/overview/)
- [Obsidian — Create a vault](https://obsidian.md/help/vault)
- [Obsidian — Internal links](https://obsidian.md/help/links)
- [OpenAI — AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Anthropic — Claude Code memory](https://code.claude.com/docs/en/memory)

