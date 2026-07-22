---
domain: technology
type: reference
tags: [subject/python]
timeline: later
status: wiki-only
source_role: reference
use_cases: [tech-stack]
stack: [flask]
---

# Web App Hosting and Deployment Options: VPS, PaaS, Web/WSGI Servers, Containers

**Summary**: A landscape map of "where does my Python web app actually
run" — the concrete technology-choice layer that this wiki's existing
`devops/` pages (Phoenix Project's Three Ways, deployment-pipeline
philosophy) don't cover, since those are about deployment *process*, not
deployment *infrastructure choice*. Note on source style: link-directory
format throughout — this page synthesizes the conceptual map, not a quoted
narrative.

**Sources**: fullStackPython.pdf (Full Stack Python: 2020 Supporter's
Edition), §5.1-5.3, 5.5-5.6, 5.9-5.10 (Hosting, VPS, PaaS, Web Servers,
WSGI Servers, Containers, Serverless).

**Last updated**: 2026-07-13

---

## The Layered Decision

Running a Python web app in production is several nested decisions, not
one:

1. **Where does the server live?** — VPS (rent a raw virtual server: e.g.
   Linode, DigitalOcean, AWS Lightsail — you manage the OS) vs. PaaS
   (Heroku, PythonAnywhere, AWS Codestar — the platform manages the OS/
   server, you push code) vs. serverless (AWS Lambda, Azure Functions,
   Google Cloud Functions — no server concept at all, code runs per-request
   and scales to zero).
2. **What web server receives the HTTP request?** — Apache, Nginx, or
   Caddy. A traditional web server understands HTTP but not Python.
3. **What WSGI server actually runs the Python code?** — Green Unicorn
   (Gunicorn), uWSGI, or mod_wsgi. This is the missing piece a raw web
   server needs: the Web Server Gateway Interface (WSGI) is the standard
   contract that lets a web server hand a request off to Python
   application code and get a response back. (Historical note: before WSGI
   standardized this, `mod_python` was the ad hoc, non-standard way Apache
   ran Python code — its security vulnerabilities and stalled development
   are literally why WSGI as a standard exists.)
4. **Is the app containerized?** — Docker packages the app plus its OS-
   level dependencies into a portable unit, so it runs identically
   regardless of which underlying server/cloud it's deployed to. Kubernetes
   is the next layer up: an orchestration system for deploying, scaling,
   and operating many containers together — relevant once there's more
   than a single container to manage, not before.

## The Practical Ladder

For a small client-facing tool (the exact use case
[[flask-web-development]] already scopes toward), the realistic sequence
is: **PaaS first** (Heroku/PythonAnywhere — zero server management, push
code and it runs) → **VPS** once PaaS pricing or control limits bite
(Linode/DigitalOcean/Lightsail — you manage Nginx + Gunicorn yourself, more
control, more responsibility) → **containers/Kubernetes** only once
there's a real multi-service or multi-environment need, not as a default
starting point. This mirrors the same "cheapest fix first" logic
`TECHNOLOGY_LIBRARY_STRATEGY.md`'s Recommendation Ladder already applies to
every other tool category in this wiki.

## Key Ideas

- "Deployment" isn't one decision — it's a stack of independent choices
  (server location, web server, WSGI server, containerization) that can
  each be swapped without touching the others.
- PaaS trades control for simplicity; VPS trades simplicity for control and
  cost savings at scale — the right choice depends on how much ops
  overhead a client engagement can actually absorb, not on which is
  "more professional."
- Containers/Kubernetes solve a real problem (consistent environments,
  multi-service orchestration) that a single small client tool usually
  doesn't have yet — resist reaching for them as a default.

## Connects to

[[flask-web-development]] — this page is the deployment layer that Flask
page's own scoped ingest explicitly excluded (Ch. 15-18, deployment-depth,
were cut from that ingest as "beyond current need"); this page fills that
gap at landscape-awareness depth, not full tutorial depth.
[[../devops/deployment-pipeline-and-continuous-delivery]] — that page
covers the *process* philosophy (small batches, automated validation); this
page covers the *infrastructure* choices that process runs on top of.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Directly relevant the first time a Flask client tool needs to go live |
| Current usefulness | 2 | No live deployment yet, but this is the map for when one happens |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 4 | The concrete "how do I actually ship this" layer under the whole Flask stack |
| Business audit value | 2 | Relevant once a client tool moves from prototype to production |
| Data/workflow value | 2 | Same |
| Reading urgency | 2 | Worth a pass before the first real Flask deployment, not urgent before then |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Use when**: A Flask client tool is ready to go from local development to
something a client can actually reach — start with PaaS (Heroku) for the
first real deployment; move to VPS only once a specific PaaS limitation
bites.

**Do not use when**: Still building/testing locally — this is a
go-live-decision page, not a development-workflow page.

**Fast retrieval query**: `stack/flask` + `use-case/tech-stack`

## North Star Connection

How this applies to the audit business: this is the concrete decision map
for the moment a first Flask client tool ([[flask-web-development]]) is
ready to actually ship — avoids either over-engineering (Kubernetes for a
single small tool) or under-planning (no plan at all for how deployment
actually works). Track relevance: Tech — the production-readiness layer
for the core client-tool stack, paired with
[[task-queues-for-background-jobs]].
