# Nashville, TN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Nashville, TN (first unchecked city). Metro’s primary STR framework is the February 2015 permitting ordinance (BL2014-951), enforced from 2015-07-01, later reorganized into Title 6 by BL2020-187 (2020-07-10) and most recently amended by BL2024-478 (2024-11-12). Non-owner-occupied STRs were phased out of single-/two-family districts (BL2017-608) and then RM districts (BL2019-1633, effective 2022-01-01), subject to Tennessee’s 2018 Short-Term Rental Unit Act legacy protections. Airbnb has collected Metro’s hotel occupancy tax since 2021-01-01 under state marketplace rules; no direct Airbnb–city listing/data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Nashville, TN (index 20).
- Compiled binding Metro and state STR-related legislation from 2008 onward from Nashville.gov STR legislative-history page, Metro ordinance texts (BL2014-909/951, BL2016-381/492, BL2017-608, BL2019-1633, BL2020-187, BL2021-913, BL2024-478), Tennessee Pub. Ch. 972 and 787, TN DOR occupancy guidance, Airbnb Nashville help article, and reputable news (Tennessean, AP).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (11 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | BL2014-951 (passed 2015-02-24; approved 2015-02-26) creates §6.28.030 permitting; applications from 2015-03-31; active enforcement 2015-07-01. Zoning companion BL2014-909 same week. |
| Early tightening | BL2016-381 (2016-12-07) and BL2016-492 (2017-02-24) strengthen applications, permit types, ad permit-number posting, and penalties. |
| Residential NOO phase-out | BL2017-608 (effective 2018-02-02) bars new non-owner-occupied STRs in single-/two-family districts; BL2019-1633 (passed 2019-08-20; RM ban effective 2022-01-01) extends the NOO phase-out to RM districts. |
| State legacy / preemption | Pub. Ch. 972 / Short-Term Rental Unit Act (signed/effective 2018-05-17) grandfathered many already-operating STRs against later local prohibitions. |
| Fees | BL2019-1627 raised permit/renewal fees from $50 to $313 (effective 2019-07-01). |
| Modern code home | BL2020-187 (effective 2020-07-10) moves operational rules to Title 6 and creates the STR Appeals Board; BL2024-478 (effective 2024-11-12) is the current governing ordinance per Nashville.gov, tightening owner-occupied residency proof. |
| Airbnb tax | Municipal hotel occupancy tax collection date **2021-01-01** (Pub. Ch. 787 / TN DOR; Metro Collections). 2018 Airbnb TN deal was sales tax only. |
| Airbnb data sharing | **null** — no City Portal/API/bulk feed/delist channel found; city relies on permitting + monitoring. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Nashville entry)
- Report: `agent/reports/2026-08-08-nashville-str-legislative-history.md`
