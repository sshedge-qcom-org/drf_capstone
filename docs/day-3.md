# Day 3 — Production issues

**Focus theme:** Staying calm, precise, and credible during production issues  
**Difficulty:** Standard C1  
**Mode:** Lite  
**Date:** 2026-08-21

*Production Issue English for Senior Engineers*

## Professional Idioms { .fe-sec--idiom }

### 1. Stop the bleeding

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Take immediate action to limit damage before solving the deeper problem.
- **IPA:** `/stɑːp ðə ˈbliːdɪŋ/`
- **Formality:** Neutral; common in incident discussions

!!! failure "Avoid"
    First we should stop the issue impact.

!!! success "Say instead"
    - First, we need to stop the bleeding.

**Examples**

=== "Engineering"
    Before we analyze the root cause, let’s stop the bleeding by disabling the failing rollout flag.

=== "Meeting"
    We can discuss the long-term fix later. Right now, the priority is to stop the bleeding.

=== "Presentation"
    Our first action was to stop the bleeding by routing traffic away from the unstable region.

### 2. Under the hood

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Refers to internal implementation details that are not visible to users.
- **IPA:** `/ˈʌndər ðə hʊd/`
- **Formality:** Neutral

!!! failure "Avoid"
    Internally inside the code, it is doing retries.

!!! success "Say instead"
    - Under the hood, it’s retrying aggressively.

**Examples**

=== "Engineering"
    Under the hood, the client is opening multiple connections per request, which explains the spike.

=== "Meeting"
    The UI looks fine, but under the hood the request path is hitting a deprecated service.

=== "Presentation"
    Under the hood, we replaced synchronous writes with buffered writes to reduce latency.

### 3. The blast radius

<span class="fe-badges"><span class="fe-badge fe-badge--idiom">Idiom</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** The scope or scale of impact caused by a failure or change.
- **IPA:** `/ðə blæst ˈreɪdiəs/`
- **Formality:** Neutral; very common in reliability and systems discussions

!!! failure "Avoid"
    The impact area is very big.

!!! success "Say instead"
    - The blast radius is too large.

**Examples**

=== "Engineering"
    We should split this deployment by region to reduce the blast radius.

=== "Meeting"
    Before we proceed, let’s understand the blast radius if this config is wrong.

=== "Presentation"
    We reduced the blast radius by isolating the new scheduler behind a per-tenant feature flag.

## Phrasal Verbs { .fe-sec--phrasal_verb }

### 1. Rule out

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Eliminate a possible cause after checking evidence.
- **IPA:** `/ruːl aʊt/`

!!! failure "Avoid"
    We can remove network from suspect list.

!!! success "Say instead"
    - We can rule out the network as the cause.

**Examples**

=== "Technical-discussion"
    We checked packet loss and latency, so we can rule out the network path for now.

=== "Code-review"
    This test helps rule out regressions in the retry logic.

=== "Leadership"
    We’ve ruled out infrastructure capacity, so the remaining risk is application-level behavior.

### 2. Dig into

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Investigate something in detail.
- **IPA:** `/dɪɡ ˈɪntuː/`

!!! failure "Avoid"
    I will deep dive on the logs.

!!! success "Say instead"
    - I’ll dig into the logs.
    - I’ll do a deep dive into the logs.

!!! warning "Note"
    “Deep dive” is a noun phrase; “dig into” is the natural verb phrase.

**Examples**

=== "Technical-discussion"
    I’ll dig into the trace spans and check where the extra 300 milliseconds are coming from.

=== "Code-review"
    Can you dig into why this branch bypasses the existing timeout handling?

=== "Leadership"
    We’re digging into the failure pattern now and should have a clearer update in 30 minutes.

### 3. Hold off on

<span class="fe-badges"><span class="fe-badge fe-badge--phrasal_verb">Phrasal verb</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Delay or pause an action until there is more clarity.
- **IPA:** `/hoʊld ɔːf ɑːn/`

!!! failure "Avoid"
    Let us wait the deployment.

!!! success "Say instead"
    - Let’s hold off on the deployment.

**Examples**

=== "Technical-discussion"
    Let’s hold off on restarting the service until we capture the heap dump.

=== "Code-review"
    I’d hold off on merging this until we add coverage for the failure path.

=== "Leadership"
    We should hold off on the external commitment until we know whether this affects all regions.

## C1/C2 Vocabulary { .fe-sec--vocabulary }

### 1. Intermittent

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Happening irregularly; not continuous or easily reproducible.
- **IPA:** `/ˌɪntərˈmɪtənt/`
- **Synonyms:** sporadic, occasional, irregular
- **Antonyms:** constant, continuous, persistent
- **Collocations:** intermittent failure, intermittent timeout, intermittent connectivity issue

!!! failure "Avoid"
    The issue is coming sometimes.

!!! success "Say instead"
    - It’s an intermittent issue.

**Examples**

=== "Software-engineering"
    The hardest part is that the timeout is intermittent and only appears under mixed traffic.

=== "Stakeholder"
    We’re treating this as high priority because the issue is intermittent, which makes it harder to detect and reproduce.

### 2. Mitigation

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A temporary or partial action that reduces impact or risk.
- **IPA:** `/ˌmɪtɪˈɡeɪʃən/`
- **Synonyms:** containment, risk reduction, workaround
- **Antonyms:** root fix, full resolution, permanent solution
- **Collocations:** short-term mitigation, mitigation plan, mitigation strategy, immediate mitigation

!!! failure "Avoid"
    We applied one workaround solution for now.

!!! success "Say instead"
    - We applied a short-term mitigation.

**Examples**

=== "Software-engineering"
    The immediate mitigation is to reduce batch size while we investigate the queue buildup.

=== "Stakeholder"
    We have a mitigation in place, but the permanent fix still needs validation.

### 3. Degradation

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** A drop in system quality, performance, reliability, or user experience.
- **IPA:** `/ˌdeɡrəˈdeɪʃən/`
- **Synonyms:** decline, deterioration, slowdown
- **Antonyms:** improvement, recovery, stabilization
- **Collocations:** performance degradation, service degradation, user-visible degradation

!!! failure "Avoid"
    There is performance down.

!!! success "Say instead"
    - We’re seeing performance degradation.

**Examples**

=== "Software-engineering"
    The new cache invalidation path caused a noticeable degradation in read latency.

=== "Stakeholder"
    Users may see some degradation during peak traffic, but the service remains available.

### 4. Resilient

<span class="fe-badges"><span class="fe-badge fe-badge--vocabulary">Vocabulary</span><span class="fe-badge fe-badge--new">New</span></span>

- **Meaning:** Able to keep working or recover quickly after failure.
- **IPA:** `/rɪˈzɪliənt/`
- **Synonyms:** robust, fault-tolerant, durable
- **Antonyms:** fragile, brittle, failure-prone
- **Collocations:** resilient architecture, resilient system, resilient service, resilient design

!!! failure "Avoid"
    The system should be strong for failures.

!!! success "Say instead"
    - The system should be more resilient to failures.

**Examples**

=== "Software-engineering"
    We need a more resilient retry strategy so one slow dependency doesn’t overload the entire pipeline.

=== "Stakeholder"
    This work makes the platform more resilient during dependency failures and traffic spikes.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| “The issue is coming sometimes.” | “The issue is intermittent.” | More precise and professional. |
| “We are checking on priority.” | “We’re treating this as high priority.” | Sounds natural and ownership-driven. |
| “Please do the needful.” | “Could you take the next step on this?” | Clearer and less old-fashioned. |
| “The server is not responding properly.” | “The service is returning elevated errors.” | More specific and incident-ready. |
| “We will update once we get the root cause.” | “We’ll share an update once we understand the root cause.” | More polished and less abrupt. |
| “There is slowness in the system.” | “We’re seeing increased latency.” | Uses engineering-specific language. |
| “We have taken one workaround.” | “We’ve applied a temporary mitigation.” | More credible in incident communication. |
| “Kindly wait for some time.” | “Please give us a little time to investigate.” | More natural and respectful. |
| “This issue is happening from yesterday.” | “This issue has been happening since yesterday.” | Correct tense and phrasing. |
| “We reverted back the change.” | “We reverted the change.” | Avoids redundant “back.” |

## Speaking Practice

Answer these ALOUD. Keep each answer to 20–40 seconds. Do not over-explain. Sound like a senior engineer giving a crisp update.  

Meeting questions  
Incident triage:  
“The service is showing elevated latency. What would you say in the first five minutes of the incident call?”  
Force in: stop the bleeding, mitigation  

Debugging discussion:  
“You have three possible causes: network, database, and a recent config change. How would you explain your investigation plan?”  
Force in: rule out, dig into  

Release decision:  
“A deployment is scheduled, but the team is still investigating a production issue. What would you recommend?”  
Force in: hold off on, the blast radius  

Presentation questions  
Reliability update:  
“Explain to leadership what happened without sounding defensive.”  
Force in: degradation, mitigation  

Architecture improvement:  
“Explain how you would redesign the system to handle dependency failures better.”  
Force in: resilient, under the hood  

Post-incident review:  
“Summarize what the team learned from the incident.”  
Force in: intermittent, rule out  

Leadership-discussion questions  
Stakeholder pressure:  
“A stakeholder asks for a fixed ETA before the root cause is known. What do you say?”  
Force in: dig into, mitigation  

Risk communication:  
“Your manager asks whether this can happen again. How do you answer honestly but confidently?”  
Force in: resilient, the blast radius  

Go/no-go call:  
“You need to recommend delaying a release. How do you phrase it diplomatically?”  
Force in: hold off on, degradation  

## Output Correction

No MY_ANSWERS were provided.  

For next session, write or speak 2 sentences using today’s expressions. Try these patterns:  

Use stop the bleeding + mitigation in an incident update.  
Use hold off on + blast radius in a release-risk discussion.  
Example structure:  

“For now, I’d recommend we ___ because . Once we , we can ___.”  

Tomorrow, I’ll correct your sentences at a C2 level for tone, register, concision, and naturalness.  

!!! tip "Tomorrow's preview"
    Next topic: Sprint planning — focus on negotiating scope and timelines without sounding negative.

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| Stop the bleeding | Idiom | Limit damage before full fix | new |
| Under the hood | Idiom | Inside the implementation details | new |
| The blast radius | Idiom | Scope of failure impact | new |
| Rule out | Phrasal verb | Eliminate a possible cause | new |
| Dig into | Phrasal verb | Investigate something in detail | new |
| Hold off on | Phrasal verb | Delay until more clarity | new |
| Intermittent | Vocabulary | Irregular and not continuous | new |
| Mitigation | Vocabulary | Action that reduces impact | new |
| Degradation | Vocabulary | Drop in system quality | new |
| Resilient | Vocabulary | Recovers well from failure | new |
