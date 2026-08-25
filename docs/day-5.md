# Day 5 — Root cause analysis

*Explaining root cause clearly without overclaiming*

<p class="fe-meta">Standard C1 · Lite · 2026-08-23</p>

## Professional Idioms { .fe-sec--idiom }

### 1. Connect the dots

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Link separate pieces of evidence to understand the full picture.
- **IPA:** `/kəˈnekt ðə dɑːts/`
- **Formality:** Neutral

!!! failure "Avoid: We need to connect all observations and conclude."

!!! success "Say instead"
    - We need to connect the dots across logs, metrics, and deployment history.

**Examples**

=== "Engineering"
    Once we connected the dots between the config change and the latency spike, the pattern became clear.

=== "Meeting"
    We don’t have the full answer yet, but we’re starting to connect the dots.

=== "Presentation"
    The incident timeline helped us connect the dots between increased retries and database saturation.

### 2. The smoking gun

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A clear piece of evidence that strongly points to the cause.
- **IPA:** `/ðə ˈsmoʊkɪŋ ɡʌn/`
- **Formality:** Neutral; slightly vivid, common in incident reviews

!!! failure "Avoid: This is the final proof for issue."

!!! success "Say instead"
    - This looks like the smoking gun.

**Examples**

=== "Engineering"
    The error spike immediately after the feature flag change was the smoking gun.

=== "Meeting"
    We should be careful — this is strong evidence, but I’m not ready to call it the smoking gun yet.

=== "Presentation"
    The heap dump gave us the smoking gun: leaked references from the session cache.

### 3. Close the loop

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Finish a discussion or process by confirming the outcome, owner, or next step.
- **IPA:** `/kloʊz ðə luːp/`
- **Formality:** Neutral

!!! failure "Avoid: Let us close this pending communication."

!!! success "Say instead"
    - Let’s close the loop with the release team after we confirm the fix.

**Examples**

=== "Engineering"
    After we validate the patch in staging, I’ll close the loop with QA.

=== "Meeting"
    Before we end, let’s close the loop on action items and owners.

=== "Presentation"
    We closed the loop by documenting the root cause, mitigation, and prevention plan.

## Phrasal Verbs { .fe-sec--phrasal_verb }

### 1. Zero in on

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Focus closely on the most likely cause or area.
- **IPA:** `/ˈzɪroʊ ɪn ɑːn/`

!!! failure "Avoid: We are focusing into the retry module."

!!! success "Say instead"
    - We’re zeroing in on the retry module.

**Examples**

=== "Technical-discussion"
    We’re zeroing in on the connection pool because the failures align with pool exhaustion.

=== "Code-review"
    This test helps us zero in on the race condition instead of debugging the whole pipeline.

=== "Leadership"
    We’ve zeroed in on two likely causes and should have a confirmed root cause today.

### 2. Trace back

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Follow evidence backward to find where something started.
- **IPA:** `/treɪs bæk/`

!!! failure "Avoid: We traced till the original commit."

!!! success "Say instead"
    - We traced it back to the original commit.

**Examples**

=== "Technical-discussion"
    We traced the latency spike back to a change in the serialization path.

=== "Code-review"
    Can you trace back why this exception is swallowed instead of propagated?

=== "Leadership"
    We traced the issue back to a deployment configuration mismatch, not a capacity problem.

### 3. Tighten up

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Make something more precise, reliable, or controlled.
- **IPA:** `/ˈtaɪtən ʌp/`

!!! failure "Avoid: We need to make monitoring more strict."

!!! success "Say instead"
    - We need to tighten up monitoring around this path.

**Examples**

=== "Technical-discussion"
    We should tighten up validation so invalid payloads fail earlier.

=== "Code-review"
    Please tighten up the error handling before this lands.

=== "Leadership"
    We’re going to tighten up the rollout checklist to prevent the same failure mode.

## C1/C2 Vocabulary { .fe-sec--vocabulary }

### 1. Intermittent

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Happening occasionally, not continuously.
- **IPA:** `/ˌɪntərˈmɪtənt/`
- **Synonyms:** sporadic, occasional, irregular
- **Antonyms:** continuous, constant, persistent
- **Collocations:** intermittent failure, intermittent timeout, intermittent issue

!!! failure "Avoid: The issue is coming sometimes."

!!! success "Say instead"
    - It’s an intermittent issue.

**Examples**

=== "Software-engineering"
    The failure is intermittent, so we need more traces before changing the retry logic.

=== "Stakeholder"
    We’re investigating an intermittent timeout that affects a small percentage of requests.

### 2. Correlate

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Show a relationship or pattern between two things.
- **IPA:** `/ˈkɔːrəleɪt/`
- **Synonyms:** associate, link, match
- **Antonyms:** disconnect, separate, decouple
- **Collocations:** correlate with metrics, correlate events, correlate failures

!!! failure "Avoid: The errors are matching with deployment."

!!! success "Say instead"
    - The errors correlate with the deployment.

**Examples**

=== "Software-engineering"
    The latency increase seems to correlate with the new cache invalidation logic.

=== "Stakeholder"
    We’re checking whether the customer impact correlates with a specific release window.

### 3. Mitigation

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** An action that reduces impact or risk, even if it does not fully fix the root cause.
- **IPA:** `/ˌmɪtɪˈɡeɪʃən/`
- **Synonyms:** risk reduction, containment, workaround
- **Antonyms:** escalation, exposure, aggravation
- **Collocations:** short-term mitigation, mitigation plan, mitigation strategy

!!! failure "Avoid: We have done one workaround solution."

!!! success "Say instead"
    - We have a short-term mitigation in place.

**Examples**

=== "Software-engineering"
    The immediate mitigation is to lower the retry count while we fix the underlying bug.

=== "Stakeholder"
    We’ve deployed a mitigation to reduce user impact while the permanent fix is being validated.

### 4. Regression

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A new bug or behavior break introduced into something that previously worked.
- **IPA:** `/rɪˈɡreʃən/`
- **Synonyms:** breakage, reintroduced defect, backward step
- **Antonyms:** improvement, fix, enhancement
- **Collocations:** regression test, performance regression, functional regression

!!! failure "Avoid: The old issue came again newly."

!!! success "Say instead"
    - This looks like a regression.

**Examples**

=== "Software-engineering"
    The latest patch introduced a regression in the timeout handling path.

=== "Stakeholder"
    We found a regression during validation, so we’re holding the rollout until the fix is verified.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| We found the issue was coming sometimes. | We found the issue was intermittent. | More precise and native. |
| This issue happened due to some mismatch. | The issue appears to be caused by a configuration mismatch. | Sounds evidence-based, not vague. |
| We are checking from where it started. | We’re trying to trace it back to the first failing change. | More technical and natural. |
| The logs are matching with the deployment. | The logs correlate with the deployment. | Correct verb + preposition. |
| We applied one workaround. | We put a short-term mitigation in place. | More senior incident-review wording. |
| We need to do permanent fix. | We need a permanent fix. | Removes unnecessary “do.” |
| This is the exact proof. | This may be the smoking gun. | Natural phrase, but still careful. |
| We will update once analysis is completed. | We’ll share an update once we confirm the root cause. | Clearer and more active. |
| Let us close all pending points. | Let’s close the loop on the open action items. | More idiomatic for meetings. |
| Same bug came again. | This looks like a regression. | More professional engineering term. |

## Speaking Practice

!!! quote "Practice out loud"
    Answer ALOUD. Keep each answer to 30–45 seconds. Force the listed expressions into your response.

=== "Meeting"

    **Incident triage**

    > The team has several theories about a timeout issue. How would you guide the discussion?

    :material-target: **Use:** `zero in on` · `correlate`

    **Root cause review**

    > You have strong evidence, but not full proof yet. How would you explain that carefully?

    :material-target: **Use:** `the smoking gun` · `intermittent`

    **Action-item closure**

    > The fix is deployed, but QA and release teams still need confirmation. What do you say?

    :material-target: **Use:** `close the loop` · `mitigation`

=== "Presentation"

    **Incident summary**

    > Present the root cause of a production issue to senior managers.

    :material-target: **Use:** `connect the dots` · `regression`

    **Technical timeline**

    > Explain how the team moved from symptoms to likely cause.

    :material-target: **Use:** `trace back` · `correlate`

    **Prevention plan**

    > Explain how you’ll prevent recurrence.

    :material-target: **Use:** `tighten up` · `mitigation`

=== "Leadership-discussion"

    **Risk communication**

    > A stakeholder asks whether the issue is fully fixed. Give a confident but careful answer.

    :material-target: **Use:** `mitigation` · `root cause optional` · `close the loop`

    **Escalation update**

    > Your manager asks what the team knows so far.

    :material-target: **Use:** `zero in on` · `intermittent`

    **Quality improvement**

    > Explain why the team needs time to improve tests after the incident.

    :material-target: **Use:** `regression` · `tighten up`

## Output Correction

!!! example "Your turn"
    For next session, write or speak 2 sentences using at least 3 of today’s expressions. For example, use:
    intermittent, trace back, close the loop, mitigation, the smoking gun.

    I’ll correct them at a C2 level for tone, naturalness, and senior-engineer phrasing.

!!! tip "Tomorrow's preview"
    Technical debt — how to frame engineering debt as risk, leverage, and long-term delivery health without sounding negative.

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| Connect the dots | <span class="fe-badge fe-badge--idiom">Idiom</span> | Link evidence into full picture | <span class="fe-badge fe-badge--new">New</span> |
| The smoking gun | <span class="fe-badge fe-badge--idiom">Idiom</span> | Clear evidence of real cause | <span class="fe-badge fe-badge--new">New</span> |
| Close the loop | <span class="fe-badge fe-badge--idiom">Idiom</span> | Confirm outcome and next steps | <span class="fe-badge fe-badge--new">New</span> |
| Zero in on | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Focus on likely cause | <span class="fe-badge fe-badge--new">New</span> |
| Trace back | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Follow evidence to origin | <span class="fe-badge fe-badge--new">New</span> |
| Tighten up | <span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span> | Make more reliable or precise | <span class="fe-badge fe-badge--new">New</span> |
| Intermittent | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Happening occasionally, not constantly | <span class="fe-badge fe-badge--new">New</span> |
| Correlate | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Show relationship between events | <span class="fe-badge fe-badge--new">New</span> |
| Mitigation | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | Action reducing risk or impact | <span class="fe-badge fe-badge--new">New</span> |
| Regression | <span class="fe-badge fe-badge--vocabulary">Vocabulary</span> | New bug in working behavior | <span class="fe-badge fe-badge--new">New</span> |
