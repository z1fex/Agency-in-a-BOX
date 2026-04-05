# SEO Overhaul
> **Teams:** Marketing (SEO, Analytics, Competitive), Content, Intelligence | **Estimated steps:** 8

## What You'll Get
- Technical SEO audit with prioritized fixes
- 100-keyword research map categorized by intent and difficulty
- Competitor SEO analysis (top 3 competitors)
- Content gap report with prioritized opportunities
- 3-month SEO content plan with 12 article briefs
- 5 fully optimized blog posts (1,500-2,000 words)
- Optimized meta titles and descriptions for top 20 pages
- Internal linking strategy with topic cluster map

## Prerequisites
- Active client profile in vault (run `onboard` first)

## Steps

### Step 1: Technical Audit
**Read:** `agents/marketing/seo/keyword-researcher.md`
**Do:** Analyze site structure, page speed indicators, mobile-friendliness, URL structure, sitemap, robots.txt, meta tags, header hierarchy, image alt text, internal linking, and duplicate content issues. Use web fetch to inspect the client's site.
**Save:** `vault/03-Research/[client]/seo-technical-audit-[date].md`

### Step 2: Keyword Research (100 Keywords)
**Read:** `agents/marketing/seo/keyword-researcher.md`
**Do:** Research and compile 100 target keywords. Categorize by intent (informational, commercial, transactional), difficulty (easy, medium, hard), and funnel stage (TOFU, MOFU, BOFU). Use web search for real search suggestions.
**Save:** `vault/03-Research/[client]/keywords-[date].md`

### Step 3: Competitor SEO
**Read:** `agents/marketing/competitive/intelligence-analyst.md`
**Do:** Analyze top 3 competitors' SEO — target keywords, top content, linking strategies, content formats, and publishing frequency. Identify what they rank for that the client does not.
**Save:** `vault/04-Intelligence/[client]/competitor-seo-[date].md`

### Step 4: Content Gaps
**Read:** `agents/marketing/seo/keyword-researcher.md`
**Do:** Identify content gaps — keywords competitors rank for that the client misses, topics with high demand and low competition, and content format opportunities (guides, comparisons, tools, listicles).
**Save:** `vault/03-Research/[client]/content-gaps-[date].md`

### Step 5: SEO Content Plan
**Read:** `agents/content/content-calendar-planner.md`
**Do:** Create 3-month SEO content plan — 12 articles mapped to target keywords, each with a content brief (title, target keyword, secondary keywords, outline, word count, intent, and competing pages to beat).
**Save:** `vault/05-Content/[client]/seo-content-plan-[date].md`

### Step 6: Optimized Blog Posts (5)
**Read:** `agents/content/blog-writer.md`
**Do:** Write 5 SEO-optimized blog posts (1,500-2,000 words each) from the top 5 content briefs. Natural keyword placement, proper H1-H3 structure, meta descriptions, internal link suggestions, and featured snippet opportunities.
**Save:** `output/[client]/[date]/seo-overhaul/seo-blogs/`

### Step 7: Meta Descriptions
**Read:** `agents/marketing/seo/keyword-researcher.md`
**Do:** Write optimized meta titles (50-60 chars) and meta descriptions (150-160 chars) for the client's top 20 pages. Each includes target keyword, benefit statement, and call-to-action.
**Save:** `output/[client]/[date]/seo-overhaul/meta-descriptions.md`

### Step 8: Internal Linking Strategy
**Read:** `agents/marketing/seo/keyword-researcher.md`
**Do:** Create internal linking map — hub-and-spoke topic clusters, page-to-page link recommendations, anchor text suggestions, and orphan page identification.
**Save:** `output/[client]/[date]/seo-overhaul/internal-linking-strategy.md`

### Final Delivery
1. Run quality gate (`quality/qa-checklist.md`) on all deliverables
2. Save all deliverables to `output/[client]/[date]/seo-overhaul/`
3. Update `vault/00-Dashboard/Agency Dashboard.md` with SEO overhaul summary
4. Update `vault/00-Dashboard/ROI Tracker.md` — log 100 keywords, 5 blogs, 20 meta descriptions, technical audit, linking strategy
