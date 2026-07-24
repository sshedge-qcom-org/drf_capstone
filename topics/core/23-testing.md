# 23. Testing

**Track:** Core · **Topic 23 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-19-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Testing Tools](#testing-tools)
- [CRUD Testing](#crud-testing)
- [Authentication Testing](#authentication-testing)
- [Advanced](#advanced)

## Testing Tools

<details>
<summary>Show 5 items</summary>

- [ ] `APITestCase`
- [ ] `APIClient`
- [ ] `APIRequestFactory`
- [ ] 🆕 `APISimpleTestCase`, `APITransactionTestCase`, `APILiveServerTestCase`, `URLPatternsTestCase`
- [ ] 🆕 `RequestsClient` (note: `CoreAPIClient` is deprecated)
</details>

## CRUD Testing

<details>
<summary>Show 7 items</summary>

- [ ] GET testing
- [ ] POST testing
- [ ] PUT testing
- [ ] PATCH testing
- [ ] DELETE testing
- [ ] 🆕 request `format='json'` vs multipart — the **multipart-default footgun** (breaks nested/JSON payloads)
- [ ] 🆕 asserting on `response.data` / `response.status_code` (with `status` constants) / `response.json()`
</details>

## Authentication Testing

<details>
<summary>Show 5 items</summary>

- [ ] `force_authenticate()`
- [ ] JWT testing
- [ ] 🆕 `APIClient.credentials()` — set auth headers / token
- [ ] 🆕 `APIClient.login()` / `logout()` — session auth
- [ ] 🆕 `enforce_csrf_checks` for CSRF testing
</details>

## Advanced

<details>
<summary>Show 5 items</summary>

- [ ] mocking
- [ ] fixtures
- [ ] coverage reports
- [ ] 🆕 `assertNumQueries` to catch N+1 regressions
- [ ] 🆕 `TEST_REQUEST_DEFAULT_FORMAT` / `TEST_REQUEST_RENDERER_CLASSES` settings
</details>

---
◀ [Prev: Exception Handling](22-exception-handling.md) · [↑ Back to top](#23-testing) · [Next: Performance & Security ▶](24-performance-and-security.md) · [⌂ Home](../../README.md)
