# 16. Authentication

**Track:** Core · **Topic 16 / 24** · [⌂ Guide Home](../../README.md)

![Track](https://img.shields.io/badge/track-core-success) ![Items](https://img.shields.io/badge/items-22-blue)

> [!TIP]
> Check off each `- [ ]` as you learn it. Items marked 🆕 were added by the coverage audit. Third-party OAuth2/social login lives in [OAuth2 / Social Authentication](../advanced/09-oauth2-social-authentication.md).

## Contents
- [Authentication Flow](#authentication-flow)
- [Types](#types)
- [Token Authentication setup](#token-authentication-setup)
- [JWT Topics](#jwt-topics)
- [Custom Authentication](#custom-authentication)

## Authentication Flow
- [ ] Request Authentication
- [ ] User Identification
- [ ] 🆕 `request.user` vs `request.auth` (what each authenticator populates)
- [ ] 🆕 `DEFAULT_AUTHENTICATION_CLASSES` (global vs per-view)
- [ ] 🆕 401 Unauthorized vs 403 Forbidden and the `WWW-Authenticate` header

## Types

<details>
<summary>Show 5 items</summary>

- [ ] `SessionAuthentication`
- [ ] `BasicAuthentication`
- [ ] `TokenAuthentication`
- [ ] JWT Authentication
- [ ] 🆕 `RemoteUserAuthentication` (SSO / `REMOTE_USER`)
</details>

## Token Authentication setup

<details>
<summary>Show 3 items · 🆕 added by coverage audit</summary>

- [ ] `'rest_framework.authtoken'` in `INSTALLED_APPS` + migrations + the `Token` model
- [ ] Obtaining tokens: `obtain_auth_token` view / `ObtainAuthToken`
- [ ] auto-create tokens via a `post_save` signal
</details>

## JWT Topics

<details>
<summary>Show 6 items</summary>

- [ ] Access Token
- [ ] Refresh Token
- [ ] Token Blacklisting
- [ ] Token Expiration
- [ ] 🆕 `TokenObtainPairView` / `TokenRefreshView` / `TokenVerifyView`
- [ ] 🆕 `SIMPLE_JWT` settings, custom token claims
</details>

## Custom Authentication
- [ ] custom authentication classes

---
◀ [Prev: Format Suffixes & Browsable API](15-format-suffixes-browsable-api.md) · [↑ Back to top](#16-authentication) · [Next: Permissions ▶](17-permissions.md) · [⌂ Home](../../README.md)
