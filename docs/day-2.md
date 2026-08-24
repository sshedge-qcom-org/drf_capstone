# Day 2 — Code reviews

**Focus theme:** Giving clear, diplomatic feedback in code/Gerrit reviews  
**Difficulty:** Standard C1  
**Mode:** Lite  
**Date:** 2026-08-20

*Code Review English for Senior Engineers*

## Professional Idioms

### 1. Raise a red flag

- **Meaning:** Point out a serious concern or possible risk.
- **IPA:** `/reɪz ə red flæɡ/`
- **Formality:** Neutral

!!! failure "Avoid"
    I have one doubt on this implementation.

!!! success "Say instead"
    - I want to raise a red flag about this implementation.

**Examples**

- *Engineering:* This shared mutable state raises a red flag because it can behave unpredictably under concurrency.
- *Meeting:* I don’t want to block the change unnecessarily, but I do want to raise a red flag on the retry behavior.
- *Presentation:* One issue that raised a red flag during testing was the spike in memory usage under sustained load.

### 2. Get to the bottom of something

- **Meaning:** Find the real cause of a problem, not just the symptom.
- **IPA:** `/ɡet tə ðə ˈbɑːtəm əv ˈsʌmθɪŋ/`
- **Formality:** Neutral

!!! failure "Avoid"
    We need to find the root exactly.

!!! success "Say instead"
    - We need to get to the bottom of why this regression happens.

**Examples**

- *Engineering:* Before we change the scheduler logic, let’s get to the bottom of why the timeout only appears on large payloads.
- *Meeting:* We shouldn’t guess here. Let’s get to the bottom of the failure pattern using logs and traces.
- *Presentation:* The team got to the bottom of the issue by correlating deployment timing with request latency.

### 3. A moving target

- **Meaning:** Something that keeps changing, making planning or implementation difficult.
- **IPA:** `/ə ˈmuːvɪŋ ˈtɑːrɡɪt/`
- **Formality:** Neutral

!!! failure "Avoid"
    The requirement is changing again and again.

!!! success "Say instead"
    - The requirement is becoming a moving target.

**Examples**

- *Engineering:* The API contract has become a moving target, so it’s risky to build the client integration this sprint.
- *Meeting:* If the acceptance criteria remain a moving target, we’ll keep reworking the same patch.
- *Presentation:* To reduce churn, we stabilized the interface first because the requirements had become a moving target.

## Phrasal Verbs

### 1. Call out

- **Meaning:** Explicitly mention something important, often a concern, assumption, or risk.
- **IPA:** `/kɔːl aʊt/`

!!! failure "Avoid"
    I want to highlight out one issue.

!!! success "Say instead"
    - I want to call out one issue.

**Examples**

- *Technical-discussion:* I want to call out that this design assumes the cache is always warm.
- *Code-review:* Can you call out this ownership assumption in the commit message?
- *Leadership:* We should call out the dependency on the platform team before committing to the date.

### 2. Clean up

- **Meaning:** Improve clarity, remove unnecessary code, or make something easier to maintain.
- **IPA:** `/kliːn ʌp/`

!!! failure "Avoid"
    Please make the code cleanly.

!!! success "Say instead"
    - Please clean up this error-handling path.

**Examples**

- *Technical-discussion:* We should clean up the boundary between validation and business logic.
- *Code-review:* Could you clean up the duplicated null checks before landing this?
- *Leadership:* We need time next sprint to clean up the migration scripts before handing this over.

### 3. Follow through

- **Meaning:** Complete something properly after starting or promising it.
- **IPA:** `/ˈfɑːloʊ θruː/`

!!! failure "Avoid"
    Please do the remaining follow-up completely.

!!! success "Say instead"
    - Please follow through on the remaining review comments.

**Examples**

- *Technical-discussion:* If we agree to add metrics, we need to follow through with dashboards and alerts.
- *Code-review:* Thanks for addressing the main issue. Please follow through on the test coverage comment as well.
- *Leadership:* We need owners who can follow through across design, implementation, rollout, and support.

## C1/C2 Vocabulary

### 1. Rationale

- **Meaning:** The reasoning behind a decision.
- **IPA:** `/ˌræʃəˈnæl/`
- **Synonyms:** reasoning, justification, basis
- **Antonyms:** guess, impulse, assumption
- **Collocations:** design rationale, technical rationale, clear rationale, document the rationale

!!! failure "Avoid"
    Please mention the logic why you did this.

!!! success "Say instead"
    - Please document the rationale for this approach.

**Examples**

- *Software-engineering:* The implementation is fine, but the rationale for choosing polling over events should be documented.
- *Stakeholder:* The rationale is that this approach reduces operational risk without delaying the release.

### 2. Regression

- **Meaning:** A new bug or broken behavior introduced by a change.
- **IPA:** `/rɪˈɡreʃən/`
- **Synonyms:** breakage, reintroduced bug, unintended failure
- **Antonyms:** fix, improvement, stabilization
- **Collocations:** performance regression, functional regression, regression test, regression risk

!!! failure "Avoid"
    This change created one issue again.

!!! success "Say instead"
    - This change introduced a regression.

**Examples**

- *Software-engineering:* The patch fixes the crash but introduces a regression in the reconnect flow.
- *Stakeholder:* We delayed the rollout because we found a regression in a high-traffic path.

### 3. Maintainable

- **Meaning:** Easy to understand, change, debug, and extend over time.
- **IPA:** `/meɪnˈteɪnəbəl/`
- **Synonyms:** sustainable, readable, supportable, extensible
- **Antonyms:** brittle, messy, hard-coded, fragile
- **Collocations:** maintainable code, maintainable design, maintainable architecture, more maintainable approach

!!! failure "Avoid"
    This code is not looking good for future.

!!! success "Say instead"
    - This code may not be maintainable long term.

**Examples**

- *Software-engineering:* This version is shorter, but the explicit version is more maintainable for future owners.
- *Stakeholder:* We’re taking an extra day to make the solution maintainable, not just functional.

### 4. Edge case

- **Meaning:** A rare or unusual scenario that can still break the system.
- **IPA:** `/edʒ keɪs/`
- **Synonyms:** corner case, rare scenario, boundary condition
- **Antonyms:** common case, typical path, happy path
- **Collocations:** handle an edge case, miss an edge case, edge-case behavior, edge-case coverage

!!! failure "Avoid"
    This is a corner scenario which can come sometimes.

!!! success "Say instead"
    - This is an edge case we still need to handle.

**Examples**

- *Software-engineering:* The parser works for normal input, but it misses an edge case where the payload is empty.
- *Stakeholder:* The issue affects only an edge case, but it’s still important because it can block enterprise customers.

## Natural English Upgrade

| Common Indian corporate English | Natural international English | Why it's better |
| --- | --- | --- |
| “I have one doubt in this code.” | “I have a question about this code.” / “I have a concern here.” | “Doubt” often sounds like mistrust in US/UK workplace English. |
| “Please do the needful.” | “Could you take care of this?” / “Could you handle this?” | More natural, direct, and modern. |
| “Kindly check and confirm.” | “Could you review this and confirm?” | Less stiff; clearer action. |
| “This logic is not proper.” | “This logic looks fragile.” / “This may not handle all cases.” | More precise and less vague. |
| “Please revert on this comment.” | “Please respond to this comment.” | “Revert” does not mean “reply” in standard workplace English. |
| “I will update the same.” | “I’ll update it.” / “I’ll update the patch.” | “The same” sounds old-fashioned and unnatural. |
| “Can you explain me this?” | “Can you explain this to me?” | Correct verb pattern: explain something to someone. |
| “This issue is coming intermittently.” | “This issue happens intermittently.” / “We’re seeing this intermittently.” | More natural technical phrasing. |
| “I am having a blocker.” | “I’m blocked on this.” / “This is blocking me.” | More idiomatic for engineering status updates. |
| “The code is working fine.” | “The code works for the main path, but we should verify edge cases.” | More senior-sounding and less overconfident. |

## Speaking Practice

Instruction: Answer these ALOUD. Keep each answer to 30–45 seconds. Force the listed expressions into your answer naturally.  

Meeting questions  
A teammate proposes merging a risky patch late in the release cycle. What do you say?  
Force: raise a red flag, regression  

The team keeps changing the API requirements during implementation. How do you respond?  
Force: a moving target, rationale  

A bug appears only under rare timing conditions. How would you guide the debugging discussion?  
Force: get to the bottom of, edge case  

Presentation questions  
Present why your team chose a slightly more verbose implementation.  
Force: maintainable, rationale  

Explain why you paused a rollout after testing.  
Force: regression, call out  

Explain how the team improved code quality before release.  
Force: clean up, follow through  

Leadership-discussion questions  
Your manager asks why the review is taking longer than expected. What do you say?  
Force: edge case, maintainable  

A stakeholder wants a quick workaround. How do you respond professionally?  
Force: raise a red flag, follow through  

You need another team to clarify an unstable interface. What do you say?  
Force: a moving target, call out  

## Output Correction

No MY_ANSWERS were provided today.  

For next session, write or speak 2 sentences using at least 4 of today’s expressions. Example topics:  

A Gerrit review where you disagree with the implementation.  
A design discussion where requirements keep changing.  
Use any of these: raise a red flag, get to the bottom of, a moving target, call out, clean up, follow through, rationale, regression, maintainable, edge case.  

I’ll correct them at C2 level next time.  

## Tracker

| Expression | Type | 5-word meaning | Status |
| --- | --- | --- | --- |
| Raise a red flag | Idiom | Point out serious potential risk | new |
| Get to the bottom of something | Idiom | Find the real underlying cause | new |
| A moving target | Idiom | Something keeps changing over time | new |
| Call out | Phrasal verb | Explicitly mention important concern | new |
| Clean up | Phrasal verb | Improve clarity and remove mess | new |
| Follow through | Phrasal verb | Complete promised actions properly | new |
| Rationale | Vocabulary | Reasoning behind a decision | new |
| Regression | Vocabulary | New bug from a change | new |
| Maintainable | Vocabulary | Easy to change over time | new |
| Edge case | Vocabulary | Rare scenario needing handling | new |
