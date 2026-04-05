# Competitor Report
> **Teams:** Intelligence, Strategy, Sales | **Estimated steps:** 8

## What You'll Get
- Competitor identification and profiles (5-8 competitors)
- Scraped competitor site data and messaging analysis
- Individual SWOT analysis per competitor
- Feature-by-feature comparison matrix
- Pricing model comparison and analysis
- 2x2 positioning map with white space identification
- One-page battlecard per competitor
- Polished competitive intelligence report

## Prerequisites
- Active client profile in vault (run `onboard` first)

## Steps

### Step 1: Identify Competitors
**Read:** `agents/intelligence/competitor-monitor.md`
**Do:** Identify top 5-8 competitors through web research. Categorize as direct, indirect, and aspirational. Capture: company name, URL, founding year, estimated size, funding, geography. Pull existing data from `vault/01-Clients/[client]/competitors.md`.
**Save:** `vault/04-Intelligence/[client]/competitor-list-[date].md`

### Step 2: Scrape Competitor Sites
**Read:** `agents/intelligence/web-scraper.md`
**Do:** For each competitor, analyze: homepage messaging, product/feature pages, pricing page, about page, blog topics, testimonials/case studies, and job postings (for strategy signals).
**Save:** `vault/04-Intelligence/[client]/scrapes/[competitor]-[date].md`

### Step 3: SWOT per Competitor
**Read:** `agents/strategy/swot-analyst.md`
**Do:** Create individual SWOT analysis for each competitor using `templates/swot-analysis.md`. Identify strategic advantages, vulnerabilities, growth trajectory, and threats they pose to the client.
**Save:** `vault/04-Intelligence/[client]/swot/[competitor]-swot.md`

### Step 4: Feature Comparison
**Read:** `agents/intelligence/data-analyst.md`
**Do:** Build feature-by-feature comparison matrix. Mark each feature as: has it, partial, missing, or superior. Identify feature gaps the client can exploit and unique advantages to highlight.
**Save:** `vault/04-Intelligence/[client]/feature-comparison-[date].md`

### Step 5: Pricing Analysis
**Read:** `agents/intelligence/price-monitor.md`
**Do:** Map competitor pricing models — tiers, per-seat, usage-based, freemium. Compare entry price, mid-tier, and enterprise. Identify pricing opportunities and positioning gaps.
**Save:** `vault/04-Intelligence/[client]/pricing-analysis-[date].md`

### Step 6: Positioning Map
**Read:** `agents/strategy/growth-strategist.md`
**Do:** Create a 2x2 positioning map using industry-relevant dimensions. Plot all competitors and client. Identify white space opportunities and underserved market positions.
**Save:** `vault/07-Strategy/[client]/positioning-map-[date].md`

### Step 7: Battlecards
**Read:** `agents/sales/battlecard-creator.md`
**Do:** Create one-page battlecard per competitor: quick facts, their pitch, counter-pitch, strengths to acknowledge, weaknesses to exploit, objection handling, landmines, and win themes.
**Save:** `output/[client]/[date]/competitor-report/battlecards/`

### Step 8: Final Report
**Read:** `agents/intelligence/industry-report-writer.md`
**Do:** Compile everything into a polished competitive intelligence report using `templates/competitive-analysis.md`. Include executive summary, key findings, detailed profiles, comparison tables, strategic recommendations, and a monitoring plan.
**Save:** `output/[client]/[date]/competitor-report/competitive-intelligence-report.md`

### Final Delivery
1. Run quality gate (`quality/qa-checklist.md`) on final report and all battlecards
2. Save all deliverables to `output/[client]/[date]/competitor-report/`
3. Update `vault/00-Dashboard/Agency Dashboard.md` with intelligence summary
4. Update `vault/00-Dashboard/ROI Tracker.md` — log competitor profiles, SWOTs, battlecards, final report
