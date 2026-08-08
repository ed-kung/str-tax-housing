# Glendale, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Glendale, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) still frames local power; Glendale’s city regime began with Ord. O22-34 (May 10, 2022 contact/prohibited-use rules; GovOS registration enforced Jan. 1, 2023) and companion nuisance Ord. O22-35, then expanded under SB 1168 via Ord. O23-08 (Mar. 14, 2023 licensing rewrite) and Ord. O24-27 (Aug. 13, 2024 neighbor notice/occupancy). Ord. O24-51 (Dec. 10, 2024) added ADU rental owner-occupancy under HB 2720. Airbnb has collected Glendale municipal lodging taxes via the ADOR OLM partnership since **2017-01-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Glendale, AZ (index 89).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; SB 1382 / Ch. 189; HB 2672 / Ch. 240; SB 1168 / Ch. 343; HB 2720 / Ch. 196), Glendale City Code Chapter 29.1 Article IV (Municode; Ords. O22-34, O23-08, O24-27), Ord. O22-35 (nuisance parties), Ord. O24-51 (ADU / ZTA24-03), city STR / GovOS pages, Airbnb Arizona occupancy-tax guidance, and local coverage (KJZZ, Arizona Republic / AZ Central, AZ Big Media).
- Confirmed Glendale had no dedicated pre-2016 STR ban/license ordinance; first city framework is O22-34, with operational registration via GovOS from January 2023.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (10 entries), Airbnb tax/data fields, and `agent_checked: 1`.
- Wrote reproducible updater: `agent/scripts/update_glendale_str_regulations.py`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy, with narrow health/safety and generally applicable nuisance exceptions. |
| Local authority restored in steps | HB 2672 (2019) allowed emergency-contact rules and banned nonresidential “party house” uses; SB 1168 (2022) authorized limited local permits, insurance, neighbor notice, and suspensions. |
| Glendale city framework | O22-34 (passed 2022-05-10; effective ~2022-06-09; registration enforced 2023-01-01 via GovOS) created the first dedicated STR contact/prohibited-use rules; O23-08 (passed 2023-03-14) rewrote Article IV into an SB 1168 licensing chapter ($100 fee / insurance / suspensions in code); O24-27 (passed 2024-08-13) added neighbor notification and IFC occupancy limits. |
| Nuisance companion | O22-35 (passed 2022-05-10) added progressive police service fees and civil penalties for nuisance parties/unlawful gatherings at all private residences, including STRs. |
| ADU / unit-type rules | HB 2720 + O24-51 (passed 2024-12-10; effective 2025-01-09) allow by-right ADUs and require owner occupancy of the main dwelling or ADU when the other unit is rented (including as an STR), with pre-9/14/2024 grandfathering. |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb OLM collection of state, county, and Glendale municipal hotel TPT + bed tax (region GE; city materials cite combined ~15.7%). No earlier Glendale-only agreement found. |
| Airbnb data sharing | **null** — city uses GovOS for registration/public-listing compliance support; no City Portal/API agreement found. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **SB 1382 (Laws 2018, Ch. 189)** — State of Arizona — Passage 2018-04-11; effective/enforced 2019-01-01 — `primary_framework`: false  
3. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
4. **Ord. O22-34 (Chapter 29.1 STR contact / prohibited uses)** — City of Glendale — Passage 2022-05-10; effective 2022-06-09; enforced 2023-01-01 — `primary_framework`: true  
5. **Ord. O22-35 (Nuisance Parties and Unlawful Gatherings)** — City of Glendale — Passage 2022-05-10; effective/enforced 2022-06-09 — `primary_framework`: false  
6. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
7. **Ord. O23-08 (Article IV licensing rewrite)** — City of Glendale — Passage 2023-03-14; effective/enforced 2023-04-13 — `primary_framework`: true  
8. **HB 2720 (Laws 2024, Ch. 196)** — State of Arizona — Passage 2024-05-21; effective/enforced 2024-09-14 — `primary_framework`: false  
9. **Ord. O24-27 (neighbor notice / occupancy / definitions)** — City of Glendale — Passage 2024-08-13; effective/enforced 2024-09-12 — `primary_framework`: false  
10. **Ord. O24-51 (ADU ZTA24-03; rental owner-occupancy)** — City of Glendale — Passage 2024-12-10; effective/enforced 2025-01-09 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Glendale entry)
- Script: `agent/scripts/update_glendale_str_regulations.py`
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_glendale.bak`
- Report: `agent/reports/2026-08-08-glendale-str-legislative-history.md`
