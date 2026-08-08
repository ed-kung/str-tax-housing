# Colorado Springs, CO short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Colorado Springs, CO (first unchecked city). The city’s first STR framework was Ordinance 18-112 (passed 2018-11-13; effective 2018-12-31; program enforcement ~2019-01-02). The current two-tier regime was set by Ordinance 19-101 (passed 2019-12-19; effective/enforced 2019-12-26), barring new non-owner-occupied STRs in single-family zones and imposing a 500-foot separation elsewhere. Occupancy caps (Ord. 19-82) and tax-clearance for permits (Ord. 19-49) followed in 2019–2020. Marketplace facilitators must collect City sales tax under Ord. 20-47 (operative 2020-09-01); Airbnb currently also remits the City’s 2% lodging tax. Ord. 25-45 (2025) bars combining ADUs with STRs after 2025-06-30 (with grandfathering). No documented Airbnb–City direct data-sharing connection; `airbnb_data_sharing_date` is null.

## What was done

- Identified first list item lacking `agent_checked`: Colorado Springs, CO (index 38).
- Reviewed Colorado Springs Legistar/signed ordinances (18-112, 19-49, 19-82, 19-101, 20-47, 25-45), City STR program page (`coloradosprings.gov/str`), AmLegal code, CML marketplace-facilitator tracking, Airbnb Colorado tax help article 2298, and VRBO/Avalara secondary sources.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| First city framework | Ord. 18-112 (2018) created annual STR permits, sales-tax license, insurance, local contact, and operating rules; program ~2019-01-02. |
| Current location/owner rules | Ord. 19-101 (2019-12-26) created owner-occupied (≥185 days) vs non-owner-occupied tiers; new non-owner STRs banned in single-family zones; 500-ft separation elsewhere. |
| Occupancy | Ord. 19-82: 2/bedroom + 2/unit, max 15 (operative ~2020-02-18 per 90-day clause). |
| Municipal platform tax | Ord. 20-47 marketplace-facilitator duties operative **2020-09-01**; Airbnb help confirms City sales (3.07%) + lodging (2%) remittance. |
| ADU interaction | Ord. 25-45: no STR on properties with ADUs after **2025-06-30**, with limited grandfathering. |
| Airbnb tax date | **2020-09-01** — grounded in Ord. 20-47 / CML; Airbnb currently collects City sales + lodging taxes. |
| Airbnb data sharing | **null** — no documented API/City Portal feed; permit display + code enforcement. |

## Legislative history recorded

1. **Ord. 18-112 (STR Part 17)** — City of Colorado Springs — Passage 2018-11-13; effective 2018-12-31; enforced 2019-01-02 — `primary_framework`: true  
2. **Ord. 19-49 (tax remittance for permits)** — Passage 2019-07-23; effective/enforced 2019-08-05 — `primary_framework`: false  
3. **Ord. 19-82 (occupancy limits)** — Passage 2019-11-12; effective/enforced 2020-02-18 — `primary_framework`: false  
4. **Ord. 19-101 (owner / non-owner location rules)** — Passage 2019-12-19; effective/enforced 2019-12-26 — `primary_framework`: true  
5. **Ord. 20-47 (marketplace facilitators / economic nexus)** — Passage 2020-07-28; effective/enforced 2020-09-01 — `primary_framework`: false  
6. **Ord. 25-45 (ADU; STR combination ban)** — Passage 2025-04-08; effective 2025-04-21; enforced 2025-06-30 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Colorado Springs, CO entry)
- Report: `agent/reports/2026-08-08-colorado-springs-str-legislative-history.md`
