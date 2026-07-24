# 22. Exception Handling

**Track:** Core · **Topic 22 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-20-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Common Exceptions](#common-exceptions)
- [Custom Exceptions](#custom-exceptions)
- [Global Exception Handling](#global-exception-handling)
- [Status Codes](#status-codes)

## Common Exceptions

<details>
<summary>Show 10 items</summary>

- [ ] `ValidationError`
- [ ] `AuthenticationFailed`
- [ ] `NotAuthenticated`
- [ ] `PermissionDenied`
- [ ] `NotFound`
- [ ] 🆕 `ParseError` (400)
- [ ] 🆕 `MethodNotAllowed` (405)
- [ ] 🆕 `NotAcceptable` (406)
- [ ] 🆕 `UnsupportedMediaType` (415)
- [ ] 🆕 `Throttled` (429)
</details>

## Custom Exceptions

<details>
<summary>Show 6 items</summary>

- [ ] `APIException`
- [ ] custom exception classes
- [ ] 🆕 `status_code` / `default_detail` / `default_code`; passing `detail`/`code` when raising
- [ ] 🆕 `ValidationError` detail shapes (single/list/dict) + `NON_FIELD_ERRORS_KEY`
- [ ] 🆕 `serializer.is_valid(raise_exception=True)` → auto 400
- [ ] 🆕 `get_full_details()` / `get_codes()` for machine-readable codes
</details>

## Global Exception Handling

<details>
<summary>Show 6 items</summary>

- [ ] `custom_exception_handler()`
- [ ] error format design (standardization)
- [ ] 🆕 the `(exc, context)` signature + `context` dict (view, request, args, kwargs)
- [ ] 🆕 default handler only converts `APIException`, Django `Http404`, Django `PermissionDenied` — **anything else becomes a 500**
- [ ] 🆕 returning `None` falls back to the default 500
- [ ] 🆕 wiring via `REST_FRAMEWORK['EXCEPTION_HANDLER']`; logging/Sentry capture of unhandled exceptions

</details>

## Status Codes
- [ ] 🆕 `rest_framework.status` constants (`HTTP_200_OK`, `HTTP_201_CREATED`, `HTTP_400_BAD_REQUEST`, `HTTP_404_NOT_FOUND`, `HTTP_429_TOO_MANY_REQUESTS`, …)
- [ ] 🆕 predicates: `is_informational` / `is_success` / `is_redirect` / `is_client_error` / `is_server_error`

---
◀ [Prev: Versioning](21-versioning.md) · [↑ Back to top](#22-exception-handling) · [Next: Testing ▶](23-testing.md) · [⌂ Home](../../README.md)
