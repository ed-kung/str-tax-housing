# Gilbert, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Gilbert, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) still frames local power; Gilbert’s December 2016 LDC registration language was never operationally enforced. The town’s binding licensing regime is Ordinance No. 2874 (Chapter 14, Article III; passed June 20, 2023; effective July 20, 2023; program/enforcement rollout September 5, 2023) with a $100/$100 fee resolution. Ordinance No. 2918 (Oct. 22, 2024) raised STR lodging TPT/bed taxes effective January 1, 2025 and remains in force despite ongoing litigation. Airbnb has collected Gilbert municipal lodging taxes via the ADOR OLM partnership since **2017-01-01**; no Airbnb–town data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Gilbert, AZ (index 78).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; SB 1382 / Ch. 189; HB 2672 / Ch. 240; SB 1168 / Ch. 343; HB 2720 / Ch. 196), Gilbert Town Code Chapter 14 Article III (Municode; Ord. 2874), June 20 / August 15 2023 Town Council packets, ADOR Gilbert Model City Tax Code profile (Ord. 2918), town STR / tax pages, Airbnb Arizona lodging-tax guidance, GovOS case materials, and local coverage (Gilbert Sun News, Daily Independent, East Valley Tribune, ABC15).
- Confirmed Gilbert had no actively enforced dedicated STR license program before Ord. 2874; earlier LDC registration text (Dec. 2016) lacked process/database/enforcement per town staff.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (9 entries), Airbnb tax/data fields, and `agent_checked: 1`.
- Wrote reproducible updater: `agent/scripts/update_gilbert_str_regulations.py`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy, with narrow health/safety and generally applicable nuisance exceptions. |
| Local authority restored in steps | HB 2672 (2019) allowed emergency-contact rules and banned nonresidential “party house” uses; SB 1168 (2022) authorized limited local permits, insurance, neighbor notice, and suspensions. |
| Gilbert town framework | Ord. 2874 (passed 2023-06-20; effective 2023-07-20; enforced with GovOS rollout 2023-09-05) created Chapter 14 licensing; Aug. 15, 2023 fee resolution set $100/$100 fees effective 2023-09-05. Staff deferred optional ad-license-number, $500k insurance, and background-check requirements. |
| Zoning cleanup | Aug. 15, 2023 Z23-07 LDC amendment removed redundant Dec. 2016-era LDC STR registration text and cross-referenced Chapter 14. |
| Lodging tax hike | Ord. 2918 (passed 2024-10-22; effective/enforced 2025-01-01) raised hotel TPT 1.5%→2.0% and bed tax 2.8%→5.0%. *Barth v. Town of Gilbert* challenges constitutionality; no injunction found; rates still published by ADOR/town. |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb OLM collection of state, county, and Gilbert municipal hotel TPT + additional bed tax (region GB). |
| Airbnb data sharing | **null** — town uses GovOS for licensing/public-listing compliance support; no City Portal/API agreement found. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **SB 1382 (Laws 2018, Ch. 189)** — State of Arizona — Passage 2018-04-11; effective/enforced 2019-01-01 — `primary_framework`: false  
3. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
4. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
5. **Ord. 2874 (Chapter 14 licensing)** — Town of Gilbert — Passage 2023-06-20; effective 2023-07-20; enforced 2023-09-05 — `primary_framework`: true  
6. **STR license fee resolution ($100/$100)** — Town of Gilbert — Passage 2023-08-15; effective/enforced 2023-09-05 — `primary_framework`: false  
7. **Z23-07 LDC STR cross-reference amendment** — Town of Gilbert — Passage 2023-08-15; effective/enforced 2023-09-14 — `primary_framework`: false  
8. **HB 2720 (Laws 2024, Ch. 196)** — State of Arizona — Passage 2024-05-21; effective/enforced 2024-09-14 — `primary_framework`: false  
9. **Ord. 2918 (TPT / bed tax increase)** — Town of Gilbert — Passage 2024-10-22; effective/enforced 2025-01-01 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Gilbert entry)
- Script: `agent/scripts/update_gilbert_str_regulations.py`
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_gilbert.bak`
- Report: `agent/reports/2026-08-08-gilbert-str-legislative-history.md`
