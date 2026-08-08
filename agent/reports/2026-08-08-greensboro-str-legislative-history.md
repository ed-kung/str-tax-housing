# Greensboro, NC — Short-term rental legislative history

**Summary:** Greensboro’s primary STR framework is the May 23, 2023 LDO amendment (Agenda ID 2023-320 / §30-8-10.4(U)), delayed by Ord. 23-165 to **2024-04-01** enforcement, with the 750-foot spacing rule repealed **2025-02-18** after legal challenge risk. State rental-registration preemption (S.L. 2011-281 → 2016-122 → 2019-73 → 160D-1207) and S.L. 2019-246 facilitator occupancy-tax duties shape the city’s approach. Greensboro has a 3% municipal occupancy tax; Airbnb currently collects local city/county occupancy taxes in NC, but no documented first collection date was found (`airbnb_tax_collection_date`: null). No Airbnb–city data connection found.

## City processed

- **City:** Greensboro, North Carolina  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 68)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Pre-2023.** LDO lacked an STR definition; staff sometimes used Tourist Home/Bed-and-Breakfast rules (Special Use Permit in some cases). Contemporary news described STRs as not specifically regulated.

2. **Primary framework (2023-05-23; enforced 2024-04-01).** Zoning permit; Homestay (primary residence + host on-site) vs Whole House (local operator in Guilford or adjacent county); occupancy/gathering/parking/multifamily caps; originally 750-ft separation. Effective date delayed from 2024-01-01 to **2024-04-01** by Ord. 23-165 (2023-12-05).

3. **Spacing repeal (2025-02-18).** Agenda ID 2025-128 removed only the 750-ft rule after lawsuit/legal concerns tied to *Schroeder* / G.S. 160D-1207(c); other STR standards remain.

4. **State preemption & tax law.** S.L. 2011-281, 2016-122, 2019-73, 2019-111/2020-25 constrain registration-style rules. S.L. 2019-246 (eff. 2020-02-01) makes accommodation facilitators liable for city occupancy tax under G.S. 160A-215 (Greensboro listed).

5. **Airbnb tax collection:** **null** — municipal 3% tax exists and Airbnb now collects NC city/county occupancy taxes, but 2015 VCA excluded Guilford; no Greensboro-specific first-collection date found.

6. **Airbnb data sharing:** **null** — no City Portal / API / compliance feed documented.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| S.L. 2011-281 (SB 683) | State of North Carolina | 2011-06-23 | 2011-06-23 | 2011-06-23 | false |
| S.L. 2016-122 (SB 326) | State of North Carolina | 2016-07-28 | 2017-01-01 | 2017-01-01 | false |
| S.L. 2019-73 (SB 483) | State of North Carolina | 2019-07-01 | 2019-07-01 | 2019-07-01 | false |
| S.L. 2019-111 / 2020-25 | State of North Carolina | 2019-07-11 | 2020-06-19 | 2020-06-19 | false |
| S.L. 2019-246 (SB 557) | State of North Carolina | 2019-11-08 | 2020-02-01 | 2020-02-01 | false |
| Ord. 2023-320 (LDO STR standards) | City of Greensboro | 2023-05-23 | 2024-04-01 | 2024-04-01 | true |
| Ord. 23-165 (2023-847 delay) | City of Greensboro | 2023-12-05 | 2023-12-05 | 2023-12-05 | false |
| Ord. 2025-128 (remove 750-ft rule) | City of Greensboro | 2025-02-18 | 2025-02-18 | 2025-02-18 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Greensboro entry)
- Script: `agent/scripts/update_greensboro_str_regulations.py`
- Report: `agent/reports/2026-08-08-greensboro-str-legislative-history.md`

## Key sources

- City of Greensboro STR page; Dec. 8, 2023 news release (April 1, 2024 effective date); proposed/adopted LDO amendment PDF (showpublisheddocument/56092)
- Greensboro City Council minutes: May 23, 2023 adoption (agenda ID 2023-320); Dec. 5, 2023 Ord. 23-165 / 2023-847; Feb. 18, 2025 agenda ID 2025-128
- Rhino Times / Yes Weekly / WFDD / FOX8 coverage of May 2023 adoption, Dec 2023 delay, Feb 2025 spacing repeal and lawsuit
- Airbnb help articles 3605 (Greensboro) and 2320 (NC occupancy taxes)
- N.C. Session Laws 2011-281, 2016-122, 2019-73, 2019-111, 2020-25, 2019-246; G.S. 160A-215; UNC SOG Coates’ Canons (McLaughlin, Nov. 2022) on Airbnb occupancy-tax remittance
- City ACFR / Guilford County occupancy-tax materials (3% city + 3% county)
