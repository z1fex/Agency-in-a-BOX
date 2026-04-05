# Lead Generation
> **Teams:** Intelligence, Sales | **Estimated steps:** 8

## What You'll Get
- Refined ICP with targeting criteria
- Market analysis with TAM/SAM/SOM
- 50-lead list with company and contact details
- Qualified and scored lead list (Hot/Warm/Cold)
- 5 cold outreach email variants
- 4-touch follow-up sequence
- Competitive battlecards for top 3 competitors
- Customizable proposal template

## Prerequisites
- Active client profile in vault (run `onboard` first)

## Steps

### Step 1: ICP Research
**Read:** `agents/intelligence/market-researcher.md`
**Do:** Deep-dive into ideal customer profile — firmographics, technographics, buying triggers, pain points, decision-making process. Refine the existing ICP with actionable targeting criteria.
**Save:** `vault/01-Clients/[client]/icp-refined-[date].md`

### Step 2: Market Analysis
**Read:** `agents/intelligence/market-researcher.md`
**Do:** Identify target market segments, estimate TAM/SAM/SOM, map buyer journey, find watering holes (communities, publications, events where prospects gather).
**Save:** `vault/03-Research/[client]/market-analysis-[date].md`

### Step 3: Build 50-Lead List
**Read:** `agents/sales/lead-generator.md`
**Do:** Research and compile 50 target companies/contacts matching ICP. Use web search for real companies. Capture: Company, Contact Name, Title, Industry, Size, Website, LinkedIn, Email Pattern, Notes.
**Save:** `output/[client]/[date]/lead-generation/lead-list.csv` and `vault/06-Sales/[client]/leads-[date].md`

### Step 4: Qualify Leads
**Read:** `agents/sales/lead-qualifier.md`
**Do:** Score each lead on ICP fit, intent signals (hiring, funding, tech changes), and accessibility. Rank as Hot / Warm / Cold. Prioritize the list for outreach.
**Save:** `vault/06-Sales/[client]/qualified-leads-[date].md`

### Step 5: Outreach Emails (5 Variants)
**Read:** `agents/sales/cold-outreach.md`
**Do:** Write 5 cold outreach email variants with different angles — pain point, case study, question, insight, mutual connection. Include personalization placeholders, subject lines, body, and CTA.
**Save:** `output/[client]/[date]/lead-generation/outreach-emails.md`

### Step 6: Follow-up Sequence
**Read:** `agents/sales/followup-automator.md`
**Do:** Write 4-touch follow-up sequence with timing (Day 3, Day 7, Day 14, Day 30). Each adds new value — case study, resource, insight, breakup email.
**Save:** `output/[client]/[date]/lead-generation/follow-up-sequence.md`

### Step 7: Battlecards
**Read:** `agents/sales/battlecard-creator.md`
**Do:** Create competitive battlecards for top 3 competitors — objection handling, differentiators, win themes, landmines to set, and counter-positioning.
**Save:** `output/[client]/[date]/lead-generation/battlecards.md`

### Step 8: Proposal Template
**Read:** `agents/sales/proposal-generator.md`
**Do:** Create customizable proposal template using `templates/sales-proposal.md` — client branding, scope sections, pricing framework, case study placeholders, terms.
**Save:** `output/[client]/[date]/lead-generation/proposal-template.md`

### Final Delivery
1. Run quality gate (`quality/qa-checklist.md`) on every deliverable
2. Save all deliverables to `output/[client]/[date]/lead-generation/`
3. Update `vault/00-Dashboard/Agency Dashboard.md` with pipeline summary
4. Update `vault/00-Dashboard/ROI Tracker.md` — log 50 leads researched, 5 emails, 4 follow-ups, 3 battlecards, 1 proposal template
