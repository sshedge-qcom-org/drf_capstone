# 9. Renderers, Parsers & Content Negotiation

**Track:** Core · **Topic 9 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-16-blue) ![Added](https://img.shields.io/badge/added-coverage_audit-blueviolet)

> [!TIP]
> Added by the coverage audit — the request/response pipeline that turns `request.data` into Python and `Response` data into bytes. Renderers = output; Parsers = input; Content Negotiation = choosing between them.

## Contents
- [Renderers (output)](#renderers-output)
- [Parsers (input)](#parsers-input)
- [Content Negotiation](#content-negotiation)

## Renderers (output)
- [ ] `JSONRenderer` (default)
- [ ] `BrowsableAPIRenderer` (the hallmark DRF web UI)
- [ ] `TemplateHTMLRenderer` / `StaticHTMLRenderer` / `AdminRenderer`
- [ ] custom renderers (CSV / XML)
- [ ] `DEFAULT_RENDERER_CLASSES` setting
- [ ] `request.accepted_renderer` / `request.accepted_media_type`

## Parsers (input)

> Parsers populate `request.data`.

<details>
<summary>Show 6 items</summary>

- [ ] `JSONParser` (default)
- [ ] `FormParser`
- [ ] `MultiPartParser` (file uploads)
- [ ] `FileUploadParser`
- [ ] `DEFAULT_PARSER_CLASSES` setting
- [ ] custom parsers
</details>

## Content Negotiation

<details>
<summary>Show 4 items</summary>

- [ ] `DefaultContentNegotiation`
- [ ] `Accept` header + `?format=` selection
- [ ] `perform_content_negotiation()`
- [ ] `content_negotiation_class`
</details>

---
◀ [Prev: APIView](08-apiview.md) · [↑ Back to top](#9-renderers-parsers--content-negotiation) · [Next: GenericAPIView ▶](10-genericapiview.md) · [⌂ Home](../../README.md)
