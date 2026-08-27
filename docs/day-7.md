# Day 7 — Project status

*Giving project status updates with senior-level clarity*

<p class="fe-meta">Standard C1 · Lite · 2026-08-26</p>

## Professional Idioms { .fe-sec--idiom }

### 1. On track

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Progressing as planned; no major concern.
- **IPA:** `/ɑːn træk/`
- **Formality:** Neutral

!!! failure "Avoid: The task is going as per plan."

!!! success "Say instead: The work is on track."

**Examples**

=== "Engineering"
    The API migration is on track; we’ve completed the client changes and started integration testing.

=== "Meeting"
    We’re on track for the milestone, but the validation window is still tight.

=== "Presentation"
    The rollout remains on track, with the remaining work focused on test coverage and release readiness.

### 2. Hit a snag

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Encounter an unexpected problem or delay.
- **IPA:** `/hɪt ə snæɡ/`
- **Formality:** Neutral; slightly conversational

!!! failure "Avoid: We faced one small issue in implementation."

!!! success "Say instead: We hit a snag during integration."

**Examples**

=== "Engineering"
    We hit a snag with backward compatibility because one downstream client still depends on the old payload format.

=== "Meeting"
    We hit a snag in staging, but we have a workaround and don’t expect it to affect the release date.

=== "Presentation"
    The team hit a snag during device-level validation, but the issue is now isolated to one configuration.

### 3. In the weeds

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Too focused on low-level details when a higher-level view is needed.
- **IPA:** `/ɪn ðə wiːdz/`
- **Formality:** Casual to Neutral

!!! failure "Avoid: We are going too much into technical depth."

!!! success "Say instead: We’re getting in the weeds."

**Examples**

=== "Engineering"
    We can discuss buffer sizes separately; for this review, I don’t want us to get in the weeds.

=== "Meeting"
    We’re getting in the weeds here. The key question is whether the risk changes the release plan.

=== "Presentation"
    I’ll avoid getting in the weeds and focus on the milestone status, risks, and decisions needed.

## Phrasal Verbs { .fe-sec--phrasal_verb }

### 1. Line up

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Arrange, coordinate, or align people, dependencies, resources, or work.
- **IPA:** `/laɪn ʌp/`

!!! failure "Avoid: We need to align all things before release."

!!! success "Say instead: We need to line up the dependencies before release."

**Examples**

=== "Technical-discussion"
    We need to line up the schema change, client update, and rollout flag before enabling this by default.

=== "Code-review"
    This patch should line up with the existing error-handling pattern in the service layer.

=== "Leadership"
    I’ll line up the validation support with QA so the team isn’t blocked next week.

### 2. Firm up

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Make something clearer, more definite, or more reliable.
- **IPA:** `/fɜːrm ʌp/`

!!! failure "Avoid: We need to make the plan more concrete."

!!! success "Say instead: We need to firm up the plan."

**Examples**

=== "Technical-discussion"
    Let’s firm up the migration sequence before we share the timeline externally.

=== "Code-review"
    Can we firm up the test expectations so the next reviewer can understand the intended behavior?

=== "Leadership"
    We’ll firm up the delivery date after we complete integration testing.

### 3. Fall behind

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Become delayed compared with the planned schedule or expected pace.
- **IPA:** `/fɔːl bɪˈhaɪnd/`

!!! failure "Avoid: We are lagging from schedule."

!!! success "Say instead: We’re falling behind schedule."

**Examples**

=== "Technical-discussion"
    We’re falling behind on validation because the test environment has been unstable.

=== "Code-review"
    If this review stays open another day, the dependent patch may fall behind.

=== "Leadership"
    We’re not blocked, but we are falling behind on documentation and release readiness.

## C1/C2 Vocabulary { .fe-sec--vocabulary }

### 1. Trajectory

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** The direction in which progress, performance, or risk is moving.
- **IPA:** `/trəˈdʒektəri/`
- **Synonyms:** direction, trend, path
- **Antonyms:** stagnation, reversal, instability
- **Collocations:** positive trajectory, current trajectory, delivery trajectory, risk trajectory

!!! failure "Avoid: The project direction is going good."

!!! success "Say instead: The project is on a positive trajectory."

**Examples**

=== "Software-engineering"
    The defect trajectory is improving after the last two fixes, but we need another validation cycle.

=== "Stakeholder"
    Based on the current trajectory, we expect to meet the milestone, assuming no new integration issues come up.

### 2. Slippage

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Delay compared with the original plan or schedule.
- **IPA:** `/ˈslɪpɪdʒ/`
- **Synonyms:** delay, schedule drift, timeline slip
- **Antonyms:** acceleration, on-time delivery, schedule recovery
- **Collocations:** schedule slippage, minor slippage, avoid slippage, cause slippage

!!! failure "Avoid: There is some delay happening in timeline."

!!! success "Say instead: There’s some schedule slippage."

**Examples**

=== "Software-engineering"
    The test instability caused minor slippage, but the implementation work is complete.

=== "Stakeholder"
    We’re seeing slight slippage in validation, but we still have room in the release buffer.

### 3. Contingency

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A backup plan or alternative action if something goes wrong.
- **IPA:** `/kənˈtɪndʒənsi/`
- **Synonyms:** backup plan, fallback, alternative plan
- **Antonyms:** single path, no fallback, fixed plan
- **Collocations:** contingency plan, build in contingency, contingency buffer, contingency option

!!! failure "Avoid: We need one backup if this is not working."

!!! success "Say instead: We need a contingency plan if this doesn’t work."

**Examples**

=== "Software-engineering"
    Our contingency is to keep the old pipeline available until the new path passes soak testing.

=== "Stakeholder"
    We have a contingency plan: if validation slips, we’ll release the feature behind a disabled flag.

### 4. Alignment

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Shared understanding or agreement across teams or stakeholders.
- **IPA:** `/əˈlaɪnmənt/`
- **Synonyms:** agreement, coordination, shared understanding
- **Antonyms:** misalignment, disagreement, disconnect
- **Collocations:** cross-team alignment, stakeholder alignment, technical alignment, alignment on priorities

!!! failure "Avoid: We need to take alignment from all teams."

!!! success "Say instead: We need to get alignment across the teams."

**Examples**

=== "Software-engineering"
    We need technical alignment between the platform and application teams before changing the API contract.

=== "Stakeholder"
    Before we commit to the customer date, we need alignment on scope, risk, and validation coverage.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| The work is going as per plan. | The work is on track. | Shorter and more natural in status updates. |
| We faced one issue in testing. | We hit a snag during testing. | Sounds natural and appropriately low-drama. |
| We are lagging from schedule. | We’re falling behind schedule. | Correct collocation: “fall behind schedule.” |
| We need to take alignment from QA. | We need to get alignment with QA. | “Take alignment” sounds non-native. |
| Timeline got delayed slightly. | We’re seeing minor schedule slippage. | More precise and senior-sounding. |
| We will confirm the date after testing completion. | We’ll firm up the date after testing is complete. | More idiomatic and concise. |
| Let us not go too deep technically now. | Let’s not get in the weeds right now. | Natural meeting phrase for staying high-level. |
| We need one backup plan. | We need a contingency plan. | More professional and specific. |
| I will arrange support from QA team. | I’ll line up QA support. | Cleaner, more native phrasing. |
| Current progress direction is good. | The current trajectory looks positive. | Executive-friendly and concise. |

## Speaking Practice

!!! quote "Practice out loud"
    Answer these ALOUD. Don’t write first. Speak naturally, then record or type your final version.

=== "Meeting"

    > Your feature is mostly on schedule, but validation is tight.

    :material-target: **Use:** `on track` · `slippage`

    > A dependency from another team may affect your milestone.

    :material-target: **Use:** `line up` · `alignment`

    > The discussion is becoming too detailed for a status meeting.

    :material-target: **Use:** `in the weeds` · `firm up`

=== "Presentation"

    > Give a 30-second project update to senior leadership.

    :material-target: **Use:** `trajectory` · `on track`

    > Explain a small delay without sounding defensive.

    :material-target: **Use:** `hit a snag` · `contingency`

    > Present the current release risk and next steps.

    :material-target: **Use:** `slippage` · `firm up`

=== "Leadership-discussion"

    > Your manager asks whether the team can still meet the commitment.

    :material-target: **Use:** `fall behind` · `contingency plan`

    > A stakeholder wants a firm date before testing is complete.

    :material-target: **Use:** `firm up` · `alignment`

    > Another team has not committed support yet.

    :material-target: **Use:** `line up` · `on track`

## Output Correction

!!! example "Your turn"
    For next session, write or speak 2 sentences using at least 3 of today’s expressions.
    **Good targets:**

    on track
    hit a snag
    firm up
    slippage
    contingency
    **Example prompt:**

    - “Give a project status update where the work is mostly fine but one dependency may affect the timeline.”

!!! tip "Tomorrow's preview"
    Leadership discussion — how to disagree upward without sounding defensive.

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| On track | <span class="fe-badge fe-badge--idiom">Idiom</span> | Progressing according to the plan | <span class="fe-badge fe-badge--new">New</span> |
| Hit a snag | <span class="fe-badge fe-badge--idiom">Idiom</span> | Encounter an unexpected small problem | <span class="fe-badge fe-badge--new">New</span> |
| In the weeds | <span class="fe-badge fe-badge--idiom">Idiom</span> | Too deep in unnecessary details | <span class="fe-badge fe-badge--new">New</span> |
| Line up | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Arrange or coordinate dependencies clearly | <span class="fe-badge fe-badge--new">New</span> |
| Firm up | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Make clearer, definite, reliable | <span class="fe-badge fe-badge--new">New</span> |
| Fall behind | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Become delayed against planned schedule | <span class="fe-badge fe-badge--new">New</span> |
| Trajectory | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Direction progress or risk moves | <span class="fe-badge fe-badge--new">New</span> |
| Slippage | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Delay against the planned timeline | <span class="fe-badge fe-badge--new">New</span> |
| Contingency | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Backup plan for possible risk | <span class="fe-badge fe-badge--new">New</span> |
| Alignment | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Shared understanding across involved groups | <span class="fe-badge fe-badge--new">New</span> |
