# AI Agency in a Box

### Your full-service AI agency. 7 teams. 100+ agents. Zero setup.

Clone this repo. Open it in [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Say `onboard`. That's it -- you now have a marketing, sales, strategy, content, intelligence, and management team working for you.

No API keys. No pip install. No configuration. Just results.

---

## What You Get

| Team | Agents | What They Do |
|------|--------|-------------|
| **Marketing** | 60 | SEO, social media, email campaigns, Google/Meta ads, landing pages, brand management, analytics, influencer marketing, A/B testing, competitive analysis, PR |
| **Sales** | 10 | Lead generation, qualification, cold outreach, proposals, CRM management, pipeline tracking, follow-ups, forecasting, battlecards |
| **Intelligence** | 10 | Competitor monitoring, market research, sentiment analysis, trend detection, price tracking, news monitoring, web scraping, data analysis |
| **Strategy** | 7 | SWOT analysis, growth strategy, pricing optimization, market entry planning, resource allocation, risk assessment, business model analysis |
| **Content** | 10 | Blog posts, copywriting, social content, newsletters, video scripts, podcast scripts, whitepapers, content repurposing, editorial calendars |
| **Direction** | 4 | OKR setting, priority management, vision alignment, decision frameworks |
| **Managing** | 4 | Task coordination, quality review, progress reporting, cross-team coordination |

---

## Quick Start

```
git clone https://github.com/z1fex/Agency-in-a-BOX.git
cd Agency-in-a-BOX
```

Open the folder in Claude Code, then:

```
You: onboard
```

The agency interviews you about your business, builds your client profile, and recommends what to work on first.

---

## Commands

| Command | What Happens |
|---------|-------------|
| `onboard` | Interactive client interview -- builds your full profile |
| `run marketing` | Activates the marketing team |
| `run sales` | Activates the sales team |
| `run [any team]` | Run any of the 7 teams |
| `workflow product-launch` | Full product launch campaign (11 steps) |
| `workflow lead-generation` | Build a qualified lead pipeline (8 steps) |
| `workflow content-month` | Full month of content: 4 blogs, 30 social posts, 4 newsletters, 2 video scripts |
| `workflow competitor-report` | Deep competitive intelligence report |
| `workflow seo-overhaul` | Complete SEO strategy with 100 keywords and 5 optimized posts |
| `workflow full-strategy` | End-to-end business strategy with 90-day action plan |
| `dashboard` | View agency status, active campaigns, deliverables |
| `roi` | See what the agency has produced and estimated cost savings |

See all 9 workflows in the [`workflows/`](workflows/) folder.

---

## How It Works

```
You give an objective
        |
        v
   CLAUDE.md routes it to the right team
        |
        v
   Agent reads your client profile from the vault
        |
        v
   Agent researches (web search, competitor scraping)
        |
        v
   Agent produces deliverable using templates
        |
        v
   Quality gate checks brand voice, accuracy, completeness
        |
        v
   Output saved to vault (memory) + output folder (delivery)
        |
        v
   Dashboard and ROI tracker updated
```

**The vault is your agency's brain.** It's an [Obsidian](https://obsidian.md)-compatible knowledge base that stores everything: client profiles, research, campaigns, deliverables, and competitive intelligence. Open the `vault/` folder in Obsidian to see your agency's knowledge graph visually.

---

## Project Structure

```
Agency-in-a-BOX/
|
|-- CLAUDE.md              # The brain -- tells the AI how the agency works
|-- README.md
|-- LICENSE
|
|-- agents/                # 66 agent prompt files across 7 teams
|   |-- marketing/         # 13 sub-teams (SEO, social, email, ads, etc.)
|   |-- sales/             # 10 agents (lead gen, outreach, proposals, etc.)
|   |-- intelligence/      # 10 agents (research, monitoring, analysis)
|   |-- strategy/          # 7 agents (SWOT, growth, pricing, risk)
|   |-- content/           # 10 agents (blog, copy, video, podcast, etc.)
|   |-- direction/         # 4 agents (goals, priorities, decisions)
|   |-- managing/          # 4 agents (coordination, QA, reporting)
|   +-- _base/             # Quality standards all agents follow
|
|-- workflows/             # 9 pre-built workflow chains
|-- templates/             # 12 professional deliverable templates
|-- tools/                 # Free tool guides + helper scripts
|-- onboarding/            # Client interview and profile builder
|-- quality/               # Quality gate checklist
|
|-- vault/                 # Obsidian vault (persistent memory)
|   |-- 00-Dashboard/      # Agency dashboard + ROI tracker
|   |-- 01-Clients/        # Client profiles (created during onboarding)
|   |-- 02-Campaigns/      # Campaign tracking
|   |-- 03-Research/       # Market research, trends
|   |-- 04-Intelligence/   # Competitor monitoring, sentiment
|   |-- 05-Content/        # Content library, calendars
|   |-- 06-Sales/          # Leads, proposals, pipeline
|   |-- 07-Strategy/       # SWOT, growth plans, pricing
|   +-- 08-Operations/     # QA reviews, reports
|
+-- output/                # Final deliverables organized by client/date
```

---

## Workflows

Each workflow chains multiple agents together to produce a complete deliverable package.

| Workflow | Steps | What You Get |
|----------|-------|-------------|
| **Product Launch** | 11 | Market research, competitor analysis, positioning, 3 blogs, 30 social posts, email sequence, ad copy, landing page, press release, launch calendar |
| **Lead Generation** | 8 | ICP research, 50-lead list, qualification, outreach emails, follow-ups, battlecards, proposal template |
| **Content Month** | 7 | Trend research, content calendar, 4 blogs, 30 social posts, 4 newsletters, 2 video scripts, repurposing plan |
| **Competitor Report** | 8 | Competitor scraping, SWOT per competitor, feature comparison, pricing analysis, battlecards |
| **Brand Audit** | 6 | Brand analysis, voice audit, messaging framework, brand guidelines, style guide |
| **SEO Overhaul** | 8 | Technical audit, 100 keywords, competitor SEO, content gaps, 5 optimized posts, meta descriptions, linking strategy |
| **Email Sequence** | 6 | Audience segments, welcome series (5), nurture series (5), re-engagement (3), 39 subject line A/B variants |
| **Social Media Blitz** | 7 | Platform strategy, 30 posts, hashtag playbook, engagement plan, community guidelines |
| **Full Strategy** | 10 | OKRs, SWOT, market research, competitive analysis, growth/marketing/sales/content strategy, 90-day plan, KPI dashboard |

---

## The Memory System

The `vault/` folder is an [Obsidian](https://obsidian.md)-compatible vault. It serves as the agency's persistent memory:

- **Client profiles** are stored with brand voice, competitors, ICP, and goals
- **Research** is saved and reused across sessions
- **Deliverables** are linked to clients and campaigns with `[[wikilinks]]`
- **The dashboard** tracks everything the agency produces

You can open `vault/` in Obsidian to browse, edit, and visualize the knowledge graph. Or just let the AI manage it -- it reads and writes to the vault automatically.

---

## Quality Gate

Every deliverable passes through a quality gate before delivery:

- Brand voice consistency (checked against your profile)
- Factual accuracy (all claims verified via web search)
- No placeholder text or TODOs
- Client-specific (never generic advice)
- Professional formatting using templates
- Saved to vault with proper linking

---

## Multi-Client Support

The agency supports multiple clients. Each client gets their own folder in `vault/01-Clients/` with a complete profile. Say `switch client [name]` to change context.

---

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (CLI, VS Code extension, or desktop app)
- Python 3.6+ (only for optional helper scripts in `tools/scripts/`)

That's it. No API keys, no packages, no environment variables.

---

## ROI Tracking

The agency tracks everything it produces in `vault/00-Dashboard/ROI Tracker.md`:

- Content pieces created
- Research reports generated
- Leads researched and qualified
- Campaigns planned
- Estimated cost savings at industry rate ($150/hr)

After a single `workflow content-month` run, you'll have ~40 deliverables worth an estimated $3,000+ in agency fees.

---

## Example Session

```
You: onboard

Agency: Welcome to your AI Agency! Let's set up your profile.
        What's your company name?

You: FreshBrew Coffee, we sell single-origin coffee beans online

Agency: [asks about target market, competitors, brand voice, goals...]
        [creates 5 vault files: profile, brand voice, competitors, ICP, goals]

        Your profile is set up! Based on your goals, I recommend:
        1. workflow content-month (build your content engine)
        2. workflow seo-overhaul (fix your organic search)
        3. workflow lead-generation (build your pipeline)

You: workflow content-month

Agency: [researches trends, plans calendar, writes 4 blogs, 30 social posts,
         4 newsletters, 2 video scripts, runs quality gate, saves everything]

You: dashboard

Agency: FreshBrew Coffee | Active | 40 deliverables | $3,075 value generated
```

---

## Contributing

Contributions are welcome. Here's how:

1. Fork the repo
2. Create a branch (`git checkout -b feature/new-workflow`)
3. Add your agents, workflows, or templates
4. Submit a pull request

**Ideas for contributions:**
- New agents for existing teams
- New workflow chains
- Industry-specific templates
- Translations

---

## License

MIT License -- see [LICENSE](LICENSE) for details.

---

**Built for business owners who want agency-level output without agency-level costs.**
