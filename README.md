# drf_capstone

A hands-on project to **learn Django REST Framework (DRF) from the ground up**,
one concept at a time, in plain language.

Instead of a toy example, we build a genericized clone of an
**open-source program-office system**: organizations own projects, projects hold
git repositories, repositories get mirrored elsewhere, and role-based access
grants tie users to projects. Learning DRF and a real-world app design at once.

The full, step-by-step curriculum lives in **[docs/LEARNING_PLAN.md](docs/LEARNING_PLAN.md)**,
and each phase has its own detailed walkthrough under [docs/](docs/).

## How this works

For each concept the tutor explains it in plain terms + *why* it exists, then
hands over copy-paste-ready code; **you** paste it into the files yourself (typing
it is how you learn), then the tutor reviews it. The tutor maintains the `docs/`
files; you own the code. Each phase ends with running the server, testing, and
pushing to GitHub. Check off `[ ]` items in the plan as you go.

## Curriculum — jump to a phase

Each links to its section in the plan; per-phase deep-dives live in `docs/phaseN_*.md`.

| # | Phase | # | Phase |
|---|---|---|---|
| 1 | [Foundations & REST fundamentals](docs/LEARNING_PLAN.md#phase-1-foundations--rest-fundamentals) | 10 | [Permissions](docs/LEARNING_PLAN.md#phase-10-permissions--deciding-what-you-may-do) |
| 2 | [Django ORM & project setup](docs/LEARNING_PLAN.md#phase-2-django-orm-refresher--project-setup) | 11 | [Throttling](docs/LEARNING_PLAN.md#phase-11-throttling--rate-limiting-abuse) |
| 3 | [Serializers Pt.1](docs/LEARNING_PLAN.md#phase-3-serializers-part-1--translating-models-to-json) | 12 | [Pagination](docs/LEARNING_PLAN.md#phase-12-pagination--serving-big-lists-in-chunks) |
| 4 | [Serializers Pt.2 (validation)](docs/LEARNING_PLAN.md#phase-4-serializers-part-2--validation--advanced-fields) | 13 | [Filtering/Search/Ordering](docs/LEARNING_PLAN.md#phase-13-filtering-searching--ordering) |
| 5 | [Relations & nested serializers](docs/LEARNING_PLAN.md#phase-5-relations--nested-serializers) | 14 | [Negotiation/Renderers/Versioning](docs/LEARNING_PLAN.md#phase-14-content-negotiation-renderersparsers--versioning) |
| 6 | [Views Pt.1 (function-based)](docs/LEARNING_PLAN.md#phase-6-views-ladder-part-1--function-based-views) | 15 | [Exception handling](docs/LEARNING_PLAN.md#phase-15-exception-handling) |
| 7 | [Views Pt.2 (class-based/generic)](docs/LEARNING_PLAN.md#phase-7-views-ladder-part-2--class-based--generic-views) | 16 | [Testing](docs/LEARNING_PLAN.md#phase-16-testing-the-api) |
| 8 | [ViewSets, routers & actions](docs/LEARNING_PLAN.md#phase-8-viewsets-routers--custom-actions) | 17 | [Schema & docs](docs/LEARNING_PLAN.md#phase-17-schema--documentation) |
| 9 | [Authentication](docs/LEARNING_PLAN.md#phase-9-authentication--proving-who-you-are) | 18 | [Performance & advanced](docs/LEARNING_PLAN.md#phase-18-performance--advanced-topics) |

## Tech stack

Django 5.2 LTS · djangorestframework 3.16 · SQLite · (added as needed:
simplejwt, django-filter, drf-nested-routers, drf-spectacular, Pillow).
See the [stack table](docs/LEARNING_PLAN.md#tech-stack-2026-current) for versions.

## Running (once set up in Phase 2)

```bash
source .venv/bin/activate
python manage.py runserver
# browse the DRF browsable API at http://127.0.0.1:8000/api/
```
