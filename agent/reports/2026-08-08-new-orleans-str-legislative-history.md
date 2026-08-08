# New Orleans, LA — Short-term rental legislative history

**Summary:** New Orleans legalized and regulated STRs in **December 2016** (Ord. 27,209 / 27,204 MCS; effective **2017-04-01**), with Airbnb collecting City occupancy taxes from **2017-01-01** and operational pass-through registration / monthly data sharing from **2017-04-01**. Major rewrites followed in **2019** (homestead/primary-residence residential rules; residency requirement struck by the Fifth Circuit in 2022) and **2023** (one-per-square density cap and lottery). **Ord. 30,074 MCS** (2024) requires platform electronic verification; City enforcement began **2025-08-01**.

## City processed

- **City:** New Orleans, Louisiana  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 52)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **2016 primary framework (Ord. 27,209 & 27,204 MCS).** Council adopted Dec. 1, 2016; permits/enforcement effective Apr. 1, 2017. Accessory / Temporary (90-day) / Commercial types; French Quarter ban (limited VCE exception); platform reporting; companion $1/night housing fee (27,210) and Airbnb CEA authorization (27,218).

2. **2018 Interim Zoning District (Motion M-18-195).** Binding May 24, 2018 pause on Temporary renewals and certain first-floor Commercial STRs during restudy.

3. **2019 overhaul (Ord. 28,156 & 28,157 MCS).** Effective Dec. 1, 2019: Residential vs Commercial permits; homestead/primary-residence requirement for residential STRs; owner/operator/platform permits and nightly fees. *Hignell-Stark* (5th Cir. Aug. 22, 2022) invalidated the residency/homestead rule.

4. **2023 density/lottery rewrite (Ord. 29,381 & 29,382 MCS; Ord. 29,398 MCS).** Effective July 1, 2023 (RSTR/ISTR sunset Aug. 31, 2023). One NSTR per square + lottery; federal PI ~Sept. 1, 2023–Feb. 28, 2024; framework later upheld.

5. **2024 platform verification (Ord. 30,074 MCS).** Passed Oct. 10, 2024; City announces first verification day Aug. 1, 2025. Courts rejected Airbnb challenge.

6. **Airbnb tax collection:** **2017-01-01** (Airbnb help + City/Advocate reporting on municipal occupancy taxes).

7. **Airbnb data sharing:** **2017-04-01** (pass-through registration and monthly platform reports under Ord. 27,204 / CEA, operational with permitting).

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Ord. 27,209 & 27,204 MCS | City of New Orleans | 2016-12-01 | 2017-04-01 | 2017-04-01 | true |
| Motion M-18-195 (STR IZD) | City of New Orleans | 2018-05-24 | 2018-05-24 | 2018-05-24 | false |
| Ord. 28,156 & 28,157 MCS | City of New Orleans | 2019-08-08 | 2019-12-01 | 2019-12-01 | true |
| Ord. 29,381 & 29,382 MCS | City of New Orleans | 2023-03-23 | 2023-07-01 | 2023-07-01 | true |
| Ord. 29,398 MCS | City of New Orleans | 2023-04-06 | 2023-04-06 | 2023-08-31 | false |
| Ord. 30,074 MCS | City of New Orleans | 2024-10-10 | 2025-08-01 | 2025-08-01 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (New Orleans entry)
- Script: `agent/scripts/update_new_orleans_str_regulations.py`
- Report: `agent/reports/2026-08-08-new-orleans-str-legislative-history.md`

## Key sources

- City of New Orleans: 2018 STR Study; STR Handbook (2019); nola.gov STR Administration announcements (2023 changes; Aug. 1, 2025 platform verification)
- Municode / City PDFs: Ord. 27,204; 28,156/28,157; 29,381/29,382; 30,074; CZO Ord. 27,209 notes
- City Council: 2019-08-08 regular meeting release; 2018 Motion M-18-195 IZD materials
- Airbnb help article 867 (New Orleans): tax collection as of 2017-01-01
- NYT (2016-12-07), The Advocate, The Lens: Airbnb CEA, pass-through registration, Jan. 1 tax / Apr. 1 rules
- *Hignell-Stark v. City of New Orleans*, 46 F.4th 317 (5th Cir. 2022); later EDLA/5th Cir. rulings on 2023–2024 ordinances
- WWNO / nola.com coverage of 2023 density rules and 2024 platform verification
