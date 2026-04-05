# Email Sequence
> **Teams:** Strategy, Marketing (Email, A/B Testing), Content | **Estimated steps:** 6

## What You'll Get
- Audience segmentation document (3-5 segments)
- Email marketing strategy with sending cadence
- Welcome series (5 emails with 2-day spacing)
- Nurture series (5 emails with weekly spacing)
- Re-engagement series (3 emails for inactive subscribers)
- A/B subject line variants (3 per email, 39 total)

## Prerequisites
- Active client profile in vault (run `onboard` first)

## Steps

### Step 1: Audience Segments
**Read:** `agents/strategy/growth-strategist.md`
**Do:** Define 3-5 audience segments based on buyer stage, persona type, industry vertical, and engagement level. For each segment: pain points, motivations, objections, and preferred content types.
**Save:** `vault/07-Strategy/[client]/email-segments-[date].md`

### Step 2: Email Strategy
**Read:** `agents/marketing/email/campaign-builder.md`
**Do:** Define email strategy — sending frequency, optimal send times, content mix, progression logic, conversion goals per series, key metrics to track, and unsubscribe handling.
**Save:** `vault/02-Campaigns/[client]/email-strategy-[date].md`

### Step 3: Welcome Series (5 Emails)
**Read:** `agents/marketing/email/campaign-builder.md`
**Do:** Write 5-email welcome series with 2-day spacing: (1) Welcome + brand story + quick win, (2) Problem education + thought leadership, (3) Solution overview + social proof, (4) Case study or success story, (5) Soft CTA + next steps. Each email: subject line, preview text, body, CTA, P.S. line.
**Save:** `output/[client]/[date]/email-sequence/welcome-series.md`

### Step 4: Nurture Series (5 Emails)
**Read:** `agents/content/newsletter-writer.md`
**Do:** Write 5-email nurture series with weekly spacing: (1) Deep-dive into primary pain point, (2) How-to guide or framework, (3) Industry trends + client perspective, (4) Comparison/evaluation guide, (5) ROI calculator or assessment offer. Each email: subject line, preview text, body, CTA.
**Save:** `output/[client]/[date]/email-sequence/nurture-series.md`

### Step 5: Re-engagement Series (3 Emails)
**Read:** `agents/marketing/email/campaign-builder.md`
**Do:** Write 3-email re-engagement series for inactive subscribers: (1) "We miss you" + compelling new content/offer, (2) "What changed?" survey + exclusive incentive, (3) "Last chance" + clear consequences. Tone: respectful and value-focused.
**Save:** `output/[client]/[date]/email-sequence/reengagement-series.md`

### Step 6: Subject Line A/B Variants
**Read:** `agents/marketing/ab-testing/experiment-designer.md`
**Do:** Create 3 subject line variants for each of the 13 emails (39 total). Test dimensions: curiosity vs. benefit, short vs. long, question vs. statement, personalization vs. generic. Include hypothesis for each test.
**Save:** `output/[client]/[date]/email-sequence/ab-variants.md`

### Final Delivery
1. Run quality gate (`quality/qa-checklist.md`) on all email series
2. Save all deliverables to `output/[client]/[date]/email-sequence/`
3. Update `vault/00-Dashboard/Agency Dashboard.md` with email campaign summary
4. Update `vault/00-Dashboard/ROI Tracker.md` — log 13 emails written, 39 subject line variants
