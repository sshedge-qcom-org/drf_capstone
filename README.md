# fantasticEnglish

A Django 6.1 + Django REST Framework project that serves a **Business-English lesson corpus** for senior
engineers as a **read-only REST API** and renders the same content as a **MkDocs (Material)** documentation
site.

Lessons are authored as plain-text files in `raw_data/` and flow through a **single shared parser** into both
the database (for the API) and Markdown (for the docs) — so the two can never drift apart.

```
raw_data/dayN ─► services/lesson_parser.py (Django-free dataclasses)
                        │                                   │
        import_lessons  ▼                                   │ export_docs --from-raw
        DB: Lesson / Expression / Example / UpgradePair      │
                        │                 │                  │
                        ├──► DRF API /api/ │                 │
        export_docs ────┴──► markdown_renderer ◄─────────────┘ ─► docs/*.md ─► mkdocs ─► site/
```

## The data

Four "Lite" lessons for senior engineers — **System design**, **Code reviews**, **Production issues**, and
**Sprint planning**. Each teaches 10 expressions (3 idioms, 3 phrasal verbs, 4 C1/C2 vocabulary words) with
meanings, IPA, ❌/✅/⚠️ mistake blocks, labelled example sentences, a "Natural English Upgrade" table, and a
tracker. Totals: **4 lessons / 40 expressions / 104 examples / 40 upgrade pairs**.

## Quick start

Windows, project-local virtualenv at `.venv` (use `.venv/Scripts/python.exe`; Python 3.14, Django 6.1):

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe manage.py migrate
.venv/Scripts/python.exe manage.py import_lessons --clear   # raw_data/ → DB (idempotent)
.venv/Scripts/python.exe manage.py runserver                # http://127.0.0.1:8000/api/
```

Build the docs site:

```bash
.venv/Scripts/python.exe manage.py export_docs --clear      # DB → docs/*.md  (--from-raw skips the DB)
.venv/Scripts/python.exe -m mkdocs serve -a 127.0.0.1:8001  # http://127.0.0.1:8001/
```

## API

Read-only, paginated (page size 20), open (`AllowAny`). Browsable API at `/api/`.

| Endpoint | Description |
| --- | --- |
| `GET /api/lessons/` | Lesson summaries (`+ expression_count`) |
| `GET /api/lessons/{day}/` | Full lesson with nested expressions + upgrades |
| `GET /api/lessons/{day}/expressions/?kind=idiom` | One lesson's expressions, optional `kind` filter |
| `GET /api/expressions/?search=roll&kind=vocabulary` | Browse/search across all lessons |

`kind` is one of `idiom`, `phrasal_verb`, `vocabulary`.

## Management commands

- `manage.py import_lessons [--clear] [--dry-run] [--strict]` — parse `raw_data/` into the DB (idempotent
  upsert on `day_number`).
- `manage.py export_docs [--clear] [--from-raw]` — render lessons to `docs/*.md` (DB by default).

## Tests

```bash
.venv/Scripts/python.exe manage.py test
```

24 tests spanning the parser, import idempotency, the API surface, the Markdown renderer, and a
`mkdocs build --strict` smoke check.

## Layout

- `BusinessEnglish/services/lesson_parser.py` — the Django-free parser (the single structural authority).
- `BusinessEnglish/services/markdown_renderer.py` — `ParsedLesson` → Material Markdown.
- `BusinessEnglish/management/commands/` — `import_lessons`, `export_docs`.
- `BusinessEnglish/{models,serializers,views,urls}.py` — the DB model and read-only API.
- `raw_data/day1..4` — the authored source lessons. `docs/` — generated MkDocs pages.
