# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`fantasticEnglish` is a Django 6.1 + Django REST Framework project (Python 3.14) that serves a
Business-English lesson corpus as a **read-only REST API** and renders the same content as a **MkDocs
(Material)** documentation site. Lessons are authored as plain-text files in `raw_data/` and flow through a
single shared parser into both the database (for the API) and Markdown (for the docs).

**Status: end-to-end pipeline working.** Models, parser, `import_lessons`, the read-only API, the Markdown
renderer, `export_docs`, the MkDocs site, and a full test suite are all in place. The full loop is:

```
manage.py import_lessons --clear   # raw_data/ → DB   (4 lessons / 40 expressions / 104 examples / 40 upgrades)
manage.py export_docs --clear      # DB → docs/*.md   (or --from-raw to skip the DB)
mkdocs build --strict              # docs/ → site/
manage.py test                     # 24 tests across parser/import/API/renderer/docs
```

The build was completed autonomously and pushed to `github.com/sshedge-qcom-org/drf_capstone` (branch
`daily_dose`). Original phased plan (now largely realized):
`C:\Users\sshedge\.claude\plans\i-want-to-create-quiet-perlis.md`.

## Environment & commands

Windows with a project-local virtualenv at `.venv` (Windows layout — use `.venv/Scripts/python.exe`, there is
no `bin/`). Python 3.14, Django 6.1.

```
# dependencies
.venv/Scripts/python.exe -m pip install -r requirements.txt

# checks / migrations / dev server  (API under /api/, admin under /admin/)
.venv/Scripts/python.exe manage.py check
.venv/Scripts/python.exe manage.py makemigrations
.venv/Scripts/python.exe manage.py migrate
.venv/Scripts/python.exe manage.py runserver               # http://127.0.0.1:8000/

# tests (Django's built-in runner)
.venv/Scripts/python.exe manage.py test                                              # all
.venv/Scripts/python.exe manage.py test BusinessEnglish.tests.SomeTest               # one class
.venv/Scripts/python.exe manage.py test BusinessEnglish.tests.SomeTest.test_method   # one test

# docs site (once mkdocs.yml exists; use 8001 to avoid runserver's 8000)
mkdocs build --strict
mkdocs serve -a 127.0.0.1:8001
```

Planned management commands (per the plan; not all implemented yet):
- `manage.py import_lessons [--clear] [--dry-run] [--strict]` — parse `raw_data/` into the DB.
- `manage.py export_docs [--clear] [--from-raw]` — render lessons to `docs/*.md` for MkDocs.

## Architecture

**Naming gotcha:** the Django project package is lowercase **`fantasticenglish`** (settings/urls/wsgi/asgi),
while the repo directory is camelCase `fantasticEnglish` and the single app is `BusinessEnglish`.

Intended data flow — single source of truth is `raw_data` at authoring time, the DB at serving time:

```
raw_data/dayN ─► BusinessEnglish/services/lesson_parser.py (Django-free dataclasses)
                        │                                   │
        import_lessons  ▼                                   │ export_docs --from-raw
        DB: Lesson / Expression / Example / UpgradePair      │
                        │                 │                  │
                        ├──► DRF API /api/ │                 │
        export_docs ────┴──► markdown_renderer ◄─────────────┘ ─► docs/*.md ─► mkdocs ─► site/
```

The **parser is the one structural authority**; both the API (via the DB) and the docs consume it, so they
cannot diverge. Keep `lesson_parser.py` free of Django imports so it stays unit-testable without the ORM.

DRF config lives in `fantasticenglish/settings.py` (`REST_FRAMEWORK`: PageNumberPagination, PAGE_SIZE 20,
AllowAny) and the API is **read-only** (`ReadOnlyModelViewSet`), wired under `/api/`.

## `raw_data/` source format (read before touching the parser)

`raw_data/day1`–`day4` are extension-less UTF-8 lessons sharing one template: a `key: value` header
(Day/Mode/Focus theme/Dialogue topic/Difficulty/Review items), numbered sections (`1 — Professional Idioms`,
`2 — Phrasal Verbs`, `3 — C1/C2 Vocabulary`, `4 — Natural English Upgrade`, `6 — Speaking Practice`,
`9 — Output Correction`), and a trailing tab-separated `Tracker` table. Each taught expression has
`Meaning:`/`IPA:`, optional `Formality:` (idioms), synonyms/antonyms/collocations (vocab), a ❌/✅(/⚠️) mistake
block, and labelled `... example:` sentences.

Parser gotchas:
- Always `encoding="utf-8"` (❌✅⚠️, curly quotes, em-dashes, IPA glyphs).
- Use `str.splitlines()` — day1–3 are LF, **day4 is CRLF**, and no file ends with a trailing newline.
- Section numbers intentionally **skip 5/7/8** ("Lite" variant); tolerate unknown numbers for future days.
- Two tab-separated tables: section 4 (3 cols) and Tracker (6 cols).
- Label variance (`Common learner mistake:` vs `Common mistake:`); a mistake block may have multiple ✅ lines
  and a ⚠️ note.
- `Tomorrow's preview` placement varies by day (before/after the Tracker, or absent) — parse leniently.
