# 24. Performance & Security

**Track:** Core · **Topic 24 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-34-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit. This is the last core topic — the [Advanced track](../advanced/01-signals-with-drf.md) continues from here.

## Contents
- [Performance](#performance)
- [Security](#security)

## Performance

<details>
<summary><strong>Query Optimization</strong></summary>

- [ ] `select_related()`
- [ ] `prefetch_related()`
- [ ] 🆕 `.only()` / `.defer()` to trim column loading
- [ ] 🆕 `Prefetch` objects with custom querysets and `to_attr`
- [ ] 🆕 profiling / N+1 tooling: Django Debug Toolbar, django-silk, `assertNumQueries`
</details>

<details>
<summary><strong>Database Optimization</strong></summary>

- [ ] indexing
- [ ] query reduction
- [ ] 🆕 pagination as a mandatory safeguard against unbounded querysets
</details>

<details>
<summary><strong>Caching</strong></summary>

- [ ] per-view caching
- [ ] low-level caching
- [ ] Redis caching
- [ ] 🆕 mechanism: `cache_page` / `vary_on_headers` / `vary_on_cookie` via `@method_decorator` on CBVs
- [ ] 🆕 HTTP conditional requests: ETag / Last-Modified → 304 Not Modified (`@condition`, `If-None-Match`/`If-Modified-Since`)
</details>

<details>
<summary><strong>Serializer Optimization</strong></summary>

- [ ] limiting fields
- [ ] avoiding heavy nested serializers
</details>

## Security

<details>
<summary><strong>Authentication Security</strong></summary>

- [ ] JWT security
- [ ] token rotation
</details>

<details>
<summary><strong>API Security</strong></summary>

- [ ] HTTPS
- [ ] CSRF protection
- [ ] CORS
- [ ] 🆕 CSRF gotcha: `SessionAuthentication` enforces CSRF; Token/JWT do not
- [ ] 🆕 django-cors-headers: `CORS_ALLOWED_ORIGINS`, `CORS_ALLOW_CREDENTIALS`; CORS-vs-CSRF distinction
- [ ] 🆕 production hardening: `DEBUG=False`, `ALLOWED_HOSTS`, `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`
- [ ] 🆕 `python manage.py check --deploy`
- [ ] 🆕 secrets management: `SECRET_KEY` / DB creds via env vars (django-environ), never in code
</details>

<details>
<summary><strong>Data Security</strong></summary>

- [ ] sensitive fields masking
- [ ] encryption
- [ ] 🆕 mass assignment / over-posting protection via explicit `fields` + `read_only_fields`
</details>

<details>
<summary><strong>Rate Protection</strong></summary>

- [ ] throttling
- [ ] request limits
</details>

<details>
<summary><strong>Common Vulnerabilities</strong></summary>

- [ ] SQL Injection
- [ ] XSS
- [ ] CSRF
- [ ] Broken Authentication
- [ ] Insecure Direct Object Reference (IDOR)
- [ ] 🆕 OWASP API Security Top 10 framing (BOLA/IDOR, excessive data exposure, mass assignment, security misconfiguration)
- [ ] 🆕 dependency vulnerability scanning (pip-audit / safety / Dependabot)
</details>

---
◀ [Prev: Testing](23-testing.md) · [↑ Back to top](#24-performance--security) · [Next: Signals with DRF ▶](../advanced/01-signals-with-drf.md) · [⌂ Home](../../README.md)
