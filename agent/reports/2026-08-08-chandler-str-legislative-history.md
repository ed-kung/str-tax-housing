# Chandler, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Chandler, AZ (first unchecked city). Arizona’s 2016 preemption (SB 1350) still frames local power; Chandler’s own regime began with Chapter 22 registration in 2020 (Ord. 4939) and shifted to a $250 annual license system in 2023 (Ord. 5048, eff. Aug. 1, 2023). A brief 2024 ADU-as-STR ban (Ord. 5075) was removed by Ord. 5113 under HB 2720. Airbnb has collected Chandler municipal lodging taxes via the ADOR OLM partnership since **2017-01-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Chandler, AZ (index 77).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; SB 1382 / Ch. 189; HB 2672 / Ch. 240; SB 1168 / Ch. 343; HB 2720 / Ch. 196), Chandler City Code Chapter 22 (Municode), City Council packets/memos for Ords. 4939, 5048, 5075, and 5113, the city’s Short-Term Rental / Tax & License pages, ADOR Chandler Model City Tax Code profile, Airbnb Chandler and Arizona occupancy-tax help articles, and local coverage (Chandler News / Daily Independent).
- Confirmed Chandler had no dedicated pre-2016 STR ban/license ordinance; first city framework is Ord. 4939 (Chapter 22 registration).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (9 entries), Airbnb tax/data fields, and `agent_checked: 1`.
- Wrote reproducible updater: `agent/scripts/update_chandler_str_regulations.py`.

## Main findings

| Theme | Finding |
| --- | --- |
| State preemption | SB 1350 (signed 2016-05-12, effective 2017-01-01) bars cities from banning STRs or regulating them by classification/use/occupancy, with narrow health/safety and generally applicable nuisance exceptions. |
| Local authority restored in steps | HB 2672 (2019) allowed emergency-contact rules and banned nonresidential “party house” uses; SB 1168 (2022) authorized limited local permits, insurance, neighbor notice, and suspensions. |
| Chandler city framework | Ord. 4939 (passed 2020-10-12; eff. 2020-11-16) created Chapter 22 registration; Ord. 5048 (passed 2023-04-13; eff./enforced 2023-08-01) converted it to the current $250 annual license regime with neighbor notice, contact-response, ad-display, and suspension tools. |
| ADU / unit-type rules | Ord. 5075 (passed 2024-02-22; eff. 2024-03-22) banned ADU STRs; HB 2720 and Ord. 5113 (passed 2024-12-09; eff. 2025-01-01) removed that ban. Guest-quarters STR limits remain; city did not add an ADU-STR owner-occupancy rule. |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb OLM collection of state, county, and Chandler municipal hotel TPT + 2.9% additional bed tax (city lodging 4.40%; combined ~11.67%). No earlier Chandler-only agreement found. |
| Airbnb data sharing | **null** — city uses third-party public-listing research; no City Portal/API agreement found. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **SB 1382 (Laws 2018, Ch. 189)** — State of Arizona — Passage 2018-04-11; effective/enforced 2019-01-01 — `primary_framework`: false  
3. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
4. **Ord. 4939 (Chapter 22 registration)** — City of Chandler — Passage 2020-10-12; effective/enforced 2020-11-16 — `primary_framework`: true  
5. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
6. **Ord. 5048 (Chapter 22 licensing)** — City of Chandler — Passage 2023-04-13; effective/enforced 2023-08-01 — `primary_framework`: true  
7. **Ord. 5075 (ADU STR ban)** — City of Chandler — Passage 2024-02-22; effective/enforced 2024-03-22 — `primary_framework`: false  
8. **HB 2720 (Laws 2024, Ch. 196)** — State of Arizona — Passage 2024-05-21; effective/enforced 2024-09-14 — `primary_framework`: false  
9. **Ord. 5113 (ADU mandate; remove ADU STR ban)** — City of Chandler — Passage 2024-12-09; effective/enforced 2025-01-01 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Chandler entry)
- Script: `agent/scripts/update_chandler_str_regulations.py`
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_chandler.bak`
- Report: `agent/reports/2026-08-08-chandler-str-legislative-history.md`
