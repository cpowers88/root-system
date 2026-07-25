---
type: pointer
timeline: reference
status: live
register: ai-loader
tags: [physics, school, governance]
---

# PHYSICS AI LOADER

load_order:
  1: ../../00-BRAIN/AGENT.md
  2: ../../00-BRAIN/CHRIS_CORE.md
  3: ../../00-BRAIN/SYSTEM_FLAGS.md
  4: OPERATIONS.md
  5: wiki/current-position.md
  6: wiki/learning-path.md

rules:
  - `OPERATIONS.md` is the canonical local machine contract.
  - `wiki/current-position.md` is the sole learner-truth authority.
  - Generated packets are readiness, not mastery.
  - Official exact-section course material overrides derivative wiki pages.
  - Never write, move, rename, archive, or delete anything under `raw/`.
  - Do not assist prohibited graded work; when status or policy is unclear, stop and ask Chris.

route:
  human_start: README.md
  human_workflow: HOW_TO_USE.md
  machine_contract: OPERATIONS.md
  page_specs: wiki/authoring-standards.md
