---
name: Use Case Generator
description: Discover and evaluate AI use cases from real workplace signals — meetings, Slack, email, and team conversations. Scans Granola meeting notes, Slack channels, and Gmail to surface pain points and automation opportunities, then evaluates each through the DVFR framework (Desirability, Viability, Feasibility, Responsibility). Generates personal use cases (for the individual's role) and department/strategic objective use cases. Output is saved as a shareable markdown doc and sent via Slack DM. Triggers include "find use cases", "generate use cases", "use case for [department]", "what should we automate", "AI opportunities", "where can AI help", "use case scout", or any request to identify AI automation opportunities.
---

# Use Case Generator

Discover AI use cases from what people are *actually saying and struggling with* — not hypothetical department tasks. Scan real signals from meetings, Slack, and email, generate evidence-based use cases, and evaluate each through the GenAI starting criteria and a streamlined DVFR framework before presenting them.

---

## Phase 0: Get to Know the User

Before doing anything else, gather context about who is using this skill. Ask the user:

1. **Name and role** — "What's your name and job title?"
2. **Department/function** — "What department or function are you in?" (e.g., Marketing, Engineering, Product, Design, Finance, People/HR, Customer Support, Customer Success, Legal, CommOps, Sales, Data Science)
3. **Strategic objectives** — "Are you part of any cross-functional strategic objectives?" (e.g., Demand Generation, Customer Retention, Platform Reliability, Pro Quality). If they're unsure, skip this.
4. **Top Slack channels** — "What are your 3-5 most-used Slack channels?" (These will be the primary channels scanned for signals.)
5. **Biggest workflow pain points** — "Off the top of your head, what are 1-2 things in your day-to-day that feel repetitive, manual, or slow?" (Optional — helps seed the scan.)

Store these answers and use them to personalize the entire workflow.

---

## Tool Stack

Thumbtack employees have access to a strong AI tool stack. When evaluating feasibility, assume these are available:

- **Gemini Enterprise** — Google Workspace-integrated AI (Docs, Sheets, Slides, Gmail, Meet)
- **ChatGPT Enterprise** (includes Codex) — general assistant, code generation, analysis
- **Claude Enterprise** — includes Claude Chat, Claude Code, and Cowork (collaborative AI workspace)
- **Granola** — meeting intelligence (company-wide)
- **Slack** — communication + unstructured data source
- **Agent builders:** Glean (~45+ users, enterprise search + agents) and Credal (BigQuery connected, agent builder)
- **Developer tools:** GitHub Copilot, Claude Code, Codex

Only flag feasibility concerns if something requires a tool or data source that genuinely doesn't exist yet.

---

## Workflow

### Mode Detection

Check the user's request to determine the mode:

- **Full scan** (no department/objective specified): Run all sources, generate personal + department/objective use cases
- **Department/objective deep-dive** (specified): Focus signal collection on that area, include a targeted Granola query, generate use cases scoped to that department or strategic objective

---

### Phase 1: Signal Collection

Collect signals from multiple sources in parallel. The goal is to find pain points, repetitive work, manual processes, workarounds, and "I wish..." moments.

#### 1A. Meeting Notes (always)

First check if `~/assistant/context/meeting-digest.md` exists. If it does, read it.

If it doesn't exist, use `query_granola_meetings` to query the user's recent meetings (last 30 days):
```
"What pain points, manual processes, repetitive tasks, open loops, and workflow frustrations have been mentioned in my recent meetings?"
```

Look for:
- Blockers and open loops
- Manual processes mentioned in passing
- Repeated complaints or friction
- "We need to figure out..." or "someone should..." statements
- Themes about what's working and what's not

If the meeting digest exists but is more than 5 days old, note this in the output and suggest running `/granola-sync` first.

#### 1B. User's Slack Channels (always)

Use `slack_search_public` to search the user's specified channels from the last 7-10 days. Run 3 targeted searches:

**Search 1 — Pain points and friction:**
```
"takes forever" OR "manual" OR "every week" OR "tedious" OR "copy paste" OR "workaround"
```

**Search 2 — AI wins and experiments:**
```
"saved time" OR "tried using" OR "AI helped" OR "automated" OR "built an agent" OR "prompt"
```

**Search 3 — Questions and blockers:**
```
"how do I" OR "is there a way" OR "anyone know" OR "struggling with" OR "can AI"
```

Scope these to the user's specified channels when possible.

#### 1C. Broader Public Slack (always in full scan, optional in deep-dive)

Use `slack_search_public` to search *all* public channels from the last 7-10 days:

**Search 4 — Org-wide pain points:**
```
"spreadsheet" OR "manual process" OR "bottleneck" OR "repetitive" OR "time-consuming"
```

**Search 5 — Org-wide wishes:**
```
"wish we could" OR "there should be" OR "would be nice" OR "if only" OR "dream tool"
```

These surface opportunities outside the user's usual channels.

#### 1D. Email (always in full scan)

Use `gmail_search_messages` to search recent email for workflow signals:
```
subject:(weekly report OR status update OR manual OR process OR recurring)
```
Scope to last 14 days, limit to 10-15 results.

Look for: recurring report requests, manual coordination threads, FYI chains that indicate someone is acting as a human router.

#### 1E. Targeted Granola Query (deep-dive only)

When a specific department or strategic objective is requested, run a direct query:
```
query_granola_meetings: "What pain points, manual processes, repetitive tasks,
and workflow frustrations have been mentioned in meetings related to [department/objective]
in the last 30 days?"
```

---

### Phase 2: Signal Processing

#### Step 1: Cluster signals into themes
Group related signals. A Slack complaint about "copying data between spreadsheets" and a meeting note about "manual reporting" might be the same underlying opportunity.

#### Step 2: Generate candidate use cases
For each cluster, draft a specific use case — not "use AI for reporting" but "auto-generate the weekly channel performance summary from BigQuery data using a Credal agent."

#### Step 3: Apply the GenAI Starting Criteria
Every candidate gets checked against four criteria. A use case should hit at least 3 of 4 to be recommended:

| Criterion | Pass when... |
|-----------|-------------|
| **Routine workflow** | It happens on a predictable cadence with consistent structure |
| **Examples available** | Past reports, templates, or historical data exist to learn from |
| **Underutilized data** | Data in Slack, BigQuery, docs, emails, or meetings isn't being systematically used |
| **Higher-value unlock** | Automating this frees someone for more strategic work |

Candidates hitting fewer than 3 go to the **Watch List**.

#### Step 4: Classify use cases

**Personal use cases** — things that help *this specific person* in their role. Based on their stated role and pain points from Phase 0.

**Department/function use cases** — grouped by the user's department (e.g., Marketing, Engineering, Product). These are opportunities that would benefit the broader team.

**Strategic objective use cases** (if applicable) — grouped by the user's cross-functional strategic objectives (e.g., Demand Generation, Customer Retention). These are opportunities that cut across departments and align to shared goals.

---

### Phase 3: DVFR Evaluation (Streamlined)

Every use case that passes the starting criteria gets a quick DVFR check. Use one line per dimension with a traffic light:

| Dimension | Question | Scoring |
|-----------|----------|---------|
| **Desirability** | Is there real evidence people want/need this? | 🟢 Multiple signals · 🟡 Inferred need · 🔴 No clear demand |
| **Viability** | Will it create measurable value? | 🟢 Clear time/quality savings · 🟡 Likely but hard to quantify · 🔴 Effort may exceed benefit |
| **Feasibility** | Can we build it with current tools? | 🟢 Prototype today · 🟡 Minor gaps (data connection, config) · 🔴 Missing infrastructure |
| **Responsibility** | Is it ethical and safe? | 🟢 Low risk, no sensitive data · 🟡 Needs guardrails or human review · 🔴 PII/bias/oversight concerns |

That's it — one emoji and a short phrase per dimension. No paragraphs.

---

### Phase 4: Output

#### 4A. Save the markdown doc

Save location:
- **Full scan:** `~/assistant/content/use-cases/YYYY-MM-DD-use-case-scout.md`
- **Department deep-dive:** `~/assistant/content/use-cases/YYYY-MM-DD-[department]-use-cases.md`
- **Strategic objective deep-dive:** `~/assistant/content/use-cases/YYYY-MM-DD-[objective]-use-cases.md`

#### 4B. Share via Slack DM

After saving, send the user a Slack DM with a summary and link to the doc. Use `slack_search_users` to find their user ID by name, then `slack_send_message` to DM them.

The DM should include:
- A brief summary (top 3 recommendations in one-liner format)
- The full markdown doc contents (formatted for Slack readability)

#### Output Template

```markdown
# AI Use Case Scout — [Date]

**Sources:** [N] meetings scanned · [N] Slack threads · [N] emails scanned
**Generated for:** [Name], [Role] — [Department]
[If applicable:] **Strategic objectives:** [Objective 1], [Objective 2]

---

## Signal Summary

[Top 5-8 pain points and patterns discovered across all sources. Each with attribution — e.g., "from #channel-name", "from 1:1 with X via meeting notes", "from email thread about Y".]

---

## Personal Use Cases

### 1. [Use Case Title]

**Signal:** [Source and what triggered this]
**The challenge:** [One sentence — what's painful]
**The approach:** [2-3 sentences — specific, names the tools]

**Starting criteria:** Routine ✓ · Examples ✓ · Underutilized data ✓ · Higher-value unlock ✓ (3/4)

**DVFR:** Desirability 🟢 multiple signals · Viability 🟢 clear time savings · Feasibility 🟢 prototype today · Responsibility 🟢 low risk

**Try this:** [Actionable first step — a prompt to try, a tool to set up, or a prototype to build]

---

## [Department Name] Use Cases

### 1. [Use Case Title]

[Same structure as personal use cases]

---

## [Strategic Objective Name] Use Cases (if applicable)

### 1. [Use Case Title]

[Same structure as personal use cases]

---

## Top 5 Recommendations

1. **[Use Case Title]** ([Personal/Department/Objective]) — [One sentence on why to prioritize. Reference signal strength and DVFR.]
2. ...

---

## Watch List

- **[Title]** — [Why not ready yet] — [What would need to change]

---

*Generated by Use Case Scout · Sources: Granola, Slack, Gmail*
```

#### Slack-Ready Format (for sharing individual use cases in channels)

When asked to format a use case for a Slack channel:

```markdown
🎯 **AI Use Case: [Department/Objective]**

**The challenge:** [One sentence — rooted in a real signal]
**The approach:** [2-3 sentences — specific tools, specific steps]
**The impact:** [Time saved, quality improved, consistency gained]
**DVFR:** Desirability 🟢 · Viability 🟢 · Feasibility 🟢 · Responsibility 🟡 (needs human review)

**Try this prompt:**
"[Copy-paste ready prompt tailored to this use case]"

#[Department] #AIatWork
```

---

## Quality Principles

- **Rooted in real signals** — every use case traces back to something someone actually said or did
- **Specific enough to try** — not "use AI for marketing" but "use Claude to draft A/B test variants for the spring campaign, using last quarter's top performers as examples"
- **Honest about effort** — acknowledge when something takes practice or iteration
- **Inclusive of skill levels** — frame so anyone could attempt it, regardless of technical background (you don't need to be technical to build with AI)
- **Evidence over assumption** — no signal backing = watch list, not recommendations

---

## Error Handling

- **Meeting digest missing:** Use `query_granola_meetings` directly as fallback. If that also fails, note it and continue with other sources.
- **Slack search returns no results:** Broaden to 14 days and retry with fewer keywords. If still nothing, note it and continue.
- **Gmail not connected:** Skip email, note it in the sources line.
- **No signals for a department/objective:** Say so honestly. Suggest the user check in with that team directly.
- **Too many signals:** Cap at the top 20 most relevant (by recency and specificity).
