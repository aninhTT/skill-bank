# Brand Asset Library — Google Drive

## Folder Map

All brand assets live in the **Thumbtack Brand Asset Library** shared drive.

**Root URL:** https://drive.google.com/drive/folders/0APRRjDovb9rGUk9PVA

```
Thumbtack Brand Asset Library
│
├── _Archive/                              ← ALWAYS IGNORE — never open or use
│
├── _Template documents/
│   URL: https://drive.google.com/drive/folders/1h3lbEUhbkA3rLa4kS6cPIZ1DwFeLW-ZA
│   Contents:
│   ├── Presentation templates (Google Slides format)
│   ├── Template – Brand Creative brief (Google Doc)
│   ├── Thumbtack_Letterhead.docx
│   └── thumbtack-partnership-lockup.pdf
│
├── App store icons/
│
├── Fonts/
│   └── Thumbtack Rise OTF/
│       URL: https://drive.google.com/drive/folders/1IpQmx6aW4fPFQgLISRW0svw8k9uqzvf7
│       Files:
│       ├── ThumbtackRise-Bold.otf
│       ├── ThumbtackRise-Heavy.otf
│       ├── ThumbtackRise-Italic.otf
│       ├── ThumbtackRise-Light.otf
│       ├── ThumbtackRise-Medium.otf
│       └── ThumbtackRise-Regular.otf
│
├── Internal branding/
│
├── Logo/
│   URL: https://drive.google.com/drive/folders/1ckeGS5Nx8xBV4cZI8Ghqy7n2QoJfS0b5
│   ├── Combination Logo/                  ← Full logo (Tack + Wordmark)
│   │   URL: https://drive.google.com/drive/folders/1d-oPsi_m4GrwyMOkT_O8i9uVdHmYqwxx
│   │   Subfolders by format: AI / EPS / JPG / PDF / PNG / SVG
│   │
│   ├── Logo animation/
│   ├── Programs/                          ← Thumbtack Guarantee, Top Pro badge, Pro Advisory Board
│   ├── Tack/                              ← Standalone Tack icon
│   └── Wordmark/                          ← Standalone wordmark text
│
├── Photography/
│   URL: https://drive.google.com/drive/folders/1kEgB6xhfD8Jej7KCdAjFzRWh9JKrujxA
│   ├── Homeowner Photography/             ← Lifestyle shots of real homes and homeowners
│   ├── Office photos/                     ← Thumbtack office and workspace photos
│   ├── Pro events/                        ← Photos from pro-focused events
│   ├── Pro headshots (ok to use in…)/     ← Professional portraits of Thumbtack pros
│   └── Studio photography/               ← Controlled studio shots
│
├── Positioning/
├── Product screens/
├── Segmentation/
└── Videos & TV spots/
```

## Retrieval Instructions

### When to retrieve assets
Only navigate to Google Drive when the task specifically calls for a downloadable file — a logo image, font file, photograph, or template document. For copy-only tasks, the brand guidelines in the other reference files are sufficient.

### Tool Priority (try in this order)
1. **Google Drive MCP connector** — If available, use Google Drive MCP tools first. They provide direct file listing, reading, and downloading without needing a browser.
2. **Browser automation (Claude in Chrome)** — If no Drive MCP is available, navigate to the folder URLs above to browse and download files.
3. **Glean** — As a fallback, use the `read_document` tool with the specific folder URL to check contents.

### Asset Selection Guide

| Need | Drive Path | Format Guidance |
|------|-----------|----------------|
| Full logo (first-touch, new audiences) | Logo → Combination Logo → [format] | PNG for digital, SVG for scalable, EPS/AI for print |
| Tack icon (familiar audiences) | Logo → Tack | PNG for digital, SVG for scalable |
| Wordmark only | Logo → Wordmark | PNG for digital, SVG for scalable |
| Program badges (Guarantee, Top Pro) | Logo → Programs | Use as provided |
| Thumbtack Rise font files | Fonts → Thumbtack Rise OTF | Download the needed weight(s) as .otf |
| Homeowner/lifestyle photos | Photography → Homeowner Photography | Browse and select based on content needs |
| Pro headshots | Photography → Pro headshots | Approved for external use |
| Pro event photos | Photography → Pro events | Event-specific imagery |
| Studio photography | Photography → Studio photography | Controlled, clean shots |
| Presentation templates | _Template documents | Google Slides or .pptx format |
| Letterhead | _Template documents → Thumbtack_Letterhead.docx | Word format |
| Partnership lockup | _Template documents → thumbtack-partnership-lockup.pdf | PDF |
| Brand creative brief template | _Template documents → Template – Brand Creative brief | Google Doc |

### Critical Rules
- **ALWAYS skip `_archive` folders** at every level of the Drive hierarchy
- When browsing a logo subfolder, each variant is organized by file format (AI, EPS, JPG, PDF, PNG, SVG) — navigate to the right format subfolder
- For internal presentations, use the bundled `assets/Internal presentation template.pptx` instead of going to the Drive
- If a needed asset is not found in the expected folder, check the root level or ask the user for clarification — do not guess
