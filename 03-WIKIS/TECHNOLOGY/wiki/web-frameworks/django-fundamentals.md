---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/django]
---

# Django Fundamentals (Models, Views, Templates, Admin)

**Summary**: Django's core MVT (model-view-template) pattern — how a URL request flows through a view function to a database query to a rendered HTML template — plus the built-in admin site for managing data without writing custom CRUD pages.

**Sources**: python-crash-course.pdf (Chapter 18)

**Last updated**: 2026-06-17

---

## Project setup

Standard sequence to start any Django project:

```
python -m venv ll_env              # virtual environment, isolates this project's packages
source ll_env/bin/activate         # (ll_env\Scripts\activate on Windows)
pip install django
django-admin startproject ll_project .   # the trailing dot matters — keeps deployment-friendly structure
python manage.py migrate           # creates the database (SQLite by default) and core tables
python manage.py runserver         # local dev server at localhost:8000
```
(source: python-crash-course.pdf)

A project is a collection of **apps** (`python manage.py startapp appname`) — each app gets its own `models.py`, `admin.py`, `views.py`. Apps must be added to `INSTALLED_APPS` in `settings.py` before Django will use them.

## Models = the data layer

A model is a class inheriting from `django.db.models.Model`; each attribute is a typed field that becomes a database column:

```python
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
```
(source: python-crash-course.pdf)

- `ForeignKey` defines a many-to-one relationship (many entries → one topic). `on_delete=models.CASCADE` means deleting the parent deletes its children — a real data-integrity decision, not boilerplate.
- A `__str__()` method controls how Django displays an instance anywhere (admin site, shell) — always worth defining.
- **Every model change follows the same three-step cycle**: edit `models.py` → `python manage.py makemigrations appname` → `python manage.py migrate`. This is the core workflow for evolving a live app's data shape over time, including against a database that already has user data in it (e.g., adding a required field requires supplying a default for existing rows during migration) (source: python-crash-course.pdf).

## The admin site

`python manage.py createsuperuser` creates a privileged account. Any model registered in `admin.py`...

```python
from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```
(source: python-crash-course.pdf)

...gets a free CRUD interface at `/admin/`. This is the fastest way to seed/manage data without building custom forms — useful for an internal tool or a client's content team needing basic data entry without engineering involvement.

## The Django shell

`python manage.py shell` opens a Python interpreter with the project's models importable, for testing queries before writing them into a view:

```python
Topic.objects.all()              # queryset of all topics
Topic.objects.get(id=1)          # single object by ID
t.entry_set.all()                # all Entry objects related via ForeignKey, by Django convention <model>_set
```
(source: python-crash-course.pdf)

This is the recommended place to debug a query — faster feedback than writing a view, template, and reloading a browser.

## Request flow: URL → view → template

Every page follows the same three-stage pattern:

1. **URL pattern** (`urls.py`) maps a path to a view function, optionally capturing parts of the URL as parameters (e.g., `path('topics/<int:topic_id>/', views.topic, name='topic')` captures an integer as `topic_id`).
2. **View function** (`views.py`) takes the request (+ any captured URL params), queries the database, builds a `context` dict, and calls `render(request, template_path, context)`.
3. **Template** (`.xhtml`/`.html`) receives the context and renders it using Django's template language: `{{ variable }}` for output, `{% for %}...{% endfor %}`, `{% if %}...{% endif %}`, and filters like `{{ value|date:'M d, Y H:i' }}` or `{{ text|linebreaks }}` (source: python-crash-course.pdf).

```python
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)
```
(source: python-crash-course.pdf)

**Template inheritance**: a `base.xhtml` defines shared structure (nav, title) plus a `{% block content %}{% endblock %}` placeholder; every page template starts with `{% extends 'app/base.xhtml' %}` and fills in its own `{% block content %}...{% endblock %}`. Changing the base template propagates to every page — the same "don't repeat yourself" logic as a shared layout component in any frontend framework.

## Connects to

- [[django-auth-and-forms]] — forms, user accounts, and data ownership built on top of these same models/views/templates.
- [[django-deployment]] — styling and shipping this same project to a live server.
- python-crash-course — source tracker for the whole book.
