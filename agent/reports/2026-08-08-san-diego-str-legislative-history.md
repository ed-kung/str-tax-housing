# San Diego, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for San Diego, CA (first unchecked city). An August 2018 STRO package (O-20977/O-20978) was repealed by referendum-driven O-21008 before enforcement. The current primary framework is Ordinance O-21305 (2021; coastal LCP mods via O-21464 in 2022), with citywide license and platform enforcement beginning May 1, 2023. Airbnb began collecting San Diego municipal TOT on 2015-07-15; the first binding Airbnb–city listing/compliance data connection is 2023-05-01.

## What was done

- Identified first list item lacking `agent_checked`: San Diego, CA (index 7).
- Compiled binding City ordinances from 2008 onward from official Municipal Code / ordinance PDFs (docs.sandiego.gov), City Treasurer STRO materials, California Coastal Commission LCP materials, and reputable news (NBC 7, Times of San Diego, Union-Tribune, KPBS).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Failed 2018 framework | O-20977/O-20978 (final passage 2018-08-02; slated ~2019-07-01) would have limited STRs to primary residence (+ one same-parcel unit), licensing, AHIF, Good Neighbor rules, and platform duties; referendum led to repeal before enforcement (`enforcement_date`: null). |
| Repeal | O-21008 (2018-11-20) granted the referendary petition and repealed O-20977/O-20978. |
| Current framework | O-21305 (final passage 2021-04-14; effective 2021-05-29 outside coastal zone) created four-tier STRO licensing with whole-home caps (1% citywide excl. Mission Beach; 30% Mission Beach), host limits, nuisance/Good Neighbor rules, and platform license verification + monthly data reporting. |
| Coastal pathway | Coastal Commission approved LCP amendment with sunset mods (March 2022); City adopted O-21464 (passage 2022-06-27; effective 2022-08-10) adding §510.0112 coastal sunset to 2030. |
| Active enforcement | Unlicensed STRO unlawful and platform reporting/verification duties active **2023-05-01** (City Treasurer STRO pages; KPBS). |
| Airbnb tax | Municipal TOT/TMD platform collection: **2015-07-15** (NBC 7 + City statement). |
| Airbnb data sharing | **2023-05-01** — first binding City↔platform listing license verification and monthly reporting under O-21305 / Treasurer guidelines. |

## Legislative history recorded

1. **Ordinances O-20977 and O-20978** — City of San Diego  
   - Passage 2018-08-02; effective (slated) 2019-07-01; enforcement null  
   - `primary_framework`: true

2. **Ordinance O-21008** — City of San Diego  
   - Passage/effective/enforced 2018-11-20  
   - `primary_framework`: false

3. **Ordinance O-21305** — City of San Diego  
   - Passage 2021-04-14; effective 2021-05-29; enforcement 2023-05-01  
   - `primary_framework`: true

4. **Ordinance O-21464** — City of San Diego  
   - Passage 2022-06-27; effective/enforced 2022-08-10  
   - `primary_framework`: false

No additional binding City/County/State STR regulatory ordinances specific to the City of San Diego were identified between 2008 and research date beyond these (City Attorney memos, MOUs, fee-schedule resolutions, and general TOT Measure C rate changes were excluded as non-binding recommendations or not STR-specific regulatory frameworks).

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (San Diego entry)
- Report: `agent/reports/2026-08-08-san-diego-str-legislative-history.md`
