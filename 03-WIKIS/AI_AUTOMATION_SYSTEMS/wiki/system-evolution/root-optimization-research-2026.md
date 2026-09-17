---
type: research
timeline: reference
status: complete
reference_priority: core
tags: [ai-automation, self-evolution, knowledge-management]
created: 2026-09-10
updated: 2026-09-10
---

# .ROOT Optimization Research

## Executive finding

`.ROOT` should keep its present macro-architecture. The evidence does not support a
PARA migration, a graph-first rebuild, a new AI-memory platform, or broad autonomous
writeback. Its strongest features—local Markdown, stable numbered domains, one live
owner, immutable evidence, progressive loading, explicit proposals, and
human-controlled promotion—already match the best-supported patterns across current
agent documentation, filesystem-memory research, local-first software, and mature
personal knowledge systems.

The next optimization is not another folder system. It is a thin verification layer
that answers three questions:

1. Did a fresh agent reach the correct owner with little irrelevant context?
2. Did the returned evidence produce a decision, test, or useful output without
   re-deriving settled work?
3. Can the canonical state be recovered and distinguished from generated projections?

The priority sequence is therefore **observe retrieval, test critical truths, then
repair only demonstrated failures**. Through the current runtime probation, the
system should gather evidence from natural work and make no structural change. After
probation, a bounded cold-session evaluation should decide whether any routing file,
instruction, summary, or derived index has earned modification.

## Decision

**Verdict: KEEP the architecture; TEST the runtime; MODIFY only evidence-backed
failure points.**

Three capabilities deserve focused improvement:

- **Observability:** measure routing accuracy, context load, correction count, and
  time-to-useful-output on real requests.
- **Diagnostic memory:** maintain a small set of cold questions that expose stale,
  missing, or contradictory owner truth.
- **Recoverability:** prove that the local canonical store can be restored without
  confusing stale replicas or generated indexes for live truth.

No new platform is justified now. A disposable local search index becomes worth a
pilot only if natural sessions repeatedly fail to find evidence across mixed files or
compositional questions. It must remain rebuildable from Markdown and source files,
never become a second owner, and pass citation, staleness, and deletion tests.

## Scope and evaluation standard

This review examines the architecture needed for a one-person, multi-domain operating
system used by humans and multiple AI surfaces. It covers folder topology, instruction
loading, retrieval, memory, provenance, writeback, maintenance, security, and recovery.
It does not evaluate journal content, alter immutable evidence, choose a new business
vehicle, or activate any system proposal.

The system is evaluated against six outcomes:

| Outcome | Required behavior |
|---|---|
| Orientation | A cold agent finds the correct lane and authoritative owner. |
| Compression | The agent loads the minimum sufficient context, not the whole vault. |
| Truth | Evidence, maintained knowledge, proposals, and active state remain distinct. |
| Action | Retrieved context produces a decision, bounded test, or useful output. |
| Durability | State is local, inspectable, portable, attributable, and recoverable. |
| Sustainability | Maintenance removes more coordination cost than it creates. |

This standard is deliberately stricter than “the files are organized.” A tidy tree
that does not improve decisions is decoration. A sophisticated memory layer that adds
latency, ambiguity, credentials, or hidden state is a regression.

## Live system snapshot

A read-only scan of the governed working areas on September 10, 2026 found 7,053
files in 944 directories, excluding `88-JOURNAL` and every directory named `raw`.
There were 1,695 Markdown files. `03-WIKIS` contained 1,175 files; `02-LIBRARY`
contained 4,916; `04-SCHOOL` contained 407. The distribution confirms that `.ROOT`
is already beyond the scale where unaided browsing should be the only retrieval mode,
but it does not prove that a new database is needed.

The normal operator boot chain—root pointer, universal OS, Codex profile, operator
profile, flags, North Star, and operator hat—is approximately 4,037 words across 506
lines and 27.9 KiB. A system-evolution task that also loads the routing map and hub
operations reaches approximately 7,505 words across 1,000 lines and 54.2 KiB. These
figures are not automatically excessive: the files contain genuine constraints and
personal operating context. They do establish a measurable context budget whose
benefit should be verified rather than assumed.

The existing architecture already uses three practical layers:

```text
orientation / index / compact owner
                ↓
focused maintained knowledge and active state
                ↓
source evidence and history, loaded only when needed
```

This is functionally similar to the tiered context designs promoted by MemGPT,
OpenViking, LongMemEval-V2's runbook approach, and the Open Agent Skills model. The
important question is therefore not whether to add layers, but whether each existing
layer selects the next one accurately and economically.

Two visible root-level locations—`Claude outputs` and `tmp`—sit outside the numbered
domain map. They contain only 41 files combined, so they are not a scale problem.
They are a routing-semantic question: each should be explicitly classified as an
interface, disposable workspace, or legacy area before any move is proposed. Naming
alone is insufficient evidence for restructuring.

## What the external evidence says

### 1. Organized filesystem memory improves retrieval economics, not necessarily answer quality

The broadest current study of filesystem-based agent memory separates three roles:
memory management, search, and task execution. Organized stores roughly halved
retrieval cost on large material, but organization degraded over time for most memory
managers, and the measured agents did not reliably turn better organization into
better final answers.[1](#source-1)

That distinction is central to `.ROOT`. Structure is valuable when it reduces search
and context cost. It is not an outcome by itself. The existing owner-and-index pattern
should be judged by retrieval economy and decision quality, not by whether another
taxonomy appears cleaner.

LongMemEval-V2 provides a complementary result. Its filesystem “runbook” system
reached 72.5% average accuracy, above the strongest reported RAG baseline at 48.5%,
but with high latency. More importantly, compact evidence slicing plus notes reached
86.3%, outperforming full oracle context at 65.3%.[2](#source-2) The practical
lesson is not “put everything in files.” It is “select the right evidence and preserve
useful working notes.” `.ROOT` already has the substrate; it needs measurement of
selection quality.

### 2. Major agent systems converge on layered, scoped instructions

OpenAI Codex loads `AGENTS.md` through a hierarchy: global guidance, repository-root
guidance, then nested guidance nearer the working directory. Later files override
earlier ones, and the combined chain has a configurable default size limit of 32
KiB.[3](#source-3) Codex skills use progressive disclosure: only skill metadata is
initially visible; the full instructions and resources load when the skill is
selected.[4](#source-4)

Claude Code recommends keeping always-loaded instructions to facts needed in every
session, moving multi-step procedures to skills or scoped rules, keeping the main
instruction file concise, and using deterministic hooks when compliance must be
guaranteed.[5](#source-5) Cursor and GitHub Copilot implement the same basic idea
through scoped project rules, nested files, path-specific instructions, and agent
instruction files.[6](#source-6)[7](#source-7) The Open Agent Skills specification
likewise defines a focused `SKILL.md` with optional references, scripts, and assets
loaded after activation.[8](#source-8)

This cross-platform convergence supports `.ROOT`'s boot-chain and skill architecture.
It also warns against allowing general instructions to absorb every procedure. The
current 4,037-word operator surface is a candidate for evaluation, not an automatic
pruning target: personal constraints may justify more resident context than a software
repository needs. A cold-session test should identify which parts change behavior and
which merely consume attention.

### 3. More instructions can increase cost without improving success

An evaluation across 138 repository tasks found that repository context files were
followed, but often caused more exploration and increased steps and cost by 20–23%.
Developer-written files showed a small average improvement that was not statistically
significant; generated files reduced average resolution performance in that
benchmark.[9](#source-9) The domain was software engineering, so the result cannot be
transferred directly to a personal operating system. It still establishes that
instruction presence and instruction value are different things.

A much larger observational study of 15,549 agentic pull requests found heterogeneous
effects: 27.7% of projects improved merge rates by at least 20%, while 26.35% declined
by at least 20%. More structured and more detailed instruction files were associated
with better outcomes among winners, but the study does not establish a universal
length rule.[10](#source-10) Together, the studies argue for local evaluation. The
right question is not “short or long?” but “which instruction changes which failure?”

OpenAI's current model guidance makes the same operational point: stronger
instruction-following makes models more sensitive to accessible instruction files,
so conflicting or unclear skills can cause blocking and priority must be explicit.[11](#source-11)

### 4. Long context is not a substitute for retrieval

Long-context systems can lose performance even when relevant information remains in
the prompt. “Lost in the Middle” found that answer quality depended on where evidence
appeared, with performance often worst when relevant material was buried in the
middle.[12](#source-12) Chroma's later Context Rot evaluation across 18 models found
that performance became less reliable as input grew; on one LongMemEval comparison,
a focused roughly 300-token context outperformed a full 113,000-token context.[13](#source-13)
The latter is a vendor technical report rather than peer-reviewed evidence, but it
aligns with the controlled academic results and with LongMemEval-V2's evidence-slicing
gain.

The consequence for `.ROOT` is direct: “load more of the vault” should not be the
fallback when a result is weak. The system should improve route selection, retrieve a
smaller evidence slice, and expose the retrieval path so failure can be diagnosed.

### 5. Compiled wikis need probes because summarization can fail catastrophically

WiCER evaluated wiki compilation across 17 domains and 6,800 questions. Blind
compilation substantially underperformed retrieval and produced a high catastrophic
failure rate. An iterative probe-evaluate-refine loop recovered about 80% of lost
quality and reduced catastrophic failures by 55%; targeted diagnosis worked far better
than generic “pinning.”[14](#source-14)

The LLM-Wiki “Retrieval as Reasoning” architecture offers a positive counterpart:
structured Markdown pages, bidirectional links, search, read, and link traversal, plus
an error book, outperformed seven comparison systems on multi-hop questions by 2.0–8.1
F1 over the strongest graph baseline.[15](#source-15) This supports `.ROOT`'s
maintained pages, indexes, links, and system flags. It also suggests an improvement:
critical maintained pages should have a few diagnostic questions that reveal whether
the current compiled truth still supports the workflows it exists to serve.

A wiki update should therefore be accepted by behavior, not merely by frontmatter and
links. For a high-value owner, the test should ask a fresh agent to locate the owner,
state the current constraint, distinguish evidence from proposal, and name the next
valid action. Failure should trigger a targeted repair to the route, page, or source
relationship that caused it.

### 6. Derived indexes are useful when disposable and observable

Current open-source systems illustrate three possible extensions:

- **Basic Memory** keeps Markdown as source of truth and builds a rebuildable SQLite
  projection with semantic links and MCP access.[16](#source-16)
- **OpenViking** exposes a virtual filesystem with roughly 100-token abstracts,
  2,000-token overviews, full content, recursive search, and an observable retrieval
  trajectory.[17](#source-17)
- **GBrain** combines local graph memory, schema packs, procedures, MCP integrations,
  ambient writeback, and scheduled consolidation.[18](#source-18)

These repositories demonstrate design options, not proven superiority. Basic Memory's
rebuildable projection and OpenViking's retrieval trace are the closest fits for
`.ROOT`. Their useful concepts can be tested without adopting their platforms. GBrain's
broad operation surface, ambient capture, credentials, and “nightly dream” maintenance
conflict with `.ROOT`'s preference for controlled promotion and minimal ceremony.

A local index should therefore be treated as a cache:

1. Canonical files remain readable and sufficient without it.
2. Every result returns exact source location and staleness information.
3. Rebuilding the index produces equivalent behavior.
4. Deleting the index loses convenience, not truth.
5. The index is scoped to a demonstrated retrieval failure, such as one mixed-file
   course or one multi-hop research corpus.

### 7. Autonomous memory writeback creates a trust boundary

Memory is an attack and truth-management surface. A 2026 poisoning study reported
that changing 1.2% of a LongMemEval corpus reduced accuracy from .850 to .300; a
write-time screen that detected conventional prompt injection missed all 360 tested
false memories.[19](#source-19) Another 2026 preprint showed that hostile documents,
web pages, or repositories could cause fabricated user memories to be stored and later
retrieved, with high success in its test conditions.[20](#source-20) Both are recent
preprints and need replication, but their attack shape is credible and directly
relevant.

The architectural response is separation, not a promise that a classifier will catch
everything. Web material and AI output should enter as attributed evidence or
candidate knowledge. They should never silently become user profile, governance,
current strategy, or an authoritative owner. `.ROOT`'s raw/maintained/proposal/verified
distinctions are therefore security controls as well as organizational conventions.

This is a strong reason to reject ambient writeback and unsupervised consolidation for
high-authority state. Automation may suggest a patch, identify a conflict, or produce a
rebuildable projection. Promotion must remain explicit and reviewable.

### 8. Instruction stores accumulate unless rules carry rationale and retirement evidence

A large longitudinal study of 247,694 instruction-file lifetimes found that instruction
files grew by 226% on average and that old rules became difficult to remove because
their original rationale was lost. In synthetic and benchmark tests, preserving latent
rationale through “prompt comments” sharply reduced excess instructions and improved
performance.[21](#source-21) This is a very recent preprint, but it explains a familiar
failure mode: every incident creates a permanent rule, while few rules acquire a safe
retirement condition.

`.ROOT` already improved this area through its September runtime reduction and its
proposal fields for evidence, check dates, and verdicts. The remaining principle should
be explicit: a new always-loaded rule must name the failure it prevents, the evidence
that justified it, the owner, the verification method, and when it can be reconsidered.
If those fields do not merit permanent context, the material belongs in a skill,
procedure, history, or test rather than the boot chain.

### 9. Local-first architecture needs tested recovery

Local-first software emphasizes offline operation, ownership, privacy, portability,
and long-term preservation.[22](#source-22) Obsidian's plain Markdown vault model
fits these properties, while PARA and Johnny.Decimal contribute action-oriented grouping
and stable numeric navigation.[23](#source-23)[24](#source-24)[25](#source-25)
`.ROOT` already takes the compatible parts: local files, numbered stable areas, active
owners, archives, and cross-domain routing. Renaming the system to match a framework
would add migration cost without adding a capability.

Local ownership alone does not guarantee durability. An unresolved stale-replica or
backup ambiguity can make recovery more dangerous because multiple plausible trees
appear authoritative. The live system flag concerning a stale second `.ROOT` is
therefore a higher-value optimization target than another taxonomy. Recovery should be
tested by restoring a bounded non-sensitive sample and proving which root, timestamp,
and owner are canonical.

## Architecture comparison

| Pattern | Canonical truth | Retrieval model | Writeback | Main strength | Main risk | `.ROOT` verdict |
|---|---|---|---|---|---|---|
| Current `.ROOT` | Local files with explicit owners | Index, route, focused read, search | Human/agent edits under governance | Truth separation and action orientation | Runtime benefit is incompletely measured | Keep; add tests |
| PARA + Johnny.Decimal | Folders grouped by action and stable number | Human navigation and search | Human filing | Simple, memorable placement | Too coarse for provenance and agent authority | Keep borrowed principles; no rename |
| LLM-Wiki | Structured Markdown and links | Search plus compositional link traversal | Maintained compilation with error learning | Multi-hop retrieval and inspectability | Blind compaction can omit decisive facts | Extend with probes, not wholesale rebuild |
| Basic Memory | Markdown plus rebuildable database | Semantic search and graph projection | Bidirectional human/AI | Local source of truth with disposable index | A second mutable access layer and easy over-promotion | Candidate pattern only after measured failure |
| OpenViking | Resource filesystem plus generated context layers | Recursive tiered search with retrieval trace | Automated session extraction/evolution | Observable L0/L1/L2 selection | Platform complexity and generated-layer drift | Borrow trace/tiering concepts only |
| GBrain | Local graph-oriented memory | Graph, schema, procedure, integrations | Ambient and scheduled consolidation | Rich procedural and relationship memory | Large surface, credentials, autonomous mutation | Do not adopt for current needs |

## What `.ROOT` already gets right

### Stable macro-topology

The numbered areas provide low-entropy orientation. They already combine the useful
parts of Johnny.Decimal and PARA while allowing richer evidence and authority rules.
Splitting school, life, business, and AI work into separate roots would duplicate the
very cross-domain constraints—capacity, recovery, financial direction, and current
strategy—that the system must coordinate.

### Local, inspectable source of truth

Markdown and ordinary files preserve portability, human auditability, and tool
independence. They can support future projections without surrendering canonical truth
to a database or vendor.

### Progressive loading

The root pointer, universal profile, hats, section operations, indexes, maintained
pages, and raw evidence form a purposeful sequence. It is already a filesystem memory
architecture. The opportunity is to observe and tune the transitions rather than add
another layer by default.

### Authority and evidence separation

Raw evidence, maintained knowledge, proposals, active state, and verified results have
different meanings. This separation addresses both epistemic drift and memory
poisoning. Many public “second brain” designs do not define this trust boundary.

### Outcome orientation

The Action Kernel, North Star, current strategy, and acceptance checks resist the
classic failure in which knowledge-system maintenance replaces work. Any optimization
that cannot state the resulting decision, experiment, or useful output should fail the
gate.

### Reversibility

Archive-over-delete, explicit proposals, checks, and keep/modify/revert verdicts make
system changes inspectable and recoverable. This is more valuable than autonomous
“self-improvement” whose causal effects cannot be isolated.

## Demonstrated and plausible gaps

| Gap | Evidence | Consequence | Status |
|---|---|---|---|
| Cold-session verification | Current probation has limited cold-context evidence | The architecture may work only when recent context is available | Demonstrated open test |
| Context-value observability | 4,037-word core operator surface; no per-file benefit trace | Redundant instructions may increase steps or conflict | Plausible; measure first |
| Retrieval-quality metrics | 7,053 files and 1,695 Markdown files; no standard retrieval score | Search friction and re-derivation can remain anecdotal | Demonstrated measurement gap |
| Critical-truth probes | Maintained pages have structural lint but few semantic acceptance questions | A concise, valid page can still omit a decisive fact | Plausible; supported by WiCER |
| Rule lifecycle | Historical instruction growth required a major runtime reduction | Old incident rules can become permanent context | Demonstrated pattern; partially repaired |
| Recovery proof | Live stale-replica flag remains unresolved | Restoration could select a plausible but stale root | Demonstrated unresolved risk |
| Derived search for mixed files | Prior school review identified one evidence-backed candidate | PDFs, slides, and notes may need exact cited retrieval | Conditional; trigger not yet met |
| Root-level transient locations | `Claude outputs` and `tmp` sit outside numbered routes | Cold agents may infer the wrong authority | Small ambiguity; classify before changing |

## Recommended operating plan

### Phase 0 — Observe during the current probation

Do not restructure folders or add a platform. Use five to ten natural, meaningful
requests spanning school, system, research, and business work. Record only evidence
needed for the probation decision:

| Measure | Pass condition |
|---|---|
| Correct lane | First chosen section matches the authoritative owner. |
| Correct owner | Agent cites the live owner without being handed its path. |
| Context economy | No unrelated domain bundle is loaded before useful work begins. |
| Truth discipline | Evidence, proposal, and active state are not conflated. |
| Useful return | Session produces the requested artifact, decision, or next test. |
| Re-derivation | No settled plan is reconstructed as if new. |
| Corrections | No more than one operator correction caused by routing or stale state. |

Avoid creating a standing dashboard for this phase. Add the bounded evidence to the
existing probation decision surface. The system must not create permanent ceremony to
evaluate a temporary rewrite.

### Phase 1 — Run a cold retrieval audit after probation

Select ten questions whose answers already have authoritative owners. Include at least
one question from each capability: orient, teach, research, build, diagnose value,
strategy, and maintain. Start each in a genuinely fresh agent context.

For each question, capture:

1. files loaded before the first correct owner;
2. time or turns to first useful action;
3. incorrect or irrelevant paths opened;
4. missing, stale, or contradictory claims;
5. whether the final output used source evidence;
6. operator corrections;
7. the smallest failing transition in the route.

**Decision rule:** modify a routing or instruction file only when at least two failures
share the same causal transition, or one high-consequence failure exposes a safety or
truth defect. A one-off weak answer is not sufficient evidence for architecture change.

### Phase 2 — Add diagnostic questions to critical owners

Create no global question bank. Add two to five probes only to the acceptance mechanism
for high-authority, frequently used owners. Suitable probe forms include:

- What is the current priority, and which source establishes it?
- Which tempting action is explicitly out of scope?
- What evidence would change the present decision?
- Which file owns the next action?
- What is a proposal rather than an activated rule?
- Which fact is time-sensitive and requires external verification?

**Decision rule:** keep a probe only if it catches a real omission, contradiction, or
misroute during cold testing. Otherwise archive the test evidence and avoid expanding
the maintenance surface.

### Phase 3 — Make instruction lifecycle explicit

For every proposed always-loaded instruction, require:

- triggering failure or risk;
- evidence and date;
- authoritative owner;
- expected behavioral change;
- verification method;
- reconsideration or retirement condition.

Rules without a permanent, cross-task role should route to a skill, scoped operating
file, checklist, proposal, or incident history. Deterministic invariants should be
enforced by deterministic checks where feasible; prose should explain authority and
intent rather than pretend to guarantee enforcement.

### Phase 4 — Prove recovery

Resolve the stale-replica ambiguity through its owning system review. Then perform a
bounded restore exercise using non-sensitive files:

1. identify the canonical root by explicit marker and live owner;
2. restore a small sample into an isolated temporary location;
3. verify content, timestamps, links, and current-state markers;
4. confirm generated indexes can be rebuilt rather than restored as truth;
5. record the recovery evidence and remove the temporary copy through the approved
   archive/destructive-action process.

**Decision rule:** local-first durability is not accepted until the restored sample can
be distinguished from every stale replica without relying on memory.

### Phase 5 — Pilot derived retrieval only if triggered

Open a tool pilot only after repeated retrieval failures meet all of these conditions:

- the failures span mixed files or genuinely compositional questions;
- ordinary filename/text search and existing indexes are insufficient;
- exact citations materially affect the output;
- the corpus has a clear owner and bounded scope;
- staleness can be detected;
- the projection can be deleted and rebuilt without losing truth.

The smallest suitable pilot remains a single course or one research corpus. Compare
current retrieval with a local projection on accuracy, citation precision, latency,
staleness, operator correction, and maintenance time. Adopt only if it improves a
real workflow enough to repay its operating cost.

## Changes not justified by the evidence

- Do not rename the numbered areas to PARA categories.
- Do not split `.ROOT` into independent school, life, business, or AI roots.
- Do not adopt Basic Memory, OpenViking, GBrain, or another AI-OS wholesale.
- Do not make a vector database, knowledge graph, or generated summary the canonical
  owner.
- Do not ingest web pages or model output directly into user profile, governance,
  strategy, or current state.
- Do not enable ambient writeback, automatic profile learning, or unsupervised nightly
  consolidation for authoritative files.
- Do not add a manually maintained L0/L1 summary layer to every directory.
- Do not create a new daily review ceremony for the sake of system optimization.
- Do not interpret the existence of 7,053 files as evidence that the hierarchy has
  failed; most mass is in library and school source material, while routing depends on
  a much smaller owner surface.

## Proposed acceptance decision

At the end of the runtime probation and cold audit, choose one of three outcomes:

| Verdict | Evidence threshold | Response |
|---|---|---|
| Keep | At least 8/10 cold tasks find the correct owner, no high-consequence truth failure, and corrections are isolated | Preserve architecture; repair individual content only |
| Modify | Repeated failures share a route, instruction, or evidence-selection cause | Change the smallest owner or transition; retest the same questions |
| Revert | The rewrite produces systemic owner confusion, repeated stale truth, or materially worse useful-output time | Restore the prior approved runtime from history and document the failed assumptions |

Tool adoption is a separate decision. A strong cold-audit result is evidence against
adding retrieval infrastructure. A weak result identifies a failure location; it is
not automatic evidence for a new platform.

## Research limitations

The empirical literature is young. Several directly relevant memory and instruction
studies are 2026 preprints and have not yet accumulated replication. Software-engineering
benchmarks do not capture the full value of personal constraints, cross-domain
coordination, or long-term human memory. Vendor documentation describes intended
behavior, while open-source repositories demonstrate mechanisms rather than comparative
outcomes. Practitioner frameworks such as PARA and Johnny.Decimal offer durable design
heuristics but not controlled performance evidence.

For those reasons, the strongest conclusion is local and experimental: preserve the
high-value architecture, measure natural and cold behavior, and require every change to
name a failing transition and a disconfirming result.

## Related `.ROOT` knowledge

- [[llm-wiki-pattern-and-second-brain-tools]]
- [[building-a-second-brain-root-application]]
- [[root-maturity-self-assessment]]
- [[../agents/ai-agent-book-ch2-context-engineering]]
- [[../agents/ai-agent-book-ch3-ch8-memory-and-evolution]]
- [[../agents/ai-agent-book-ch10-multi-agent-collaboration]]

## Sources

<a id="source-1"></a>1. Li et al., “Filesystem-Based Memory for LLM Agents:
Organization, Evolution, and Sustainability,” arXiv, 2026.
https://arxiv.org/abs/2607.26637

<a id="source-2"></a>2. “LongMemEval-V2: Benchmarking Memory in Long-Term Agentic
Tasks,” arXiv, 2026. https://arxiv.org/abs/2605.12493

<a id="source-3"></a>3. OpenAI, “Custom instructions with AGENTS.md.”
https://learn.chatgpt.com/docs/agent-configuration/agents-md

<a id="source-4"></a>4. OpenAI, “Build skills.”
https://learn.chatgpt.com/docs/build-skills

<a id="source-5"></a>5. Anthropic, “Manage Claude's memory.”
https://code.claude.com/docs/en/memory

<a id="source-6"></a>6. Cursor, “Rules.”
https://docs.cursor.com/context/rules-for-ai

<a id="source-7"></a>7. GitHub, “Adding custom instructions for GitHub Copilot CLI.”
https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions

<a id="source-8"></a>8. Open Agent Skills, “Specification.”
https://openagentskills.dev/docs/specification

<a id="source-9"></a>9. Gloaguen et al., “Evaluating AGENTS.md: Are Repository-Level
Context Files Helpful for Coding Agents?” arXiv, 2026.
https://arxiv.org/abs/2602.11988

<a id="source-10"></a>10. “Toward Instructions-as-Code: An Empirical Study of Agent
Instruction Files,” arXiv, 2026. https://arxiv.org/abs/2606.13449

<a id="source-11"></a>11. OpenAI, “Using GPT-5.4,” section on coding and instruction
files. https://developers.openai.com/api/docs/guides/latest-model

<a id="source-12"></a>12. Liu et al., “Lost in the Middle: How Language Models Use Long
Contexts,” arXiv, 2023. https://arxiv.org/abs/2307.03172

<a id="source-13"></a>13. Chroma Research, “Context Rot: How Increasing Input Tokens
Impacts LLM Performance,” 2025. https://www.trychroma.com/research/context-rot

<a id="source-14"></a>14. “WiCER: Wiki-Compilation with Iterative Evaluation and
Refinement,” arXiv, 2026. https://arxiv.org/abs/2605.07068

<a id="source-15"></a>15. “Retrieval as Reasoning: LLM-Wiki for Multi-Hop Knowledge
Work,” arXiv, 2026. https://arxiv.org/abs/2605.25480

<a id="source-16"></a>16. Basic Machines, “Basic Memory,” GitHub repository.
https://github.com/basicmachines-co/basic-memory

<a id="source-17"></a>17. Volcano Engine, “OpenViking,” GitHub repository and context
layer documentation. https://github.com/volcengine/OpenViking

<a id="source-18"></a>18. Garry Tan, “GBrain,” GitHub repository.
https://github.com/garrytan/gbrain

<a id="source-19"></a>19. “Utility Under Attack: Benchmarking Memory Poisoning in
Long-Horizon LLM Agents,” arXiv, 2026. https://arxiv.org/abs/2608.21230

<a id="source-20"></a>20. “Hidden in Memory: Sleeper Memory Poisoning in LLM Agents,”
arXiv, 2026. https://arxiv.org/abs/2605.15338

<a id="source-21"></a>21. “Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in
Agent Instruction Files,” arXiv, 2026. https://arxiv.org/abs/2608.11095

<a id="source-22"></a>22. Kleppmann et al., “Local-first software: You own your data, in
spite of the cloud,” Ink & Switch, 2019.
https://www.inkandswitch.com/essay/local-first/

<a id="source-23"></a>23. Obsidian, “How Obsidian stores data.”
https://help.obsidian.md/data-storage

<a id="source-24"></a>24. Tiago Forte, “The PARA Method: The Simple System for
Organizing Your Digital Life in Seconds,” updated 2026.
https://fortelabs.com/blog/para/

<a id="source-25"></a>25. Johnny.Decimal, “Introduction.”
https://johnnydecimal.com/documentation/introduction
