# A2. Transactions & Atomic Operations

**Track:** Advanced · **Topic 2 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-8-blue) ![Merged](https://img.shields.io/badge/merged-2_topics-yellow)

> [!NOTE]
> **Merged topic:** the original "Transactions" and "Atomic Operations" are the same Django/DRF subject, combined here per the coverage audit.

## Contents
- [Atomicity](#atomicity)
- [In DRF views](#in-drf-views)

## Atomicity
- [ ] `transaction.atomic` as decorator **and** context manager
- [ ] `ATOMIC_REQUESTS` setting
- [ ] savepoints and nested `atomic` blocks
- [ ] `select_for_update()` row locking
- [ ] `transaction.on_commit()` (fire Celery task / webhook only after commit)
- [ ] `non_atomic_requests` / disabling per-view

## In DRF views
- [ ] wrapping `perform_create` / `perform_update` / `create` / `update`
- [ ] rollback on serializer / DB errors

---
◀ [Prev: Signals with DRF](01-signals-with-drf.md) · [↑ Back to top](#a2-transactions--atomic-operations) · [Next: Bulk Create & Update APIs ▶](03-bulk-create-and-update-apis.md) · [⌂ Home](../../README.md)
