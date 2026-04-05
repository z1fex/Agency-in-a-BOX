# Web Research Guide

> How to use Claude Code's built-in web search and web fetch for thorough, sourced research.

---

## Available Tools

### Web Search
Use Claude Code's web search to find current information on any topic. This works like a search engine query directly inside your session.

### Web Fetch
Use web fetch to read the full content of any webpage. Useful for deep-diving into specific articles, pages, or data sources found via search.

---

## Research Strategies

### 1. Broad-to-Narrow Search
Start wide, then refine:
1. **Broad:** Search for the industry or category (e.g., "SaaS project management market 2025")
2. **Narrow:** Search for specific aspects (e.g., "project management software pricing comparison")
3. **Specific:** Search for exact data points (e.g., "Monday.com annual revenue 2024")

### 2. Multi-Source Verification
Never rely on a single source. For each key claim:
1. Find at least 2 independent sources
2. Note any discrepancies between sources
3. Prefer primary sources (company websites, SEC filings, press releases) over secondary (blog posts, news aggregators)

### 3. Competitor Research Queries
Effective search patterns for competitor intelligence:
- `"[competitor name]" pricing` — Find pricing pages and discussions
- `"[competitor name]" review site:reddit.com` — Real user opinions
- `"[competitor name]" vs` — Find comparison articles
- `"[competitor name]" alternative` — Find their competitors
- `"[competitor name]" funding OR revenue OR valuation` — Financial data
- `"[competitor name]" hiring OR careers` — Strategic direction from job postings

### 4. Market Research Queries
- `[industry] market size 2025` — TAM data
- `[industry] trends report` — Industry reports
- `[industry] statistics` — Key metrics
- `[industry] challenges survey` — Pain points
- `site:statista.com [topic]` — Statistical data
- `site:mckinsey.com OR site:hbr.org [topic]` — Thought leadership

### 5. Customer Research Queries
- `[product category] review` — User sentiment
- `"looking for" [product category] site:reddit.com` — Buyer intent
- `[product category] comparison` — Decision factors
- `[product category] complaints` — Pain points with existing solutions

---

## Compiling Research Findings

### Structure Your Notes
For each research session, create a note in vault with this structure:

```markdown
# Research: [Topic]
**Date:** [date]
**Client:** [[Client Name]]
**Purpose:** [why this research was conducted]

## Key Findings
1. [Finding with source URL]
2. [Finding with source URL]
3. [Finding with source URL]

## Data Points
| Metric | Value | Source | Date |
|--------|-------|--------|------|
| [metric] | [value] | [URL] | [when published] |

## Analysis
[Your interpretation of the findings]

## Implications for [Client]
[How this affects the client's strategy]

## Sources
1. [Title] - [URL] - accessed [date]
2. [Title] - [URL] - accessed [date]
```

---

## Citing Sources

### In Deliverables
Always include sources in deliverables:
- Inline: "The SaaS market is projected to reach $X by 2026 ([Source Name](URL))"
- Footnotes: Use numbered references at the bottom
- Source section: Always include a Sources section at the end of reports

### Source Quality Hierarchy
1. **Primary:** Company filings, official announcements, government data
2. **Strong secondary:** Major publications (WSJ, Bloomberg, TechCrunch), research firms (Gartner, Forrester)
3. **Good secondary:** Industry blogs, analyst reports, reputable news sites
4. **Use with caution:** Social media, forums, unverified blog posts
5. **Avoid:** Wikipedia (use it to find primary sources, not as a source itself)

---

## Common Research Tasks

### Company Profile
1. Search `"[company]" about` — fetch their About page
2. Search `"[company]" crunchbase OR linkedin` — company data
3. Search `"[company]" funding round` — financial history
4. Search `"[company]" team leadership` — key people
5. Fetch their homepage, product pages, and blog

### Industry Overview
1. Search `[industry] market report 2025`
2. Search `[industry] trends`
3. Search `[industry] challenges`
4. Search `[industry] major players`
5. Search `[industry] regulation`

### Audience Research
1. Search `[target role] challenges survey`
2. Search `[target role] tools stack`
3. Search `[target role] community forum`
4. Search `[target role] conference events`

---

## Tips

- **Be specific in queries** — "B2B SaaS customer acquisition cost 2025" beats "marketing costs"
- **Use quotes** — "exact phrase" forces exact match
- **Use site:** — Restrict to specific domains for targeted results
- **Check dates** — Data older than 2 years may be outdated for fast-moving markets
- **Save as you go** — Write findings to vault immediately; don't wait until the end
- **Note contradictions** — When sources disagree, note both and explain which seems more reliable
