---
name: AI Intel Digest
description: FULL PIPELINE — fetches fresh 30-day data, then generates an audio script (<1000 words, ~5–6 min). Always run the fetcher scripts first to get current content. Triggers: "/ai-intel", "ai-intel-digest", "run my ai-intel skill", "generate AI digest", "audio script". This is the default ai-intel skill.
---

# AI Intel Digest

Complete pipeline to fetch AI news sources (last 30 days), synthesize into a corporate audio script (<1000 words, ~5–6 minutes).

## Prerequisites

- yt-dlp installed: `brew install yt-dlp`
- Python 3.10+

## Workflow

### Step 1: Archive Prior Source Data

Move the previous run's source data into a dated archive folder so it's recoverable for debugging or re-synthesis:

```bash
RUN_DATE=$(date +%Y-%m-%d)
mkdir -p ~/assistant/content/ai-intel/sources/archive/$RUN_DATE
mv ~/assistant/content/ai-intel/sources/youtube/* \
   ~/assistant/content/ai-intel/sources/archive/$RUN_DATE/ 2>/dev/null || true
mv ~/assistant/content/ai-intel/sources/newsletters/* \
   ~/assistant/content/ai-intel/sources/archive/$RUN_DATE/ 2>/dev/null || true
```

### Step 2: Fetch YouTube Transcripts

```bash
python3 ~/assistant/skills/ai-intel-digest/youtube_fetcher.py \
  ~/assistant/context/youtube_sources.json \
  ~/assistant/content/ai-intel/sources/youtube
```

Sources:
- **Daily**: AI Daily Brief, Everyday AI
- **Monthly**: Lenny's Podcast, BG2 Pod, Hard Fork, Every Inc, AI Context playlist

Output: `~/assistant/content/ai-intel/sources/youtube/youtube_content.json`

### Step 3: Fetch Newsletter Content

```bash
python3 ~/assistant/skills/ai-intel-digest/newsletter_fetcher.py \
  ~/assistant/context/newsletter_sources.json \
  ~/assistant/content/ai-intel/sources/newsletters
```

Sources:
- **RSS**: The Rundown AI, The Neuron Daily, AI Adopters Club, Montreal Ethics Brief, Import AI
- **Web scrape**: The Batch (deeplearning.ai)

Output: `~/assistant/content/ai-intel/sources/newsletters/newsletter_content.json`

### Step 4: Read Source Content

Read the fetched content:
- `~/assistant/content/ai-intel/sources/youtube/youtube_content.json`
- `~/assistant/content/ai-intel/sources/newsletters/newsletter_content.json`

### Step 5: Identify Cross-Source Corroboration

Before synthesis, scan for stories that appear in **3 or more sources** (across YouTube + newsletters). These are almost always the highest-signal stories — surface them first. Note source count per story; prioritize stories with broader coverage over single-source mentions when picking what to cover.

### Step 6: Read Prior Outputs for Dedup + Continuity

Read the most recent 2–3 scripts in `~/assistant/content/ai-intel/outputs/monthly-digest/` and the running theme log at `~/assistant/content/ai-intel/outputs/themes.md` (if it exists).

Use these to:
- **Avoid repeating** stories already covered (a story isn't "new" just because it's still in the news cycle — if you covered it last run, skip or briefly reference)
- **Reference ongoing threads** ("Following up on last month's Mythos discussion...")
- **Maintain narrative continuity** across runs

### Step 7: Read Style Guide

Read and follow: `~/assistant/skills/ai-intel-digest/references/style_corporate.md`

Key principles:
- Warmly informative, grounded, employee-centered
- Casual/conversational tone (talk like catching up with a colleague)
- Acknowledge tensions (opportunity + uncertainty)
- Center human judgment and agency
- Heavier on implications than on news reporting

### Step 8: Generate Audio Script (<1000 words, ~5–6 min)

**Filename:** `~/assistant/content/ai-intel/outputs/monthly-digest/YYYY-MM-DD-{theme-slug}.md`

The theme slug is a 2–4 word kebab-case summary of the dominant thread (e.g. `mythos-trust-gap`, `agent-superapps`, `model-pricing-shift`). Pick something that will help future-you scan the folder.

**Template:**

```markdown
# AI Context Brief — Audio Script
**Date:** [Month Day, Year]
**Duration:** ~5–6 minutes

---

## Intro (~30 seconds)

[Date, conversational welcome, preview of 2–4 stories you'll cover]

---

## Part 1 — The News (~2 minutes)

[Cover the key stories with enough detail to understand what happened. Group related developments. Lead with cross-corroborated stories from Step 5.]

---

## Part 2 — What This Means for Us (~3 minutes)

[The bulk of the episode. Cover both:]

**For our business:** [marketplace dynamics, pro/customer experience, partnerships]

**Internally:** [automation opportunities, security posture, team productivity, skills to develop]

[Acknowledge tensions honestly. Center human judgment.]

---

## Outro (~30 seconds)

[One concrete action item or reflection. Sign-off.]

---

*Sources: [list sources used]*
```

### Step 9: Validate Length

Run a word count on the generated script:

```bash
wc -w ~/assistant/content/ai-intel/outputs/monthly-digest/YYYY-MM-DD-{theme-slug}.md
```

Target: **<1000 words**. If over, tighten Part 1 (news section) first — implications are the value, news is just context.

### Step 10: Update Theme Log

Append to `~/assistant/content/ai-intel/outputs/themes.md`:

```markdown
## YYYY-MM-DD — {theme-slug}
- Story 1 short title
- Story 2 short title
- Story 3 short title
```

This running log makes month-over-month dedup and continuity automatic instead of vibes-based.

### Step 11: Confirm and Report

Report to user:
- Output file path (with theme slug)
- Word count
- Number of YouTube videos / newsletter items processed
- Stories that appeared in 3+ sources (the corroborated ones)
- Stories skipped because already covered in prior runs
- Key themes for this run

## Output Directory Structure

```
content/ai-intel/
├── sources/
│   ├── youtube/                    # Current run only
│   │   └── youtube_content.json
│   ├── newsletters/                # Current run only
│   │   └── newsletter_content.json
│   └── archive/                    # Dated archives of prior runs
│       └── YYYY-MM-DD/
│           ├── youtube_content.json
│           └── newsletter_content.json
└── outputs/
    └── monthly-digest/             # Preserved permanently
        ├── themes.md               # Running theme log
        ├── 2026-04-22-mythos-trust-gap.md
        └── ...
```

## Notes

- Run 1–2 times per month
- Source data is always the last 30 days (rolling window)
- If YouTube fetch fails (yt-dlp issues), proceed with newsletters only
- Prioritize practical insights over hype
- Flag anything with equity/access implications
