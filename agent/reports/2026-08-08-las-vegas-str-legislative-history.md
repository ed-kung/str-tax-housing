# Las Vegas, NV short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Las Vegas, NV (first unchecked city). The City has regulated STRs since Ord. No. 6357 (2014), then tightened to owner-only (2017) and owner-occupied primary-residence hosted stays (2018). State AB 321 (2017) enabled platform reporting (implemented by Ord. 6600); AB 363 (eff. 2022-07-01) mandated accommodations-facilitator tax remittance and minimum standards, implemented locally by Ord. No. 6815 (~2022-08-24). Airbnb municipal room-tax collection is dated **2022-08-24**; platform data reporting begins **2017-11-01**.

## What was done

- Identified first list item lacking `agent_checked`: Las Vegas, NV (index 23).
- Compiled binding City ordinances and Nevada statutes relevant to City of Las Vegas STRs from Municode Chapter 6.75 history notes, City ordinance PDFs, NRS/AB texts, Legislative Counsel Bureau research brief, Review-Journal / AP / KNPR coverage, Avalara lodging-tax notes, and Airbnb help article 2315 (including Wayback archives).
- Excluded unincorporated Clark County’s ban and 2022 county licensing ordinance (different jurisdiction), non-binding resolutions, and Ord. No. 6929 (11-19-25) for lack of a clear substantive STR policy change in public materials.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (7 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary city framework | Ord. No. 6357 (2014-10-01) created LVMC Ch. 6.75 licensing for stays &lt;31 days ($500 fee, local contact, occupancy/party/noise rules). |
| 2017 tightening | Ord. No. 6585 (eff. 2017-07-01): new licenses limited to owners; 3-bedroom / 660-ft conditional-use path; SUP path for non-hosted/larger homes. |
| Platform data | AB 321 (eff. 2017-07-01) authorized quarterly hosting-platform reports; Ord. No. 6600 (2017-11-01) imposed them on Airbnb et al. in the City. |
| 2018 hosted-only | Ord. No. 6663 (2018-12-05): new STRs must be owner-occupied primary residences with host present; whole-home new permits effectively ended (prior licenses grandfathered). |
| State AB 363 | Signed 2021-06-04; substantive eff. 2022-07-01. Requires Clark County cities to regulate STRs/facilitators, collect room tax via platforms, meet separation/apartment/party minima; bans total local bans. |
| 2022 city update | Ord. No. 6815 (passed 2022-08-17; eff. ~2022-08-24): facilitator licenses, mandatory City room-tax remittance, listing reports, apartment ban, min stays, higher fines—AB 363 conformity atop existing hosted model. |
| Airbnb tax | **2022-08-24** — first municipal remittance duty under Ord. 6815 / AB 363; Airbnb help confirms City TOT collection (Las Vegas absent from Oct 2021 archive; present by Feb 2023). |
| Airbnb data sharing | **2017-11-01** — Ord. 6600 quarterly platform reports / subpoenas (later reinforced by Ord. 6815). |

## Legislative history recorded

1. **Ord. No. 6357** — City of Las Vegas — 2014-10-01 — `primary_framework`: true  
2. **AB 321 (Ch. 347)** — State of Nevada — Passage 2017-06-04; effective/enforced 2017-07-01 — `primary_framework`: false  
3. **Ord. No. 6585** — City of Las Vegas — Passage 2017-06-21; effective/enforced 2017-07-01 — `primary_framework`: false  
4. **Ord. No. 6600** — City of Las Vegas — 2017-11-01 — `primary_framework`: false  
5. **Ord. No. 6663** — City of Las Vegas — 2018-12-05 — `primary_framework`: false  
6. **AB 363 (Ch. 388)** — State of Nevada — Passage 2021-06-04; effective/enforced 2022-07-01 — `primary_framework`: true  
7. **Ord. No. 6815** — City of Las Vegas — Passage 2022-08-17; effective/enforced 2022-08-24 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Las Vegas entry)
- Report: `agent/reports/2026-08-08-las-vegas-str-legislative-history.md`
