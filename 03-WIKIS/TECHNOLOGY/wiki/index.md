---
type: map
timeline: reference
tags: [technology]
---

# TECHNOLOGY Wiki — Index

### Scope: tech-skill and tech-adoption roadmap, plus (as of July 7, 2026) an applied-reference layer inherited from FORGE's retirement — deep technical material on web frameworks, distributed systems, DevOps, AI/LLM concepts, and applied data science. Spine reference: `02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md`.

## Status

68 pages migrated from FORGE's `wiki\technology\` on July 7, 2026, split by subject
from FORGE's original 135-page technology folder (the other 67 — Python/data-analysis
fundamentals — went to `03-WIKIS\PYTHON` instead; see that wiki's `source-map.md`).
**2026-07-13: full raw/ audit and ingest (107 pages at completion; 106 current).**
The audit produced 39 new pages across 9 books + 4 landscape clippings. The
July 15 structure review moved the post-closure AI-coding landscape into
`03-WIKIS\AI_AUTOMATION_SYSTEMS`, its canonical intake lane. The audit found 3 confirmed
duplicates (documented, not re-ingested), 3 misplaced Python-fundamentals books
(rerouted to `03-WIKIS\PYTHON`), and 1 book judged too introductory to warrant a
dedicated ingest (see `log.md`). Four new category subfolders added
(`database-sql/`, `software-craft/`, `security/`, `software-engineering/`) plus
the wiki's first-ever landscape-research pages (3 remain at wiki root) — the original
stated purpose this wiki carried as an open "next action" since July 7.
The 28-file raw collection (~669 MiB) is fully accounted, not uniformly compiled:
five Stanford AI Index files are covered cross-hub, the prior PDFs were compiled
or explicitly classified, and earlier web clips have derived or lookup coverage.
The July 16 intake added *Learning Domain-Driven Design* and *The Elements of User
Experience* as need-driven applied references plus a 2016 data-mining adoption deck
as historical context; none is marked compiled.

## Web Frameworks (`web-frameworks/`, 15 pages)

- [[web-frameworks/flask-web-development|Flask Web Development]] — source summary and navigation hub
- [[web-frameworks/flask-basic-application-structure|Flask: Basic Application Structure]]
- [[web-frameworks/flask-templates-and-jinja2|Flask: Templates and the Jinja2 Engine]]
- [[web-frameworks/flask-web-forms|Flask: Web Forms]]
- [[web-frameworks/flask-databases-with-sqlalchemy|Flask: Databases with Flask-SQLAlchemy]]
- [[web-frameworks/flask-user-authentication|Flask: User Authentication]]
- [[web-frameworks/flask-email-with-flask-mail|Flask: Email with Flask-Mail]]
- [[web-frameworks/flask-large-application-structure|Flask: Large Application Structure]]
- [[web-frameworks/flask-rest-apis|Flask: Building RESTful APIs]]
- [[web-frameworks/django-fundamentals|Django Fundamentals (Models, Views, Templates, Admin)]]
- [[web-frameworks/django-auth-and-forms|Django Forms, Authentication & Data Ownership]]
- [[web-frameworks/django-deployment|Styling and Deploying a Django App]]
- [[web-frameworks/lightweight-python-web-frameworks-beyond-flask-django|Lightweight Python Web Frameworks Beyond Flask/Django]] — Bottle, Pyramid, TurboGears, Falcon (source: *Full Stack Python*)
- [[web-frameworks/task-queues-for-background-jobs|Task Queues for Background Jobs]] — Celery, RQ, Dramatiq (source: *Full Stack Python*)
- [[web-frameworks/web-app-hosting-and-deployment-options|Web App Hosting and Deployment Options]] — VPS/PaaS/WSGI/containers/serverless decision map (source: *Full Stack Python*)

## Distributed Systems (`distributed-systems/`, 19 pages)

- [[distributed-systems/foundations-of-scalable-systems|Foundations of Scalable Systems (Ian Gorton)]]
- [[distributed-systems/scalability-fundamentals|Scalability Fundamentals]]
- [[distributed-systems/application-services|Application Services: API Design, State, and Horizontal Scaling]]
- [[distributed-systems/concurrency-fundamentals|Concurrency Fundamentals]]
- [[distributed-systems/asynchronous-messaging|Asynchronous Messaging]]
- [[distributed-systems/microservices|Microservices]]
- [[distributed-systems/distributed-systems-essentials|Distributed Systems Essentials]]
- [[distributed-systems/distributed-systems-architecture-patterns|Distributed Systems Architecture Patterns]]
- [[distributed-systems/distributed-caching|Distributed Caching]]
- [[distributed-systems/distributed-database-implementations|Distributed Database Implementations: Redis, MongoDB, DynamoDB]]
- [[distributed-systems/scalable-database-fundamentals|Scalable Database Fundamentals]]
- [[distributed-systems/eventual-consistency|Eventual Consistency]]
- [[distributed-systems/strong-consistency|Strong Consistency]]
- [[distributed-systems/scalable-event-driven-processing|Scalable Event-Driven Processing (Apache Kafka)]]
- [[distributed-systems/stream-processing-systems|Stream Processing Systems (Apache Flink)]]
- [[distributed-systems/serverless-processing|Serverless Processing Systems]]
- [[distributed-systems/storage-engines-btrees-and-lsm-trees|Storage Engines: B-Trees and LSM-Trees]] — source: Kleppmann, *Designing Data-Intensive Applications*
- [[distributed-systems/transaction-isolation-levels-and-concurrency-control|Transaction Isolation Levels and Concurrency Control]] — read committed, snapshot isolation/MVCC, write skew (source: Kleppmann)
- [[distributed-systems/serializability-2pl-and-serializable-snapshot-isolation|Serializability: 2PL and Serializable Snapshot Isolation]] — source: Kleppmann

## DevOps & IT Operations (`devops/`, 19 pages)

- [[devops/the-phoenix-project|The Phoenix Project (Gene Kim, Kevin Behr & George Spafford)]]
- [[devops/the-three-ways-devops|The Three Ways (DevOps)]]
- [[devops/devops-origins-and-myths|DevOps Origins and Myths]]
- [[devops/devops-reading-map|DevOps Reading Map]]
- [[devops/four-types-of-work|The Four Types of Work (IT Operations)]]
- [[devops/it-operations-bottleneck-management|IT Operations as a Bottleneck-Management Problem]]
- [[devops/it-work-centers-and-kanban|IT Work Centers and Kanban]]
- [[devops/it-risk-and-business-value-chains|IT Risk and Business Value Chains]]
- [[devops/change-management-failure-modes|Why Change Management Programs Collapse (and What Bill Tries Instead)]]
- [[devops/deployment-pain-and-deploy-frequency|Deployment Pain: The Lengthening-Interval Downward Spiral]]
- [[devops/deployment-pipeline-and-continuous-delivery|Deployment Pipeline and Continuous Delivery]]
- [[devops/resilience-engineering-and-chaos-testing|Resilience Engineering and Chaos Testing]]
- [[devops/security-work-and-business-outcomes|Security Work and Business Outcomes]]
- [[devops/web-application-security-basics|Web Application Security Basics: SQL Injection and CSRF]]
- [[devops/final-tips-for-success|Final Tips for Success: Automation, Observability, Deployment, Data Lakes]]
- [[devops/conways-law-and-organizational-design|Conway's Law and Organizational Design]] — source: *The DevOps Handbook*
- [[devops/production-telemetry-and-monitoring-architecture|Production Telemetry and Monitoring Architecture]] — the 3-layer monitoring architecture; source: *The DevOps Handbook*
- [[devops/just-culture-and-blameless-postmortems|Just Culture and Blameless Postmortems]] — source: *The DevOps Handbook*
- [[devops/integrating-security-into-the-deployment-pipeline|Integrating Security into the Deployment Pipeline]] — source: *The DevOps Handbook*

## AI & LLM Concepts (`ai-and-llm/`, 10 pages)

- [[ai-and-llm/llm-fundamentals|LLM Fundamentals: Pretraining, Fine-Tuning, and Emergence]]
- [[ai-and-llm/ai-alignment-and-ethics|AI Alignment and Ethics]]
- [[ai-and-llm/co-intelligence-mollick|Co-Intelligence: Living and Working with AI (Ethan Mollick)]]
- [[ai-and-llm/four-rules-for-co-intelligence|Four Rules for Co-Intelligence]]
- [[ai-and-llm/ai-as-a-coworker|AI as a Coworker: Tasks, Systems, Jobs, and the Centaur/Cyborg Distinction]]
- [[ai-and-llm/ai-as-a-person|AI as a Person: Behavioral Realism and the Limits of the Turing Test]]
- [[ai-and-llm/ai-as-tutor-and-coach|AI as a Tutor and Coach]]
- [[ai-and-llm/ai-creativity-and-hallucination|AI Creativity and Hallucination]]
- [[ai-and-llm/ai-future-scenarios|AI Future Scenarios]]
- [[ai-and-llm/ai-developer-tools-landscape-2026|AI Developer Tools Landscape (2026)]]

## Applied Data Science / ML (`data-science-ml/`, 18 pages)

- [[data-science-ml/data-driven-decision-making-and-data-science-definition|Data-Driven Decision-Making: What It Actually Buys You, and Why "Big Data" Isn't "Data Science"]]
- [[data-science-ml/crisp-dm-process-and-data-leakage|The CRISP-DM Process: Why Data Mining Is R&D, Not Software Engineering]]
- [[data-science-ml/canonical-data-mining-tasks-and-supervised-unsupervised|The Nine Canonical Data Mining Tasks]]
- [[data-science-ml/related-analytics-techniques-and-business-questions|Statistics, Database Queries, OLAP, and Data Mining Are Different Tools]]
- [[data-science-ml/information-gain-entropy-and-attribute-selection|Information Gain and Entropy]]
- [[data-science-ml/tree-induction-and-decision-boundaries|Tree Induction: "Find the Best Split, Then Recurse"]]
- [[data-science-ml/tree-vs-linear-models-and-nonlinear-extensions|Trees vs. Linear Models]]
- [[data-science-ml/linear-regression-least-squares-and-logistic-regression|Why "Least Squares" Is a Convenience, Not a Law of Nature]]
- [[data-science-ml/linear-discriminants-objective-functions-and-svm|Parametric Modeling: "Best Fit" as a Choice, Not a Fact]]
- [[data-science-ml/probability-estimation-trees-laplace-correction-and-churn-case|Why a Model That Predicts "Nobody Defaults" Can Still Be Useful]]
- [[data-science-ml/generalization-overfitting-and-fitting-graphs|Overfitting: "If You Torture the Data Long Enough, It Will Confess"]]
- [[data-science-ml/holdout-cross-validation-and-learning-curves|Cross-Validation and the Lab-vs-Field Mismatch]]
- [[data-science-ml/data-asset-strategy-signet-bank-capital-one-case|Data as a Strategic Asset: Signet Bank → Capital One]]
- [[data-science-ml/business-experimentation-and-project-unicorn|Business Experimentation and Project Unicorn]]
- [[data-science-ml/date-driven-launch-failure|Date-Driven Launches and the Cost of Cutting Testing/Ops Readiness]]
- [[data-science-ml/estimates-of-location-and-variability|Estimates of Location and Variability]] — mean/median/trimmed mean, variance/MAD/IQR (source: *Practical Statistics for Data Scientists*)
- [[data-science-ml/statistical-distributions-normal-long-tailed-t-and-binomial|Statistical Distributions: Normal, Long-Tailed, t, and Binomial]] — source: *Practical Statistics for Data Scientists*
- [[data-science-ml/ab-testing-hypothesis-tests-and-p-values|A/B Testing, Hypothesis Tests, and P-Values]] — the ASA's 2016 p-value misinterpretation caution; source: *Practical Statistics for Data Scientists*

## Database & SQL (`database-sql/`, 11 pages, new 2026-07-13)

- [[database-sql/practical-sql|Practical SQL — Source Summary and Navigation Hub]]
- [[database-sql/sql-select-where-and-filtering|SQL: SELECT, WHERE, and Filtering]]
- [[database-sql/sql-data-types|SQL: Data Types]]
- [[database-sql/sql-importing-and-basic-math|SQL: Importing Data and Basic Math]]
- [[database-sql/sql-joining-tables-and-relationships|SQL: Joining Tables and Relationships]]
- [[database-sql/sql-table-design-constraints-and-indexes|SQL: Table Design, Constraints, and Indexes]]
- [[database-sql/sql-grouping-and-aggregate-functions|SQL: Grouping and Aggregate Functions]]
- [[database-sql/sql-inspecting-and-modifying-data|SQL: Inspecting and Modifying Data]]
- [[database-sql/sql-window-functions-and-ranking|SQL: Window Functions and Ranking]]
- [[database-sql/sql-advanced-query-techniques|SQL: Advanced Query Techniques]]
- [[database-sql/sql-views-functions-and-triggers|SQL: Views, Functions, and Triggers]]

## Software Craft (`software-craft/`, 4 pages, new 2026-07-13)

- [[software-craft/clean-code-naming-functions-and-comments|Clean Code: Naming, Functions, and Comments]] — source: Robert C. Martin, *Clean Code*
- [[software-craft/clean-code-error-handling-testing-and-smells-checklist|Clean Code: Error Handling, Testing, and the Smells Checklist]] — source: *Clean Code*
- [[software-craft/the-clean-coder-professionalism-and-saying-no|The Clean Coder: Professionalism and Saying No]] — source: Martin, *The Clean Coder*
- [[software-craft/pragmatic-programmer-core-principles|Pragmatic Programmer Core Principles]] — DRY, broken windows, orthogonality, tracer bullets; source: Hunt & Thomas, *The Pragmatic Programmer*

## Security (`security/`, 3 pages, new 2026-07-13)

- [[security/hacking-apis-source-summary|Hacking APIs — Source Summary and Navigation Hub]] — source: Corey Ball, *Hacking APIs*
- [[security/api-vulnerability-classes-owasp-top-10|API Vulnerability Classes: The OWASP API Security Top 10]] — reframed as audit checks, not attack techniques
- [[security/api-security-testing-engagement-scoping-and-checklist|API Security Testing: Engagement Scoping and Checklist]]

## Software Engineering (`software-engineering/`, 4 pages, new 2026-07-13)

- [[software-engineering/agile-software-engineering-and-scrum|Agile Software Engineering and Scrum]] — source: Ian Sommerville, *Engineering Software Products*
- [[software-engineering/personas-scenarios-and-user-stories|Personas, Scenarios, and User Stories]] — source: Sommerville
- [[software-engineering/reliable-programming-techniques|Reliable Programming Techniques]] — complexity, patterns, refactoring, defensive validation; source: Sommerville
- [[software-engineering/software-testing-levels-and-techniques|Software Testing Levels and Techniques]] — source: Sommerville

## Landscape Research (wiki root, 3 pages, new 2026-07-13)

This wiki's first landscape-research pages — the original stated purpose
(tool/category watching, tied to `TECHNOLOGY_LIBRARY_STRATEGY.md`'s 12
categories) carried as an open "next action" since July 7, 2026.

- [[looker-studio-free-bi-dashboards|Looker Studio (Data Studio) — Free BI Dashboards]] — Category 3
- [[vs-code-data-tooling-data-wrangler-and-edit-csv|VS Code Data Tooling: Data Wrangler, Edit CSV, and the Titanic Tutorial]] — Category 5
- [[spreadjs-embeddable-excel-import-export|SpreadJS — Embeddable Excel Import/Export for Custom Web Tools]] — Category 9/12, landscape-only
