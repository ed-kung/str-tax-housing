# Arlington, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Arlington, TX (first unchecked city). Arlington’s binding STR framework is companion Ordinances 19-014 (UDC zoning / STR Zone) and 19-022 (Short-term Rental Chapter permitting and operations), both passed 2019-04-23 and effective/enforced 2019-08-01; a temporary injunction was denied and affirmed on appeal in *Draper*. State H.B. 1905 confirmed STRs are “hotels” for HOT. Airbnb collects Texas state HOT only; no municipal Airbnb tax or direct data-sharing arrangement was found.

## What was done

- Identified first list item lacking `agent_checked`: Arlington, TX (index 49).
- Compiled binding City/State actions from 2008 onward from City STR pages and Ordinance 19-022 PDF, *Draper v. City of Arlington* (Tex. App.—Fort Worth 2021), City Treasury HOT materials, Airbnb’s Texas occupancy-tax help page, and contemporaneous reporting (Shorthorn, KRLD, Dallas Morning News, Fort Worth Report/KERA).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2019 | 2013 registration proposal tabled; no binding STR land-use/licensing framework. STRs subject to City HOT as hotels after H.B. 1905. |
| Zoning framework | Ord. 19-014 (passed 2019-04-23; effective 2019-08-01) defined STRs (&lt;30 days), created Entertainment District STR Zone, and limited STRs to that zone / RM-12 / RMF-22 / nonresidential & mixed-use (existing structures). |
| Operational framework | Ord. 19-022 (passed 2019-04-23; effective 2019-08-01) created annual permit (~$500 by fee resolution), inspection, $1M insurance, local contact (1-hour response), occupancy/parking/noise/event rules, HOT duties, and platform notice obligation. |
| Litigation | *Draper* temporary injunction denied; Second Court of Appeals affirmed 2021-07-15; ordinances remained enforceable. |
| State HOT | H.B. 1905 (effective 2015-09-01) confirmed STRs are hotels for HOT. |
| Airbnb tax | Municipal platform collection: **null** (state-only since 2017-05-01; hosts remit City 9% HOT). |
| Airbnb data sharing | **null** — platform notice-only duty; City uses Host Compliance/Granicus monitoring, not an Airbnb data feed. |

## Legislative history recorded

1. **H.B. 1905** — State of Texas — 2015-06-20 / 2015-09-01 — `primary_framework`: false  
2. **Ordinance No. 19-014** — City of Arlington — 2019-04-23 / 2019-08-01 — `primary_framework`: true  
3. **Ordinance No. 19-022** — City of Arlington — 2019-04-23 / 2019-08-01 — `primary_framework`: true  

Non-binding items excluded: 2013 tabled registration ordinance; Council fee resolutions setting the permit amount (authorized by Ord. 19-022 § 3.09); and informal reports / World Cup enforcement briefings.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Arlington entry)
- Report: `agent/reports/2026-08-08-arlington-str-legislative-history.md`
