# 18. Filtering

**Track:** Core · **Topic 18 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-13-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Filtering Methods](#filtering-methods)
- [DRF Filters](#drf-filters)
- [Configuration & Wiring](#configuration--wiring)
- [Advanced](#advanced)

## Filtering Methods
- [ ] Query Parameters
- [ ] Manual Filtering
- [ ] 🆕 Filtering against `request.user` — ownership/tenant scoping via `get_queryset()` (the most common production pattern)

## DRF Filters

<details>
<summary>Show 6 items</summary>

- [ ] `DjangoFilterBackend`
- [ ] `SearchFilter`
- [ ] `OrderingFilter`
- [ ] 🆕 `SearchFilter`: `search_fields` prefixes (`^` startswith, `=` exact, `@` full-text, `$` regex), `search_param`
- [ ] 🆕 `OrderingFilter`: `ordering_fields` (and `'__all__'`), default ordering, `ordering_param`
- [ ] 🆕 `DjangoFilterBackend` setup: install django-filter, `filterset_fields` vs `filterset_class`, lookups (`gte`/`lte`/`contains`/`in`)
</details>

## Configuration & Wiring
- [ ] 🆕 `DEFAULT_FILTER_BACKENDS` (global) vs per-view `filter_backends`

## Advanced
- [ ] multiple filters
- [ ] custom filter classes
- [ ] filter sets

---
◀ [Prev: Permissions](17-permissions.md) · [↑ Back to top](#18-filtering) · [Next: Pagination ▶](19-pagination.md) · [⌂ Home](../../README.md)
