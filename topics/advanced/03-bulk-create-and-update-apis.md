# A3. Bulk Create & Update APIs

**Track:** Advanced · **Topic 3 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-7-blue) ![Merged](https://img.shields.io/badge/merged-2_topics-yellow)

> [!NOTE]
> **Merged topic:** the original "Bulk Create APIs" and "Bulk Update APIs" share one mechanism, combined here per the coverage audit.

## Contents
- [Mechanism](#mechanism)
- [Gotchas & performance](#gotchas--performance)

## Mechanism
- [ ] `ListSerializer` and `many=True`
- [ ] default `create()` supports bulk; `update()` must be implemented manually on `ListSerializer`
- [ ] overriding `ListSerializer.create()` / `update()`
- [ ] QuerySet `bulk_create()` / `bulk_update()`

## Gotchas & performance

<details>
<summary>Show 3 items</summary>

- [ ] per-item error validation/reporting in bulk payloads; partial bulk updates
- [ ] third-party helpers (`djangorestframework-bulk`) and caveats
- [ ] performance vs N inserts; transaction wrapping (see [Transactions](02-transactions-and-atomic-operations.md))
</details>

---
◀ [Prev: Transactions & Atomic Operations](02-transactions-and-atomic-operations.md) · [↑ Back to top](#a3-bulk-create--update-apis) · [Next: Upload Files API ▶](04-upload-files-api.md) · [⌂ Home](../../README.md)
