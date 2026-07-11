# Phase 1 — Foundations: What an API Is & REST Fundamentals

> No code yet. This phase builds the mental model so every later concept has a
> place to hang. Read it top-to-bottom; the endpoint tables at the end are the
> "menu" DRF will later generate for us automatically.

Back to the [Learning Plan ▸ Phase 1](LEARNING_PLAN.md#phase-1-foundations--rest-fundamentals).

---

## 1. What a Web API is 🍽️

Imagine a restaurant. You (the **client**) don't walk into the kitchen and cook.
You tell a **waiter** what you want; the waiter carries your order to the
**kitchen** (the **server**) and brings food back.

A **Web API** is that waiter. Your program says *"give me the list of
organizations"* and the API carries that request to the server and brings back
the answer. You never touch the database directly — you talk to the waiter using
an agreed language.

**REST** is a popular *style* for designing that menu. Its big idea: everything
is a **resource** (a noun) with a **URL** (an address), and you act on it with a
small set of **verbs**.

## 2. HTTP verbs — the action words 🔤

The same address means different things depending on the verb:

| Verb | Plain meaning | Restaurant |
|---|---|---|
| `GET` | Read / fetch (never changes anything) | Read the menu |
| `POST` | Create a new thing | Place a new order |
| `PUT` | Replace an existing thing **entirely** | Re-write the whole order |
| `PATCH` | Change **part** of an existing thing | "Actually, no onions" |
| `DELETE` | Remove a thing | Cancel the order |

REST convention — **the URL is a noun, the verb is the action**. Same URL
`/organizations/5/`, three verbs, three outcomes:

- `GET /organizations/5/` → read org #5
- `PATCH /organizations/5/` → edit part of #5
- `DELETE /organizations/5/` → delete #5

## 3. HTTP status codes — the traffic light 🚦

Every response carries a 3-digit code telling you *what happened*:

| Range | Meaning | Common ones |
|---|---|---|
| **2xx** 🟢 | Success | `200 OK`, `201 Created`, `204 No Content` |
| **4xx** 🟡 | *You* sent something wrong | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` |
| **5xx** 🔴 | The *server* broke | `500 Internal Server Error` |

The classic gotcha: **401 = "I don't know who you are"** (log in) vs
**403 = "I know who you are, but you're not allowed"** (wrong role).

## 4. JSON — the universal shipping label 📦

Client and server may run different languages internally, so they agree on a
neutral written format: **JSON**. Keys and values:

```json
{
  "id": 5,
  "name": "Acme Open Source",
  "slug": "acme-oss",
  "is_active": true,
  "contact_email": "oss@acme.example"
}
```

Rules: `{}` object, `[]` list, strings in `"double quotes"`, `true`/`false`/`null`
lowercase, no trailing commas, no comments. DRF's whole job is turning Django
objects into JSON like this and back.

## 5. Client–server & statelessness 🔁

Every request hits a **fresh counter with an amnesiac cashier** — the server does
**not** remember you between requests. So each request must carry *everything*
needed to serve it, including **who you are** (credentials). That's why later we
don't "stay logged in"; every call re-introduces itself (a token in a header).
Statelessness is what lets any server handle any request, so APIs scale.

---

## The REST menu for our app

This is the design we'll build toward. DRF routers (Phase 8) will generate
almost exactly these URLs for us — predicting them now makes the framework feel
obvious instead of magical.

### Organizations

| Verb | URL | Purpose | Success |
|---|---|---|---|
| GET | `/organizations/` | list all organizations | `200 OK` |
| POST | `/organizations/` | create an organization | `201 Created` |
| GET | `/organizations/{id}/` | get one organization | `200 OK` |
| PATCH | `/organizations/{id}/` | edit part of an org | `200 OK` |
| PUT | `/organizations/{id}/` | replace an org entirely | `200 OK` |
| DELETE | `/organizations/{id}/` | delete an org | `204 No Content` |

### Projects

| Verb | URL | Purpose | Success |
|---|---|---|---|
| GET | `/projects/` | list all projects | `200 OK` |
| POST | `/projects/` | create a project | `201 Created` |
| GET | `/projects/{id}/` | get one project | `200 OK` |
| PATCH | `/projects/{id}/` | edit part of a project | `200 OK` |
| PUT | `/projects/{id}/` | replace a project | `200 OK` |
| DELETE | `/projects/{id}/` | delete a project | `204 No Content` |

### Repositories

| Verb | URL | Purpose | Success |
|---|---|---|---|
| GET | `/repositories/` | list all repositories | `200 OK` |
| POST | `/repositories/` | create a repository | `201 Created` |
| GET | `/repositories/{id}/` | get one repository | `200 OK` |
| PATCH | `/repositories/{id}/` | edit part of a repo | `200 OK` |
| PUT | `/repositories/{id}/` | replace a repo | `200 OK` |
| DELETE | `/repositories/{id}/` | delete a repo | `204 No Content` |

### Two special cases we designed for on purpose

**Nested resources (children of a parent).** Projects belong to an org, so to list
*the projects of org #5* we nest the child under the parent:

```
GET  /organizations/5/projects/     list projects belonging to org #5   -> 200
POST /organizations/5/projects/     create a project under org #5        -> 201
```

The context (`which org`) lives in the URL path. We build this in
[Phase 8](LEARNING_PLAN.md#phase-8-viewsets-routers--custom-actions) with
`drf-nested-routers`.

**Custom actions (verbs that aren't CRUD).** "Sync a mirror now" is not
create/read/update/delete — it's an *action*. REST models it as a sub-resource
verb via `POST` (it changes server state and isn't idempotent):

```
POST /mirrors/12/sync/     trigger a sync of mirror #12    -> 202 Accepted
POST /mirrors/12/retry/    retry a failed mirror sync      -> 202 Accepted
```

`202 Accepted` = "I got your request and started working; it may finish later"
(the real system enqueues a background job). We build these with DRF's `@action`
in [Phase 8](LEARNING_PLAN.md#phase-8-viewsets-routers--custom-actions).

---

## Takeaways

- A resource = a noun with a URL; a verb = the action on it.
- CRUD maps to POST / GET / PUT+PATCH / DELETE.
- Status codes are a contract: 2xx worked, 4xx caller's fault, 5xx server's fault.
- JSON is the neutral wire format; serializers (Phase 3) produce and parse it.
- APIs are stateless: every request re-proves who it is.

**Next:** [Phase 2 — Django ORM refresher & project setup](phase2_setup_and_models.md)
(you'll type the real `pip install` / `startproject` commands; the tutor explains each).
