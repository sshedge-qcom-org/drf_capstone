# DRF Learning Plan

A step-by-step, concept-by-concept curriculum for learning **Django REST
Framework** from the ground up — explained in layman's terms.

We learn by **building one real app**: a genericized clone of an open-source
program-office system (organizations that own projects, projects that hold git
repositories, repositories that get mirrored elsewhere, and role-based access
grants tying users to projects). Two birds, one stone — you learn DRF *and* how
this class of platform is structured.

> **How we work each lesson:**
> 1. **Tutor explains** the concept in plain English + a tiny snippet, and *why* it exists.
> 2. **Tutor hands over copy-paste-ready code in chat; you paste it into the files yourself** (typing it is how you learn). The tutor never edits your `.py` files directly.
> 3. **Tutor reviews** what you pasted/ran — points out bugs, what you missed, and why.
>
> **Docs are the tutor's job:** this plan and the per-phase `docs/phaseN_*.md`
> walkthroughs are written and kept updated by the tutor, so you can retrace
> every step later. **Code is yours.**
>
> **Per phase:** run the server, test the new endpoint, then commit & push to
> GitHub before moving on. Check off each `[ ]` as we complete it. This file is
> the master tracker.

---

## Tech stack (2026-current)

| Package | Version | Purpose | First used |
|---|---|---|---|
| Django | 5.2 LTS | Framework, ORM, admin | Phase 2 |
| djangorestframework | 3.16.x | Core DRF | Phase 3 |
| djangorestframework-simplejwt | 5.4+ | JWT auth | Phase 9 |
| django-filter | 25.1+ | Field filtering | Phase 13 |
| drf-nested-routers | latest | Nested routes | Phase 8 |
| drf-spectacular[sidecar] | 0.28+ | OpenAPI 3 + Swagger/ReDoc | Phase 17 |
| Pillow | 11+ | ImageField (org logo) | Phase 14 |
| pytest-django, model-bakery | latest | Testing (optional) | Phase 16 |

**DB:** SQLite (zero setup; the ORM/DRF code is identical to Postgres).

---

## The example domain

Ownership chain: **Organization → Project → Repository → Mirror**, plus
**AccessGrant** (the entitlement "through" model) linking Users to Projects by role.

| Model | Genericizes | Teaches |
|---|---|---|
| **Organization** | external customer account | org-scoping root; Email/URL validation; file upload |
| **Project** | an open-source project | FK, choices, composite uniqueness, M2M-through, archive action |
| **Repository** | a git repo | nested routes, permission inheritance up the FK chain |
| **Mirror** | synced copy elsewhere | status lifecycle → custom actions; write-only secret; nullable fields |
| **AccessGrant** | the entitlement | M2M-through, role/object permissions, org-scoped querysets, revoke |
| **ActivityEvent** | append-only audit feed | cursor pagination |
| **User** | *Django built-in, reused* | auth, `request.user`, second-FK disambiguation |

**Roles:** OWNER (archive/grant) · MAINTAINER (edit repos/mirrors) ·
CONTRIBUTOR (trigger syncs) · VIEWER (read-only).

**Routing rule:** `Project.slug`/`Repository.slug` are unique only *within their
parent*. Flat detail routes therefore use **`pk`**; **slug** is used only on
**nested** routes (`/organizations/{org_slug}/projects/{project_slug}/`).

**Design philosophy — "build it open, then lock it down":** Phases 6–8 build the
views ladder with simple, auth-free querysets. Phases 9–10 retrofit authentication,
org-scoping, and role gates. Lessons completed later are forward-referenced.

---

## Phase 1: Foundations & REST fundamentals

*Goal: build the mental model of HTTP APIs before writing any code.*
📖 Full walkthrough: [docs/phase1_rest_fundamentals.md](phase1_rest_fundamentals.md)

- [x] **What a Web API is** — an API is a waiter carrying your order to the kitchen and bringing food back. → *sketched the endpoints our app will expose.*
- [x] **HTTP verbs** (GET/POST/PUT/PATCH/DELETE) — the action words: read / create / replace / edit / delete. → *mapped each Organization+Project operation to a verb.*
- [x] **HTTP status codes** (2xx/4xx/5xx) — a traffic light: green success, yellow "your fault", red "server broke". → *chose codes: 201/400/403.*
- [x] **JSON** — a universal shipping-label format both sides can read. → *hand-wrote the JSON shape of an Organization.*
- [x] **Client–server & statelessness** — every request is a fresh counter with an amnesiac cashier; you must re-introduce yourself each time. → *why every request carries its own auth.*

---

## Phase 2: Django ORM refresher & project setup

*Goal: stand up the project and model the whole domain so later phases have real tables.*

- [ ] **Project & DRF setup** — tidy the workbench before woodworking. → *`pip install`, `startproject config .`, `startapp api`, register apps, `migrate`, `runserver`.*
- [ ] **Models as blueprints** — a model declares the columns every row will have. → *define Organization, Project, Repository, Mirror, AccessGrant, ActivityEvent.*
- [ ] **Relationships (FK & M2M-through)** — wiring boxes together; AccessGrant links User↔Project *and carries a role*. → *add the FKs + the through model.*
- [ ] **Migrations** — version-controlled instructions that reshape the DB. → *`makemigrations` + `migrate`.*
- [ ] **Django admin** — a free control panel for your data. → *register every model in `admin.py`.*
- [ ] **ORM & `manage.py shell`** — talk to the DB in plain Python. → *create an Org + Projects, query them back.*
- [ ] **Reusing Django's `User`** — Django ships a "people" table; never reinvent logins. → *point AccessGrant at `User`, create a couple of users.*

---

## Phase 3: Serializers, Part 1 — translating models to JSON

*Goal: the serializer's core job (object→JSON out, validated JSON→object in).*

- [ ] **Why serializers exist** — a bilingual translator between Python and JSON. → *first `OrganizationSerializer` in the shell.*
- [ ] **`Serializer` vs `ModelSerializer`** — hand-sewing every button vs buying the shirt pre-made. → *build OrganizationSerializer both ways.*
- [ ] **Fields & the `Meta` class** — choose which columns to expose and how. → *`ProjectSerializer` via `Meta.fields` (try `exclude`).*
- [ ] **Serialize vs deserialize** — `.data` goes out, `.validated_data` comes in. → *shell: serialize an Org, then feed a dict + inspect `is_valid()`.*
- [ ] **`.save()`: create vs update** — same Submit button files new *or* edits existing, based on `instance=`. → *create a Project, then update it.*
- [ ] **`read_only` / `write_only`** — display-only price tags vs one-way secret drop-boxes. → *`created_at` read-only; `Mirror.sync_token` write-only.*
- [ ] **`many=True`** — serialize/validate a whole list at once. → *serialize a queryset of Projects.*

---

## Phase 4: Serializers, Part 2 — validation & advanced fields

*Goal: master every way DRF validates and shapes data.*

- [ ] **Field-level `validate_<field>`** — a bouncer checking one thing per guest. → *`validate_slug()` enforces lowercase-hyphenated.*
- [ ] **Object-level `validate`** — a bouncer inspecting the whole party for multi-field rules. → *`MirrorSerializer.validate()`: source ≠ target URL.*
- [ ] **Validators** (`UniqueValidator`, `UniqueTogetherValidator`, custom) — reusable rule stamps. → *unique Org name; unique (project, user) on AccessGrant.*
- [ ] **`source`** — a field's stage name vs its real name. → *expose `granted_by.username` as `granted_by_name`.*
- [ ] **`SerializerMethodField`** — a computed column running a function. → *`repo_count` on OrganizationSerializer.*
- [ ] **`required` / `default` / `allow_null`** — mandatory vs pre-filled vs blank-allowed. → *Project.visibility default `PRIVATE`; description optional.*
- [ ] **`to_representation` / `to_internal_value`** — manual override of output/input shape. → *wrap Repository output; normalize an incoming clone URL.*

---

## Phase 5: Relations & nested serializers

*Goal: represent connections in every idiom; know when to reference vs embed.*

- [ ] **`PrimaryKeyRelatedField`** — cite a relation by ID (like a docket number). → *ProjectSerializer shows its org as an ID.*
- [ ] **`StringRelatedField`** — show a relation by its `__str__` name. → *RepositorySerializer shows its project as a string.*
- [ ] **`SlugRelatedField`** — reference by a friendly unique handle. → *AccessGrant points to its project by slug.*
- [ ] **`HyperlinkedRelatedField` + serializer `context`** — return a clickable URL; needs `request` in context. → *render Project's org as a link.*
- [ ] **Nested serializers (read)** — embed the full related object. → *OrganizationSerializer embeds its Projects.*
- [ ] **Writable nested — create *and* update** — one form creates/edits parent + children; writable relations need `queryset=`. → *create an Org with initial Projects; then update them.*
- [ ] **`depth`** — a dial to auto-expand relations N levels. → *`Meta.depth=1` on ProjectSerializer.*

---

## Phase 6: Views ladder, Part 1 — function-based views

*Goal: write your first endpoints the explicit way so later "magic" is understood.*

- [ ] **`@api_view`** — a sticker upgrading a plain function into a DRF endpoint. → *GET(list)+POST(create) for Organizations.*
- [ ] **The `Request` object** — an envelope that already unpacked body/params/user. → *read `request.data` and `request.query_params`.*
- [ ] **The `Response` object** — auto-formats a Python dict into JSON. → *`Response(serializer.data, status=201)`.*
- [ ] **The `status` module** — named constants instead of magic numbers. → *replace `201` with `status.HTTP_201_CREATED`.*

---

## Phase 7: Views ladder, Part 2 — class-based & generic views

*Goal: climb from raw APIView through mixins to one-line generics.*

- [ ] **`APIView`** — a class with one method per verb. → *rewrite Org list+detail as APIView.*
- [ ] **`GenericAPIView` + mixins** — Lego bricks (List/Create/Retrieve) you snap on. → *ProjectList from mixins.*
- [ ] **`queryset` & `serializer_class`** — the two dials a generic view reads. → *wire them on ProjectList.*
- [ ] **Concrete generics** — pre-assembled kits (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`). → *Repositories in one line each.*
- [ ] **`get_queryset` / `get_serializer_class` overrides** — swap the dial per request. → *stub org-scoping (finished in Phase 10).*
- [ ] **`lookup_field`** — which column identifies one record in the URL (pk vs slug). → *Org detail by pk (slug only on nested routes).*
- [ ] **`perform_create` / `perform_update` / `perform_destroy`** — hooks to inject data at save time. → *stamp `granted_by=request.user` on AccessGrant create.*

---

## Phase 8: ViewSets, routers & custom actions

*Goal: top of the ladder — bundle actions, auto-generate URLs, add custom/nested endpoints.*

- [ ] **`ViewSet`** — bundle all of a resource's actions into one class. → *Repository list/retrieve/create.*
- [ ] **`ModelViewSet`** — full CRUD in ~3 lines. → *`OrganizationViewSet`.*
- [ ] **`ReadOnlyModelViewSet`** — a museum exhibit: list+retrieve only. → *`MirrorViewSet` (managed by jobs).*
- [ ] **Routers (`DefaultRouter`)** — an automatic URL-wiring machine. → *register orgs/projects/repos under `/api/`.*
- [ ] **`@action` custom endpoints** — bolt a custom button onto a resource. → *`archive`, `sync`, `retry`, `revoke`.*
- [ ] **Nested routing (drf-nested-routers)** — URLs mirror ownership. → *`/organizations/{org_slug}/projects/`.*
- [ ] **Router `basename`** — required when `get_queryset` is overridden without a `queryset` attr. → *set it on scoped viewsets.*

---

## Phase 9: Authentication — proving who you are

*Goal: how DRF identifies the caller across every scheme; how `request.user` flows in.*

- [ ] **`request.user` & `AnonymousUser`** — the API's caller-ID. → *`GET /me/` returns the caller's entitlements.*
- [ ] **`SessionAuthentication` (+ CSRF)** — the website wristband; session auth enforces CSRF on unsafe verbs. → *browsable API login works.*
- [ ] **`BasicAuthentication`** — shout user+pass every request (HTTPS only). → *quick curl testing.*
- [ ] **DRF `TokenAuthentication`** — a coat-check ticket: log in once, show token after. → *`authtoken`, obtain-token endpoint, `Authorization: Token …`.*
- [ ] **JWT (SimpleJWT)** — a self-contained tamper-proof badge with its own expiry. → *`/token/` + `/token/refresh/`.*
- [ ] **Custom authentication** — your own doorman for an odd credential. → *`X-API-Key` header for service accounts.*

---

## Phase 10: Permissions — deciding what you may do

*Goal: layer authorization on auth; coarse built-ins → object-level → role-based → composed.*

- [ ] **Built-in permission classes** — velvet ropes: AllowAny / IsAuthenticated / IsAdminUser. → *lock writes behind IsAuthenticated globally.*
- [ ] **`IsAuthenticatedOrReadOnly`** — anyone window-shops; only members rearrange. → *public GET, login for writes.*
- [ ] **Object-level `has_object_permission`** — not "enter the building" but "touch THIS item"; runs via `get_object()`, and **must be called manually** (`self.check_object_permissions(obj)`) inside `@action`s. → *only org members edit that project.*
- [ ] **Custom role-based permission** — read the job title before allowing action. → *`IsProjectMaintainer` consults AccessGrant.role.*
- [ ] **Composing with `& | ~`** — logic gates for rules. → *`(IsOrgAdmin | ReadOnly) & ~IsSuspended`.*
- [ ] **Finish org-scoping + secure Phase-8 actions** — complete the deferred `get_queryset` scoping and role-gate archive/sync/retry/revoke.

---

## Phase 11: Throttling — rate-limiting abuse

*Goal: protect the API with global and per-endpoint rate limits.*

- [ ] **`AnonRateThrottle` & `UserRateThrottle`** — a turnstile capping requests/hour. → *set global rates; observe `429`.*
- [ ] **`ScopedRateThrottle`** — a stricter turnstile on one heavy door. → *`throttle_scope='mirror_sync'`.*

---

## Phase 12: Pagination — serving big lists in chunks

*Goal: return large collections in navigable pages; know which strategy when.*

- [ ] **`PageNumberPagination`** — book pages: `?page=2`. → *paginate repositories.*
- [ ] **`LimitOffsetPagination`** — a sliding window: take N from position M. → *projects list.*
- [ ] **`CursorPagination`** — a bookmark that survives inserts (no dupes on a live feed). → *`ActivityEvent` feed ordered by `created_at`.*

---

## Phase 13: Filtering, searching & ordering

*Goal: let clients narrow, search, and sort without bespoke query code.*

- [ ] **`django-filter` `FilterSet`** — the faceted sidebar filters. → *`?organization=&visibility=` on projects.*
- [ ] **`SearchFilter`** — one search box across several columns. → *`?search=` over repo name+description.*
- [ ] **`OrderingFilter`** — the "sort by" dropdown. → *`?ordering=-created_at`.*

---

## Phase 14: Content negotiation, renderers/parsers & versioning

*Goal: control the wire formats and evolve the API without breaking clients.*

- [ ] **Content negotiation** — the waiter asking "JSON or HTML?" per Accept header. → *same org data as JSON to curl, HTML to a browser.*
- [ ] **Renderers** — the plating station (JSON / browsable / CSV). → *add a custom CSV renderer for a repo export.*
- [ ] **Parsers** — the intake understanding JSON / form / file uploads. → *`MultiPartParser` for an org `logo` upload.*
- [ ] **Versioning** — keep v1 and v2 menus so old orders still work. → *`URLPathVersioning` `/api/v1/` vs `/api/v2/` (note Namespace/AcceptHeader).*

---

## Phase 15: Exception handling

*Goal: standardize how errors are raised and shaped.*

- [ ] **Built-in DRF exceptions** — pre-printed error cards (NotFound/PermissionDenied/ValidationError). → *raise them in the archive action.*
- [ ] **Custom exception handler** — one complaints desk reformatting every error. → *`{error:{code,message}}` via `EXCEPTION_HANDLER`.*

---

## Phase 16: Testing the API

*Goal: prove endpoints behave so future refactors are safe.*

- [ ] **`APITestCase` & `APIClient`** — a robot user hitting endpoints and checking replies. → *create+list Organizations, assert 201/200.*
- [ ] **`APIRequestFactory`** — a lab bench feeding a raw request into a view. → *drive ProjectViewSet actions directly.*
- [ ] **`force_authenticate`** — a skeleton key logging the test-robot in. → *maintainer 200 vs viewer 403.*

---

## Phase 17: Schema & documentation

*Goal: turn the API into a self-describing, interactively documented product.*

- [ ] **Browsable API** — a free clickable UI in the box. → *exercise every endpoint in the browser.*
- [ ] **OpenAPI schema** — a machine-readable table of contents. → *generate the schema document.*
- [ ] **drf-spectacular (Swagger UI + ReDoc)** — an auto-generated, always-current manual with a try-it console. → *`/api/schema/`, `/api/docs/`, `/api/redoc/`; refine with `@extend_schema`.*

---

## Phase 18: Performance & advanced topics

*Goal: production concerns — query efficiency, hyperlinked APIs, caching, signals, async.*

- [ ] **N+1 & `select_related` / `prefetch_related`** — grab everything in one trip, not a hundred. → *optimize the projects list.*
- [ ] **`HyperlinkedModelSerializer`** — every relation a clickable URL; self-navigable like a website. → *re-expose Organizations.*
- [ ] **Caching responses** — keep a photocopy of a slow answer. → *`cache_page` on an org-stats action.*
- [ ] **Signals** — tripwires that run code on events. → *`post_save` auto-creates an auth Token for every new User.*
- [ ] **Async views (brief)** — one worker juggling many slow I/O calls. → *a plain Django async view fanning out mirror health-checks.*

---

## Progress log

_Add a dated line as we finish each phase._

- **2026-07-11 — Phase 1 complete.** REST fundamentals covered; endpoint menu designed in [phase1_rest_fundamentals.md](phase1_rest_fundamentals.md). Docs moved to `docs/`. Next: Phase 2 setup.
