# 20. Throttling

**Track:** Core · **Topic 20 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-12-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Purpose](#purpose)
- [Types](#types)
- [Configuration](#configuration)
- [Custom Throttling](#custom-throttling)

## Purpose
- [ ] API protection
- [ ] Rate limiting

## Types
- [ ] `AnonRateThrottle`
- [ ] `UserRateThrottle`
- [ ] `ScopedRateThrottle`

## Configuration

<details>
<summary>Show 5 items</summary>

- [ ] throttle rates
- [ ] scope definitions
- [ ] 🆕 `DEFAULT_THROTTLE_CLASSES` (global); applying multiple throttles to one view
- [ ] 🆕 throttle state cache backend — counters in Django cache; shared/Redis in production
- [ ] 🆕 429 Too Many Requests + `Retry-After` header
</details>

## Custom Throttling

<details>
<summary>Show 3 items</summary>

- [ ] custom throttle classes
- [ ] 🆕 `SimpleRateThrottle` / `BaseThrottle` base classes (`get_cache_key`, `get_rate`, `allow_request`)
- [ ] 🆕 client identification behind proxies: `get_ident()`, `X-Forwarded-For` vs `REMOTE_ADDR`, `NUM_PROXIES`
</details>

---
◀ [Prev: Pagination](19-pagination.md) · [↑ Back to top](#20-throttling) · [Next: Versioning ▶](21-versioning.md) · [⌂ Home](../../README.md)
