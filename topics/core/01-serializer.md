# 1. Serializer

**Track:** Core · **Topic 1 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-46-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it — GitHub renders the progress live. Items marked 🆕 were added by the coverage audit against the official DRF API guide.

## Contents
- [Core Concepts](#core-concepts)
- [Fields](#fields)
- [Methods](#methods)
- [Advanced](#advanced)

## Core Concepts
- [ ] What is Serialization?
- [ ] What is Deserialization?
- [ ] Serializer lifecycle
- [ ] Data transformation
- [ ] 🆕 The `context` dict / `self.context` — access `request`, `view`, current user; build absolute URLs

## Fields

<details>
<summary>Show 23 items</summary>

- [ ] CharField
- [ ] IntegerField
- [ ] FloatField
- [ ] 🆕 DecimalField (`max_digits`, `decimal_places`, `coerce_to_string`) — money/precision
- [ ] BooleanField
- [ ] DateField
- [ ] DateTimeField
- [ ] 🆕 TimeField
- [ ] 🆕 DurationField
- [ ] EmailField
- [ ] URLField
- [ ] 🆕 SlugField
- [ ] 🆕 UUIDField (`format='hex_verbose'/'hex'/'int'/'urn'`)
- [ ] ChoiceField
- [ ] 🆕 MultipleChoiceField
- [ ] ListField
- [ ] DictField
- [ ] 🆕 JSONField
- [ ] FileField
- [ ] ImageField
- [ ] 🆕 RegexField (a distinct **field**, not the `RegexValidator`)
- [ ] 🆕 ReadOnlyField (the field **class**, not the `read_only=True` argument)
- [ ] 🆕 HiddenField (+ `CurrentUserDefault` / `CreateOnlyDefault`) — stamp `request.user`
</details>

## Methods

<details>
<summary>Show 5 items</summary>

- [ ] `is_valid()`
- [ ] `validated_data`
- [ ] `errors`
- [ ] `save()`
- [ ] `data`
</details>

## Advanced

<details>
<summary>Show 13 items</summary>

- [ ] partial updates
- [ ] `read_only` fields
- [ ] `write_only` fields
- [ ] `required` fields
- [ ] default values
- [ ] 🆕 `source=` — attribute remap, dotted paths (`source='user.email'`), `source='*'`
- [ ] 🆕 `allow_null` (distinct from `allow_blank`)
- [ ] 🆕 `allow_blank`, `max_length` / `min_length` / `trim_whitespace` (CharField)
- [ ] 🆕 `label` / `help_text` (drive the browsable API + OpenAPI schema)
- [ ] 🆕 `to_representation()` — custom output shape
- [ ] 🆕 `to_internal_value()` — custom input parsing/coercion
- [ ] 🆕 `many=True` and the `ListSerializer` it produces (`Meta.list_serializer_class`)
- [ ] 🆕 `BaseSerializer` — fully custom read/write
</details>

---
◀ _(start)_ · [↑ Back to top](#1-serializer) · [Next: ModelSerializer ▶](02-modelserializer.md) · [⌂ Home](../../README.md)
