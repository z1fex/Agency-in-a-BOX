# Quality Gate — Pre-Delivery Checklist

Every deliverable produced by this agency MUST pass through this quality gate before being delivered to the client or saved as a final output. No exceptions.

**How to use:** Before finalizing any deliverable, read this checklist and verify every item. If any check fails, fix the issue before delivery. Record the QA result in `vault/08-Operations/`.

---

## Brand Consistency

- [ ] **Matches client's brand voice** — Cross-reference `vault/01-Clients/[client]/brand-voice.md` and verify tone, personality, and word choices align
- [ ] **Uses approved terminology** — No banned words or phrases; uses the client's preferred language
- [ ] **Tone fits target audience** — Cross-reference `vault/01-Clients/[client]/icp.md` to ensure the tone resonates with the ideal customer
- [ ] **Consistent with previous deliverables** — Check `vault/05-Content/` and `output/` for past work; ensure stylistic consistency

---

## Accuracy

- [ ] **All facts verified via web search** — Every factual claim must be verified; do not rely on training data alone
- [ ] **All claims have sources cited** — Include links or references for statistics, quotes, and data points
- [ ] **Statistics are current** — Data should be from the last 12 months unless historical context is specifically needed
- [ ] **No hallucinated data** — Zero tolerance for made-up statistics, fake company names, fabricated quotes, or invented case studies
- [ ] **Competitor information is accurate** — Cross-reference `vault/01-Clients/[client]/competitors.md` and verify with live web data

---

## Completeness

- [ ] **No placeholder text** — Search for `{{`, `}}`, `TODO`, `TBD`, `FIXME`, `[insert`, `[placeholder`, `lorem ipsum` — none should exist in final output
- [ ] **All sections filled in** — Every section of the deliverable template is complete; no empty headers or skeletal outlines
- [ ] **Actionable recommendations** — Every recommendation includes specific steps, not vague advice like "improve your marketing"
- [ ] **Client-specific** — All content is tailored to this specific client; nothing is generic or could apply to any business
- [ ] **Includes next steps** — Every deliverable ends with clear next actions for the client or the agency

---

## Formatting

- [ ] **Uses correct template** — Check `templates/` for the appropriate template; deliverable structure should match
- [ ] **Client name and date included** — Frontmatter or header includes client name and creation date
- [ ] **Professional formatting** — Consistent headers, clean tables, proper markdown syntax, no broken formatting
- [ ] **Table of contents for long documents** — Any deliverable over 500 words should include a TOC or clear section navigation
- [ ] **Readable** — Short paragraphs, bullet points where appropriate, clear hierarchy; no walls of text

---

## Vault Integration

- [ ] **Saved to correct vault location** — Deliverable is in the right `vault/` subfolder per the vault structure
- [ ] **Tagged appropriately** — Frontmatter includes relevant tags: `#deliverable`, `#client`, `#campaign`, team tag, content type
- [ ] **Linked to client profile** — Uses `[[wikilinks]]` to connect to the client's profile, campaign, and related documents
- [ ] **Dashboard updated** — `vault/00-Dashboard/Agency Dashboard.md` reflects the new deliverable in Recent Activity and Stats
- [ ] **ROI tracker updated** — `vault/00-Dashboard/ROI Tracker.md` has a new entry for this deliverable with hours saved and value

---

## Final Signoff

After all checks pass:

1. Add a QA note to the deliverable's frontmatter:
   ```yaml
   qa_status: passed
   qa_date: YYYY-MM-DD
   ```

2. Save a QA record to `vault/08-Operations/` with:
   - Deliverable name and path
   - Date reviewed
   - Any issues found and how they were resolved
   - Final status: PASSED or FAILED (with reasons)

3. Copy the final deliverable to `output/[client-name]/[YYYY-MM-DD]/`

---

## Quality Standards by Deliverable Type

| Type | Min Word Count | Must Include | Extra Checks |
|------|---------------|--------------|--------------|
| Blog Post | 800 | Sources, CTA, SEO keywords | Readability score, keyword density |
| Social Post | 20 | Hashtags, CTA | Platform-appropriate length and format |
| Email Campaign | 200 | Subject line, CTA, preview text | Spam word check, mobile-friendly |
| Competitor Analysis | 500 | Data sources, comparison table | Verify all competitor data is current |
| Sales Proposal | 600 | Pricing, timeline, deliverables | Customized to prospect's stated needs |
| Strategy Document | 1000 | Data backing, action items, timeline | Executive summary included |
| Market Research | 800 | Sources, data tables, insights | All data points sourced and dated |
| SEO Audit | 500 | Technical issues, keyword gaps, action plan | Verified with live site data |
| Ad Copy | 50 | Headline, body, CTA | Character limits per platform |
| Landing Page | 300 | Headline, benefits, CTA, social proof | Mobile-responsive structure |

---

> **Remember:** A deliverable that fails quality gate is worse than no deliverable at all. It damages trust. Take the extra 2 minutes to check everything.
