# Day 6 — Technical debt

*Discussing technical debt without sounding negative or vague*

<p class="fe-meta">Standard C1 · Lite · 2026-08-24</p>

## Professional Idioms { .fe-sec--idiom }

### 1. Kick the can down the road

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Delay dealing with a problem, usually making it worse later.
- **IPA:** `/kɪk ðə kæn daʊn ðə roʊd/`
- **Formality:** Neutral; slightly conversational but common in leadership discussions

!!! failure "Avoid: We are postponing this problem for future."

!!! success "Say instead: We’re kicking the can down the road."

**Examples**

=== "Engineering"
    If we keep adding feature-specific patches without addressing the core abstraction, we’re just kicking the can down the road.

=== "Meeting"
    I understand the release pressure, but skipping this cleanup again feels like kicking the can down the road.

=== "Presentation"
    The recommendation is to address the dependency issue now rather than kick the can down the road into the next release cycle.

### 2. Pay down technical debt

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Reduce accumulated shortcuts, complexity, or maintainability problems.
- **IPA:** `/peɪ daʊn ˈtɛknɪkəl dɛt/`
- **Formality:** Neutral; very common in engineering

!!! failure "Avoid: We need to clear technical debt."

!!! success "Say instead: We need to pay down technical debt."

**Examples**

=== "Engineering"
    We should reserve capacity each sprint to pay down technical debt in the configuration layer.

=== "Meeting"
    This isn’t just cleanup; it’s necessary work to pay down technical debt that is slowing feature delivery.

=== "Presentation"
    Over the last quarter, we paid down technical debt by removing legacy code paths and consolidating duplicate services.

### 3. Come back to bite us

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Cause problems later because it was ignored or handled poorly earlier.
- **IPA:** `/kʌm bæk tə baɪt ʌs/`
- **Formality:** Neutral; conversational but professional

!!! failure "Avoid: This issue will create problem in future."

!!! success "Say instead: This could come back to bite us."

**Examples**

=== "Engineering"
    If we don’t validate the migration path now, this could come back to bite us during customer rollout.

=== "Meeting"
    I’m okay with a short-term workaround, but undocumented behavior will come back to bite us.

=== "Presentation"
    The team identified several assumptions that could come back to bite us at scale.

## Phrasal Verbs { .fe-sec--phrasal_verb }

### 1. Chip away at

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Gradually reduce a large problem through steady, repeated effort.
- **IPA:** `/tʃɪp əˈweɪ æt/`

!!! failure "Avoid: We will slowly reduce technical debt little by little."

!!! success "Say instead: We’ll chip away at the technical debt over the next few sprints."

**Examples**

=== "Technical-discussion"
    We don’t need a big rewrite; we can chip away at the legacy dependency by replacing one caller at a time.

=== "Code-review"
    This patch is small, but it helps us chip away at the old error-handling pattern.

=== "Leadership"
    We’re planning a sustained effort to chip away at the maintenance burden without blocking feature work.

### 2. Phase out

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Gradually remove or replace something over time.
- **IPA:** `/feɪz aʊt/`

!!! failure "Avoid: We will remove this API slowly-slowly."

!!! success "Say instead: We’ll phase out this API over two releases."

**Examples**

=== "Technical-discussion"
    We should phase out the old client library instead of forcing all teams to migrate at once.

=== "Code-review"
    Can you add a TODO with the plan to phase out this compatibility branch?

=== "Leadership"
    We’ll phase out the legacy service after the top three consumers move to the new interface.

### 3. Shore up

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Strengthen something weak or risky.
- **IPA:** `/ʃɔːr ʌp/`

!!! failure "Avoid: We need to make this area strong."

!!! success "Say instead: We need to shore up this area."

**Examples**

=== "Technical-discussion"
    Before scaling this to more customers, we need to shore up the retry and timeout behavior.

=== "Code-review"
    This change helps shore up validation around malformed input.

=== "Leadership"
    We should shore up the test coverage before committing to the broader rollout.

## C1/C2 Vocabulary { .fe-sec--vocabulary }

### 1. Brittle

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Easily broken by small changes; fragile and hard to modify safely.
- **IPA:** `/ˈbrɪtəl/`
- **Synonyms:** fragile, delicate, unstable
- **Antonyms:** robust, resilient, flexible
- **Collocations:** brittle code, brittle tests, brittle integration, brittle dependency

!!! failure "Avoid: This code is very breakable."

!!! success "Say instead: This code is brittle."

**Examples**

=== "Software-engineering"
    The parser is brittle because small format changes cause unrelated tests to fail.

=== "Stakeholder"
    The current flow works, but it’s brittle, so every new customer-specific requirement increases delivery risk.

### 2. Sustainable

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Able to continue over time without creating excessive cost, risk, or burnout.
- **IPA:** `/səˈsteɪnəbəl/`
- **Synonyms:** maintainable, viable, durable
- **Antonyms:** unsustainable, fragile, short-lived
- **Collocations:** sustainable pace, sustainable architecture, sustainable delivery model, sustainable process

!!! failure "Avoid: This approach is not long-time good."

!!! success "Say instead: This approach is not sustainable."

**Examples**

=== "Software-engineering"
    Manually updating these configs for every release is not sustainable.

=== "Stakeholder"
    We can meet the immediate deadline, but we need a more sustainable delivery model for future releases.

### 3. Incremental

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Done in small, controlled steps rather than all at once.
- **IPA:** `/ˌɪŋkrəˈmɛntəl/`
- **Synonyms:** gradual, step-by-step, phased
- **Antonyms:** big-bang, abrupt, wholesale
- **Collocations:** incremental rollout, incremental migration, incremental improvement, incremental refactor

!!! failure "Avoid: We should do this step by steply."

!!! success "Say instead: We should take an incremental approach."

**Examples**

=== "Software-engineering"
    An incremental migration is safer because we can validate each service before moving the next one.

=== "Stakeholder"
    We recommend an incremental rollout to reduce risk and keep customer impact low.

### 4. Deprecation

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** The process of marking something as outdated and scheduled for future removal.
- **IPA:** `/ˌdɛprəˈkeɪʃən/`
- **Synonyms:** retirement, sunset, phase-out
- **Antonyms:** introduction, adoption, launch
- **Collocations:** deprecation plan, deprecation notice, deprecation timeline, API deprecation

!!! failure "Avoid: We will obsolete this API."

!!! success "Say instead"
    - We’ll define a deprecation plan for this API.
    - We’ll deprecate this API.

**Examples**

=== "Software-engineering"
    We need a clear deprecation timeline before removing the old endpoint.

=== "Stakeholder"
    The deprecation plan gives partner teams enough time to migrate without blocking the release.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| This code is having many issues. | This code has several maintainability issues. | More direct and technical. |
| We should not take this lightly. | We shouldn’t underestimate this risk. | Sounds more senior and precise. |
| This will create problems in future. | This could create problems later. | More natural phrasing; avoids over-formality. |
| We need to do cleanup activity. | We need to clean this up. | Uses the natural verb form. |
| This is not a scalable way of working. | This approach won’t scale. | Shorter and more idiomatic. |
| We are doing temporary solution only. | This is only a short-term workaround. | More native engineering wording. |
| We need to remove old implementation slowly. | We need to phase out the old implementation. | Uses the correct phrasal verb. |
| It is creating maintenance overheads. | It’s increasing the maintenance overhead. | “Overhead” is usually singular in this context. |
| We should discuss on technical debt. | We should discuss the technical debt. | No “on” after “discuss.” |
| This issue may come in later stage. | This issue may resurface later. | More natural and concise. |

## Speaking Practice

!!! quote "Practice out loud"
    Answer these ALOUD. Don’t just read them silently. Your goal is to sound calm, senior, and specific.

=== "Meeting"

    > Your team wants to skip refactoring again to meet a deadline. What do you say?

    :material-target: **Use:** `kick the can down the road` · `sustainable`

    > A teammate says, “Let’s rewrite the whole module.” You prefer a safer approach. How do you respond?

    :material-target: **Use:** `incremental` · `chip away at`

    > A legacy API is still used by multiple teams. How do you propose handling it?

    :material-target: **Use:** `phase out` · `deprecation`

=== "Presentation"

    > Explain why technical debt is affecting delivery speed.

    :material-target: **Use:** `brittle` · `pay down technical debt`

    > Present a plan to improve system maintainability over the next quarter.

    :material-target: **Use:** `incremental` · `shore up`

    > Explain why a short-term workaround is acceptable only with follow-up ownership.

    :material-target: **Use:** `come back to bite us` · `sustainable`

=== "Leadership-discussion"

    > Your manager asks why the team needs capacity for cleanup. What do you say?

    :material-target: **Use:** `pay down technical debt` · `maintenance overhead`

    > A stakeholder wants faster delivery, but the platform is becoming fragile. How do you explain the risk?

    :material-target: **Use:** `brittle` · `come back to bite us`

    > You need to propose retiring an old component without disrupting partner teams. What’s your plan?

    :material-target: **Use:** `deprecation` · `phase out`

## Output Correction

!!! example "Your turn"
    For next session, write or speak 2 sentences using at least 3 of today’s expressions. For example, use:

    kick the can down the road
    pay down technical debt
    brittle
    phase out
    incremental
    I’ll correct them at a C2 workplace-English level and flag anything that sounds too textbook or “Indian corporate English.”

!!! tip "Tomorrow's preview"
    Project status updates — focus on giving concise, executive-friendly updates without sounding defensive.

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| Kick the can down the road | <span class="fe-badge fe-badge--idiom">Idiom</span> | Delay problem to future | <span class="fe-badge fe-badge--new">New</span> |
| Pay down technical debt | <span class="fe-badge fe-badge--idiom">Idiom</span> | Reduce accumulated engineering debt | <span class="fe-badge fe-badge--new">New</span> |
| Come back to bite us | <span class="fe-badge fe-badge--idiom">Idiom</span> | Cause problems later unexpectedly | <span class="fe-badge fe-badge--new">New</span> |
| Chip away at | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Reduce gradually over time | <span class="fe-badge fe-badge--new">New</span> |
| Phase out | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Remove gradually over time | <span class="fe-badge fe-badge--new">New</span> |
| Shore up | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Strengthen weak risky area | <span class="fe-badge fe-badge--new">New</span> |
| Brittle | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Fragile under small changes | <span class="fe-badge fe-badge--new">New</span> |
| Sustainable | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Viable over long term | <span class="fe-badge fe-badge--new">New</span> |
| Incremental | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Done in small steps | <span class="fe-badge fe-badge--new">New</span> |
| Deprecation | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Planned retirement of old feature | <span class="fe-badge fe-badge--new">New</span> |
