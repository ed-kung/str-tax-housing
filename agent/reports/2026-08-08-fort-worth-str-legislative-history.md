# Fort Worth, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Fort Worth, TX (first unchecked city). Fort Worth’s binding STR framework is zoning Ordinance No. 23110-02-2018 (residential ban / commercial allowance) plus registration Ordinance No. 26005-02-2023 (annual registration, occupancy/nuisance rules, HOT duties). State H.B. 1905 confirmed STRs are “hotels” for HOT. Airbnb collects Texas state HOT only; no municipal Airbnb tax or direct data-sharing arrangement was found.

## What was done

- Identified first list item lacking `agent_checked`: Fort Worth, TX (index 11).
- Compiled binding City/State actions from 2008 onward from City ordinance PDFs, AmLegal code citations, City informal reports / STR web pages, Tarrant County litigation coverage (Fort Worth Report, CBS Texas, Dallas Observer), and Airbnb’s Texas occupancy-tax help page.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2018 | STRs not defined in Zoning Ordinance; treated as hotel/motel-analogous commercial uses (City IR 12-07-2021). |
| Zoning framework | Ord. 23110-02-2018 (passed 2018-02-06) defined Short Term Home Rental (<30 days) and barred STRs by right in residential districts while allowing them in mixed-use / most form-based / commercial / industrial with CO. |
| Registration framework | Ord. 26005-02-2023 (passed 2023-02-14; effective 2023-02-28) created Chapter 7 Art. XIII annual registration ($150/$100), local contact, occupancy/parking/event limits, ad registration numbers, and HOT remittance duties. Kept residential ban. |
| Litigation | Kelray LLC et al. suit (June 2023) sought to block STR ordinances; no injunction. District court summary judgment for City on 2025-03-06. |
| State HOT | H.B. 1905 (effective 2015-09-01) confirmed STRs are hotels for HOT. |
| Airbnb tax | Municipal platform collection: **null** (state-only since 2017-05-01; hosts remit City 9% HOT). |
| Airbnb data sharing | **null** — no binding City↔Airbnb listing API / delist channel; monitoring via Code Compliance / third-party tools. |

## Legislative history recorded

1. **H.B. 1905** — State of Texas — 2015-06-20 / 2015-09-01 — `primary_framework`: false  
2. **Ordinance No. 23110-02-2018** — City of Fort Worth — 2018-02-06 / 2018-02-06 — `primary_framework`: true  
3. **Ordinance No. 26005-02-2023** — City of Fort Worth — 2023-02-14 / 2023-02-28 — `primary_framework`: true  

Non-binding items excluded: City Council informal reports and briefings (2021–2024), rejected Short-Term and Hotel Online Platform RFP (M&C 23-0102), and resolutions retaining outside counsel for STR litigation.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Fort Worth entry)
- Report: `agent/reports/2026-08-08-fort-worth-str-legislative-history.md`
