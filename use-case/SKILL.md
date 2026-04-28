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
6. **Pain points you've been trying to solve** — "Are there any pain points or challenges you've been actively trying to solve recently — even if you haven't found a good solution yet?" (This surfaces problems the user is already aware of and motivated to fix, which often make the best use case candidates.)
7. **Wish-list items** — "Is there anything you wish you could do in your role but just don't have the time for?" (This uncovers latent opportunities — things the user would do if the cost were lower. These often point to high-value automation or AI-assist use cases.)

Store these answers and use them to personalize the entire workflow.

---

## Tool Stack

Thumbtack employees have access to a strong AI tool stack. Default to **Claude Enterprise + Cowork** for most use cases — it covers the majority of what people actually need. When evaluating feasibility, assume these are available:

- **Claude Enterprise** (Claude Chat, Claude Code, Cowork) — *default tool for most use cases*; covers chat, drafting, analysis, agentic workflows, and code
- **Gemini Enterprise** — when Google Workspace integration is needed (Docs, Sheets, Slides, Gmail, Meet)
- **ChatGPT Enterprise** (incl. Codex) — alternative general assistant
- **Granola** — meeting intelligence (company-wide)
- **Slack** — communication + unstructured data source
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

Use `query_granola_meetings` to query the user's recent meetings (last 30 days, or whatever timeframe the user specified):
```
"What pain points, manual processes, repetitive tasks, open loops, and workflow frustrations have been mentioned in my recent meetings?"
```

Look for:
- Blockers and open loops
- Manual processes mentioned in passing
- Repeated complaints or friction
- "We need to figure out..." or "someone should..." statements
- Themes about what's working and what's not

#### 1B. User's Slack Channels (always)

Query Slack live every run — there is no cached digest. Use `slack_search_public` to search the user's specified channels from the last 7-10 days. Run 3 targeted searches:

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

Use `search_threads` (Gmail MCP) to search recent email for workflow signals:
```
subject:(weekly report OR status update OR manual OR process OR recurring) newer_than:14d
```
Limit to 10-15 results. Use `get_thread` to pull body content for any threads that look promising.

Look for: recurring report requests, manual coordination threads, FYI chains that indicate someone is acting as a human router.

> **If the user names additional connectors at intake** (Calendar, Drive, Linear, Jira, Confluence, Coda, Notion, etc.), include them as additional signal sources using the appropriate connected MCP tools.

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
For each cluster, draft a specific use case — not "use AI for reporting" but "draft the weekly channel performance summary in Cowork using last quarter's reports and the latest data export as context."

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
| **Feasibility** | Can we build it with current tools? | 🟢 Buildable today in Claude Chat, Cowork, or a short Claude Code script · 🟡 Needs Gemini/ChatGPT Workspace integration or non-trivial setup · 🔴 Missing infrastructure or data access |
| **Responsibility** | Is it ethical and safe? | 🟢 Low risk, no sensitive data · 🟡 Needs guardrails or human review · 🔴 PII/bias/oversight concerns |

That's it — one emoji and a short phrase per dimension. No paragraphs.

---

### Phase 4: Output

Before generating output, ask the user (or read from their request):

1. **Where to save?** Accept any path the user provides. If they don't specify, ask. Suggest the current working directory or `~/Documents/` as a fallback. **Do not hardcode** any specific directory — most users won't have it.
2. **What format?** Offer:
   - **Full markdown doc** (default if unsure) — uses the Output Template below
   - **Slack-ready post** — uses the Slack-Ready Format below
   - **Google Doc** — created via the Workspace tooling (Gemini / Drive MCP)
   - **Slack DM only with TL;DR** — no saved file; top 3 recommendations DM'd to the user

Filename suggestion when saving markdown: `YYYY-MM-DD-use-case-scout.md`, `YYYY-MM-DD-[department]-use-cases.md`, or `YYYY-MM-DD-[objective]-use-cases.md`.

#### 4A. Save the doc

Save to the user-specified location in the chosen format.

#### 4B. Share via Slack DM (optional)

If the user wants a Slack DM, use `slack_search_users` to find their user ID by name, then `slack_send_message`. The DM should include a brief summary (top 3 recommendations as one-liners) and a pointer to the saved file (or the full content if no file was saved).

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

**DVFR:** Desirability 🟢 multiple signals · Viability 🟢 clear time savings · Feasibility 🟢 buildable in Cowork today · Responsibility 🟢 low risk

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

## Gotchas

This skill runs against *the individual user's* connected tools, and configurations vary person to person. Defaults must be opinionated where reasonable, and overridable everywhere.

- **Don't assume any specific channel list, calendar, dept, or naming convention.** Pull from Phase 0 answers (and auto-memory if available).
- **Pick sensible defaults when the user is silent:**
  - No channel list given → query the user's DMs and most recent active public channels via `slack_search_public`
  - No save path given → ask the user. If they want a quick default, suggest the current working directory or `~/Documents/`. Never hardcode a path that assumes a directory like `~/assistant/content/use-cases/` exists.
  - No output format given → full markdown doc + Slack DM TL;DR
  - No timeframe given → 30 days for meetings, 7-10 days for Slack, 14 days for Gmail
- **Degrade gracefully when a connector returns nothing.** Note it in the Sources line and continue rather than failing the run.
- **Honor any non-default tool the user names** (e.g. "use Linear instead of Jira", "save to Notion") by routing to the appropriate connected MCP.

The point: this skill is a personal tool, not a one-size workflow. Assume Gmail, Slack, and Granola are connected via Claude Desktop — if a user is running this skill, those should be live.

## Error Handling

- **Slack search returns no results:** Broaden to 14 days and retry with fewer keywords. If still nothing, note it and continue.
- **Granola returns no meetings:** Note it and continue with other sources.
- **No signals for a department/objective:** Say so honestly. Suggest the user check in with that team directly.
- **Too many signals:** Cap at the top 20 most relevant (by recency and specificity).
