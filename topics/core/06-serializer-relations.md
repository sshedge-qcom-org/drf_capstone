# 6. Serializer Relations

**Track:** Core · **Topic 6 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-13-blue) ![Added](https://img.shields.io/badge/added-coverage_audit-blueviolet)

> [!TIP]
> This whole topic was added by the coverage audit — the biggest gap found. It covers the relational **field classes** (how a related object is *represented*), distinct from the relationship concepts and nested writes in [Nested Serializers](05-nested-serializers.md).

## Contents
- [Relational field types](#relational-field-types)
- [Writable relations](#writable-relations)
- [Custom & advanced](#custom--advanced)

## Relational field types
- [ ] `PrimaryKeyRelatedField` (default for FK/M2M)
- [ ] `StringRelatedField` (uses the model's `__str__`)
- [ ] `SlugRelatedField`
- [ ] `HyperlinkedRelatedField`
- [ ] `HyperlinkedIdentityField`

## Writable relations

<details>
<summary>Show 4 items</summary>

- [ ] `queryset=` argument (required for writable relations)
- [ ] `many=True` → `ManyRelatedField`
- [ ] `source=` and reverse relations via `related_name`
- [ ] `pk_field`, `html_cutoff`
</details>

## Custom & advanced

<details>
<summary>Show 2 items</summary>

- [ ] Custom `RelatedField` (`to_representation()` / `to_internal_value()`)
- [ ] Generic relations (`GenericRelatedField` pattern)
</details>

---
◀ [Prev: Nested Serializers](05-nested-serializers.md) · [↑ Back to top](#6-serializer-relations) · [Next: Function-Based Views ▶](07-function-based-views.md) · [⌂ Home](../../README.md)
