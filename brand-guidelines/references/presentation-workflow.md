# Presentation Workflow

## Two-Deck Hierarchy

Internal presentations use two bundled reference decks with distinct roles:

1. **`assets/Internal presentation template.pptx`** — The **base deck**. Every new internal presentation starts by copying this file. It defines the slide structure, layouts, and patterns. Title slides, section dividers, content layouts, grids, and all standard slide types are pulled from here first.

2. **`assets/All Thumbs - Q1 People.pptx`** — A **polished real-world example** (68 slides). Shows how the base template patterns look when populated with real content. Use this as the quality bar for visual consistency, typography refinement, and content flow.

**Rule**: Always start from the base template. Reference the All Thumbs deck for how slides should look when polished and populated.

---

## Editing Workflow

1. **Copy** the base template: `cp assets/Internal\ presentation\ template.pptx output.pptx`
2. **Unpack** using the pptx skill to inspect/edit slides
3. **Select** the slide types needed for the content (see mapping table below)
4. **Delete** unused template slides
5. **Populate** slides with content, following the visual specs per slide type
6. **Add consistent elements** (footer, bottom line, page numbers, logo)
7. **Pack** and output as `.pptx`

**Important**: Never rebuild internal decks from scratch. Always start from the base template. Brand overrides any default styling from the pptx skill.

---

## Template Slide Map (XML Filenames)

In this template, visual order matches XML filenames 1:1. When unpacked, `slide1.xml` is visual slide 1, `slide2.xml` is visual slide 2, etc.

| XML File | Slide Type | Key Content |
|----------|-----------|-------------|
| `slide1.xml` | Title / Opening | Left text + right photo. Placeholder: "Headline", "Subhead" |
| `slide2.xml` | Section Divider (white bg) | Eyebrow + big statement. Placeholder: "Big headline." |
| `slide3.xml` | Section Divider (with eyebrow) | "EYEBROW TEXT" + "Title page" |
| `slide4.xml` | Agenda (3 items) | "Thing 1", "Thing 2", "Thing 3" |
| `slide5.xml` | Timeline (multi-step) | "Step 01", "Step 02", etc. |
| `slide6.xml` | Emphasis (black bg) | "Black emphasis" |
| `slide7.xml` | Emphasis (blue bg) | "This is the blue emphasis page" |
| `slide8.xml` | Content (2-idea) | "Idea 1", "Idea 2" |
| `slide9.xml` | Content (continuation) | Single text block |
| `slide10.xml` | Content (3-idea) | "This is idea 1.", "This is the second idea.", "Wow idea 3?!" |
| `slide11.xml` | Content + Eyebrow | "EYEBROW TEXT" + "Content page" + body |
| `slide12.xml` | Content (title + body) | "Content page" + body text |
| `slide13.xml` | Content + Image | "Content page" + image + caption |
| `slide14.xml` | 4-Item Grid | "Thing 01", "Thing 02", etc. |
| `slide15.xml` | Big Emphasis | Large text, centered |
| `slide16.xml` | Bar Chart (horizontal) | "What's Next" + bars |
| `slide17.xml` | Bar Chart (vertical) | "What's Next" + bars |
| `slide18.xml` | Split Layout (color block) | Left color block + right stacked text |
| `slide19.xml` | Split Layout (two-column) | "Why?" + body in two halves |
| `slide20.xml` | Table / Chart | "NEED A CHART?" + table |
| `slide21.xml` | Bar Graph | "NEED A BAR GRAPH?" + graph shapes |
| `slide22.xml` | OKR Scorecard | "OKR Scorecard Review" |
| `slide23.xml` | Roadmap | "2021 Roadmap" + timeline shapes |
| `slide24.xml` | Team / Contact | "TEAM" + names |
| `slide25.xml` | Thank You | "Thank you!" |

---

## Placeholder Text Warning

Every slide in the template contains **hipster ipsum** filler text (phrases like "Iceland activated charcoal bushwick flexitarian", "La croix next level selvage tacos", "lomo skateboard celiac", etc.). This text appears in every `<a:t>` element within text runs and table cells.

When populating slides, you must replace **all** `<a:t>` content — not just the first text run in a shape. Many slides have multiple paragraphs (`<a:p>`) within a single text body, and each may contain separate filler. If you replace only the first paragraph and leave the rest, the hipster ipsum will be visible on the final slide.

**How to verify**: After editing, search all slide XML files for these marker words: `Iceland`, `charcoal`, `bushwick`, `flexitarian`, `knausgaard`, `humblebrag`, `La croix`, `selvage`, `glossier`, `godard`, `lomo`, `celiac`. If any remain, you missed a placeholder.

---

## Font Size Constraints

The template's default font sizes are designed for short placeholder text. When replacing with real content, you often need to reduce sizes to prevent text from overflowing its container.

| Slide Type | Default Size | Reduce to | When |
|-----------|-------------|-----------|------|
| 3-idea (slide10) | 29pt | 16–18pt | Body text exceeds ~80 chars per idea |
| Content + Eyebrow (slide11) | 11pt body | Keep 11pt | Rarely overflows; safe for ~500 chars |
| Split layout (slide19) | 11pt body | Keep 11pt | Safe for ~200 chars per section |
| 4-item grid (slide14) | 11pt body | 9–10pt | Each item exceeds ~120 chars |
| Table cells (slide20) | 9–10pt | Keep | Tables auto-wrap; reduce row count if needed |

The key rule: if you're putting 3+ sentences into a text box that was designed for a single line, reduce the `sz` attribute. In OOXML, `sz` values are in hundredths of a point (so 29pt = `sz="2900"`, 18pt = `sz="1800"`).

---

## Slide Dimensions

- Width: 10.0" (9,144,000 EMU)
- Height: 5.6" (5,080,000 EMU)
- Aspect ratio: Widescreen

---

## Consistent Elements

Apply these to every slide (derived from the All Thumbs polished example):

| Element | Spec |
|---------|------|
| **Footer text** | Deck title or series name — Montserrat SemiBold, 7pt, #79D2F2, center-bottom |
| **Bottom line** | Horizontal rule at y=5.2" across full slide width |
| **Page numbers** | Bottom-right, small text |
| **Thumbtack logo** | Tack icon, top-left (~0.6", 0.7"), ~1.3"×0.2" |

---

## Slide-to-Content Mapping Table

### 1. Title / Opening Slide

**Base**: Template slide 1 | **Polished example**: All Thumbs slide 1

| Element | Spec |
|---------|------|
| Layout | Left 60% text, right 40% full-height photo |
| Title | Montserrat Medium, 57pt, #2F3033 |
| Photo | 3.7–3.9" wide × 5.6" tall (full slide height) |
| Metadata tags | Pill-shaped containers below title — Montserrat SemiBold, 12pt |
| Logo | Thumbtack Tack, top-left |
| Optional | Speaker headshot overlaid on right photo boundary |

**Use for**: Opening slide of every deck.

---

### 2. Section Divider / Big Statement

**Base**: Template slides 2, 6, 7 | **Polished examples**: All Thumbs slides 4–6, 8–9, 30–31, 35–37

| Element | Spec |
|---------|------|
| Eyebrow | ALL CAPS, Montserrat ExtraBold, 9pt, #009FD9 |
| Statement | Montserrat Medium, 40–42pt, #2F3033 |
| Emphasis line | Optional second clause in TT Blue (#18A2D5 or #019ED9) |
| Position | (0.5", 2.0"), ~9" wide |

**Variants**:
- White background (Template slide 2) — default
- Black background (Template slide 6) — high-impact moments
- Blue background (Template slide 7) — high-impact moments

**Use for**: Transitioning between major sections, big strategic statements, key themes.

---

### 3. Agenda / Timeline

**Base**: Template slides 3–5

**Use for**: Meeting agendas, project timelines, phase breakdowns.

---

### 4. Speaker / Topic Intro

**Polished examples**: All Thumbs slides 7, 18, 38, 55 (no direct template equivalent — build from title slide pattern)

| Element | Spec |
|---------|------|
| Photo | Right side, full height, 3.7" wide |
| Title | Left side — Montserrat Medium, 47–57pt, #2F3033 |
| Name tags | Bottom — pill-shaped, Montserrat SemiBold, 12pt |
| Headshot | Circular, overlaid at photo boundary (~1.1"×1.1") |

**Use for**: Introducing speakers, team members, or topic owners.

---

### 5. Content with Title + Image

**Base**: Template slide 13 | **Polished examples**: All Thumbs slides 10, 28

| Element | Spec |
|---------|------|
| Eyebrow | Above title — Montserrat ExtraBold, 7pt, ALL CAPS |
| Title | Montserrat Medium, 23–30pt, #2F3033, top-left |
| Image | Large image/screenshot below (~8.8"×4.1") |

**Use for**: Showcasing product screenshots, data visualizations, photos with context.

---

### 6. Content (text only)

**Base**: Template slides 8–12

**Use for**: Bullet points, text-heavy content, detailed explanations.

---

### 7. Split Layout

**Base**: Template slide 18 | **Polished examples**: All Thumbs slides 20, 24, 27

| Element | Spec |
|---------|------|
| Divider | Vertical line at ~6.0–6.5" |
| Left | Image or screenshot |
| Right | Stacked sections with headers |
| Section headers | Montserrat ExtraBold, 7pt, ALL CAPS (e.g., PROBLEM / APPROACH / RESULT) |
| Body text | Montserrat Medium, 10–11pt, #2F3033 |

**Use for**: Before/after comparisons, problem/solution pairs, case studies.

---

### 8. 3-Column Learnings

**Polished examples**: All Thumbs slides 25, 29 (no direct template equivalent — build from 3-column template)

| Element | Spec |
|---------|------|
| Separator | Horizontal line at y=2.4" |
| Columns | 2 vertical lines creating 3 equal columns |
| Heading | Montserrat Medium, 17pt, bold |
| Body | Montserrat Medium, 9pt |

**Use for**: Key takeaways, learnings, principles (groups of 3).

---

### 9. Numbered List / Principles

**Polished examples**: All Thumbs slides 41, 43, 56, 57

| Element | Spec |
|---------|------|
| Rows | Full-width (8.6" wide, 0.8–1.0" tall), light background fill |
| Number | TT Blue #009FD9, 19pt, in light circle |
| Item text | Montserrat SemiBold, 17pt, #2F3033 |
| Subtitle | Montserrat Medium, 17pt |

**Use for**: Ordered principles, priorities, action items, numbered lists.

---

### 10. Card Grid (3-column)

**Polished examples**: All Thumbs slides 46, 49–53

| Element | Spec |
|---------|------|
| Cards | 3 equal cards (2.8" wide, ~2.4–3.1" tall), solid light fill |
| Number | TT Blue circle with number at top |
| Card title | Montserrat SemiBold, 21pt, #2F3033 |
| Card body | Montserrat Medium, 10–14pt |

**Use for**: Resources, categories, north stars, strategic pillars (groups of 3).

---

### 11. Card Grid (4-column)

**Base**: Template slide 14 | **Polished example**: All Thumbs slide 47

| Element | Spec |
|---------|------|
| Cards | 4 equal cards (2.1" wide), solid fill |
| Title | Montserrat SemiBold, 16pt, #222222 |

**Use for**: Four-item grids, team structures, quadrants.

---

### 12. Chart / Bar Graph

**Base**: Template slides 15–17

**Use for**: Data visualization, metrics, OKR scorecards.

---

### 13. Comparison / Side-by-Side

**Polished example**: All Thumbs slide 21

| Element | Spec |
|---------|------|
| Columns | Two columns with colored background fills |
| Divider | Vertical line |
| Eyebrows | Montserrat ExtraBold, 7pt, ALL CAPS |
| Content | Screenshots or text in each column |

**Use for**: Feature comparisons, A/B results, old vs. new.

---

### 14. Full-Bleed Photo

**Polished examples**: All Thumbs slides 2, 16, 33

| Element | Spec |
|---------|------|
| Image | Covers entire slide (10.0"×5.6") |
| Overlay | None or minimal with semi-transparent fill |

**Use for**: Transition/mood slides between sections, emotional emphasis.

---

### 15. Roadmap

**Base**: Template slide 21

**Use for**: Project roadmaps, quarterly plans, milestone timelines.

---

### 16. OKR Scorecard

**Base**: Template slide 20

**Use for**: OKR tracking, goal progress, performance scorecards.

---

### 17. Team / Contact

**Base**: Template slide 23

**Use for**: Team introductions, contact information, org charts.

---

### 18. Thank You / Closing

**Base**: Template slide 25

**Use for**: Final slide of every deck.

---

## Common Slide Combinations

### All-Hands Meeting (8–12 slides)
1. Title slide (slide type 1)
2. Agenda (slide type 3)
3. Section divider per topic (slide type 2)
4. Content slides with data/screenshots (slide types 5, 6, 12)
5. Key takeaways (slide type 8)
6. Thank you (slide type 18)

### Quarterly Review (10–15 slides)
1. Title slide (slide type 1)
2. Agenda (slide type 3)
3. Section divider: Results (slide type 2)
4. OKR scorecard (slide type 16)
5. Charts and metrics (slide type 12)
6. Section divider: Learnings (slide type 2)
7. 3-column learnings (slide type 8)
8. Section divider: Next Quarter (slide type 2)
9. Roadmap (slide type 15)
10. Thank you (slide type 18)

### Project Proposal (6–8 slides)
1. Title slide (slide type 1)
2. Big statement — the problem (slide type 2)
3. Split layout — problem/approach (slide type 7)
4. Card grid — key pillars (slide type 10)
5. Numbered list — next steps (slide type 9)
6. Thank you (slide type 18)

### Team Intro (5–8 slides)
1. Title slide (slide type 1)
2. Big statement — team mission (slide type 2)
3. Speaker/topic intros per team member (slide type 4)
4. Thank you (slide type 18)

---

## Font and Color Constants for Programmatic Editing

### Montserrat Weights by Element

| Element | Weight | Size (pt) | Color |
|---------|--------|-----------|-------|
| Slide title | Medium | 57 | #2F3033 |
| Section eyebrow | ExtraBold | 9 | #009FD9 |
| Section statement | Medium | 40–42 | #2F3033 |
| Content title | Medium | 23–30 | #2F3033 |
| Body text | Medium | 10–11 | #2F3033 |
| Metadata tags | SemiBold | 12 | #2F3033 |
| Footer | SemiBold | 7 | #79D2F2 |
| Card title | SemiBold | 21 | #2F3033 |
| Card body | Medium | 10–14 | #2F3033 |
| Numbered item | SemiBold | 17 | #2F3033 |
| Numbered circle | Regular | 19 | #009FD9 |

### Key Hex Values

| Color | Hex | Usage |
|-------|-----|-------|
| TT Blue | #009FD9 | Eyebrows, numbered circles, accents |
| Primary text | #2F3033 | All body and title text |
| Footer text | #79D2F2 | Footer/series name |
| Emphasis blue | #18A2D5 | Optional emphasis lines in section dividers |
| Card fill (light) | #E9ECED | Card and row backgrounds |

### EMU Reference

| Dimension | Inches | EMU |
|-----------|--------|-----|
| Slide width | 10.0 | 9,144,000 |
| Slide height | 5.6 | 5,080,000 |
| 1 inch | 1.0 | 914,400 |
| Bottom line y | 5.2 | 4,754,880 |
| Left margin | 0.5 | 457,200 |
| Right photo width | 3.8 | 3,474,720 |

---

## XML Editing Quick Reference

When editing unpacked slide XML directly, these are the key elements and attributes:

| What | XML Element/Attribute | Example |
|------|----------------------|---------|
| Text content | `<a:t>Your text here</a:t>` | Replace the text between tags |
| Font size | `sz="1800"` on `<a:rPr>` or `<a:endParaRPr>` | Value is hundredths of a point (1800 = 18pt) |
| Font face | `<a:latin typeface="Montserrat"/>` | Also set `<a:ea>`, `<a:cs>`, `<a:sym>` |
| Font weight | `typeface="Montserrat ExtraBold"` | Weight is part of the typeface name string |
| Bold | `b="1"` on `<a:rPr>` | |
| Text color | `<a:solidFill><a:srgbClr val="009FD9"/></a:solidFill>` | Inside `<a:rPr>` |
| Shape fill | `<a:solidFill><a:srgbClr val="E9ECED"/></a:solidFill>` | Inside `<p:spPr>` |
| Shape position | `<a:off x="457200" y="914400"/>` | Values in EMU |
| Shape size | `<a:ext cx="9144000" cy="5080000"/>` | Values in EMU |
| Paragraph | `<a:p>` | Contains `<a:pPr>` (properties) and `<a:r>` (runs) |
| Line spacing | `<a:spcPct val="115000"/>` inside `<a:lnSpc>` | 115000 = 115% |
| Space before | `<a:spcBef><a:spcPts val="1000"/></a:spcBef>` | 1000 = 10pt spacing |

When replacing text, preserve the surrounding `<a:rPr>` (run properties) and `<a:endParaRPr>` (end paragraph properties) — those carry the font, size, and color formatting. Only change what's between `<a:t>` and `</a:t>`.

To remove an entire paragraph (e.g., leftover lorem ipsum), delete the full `<a:p>...</a:p>` block including its `<a:pPr>` and all `<a:r>` runs.

---

## Final Cleanup Step

After packing the PPTX from edited XML, always re-save through python-pptx to ensure structural validity and maximum viewer compatibility:

```python
from pptx import Presentation
prs = Presentation('output.pptx')
prs.save('output_clean.pptx')
```

This fixes minor XML inconsistencies (missing attributes, ordering issues) that raw XML editing can introduce. The cleaned file will open reliably in PowerPoint, Google Slides, and web-based previews.

---

## Visual Consistency Checklist

Before finalizing any internal deck, verify:

- [ ] Started from base template (not built from scratch)
- [ ] All placeholder/lorem ipsum text replaced (search for: Iceland, charcoal, bushwick, La croix, lomo, celiac)
- [ ] No text overflow — font sizes reduced for slides with dense content
- [ ] Re-saved through python-pptx for structural cleanup
- [ ] Title slide uses Template slide 1 pattern (left title, right photo)
- [ ] All section dividers have eyebrow text in ALL CAPS TT Blue
- [ ] Footer text present on every slide (deck title, Montserrat SemiBold, 7pt, #79D2F2)
- [ ] Bottom horizontal rule at y=5.2" on every slide
- [ ] Page numbers in bottom-right
- [ ] Thumbtack Tack logo in top-left
- [ ] Font is Montserrat only (no other fonts)
- [ ] Colors are from the brand palette only
- [ ] No rounded corners on rectangular shapes
- [ ] No drop shadows on text
- [ ] White space maintained — not filled with secondary palette tints
