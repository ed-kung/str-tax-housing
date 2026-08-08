# Phoenix, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Phoenix, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) still frames local power; Phoenix’s own regime began with registration in 2020 (G-6653) and shifted to a permit system in 2023 (G-7156). Airbnb began collecting Phoenix municipal lodging/sales tax on 2015-07-01; no documented direct Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Phoenix, AZ (index 4).
- Compiled binding city and state STR-related legislation from 2008 onward from Arizona session laws, Phoenix City Code/Legistar materials, and reputable news (AZ Central, Phoenix New Times, city STR registry pages).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (11 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy, with narrow health/safety and generally applicable nuisance exceptions. |
| Local authority restored in steps | HB 2672 (2019) allowed emergency-contact rules and banned nonresidential “party house” uses; SB 1168 (2022) authorized limited local permits, insurance, neighbor notice, and suspensions. |
| Phoenix city framework | G-6653 (2020) created registration + contact/response duties; G-7156 (passed 2023-09-20, effective 2023-11-06, enforcement 2024-01-15) replaced it with the current $250 annual permit regime. |
| ADUs | 2023 casita zoning banned ADU-as-STR; HB 2720 (2024) and later city code/zoning amendments replaced that ban with owner-occupancy conditions for newer ADUs (G-7323, G-7495; attestation rule effective 2026-04-04). |
| Airbnb tax | Municipal collection agreement reported for **2015-07-01** (Phoenix sales + transient lodging tax). |
| Airbnb data sharing | **null** — city uses/planned third-party listing mining; no City Portal/API agreement found. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Phoenix entry)
- Report: `agent/reports/2026-08-08-phoenix-str-legislative-history.md`
