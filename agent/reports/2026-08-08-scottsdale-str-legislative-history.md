# Scottsdale, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Scottsdale, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) ended Scottsdale’s prior SFR short-stay ban and set the statewide OLM tax path; Scottsdale’s first dedicated local STR chapter was Ordinance No. 4416 (Sept. 24, 2019; effective Oct. 24, 2019), paired with citywide nuisance-party Ordinance No. 4417. After SB 1168, Ordinance No. 4566 (Oct. 25, 2022; license requirement Jan. 8, 2023) established the current $250 licensing framework. Later amendments tightened emergency response, nuisance enforcement, juvenile rentals, ADU-STR owner-residency, and “event center” definitions. Airbnb has collected Scottsdale municipal lodging taxes via the ADOR OLM partnership since **2017-01-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Scottsdale, AZ (index 92).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; SB 1382 / Ch. 189; HB 2672 / Ch. 240; SB 1168 / Ch. 343; HB 2720 / Ch. 196; HB 2928 / Ch. 217), Scottsdale council reports for Ords. 4416/4417 (Sept. 24, 2019), 4527/4528 (Dec. 8, 2021), 4566 (Oct. 25, 2022), 4626/4627 (May 6, 2024), 4652 (Nov. 25, 2024), 4687 (Sept. 30, 2025), and 4719 (June 23, 2026), plus city STR/ADU pages, ADOR OLM guidance, Airbnb Scottsdale host materials, and local coverage (Scottsdale Progress / scottsdale.org, KJZZ, KTAR, Signals AZ).
- Confirmed Scottsdale’s pre-2017 SFR short-stay prohibition was preempted (not re-enacted as a local ban) and that licensing under Ord. 4566 is the operative local primary framework.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (16 entries), Airbnb tax/data fields, and `agent_checked: 1`.
- Wrote reproducible updater: `agent/scripts/update_scottsdale_str_regulations.py`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy; city materials state it removed Scottsdale’s prior ≤30-day rental prohibition in SFR districts. |
| Early local tools | Ord. 4416 (2019-09-24 / effective 2019-10-24) created Chapter 18 Article IX contact-info + nonresidential-use rules under HB 2672; Ord. 4417 created citywide nuisance-party fees/fines (enforcement from 2019-10-24). |
| 2021 strengthening | Ords. 4527/4528 (passed 2021-12-08; effective 2022-01-07) added one-hour in-person emergency response and converted nuisance enforcement to higher civil fines/citations. |
| Licensing framework | SB 1168 (2022) enabled Ord. 4566 (passed 2022-10-25; license required 2023-01-08): $250 annual license, insurance, neighbor notice, background checks, health/safety rules, suspension authority. |
| Later amendments | Ords. 4626/4627 (2024-05-06 / effective 2024-06-06) added promoter liability, police dispersal, and juvenile-rental ban; Ord. 4652 / HB 2720 and Ord. 4687 / HB 2928 added ADU-STR owner-residency; Ord. 4719 (2026-06-23 / effective 2026-07-23) defined “event center.” |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb OLM collection of state, county, and Scottsdale municipal hotel TPT + additional bed tax (region SC). |
| Airbnb data sharing | **null** — city uses Accela + Rentalscape/public-listing tools; informal complaint cooperation with platforms is not a direct data connection. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **SB 1382 (Laws 2018, Ch. 189)** — State of Arizona — Passage 2018-04-11; effective/enforced 2019-01-01 — `primary_framework`: false  
3. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
4. **Ord. 4416 (Chapter 18 Article IX)** — City of Scottsdale — Passage 2019-09-24; effective/enforced 2019-10-24 — `primary_framework`: true  
5. **Ord. 4417 (nuisance parties)** — City of Scottsdale — Passage 2019-09-24; effective/enforced 2019-10-24 — `primary_framework`: false  
6. **Ord. 4527 (one-hour emergency response)** — City of Scottsdale — Passage 2021-12-08; effective/enforced 2022-01-07 — `primary_framework`: false  
7. **Ord. 4528 (nuisance civil fines)** — City of Scottsdale — Passage 2021-12-08; effective/enforced 2022-01-07 — `primary_framework`: false  
8. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
9. **Ord. 4566 (licensing)** — City of Scottsdale — Passage 2022-10-25; effective/enforced 2023-01-08 — `primary_framework`: true  
10. **Ord. 4626 (promoters / police dispersal)** — City of Scottsdale — Passage 2024-05-06; effective/enforced 2024-06-06 — `primary_framework`: false  
11. **Ord. 4627 (juvenile rental ban)** — City of Scottsdale — Passage 2024-05-06; effective/enforced 2024-06-06 — `primary_framework`: false  
12. **HB 2720 (Laws 2024, Ch. 196)** — State of Arizona — Passage 2024-05-21; effective/enforced 2024-09-14 — `primary_framework`: false  
13. **Ord. 4652 (ADU / ADU-STR owner-residency)** — City of Scottsdale — Passage 2024-11-25; effective/enforced 2024-12-25 — `primary_framework`: false  
14. **HB 2928 (Laws 2025, Ch. 217)** — State of Arizona — Passage 2025-05-23; effective/enforced 2025-09-26 — `primary_framework`: false  
15. **Ord. 4687 (ADU update under HB 2928)** — City of Scottsdale — Passage 2025-09-30; effective/enforced 2025-10-30 — `primary_framework`: false  
16. **Ord. 4719 (event-center definition)** — City of Scottsdale — Passage 2026-06-23; effective/enforced 2026-07-23 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Scottsdale entry)
- Script: `agent/scripts/update_scottsdale_str_regulations.py`
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_scottsdale.bak`
- Report: `agent/reports/2026-08-08-scottsdale-str-legislative-history.md`
