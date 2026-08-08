# Mesa, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Mesa, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) remains the statewide frame; Mesa’s own regime is Ordinance No. 5734 (Oct. 17, 2022; eff. Feb. 1, 2023), creating City Code Title 5, Chapter 15 licensing after SB 1168 restored limited local permit authority. Airbnb has collected Mesa municipal lodging taxes via the ADOR OLM partnership since **2017-01-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Mesa, AZ (index 35).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; SB 1382 / Ch. 189; HB 2672 / Ch. 240; SB 1168 / Ch. 343; HB 2720 / Ch. 196), Mesa City Council minutes (Oct. 17, 2022 Ord. 5734; Jan. 9, 2023 Res. 11989), the city’s Short-Term Rental License page, ADOR/Airbnb tax materials, and Mesa Tribune / KJZZ / city press coverage.
- Confirmed Mesa had no dedicated pre-2016 STR ban/license ordinance; first city framework is Chapter 5-15.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (7 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy, with narrow health/safety and generally applicable nuisance exceptions. |
| Local authority restored in steps | HB 2672 (2019) allowed emergency-contact rules and banned nonresidential “party house” uses; SB 1168 (2022) authorized limited local permits, insurance, neighbor notice, and suspensions. |
| Mesa city framework | Ordinance No. 5734 (passed 2022-10-17; effective/enforced 2023-02-01) created MCC Title 5, Chapter 15; Resolution No. 11989 (2023-01-09) set the $250 annual license fee. |
| ADU / host presence | HB 2720 (eff. 2024-09-14) authorizes cities to require owner residence when a post-effective-date ADU is used as an STR. |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb OLM collection of state, county, and Mesa municipal TPT + 5% transient lodging tax (no earlier Mesa-only agreement found). |
| Airbnb data sharing | **null** — city staff stated platforms do not share listing data; enforcement relies on public listing research. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **SB 1382 (Laws 2018, Ch. 189)** — State of Arizona — Passage 2018-04-11; effective/enforced 2019-01-01 — `primary_framework`: false  
3. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
4. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
5. **Ord. 5734 (MCC 5-15)** — City of Mesa — Passage 2022-10-17; effective/enforced 2023-02-01 — `primary_framework`: true  
6. **Res. 11989** — City of Mesa — Passage 2023-01-09; effective/enforced 2023-02-01 — `primary_framework`: false  
7. **HB 2720 (Laws 2024, Ch. 196)** — State of Arizona — Passage 2024-05-21; effective/enforced 2024-09-14 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Mesa entry)
- Report: `agent/reports/2026-08-08-mesa-str-legislative-history.md`
