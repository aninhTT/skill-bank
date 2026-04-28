# Amie's AI Change Skills

Workspace owner: Amie Nguyen (aninh@thumbtack.com), AI Champion at Thumbtack.
These skills support driving AI adoption across Thumbtack functions.

## Skills in this workspace

| Skill | Load when user says... | Produces |
|---|---|---|
| `ai-intel-digest` | "/ai-intel", "AI digest", "audio script", "AI news" | 5–6 min audio script (markdown) |
| `use-case` | "find use cases", "AI opportunities", "what should we automate", "use case for [department]" | DVFR-evaluated use case doc + Slack DM |
| `change-management` | "enablement plan", "change management plan", "AI champion plan", "leading AI change", "cascade AI" | 60-day plan (champion) or org plan (leader) |

## Loading rules

- Match the trigger phrases above. If a request straddles two skills, ask before loading.
- Each skill's `SKILL.md` is the source of truth for its workflow — do not duplicate logic at this layer.
- For `change-management`: always ask Phase 0 ("AI Champion or Manager/Leader?") before doing anything else.
- For `use-case`: always run Phase 0 intake (name, role, department, channels) before signal collection.
- For `ai-intel-digest`: always run the fetcher scripts first — never synthesize from stale source data.

## Conventions

- Default output path: `~/assistant/content/<skill>/...` unless the user specifies otherwise.
- File naming: `YYYY-MM-DD-<slug>.md`.
- Today's date and the user's email come from session context — don't ask for them.
- Never invent signals or fabricate quotes from search results. If a source returns nothing, note it and continue.

## Repo notes

This repo will move to the Thumbtack GitHub org. `README.md` is the public-facing doc; this file is internal Claude instructions and should not be treated as documentation for human readers.
