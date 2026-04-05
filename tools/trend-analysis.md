# Trend Analysis Guide

> Free methods for detecting and analyzing trends using Claude Code's built-in capabilities.

---

## Trend Sources

### 1. Google Trends (via Web)

Google Trends data is accessible through web search and web fetch:

**Search Patterns:**
- Web search: `google trends [topic] [year]` — Find articles referencing trend data
- Web search: `[industry] trending topics [year]` — Current trends coverage
- Web search: `[industry] search trends rising` — Growing interest areas

**What to Look For:**
- Rising search terms in the industry
- Seasonal patterns (if applicable to client's business)
- Geographic interest variations
- Related queries and topics
- Breakout terms (>5000% growth signals emerging trends)

### 2. Industry Publications

**Finding Trend Reports:**
- Web search: `[industry] trends [year] report`
- Web search: `[industry] predictions [year]`
- Web search: `[industry] state of report [year]`
- Web search: `site:mckinsey.com OR site:hbr.org OR site:forrester.com [industry]`

**Key Publications by Sector:**
| Sector | Publications |
|--------|-------------|
| Tech/SaaS | TechCrunch, The Verge, Ars Technica, Protocol |
| Marketing | Marketing Land, Adweek, Marketing Week, HubSpot Blog |
| E-commerce | Practical Ecommerce, Retail Dive, eMarketer |
| Finance | Financial Times, Bloomberg, Finextra |
| Healthcare | Fierce Healthcare, Modern Healthcare, STAT News |
| General Business | Harvard Business Review, McKinsey Insights, MIT Sloan |

**What to Extract:**
- Key trend predictions with supporting data
- Expert quotes and forecasts
- Statistical projections
- Emerging technologies or methodologies
- Regulatory changes on the horizon

### 3. Reddit Trending

**Finding Trends on Reddit:**
- Fetch: `https://www.reddit.com/r/[industry_subreddit]/top.json?t=month` — Top posts this month
- Fetch: `https://www.reddit.com/r/[industry_subreddit]/hot.json` — Current hot topics
- Web search: `site:reddit.com [industry] trend OR emerging OR growing [year]`

**Useful Trend Subreddits:**
- r/technology — Tech trends
- r/Futurology — Emerging trends
- r/dataisbeautiful — Data-driven insights
- r/startups — Startup ecosystem trends
- Industry-specific subreddits for niche trends

**Signals to Watch:**
- Topics getting unusual upvotes/engagement
- Recurring questions (signals unmet needs)
- New tools/products being discussed
- Complaints about existing solutions (opportunity signals)

### 4. GitHub Trending

**For Tech/Product Trends:**
- Fetch: `https://github.com/trending` — Overall trending repos
- Fetch: `https://github.com/trending/[language]?since=monthly` — Language-specific trends
- Web search: `github trending [technology] [year]`

**What It Reveals:**
- Emerging technologies and frameworks
- Developer interest shifts
- Open-source alternatives to paid tools
- New integration possibilities

### 5. Product Hunt

**For Product/Market Trends:**
- Web search: `site:producthunt.com [category] [year]`
- Web search: `product hunt [category] trending`

**What It Reveals:**
- New products entering the market
- Feature trends (what new products emphasize)
- Pricing model trends
- Design/UX trends
- Market demand signals (upvote patterns)

---

## Trend Analysis Framework

### Step 1: Scan (Cast a Wide Net)
1. Search across all 5 sources for the client's industry
2. Collect 20-30 potential trends
3. Record source and date for each
4. Note how many sources mention each trend

### Step 2: Filter (Separate Signal from Noise)

Score each trend on:

| Criteria | 1 (Low) | 3 (Medium) | 5 (High) |
|----------|---------|------------|----------|
| **Relevance** | Tangential to client | Related industry | Direct impact on client |
| **Momentum** | One-off mention | Multiple sources | Widespread coverage |
| **Timeframe** | 3+ years out | 1-2 years | Already happening |
| **Actionability** | Hard to act on | Possible with effort | Easy to leverage |

Keep trends scoring 12+ out of 20.

### Step 3: Analyze (Go Deep on Top Trends)

For each kept trend:
1. Research its current state and trajectory
2. Identify early adopters and results
3. Assess impact on client's market
4. Map to client's strengths/weaknesses
5. Define potential actions

### Step 4: Recommend (Make It Actionable)

For each trend, provide:
- **What it is:** Clear description
- **Why it matters:** Impact on client's market
- **Who's doing it:** Examples of companies leveraging it
- **What to do:** Specific recommendation for the client
- **When to act:** Urgency level (now, next quarter, watch)

---

## Trend Report Template

```markdown
# Trend Report: [Industry/Topic]
**Client:** [[Client Name]]
**Date:** [date]
**Period Analyzed:** [timeframe]

## Top Trends

### Trend 1: [Name]
- **Category:** [Technology / Market / Consumer / Regulatory]
- **Momentum:** [Rising / Peaking / Stabilizing / Declining]
- **Relevance Score:** [X/5]
- **Summary:** [2-3 sentences]
- **Evidence:** [Sources with links]
- **Impact on [Client]:** [Specific impact]
- **Recommended Action:** [What to do]

### Trend 2: [Name]
[Same structure]

## Emerging Signals (Watch List)
- [Signal 1]: [Brief description] — [Source]
- [Signal 2]: [Brief description] — [Source]

## Declining Trends (Phase Out)
- [Trend]: [Why it's declining] — [Implication]
```

---

## Trend Monitoring Cadence

| Frequency | Activity | Time |
|-----------|----------|------|
| Weekly | Quick scan of Reddit, HN, Product Hunt | 15 min |
| Monthly | Full trend analysis across all sources | 1 hour |
| Quarterly | Comprehensive trend report with recommendations | 2 hours |

---

## Save Location

```
vault/03-Research/[client]/trends/[date].md
```
