# Client Onboarding — Welcome to Your AI Agency

## Instructions for Claude Code

When the user says `onboard`, follow this interview process step by step. **Be conversational and friendly** — this is their first impression of the agency. Do NOT dump all questions at once. Ask one phase at a time, wait for answers, then move to the next phase.

Start with this greeting:

> "Welcome to your AI Agency! I'm excited to get started. I'll ask you some questions about your business so I can set up your client profile and tailor everything we do to your needs. This takes about 5-10 minutes, and once we're done, you'll have a full agency team ready to work for you.
>
> Let's start with the basics."

---

## Phase 1 — Company Basics

Ask these questions conversationally (adapt based on their answers — don't be robotic):

1. **What's your company name?** (And your website URL if you have one)
2. **What industry are you in?**
3. **How long have you been in business, and roughly how big is the team?** (Just you? 5 people? 50? 500?)
4. **What do you sell?** Walk me through your main products or services, and roughly what they cost.
5. **What's your unique value proposition?** In one sentence, why should someone choose you over alternatives?

After they answer, briefly summarize what you heard and confirm before moving on:
> "Got it — so you're [summary]. Let me ask about your customers next."

---

## Phase 2 — Target Market

1. **Who is your ideal customer?** Paint me a picture — demographics, job titles, company size, whatever is relevant.
2. **What are the top 3 pain points you solve for them?**
3. **Where do your customers find you, or where do they hang out online?** (LinkedIn? Google search? TikTok? Industry forums? Referrals?)
4. **What's your average deal size or customer lifetime value?** (Rough numbers are fine — just helps me prioritize the right strategies)

Summarize and confirm:
> "So your ideal customer is [summary], and they're struggling with [pain points]. Great — now let's look at the competition."

---

## Phase 3 — Competition

1. **Who are your top 3-5 competitors?** (Names and websites if you have them)
2. **What makes you genuinely different from them?** Not marketing speak — the real answer.
3. **What do your competitors do better than you?** (Be honest — it helps me know where to focus)

If the user doesn't know competitors or only names a couple, offer to research:
> "No worries — I can research your competitive landscape after we finish onboarding. My Intelligence team is great at this."

---

## Phase 4 — Brand & Voice

1. **If your brand were a person, how would you describe their personality?** Give me 3-5 adjectives. (e.g., bold, witty, trustworthy, nerdy, warm)
2. **Formal or casual?** Where do you fall on the spectrum? Think buttoned-up corporate vs. texting a friend.
3. **Any words or phrases you love using? Any you absolutely hate?** (Industry jargon you embrace or avoid, etc.)
4. **Can you point me to a piece of content — yours or someone else's — that feels like the vibe you're going for?** (A blog post, ad, social account, anything)

---

## Phase 5 — Goals & Priorities

1. **What are your top 3 business goals right now?** (Could be growth, leads, brand awareness, product launch, anything)
2. **What's your single biggest marketing or sales challenge today?**
3. **What have you tried before that didn't work?** (So we don't repeat mistakes)
4. **What does success look like for you in 90 days?** Be specific — numbers, outcomes, feelings.
5. **What's your monthly budget for marketing and sales?** (Rough range is fine — helps me recommend the right strategies)

---

## After the Interview — File Creation

Once you have all answers (it's okay if some are partial — work with what you've got), do the following:

### Step 1: Create the Client Folder

Create the folder: `vault/01-Clients/[Company Name]/`

### Step 2: Create profile.md

Save to: `vault/01-Clients/[Company Name]/profile.md`

Use the template from `vault/01-Clients/_Client Template.md` but fill in ALL gathered information. Replace every `{{placeholder}}` with real answers. If something wasn't answered, write "To be determined" — never leave placeholders in a live profile.

Frontmatter must include:
```yaml
---
client: "[Company Name]"
industry: "[Industry]"
website: "[URL]"
onboarded: "[Today's Date]"
status: active
tags:
  - client
---
```

### Step 3: Create brand-voice.md

Save to: `vault/01-Clients/[Company Name]/brand-voice.md`

Structure:
```markdown
---
tags:
  - client
  - brand-voice
client: "[Company Name]"
---

# [Company Name] — Brand Voice Guide

## Personality
[The 3-5 adjectives they gave, with brief explanations of what each means in practice]

## Tone Spectrum
[Where they fall on formal-to-casual, with examples of how this sounds]

## Voice Dos
- [Words and phrases to use]
- [Tone qualities to maintain]
- [Sentence style preferences]

## Voice Don'ts
- [Words and phrases to avoid]
- [Tones to never use]
- [Common mistakes to watch for]

## Example Content They Like
[Links or descriptions they provided]

## Writing Samples
[Generate 2-3 sample sentences in their voice so agents can reference this]
```

### Step 4: Create competitors.md

Save to: `vault/01-Clients/[Company Name]/competitors.md`

Structure:
```markdown
---
tags:
  - client
  - competitors
client: "[Company Name]"
---

# [Company Name] — Competitive Landscape

## Our Position
[Summary of the client's differentiation]

## Competitor Analysis

### [Competitor 1]
- **Website:** [URL]
- **What They Do Well:** [Strengths]
- **Where They're Weak:** [Weaknesses]
- **How We Beat Them:** [Client's advantage]

[Repeat for each competitor]

## Competitive Gaps & Opportunities
[Based on what the client shared, identify 2-3 opportunities]
```

### Step 5: Create icp.md

Save to: `vault/01-Clients/[Company Name]/icp.md`

Structure:
```markdown
---
tags:
  - client
  - icp
client: "[Company Name]"
---

# [Company Name] — Ideal Customer Profile

## Demographics
[Everything gathered about ideal customer]

## Pain Points
1. [Pain point 1 — with context]
2. [Pain point 2 — with context]
3. [Pain point 3 — with context]

## Where to Find Them
[Channels and platforms where ICP hangs out]

## Buying Behavior
- **Average Deal Size:** $[X]
- **Customer Lifetime Value:** $[X]
- **Decision Process:** [What we know]
- **Key Objections:** [Common objections to anticipate]

## Messaging That Resonates
[Based on pain points and brand voice, draft 3-5 key messages]
```

### Step 6: Create goals.md

Save to: `vault/01-Clients/[Company Name]/goals.md`

Structure:
```markdown
---
tags:
  - client
  - goals
client: "[Company Name]"
---

# [Company Name] — Goals & Success Criteria

## Top 3 Business Goals
1. [Goal 1 — with context and any numbers]
2. [Goal 2 — with context]
3. [Goal 3 — with context]

## Biggest Challenge
[Their single biggest marketing/sales pain]

## What Has NOT Worked
[Past failures to avoid repeating]

## 90-Day Success Criteria
[Specific, measurable outcomes they want in 90 days]

## Budget
- **Monthly Marketing/Sales Budget:** $[X]
- **Budget Notes:** [Any constraints or preferences]

## Recommended Priority Actions
[Based on goals, suggest 3-5 immediate actions the agency should take]
```

### Step 7: Update the Dashboard

Open `vault/00-Dashboard/Agency Dashboard.md` and:
- Replace "No client onboarded yet" with the new client name and link: `[[Company Name]]`
- Add an entry to Recent Activity: today's date, "Client onboarded", "Managing", "Complete"
- Update Stats Summary: increment any relevant counters

### Step 8: Recommend Next Steps

After saving everything, tell the user:

> "Your profile is set up! Here's what I've created for you:
>
> - **Client Profile** — Your complete business overview
> - **Brand Voice Guide** — So everything we create sounds like you
> - **Competitive Landscape** — Your position vs. competitors
> - **Ideal Customer Profile** — Who we're targeting
> - **Goals & Success Criteria** — Our north star for the next 90 days
>
> Based on your goals, here are the 3 workflows I'd recommend starting with:"

Then recommend 3 workflows from the `workflows/` folder that best match their stated goals. For each recommendation, explain WHY it fits their situation in 1-2 sentences.

Common matches:
- High-growth goal → `workflow content-month` or `workflow full-strategy`
- Need leads → `workflow lead-generation`
- Brand building → `workflow brand-audit` or `workflow social-media-blitz`
- Competitive pressure → `workflow competitor-report`
- Product launch → `workflow product-launch`
- Need SEO → `workflow seo-overhaul`
- Email marketing → `workflow email-sequence`

Finally, ask:
> "What would you like to work on first? Pick a workflow above, or tell me what's most urgent and I'll point you to the right team."

---

## Tips for a Great Onboarding

- **Don't interrogate.** If the user gives short answers, work with what you have. You can always learn more later.
- **Offer to research.** If they don't know competitors, market data, or industry benchmarks, tell them you'll research it.
- **Be encouraging.** Especially for small businesses or solopreneurs — make them feel like they just hired a real team.
- **Adapt.** If they're B2B, lean into company size/role titles. If they're B2C, lean into demographics/interests. If they're a creator, lean into audience and content.
- **Never leave blanks.** Every field should have either a real answer or "To be determined — will research."
