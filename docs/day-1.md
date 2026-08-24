# Day 1 — System design

**Focus theme:** Sounding natural and confident in system design discussions  
**Difficulty:** Standard C1  
**Mode:** Lite  
**Date:** 2026-08-19

*System Design English for Senior Engineers*

## Professional Idioms { .fe-sec--idiom }

### 1. Paint ourselves into a corner

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Create a situation where future options become limited.
- **IPA:** `/peɪnt aʊərˈsɛlvz ˈɪntu ə ˈkɔːrnər/`
- **Formality:** Neutral

!!! failure "Avoid"
    This design may block us in future.

!!! success "Say instead"
    - This design may paint us into a corner later.

**Examples**

=== "Engineering"
    If we hard-code the tenant model now, we may paint ourselves into a corner when enterprise customers ask for custom isolation.

=== "Meeting"
    I’m fine with the short-term fix, but let’s make sure we don’t paint ourselves into a corner architecturally.

=== "Presentation"
    We avoided a single-region assumption because it would have painted us into a corner for global rollout.

### 2. Put a stake in the ground

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Make an initial clear decision or proposal so discussion can move forward.
- **IPA:** `/pʊt ə steɪk ɪn ðə ɡraʊnd/`
- **Formality:** Neutral

!!! failure "Avoid"
    Let us freeze one proposal for discussion.

!!! success "Say instead"
    - Let’s put a stake in the ground and iterate from there.

**Examples**

=== "Engineering"
    To unblock the design review, I’ll put a stake in the ground: we should start with async replication and revisit sync guarantees later.

=== "Meeting"
    We don’t need the perfect answer today. Let’s put a stake in the ground and validate it with data.

=== "Presentation"
    Our initial architecture puts a stake in the ground around service ownership and failure isolation.

### 3. Not set in stone

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Still changeable; not final.
- **IPA:** `/nɑːt sɛt ɪn stoʊn/`
- **Formality:** Neutral

!!! failure "Avoid"
    This is not freezed yet.

!!! success "Say instead"
    - This is not set in stone yet.

**Examples**

=== "Engineering"
    The API shape is not set in stone, but the ownership boundaries should be stable.

=== "Meeting"
    The timeline is not set in stone, but we need a realistic estimate before committing externally.

=== "Presentation"
    These numbers are not set in stone; they’re based on early load-test results.

## Phrasal Verbs { .fe-sec--phrasal_verb }

### 1. Factor in

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Include something as part of your thinking, estimate, or decision.
- **IPA:** `/ˈfæktər ɪn/`

!!! failure "Avoid"
    We should consider about migration cost.

!!! success "Say instead"
    - We should factor in the migration cost.

**Examples**

=== "Technical-discussion"
    We need to factor in retry storms when estimating peak load.

=== "Code-review"
    This looks correct, but can we factor in the null-response case before merging?

=== "Leadership"
    When we discuss the deadline, we should factor in testing, rollout, and support readiness.

### 2. Spell out

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Explain clearly and explicitly.
- **IPA:** `/spɛl aʊt/`

!!! failure "Avoid"
    Please explain in more detailly.

!!! success "Say instead"
    - Can you spell out the failure scenario?

**Examples**

=== "Technical-discussion"
    Can you spell out what happens if the primary region becomes unavailable?

=== "Code-review"
    Please spell out the assumption in a comment so future maintainers don’t misread this.

=== "Leadership"
    We should spell out the risk clearly instead of saying the plan is ‘mostly fine.’

### 3. Roll back

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Revert to an earlier version or previous state.
- **IPA:** `/roʊl bæk/`

!!! failure "Avoid"
    We will revert back the deployment.

!!! success "Say instead"
    - We will roll back the deployment.
    - We will revert the change.

!!! warning "Note"
    Avoid “revert back” — “revert” already means “go back.”

**Examples**

=== "Technical-discussion"
    If the error rate crosses the threshold, we’ll roll back automatically.

=== "Code-review"
    Can we make this easier to roll back if the new parser behaves differently in production?

=== "Leadership"
    We have a controlled rollout plan and a clear path to roll back if customer impact appears.

## C1/C2 Vocabulary { .fe-sec--vocabulary }

### 1. Constraint

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A limitation or condition that shapes what you can do.
- **IPA:** `/kənˈstreɪnt/`
- **Synonyms:** limitation, restriction, boundary
- **Antonyms:** freedom, flexibility, openness
- **Collocations:** technical constraint, design constraint, resource constraint, latency constraint

!!! failure "Avoid"
    We have one limitation that latency should be low.

!!! success "Say instead"
    - We have a latency constraint.

**Examples**

=== "Software-engineering"
    The main constraint is that the service must respond within 50 milliseconds under peak load.

=== "Stakeholder"
    Given the timeline constraint, we can deliver the core workflow first and defer advanced reporting.

### 2. Robust

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Strong, reliable, and able to handle failures or edge cases.
- **IPA:** `/roʊˈbʌst/`
- **Synonyms:** resilient, reliable, sturdy
- **Antonyms:** fragile, brittle, unreliable
- **Collocations:** robust design, robust implementation, robust error handling, robust validation

!!! failure "Avoid"
    We need a strong error handling.

!!! success "Say instead"
    - We need robust error handling.

**Examples**

=== "Software-engineering"
    The parser needs to be robust against malformed input, not just valid test data.

=== "Stakeholder"
    This approach gives us a more robust rollout because we can isolate failures by region.

### 3. Pragmatic

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Practical and realistic rather than overly theoretical or idealistic.
- **IPA:** `/præɡˈmætɪk/`
- **Synonyms:** practical, realistic, sensible
- **Antonyms:** idealistic, theoretical, impractical
- **Collocations:** pragmatic approach, pragmatic solution, pragmatic compromise, pragmatic decision

!!! failure "Avoid"
    We need a practical way only.

!!! success "Say instead"
    - We need a pragmatic approach.

**Examples**

=== "Software-engineering"
    A fully generic framework would be elegant, but a pragmatic implementation is better for this release.

=== "Stakeholder"
    We’re taking a pragmatic approach: reduce the highest-risk failures first, then improve automation.

### 4. Defensible

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Easy to justify with solid reasoning, data, or constraints.
- **IPA:** `/dɪˈfɛnsəbəl/`
- **Synonyms:** justifiable, reasonable, supportable
- **Antonyms:** weak, unjustified, arbitrary
- **Collocations:** defensible decision, defensible estimate, defensible architecture, defensible position

!!! failure "Avoid"
    This decision can be defended by us.

!!! success "Say instead"
    - This is a defensible decision.

**Examples**

=== "Software-engineering"
    Choosing Postgres here is defensible because the access pattern is relational and the team already has operational experience.

=== "Stakeholder"
    The revised timeline is defensible because it includes integration testing and staged rollout.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| “This is not freezed yet.” | “This is not set in stone yet.” | “Freezed” is incorrect; this sounds natural in meetings. |
| “Please explain in detailly.” | “Can you spell out the details?” | “Detailly” is not natural English. |
| “We need to consider about latency.” | “We need to factor in latency.” | “Consider about” is incorrect; “factor in” is concise. |
| “We will revert back the deployment.” | “We’ll roll back the deployment.” | Avoids the redundant phrase “revert back.” |
| “This design will block us in future.” | “This design may paint us into a corner later.” | More idiomatic and executive-level. |
| “Let us freeze one proposal.” | “Let’s put a stake in the ground.” | Sounds collaborative, not rigid. |
| “We need strong error handling.” | “We need robust error handling.” | More precise technical vocabulary. |
| “Due to timeline limitation…” | “Given the timeline constraint…” | More natural and professional. |
| “This is a practical solution.” | “This is a pragmatic solution.” | More senior-level wording. |
| “This decision has justification.” | “This is a defensible decision.” | Cleaner, more natural phrasing. |

## Speaking Practice

!!! quote "Practice out loud"
    Answer these ALOUD. Don’t just read them silently. Your goal is to make the expressions feel automatic.

=== "Meeting"

    **Design review**

    > The team wants to hard-code a customer-specific rule to meet a deadline. What would you say?

    :material-target: **Use:** `paint ourselves into a corner` · `pragmatic`

    **Architecture discussion**

    > You need the team to choose an initial design even though some details are still open. What would you say?

    :material-target: **Use:** `put a stake in the ground` · `not set in stone`

    **Risk discussion**

    > A proposed solution looks simple, but it ignores failure recovery. What would you say?

    :material-target: **Use:** `factor in` · `robust`

=== "Presentation"

    **Management update**

    > Explain why your team chose a slightly slower but safer rollout plan.

    :material-target: **Use:** `defensible` · `constraint`

    **Technical presentation**

    > Explain why your API proposal may change after performance testing.

    :material-target: **Use:** `not set in stone` · `spell out`

    **Release readiness**

    > Describe your rollback strategy for a risky deployment.

    :material-target: **Use:** `roll back` · `robust`

=== "Leadership-discussion"

    **Pushback upward**

    > A stakeholder wants the fastest possible delivery, but the quality risk is high. What would you say?

    :material-target: **Use:** `factor in` · `defensible`

    **Cross-team alignment**

    > Two teams disagree on ownership boundaries. How would you frame the discussion?

    :material-target: **Use:** `put a stake in the ground` · `spell out`

    **Strategic design**

    > Your team is choosing between a quick fix and a scalable design. What would you say?

    :material-target: **Use:** `paint ourselves into a corner` · `pragmatic`

## Output Correction

!!! example "Your turn"
    For next session, write or speak 2 sentences using today’s expressions. Example prompts:

    - Use paint ourselves into a corner and constraint in one sentence.
    - Use factor in and defensible in one sentence.

    I’ll correct them for C2-level tone, naturalness, and leadership polish.

!!! tip "Tomorrow's preview"
    Next topic: Code reviews — focus on giving firm but respectful feedback without sounding blunt or defensive.

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| Paint ourselves into a corner | <span class="fe-badge fe-badge--idiom">Idiom</span> | limit our future options badly | <span class="fe-badge fe-badge--new">New</span> |
| Put a stake in the ground | <span class="fe-badge fe-badge--idiom">Idiom</span> | make initial clear proposal now | <span class="fe-badge fe-badge--new">New</span> |
| Not set in stone | <span class="fe-badge fe-badge--idiom">Idiom</span> | still changeable, not final yet | <span class="fe-badge fe-badge--new">New</span> |
| Factor in | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | include in decision or estimate | <span class="fe-badge fe-badge--new">New</span> |
| Spell out | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | explain clearly and explicitly | <span class="fe-badge fe-badge--new">New</span> |
| Roll back | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | revert to previous working state | <span class="fe-badge fe-badge--new">New</span> |
| Constraint | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | limitation shaping possible choices | <span class="fe-badge fe-badge--new">New</span> |
| Robust | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | reliable under difficult conditions | <span class="fe-badge fe-badge--new">New</span> |
| Pragmatic | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | practical rather than overly idealistic | <span class="fe-badge fe-badge--new">New</span> |
| Defensible | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | justifiable with solid reasoning | <span class="fe-badge fe-badge--new">New</span> |
