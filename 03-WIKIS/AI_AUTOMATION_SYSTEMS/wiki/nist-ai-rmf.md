---
type: research
tags: [ai-automation, governance, risk-management, nist, audit-vocabulary]
source: raw/NIST.AI.100-1.pdf (NIST AI RMF 1.0, January 2023)
---

# NIST AI Risk Management Framework (AI RMF 1.0)

**NIST AI 100-1, January 2023.** The U.S. reference framework for managing
AI risk — voluntary, rights-preserving, sector-agnostic, directed by the
National AI Initiative Act of 2020. A living document (formal community
review expected by 2028; companion Playbook updated continually).

## One-paragraph summary

The AI RMF gives organizations a shared structure and vocabulary for
managing AI risk across the system lifecycle. Part 1 frames why AI risk is
different (socio-technical systems, data drift, emergent behavior, hard-to-
measure harms — see its Appendix B on how AI risks differ from traditional
software risks) and defines seven **trustworthiness characteristics**.
Part 2 is the **Core**: four functions — GOVERN, MAP, MEASURE, MANAGE —
broken into categories/subcategories, with GOVERN cross-cutting and the
other three applied per-system. Its center of gravity is the same finding
this wiki logged from industry interviews: trust is built by
*verification* — documented, repeatable measurement — not by capability.

## The seven trustworthiness characteristics

Valid & reliable (the necessary base condition); safe; secure & resilient;
accountable & transparent (cross-cutting — relates to all others);
explainable & interpretable; privacy-enhanced; fair with harmful bias
managed. Tradeoffs between them are expected; measurement is what makes
the tradeoff decisions traceable.

## The four Core functions

- **GOVERN** (cross-cutting, always on): risk-management culture,
  policies, accountability structures, AI inventory and decommissioning
  processes, third-party/legal handling. Senior leadership sets risk
  tolerance; documentation is the accountability backbone.
- **MAP** (context first): establish intended purpose, users, business
  value, and risk tolerances *before* measuring anything — because early
  design decisions and deployment context shape impacts that no single
  actor in the lifecycle can see alone. MAP outputs are the basis for the
  other two functions, including the threshold question "is an AI solution
  appropriate here at all?"
- **MEASURE**: quantitative/qualitative assessment of the mapped risks —
  rigorous testing before deployment and regularly in operation, TEVV
  (test, evaluation, verification, validation) processes, independent
  review to counter internal bias, tracked metrics for trustworthy
  characteristics.
- **MANAGE**: allocate resources to the mapped-and-measured risks per the
  GOVERN-set tolerance; response/recovery/communication plans; monitor
  residual risk and emergent risk continually.

**Profiles** then instantiate the Core for a sector or use case — a
"current profile" vs. "target profile" comparison shows the gap to close.

## Why this matters for this wiki / `.ROOT`

- **It formalizes the verification-gap finding.** MEASURE is the
  institutional version of what [[agentic-ai-industry-adoption-barriers]]
  found empirically: deployment is gated on verification capacity. The
  [[root-maturity-self-assessment]] flagged Chris's review time as
  `.ROOT`'s scaling limit — in RMF terms, `.ROOT` has a strong GOVERN
  (AI_Agent.md (now AGENT.md), hats, flags, review cadence) and MAP (routing, scope
  rules), a thin MEASURE, and a MANAGE embodied in the
  handoff→weekly→monthly→quarterly cadence. That framing sharpens the
  drift-check baseline without requiring any governance change.
- **Audit vocabulary for client work.** For the castle's profit-skill
  gate and any future AI-readiness audit offering: GOVERN/MAP/MEASURE/
  MANAGE and the seven characteristics are the credible, citable skeleton
  a small-business audit can hang on — "voluntary NIST framework" travels
  well with U.S. clients. The Profiles concept (current vs. target) is
  literally an audit deliverable format.
- **Complements the vetting screen.** The Category 10 screen vets *tools*;
  the RMF frames the *organization using them*. Together they cover both
  sides of the question a client will actually ask.
- Related: [[mcp-security-and-authorization]] supplies the
  secure-and-resilient depth for the specific case of MCP-connected
  agents; [[2025-ai-agent-index]] documents how rarely deployed agents
  publish anything MEASURE-shaped.

---
*Processed July 8, 2026. Source PDF in `raw/` (immutable); text extracted
to scratchpad for reading. Note: published January 2023 — predates the
agentic wave; NIST's generative-AI companion profile (NIST AI 600-1) is
not in `raw/` and would be the natural follow-up source.*

