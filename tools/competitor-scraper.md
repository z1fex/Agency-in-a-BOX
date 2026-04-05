# Competitor Scraper Guide

> How to use Claude Code's web fetch to systematically analyze competitor websites.

---

## How It Works

Claude Code can fetch and read any public webpage. This guide shows how to systematically analyze competitor sites to extract positioning, pricing, features, messaging, and strategy signals.

---

## Scraping Playbook

### Step 1: Homepage Analysis

**Fetch:** `[competitor].com`

**Extract:**
- **Hero headline:** What's their primary value proposition?
- **Sub-headline:** How do they explain what they do?
- **CTA text:** What action do they want visitors to take? (e.g., "Start Free Trial" vs "Book a Demo" vs "Get Started")
- **Social proof:** Logos, testimonial quotes, user counts
- **Navigation structure:** What pages do they prioritize?
- **Above-the-fold messaging:** What problem do they lead with?

**Save as:**
```markdown
## Homepage Analysis: [Competitor]
- **Headline:** "[exact headline]"
- **Sub-headline:** "[exact sub-headline]"  
- **Primary CTA:** [button text] → [destination]
- **Social Proof:** [logos/numbers/testimonials shown]
- **Key Messaging Themes:** [list]
```

### Step 2: Pricing Page

**Fetch:** `[competitor].com/pricing`

**Extract:**
- Tier names and prices
- Features per tier
- Pricing model (per user, per month, usage-based, flat rate)
- Free tier or trial availability and limitations
- Enterprise/custom pricing signals
- Annual vs monthly discount
- Hidden costs (setup fees, overages, add-ons)

**Save as:**
```markdown
## Pricing: [Competitor]
| Tier | Price | Key Features | Limits |
|------|-------|-------------|--------|
| [tier] | [price] | [features] | [limits] |
```

### Step 3: Product/Features Pages

**Fetch:** `[competitor].com/features` or `/product`

**Extract:**
- Feature categories and specific features
- How they describe each feature (benefit-driven vs technical)
- Screenshots or demo descriptions (note what they choose to show)
- Integration partnerships
- What they emphasize most (usually their strongest differentiators)

### Step 4: About Page

**Fetch:** `[competitor].com/about`

**Extract:**
- Mission/vision statements
- Company story and founding date
- Team size indicators
- Leadership team names and backgrounds
- Office locations
- Culture signals
- Investor/backer names

### Step 5: Blog/Content

**Fetch:** `[competitor].com/blog`

**Extract:**
- Publishing frequency
- Content categories/topics
- Content types (how-to, thought leadership, product updates, case studies)
- Authors (in-house vs guest)
- Engagement indicators (comments, shares if visible)
- SEO strategy signals (what keywords they target in titles)

### Step 6: Case Studies/Testimonials

**Fetch:** `[competitor].com/customers` or `/case-studies`

**Extract:**
- Client industry verticals
- Company sizes they showcase
- Results/metrics they highlight
- Testimonial themes (what customers praise most)
- Use cases they promote

### Step 7: Careers Page

**Fetch:** `[competitor].com/careers`

**Extract:**
- Total open positions (growth indicator)
- Departments hiring most (strategic priorities)
- Tech stack (from engineering job posts)
- New role types (signals new product areas)
- Location requirements (expansion plans)

---

## Analysis Framework

After scraping, organize findings into:

### Messaging Analysis
| Element | Competitor A | Competitor B | Competitor C | Our Client |
|---------|-------------|-------------|-------------|------------|
| Primary Value Prop | | | | |
| Target Persona | | | | |
| Key Benefit | | | | |
| Proof Points | | | | |
| Tone/Voice | | | | |
| CTA Strategy | | | | |

### Feature Matrix
Build from product pages — see `templates/competitive-analysis.md`

### Pricing Matrix
Build from pricing pages — compare tiers, models, and value

### Content Strategy Comparison
| Aspect | Competitor A | Competitor B | Competitor C |
|--------|-------------|-------------|-------------|
| Blog Frequency | | | |
| Top Topics | | | |
| Content Types | | | |
| SEO Focus | | | |
| Social Channels | | | |

---

## Pro Tips

- **Check robots.txt first:** Fetch `[competitor].com/robots.txt` to understand what they restrict
- **Check sitemap:** Fetch `[competitor].com/sitemap.xml` to discover all public pages
- **Look at page source context:** Meta descriptions and title tags reveal SEO strategy
- **Check for schema markup mentions** in content — signals SEO maturity
- **Note what's missing:** Sometimes what a competitor DOESN'T show is as informative as what they do
- **Save raw data:** Always save the raw scraped content to vault before analysis
- **Date-stamp everything:** Competitor sites change — record when you analyzed them
- **Check Web Archive:** Search for `web.archive.org/web/*/[competitor].com` to see how their messaging has evolved

---

## Output Location

Save all competitor scrape data to:
```
vault/04-Intelligence/[client]/scrapes/[competitor]-[date].md
```
