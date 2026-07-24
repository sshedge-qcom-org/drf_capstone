# Django REST Framework — Topic Guide

A structured, checkable study guide for **Django REST Framework**, split one file
per topic across two tracks: **Core** (the DRF API surface) and **Advanced**
(production concerns and companions).

![Topics](https://img.shields.io/badge/topics-41-blue)
![Core](https://img.shields.io/badge/core-24-success)
![Advanced](https://img.shields.io/badge/advanced-17-orange)
![Format](https://img.shields.io/badge/format-checklist-informational)

> [!NOTE]
> **How to use this guide**
> - Each topic is its own file with a table of contents, collapsible groups, and a bottom **nav bar** (◀ Prev · ↑ Top · Next ▶ · ⌂ Home).
> - Every item is a task-list checkbox — tick `- [x]` as you learn it and GitHub shows live progress per file.
> - Items marked **🆕** were added by a coverage audit against the official [DRF API guide](https://www.django-rest-framework.org/api-guide/); files badged `merged` combine former separate topics; files badged `companion` are production topics that are **not** stock DRF.

---

## Core Topics

The DRF API surface, in learning order.

| # | Topic | # | Topic |
|---|---|---|---|
| 1 | [Serializer](topics/core/01-serializer.md) | 13 | [ViewSets](topics/core/13-viewsets.md) |
| 2 | [ModelSerializer](topics/core/02-modelserializer.md) | 14 | [Routers](topics/core/14-routers.md) |
| 3 | [Validation](topics/core/03-validation.md) | 15 | [Format Suffixes & Browsable API](topics/core/15-format-suffixes-browsable-api.md) 🆕 |
| 4 | [SerializerMethodField](topics/core/04-serializermethodfield.md) | 16 | [Authentication](topics/core/16-authentication.md) |
| 5 | [Nested Serializers](topics/core/05-nested-serializers.md) | 17 | [Permissions](topics/core/17-permissions.md) |
| 6 | [Serializer Relations](topics/core/06-serializer-relations.md) 🆕 | 18 | [Filtering](topics/core/18-filtering.md) |
| 7 | [Function-Based Views](topics/core/07-function-based-views.md) | 19 | [Pagination](topics/core/19-pagination.md) |
| 8 | [APIView](topics/core/08-apiview.md) | 20 | [Throttling](topics/core/20-throttling.md) |
| 9 | [Renderers, Parsers & Content Negotiation](topics/core/09-renderers-parsers-content-negotiation.md) 🆕 | 21 | [Versioning](topics/core/21-versioning.md) |
| 10 | [GenericAPIView](topics/core/10-genericapiview.md) | 22 | [Exception Handling](topics/core/22-exception-handling.md) |
| 11 | [Mixins](topics/core/11-mixins.md) | 23 | [Testing](topics/core/23-testing.md) |
| 12 | [Generic Views](topics/core/12-generic-views.md) | 24 | [Performance & Security](topics/core/24-performance-and-security.md) |

## Advanced Topics

Production concerns, deeper DRF, and companion (non-DRF-core) topics.

| # | Topic | # | Topic |
|---|---|---|---|
| 1 | [Signals with DRF](topics/advanced/01-signals-with-drf.md) | 10 | [OpenAPI Schema & API Docs](topics/advanced/10-openapi-schema-and-api-docs.md) 🔀 |
| 2 | [Transactions & Atomic Operations](topics/advanced/02-transactions-and-atomic-operations.md) 🔀 | 11 | [Multi-Tenant APIs](topics/advanced/11-multi-tenant-apis.md) |
| 3 | [Bulk Create & Update APIs](topics/advanced/03-bulk-create-and-update-apis.md) 🔀 | 12 | [API Gateway Concepts](topics/advanced/12-api-gateway-concepts.md) |
| 4 | [Upload Files API](topics/advanced/04-upload-files-api.md) | 13 | [Microservices Integration](topics/advanced/13-microservices-integration.md) |
| 5 | [Download Files API](topics/advanced/05-download-files-api.md) | 14 | [Audit Logging](topics/advanced/14-audit-logging.md) |
| 6 | [Async Views](topics/advanced/06-async-views.md) | 15 | [Application Logging](topics/advanced/15-application-logging.md) 🧩 |
| 7 | [Streaming Responses](topics/advanced/07-streaming-responses.md) | 16 | [API Monitoring](topics/advanced/16-api-monitoring.md) |
| 8 | [Webhooks](topics/advanced/08-webhooks.md) | 17 | [DRF Internals](topics/advanced/17-drf-internals.md) |
| 9 | [OAuth2 / Social Authentication](topics/advanced/09-oauth2-social-authentication.md) 🧩🆕 | | |

**Legend:** 🆕 new from coverage audit · 🔀 merged from former separate topics · 🧩 companion (not stock DRF)

---

## Progress overview

| Track | Topics | Files | Notes |
|---|---|---|---|
| Core | 24 | `topics/core/` | DRF API surface (topics 1–24) |
| Advanced | 17 | `topics/advanced/` | Production + companions |
| **Total** | **41** | — | 4 new · 3 merged · 2 companion |

Start at [Serializer](topics/core/01-serializer.md) and follow the **Next ▶** links straight through both tracks.

---

## Further topics (backlog)

Optional/niche topics flagged by the coverage audit, not yet built out — kept here
so nothing is lost:

- Metadata / OPTIONS handling (`SimpleMetadata`, `determine_metadata()`)
- Returning URLs (`reverse` / `reverse_lazy` / hyperlinking)
- Background & scheduled tasks (Celery / RQ / django-q)
- Deployment & runtime (WSGI vs ASGI, Gunicorn/Uvicorn, static/media, Docker)
- Settings & environment configuration (12-factor, `REST_FRAMEWORK` dict)
- Real-time / WebSockets (Django Channels)
- GraphQL as an alternative (graphene-django / strawberry)
- Internationalization & localization (i18n / l10n)
- Niche serializer field classes (`IPAddressField`, `FilePathField`, `HStoreField`, `ModelField`)
