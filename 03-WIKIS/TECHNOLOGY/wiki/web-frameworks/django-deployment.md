---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/django]
---

# Styling and Deploying a Django App

**Summary**: Applying Bootstrap for a professional look with minimal custom CSS, then taking a Django project from a local dev server to a live, publicly accessible deployment (Platform.sh in the book's example) — including the production-vs-development settings split and basic hardening.

**Sources**: python-crash-course.pdf (Chapter 20)

**Last updated**: 2026-06-17

---

## Styling with Bootstrap

`django-bootstrap5` (installed via pip, added to `INSTALLED_APPS`) provides template tags that load Bootstrap's CSS/JS and render styled form elements:

```
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
...
{% bootstrap_form form %}
{% bootstrap_button button_type="submit" content="Log in" %}
```
(source: python-crash-course.pdf)

- Practical sequencing lesson: **style last**. Build and verify functionality first with zero styling, then layer Bootstrap on afterward — an app that's pretty but broken is useless, and reversing the order wastes styling work on code that's still changing.
- Bootstrap selectors are applied directly as HTML classes (`navbar`, `card`, `list-group`, `mb-3`, `p-3`) — no custom CSS file needed for a reasonably professional baseline. Useful default for any client deliverable where custom design isn't in scope/budget.
- A base template built once (nav bar, responsive collapse behavior, account-aware links) and inherited everywhere means a full visual refresh later only touches one file.

## Deployment workflow (Platform.sh as the example PaaS)

The general shape here generalizes to most "git push to deploy" PaaS providers, not just Platform.sh specifically:

1. **`requirements.txt`** — generated via `pip freeze > requirements.txt`, tells the remote server exactly which package versions to install so the deployed environment matches local. A separate `requirements_remote.txt` lists packages needed only in production (e.g., `gunicorn` as the production WSGI server, `psycopg2` for Postgres) — dev and prod dependency sets aren't always identical (source: python-crash-course.pdf).
2. **Platform-specific YAML config** (`.platform.app.yaml`, `routes.yaml`, `services.yaml`) declares the runtime, build/deploy hook commands, routing rules, and attached services (e.g., a Postgres database) — every PaaS has some equivalent declarative config; the structure (build hooks → deploy hooks → routing) is a recurring pattern worth recognizing in any hosting provider's docs.
3. **Settings split by environment**: a block at the end of `settings.py`, gated on detecting the live platform, overrides `ALLOWED_HOSTS`, `STATIC_ROOT`, `SECRET_KEY`, and the database connection — `DATABASES` switches from local SQLite to the platform's Postgres credentials only when actually running remotely (source: python-crash-course.pdf). This single-file environment branch is a lighter-weight alternative to separate `settings/dev.py` / `settings/prod.py` modules.
4. **Git is the deployment mechanism**: `git init` → `git add .` → `git commit` → `platform create` (registers the remote project) → `platform push` (deploys). A `.gitignore` excludes the virtual environment, `__pycache__`, and the local SQLite file — the local dev database should never be pushed over the production one.
5. **Post-deploy steps mirror local setup**: SSH into the live environment (`platform environment:ssh`) to run `createsuperuser` against the production database, since local superusers don't exist there.

## Security hardening before going live

- **`DEBUG = False` in production is non-negotiable.** With `DEBUG=True`, an unhandled error dumps a full traceback including settings, installed packages, and request data to any visitor — a direct information-disclosure risk. This is set conditionally, only when the platform-detection check confirms the code is running remotely, so local debugging is unaffected (source: python-crash-course.pdf).
- **Custom error templates** (`404.xhtml`, `500.xhtml` in the project's root template directory) replace Django's generic error pages with ones styled consistently with the rest of the site — small detail, but it's the difference between "this site looks broken" and "this site handled an error gracefully" from a client's end-user perspective.
- **Ongoing change process** is the same loop every time: edit locally → `git add`/`commit` → `platform push` → verify on the live URL. Database migrations run automatically via the deploy hook, so schema changes ship the same way as code changes.

## Connects to

- [[django-auth-and-forms]] — the authenticated, multi-user app being deployed here.
- [[django-fundamentals]] — the underlying models/views/templates this ships to production.
- python-crash-course — source tracker for the whole book.

This chapter is the clearest single link in the book to the audit/integration business: **build it locally → style it minimally → ship it to a real URL a client can use**, including the specific security step (`DEBUG=False`) that's easy to forget and directly exposes a client's data if missed. Worth proposing a link to a future `wiki/business/` page on client deliverable handoff once that side of the wiki exists.
