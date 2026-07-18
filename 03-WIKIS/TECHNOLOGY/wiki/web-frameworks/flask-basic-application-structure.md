---
domain: technology
type: tool
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/tech-stack, use-case/automation, subject/flask, subject/python, stack/flask]
---

# Flask: Basic Application Structure

**Summary**: How a Flask application is built from the ground up — the application instance, routes and view functions (including dynamic URL segments), the development server and debug mode, the application/request context system, the request and response objects, and request hooks.

**Sources**: FlaskWebDevelopment.pdf (Miguel Grinberg, 2nd ed., 2018), Chapter 2 ("Basic Application Structure")

**Last updated**: 2026-06-20

---

## The Application Instance

Every Flask application creates a single `Flask` instance — `app = Flask(__name__)` — which the web server hands every incoming request to via the WSGI (Web Server Gateway Interface) protocol. The `__name__` argument tells Flask the location of the application's own package, which it needs to find associated files like templates and static assets.

## Routes and View Functions

A **route** maps a URL to the Python function that handles it (a **view function**). The `@app.route('/')` decorator is the standard way to register one; `app.add_url_rule()` is the equivalent non-decorator form. A view function's return value becomes the **response** sent to the client.

Routes can include **dynamic segments** in angle brackets — `@app.route('/user/<name>')` — which Flask passes to the view function as an argument. Dynamic segments are strings by default but can be typed (`<int:id>`, `<float:...>`, `<path:...>` for segments that may contain forward slashes).

## Development Web Server and Debug Mode

`flask run` starts Flask's built-in development server, reading the script name from the `FLASK_APP` environment variable — **this server is for development/testing only, never production** (Chapter 17 in the full book covers production servers, out of scope here). **Debug mode** (`FLASK_DEBUG=1`) enables two features: the **reloader** (auto-restarts the server when source files change) and the **debugger** (an interactive, browser-based stack trace shown on unhandled exceptions, protected by a console-printed PIN). **Never enable debug mode on a production server** — the debugger allows remote code execution.

## Application and Request Contexts

Flask uses **contexts** to make certain objects temporarily, thread-safely "global" without requiring every view function to accept them as explicit arguments — necessary because a multithreaded server handles many simultaneous requests, each needing its own isolated view of these values. Two contexts exist: the **application context** (exposes `current_app`, the active app instance, and `g`, a per-request scratch-storage object) and the **request context** (exposes `request`, the incoming HTTP request, and `session`, a dictionary of values "remembered" across requests for one client). Both contexts are pushed before a request is dispatched and popped after it's handled — accessing any of these four variables outside an active context raises a `RuntimeError`.

## The Request Object

`request` (a request-context variable) exposes everything about the incoming HTTP request: `request.form` (submitted form fields), `request.args` (query-string arguments), `request.cookies`, `request.headers`, `request.files` (uploads), `request.method`, `request.path`/`request.url`, and `request.remote_addr` (client IP), among others.

## Request Hooks

Four decorators register functions to run automatically around the request lifecycle: `before_request` (before every request — e.g., loading the logged-in user), `before_first_request` (once, before the very first request — useful for server init tasks), `after_request` (after every request, only if no unhandled exception occurred), and `teardown_request` (after every request regardless of exceptions). A common pattern is sharing data between a hook and the view function via the `g` context object (e.g., `g.user`).

## Responses

A view function's return value is normally a string (HTML), but Flask also accepts a `(body, status_code)` tuple or a `(body, status_code, headers)` tuple for more control. `make_response()` builds a response object directly, useful when the response needs further configuring (e.g., `response.set_cookie(...)`) before being returned. Two special response helpers: `redirect(url)` issues a 302 redirect to a new URL (commonly used after handling a form submission — see [[flask-web-forms]]), and `abort(code)` immediately raises an HTTP error (e.g., `abort(404)`), short-circuiting the rest of the view function.

## Flask Extensions

Flask deliberately omits database access, form validation, user authentication, and other high-level services from its core — these are expected to come from third-party **extensions** (or hand-rolled code). This is the framework's defining design choice: a small, extensible core rather than a large framework with built-in opinions on every concern.

## Key Takeaways

- A Flask app is fundamentally a URL-to-function map (the route system) plus a request/response cycle — everything else (templates, forms, databases, auth) is an extension layered on top of this core.
- Contexts (`current_app`/`g`/`request`/`session`) exist specifically to avoid threading every view function's argument list with objects it might need — understanding when each is available (app context vs. request context) prevents confusing `RuntimeError`s.
- Debug mode is a development-only convenience (auto-reload + interactive debugger) and a serious security risk if left on in production.

## Connects to

- [[flask-templates-and-jinja2]] — view functions return responses; the next concern is generating those responses cleanly rather than embedding HTML strings in Python code.
- [[flask-web-forms]] — `redirect()`, `session`, and `request.form` introduced here are the exact mechanisms web form handling builds on.

## North Star Connection

- How this applies to the audit business: this is the literal skeleton of any lightweight client-facing tool — a dashboard, a data-entry form, a small internal app for a client's crew to log job data. The route/view-function model is simple enough to build and maintain solo, which matches the audit-retainer model's need for tools that don't require an ongoing engineering team.
- Track relevance: Tech — foundational for any Flask-based client tool.
- Possible future Second Brain use: Not yet — this is foundational knowledge; the conversion candidate is whatever first real client tool gets built on top of it.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The literal skeleton of any lightweight client-facing tool the audit business will build. |
| Current usefulness | 3 | Foundational — useful once a real Flask build starts, not standalone. |
| KSU support | 1 | Not connected to ISYE coursework. |
| Tech-stack relevance | 5 | Flask is in the technology possibility map; timing follows a real web-tool need. |
| Business audit value | 3 | Indirect — enables future client tools rather than a direct audit technique itself. |
| Data/workflow value | 2 | Structural/foundational rather than a data-handling technique. |
| Reading urgency | 2 | Low urgency until an actual Flask build is scheduled. |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Tech-stack decision

**Use when**:
Starting a new Flask project, or needing a refresher on routes/contexts/requests before building a client tool.

**Do not use when**:
The question is about a specific Flask feature (forms, database, auth) — go to that dedicated page instead.

**Fast retrieval query**:
"Flask routes view functions contexts" / tags stack/flask + use-case/tech-stack
