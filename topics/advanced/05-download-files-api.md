# A5. Download Files API

**Track:** Advanced · **Topic 5 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-6-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Overlaps with [Streaming Responses](07-streaming-responses.md).

## Contents
- [Response classes](#response-classes)
- [Production patterns](#production-patterns)

## Response classes
- [ ] `FileResponse` for downloads
- [ ] `StreamingHttpResponse` for large / generated files
- [ ] `Content-Disposition` (inline vs attachment) and content-type

## Production patterns

<details>
<summary>Show 3 items</summary>

- [ ] X-Sendfile / X-Accel-Redirect offloading to nginx/apache
- [ ] presigned URL redirects for cloud-stored files
- [ ] range requests / partial content
</details>

---
◀ [Prev: Upload Files API](04-upload-files-api.md) · [↑ Back to top](#a5-download-files-api) · [Next: Async Views ▶](06-async-views.md) · [⌂ Home](../../README.md)
