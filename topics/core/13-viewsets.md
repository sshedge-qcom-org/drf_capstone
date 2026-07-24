# 13. ViewSets

**Track:** Core · **Topic 13 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-13-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Types](#types)
- [Actions](#actions)
- [Customizations](#customizations)
- [Action mechanics](#action-mechanics)

## Types

<details>
<summary>Show 4 items</summary>

- [ ] `ViewSet`
- [ ] `GenericViewSet`
- [ ] `ModelViewSet`
- [ ] `ReadOnlyModelViewSet`
</details>

## Actions

<details>
<summary>Show 6 items</summary>

- [ ] `list()`
- [ ] `create()`
- [ ] `retrieve()`
- [ ] `update()`
- [ ] `partial_update()`
- [ ] `destroy()`
</details>

## Customizations
- [ ] custom actions
- [ ] custom serializers
- [ ] custom permissions

## Action mechanics

<details>
<summary>Show 4 items · 🆕 added by coverage audit</summary>

- [ ] `@action` decorator: `detail=True` vs `detail=False`, `methods=[...]`, `url_path`, `url_name`
- [ ] per-action `serializer_class` / `permission_classes`
- [ ] `self.action` (branch inside `get_serializer_class` / `get_permissions` / `get_queryset`)
- [ ] mapping without a router: `.as_view({'get': 'list', 'post': 'create'})`
</details>

---
◀ [Prev: Generic Views](12-generic-views.md) · [↑ Back to top](#13-viewsets) · [Next: Routers ▶](14-routers.md) · [⌂ Home](../../README.md)
