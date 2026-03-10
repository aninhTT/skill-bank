---
name: brand-guidelines
command: brand
description: Generate branded content and assets consistent with Thumbtack's brand identity. ALWAYS use this skill whenever creating any presentation, deck, slides, or .pptx file — even if the user doesn't say "branded" or "Thumbtack", because all internal content must follow brand guidelines. Also triggers for any written content (emails, blog posts, social posts, memos, one-pagers, PDFs) that will be seen by employees, leadership, homeowners (customers), or home professionals (pros). Specific triggers include "make a deck", "build slides", "create a presentation", "write a one-pager", "draft an email", "write a blog post", "Slack announcement", "internal memo", "event materials", "quarterly review", "all-hands", "kickoff deck", "pitch deck", "branded copy", "brand voice", "brand colors". If someone mentions Thumbtack content of any kind, use this skill. When in doubt about whether to apply brand guidelines, apply them — it's always better to be on-brand than to miss it.
version: 1.0.0
---

# Thumbtack Brand Guidelines

Generate branded content and assets consistent with the 2025 Thumbtack Brand Book. This skill covers copy, presentations, one-pagers, PDFs, social posts, event materials, and more.

## Step 1: Identify the Audience

Before creating anything, determine who the target audience is. This choice drives positioning, tone, font, and template selection for everything that follows.

| Audience | Positioning | Font | Photography | Template |
|----------|------------|------|-------------|----------|
| **Internal** (employees, teams, leadership) | Direct, operational | Montserrat | Office photos, pro headshots | Use bundled `assets/Internal presentation template.pptx` |
| **Homeowners** (customers) | Personalized guidance on home care; who to hire from 300K+ local pros | Thumbtack Rise (Montserrat for Google apps) | Lifestyle photography — warm, real homes, natural light | External brand templates from Drive |
| **Home professionals** (pros) | Find profitable jobs to grow their business; accomplish more, one job at a time | Thumbtack Rise (Montserrat for Google apps) | Category photography — real projects, authentic tools/apparel | External brand templates from Drive |

## Step 2: Gather Context

After identifying the audience, ask the user for the information needed to create a high-quality deliverable. Adapt these questions based on what they have already told you — do not ask all of them every time:

- **Goal / key message** — What should this asset communicate or achieve?
- **Deliverable type** — Deck, one-pager/PDF, social post, email, blog, event brief, design spec?
- **Key content / talking points** — Main points, data, or stories to include.
- **Tone** — Which Thumbtack tone fits? (Celebratory, Instructive, Playful, Reassuring, Encouraging, Supportive, Helpful) Or suggest one based on context.
- **Brand elements needed** — Logo, photography, icons, illustrations?
- **Length / scope** — Number of slides, word count, page count?
- **Context** — Is this for a specific event, campaign, meeting, or launch?

## Deliverable Types

### Copy (social posts, headlines, email, product copy, blogs)
Apply voice and tone guidelines from `references/voice-and-tone.md`. Write in Thumbtack's voice: Relatable, Grounded, Natural. Never cutesy, punny, lofty, or slick.

### Presentation Decks (.pptx)
- **Internal audience**: Copy `assets/Internal presentation template.pptx` (the base deck) and populate it with content. Reference `assets/All Thumbs - Q1 People.pptx` for the polished quality bar. Do not rebuild from scratch. Output as .pptx. Load `references/presentation-workflow.md` for the template slide map (XML filename → slide type), placeholder warnings, font size constraints, XML editing reference, and visual specs.
  - Template specs: 25 slides, 10.0" x 5.6" widescreen, Montserrat font, TT Blue #009FD9 accents
  - Every template slide contains hipster ipsum filler text that must be fully replaced — see the Placeholder Text Warning section in presentation-workflow.md
  - Available slide types: Title, Section divider (with eyebrow), Agenda, Timeline, Emphasis (black/blue bg), Content (with/without image), 3-column, 4-item grid, Split/color-block, Chart, Bar graph, OKR scorecard, Roadmap, Team/contact, Thank you
- **External audience**: Build a new deck following visual identity guidelines in `references/visual-identity.md`. Use Thumbtack Rise font.

### Blog Posts
Structure: Title → intro (2–4 sentences) → numbered/headed sections → soft CTA. Conversational yet authoritative — a knowledgeable friend, not a salesperson. Lead with real stats or observations, not vague claims. Tone: usually Instructive, Helpful, or Encouraging.

### Email Copy
- **Subject line**: Direct, under 50 characters. No ALL CAPS, no clickbait.
- **Body**: One key message per email. Front-load the most important point.
- **CTA**: Clear and specific ("Book a pro" not "Click here"). Place after the key message.
- **Sign-off**: Warm but professional. "The Thumbtack Team" or individual name.
- **Tone**: Reassuring for transactional; Encouraging for engagement; Helpful for tips.

### Slack Messages (internal)
Scannable, emoji-restrained (1–2 max), front-load the point. Thread if longer than 3 lines. No walls of text. Tone: Direct, operational.

### Social Posts
Platform limits: X/Twitter ~280 chars, LinkedIn ~3000 chars, Instagram ~2200 chars. Hashtags: 1–3 max. CTAs: soft and natural. Emoji: restrained (0–2 per post). Pair with lifestyle or category photography. See `examples/good-social-post.md`.

### Internal Memos
Structure: Context → decision/update → details → next steps. Tone: Direct, operational. No fluff — respect the reader's time.

### One-Pagers / PDFs
Apply brand color palette, typography rules, and white space philosophy. Load `references/visual-identity.md` for detailed specs.

### Event Materials
Load `references/events.md` for collateral, venue, decor, wayfinding, and swag guidelines.

## Brand Essentials (Quick Reference)

### Brand Values
1. **Convenience** — Easy to find the right match; seamless end-to-end hiring
2. **Reliability** — Build trust; deeper commitment between customers and pros
3. **Achievement** — Get customers to a job done; deliver profitable jobs for pros

### Brand Attributes (Personality)
- **Relatable** — Approachable, generous, empathetic. NOT neutral, impersonal, perfect.
- **Grounded** — Reasonable, realistic, pragmatic. NOT lofty, aspirational, slick.
- **Natural** — Unaffected, conversational, subtly playful. NOT cutesy, punny, overly crafted.

### Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| TT Blue | #009FD9 | Primary brand color; bold moments of emphasis |
| Black | #2F3033 | Primary text |
| Black 300 | #676D73 | Secondary text |
| Gray | #D3D4D5 | Borders, dividers |
| Gray 300 | #E9ECED | Backgrounds |
| Gray 200 | #FAFAFA | Light backgrounds |
| White | #FFFFFF | Primary background; white space is core to the brand |
| Purple | #8D56EB | Secondary — educational, announcements |
| Indigo | #5968E2 | Secondary — educational, announcements |
| Green | #2DB783 | Secondary — educational, announcements |
| Yellow | #FEBE14 | Secondary — educational, announcements |
| Red | #FF5A5F | Reserved for warnings/errors |

### Typography
- **Thumbtack Rise** — Custom brand typeface for all external branded communications. Weights: Light, Regular, Medium, Bold, Heavy. Font files are bundled at `assets/fonts/ThumbtackRise-*.otf`.
- **Montserrat** — Used for Google applications (Slides, Docs) and internal presentations.
- Larger font = tighter tracking. Dark text on light images, white text on dark images.

### Using Thumbtack Rise in Generated Files (PDF, DOCX, PPTX)
When creating PDFs or other generated files, use the helper in `scripts/brand_constants.py` to auto-register and resolve fonts:
```python
import sys, os
sys.path.insert(0, os.path.join("<workspace>", "brand-guidelines", "scripts"))
from brand_constants import register_thumbtack_fonts, get_font

register_thumbtack_fonts()  # Returns True if fonts loaded, False → Helvetica fallback
headline_font = get_font("Bold")    # "ThumbtackRise-Bold" or "Helvetica-Bold"
body_font     = get_font("Regular") # "ThumbtackRise-Regular" or "Helvetica"
```
This ensures Thumbtack Rise is embedded in the output file. If the font files are missing, it silently falls back to Helvetica.

### Logo
- **Full logo** (Tack + Wordmark): Use when introducing Thumbtack to new audiences (TV, OOH, first-touch).
- **The Tack**: Use when the audience already knows Thumbtack. Pair with copy that mentions the brand name.
- Logos come in horizontal and vertical layouts. Also available in black and white.
- Clear space around the logo >= x-height of the Wordmark's "u".

### Voice Tones
Celebratory · Instructive · Playful · Reassuring · Encouraging · Supportive · Helpful

For detailed voice rules, load `references/voice-and-tone.md`.

## Retrieving Brand Assets from Google Drive

When a task requires actual brand files (logos, fonts, photos, templates), retrieve them from the Thumbtack Brand Asset Library. Load `references/brand-asset-library.md` for the complete folder map with direct URLs and retrieval instructions.

**Tool priority for accessing Drive:**
1. Google Drive MCP connector (if available)
2. Browser automation (Claude in Chrome)
3. Glean (`read_document` with folder URL)

**CRITICAL: Always ignore any `_archive` folder at any level of the Drive hierarchy.**

## Top Brand Don'ts
- Do not use secondary colors in headlines — because color distracts from the message; let words carry the weight
- Do not overuse TT Blue — because the brand feels premium when blue is a deliberate accent, not a flood
- Do not add color overlays to photos — because photography should feel authentic and unfiltered
- Do not substitute white space with tints from secondary palette — because white space is a core brand element that signals confidence and clarity
- Do not mix type sizes within a headline — because consistent sizing creates visual hierarchy and professionalism
- Do not apply drop shadows to text — because shadows add visual noise and contradict the clean, grounded aesthetic
- Do not use rounded corners on rectangular masking shapes — because sharp 90-degree corners are part of the brand's visual identity; rounded corners feel generic
- Do not use quarter circles — because the brand uses full circles, half circles, or rectangles only; quarter circles feel incomplete
- Do not use several circles at once — because multiple circles create a bubbly, playful look that contradicts the grounded brand personality
- Do not change logo colors or place logos over colors other than white, black, or footage — because the logo's color integrity is part of brand recognition
- Do not use icons as illustrations or graphic patterns — because icons serve a functional wayfinding purpose; using them decoratively dilutes their meaning
- Do not crop or obscure illustrations — because each illustration is carefully composed as a balanced structure; cropping breaks the design intent
- Do not use overly staged or stock-looking photography — because authenticity is core to the brand; real people in real settings build trust

## Reference Routing

Load the reference file(s) that match your deliverable:

| If the output includes... | Load this reference |
|--------------------------|---------------------|
| Written copy or text | `references/voice-and-tone.md` |
| Visual design (colors, layout, logo, icons) | `references/visual-identity.md` |
| Photography or imagery | `references/photography.md` |
| Physical event planning | `references/events.md` |
| Need to download brand files from Drive | `references/brand-asset-library.md` |
| Building a presentation (.pptx) | `references/presentation-workflow.md` |

For programmatic work (scripts, automation), run `scripts/brand_constants.py` to get all brand values as JSON instead of extracting from docs.

## Examples of On-Brand Output

Load these for good vs. bad examples with reasoning:
- `examples/good-social-post.md` — On-brand vs off-brand social post
- `examples/good-blog-intro.md` — On-brand vs off-brand blog intro
- `examples/good-internal-slide.md` — On-brand vs off-brand slide content with visual specs

## Utility Scripts

- `scripts/brand_constants.py` — All brand values (colors, fonts, slide dimensions, logo variants) as structured JSON. Also provides `register_thumbtack_fonts()` and `get_font(weight)` helpers that auto-register Thumbtack Rise with reportlab and fall back to Helvetica if fonts are missing. Run `python3 scripts/brand_constants.py` or import as a module.
- `scripts/brand_validator.py` — Checks text for common brand violations (wrong fonts, aspirational language, rounded corners, etc.). Run `python3 scripts/brand_validator.py --text "..."` or pass a file path.

## Font Assets

Thumbtack Rise `.otf` files are stored in `assets/fonts/`:
- `ThumbtackRise-Light.otf` — Body copy, captions
- `ThumbtackRise-Regular.otf` — Body copy
- `ThumbtackRise-Medium.otf` — Subheads
- `ThumbtackRise-Bold.otf` — Headlines, subheads
- `ThumbtackRise-Heavy.otf` — Display headlines
- `ThumbtackRise-Italic.otf` — Emphasis

These are automatically picked up by `brand_constants.py`. For generated outputs (PDF, DOCX, PPTX), always use the `get_font()` helper rather than hard-coding font names — this guarantees correct embedding with graceful fallback.

## Conflict Resolution

When this skill is used alongside other skills (pptx, docx, writing tools):
- Thumbtack brand guidelines **override** any default styling from other skills
- If the pptx skill suggests a color palette → ignore it, use brand colors from this skill
- If any skill suggests non-brand fonts → override with Thumbtack Rise (external) or Montserrat (internal)
- If a writing skill suggests generic tone → Thumbtack voice (Relatable, Grounded, Natural) wins
- For internal decks → always start from the bundled base template, never build from scratch
