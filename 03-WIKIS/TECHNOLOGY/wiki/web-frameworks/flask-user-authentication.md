---
domain: technology
type: tool
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/tech-stack, use-case/automation, subject/flask, subject/python, stack/flask]
---

# Flask: User Authentication

**Summary**: A complete login system built from Werkzeug password hashing, Flask-Login session management, and itsdangerous token generation — covering secure password storage, an auth blueprint, login/logout, the full Flask-Login request flow, registration with custom validators, and token-based email account confirmation.

**Sources**: FlaskWebDevelopment.pdf (Miguel Grinberg, 2nd ed., 2018), Chapter 8 ("User Authentication")

**Last updated**: 2026-06-20

---

## The Three Authentication Packages

No single package handles authentication end to end, so three are combined: **Flask-Login** (manages the logged-in state in the user session), **Werkzeug** (password hashing/verification — already a Flask dependency), and **itsdangerous** (cryptographically secure, expiring tokens — used for email confirmation and password resets).

## Password Security with Werkzeug

**Never store a password itself** — store a **hash** of it. Werkzeug's `generate_password_hash(password)` applies a random salt plus one-way cryptographic transformations, producing a string with no recoverable path back to the original password; `check_password_hash(hash, password)` verifies a plaintext password against a stored hash, returning `True`/`False`. The standard pattern wraps this in a write-only `password` property on the `User` model:

```python
@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)
```

Reading `user.password` raises an error by design — the plaintext is never retrievable. Two identical passwords from different users produce **different** hashes (because of the random salt), which is itself a property worth unit-testing.

## The Auth Blueprint

Authentication routes live in their own `auth` blueprint (the same mechanism from [[flask-large-application-structure]]), kept in its own template subdirectory (`templates/auth/...`) to avoid naming collisions with other blueprints, and registered with an optional URL prefix (`url_prefix='/auth'`) so every route becomes e.g. `/auth/login`.

## Flask-Login: Session Management

Flask-Login requires the `User` model to implement four items — `is_authenticated`, `is_active`, `is_anonymous`, `get_id()` — most conveniently satisfied by inheriting from Flask-Login's `UserMixin` class, which provides sane defaults for all four. A `LoginManager` instance is created and configured with `login_view = 'auth.login'` (the blueprint-prefixed endpoint Flask-Login redirects unauthenticated users to), and a `@login_manager.user_loader` function tells Flask-Login how to reload a `User` object from the ID stored in the session (`User.query.get(int(user_id))`).

`@login_required` (from Flask-Login) is the decorator that protects any route, redirecting an anonymous visitor to the login page — **decorator order matters**: `login_required` must sit above the route's own logic so it can intercept before the view function runs. `login_user(user, remember=form.remember_me.data)` records the login in the session; the `remember` boolean controls whether a long-term cookie persists the session past the browser closing (`REMEMBER_COOKIE_DURATION` configures its lifetime, default one year). `logout_user()` clears it. `current_user` (a Flask-Login context variable, available in both views and templates) exposes the logged-in user — or a proxy `AnonymousUser` with `is_authenticated == False` — and `current_user.is_authenticated` is the standard "is someone logged in" check, including inside Jinja2 templates for conditionally showing Log In/Log Out links.

**The login route follows Post/Redirect/Get** ([[flask-web-forms]]): on successful login, it redirects to whatever URL was originally requested before being redirected to login (stashed by Flask-Login in `request.args.get('next')`), defaulting to the home page — **and that `next` URL must be validated as relative**, to prevent a malicious actor from using it to redirect a logged-in user to an external phishing site.

**Caution: production deployments must serve the application over HTTPS** — without it, login credentials and session cookies are transmitted in the clear and can be intercepted.

## Registration and Custom Validators

A `RegistrationForm` (Flask-WTF, as in [[flask-web-forms]]) collects email, username, and a confirmed password. WTForms's `Regexp` validator constrains the username format (letters/numbers/dots/underscores, must start with a letter); `EqualTo('password2', message=...)` cross-validates the two password fields match. **Custom field validators** are defined as form methods named `validate_<fieldname>` — WTForms calls these automatically alongside the declared validators, and raising `ValidationError(message)` inside one reports a failure (used here to reject duplicate emails/usernames already in the database). On successful registration, the new `User` is added/committed to the database.

## Token-Based Account Confirmation

To verify a registering user actually owns the email address they gave, the application emails a confirmation link containing a signed, time-limited **token**. itsdangerous's `TimedJSONWebSignatureSerializer` (constructed with the app's `SECRET_KEY` and an `expires_in` value) generates these: `.dumps(data)` produces a signed token string encoding arbitrary data (here, just `{'confirm': user.id}`); `.loads(token)` verifies the signature and expiration and returns the original data, raising an exception if either check fails. This is materially safer than a confirmation link built from a raw, guessable user ID — only the server's secret key can produce a valid signature.

The `User` model gains `generate_confirmation_token()` and a `confirm(token)` method that decodes the token, **checks the embedded ID against the currently logged-in user** (so one user's confirmation token can't be used to confirm a different account), and on success sets a new `confirmed` boolean column to `True`. Sending the actual link requires `url_for(..., _external=True)` — confirmation links go out in an email, not a browser page, so they need a fully qualified absolute URL rather than Flask's default relative path.

**Gating unconfirmed accounts**: a `before_app_request` hook (the blueprint-spanning version of `before_request` — fires for every request in the whole app, not just one blueprint) checks three conditions (user is logged in, account not yet confirmed, requested route isn't part of the auth blueprint or a static file) and redirects to an "unconfirmed" info page if all three hold — letting unconfirmed users log in but blocking them from everything except confirming or resending the confirmation email.

## Account Management (Summarized)

Briefly noted as natural extensions using the same toolkit, with implementations available in the book's companion repository rather than walked through line by line: **password updates** (a logged-in user supplies old + new password, validated the same way as login); **password resets** (the same itsdangerous token pattern as confirmation, emailed on request, verified before allowing a new password); **email address changes** (the new address is held pending until confirmed via a token sent to it, mirroring the registration confirmation flow).

## Key Takeaways

- Never store plaintext passwords — Werkzeug's `generate_password_hash()`/`check_password_hash()` pair, wrapped in a write-only model property, is the standard, low-effort way to do this correctly.
- Flask-Login handles the session-state half of authentication (who's logged in, for how long) but is deliberately agnostic about how credentials are actually verified — that's the application's own job (Werkzeug hashing here).
- itsdangerous's signed, expiring tokens are the correct mechanism for any "prove you control this email address" flow — confirmation, password reset, email change — never build that from a raw guessable ID.
- A production deployment of any authentication system requires HTTPS; without it, the whole scheme is defeated by network interception.

## Connects to

- [[flask-databases-with-sqlalchemy]] — the `User` model, its relationship setup, and the migration requirement when adding the `confirmed` column all build directly on that chapter.
- [[flask-web-forms]] — login/registration forms reuse Flask-WTF/Flask-Bootstrap rendering and the Post/Redirect/Get pattern verbatim.
- [[flask-email-with-flask-mail]] — confirmation emails are sent via the `send_email()` helper from that chapter, rendering both .txt and .html templates.
- [[flask-large-application-structure]] — the auth blueprint follows the exact blueprint-registration pattern introduced there.
- [[web-application-security-basics]] — the HTTPS requirement and the never-store-plaintext-passwords rule are both core items on that page's security checklist.

## North Star Connection

- How this applies to the audit business: any client-facing tool that needs different access levels (a client viewing their own dashboard vs. Chris managing the backend) needs exactly this login system. The token-based confirmation pattern is also directly reusable for any "verify this email/invite a teammate" feature in a client tool, beyond just account signup.
- Track relevance: Tech — required for any multi-user or access-gated client tool.
- Possible future Second Brain use: Yes — this whole chapter is a ready-to-reuse login/registration/confirmation module for a first login-gated client dashboard.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Required the moment a client tool needs to distinguish "client view" from "Chris/admin view." |
| Current usefulness | 3 | Ready to reuse, but only relevant once a tool needs more than one access level. |
| KSU support | 1 | Not connected to ISYE coursework. |
| Tech-stack relevance | 5 | Flask is explicitly in the Top 12 stack. |
| Business audit value | 3 | Indirect — enables access control for a client deliverable rather than an audit technique itself. |
| Data/workflow value | 2 | Access-control mechanism, not a data-handling technique. |
| Reading urgency | 2 | Low urgency until a multi-user client tool is actually scoped. |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Tech-stack decision / automation

**Use when**:
A client tool needs a login-gated dashboard, different access levels (client vs. admin), or an email-verification/invite flow.

**Do not use when**:
The tool is single-user or has no need to gate access by account.

**Fast retrieval query**:
"Flask-Login Werkzeug password hash itsdangerous token" / tags stack/flask + use-case/tech-stack
