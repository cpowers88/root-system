---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/django]
---

# Django Forms, Authentication & Data Ownership

**Summary**: Letting users submit data through HTML forms (ModelForms), building login/logout/registration with Django's built-in auth system, and restricting both page access and data visibility so each user only sees their own records.

**Sources**: python-crash-course.pdf (Chapter 19)

**Last updated**: 2026-06-17

---

## ModelForms: forms generated from models

A `ModelForm` builds an HTML form directly from a model definition — fields, validation, and types are inferred:

```python
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
```
(source: python-crash-course.pdf)

`widgets` can override the default HTML element for a field (e.g., a larger `forms.Textarea` instead of a single-line input) (source: python-crash-course.pdf).

## The GET/POST view pattern

Every form-handling view follows the same shape: blank form on GET, validate-and-save on POST, then redirect.

```python
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)
```
(source: python-crash-course.pdf)

- `form.is_valid()` does Django's built-in validation (required fields, max lengths, type checks) — a meaningful chunk of input-sanitization work done for free.
- `form.save(commit=False)` lets you attach additional data (e.g., the current user, a foreign key) to the object *before* it's written to the database — used both for setting `owner` on a new topic and for associating a new entry with its topic.
- Templates use `{{ form.as_div }}` to auto-render all form fields, plus `{% csrf_token %}` inside every `<form>` — Django's defense against cross-site request forgery; omitting it breaks the form (source: python-crash-course.pdf).
- Editing an existing object: `EntryForm(instance=entry)` pre-fills the form with current values; `EntryForm(instance=entry, data=request.POST)` applies submitted changes on top of that instance.

## Authentication

Django ships a complete auth system — no need to hand-roll password hashing or session handling.

- **Registration**: `django.contrib.auth.forms.UserCreationForm` validates username/password rules; `form.save()` returns the new `User`, then `login(request, new_user)` logs them in immediately (source: python-crash-course.pdf).
- **Login/logout**: included via `path('', include('django.contrib.auth.urls'))` in an app's `urls.py` — Django provides the views, you provide templates (placed under a `registration/` folder by convention) and the `LOGIN_REDIRECT_URL` / `LOGOUT_REDIRECT_URL` / `LOGIN_URL` settings.
- **Session state in templates**: every template has access to a `user` object — `{% if user.is_authenticated %}` / `{{ user.username }}` lets you branch UI between logged-in and anonymous visitors.
- **Restricting a whole view**: the `@login_required` decorator redirects unauthenticated requests to `LOGIN_URL` automatically:

```python
@login_required
def topics(request):
    ...
```
(source: python-crash-course.pdf)

The book's guidance on scope: decide which pages must stay **public** first (home, registration), then restrict everything else by default — "easier to correct over-restricted access... less dangerous than leaving sensitive pages unrestricted" (source: python-crash-course.pdf). That's a real security default worth carrying into any client-facing app.

## Data ownership: multi-tenant-style isolation

This is the part of the book most directly transferable to client work — making sure user A can never see user B's records, which is the baseline requirement for *any* app with more than one account.

1. Add an `owner` foreign key to the top-level model: `owner = models.ForeignKey(User, on_delete=models.CASCADE)`. Child records (Entries) inherit ownership transitively through their parent (Topic) — you only need to tag the top of the hierarchy.
2. Migrating a non-nullable field onto a table that already has rows forces a choice: supply a one-off default value (e.g., assign all existing rows to an existing user's ID) or define a default in the model. This is a real-world migration concern, not just a tutorial step (source: python-crash-course.pdf).
3. **Filter queries by the current user** rather than returning everything: `Topic.objects.filter(owner=request.user).order_by('date_added')`.
4. **Defense in depth on detail pages**: filtering the list isn't enough — a user could still guess another user's object URL directly (e.g., `/topics/7/`). Explicitly check ownership in every detail/edit view and raise `Http404` if it doesn't match:

```python
topic = Topic.objects.get(id=topic_id)
if topic.owner != request.user:
    raise Http404
```
(source: python-crash-course.pdf)

This two-layer pattern (filter the list + explicitly verify ownership on direct access) is the general shape of authorization checks in any multi-user system — directly applicable to building client tools where different staff/customers must not see each other's data.

## Connects to

- [[django-fundamentals]] — the models, views, and templates this builds on top of.
- [[django-deployment]] — taking this same authenticated, multi-user app live, including the `DEBUG=False` security step.
- python-crash-course — source tracker for the whole book.
