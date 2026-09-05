---
domain: tech
type: framework
tags: [subject/ai, start]
timeline: next
status: wiki-only
---

# AI as a Coworker: Tasks, Systems, Jobs, and the Centaur/Cyborg Distinction

**Summary**: Whether AI "takes your job" depends on three separable levels — tasks, the organizational systems jobs sit inside, and jobs themselves — plus a working task taxonomy (Just Me / Delegated / Automated) and two integration styles (Centaur vs. Cyborg). This is the strongest promotable artifact from this chunk: a ready-made structure for auditing a client's tasks for AI fit.

**Sources**: CoIntelligence.pdf (Chapter 6, "AI as a Coworker")

**Last updated**: 2026-06-17

---

## Three levels: tasks, systems, jobs

Mollick's framework for thinking clearly about AI and employment, instead of asking "will AI replace [job title]":

1. **Tasks** — the actual bundle of activities that make up a job. A professor's job title is just a label over teaching, research, writing, admin, letters of recommendation, etc. AI can plausibly automate some of these (administrative paperwork) without the job disappearing — the same way spreadsheets sped up accountants without eliminating them.
2. **Systems** — the organizational structures (tenure, licensing, liability law, professional bodies, classroom technology, accreditation rankings) that a job is embedded in. These change far more slowly than raw task capability, which is why jobs resist disruption even when individual tasks are fully automatable. This is the chapter's central claim: **"our systems will prove more resistant to change than our tasks."**
3. **Jobs** — the labeled role itself, which survives or changes based on both of the above. Research by Felten, Raj, and Seamans across 1,016 professions found near-universal overlap between AI capability and job tasks — the highest-overlap jobs are the most highly compensated, creative, and educated (college professors rank in the top 20; only 36 categories, mostly highly physical work like dancers, pile-driver operators, and roofers, showed zero overlap) — inverting every prior automation wave, which started with the most repetitive and dangerous work.

## Tasks for AI: a working taxonomy

A practical way to sort the tasks that make up a job by AI suitability:

- **Just Me Tasks** — AI isn't useful, or you choose to keep them human for ethical/personal reasons (raising children, important decisions, joke-writing — AI is "currently terrible" at jokes per Mollick's own test). As AI improves, the "AI genuinely can't do this" subset shrinks, but the "I choose to keep this human" subset can grow in its place.
- **Delegated Tasks** — assigned to AI but checked by a human before acting on the result. The right fit: tedious, repetitive, or time-consuming for humans, but easy and efficient for AI (expense reports, scheduling, summarizing a long paper). Not necessarily low-stakes — these can be complex and have real consequences if AI errs and the human doesn't catch it.
- **Automated Tasks** — fully delegated with no human check at all (spam filtering is the chapter's clean example). Still a small category today because hallucination rates make unchecked automation risky for most tasks; will grow as either accuracy improves or external systems start verifying AI output automatically (e.g., a Python compiler's error messages let an AI self-correct its own code without human review).

## Centaur vs. Cyborg: two ways to integrate AI into work

- **Centaur work** — a clean division of labor between human and AI, like the literal human-torso/horse-body split of the myth. The human decides strategy/approach; the AI executes a separable sub-task (e.g., a human picks the statistical method, the AI generates the graphs).
- **Cyborg work** — deeply interleaved, with the human and AI trading off mid-task rather than handing off discrete chunks (e.g., letting AI complete a sentence the human started, or maintaining a running back-and-forth across a whole writing project, as Mollick describes doing throughout this book).

Mollick's progression for an individual learning to use AI well: follow Principle 1 ([[four-rules-for-co-intelligence]] — always invite AI to the table) until you've learned the shape of your own Jagged Frontier, start as a Centaur on tasks you hate but can easily check, then transition naturally into Cyborg use as AI proves indispensable for harder, more interleaved problems.

## The "falling asleep at the wheel" risk

A BCG/Harvard field study (Dell'Acqua, McFowland, Lakhani, Lifshitz-Assaf, Kellogg) gave ~800 consultants 18 realistic tasks; the AI-assisted group did significantly better across every measure — faster, more creative, better written, more analytical, replicated across 118 separate analyses. But a deliberately AI-unsolvable task (designed to sit outside the Jagged Frontier) revealed the danger: human-only consultants got it right 84% of the time; AI-assisted consultants, having learned to trust the AI, got it right only 60–70% of the time.

A related study had 181 recruiters evaluate job applications with varying AI assistance quality. Recruiters given **higher-quality** AI assistance became less accurate, less careful, and didn't improve over time — they "fell asleep at the wheel" and blindly followed AI recommendations. Recruiters with **lower-quality** AI stayed alert, critical, and kept improving their own judgment. The lesson generalizes the warning already given as [[four-rules-for-co-intelligence]] Principle 2: the better the AI gets, the *more* deliberate effort is required to stay the human in the loop, not less.

## Why organizations struggle to capture AI's value: shadow use

Workers who discover powerful AI uses for their own jobs frequently keep them secret, for three converging reasons: (1) many companies initially banned tools like ChatGPT outright, pushing usage onto personal devices as unsanctioned "shadow IT"; (2) AI-generated work is judged more harshly once people know it's AI-generated, so revealing AI use can cost credit; (3) workers reasonably fear that admitting they've automated 90% of their job will get 90% of their team laid off rather than rewarded. Mollick's prescription for organizations: include all levels of the org (not just senior staff) in AI policy, since AI skill correlates with nothing about seniority or history; remove the fear of revealing AI use (commitments not to use efficiency gains for headcount cuts); and actively incentivize surfacing AI use (large rewards, not just permission) rather than treating it as something to police.

## Connects to

- [[co-intelligence-mollick]] — source tracker
- [[ai-creativity-and-hallucination]] — "The Button" sets up the same task-allocation question this chapter answers structurally
- [[four-rules-for-co-intelligence]] — Principle 2 (human in the loop) is directly validated by the "falling asleep at the wheel" findings; Principle 1 (always invite AI to the table) is the prerequisite for learning your own Jagged Frontier well enough to use this taxonomy
- [[theory-of-constraints]] — "our systems will prove more resistant to change than our tasks" is the same insight as TOC's point that improving a non-bottleneck task doesn't change total system throughput; the constraint here is organizational, not task-level capability
- [[ai-as-tutor-and-coach]] — the skill-leveling effect (BCG's 22%→4% performance-gap finding) is the individual-performance mirror of this page's task/systems/jobs framework: AI changes who can do a task well, not just how fast it gets done
- **Promotable artifact**: the Just Me / Delegated / Automated taxonomy, combined with Centaur vs. Cyborg, is close to ready-made as a structured client audit instrument — walk a business through its task list and sort each task into a bucket, which is literally a first-pass AI-adoption audit for the audit/integration business
- [[ai-developer-tools-landscape-2026]] — the concrete tool ecosystem (coding agents, IDEs, code generators) that this chapter's tasks/systems/jobs framework abstractly describes; useful for mapping which named tool fits which delegation bucket
