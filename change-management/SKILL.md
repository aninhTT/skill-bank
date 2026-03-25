---
name: change-management
description: >
  Builds AI change management plans for two Thumbtack audiences. For AI Champions:
  generates a 60-day functional enablement plan after AI Champions Day, diagnoses
  the function's current state, and recommends the right team activation format
  (offsite, session, or cadence). For Managers/Leaders: builds a structured
  org-level change management plan using Thumbtack's 3-pillar framework (Get
  Personally Fluent, Facilitate the Learning Chain, Make Explicit Space) and AI
  Expectations framework. Both paths optionally gather signals from Granola/Slack/
  Drive, synthesize those signals back to the person for approval before building,
  then recommend tools from the approved stack and matching learning offerings.
  Both paths close by connecting cross-functional peers via Slack intro.
  Trigger phrases: "change management plan", "enablement plan", "AI champion plan",
  "leading AI change", "cascade AI", "make space for AI", "champion enablement",
  "explorer operator builder", "tackstart tackshift", "functional enablement".
version: 1.0
---

# Change Management Skill

## Purpose
This skill helps two Thumbtack audiences build real, specific AI change management plans — not generic advice, but something grounded in where their function actually is today.

---

## ⚠️ Common Pitfalls — Read Before Building the Plan

1. **Don't skip the preview step.** It's tempting to jump to the formatted plan once signals are collected. Always show Phase 2.7 first — users often want to redirect before seeing the full output.

2. **Don't make the plan generic.** If you don't have enough signal to name specific use cases, tools, or team behaviors, go back and ask. A plan that could apply to any team at any company is not useful here.

3. **Don't assign the wrong activation format.** Read the team's maturity and signal carefully before routing to a format. Match the format to where the team actually is, not where you'd like them to be.

4. **Don't skip scheduling.** If the user doesn't explicitly decline, always offer it. Plans without reminders rarely get executed.

5. **Don't assume Slack = DM.** Ask where Slack reminders should go. Leaders often want messages going to their team or a channel, not just themselves.

6. **Don't treat the three pillars as equal.** For Leaders, always identify which pillar is most at risk based on signals and lead with that in the plan. Pillar 1 (personal fluency) is almost always the real blocker even when people think it's Pillar 3.

7. **Don't over-schedule.** If the user's calendar is already packed, recommend fewer, higher-impact milestones rather than loading every week with reminders.

8. **Don't ignore partial or missing signals.** If Granola, Slack, or Drive searches come back empty, note it explicitly and adjust confidence level in the plan. Don't present the plan as fully grounded when it isn't.

---

## Phase 0: Identify Role

Ask:

> "Are you an **AI Champion** building an enablement plan for your function, or a **Manager/Leader** building a change management plan for your org?"

Branch based on their answer.

---

## Branch A: AI Champions

### Phase 1 — Intake

> 💡 **Tip:** For faster input, try voice dictating your answers. On Mac, press `Fn Fn` (double-tap Function key) to start dictation anywhere. On iPhone/iPad, tap the mic on the keyboard. You don't need to be precise — rough, spoken answers work great.

Ask all questions in a single message. Note that the user doesn't need to answer every question — even rough or partial answers help. The more context they share, the more specific the plan will be. If their answers are too sparse to build a meaningful plan (e.g., function name only with no maturity or barriers), ask 1–2 targeted follow-up questions to fill the most critical gaps before proceeding to signal collection.

> "Great — let's build your functional enablement plan. Share whatever you can for each question below — even rough answers help. Voice dictate if it's faster, and skip anything you're unsure about.
>
> A few questions to get started:
>
> 1. **What's your function?** (e.g., Product, People, Finance, Legal, Marketing)
>
> 2. **Describe where your function is on the AI journey right now — be specific.** A few prompts:
>    - What percentage of your team is actively using AI tools in their real work?
>    - Who's doing interesting things? Who hasn't started?
>    - What are people trying? What's working or not?
>    - Is there a specific workflow or problem the team keeps hitting?
>
> 3. **What feels hardest about AI adoption in your function right now?** (e.g., mindset/fear, no time or space, unclear priorities, technical barriers)
>
> 4. **What are your top 2–3 priorities for your function over the next 60 days?**
>
> 5. **Do you have any upcoming team events, offsites, or calendar space that could anchor an AI session?** (This helps match you to the right format)
>
> 6. **Have you already started building an enablement plan, or are you starting from scratch?**"

---

### Phase 2 — Signal Collection

Ask before searching:

> "Would you like me to search Slack, Granola meeting notes, or Google Drive to find context that can make your plan more specific? If yes, what should I look for? (e.g., recent AI discussions in your function, notes from Champions Day, any existing plan drafts)"

If yes → run only what they confirm. Sensible defaults if they say "go ahead":
- **Granola**: `query_granola_meetings("AI champions [function] enablement")` + `query_granola_meetings("[function] AI adoption priorities")`
- **Slack**: `slack_search_public_and_private("[function] AI")` + `slack_search_public("AI champions enablement [function]")`
- **Google Drive**: `google_drive_search("[function] enablement plan AI")` — if Drive MCP unavailable, use `gmail_search_messages("[function] AI enablement")` as proxy and note the substitution

---

### Phase 2.5 — Signal Synthesis + Approval

After running any searches, synthesize findings and share back **before building the plan**:

> "Here's what I found before building your plan. Let me know if anything looks off, is missing, or if I should search for something different.
>
> **Function context (from your intake):**
> [2–3 sentence summary of their function's maturity level, biggest blocker, key priorities]
>
> **Signals from [Granola / Slack / Drive] (if searched):**
> - [Source]: [Key signal or theme found]
> - [Source]: [Next signal]
>
> **What I didn't find / gaps:**
> [e.g., "No Granola meetings matched — plan will be based on intake only" or "Drive search unavailable; used Gmail as proxy"]
>
> **My read on where your function is:**
> [1–2 sentence honest diagnosis — e.g., "Your function sounds like it's in early Explorer territory, with a few individuals trying things but no shared momentum yet. The main barrier seems to be time + unclear priorities, not mindset."]
>
> Does this match your read? Anything to add, correct, or search for before I build the plan?"

**Wait for confirmation or corrections before proceeding.**

---

### Phase 2.6 — Diagnose → Route to Activation Format

Based on intake + confirmed signals, determine the right team activation format:

| Signal | Recommended format |
|-------|-------------------|
| Upcoming offsite / team day available | **AI Day** (DGLT full-day or EFLT 3.5h — see `references/offsite-templates.md`) |
| Team mostly new to AI, cold-start or mindset barrier | **Show, Don't Tell** (30–60 min) → then TackStart |
| Mixed team, specific workflow pain to solve | **AI Workflow Mapping Session** (60 min) |
| Mixed team, want energy + rapid ideas | **AI Brainstorm / Mini Hackathon** (~2 hrs) |
| No bandwidth for a session; needs ongoing rhythms | **Weekly AI Moment** cadence from Manager Playbook |
| Senior leadership function (Director+) | **EFLT format** (3.5h, hands-on build) or **SLT format** (full day) |
| Individuals hitting specific walls | **Office Hours / Buddy Pairings** |

---

### Phase 2.7 — Plan Preview + Output Format

Before building the full plan, share a substantive preview with **at least 4–5 concrete recommendations** grounded in what you've learned. This should be detailed enough for the user to redirect before the full formatted plan is generated.

> "📋 Here's my recommended approach — tell me what to adjust before I build the full plan:
>
> **Recommended activation format:** [e.g., Show/Don't Tell → Workflow Mapping]
> **Why:** [2–3 sentences grounded in signals and intake]
>
> **Top recommendations:**
> 1. [Specific, actionable recommendation with brief rationale]
> 2. [Specific, actionable recommendation with brief rationale]
> 3. [Specific, actionable recommendation with brief rationale]
> 4. [Specific, actionable recommendation with brief rationale]
> 5. [Specific, actionable recommendation with brief rationale]
>
> **Suggested learning path:** [Explorer → TackStart / Operator → TackShift / Builder → targeted sessions]
> **Plan structure:** 60-day sprint across 3 phases
> **Top use cases to pilot:** [3 specific, function-grounded use cases — not generic]
>
> Does this direction look right? Reply **yes** to generate the full plan, or tell me what to adjust.
>
> Also — what format would you like your plan in?
> - **Markdown** (default) — saved to ~/assistant/content/change-management/
> - **Word Doc (.docx)** — formatted document you can edit and share
> - **Slides (.pptx)** — deck version of the plan
>
> Leave blank for Markdown."

**Wait for confirmation (and any adjustments) before proceeding. Also note the output format choice.**
- Markdown → write to file system (default behavior)
- DOCX → invoke the `docx` skill
- PPTX → invoke the `pptx` skill (use Thumbtack internal template per CLAUDE.md)

---

### Phase 3 — Build 60-Day Enablement Plan

**Reference files to use:**
- `references/tool-stack.md` → filter to tools appropriate for the function's maturity level
- `references/learning-offerings.md` → map to stage (Explorer = TackStart; Operator = TackShift; Builder = targeted sessions)
- `references/ai-champions-context.md` → frame expectations + Amie's support model
- `references/ai-expectations.md` → ground in company-wide expectations
- `references/team-experimentation.md` → cadence ideas + coaching-by-modes
- `references/offsite-templates.md` → if a session or offsite format is recommended

**Stage → Tools + Offerings:**
| Stage | Primary Tools | Learning Offering |
|-------|--------------|-------------------|
| Explorer | Claude Chat, ChatGPT, Gemini in Workspace, NotebookLM, Slack AI | TackStart (30 Days of Exploring AI) — cohorts 3/16, 3/30, 4/13 |
| Operator | Claude Projects + Artifacts, Granola + custom recipes, ChatGPT Data Analysis/Canvas, Gemini in Sheets/Docs | TackShift (30 Days of Operating Better with AI) |
| Builder | Claude Code/Cowork, Codex, ChatGPT Agents/GPTs, Gemini AI Studio, Enterprise Agent Builder (Credal — pilot) | Targeted learning sessions: agent-building, Claude Code; #ai-lab for sharing |

**Save output to:** `~/assistant/content/change-management/YYYY-MM-DD-[function]-enablement-plan.md`

**Output structure:**

```
# [Function] AI Enablement Plan — [Name]
Generated: [date]

## Function Diagnosis
[Team maturity level + main blocker + what this means for the plan approach.
Be specific and honest — not cheerful, not alarmist.]

## Situation Summary
[Key signals from intake + any Slack/Granola context gathered.
Note which sources were searched and what was found.]

## What Thumbtack Expects
[Brief, direct anchor to the 4 engagement expectations from ai-expectations.md:
be AI-first in consequential work, own outcomes, stay at the frontier, share openly]

## Recommended Tools for Your Function's Stage
[From tool-stack.md, filtered. Specific names, what they're for, how to access.
Don't list everything — pick the 3-5 most relevant given their stage and function.]

## Learning Offerings to Sign Up For
[Specific programs from learning-offerings.md matched to their stage.
Include cohort dates where relevant. Be direct — "Sign up for TackStart.
Next cohort is 3/30. Here's what it covers."]

## Top 3 Use Cases to Pilot
[Ranked. Tailored to their function + priorities. Specific, not generic.
"Use Claude to summarize meeting notes" is not a use case.
"Use Granola + Claude Projects to auto-draft the weekly Finance leadership
update from call notes" is a use case.]

## 60-Day Action Plan
### Weeks 1–2: Foundation
[What to set up, what to sign up for, first thing to try. One or two specific actions.]

### Weeks 3–4: First Real Pilots
[Run the first use case. Document what worked and what didn't. Share in #ai-lab.]

### Weeks 5–8: Expand & Cascade
[Add a second use case. Begin enabling the team. Prepare for the session with Amie.]

## Recommended Team Activation Format
[The format chosen from the routing table above. Why this one for their context.

If a session or offsite format: include the adapted agenda from offsite-templates.md
or team-experimentation.md, customized for their function and team size.
Example: "Given that you have an offsite on April 15 and your team is mostly in
early Explorer territory, I'd recommend running the DGLT-style AI Day format.
Here's a customized agenda for a [N]-person [Function] team..."]

If a cadence: include specific weekly/monthly rhythm ideas from team-experimentation.md.]

## Coaching Your Team Through This
[From coaching-by-modes in team-experimentation.md:
- If team is mostly Explorer: what that looks like, coach moves, how to reduce cold-start friction
- If mixed: how to support both groups
- If relevant blockers surfaced (e.g., "I don't have time", "I'm not technical"):
  include the appropriate talk track from team-experimentation.md]

## Channels + Resources
- #ai-lab — share wins, before/afters, lessons, questions (make this a habit)
- #ai-resources — company updates, industry news
- AI Hub — start here for anything AI at Thumbtack
- Manager AI Playbook — go/manager-ai

## Amie's Support
Amie will set up time with each functional group to work through enablement
plans together. Your plan can adapt existing structure or be fully bespoke —
what matters is that it reflects your actual context.
```

---

### Phase 3.5 — Schedule Reminders

After the plan is saved, parse the 60-day action plan into key milestones and present them for the user to review and customize before scheduling anything.

> "📅 Here are the key milestones I pulled from your plan. Adjust timing, remove any, or add your own before I schedule them:
>
> 1. Week 1 — [First activation event] → [suggested date based on today]
> 2. Week 2 — [First use case pilot kickoff] → [suggested date]
> 3. Week 4 — [Mid-point check-in] → [suggested date]
> 4. Week 6 — [Second use case or iteration] → [suggested date]
> 5. Week 8 — [60-day retrospective + next quarter planning] → [suggested date]
>
> **Where should I send reminders?**
> - Google Calendar (creates a 30-min event per milestone)
> - Slack message — to yourself, a specific channel, or a team DM (let me know which)
> - Both
>
> What would you like to schedule, and where should the reminders go?"

**If Google Calendar selected:** Use `gcal_create_event` for each milestone with title `[AI] [Milestone name]`, 30-min duration, and the specific action from the plan as the description.

**If Slack selected:** Use `slack_schedule_message` to send a brief nudge on each milestone date. Ask the user for destination: DM to themselves (default), a specific channel, or a team DM (ask for member names). Content: the milestone action + reference to the saved plan.

**Confirm all scheduled items** and display a summary list.

---

### Phase 4 — Slack Connections

Ask:
> "Who should I loop together on this? I can send a Slack intro connecting you with cross-functional peers or others building AI enablement plans right now."

If they provide names → send a group DM:
> "Hey [names] 👋 Looping you together — you're each building AI enablement plans for your functions and I think there's real overlap worth connecting on. [Name] is leading this for [Function], [Name] for [Function]. Thought a quick conversation could be valuable."

Also send the completed plan to the champion as a Slack DM.

---

## Branch B: Managers/Leaders

### Phase 1 — Intake

> 💡 **Tip:** For faster input, try voice dictating your answers. On Mac, press `Fn Fn` (double-tap Function key) to start dictation anywhere. On iPhone/iPad, tap the mic on the keyboard. You don't need to be precise — rough, spoken answers work great.

Ask all questions in a single message. Note that the user doesn't need to answer every question — even rough or partial answers help. The more context they share, the more specific the plan will be. If their answers are too sparse to build a meaningful plan, ask 1–2 targeted follow-up questions to fill the most critical gaps before proceeding to signal collection.

> "Great — let's build your change management plan. Share whatever you can for each question below — even rough answers help. Voice dictate if it's faster, and skip anything you're unsure about.
>
> A few questions first:
>
> 1. **What's your function/org and how many direct reports do you have?**
>
> 2. **Where are you as a leader on the AI journey right now? Describe your own use — be honest and specific:**
>    - What tools are you using, and for what kinds of real work?
>    - Are you exploring (trying things out), operating (using AI regularly as part of how you work), or building (creating things for your team, redesigning workflows)?
>    - What's your relationship with the tools been like — energizing, uncertain, inconsistent?
>
> 3. **Describe where your direct reports and broader org are on the AI journey:**
>    - What percentage are actively using AI in their work?
>    - Who's leading? Who's lagging? What's in the way for those who haven't started?
>    - What signals are you seeing — enthusiasm, resistance, confusion?
>
> 4. **Pillar 1 — Get Personally Fluent:** What have you used AI for in the last 2 weeks? Be specific: what tool, what task.
>
> 5. **Pillar 2 — Facilitate the Chain:** How are you currently passing AI learning to your managers? What has actually gotten in the way?
>
> 6. **Pillar 3 — Make Space:** What would you need to trade off to create real space for experimentation? What cover do you need from peers or above?
>
> 7. **Do you have any upcoming team events, offsites, or calendar space that could anchor an AI session?**
>
> 8. **Who in adjacent functions are you most dependent on for making AI adoption real in your org?**"

---

### Phase 2 — Signal Collection

Ask before searching:
> "Would you like me to search Slack, Granola meeting notes, Confluence, or Google Drive for context that can sharpen your plan? If yes, what should I look for? (e.g., recent AI discussions in your org, notes from the Leading AI Change session, existing strategy docs)"

If yes → run only what they confirm. Sensible defaults:
- **Granola**: `query_granola_meetings("AI change management [org/function]")` + `query_granola_meetings("[name] managers AI adoption")`
- **Slack**: `slack_search_public_and_private("AI adoption [org] blockers")` + `slack_search_public("director AI cascade leading")`
- **Confluence**: `searchConfluenceUsingCql("text ~ 'AI adoption' AND space.title = '[relevant space]'")` — search for AI strategy, team norms, enablement pages
- **Google Drive**: `google_drive_search("AI change management [function]")` — if unavailable, use `gmail_search_messages` as proxy

---

### Phase 2.5 — Signal Synthesis + Approval

After searching, synthesize and share back **before building**:

> "Here's what I found before building your plan. Let me know if anything looks off or if I should search for something different.
>
> **Your situation (from intake):**
> [2–3 sentence summary: personal fluency level, org maturity, key blockers, space constraints]
>
> **Signals from [Granola / Slack / Confluence / Drive] (if searched):**
> - [Source]: [Key signal]
> - [Source]: [Next signal]
>
> **What I didn't find / gaps:**
> [Note any sources that returned nothing or weren't available]
>
> **My read:**
> [1–2 sentence honest diagnosis — e.g., "You're personally in Explorer/Operator territory. Your org sounds mixed: some engaged, but no shared language or explicit space yet. The space question seems like the real unlock here."]
>
> Does this match your read? Anything to add or correct before I build the plan?"

**Wait for confirmation before proceeding.**

---

### Phase 2.6 — Diagnose → Route to Activation Format

| Signal | Recommended format |
|-------|-------------------|
| Upcoming offsite / leadership team day | **EFLT format** (3.5h, build skills) or **SLT format** (full day) — depends on seniority + goals |
| Team mostly Explorers, psychological barriers | **Show, Don't Tell** (30–60 min) to build comfort |
| Specific workflow bottleneck to solve | **AI Workflow Mapping Session** (60 min) |
| Need energy + momentum | **AI Brainstorm / Mini Hackathon** (~2 hrs) |
| No bandwidth; wants ongoing integration | **Weekly AI Moment** cadence |
| Individuals need direct support | **Office Hours / Buddy Pairings** |

---

### Phase 2.7 — Plan Preview + Output Format

Before building the full plan, share a substantive preview with **at least 4–5 concrete recommendations** grounded in what you've learned. This should be detailed enough for the user to redirect before the full formatted plan is generated.

> "📋 Here's my recommended approach — tell me what to adjust before I build the full plan:
>
> **Recommended activation format:** [e.g., EFLT 3.5-hour hands-on build / Show Don't Tell]
> **Why:** [2–3 sentences grounded in signals and intake]
>
> **Top recommendations:**
> 1. [Specific, actionable recommendation with brief rationale]
> 2. [Specific, actionable recommendation with brief rationale]
> 3. [Specific, actionable recommendation with brief rationale]
> 4. [Specific, actionable recommendation with brief rationale]
> 5. [Specific, actionable recommendation with brief rationale]
>
> **Most at-risk pillar:** [Pillar 1 / 2 / 3 — and why, based on signals]
> **Suggested learning path for your team:** [TackStart / TackShift / mix]
> **Plan structure:** 8-week sprint across phases
>
> Does this direction look right? Reply **yes** to generate the full plan, or tell me what to adjust.
>
> Also — what format would you like your plan in?
> - **Markdown** (default) — saved to ~/assistant/content/change-management/
> - **Word Doc (.docx)** — formatted document you can edit and share
> - **Slides (.pptx)** — deck version of the plan
>
> Leave blank for Markdown."

**Wait for confirmation (and any adjustments) before proceeding. Also note the output format choice.**
- Markdown → write to file system (default behavior)
- DOCX → invoke the `docx` skill
- PPTX → invoke the `pptx` skill (use Thumbtack internal template per CLAUDE.md)

---

### Phase 3 — Build Change Management Plan

**Reference files to use:**
- `references/three-pillars.md` → anchor each pillar section
- `references/ai-expectations.md` → 4 leader expectations + Explorer/Operator/Builder framing
- `references/tool-stack.md` → tools at their stage; cascade-ready offerings for their team
- `references/learning-offerings.md` → offerings to deploy with managers
- `references/team-experimentation.md` → cadence, coaching-by-modes, talk tracks
- `references/offsite-templates.md` → if a session or offsite format is recommended

**Save output to:** `~/assistant/content/change-management/YYYY-MM-DD-[name]-leader-plan.md`

**Output structure:**

```
# Change Management Plan — [Name], [Function]
Generated: [date]

## Your Honest Starting Point
[Where they are as a leader personally (Explorer/Operator/Builder — their own words,
reflected back honestly) + where their org is. Be specific, not motivational.
Explorer is not a criticism. Staying stagnant over time is the issue.]

## Team Diagnosis
[Org maturity level + main blocker + what this means for which levers to pull.
E.g., "Your team sounds mostly Explorer with pockets of Operator. The real
constraint isn't access or mindset — it's that you haven't made explicit space,
so people are trying things ad hoc but not compounding."]

## Situation Assessment
[Signals from intake + Slack/Granola/Confluence if searched.
Note sources searched + what was found.]

## Your Leader Expectations Right Now
[Specific to this person's intake. Anchor to the 4 leader expectations from
ai-expectations.md — not as a checklist but as a diagnostic. Where are they
strong? Where is the real gap?]

## Pillar 1: Get Personally Fluent
**Where you are:** [honest, from their intake answer — their words reflected back]
**What to do at your stage:** [from tool-stack.md, filtered to their level]
**One rep to take this week:** [specific, single action — not a list]
**30-day milestone:** [concrete and measurable]

## Pillar 2: Facilitate the Learning Chain
**Current approach:** [from intake + signals — what they said, what signals showed]
**What's actually in the way:** [name the real friction specifically]
**Cascade plan:** [who → which managers → what format → what timeline]
**Learning offerings to deploy with your team:** [from learning-offerings.md,
mapped to their team's maturity level — TackStart for explorers, TackShift for operators]
**30-day milestone:**

## Pillar 3: Make Explicit Space
**What you're trading off:** [from intake — specific, not "prioritize AI"]
**Cover you need:** [from intake — name who and what kind of cover]
**Peers to coordinate with:** [from intake Q8 + signals — name them if possible]
**30-day milestone:**

## Recommended Team Activation Format
[The format chosen from the routing table. Why this one.

If a session or offsite: include adapted agenda from offsite-templates.md or
team-experimentation.md, customized for function, team size, and maturity.
E.g., "Given your upcoming leadership offsite and that your team is mostly
Operator-level, here's an EFLT-style 3.5-hour agenda adapted for [Function]..."]

If a cadence: specific weekly/monthly/quarterly rhythm ideas from
team-experimentation.md, with suggested starting points.]

## Coaching Your Team Through This
[From coaching-by-modes in team-experimentation.md.
What the manager focus should be for the modes present on their team.
Include relevant talk tracks if specific blockers surfaced in intake —
e.g., if they mentioned "resistance" or "I don't have time" coming from reports.]

## Your 30-Day Sprint
[3 actions, in sequence. Real, not a wishlist. Each with:
- What it is
- Who owns it
- What done looks like]

## Learning Offerings for Your Team
[Specific programs to cascade. TackStart for explorers, TackShift for operators,
targeted sessions for builders. Include #ai-lab and #ai-resources as ongoing habits.
Manager AI Playbook: go/manager-ai]
```

---

### Phase 3.5 — Schedule Reminders

After the plan is saved, parse the action plan into key milestones across 8 weeks and present them for the user to review and customize before scheduling anything.

> "📅 Here are the key milestones I pulled from your plan. Adjust timing, remove any, or add your own before I schedule them:
>
> 1. Week 1 — [Personal fluency commitment — Pillar 1 action] → [suggested date]
> 2. Week 2 — [First team activation event] → [suggested date]
> 3. Week 3 — [Learning chain check-in with direct reports] → [suggested date]
> 4. Week 4 — [Mid-point reflection: what's working, what's blocked] → [suggested date]
> 5. Week 6 — [Second use case or team activation iteration] → [suggested date]
> 6. Week 8 — [Sprint retrospective + next phase planning] → [suggested date]
>
> **Where should I send reminders?**
> - Google Calendar (creates a 30-min event per milestone)
> - Slack message — to yourself, a specific channel, or a team DM (let me know which)
> - Both
>
> What would you like to schedule, and where should the reminders go?"

**If Google Calendar selected:** Use `gcal_create_event` for each milestone with title `[AI] [Milestone name]`, 30-min duration, and the specific action from the plan as the description.

**If Slack selected:** Use `slack_schedule_message` to send a brief nudge on each milestone date. Ask the user for destination: DM to themselves (default), a specific channel, or a team DM (ask for member names). Content: the milestone action + reference to the saved plan.

**Confirm all scheduled items** and display a summary list.

---

### Phase 4 — Slack Connections

Ask:
> "Who should I loop together on this? I can send a Slack intro connecting you with peer leaders navigating similar change management challenges right now."

If they provide names → send group DM:
> "Hey [names] — looping you together because you're each navigating how to lead AI change in your orgs right now, and I think there's real overlap (especially on making explicit space). [Name] leads [Function], [Name] leads [Function]. Worth a conversation."

Also send the completed plan as a Slack DM to the person who ran the skill.

---

## Error Handling

- If Granola/Slack/Drive returns no results → skip that source, note "no signals found for this source," build from intake
- If user declines signal search → build from intake alone, note "plan based on intake only, no external signals gathered"
- If Google Drive MCP is unavailable → use `gmail_search_messages` as proxy, note the substitution in the plan
- If Confluence returns no results → skip, note it, proceed
- Always produce a complete plan even with partial or no signals — intake alone is sufficient
- Never invent signals or fabricate quotes from searches
