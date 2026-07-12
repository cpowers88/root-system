---
domain: tech
type: reference
tags: [priority/later, status/wiki-only, subject/devops]
---

# DevOps Origins and Myths

**Summary**: The Phoenix Project Resource Guide positions DevOps as the application of Lean principles to the whole IT value stream, then clears away common misunderstandings that make enterprises dismiss or shrink it.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Resource Guide "Where DevOps Came From" and "Top DevOps Myths", pp. 354-361)

**Last updated**: 2026-06-18

---

## Where DevOps came from

The Resource Guide says the term "devops" was coined by Patrick Debois and Andrew Shafer in 2008, and the book uses "DevOps" to mean the outcome of applying Lean principles to accelerate work through Product Management, Development, QA, IT Operations, and InfoSec (source: thePhoenixProject.pdf, p. 354).

DevOps builds on Agile, continuous integration, continuous deployment, Lean Startup, Innovation Culture, Toyota Kata, Rugged Computing, and the Velocity community, rather than replacing all earlier practice with one new doctrine (source: thePhoenixProject.pdf, pp. 354-355). The point is convergence: many movements were independently pushing toward smaller batches, faster feedback, safer production systems, and tighter collaboration across the IT value stream.

## Myths the appendix rejects

- **DevOps replaces Agile**: DevOps extends Agile's definition of done past "code complete" to tested and operating in production as designed; Agile helps, but is not a prerequisite (source: thePhoenixProject.pdf, p. 358).
- **DevOps replaces ITIL/ITSM**: ITIL and ITSM still describe important operations capabilities, but faster lead times require automation around change, configuration, and release, while incident/problem management remain important for fast recovery (source: thePhoenixProject.pdf, pp. 358-359).
- **DevOps means NoOps**: Operations work does not disappear; more of it becomes self-service or is taken on by Development, especially environment creation, telemetry, deployment, and service-level responsibility (source: thePhoenixProject.pdf, p. 359).
- **DevOps is only for open-source stacks**: the appendix names .NET, SAP, COBOL/mainframe, and firmware examples to stress that the principles are largely technology-independent, even when some implementation patterns require automation or version-controlled configuration (source: thePhoenixProject.pdf, pp. 359-360).
- **DevOps is just infrastructure as code or automation**: automation matters, but DevOps also requires shared goals and shared pain across the IT value stream (source: thePhoenixProject.pdf, p. 360).
- **DevOps is only for startups and unicorns**: the Resource Guide argues that enterprises need DevOps because they must increase planned-work flow while maintaining quality, reliability, and security; it lists large financial services, retail, higher education, and government adopters as evidence (source: thePhoenixProject.pdf, pp. 360-361).

## North Star application

For the audit/integration business, this page is a diagnostic guardrail. A client can reject DevOps by making it sound like "we do not use open source," "we are ITIL," "we cannot get rid of Ops," or "we are not a startup." The appendix's answer is to translate DevOps back into business-system language: improve planned-work flow, preserve operational quality, shorten feedback, and make the work visible.

## Connects to

- [[the-phoenix-project]] - source tracker for the full narrative and appendix.
- [[the-three-ways-devops]] - the origins and myths page explains the broader movement behind the Three Ways.
- [[deployment-pipeline-and-continuous-delivery]] - the "not just automation" point keeps the pipeline framed as a socio-technical system, not only tooling.
- [[deployment-pain-and-deploy-frequency]] - the myths explain why enterprises often resist the very practices that would fix their release pain.
- [[devops-reading-map]] - the appendix's further reading list identifies the source bodies behind these claims.
