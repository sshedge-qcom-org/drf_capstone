# A4. Upload Files API

**Track:** Advanced · **Topic 4 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-6-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. The parser side pairs with [Renderers, Parsers & Content Negotiation](../core/09-renderers-parsers-content-negotiation.md); the field basics are in [Serializer](../core/01-serializer.md).

## Contents
- [Receiving uploads](#receiving-uploads)
- [Storage](#storage)

## Receiving uploads
- [ ] parsers: `MultiPartParser`, `FormParser`, `FileUploadParser`
- [ ] `FileField` / `ImageField` validation (size, content-type, extension)

## Storage

<details>
<summary>Show 4 items</summary>

- [ ] default `FileSystemStorage` vs django-storages (S3/GCS/Azure)
- [ ] direct-to-cloud uploads via presigned URLs
- [ ] chunked / resumable uploads for large files
- [ ] `MEDIA_ROOT` / `MEDIA_URL` and serving uploaded media in prod
</details>

---
◀ [Prev: Bulk Create & Update APIs](03-bulk-create-and-update-apis.md) · [↑ Back to top](#a4-upload-files-api) · [Next: Download Files API ▶](05-download-files-api.md) · [⌂ Home](../../README.md)
