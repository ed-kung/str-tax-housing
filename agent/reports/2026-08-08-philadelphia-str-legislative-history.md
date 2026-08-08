# Philadelphia, PA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Philadelphia, PA (first unchecked city). Philly’s STR regime began with Bill 150441-A (2015), which legalized Limited Lodging and authorized booking-agent collection of the City’s 8.5% hotel tax; Bill 210081 (2021) replaced the day-count tiers with universal operator/booking-agent licensing, with platform license verification enforced from 2023-01-01. Airbnb began collecting Philadelphia municipal hotel tax on 2015-07-15; the first operational Airbnb–city listing-compliance data connection is 2023-01-01.

## What was done

- Identified first list item lacking `agent_checked`: Philadelphia, PA (index 5).
- Compiled binding City ordinances from 2008 onward from certified bill PDFs (amlegal), Philadelphia Legistar, City Commerce/L&I guidance, and reputable news (Inquirer, WHYY, Billy Penn).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (2 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| First city framework | Bill 150441-A (signed/passed 2015-06-18, effective/enforced 2015-07-01) defined Limited Lodging (≤90 days/year no permit; 91–180 days/year with permit; 180-day annual cap; primary-resident accessory use) and clarified City Hotel Room Rental Tax applicability, authorizing booking-agent collection/remittance. |
| Current licensing framework | Bill 210081 (signed 2021-06-23; licensing effective 2022-04-01; platform enforcement 2023-01-01) removed annual day-count tiers, required Limited Lodging Operator and Booking Agent licenses, forced listings through licensed platforms, and mandated license verification, quarterly reports, and 5-day delisting. |
| Non-primary units | Non-primary STRs are treated as Visitor Accommodation (hotel rental license) and are by-right only in specified commercial/mixed districts; otherwise a ZBA variance is required—tightened in practice by the 2021 licensing rewrite. |
| Airbnb tax | Municipal Hotel Room Rental Tax (8.5%) platform collection associated with **2015-07-15** (Inquirer; Airbnb spokeswoman; later remittance reporting). Distinct from PA state hotel-occupancy collection starting 2016-07-01. |
| Airbnb data sharing | **2023-01-01** — City-extended deadline for platforms to collect/verify license numbers under Bill 210081 (original mid-2022 target deferred). L&I began formal unlicensed delisting notices to booking agents on 2023-07-12. |

## Legislative history recorded

1. **Bill No. 150441-A** — City of Philadelphia  
   - Passage 2015-06-18; effective/enforced 2015-07-01  
   - `primary_framework`: true

2. **Bill No. 210081** — City of Philadelphia  
   - Passage 2021-06-23; effective 2022-04-01; enforcement 2023-01-01  
   - `primary_framework`: true

No additional binding City/County/State STR regulatory ordinances specific to Philadelphia were identified between 2008 and research date beyond these two (administrative L&I regulations and the 2016 state tax collection agreement were excluded as non-legislative / state-tax-only).

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Philadelphia entry)
- Report: `agent/reports/2026-08-08-philadelphia-str-legislative-history.md`
