# A17. DRF Internals

**Track:** Advanced · **Topic 17 / 17** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-advanced-orange) ![Items](https://img.shields.io/badge/items-7-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. This is the final topic — read the source alongside these checkpoints.

## Contents
- [Request lifecycle](#request-lifecycle)
- [Composition & pipelines](#composition--pipelines)

## Request lifecycle
- [ ] `APIView.dispatch()` flow: `initialize_request()` / `initial()` / `finalize_response()`
- [ ] `Request` wrapper vs Django `HttpRequest`
- [ ] authentication / permission / throttle evaluation order
- [ ] exception handling pipeline (`exception_handler`)

## Composition & pipelines
- [ ] content negotiation + renderer/parser selection pipeline
- [ ] how mixins + `GenericAPIView` compose the generic views
- [ ] how ViewSet actions map to router URLs (`as_view` mapping)

---
◀ [Prev: API Monitoring](16-api-monitoring.md) · [↑ Back to top](#a17-drf-internals) · _(end)_ · [⌂ Home](../../README.md)
