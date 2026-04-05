# Report Generator Guide

> How to compile research and data into polished, professional reports using Claude Code.

---

## Report Generation Process

### Step 1: Gather Inputs

Before generating any report, collect:
1. **Client context** — Read `vault/01-Clients/[client]/profile.md` and `brand-voice.md`
2. **Research data** — Check `vault/03-Research/[client]/` for existing research
3. **Template** — Select the appropriate template from `templates/`
4. **Previous reports** — Check `vault/08-Operations/` for past reports to maintain consistency

### Step 2: Select the Right Template

| Report Type | Template | When to Use |
|-------------|----------|-------------|
| Full marketing plan | `templates/marketing-strategy.md` | Quarterly strategy |
| SEO analysis | `templates/seo-audit-report.md` | SEO audits |
| Content schedule | `templates/content-calendar.md` | Monthly content planning |
| Sales proposal | `templates/sales-proposal.md` | Client proposals |
| Competitor intel | `templates/competitive-analysis.md` | Competitive reports |
| Email campaigns | `templates/email-campaign.md` | Email marketing plans |
| Social media plan | `templates/social-media-batch.md` | Social content batches |
| Weekly update | `templates/weekly-report.md` | Status updates |
| Monthly review | `templates/monthly-report.md` | Monthly performance |
| Strategic analysis | `templates/swot-analysis.md` | SWOT assessments |
| Media announcements | `templates/press-release.md` | PR and launches |
| Success stories | `templates/case-study.md` | Client case studies |

### Step 3: Fill the Template

Replace all `{{placeholder}}` values with real data:

1. Read the template file
2. For each placeholder:
   - Pull from research data if available
   - Use web search for missing data points
   - Mark any gaps that need client input as `[CLIENT INPUT NEEDED: description]`
3. Remove any unused optional sections
4. Add additional sections if the data warrants it

### Step 4: Structure the Report

Every report should follow this structure:

```
1. Title & Metadata (client, date, version)
2. Executive Summary (1 paragraph — the "so what")
3. Key Findings / Highlights (3-5 bullet points)
4. Detailed Sections (the body of the report)
5. Recommendations (specific, actionable)
6. Next Steps (what to do and when)
7. Sources (links, dates accessed)
```

---

## Writing Guidelines

### Executive Summary
- Write this LAST after completing the full report
- Keep to 3-5 sentences
- Answer: What did we do? What did we find? What should we do about it?
- Include the single most important number or finding
- Make it standalone — readers should understand the report from this alone

### Table of Contents
For reports longer than 3 pages, include a TOC:
```markdown
## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Key Findings](#key-findings)
3. [Detailed Analysis](#detailed-analysis)
4. [Recommendations](#recommendations)
5. [Next Steps](#next-steps)
6. [Sources](#sources)
```

### Data Presentation

**Use tables for comparisons:**
```markdown
| Metric | Q1 | Q2 | Change |
|--------|----|----|--------|
| Revenue | $100K | $120K | +20% |
```

**Use bullet points for lists of 3-7 items:**
```markdown
- Item one with context
- Item two with context
- Item three with context
```

**Use numbered lists for sequential items or rankings:**
```markdown
1. First priority
2. Second priority
3. Third priority
```

**Use blockquotes for key findings or callouts:**
```markdown
> Key finding: Organic traffic increased 45% after implementing the recommended content strategy.
```

### Tone and Voice

1. **Match the client's brand voice** — Check `vault/01-Clients/[client]/brand-voice.md`
2. **Be direct** — Lead with conclusions, then supporting evidence
3. **Be specific** — "Increased by 23%" not "significantly improved"
4. **Be actionable** — Every finding should connect to a recommendation
5. **Avoid jargon** — Unless the audience is technical and expects it

### Formatting Standards

- **Headings:** Use H1 for title, H2 for major sections, H3 for subsections
- **Bold:** For key terms, metrics, and emphasis
- **Italics:** For definitions and secondary emphasis
- **Code blocks:** Only for technical content or data
- **Horizontal rules:** Between major sections
- **Line spacing:** One blank line between paragraphs

---

## Quality Checks Before Delivery

Run through this checklist for every report:

### Content Quality
- [ ] Executive summary accurately reflects the full report
- [ ] All claims are supported by data or sources
- [ ] No placeholder text remains (search for `{{`, `TODO`, `TBD`, `[CLIENT`)
- [ ] All tables have headers and consistent formatting
- [ ] Numbers are formatted consistently (commas, decimals, currency symbols)
- [ ] Dates are in consistent format throughout

### Brand Alignment
- [ ] Tone matches client's brand voice
- [ ] Terminology matches client's glossary
- [ ] Client name spelled correctly throughout
- [ ] Competitor names are accurate

### Structure
- [ ] Logical flow from section to section
- [ ] Table of contents matches actual sections (if included)
- [ ] No orphaned sections (headers without content)
- [ ] Recommendations are specific and numbered

### Technical
- [ ] All links are valid (test with web fetch if unsure)
- [ ] Wikilinks use correct `[[note name]]` format for vault cross-references
- [ ] Tags are included (`#client #deliverable #type`)
- [ ] File is saved to the correct location

---

## Combining Multiple Research Notes into a Report

When you have multiple vault notes that need to be combined:

1. **List all source files:**
   ```
   vault/03-Research/[client]/market-research-2025-01.md
   vault/04-Intelligence/[client]/competitor-analysis-2025-01.md
   vault/07-Strategy/[client]/swot-2025-01.md
   ```

2. **Read each file** and extract key findings

3. **Cross-reference:** Look for patterns across sources:
   - Themes that appear in multiple notes
   - Contradictions that need resolution
   - Gaps that need additional research

4. **Synthesize:** Don't just concatenate — create a narrative:
   - What story does the data tell?
   - What's the most important takeaway?
   - What should the client do differently?

5. **Cite internal sources:** Use wikilinks:
   ```markdown
   Based on our [[Market Research Q1 2025]], the addressable market is growing at 12% annually.
   This aligns with the competitive shifts identified in our [[Competitor Analysis Q1 2025]].
   ```

---

## Output Locations

| Report Type | Save Location |
|-------------|--------------|
| Client deliverable | `output/[client]/[YYYY-MM-DD]/[report-name].md` |
| Internal report | `vault/08-Operations/[report-name]-[date].md` |
| Research findings | `vault/03-Research/[client]/[topic]-[date].md` |
| Campaign report | `vault/02-Campaigns/[client]/[campaign]-[date].md` |

---

## Tips

- **Start with the template** — Never write from scratch when a template exists
- **Pull, don't push** — Let the data drive the narrative, not the other way around
- **Front-load value** — Put the most important finding in the first paragraph
- **Use visuals where possible** — Markdown tables, comparison matrices, even ASCII charts
- **Version your reports** — Include version numbers for living documents
- **Archive old versions** — Move superseded reports to a subfolder, don't delete them
