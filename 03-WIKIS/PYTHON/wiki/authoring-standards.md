---
type: reference
tags: [programming, governance]
timeline: reference
---

# Authoring Standards — Python Wiki
### Moved out of CLAUDE.md July 11, 2026 (slim pass — always-on OS keeps one line per artifact; the full format specs live here).
### Load this page when CREATING or RESTRUCTURING pages. Not needed for teaching/reading sessions.
### Templates in `templates/` are the skeletons; these are the content rules.

---

## Required Learning Page Shape

Every concept page must answer:

1. What is this?
2. What problem does it solve?
3. When do I use it?
4. When should I not use it?
5. What does it look like in code?
6. What mistake will a beginner make?
7. What terms must go into the glossary?
8. What flashcards should be created?
9. What should Chris practice next?
10. What prerequisite does this depend on?

Use short paragraphs. Prefer tables and examples over long prose.

---

## Glossary Rule

Every new programming or computer-science term must generate or update a glossary entry in `wiki/glossary/`.

A glossary entry must include:

```markdown
# Term

## Plain-English Definition

## What Problem It Helps Solve

## When Chris Will See It

## Code Example

## Common Confusion

## Physical-World Anchor

## Related Terms

## Flashcard Q/A
```

Glossary pages are not optional. Vocabulary is a major bottleneck.

---

## Flashcard Rule

Every new concept and glossary entry must create flashcard-ready Q/A in `wiki/flashcards/`.

Flashcards must be simple enough to import or copy into a card system.

Required format:

```markdown
## Card: [term or concept]

**Front:** [Question]

**Back:** [Answer]

**Tags:** python, stage-XX, [concept]
```

Avoid giant cards. One fact or decision rule per card.

---

## Code Pattern Rule

Every syntax construct must create a code-pattern page in `wiki/code-patterns/`.

A code-pattern page must include:

- Pattern name.
- When to use it.
- When not to use it.
- Skeleton code.
- Filled example.
- Beginner mistakes.
- Drill link.
- Related concepts.

Examples:

- `if-elif-else-decision-chain.md`
- `for-loop-over-list.md`
- `while-loop-until-condition.md`
- `function-with-parameter.md`
- `function-with-return-value.md`

---

## Drill Rule

Every current-stage concept must have at least one drill in `wiki/drills/`.

Drills must be small, focused, and solvable without AI doing the work.

A drill must include:

- Objective.
- Concepts practiced.
- Starter prompt.
- Constraints.
- Expected behavior.
- Self-check questions.
- Do not include the final solution unless Chris explicitly requests a separate answer key and confirms it is not for graded work.

---

## Mini-Project Rule

Every stage should end with one mini-project.

Mini-projects must be small enough to complete, but real enough to prove skill.

Each mini-project must include:

- User story.
- Required concepts.
- Build phases.
- Acceptance checklist.
- Stretch goals parked separately.
- Reflection questions.

Do not overbuild. If scope expands, park it.

---

## Tool Capability Library Rule

The `tool-capability-library/` answers:

> What can code solve?

Each page maps a real-world problem category to Python capabilities.

Example categories:

- Organize files.
- Clean text.
- Read and write spreadsheets.
- Validate forms/data.
- Generate reports.
- Scrape or call APIs.
- Build dashboards.
- Build small internal tools.
- Automate repetitive decisions.

Each capability page must include:

- Problem type.
- Beginner version.
- Python tools involved.
- Prerequisites.
- Example mini-project.
- Business/school relevance.
- Parked advanced version.

---

## Parked Advanced Rule (detail)

Advanced material is allowed in the vault, but it must not pollute the active learning path.

Park material when:

- prerequisite concepts are missing,
- it is useful later but not now,
- it belongs to another hub (`03-WIKIS\BUSINESS`, `03-WIKIS\SYSTEMS`, or `03-WIKIS\TECHNOLOGY`) rather than this Python track,
- it is application architecture before syntax fundamentals,
- it is advanced computer science before programming fluency.

All parked material must record:

- source,
- topic,
- why parked,
- prerequisite needed,
- when to revisit.

---

## Citation and Source Rule (detail)

Every extracted claim must cite its source file and location when available.

Use:

```text
(source: filename, chapter/section/page if available)
```

If the source is OCR-limited or uncertain, state that. Do not invent citations.
