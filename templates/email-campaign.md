# Email Campaign: {{campaign_name}}

---

| | |
|---|---|
| **Client** | {{client_name}} |
| **Campaign Goal** | {{campaign_goal}} |
| **Target Audience** | {{target_audience}} |
| **Sequence Length** | {{sequence_length}} emails |
| **Duration** | {{campaign_duration}} |
| **Prepared By** | AI Agency — Email Team |
| **Date** | {{date}} |

---

## Campaign Overview

### Objective

{{campaign_objective}}

### Target Outcome

- **Primary Goal:** {{primary_goal}}
- **Secondary Goal:** {{secondary_goal}}
- **Revenue Target:** {{revenue_target}}

### Campaign Type

{{campaign_type}} (e.g., Welcome Series / Nurture / Re-engagement / Product Launch / Promotional)

---

## Audience Segment

| Attribute | Detail |
|---|---|
| **Segment Name** | {{segment_name}} |
| **Segment Size** | {{segment_size}} contacts |
| **Demographics** | {{segment_demographics}} |
| **Behavior Criteria** | {{segment_behavior}} |
| **Lifecycle Stage** | {{lifecycle_stage}} |
| **Source** | {{segment_source}} |
| **Exclusions** | {{segment_exclusions}} |

---

## Email 1: {{email_1_name}}

**Send Timing:** {{email_1_timing}} ({{email_1_day}})

### Subject Lines

| Version | Subject Line |
|---|---|
| **Primary** | {{email_1_subject_a}} |
| **A/B Variant B** | {{email_1_subject_b}} |
| **A/B Variant C** | {{email_1_subject_c}} |

**Preview Text:** {{email_1_preview}}

### Body Copy

{{email_1_body}}

**CTA Button:** {{email_1_cta}}
**CTA Link:** {{email_1_cta_link}}

---

## Email 2: {{email_2_name}}

**Send Timing:** {{email_2_timing}} ({{email_2_day}})
**Trigger / Delay:** {{email_2_trigger}}

### Subject Lines

| Version | Subject Line |
|---|---|
| **Primary** | {{email_2_subject_a}} |
| **A/B Variant B** | {{email_2_subject_b}} |
| **A/B Variant C** | {{email_2_subject_c}} |

**Preview Text:** {{email_2_preview}}

### Body Copy

{{email_2_body}}

**CTA Button:** {{email_2_cta}}
**CTA Link:** {{email_2_cta_link}}

---

## Email 3: {{email_3_name}}

**Send Timing:** {{email_3_timing}} ({{email_3_day}})
**Trigger / Delay:** {{email_3_trigger}}

### Subject Lines

| Version | Subject Line |
|---|---|
| **Primary** | {{email_3_subject_a}} |
| **A/B Variant B** | {{email_3_subject_b}} |
| **A/B Variant C** | {{email_3_subject_c}} |

**Preview Text:** {{email_3_preview}}

### Body Copy

{{email_3_body}}

**CTA Button:** {{email_3_cta}}
**CTA Link:** {{email_3_cta_link}}

---

## Email 4: {{email_4_name}}

**Send Timing:** {{email_4_timing}} ({{email_4_day}})
**Trigger / Delay:** {{email_4_trigger}}

### Subject Lines

| Version | Subject Line |
|---|---|
| **Primary** | {{email_4_subject_a}} |
| **A/B Variant B** | {{email_4_subject_b}} |
| **A/B Variant C** | {{email_4_subject_c}} |

**Preview Text:** {{email_4_preview}}

### Body Copy

{{email_4_body}}

**CTA Button:** {{email_4_cta}}
**CTA Link:** {{email_4_cta_link}}

---

## Email 5: {{email_5_name}}

**Send Timing:** {{email_5_timing}} ({{email_5_day}})
**Trigger / Delay:** {{email_5_trigger}}

### Subject Lines

| Version | Subject Line |
|---|---|
| **Primary** | {{email_5_subject_a}} |
| **A/B Variant B** | {{email_5_subject_b}} |
| **A/B Variant C** | {{email_5_subject_c}} |

**Preview Text:** {{email_5_preview}}

### Body Copy

{{email_5_body}}

**CTA Button:** {{email_5_cta}}
**CTA Link:** {{email_5_cta_link}}

---

## A/B Test Plan

| Email | Element Tested | Variant A | Variant B | Sample Size | Duration | Winner Criteria |
|---|---|---|---|---|---|---|
| Email 1 | {{test_1_element}} | {{test_1_a}} | {{test_1_b}} | {{test_1_sample}} | {{test_1_duration}} | {{test_1_criteria}} |
| Email 2 | {{test_2_element}} | {{test_2_a}} | {{test_2_b}} | {{test_2_sample}} | {{test_2_duration}} | {{test_2_criteria}} |
| Email 3 | {{test_3_element}} | {{test_3_a}} | {{test_3_b}} | {{test_3_sample}} | {{test_3_duration}} | {{test_3_criteria}} |
| Email 4 | {{test_4_element}} | {{test_4_a}} | {{test_4_b}} | {{test_4_sample}} | {{test_4_duration}} | {{test_4_criteria}} |
| Email 5 | {{test_5_element}} | {{test_5_a}} | {{test_5_b}} | {{test_5_sample}} | {{test_5_duration}} | {{test_5_criteria}} |

---

## Success Metrics

| Metric | Industry Benchmark | Our Target | Actual |
|---|---|---|---|
| Open Rate | {{open_benchmark}} | {{open_target}} | {{open_actual}} |
| Click-Through Rate (CTR) | {{ctr_benchmark}} | {{ctr_target}} | {{ctr_actual}} |
| Click-to-Open Rate (CTOR) | {{ctor_benchmark}} | {{ctor_target}} | {{ctor_actual}} |
| Conversion Rate | {{conv_benchmark}} | {{conv_target}} | {{conv_actual}} |
| Unsubscribe Rate | {{unsub_benchmark}} | {{unsub_target}} | {{unsub_actual}} |
| Bounce Rate | {{bounce_benchmark}} | {{bounce_target}} | {{bounce_actual}} |
| Revenue per Email | {{rpe_benchmark}} | {{rpe_target}} | {{rpe_actual}} |
| Total Revenue | — | {{revenue_target}} | {{revenue_actual}} |

### Tracking Setup

- **UTM Source:** {{utm_source}}
- **UTM Medium:** email
- **UTM Campaign:** {{utm_campaign}}
- **Conversion Page:** {{conversion_page}}

---

## Sequence Flow

```
[Email 1: {{email_1_name}}]
    |
    ├── Opened → Wait {{delay_2}} → [Email 2: {{email_2_name}}]
    └── Not Opened → Wait {{delay_2_alt}} → [Email 2 Resend: New Subject]
                                                |
                                                ├── Clicked → [Email 3: {{email_3_name}}]
                                                └── No Action → Wait {{delay_3}} → [Email 3]
                                                                                      |
                                                                                      └── [Email 4: {{email_4_name}}] → [Email 5: {{email_5_name}}]
```

---

*Prepared by AI Agency — Email Team for [[{{client_name}}]] | Confidential*
*Tags: #email #campaign #deliverable #{{client_tag}}*
