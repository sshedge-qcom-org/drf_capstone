# A11. Multi-Tenant APIs

**Track:** Advanced · **Topic 11 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-5-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Connects to [Permissions](../core/17-permissions.md) (IDOR) and [Filtering](../core/18-filtering.md) (queryset scoping).

## Contents
- [Isolation strategy](#isolation-strategy)
- [Scoping & safety](#scoping--safety)

## Isolation strategy
- [ ] shared schema (tenant FK) vs schema-per-tenant (django-tenants) vs database-per-tenant
- [ ] tenant resolution: subdomain, custom header, or JWT claim + middleware

## Scoping & safety
- [ ] row-level queryset scoping (per-tenant `get_queryset`)
- [ ] preventing cross-tenant IDOR
- [ ] per-tenant settings / throttling / rate limits

---
◀ [Prev: OpenAPI Schema & API Docs](10-openapi-schema-and-api-docs.md) · [↑ Back to top](#a11-multi-tenant-apis) · [Next: API Gateway Concepts ▶](12-api-gateway-concepts.md) · [⌂ Home](../../README.md)
