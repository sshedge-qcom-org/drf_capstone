# 17. Permissions

**Track:** Core · **Topic 17 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-13-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit.

## Contents
- [Built-in Permissions](#built-in-permissions)
- [Object-Level Permissions](#object-level-permissions)
- [Custom Permissions](#custom-permissions)

## Built-in Permissions

<details>
<summary>Show 8 items</summary>

- [ ] `AllowAny`
- [ ] `IsAuthenticated`
- [ ] `IsAdminUser`
- [ ] `IsAuthenticatedOrReadOnly`
- [ ] 🆕 `DjangoModelPermissions` (maps view access to model add/change/delete perms; requires a `queryset`)
- [ ] 🆕 `DjangoModelPermissionsOrAnonReadOnly`
- [ ] 🆕 `DjangoObjectPermissions` (object-level, via django-guardian)
- [ ] 🆕 `DEFAULT_PERMISSION_CLASSES` (secure-by-default; the #1 production security default)
</details>

## Object-Level Permissions
- [ ] `has_permission()`
- [ ] `has_object_permission()`
- [ ] 🆕 **Gotcha:** `has_object_permission` runs only when `get_object()` is called — NOT on list endpoints. Filter `get_queryset()` separately (ties to IDOR in [Performance & Security](24-performance-and-security.md)).

## Custom Permissions
- [ ] role-based permissions
- [ ] ownership permissions
- [ ] 🆕 composing with `&` (AND), `|` (OR), `~` (NOT) — DRF 3.9+
- [ ] 🆕 `message` / `code` attributes on custom permission classes

---
◀ [Prev: Authentication](16-authentication.md) · [↑ Back to top](#17-permissions) · [Next: Filtering ▶](18-filtering.md) · [⌂ Home](../../README.md)
