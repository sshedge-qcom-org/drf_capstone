# 19. Pagination

**Track:** Core · **Topic 19 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-9-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Pagination Types](#pagination-types)
- [Configuration](#configuration)
- [Custom Pagination](#custom-pagination)

## Pagination Types
- [ ] `PageNumberPagination`
- [ ] `LimitOffsetPagination`
- [ ] `CursorPagination`
- [ ] 🆕 `CursorPagination` trade-offs: mandatory ordering field, opaque cursor, stable over large/changing datasets

## Configuration

<details>
<summary>Show 4 items</summary>

- [ ] page size
- [ ] custom page size
- [ ] 🆕 `DEFAULT_PAGINATION_CLASS` — pagination stays **off** until set (`PAGE_SIZE` alone is not enough)
- [ ] 🆕 applies only to `GenericAPIView`/ViewSets, not plain `APIView` (manual `paginate_queryset()` otherwise)
</details>

## Custom Pagination
- [ ] creating pagination classes
- [ ] custom response formats

---
◀ [Prev: Filtering](18-filtering.md) · [↑ Back to top](#19-pagination) · [Next: Throttling ▶](20-throttling.md) · [⌂ Home](../../README.md)
