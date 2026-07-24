# A1. Signals with DRF

**Track:** Advanced · **Topic 1 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-6-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items were expanded from the original bare topic by the coverage audit.

## Contents
- [Signals & wiring](#signals--wiring)
- [When to use](#when-to-use)

## Signals & wiring
- [ ] `pre_save` / `post_save`, `pre_delete` / `post_delete`, `m2m_changed`
- [ ] `@receiver` decorator; connecting in `apps.py` `ready()`
- [ ] `dispatch_uid` to prevent duplicate connections

## When to use

<details>
<summary>Show 3 items</summary>

- [ ] signals vs overriding `serializer.create()` / `perform_create()` — when to use which
- [ ] pitfalls: hidden side effects, hard to test, ordering, transaction timing (use `transaction.on_commit`)
- [ ] testing signals
</details>

---
◀ [Prev: Performance & Security](../core/24-performance-and-security.md) · [↑ Back to top](#a1-signals-with-drf) · [Next: Transactions & Atomic Operations ▶](02-transactions-and-atomic-operations.md) · [⌂ Home](../../README.md)
