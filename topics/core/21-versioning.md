# 21. Versioning

**Track:** Core · **Topic 21 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-11-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Why Version APIs](#why-version-apis)
- [Techniques](#techniques)
- [Configuration & Usage](#configuration--usage)
- [Best Practices](#best-practices)

## Why Version APIs
- [ ] the case for versioning

## Techniques

<details>
<summary>Show 5 items</summary>

- [ ] `URLPathVersioning`
- [ ] `NamespaceVersioning`
- [ ] `QueryParameterVersioning`
- [ ] `HeaderVersioning` — this is DRF's `AcceptHeaderVersioning` (vendor media-type versioning) under an informal name
- [ ] `HostNameVersioning`
</details>

## Configuration & Usage

<details>
<summary>Show 3 items · 🆕 added by coverage audit</summary>

- [ ] global config: `DEFAULT_VERSIONING_CLASS`, `DEFAULT_VERSION`, `ALLOWED_VERSIONS`, `VERSION_PARAM`
- [ ] `request.version` — branch behavior per version in views/serializers
- [ ] version-aware URL building: `reverse()` / `HyperlinkedModelSerializer` under `NamespaceVersioning` / `URLPathVersioning`
</details>

## Best Practices
- [ ] backward compatibility
- [ ] API migration

---
◀ [Prev: Throttling](20-throttling.md) · [↑ Back to top](#21-versioning) · [Next: Exception Handling ▶](22-exception-handling.md) · [⌂ Home](../../README.md)
