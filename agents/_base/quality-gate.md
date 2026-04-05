# Quality Gate Standards

> **Applies to:** ALL Agents | **Version:** 2.0

## Purpose

This document defines the minimum quality standards every agent in the agency must follow before saving any deliverable. Claude Code reads this file as a universal checkpoint. No output leaves the agency without passing these checks.

## Pre-Work Requirements

Before starting ANY work, every agent MUST:

1. **Read the active client profile** from `vault/01-Clients/[active-client]/profile.md`
2. **Read the brand voice guide** from `vault/01-Clients/[active-client]/brand-voice.md` (if it exists)
3. **Check for existing work** in the relevant vault folder to avoid duplication
4. **Confirm the client's current goals** from `vault/01-Clients/[active-client]/goals.md`

## Quality Checklist

### 1. Client Alignment
- [ ] Output references the correct company name, industry, and target audience
- [ ] Tone and voice match the client's brand guidelines in `brand-voice.md`
- [ ] Content addresses the client's specific situation, not generic advice
- [ ] No conflicting information with existing client deliverables in vault

### 2. Factual Accuracy
- [ ] Never hallucinate data -- use web search to find real information
- [ ] All statistics and data points are sourced with URLs or publication names
- [ ] No fabricated URLs, phone numbers, email addresses, or company details
- [ ] Company names, product names, and proper nouns are spelled correctly
- [ ] Dates and timelines are realistic and internally consistent
- [ ] If a fact cannot be verified, mark it clearly as "[unverified]"

### 3. Specificity
- [ ] Every recommendation is tailored to this specific client
- [ ] No generic advice that could apply to any business
- [ ] Action items include specific next steps with enough detail to execute
- [ ] Numbers are used where possible (percentages, dollar amounts, timeframes)

### 4. Completeness
- [ ] All sections required by the agent's output format are present
- [ ] No placeholder text like "[INSERT HERE]", "TBD", or "TODO" remains
- [ ] Deliverable can stand alone without additional explanation
- [ ] Sources are cited for all claims and data points

### 5. Professional Standards
- [ ] Grammar and spelling are error-free
- [ ] Formatting is clean and consistent (proper Markdown headings, lists, tables)
- [ ] No duplicate content or repeated paragraphs
- [ ] Logical flow from section to section

### 6. Vault Integration
- [ ] Save all work to vault with `[[wikilinks]]` connecting related notes
- [ ] Follow the template from `templates/` if one exists for this deliverable type
- [ ] File saved in BOTH locations: `vault/[section]/` and `output/[client]/[date]/`
- [ ] Update the dashboard (`vault/00-Dashboard/`) after significant work
- [ ] Include YAML front-matter for cross-agent consumption:

```yaml
---
agent: [agent-name]
client: [client-slug]
date: [YYYY-MM-DD]
status: complete|draft|blocked
depends-on: [list of input files used]
feeds-into: [list of agents that consume this output]
---
```

## Quality Scoring

Each deliverable receives an internal score (not shown to users unless requested):

| Score | Meaning | Action |
|-------|---------|--------|
| 5/5 | Exceptional -- exceeds all requirements | Save and deliver |
| 4/5 | Strong -- meets all requirements with minor polish opportunities | Save and deliver |
| 3/5 | Acceptable -- meets minimum requirements | Save but flag improvements |
| 2/5 | Below standard -- missing key elements | Revise before saving |
| 1/5 | Unacceptable -- fundamentally flawed | Rewrite from scratch |

**Minimum threshold to save and deliver: 3/5**

## File Naming Convention

All output files must follow this pattern:

```
[YYYY-MM-DD]-[agent-name]-[deliverable-type].md
```

Examples:
- `2026-04-05-keyword-researcher-keyword-report.md`
- `2026-04-05-blog-writer-article-draft.md`
- `2026-04-05-swot-analyst-swot-analysis.md`

## Dual Save Requirement

Every deliverable MUST be saved in two locations:

1. **Vault (organized by function):** `vault/[section]/[filename].md`
2. **Output (organized by client + date):** `output/[client-slug]/[YYYY-MM-DD]/[filename].md`

## Error Handling

If an agent cannot complete its task due to missing information:

1. Save a partial deliverable with clear `<!-- BLOCKED: [reason] -->` comments
2. List exactly what information is needed to complete the work
3. Suggest which other agent or data source could provide the missing information
4. Save the partial file with `-DRAFT` appended to the filename
5. Do NOT fill in gaps with fabricated data

## Summary of Non-Negotiable Rules

1. Always read client profile first
2. Never hallucinate data -- use web search for real information
3. Save all work to vault with `[[wikilinks]]`
4. Follow the template from `templates/` if available
5. Be specific to the client, never generic
6. Cite sources for all claims
7. Update dashboard after significant work
