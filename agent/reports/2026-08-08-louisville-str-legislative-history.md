# Louisville, KY short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Louisville, KY (first unchecked city). Metro’s binding STR framework began with Ordinance 217-2015 (registration/tax) and Ordinance 100-2016 (zoning/CUPs), both effective 2016-08-01; major amendments followed in 2019 (600-foot rule, platform advertising duties) and 2023 (owner-occupancy tightening, $250 fee). Airbnb began collecting Louisville’s 8.5% Transient Room Tax on 2018-04-01; no direct Airbnb–city compliance data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Louisville, KY (index 27).
- Compiled binding Metro STR ordinances from Louisville Legistar, AmLegal LMCO Chapter 115 history notes, LouisvilleKY.gov Planning STR pages/PDFs, Airbnb/Louisville tax announcements, and reputable local reporting (LPM, WLKY, Courier-Journal).
- Excluded non-binding resolutions (e.g., R-178-18, R-126-22/Res. 143-2022 study directs), failed/withdrawn moratoria (O-476-18, O-072-23), and failed 2025 state preemption (KY SB 61).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Initial registration framework | Ord. 217-2015 (passed 2015-12-17; effective 2016-08-01 after Ord. 70-2016 delay) created LMCO short-term rental registration, safety/occupancy rules, and local tax duties. |
| Initial zoning framework | Ord. 100-2016 (passed 2016-06-23; effective 2016-08-01) added LDC CUP rules for non-primary-residence and many multifamily STRs. |
| Condo tweak | Ord. 201-2016 (passed 2016-11-17) allowed primary-residence condo STRs by CUP with association approval. |
| 2019 density / platform update | Ord. 056-2019 (passed 2019-04-25; approved/effective 2019-05-08) added the 600-foot rule, raised fees to $100, required registration numbers in ads, and authorized platform removal/aggregate-data requests. |
| 2023 tightening | Ord. 130-2023 (council 2023-09-14; effective 2023-09-28) raised fees to $250, required 6 months’ prior residency for owner-occupied registration, shifted host→owner standards, and hardened CUP/density rules. |
| Airbnb tax | Municipal Transient Room Tax collection date **2018-04-01** (Airbnb/Louisville agreement). Statewide KY sales tax (2017) excluded per guidelines. |
| Airbnb data sharing | **null** — no City Portal/API or implemented compliance data feed found; 2019 ordinance tools are discretionary request/subpoena authority only. |
| State preemption attempt | KY SB 61 (2025) House amendment targeting local STR density spacing (incl. Louisville’s 600-foot rule) did not become law. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Louisville entry)
- Report: `agent/reports/2026-08-08-louisville-str-legislative-history.md`
