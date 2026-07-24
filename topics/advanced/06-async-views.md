# A6. Async Views

**Track:** Advanced · **Topic 6 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-5-blue)

> [!IMPORTANT]
> The key clarification: **stock DRF views are synchronous.** `APIView`/`ViewSet` are sync; for true async you need `adrf`. Don't be misled about DRF's async story.

## Contents
- [Async basics](#async-basics)
- [The DRF caveat](#the-drf-caveat)

## Async basics
- [ ] `async def` views and the ASGI requirement
- [ ] async ORM queries and `sync_to_async` / `async_to_sync` bridging
- [ ] when async helps (I/O-bound external calls) vs when it does not

## The DRF caveat
- [ ] DRF core is largely synchronous — document the limitation
- [ ] `adrf` package (async `APIView` / `ViewSet` / serializers)

---
◀ [Prev: Download Files API](05-download-files-api.md) · [↑ Back to top](#a6-async-views) · [Next: Streaming Responses ▶](07-streaming-responses.md) · [⌂ Home](../../README.md)
