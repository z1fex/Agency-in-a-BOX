# Social Listening Guide

> Free methods for monitoring brand mentions, sentiment, and industry conversations using Claude Code.

---

## Available Free Sources

### 1. Reddit (JSON API)

Reddit exposes every page as JSON by appending `.json` to the URL. No API key needed.

**Search Reddit:**
- Web search: `site:reddit.com "[brand name]"` or `site:reddit.com [topic]`
- Fetch: `https://www.reddit.com/search.json?q=[query]&sort=relevance&t=month`

**Subreddit Monitoring:**
- Fetch: `https://www.reddit.com/r/[subreddit]/new.json?limit=25`
- Fetch: `https://www.reddit.com/r/[subreddit]/search.json?q=[query]&restrict_sr=1&sort=new`

**Useful Subreddits by Industry:**
- **SaaS/Tech:** r/SaaS, r/startups, r/entrepreneur, r/smallbusiness
- **Marketing:** r/marketing, r/digital_marketing, r/SEO, r/socialmedia
- **Design:** r/web_design, r/userexperience, r/graphic_design
- **E-commerce:** r/ecommerce, r/shopify, r/FulfillmentByAmazon
- **Industry-specific:** Search for subreddits related to client's industry

**What to Extract:**
- Brand mentions (positive, negative, neutral)
- Competitor mentions and sentiment
- Common questions and pain points
- Feature requests and complaints
- Product recommendations threads
- "What tool do you use for X?" threads

### 2. Hacker News (Algolia API)

**Search HN:**
- Fetch: `https://hn.algolia.com/api/v1/search?query=[term]&tags=story`
- Fetch: `https://hn.algolia.com/api/v1/search?query=[term]&tags=comment`
- Fetch: `https://hn.algolia.com/api/v1/search_by_date?query=[term]` (most recent)

**Useful Queries:**
- `[brand name]` — Direct mentions
- `[product category]` — Industry discussions
- `"Show HN" [category]` — New product launches in the space
- `"Ask HN" [topic]` — Questions from the community

**What to Extract:**
- Tech community sentiment
- Early adopter opinions
- Technical critiques
- Emerging trends and tools

### 3. Google Search for Reviews & Mentions

**Review Sites:**
- Web search: `"[brand]" site:g2.com`
- Web search: `"[brand]" site:capterra.com`
- Web search: `"[brand]" site:trustpilot.com`
- Web search: `"[brand]" site:producthunt.com`
- Web search: `"[brand]" review [year]`

**Social Mentions:**
- Web search: `"[brand]" site:twitter.com` or `"[brand]" site:x.com`
- Web search: `"[brand]" site:linkedin.com`
- Web search: `"[brand]" site:youtube.com`

**Forum Discussions:**
- Web search: `"[brand]" forum OR discussion OR thread`
- Web search: `"[brand]" alternative OR switch OR migrate`

### 4. Twitter/X Search

**Via Web Search:**
- `"[brand]" site:x.com` — Find tweets mentioning the brand
- `"[brand]" OR "@[handle]" site:x.com` — Brand + handle mentions

**Useful Search Patterns:**
- `"[brand]" love OR great OR amazing site:x.com` — Positive sentiment
- `"[brand]" hate OR terrible OR worst site:x.com` — Negative sentiment
- `"[brand]" vs "[competitor]" site:x.com` — Comparison discussions
- `"[brand]" alternative site:x.com` — Churn signals

### 5. Product Hunt

**Via Web Search and Fetch:**
- Web search: `site:producthunt.com "[brand]"`
- Fetch product pages for launch comments and upvote counts

---

## Monitoring Playbook

### Daily Quick Check (5 min)
1. Search Reddit for brand mentions (last 24 hours)
2. Search Google for new reviews
3. Check HN for industry mentions

### Weekly Deep Dive (30 min)
1. All daily checks
2. Competitor mention analysis
3. Industry trend scan on Reddit and HN
4. Review site sentiment summary
5. Save findings to vault

### Monthly Report (1 hour)
1. Compile all weekly findings
2. Sentiment trend analysis
3. Top themes and topics
4. Competitor sentiment comparison
5. Actionable recommendations

---

## Sentiment Analysis Framework

When reading mentions, categorize each as:

| Sentiment | Indicators | Action |
|-----------|-----------|--------|
| **Positive** | Praise, recommendations, success stories | Capture for testimonials, case studies |
| **Negative** | Complaints, frustrations, churn signals | Flag for product/support team |
| **Neutral** | Questions, comparisons, general mentions | Monitor for trends |
| **Feature Request** | "I wish", "it would be great if", "does it support" | Log for product roadmap |
| **Competitor Win** | "Switched to [competitor]", "[competitor] is better" | Analyze why, update battlecards |

---

## Output Template

Save monitoring results to vault:

```markdown
# Social Listening Report: [Client]
**Period:** [date range]
**Sources Monitored:** Reddit, HN, Review Sites, Twitter/X

## Mention Summary
| Source | Positive | Negative | Neutral | Total |
|--------|----------|----------|---------|-------|
| Reddit | X | X | X | X |
| HN | X | X | X | X |
| Reviews | X | X | X | X |
| Twitter | X | X | X | X |

## Key Themes
1. [Theme with examples]
2. [Theme with examples]

## Notable Mentions
- [Quote] — [Source] — [Sentiment]
- [Quote] — [Source] — [Sentiment]

## Competitor Mentions
- [Competitor]: [Summary of sentiment]

## Action Items
- [ ] [Action based on findings]
```

---

## Save Location

```
vault/04-Intelligence/[client]/social-listening/[date].md
```
