# 8. APIView

**Track:** Core · **Topic 8 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-23-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Basics](#basics)
- [The Request object](#the-request-object)
- [The Response object](#the-response-object)
- [HTTP method handlers](#http-method-handlers)
- [Features](#features)
- [Customizations](#customizations)

## Basics
- [ ] APIView architecture
- [ ] Request object
- [ ] Response object

## The Request object

<details>
<summary>Show 6 items · 🆕 added by coverage audit</summary>

- [ ] `request.data` (parsed body — replaces `request.POST`)
- [ ] `request.query_params` (vs Django `request.GET`)
- [ ] `request.user`
- [ ] `request.auth`
- [ ] `request.method`, `request.content_type`
- [ ] `request.stream`, `request.FILES`
</details>

## The Response object

<details>
<summary>Show 3 items · 🆕 added by coverage audit</summary>

- [ ] `Response(data, status=, headers=, content_type=, template_name=)`
- [ ] `.data`, `.status_code`, `.content`, `.rendered_content`
- [ ] why it differs from Django `HttpResponse`
</details>

## HTTP method handlers
- [ ] `get()`
- [ ] `post()`
- [ ] `put()`
- [ ] `patch()`
- [ ] `delete()`

## Features

<details>
<summary>Show 6 items</summary>

- [ ] `authentication_classes`
- [ ] `permission_classes`
- [ ] `throttle_classes`
- [ ] 🆕 `renderer_classes` / `parser_classes`
- [ ] 🆕 `content_negotiation_class`, `metadata_class`, `versioning_class`
- [ ] 🆕 `http_method_names` and the auto-provided `options()` handler
</details>

## Customizations

<details>
<summary>Show 3 items</summary>

- [ ] overriding methods
- [ ] custom responses
- [ ] 🆕 dispatch lifecycle (`initial()`, `check_permissions()`, `handle_exception()`, `finalize_response()`) — see [DRF Internals](../advanced/17-drf-internals.md)
</details>

---
◀ [Prev: Function-Based Views](07-function-based-views.md) · [↑ Back to top](#8-apiview) · [Next: Renderers, Parsers & Content Negotiation ▶](09-renderers-parsers-content-negotiation.md) · [⌂ Home](../../README.md)
