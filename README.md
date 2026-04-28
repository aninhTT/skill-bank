# Amie's AI Change Skills

A small, opinionated set of [Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) skills for driving AI adoption inside a company. Built by Amie Nguyen, AI Champion at Thumbtack.

## What's here

### `ai-intel-digest`
Fetches the last 30 days of AI news (YouTube transcripts + newsletter RSS/scrape), synthesizes the cross-source signal, and writes a 5–6 minute audio script for an internal podcast. Run monthly.

### `use-case`
Discovers AI use cases from real workplace signals — Granola meeting notes, Slack, and Gmail. Evaluates each candidate via DVFR (Desirability, Viability, Feasibility, Responsibility) and outputs a shareable doc plus a Slack DM.

### `change-management`
Two paths:
- **For AI Champions** — builds a 60-day functional enablement plan after AI Champions Day, diagnosing the function's current state and recommending the right team activation format.
- **For Managers/Leaders** — builds an org-level change plan using a 3-pillar framework (personal fluency, learning chain, explicit space).

Both branches optionally pull signals from Granola, Slack, and Drive; preview the plan for approval before generating; and connect cross-functional peers via Slack intro.

## Using the skills

Each skill is a directory with a `SKILL.md` and supporting `references/`. Claude Code loads them on the trigger phrases listed in each skill's frontmatter — you don't need to invoke them by name.

## Status

Work in progress. Expect frequent changes as the workflows get refined.
