# 10. GenericAPIView

**Track:** Core · **Topic 10 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-14-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Key Attributes](#key-attributes)
- [Useful Methods](#useful-methods)
- [Advanced](#advanced)

## Key Attributes

<details>
<summary>Show 6 items</summary>

- [ ] `queryset`
- [ ] `serializer_class`
- [ ] `lookup_field`
- [ ] 🆕 `lookup_url_kwarg` (when the URL kwarg name differs from `lookup_field`)
- [ ] `pagination_class`
- [ ] 🆕 `filter_backends` (the bridge to the [Filtering](18-filtering.md) topic)
</details>

## Useful Methods

<details>
<summary>Show 7 items</summary>

- [ ] `get_queryset()`
- [ ] `get_serializer()`
- [ ] `get_serializer_class()`
- [ ] `get_object()`
- [ ] 🆕 `get_serializer_context()` (pass `request`/`view`/`format` to serializers)
- [ ] 🆕 `filter_queryset()`
- [ ] 🆕 `paginate_queryset()` / `get_paginated_response()`
</details>

## Advanced
- [ ] dynamic serializer selection
- [ ] dynamic queryset filtering

---
◀ [Prev: Renderers, Parsers & Content Negotiation](09-renderers-parsers-content-negotiation.md) · [↑ Back to top](#10-genericapiview) · [Next: Mixins ▶](11-mixins.md) · [⌂ Home](../../README.md)
