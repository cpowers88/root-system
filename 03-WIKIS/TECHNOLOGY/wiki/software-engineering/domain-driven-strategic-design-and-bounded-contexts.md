---
domain: technology
type: concept
timeline: reference
tags: [priority/later, status/wiki-only, domain/technology, source-role/primary, use-case/tech-stack, subject/ddd, subject/domain-modeling]
---

# Domain-Driven Strategic Design and Bounded Contexts

## Core Idea

Software design begins with the business problem, not the database schema. DDD
first identifies what the organization does, where it differentiates, which
language its experts use, and where different models need explicit boundaries.

## Classify the Business Before Choosing the Build

| Subdomain | Meaning | Default investment decision |
|---|---|---|
| Core | Differentiating capability tied to competitive advantage | Keep close to domain experts; invest in the best design and evolve it |
| Generic | Complex but solved similarly across organizations | Buy or adopt a proven external solution |
| Supporting | Necessary, non-differentiating, usually simple CRUD/ETL logic | Implement simply or outsource; do not overengineer |

This classification is not permanent. Strategy changes can turn a former core
capability into a commodity or make a supporting capability strategically
important. Revisit it when the business model or constraints change.

For the Technology Recommendation Ladder, this sharpens the build decision:
custom work belongs primarily in a real core subdomain or in small integration
glue that existing products cannot supply. Authentication, payments, and other
generic capabilities usually belong to proven vendors.

## Discover the Ubiquitous Language

A ubiquitous language is the precise language domain experts and engineers use
together to describe the business. It must contain business terms, rules,
behaviors, invariants, and important distinctions, not technical translations.

Working rules:

- ask the people who perform or own the domain work, not only intermediaries;
- eliminate ambiguous terms with multiple meanings;
- do not allow different words to hide distinct concepts;
- express rules and examples in language domain experts can correct;
- use the language in conversation, requirements, tests, documentation, and code;
- evolve it continuously as edge cases reveal a better model.

A glossary captures nouns but not enough behavior. Pair it with scenarios,
examples, process maps, or readable acceptance tests. Documentation supports
shared language; it cannot replace direct knowledge exchange.

## Bounded Contexts

A bounded context is the boundary within which one model and its language are
consistent. The same real-world thing may legitimately have different models in
different contexts: a customer in sales, billing, delivery, and support need not
share one enterprise-wide object.

Boundary signals include:

- a term changes meaning between teams or workflows;
- rules and invariants are owned by different experts;
- one model changes for different business reasons than another;
- integration requires translation rather than shared internal objects;
- a team can own the model and its lifecycle end to end.

Subdomains describe the business problem space. Bounded contexts define the
solution/model boundary. They may align, but they are not synonyms.

## Context Map and Integration Relationships

A context map records how bounded contexts and teams relate. Choose the
relationship deliberately:

- **partnership:** teams coordinate changes and success is interdependent;
- **shared kernel:** contexts share a small model/code subset and coordinate it;
- **customer-supplier:** upstream serves downstream needs through an explicit relationship;
- **conformist:** downstream accepts the upstream model as-is;
- **anticorruption layer:** downstream translates the upstream model to protect its own language;
- **open-host service/published language:** upstream exposes a stable protocol for many consumers;
- **separate ways:** integration cost exceeds its value, so contexts do not integrate.

The map is both technical and organizational. A desired API boundary that ignores
team authority and communication constraints will not hold.

## Advisor-Builder Application

During workflow discovery:

1. Identify the business outcome and the domain experts.
2. Record important terms, rules, exceptions, and disagreements.
3. Classify capabilities as core, generic, or supporting.
4. Draw boundaries where terminology, ownership, and change reasons diverge.
5. Apply the Recommendation Ladder inside each boundary.
6. Build only the small area where differentiation or integration economics justify it.

## Failure Modes

- Treating an org chart or database table as a domain boundary.
- Seeking one universal enterprise model for terms that mean different things.
- Building generic capabilities because custom code feels more sophisticated.
- Letting analysts translate all domain knowledge without engineer-expert contact.
- Naming microservices before understanding the business boundaries.

## Source Coverage

Primary source: `raw/LearningDomainDrivenDesign.pdf`, physical PDF pages 1-91
(front matter plus Part I, Chapters 1-4). Chapter 2 is emitted out of physical
order by the tagged text layer and was reconciled into this range through visual
boundary checks. See [[learning-domain-driven-design|source hub]] for complete
446-page disposition.

## Related Pages

- [[learning-domain-driven-design|Learning DDD Source Hub]]
- [[personas-scenarios-and-user-stories|Personas, Scenarios, and User Stories]]
- [[../distributed-systems/microservices|Microservices]]

