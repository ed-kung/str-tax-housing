# Lexington, KY — Short-term rental legislative history

**Summary:** Lexington’s modern STR regime was built in two stages: a 2018 tax-definition ordinance (O-042-2018), then the July 11, 2023 paired zoning (O-074-2023) and licensing (O-080-2023) ordinances that created hosted/un-hosted zoning rules and a special fees license—actively enforced beginning **January 11, 2024** after a six-month grace period. State **HB 8 / Acts Ch. 212** (eff. 2023-01-01) and local **O-132-2022** required platforms to collect local transient room tax. December 2024 and January 2025 ordinances added density caps, occupancy/booking limits, and agricultural-zone rules. Airbnb began collecting Lexington’s 8.5% municipal transient room tax on **2018-02-01**; no Airbnb listing-level data-sharing connection was found (city uses Granicus and complaint-driven enforcement).

## City processed

- **City:** Lexington, Kentucky (Lexington-Fayette Urban County Government)
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 58)
- **Marked:** `agent_checked: 1`

## Main findings

1. **O-042-2018 (2018-07-03)** first defined STRs in the Code and expressly applied local transient room tax, without zoning or licensing.
2. **Airbnb municipal tax collection began 2018-02-01** under a voluntary collection agreement authorized by R-777-2017 (announced Jan. 18, 2018).
3. **HB 8 (Acts Ch. 212) and O-132-2022** (eff. 2023-01-01) mandated facilitator/platform collection of local TRT on total rent.
4. **O-074-2023 + O-080-2023 (2023-07-11)** are the primary framework: hosted accessory use vs. unhosted conditional use in residential zones; special fees license, registration numbers in ads, host duties, and penalties. Licensing enforcement deferred six months to **2024-01-11**.
5. **O-138/O-139-2024** tightened occupancy, hosted-unit rules, and unhosted density (600 ft / 2% caps). **O-001/O-002-2025** extended rules to agricultural zones and septic Health Dept. approval.
6. **Airbnb data sharing:** null — tax VCA only; enforcement via Revenue licensing, hotline, and Granicus—not Airbnb City Portal.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| O-042-2018 | LFUCG | 2018-07-03 | 2018-07-03 | 2018-07-03 | false |
| Acts Ch. 212 (HB 8) | State of Kentucky | 2022-04-14 | 2023-01-01 | 2023-01-01 | false |
| O-132-2022 | LFUCG | 2022-12-01 | 2023-01-01 | 2023-01-01 | false |
| O-074-2023 (ZOTA) | LFUCG | 2023-07-11 | 2023-07-11 | 2023-07-11 | true |
| O-080-2023 (license) | LFUCG | 2023-07-11 | 2023-07-11 | 2024-01-11 | true |
| O-138-2024 | LFUCG | 2024-12-05 | 2024-12-05 | 2024-12-05 | false |
| O-139-2024 (ZOTA) | LFUCG | 2024-12-05 | 2024-12-12 | 2024-12-12 | false |
| O-001-2025 (ag ZOTA) | LFUCG | 2025-01-23 | 2025-01-23 | 2025-01-23 | false |
| O-002-2025 (septic/license) | LFUCG | 2025-01-23 | 2025-01-23 | 2025-01-23 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Lexington entry)
- Script: `agent/scripts/update_lexington_str_regulations.py`
- Report: `agent/reports/2026-08-08-lexington-str-legislative-history.md`

## Key sources

- LFUCG Legistar: 0623-18 (O-042-2018), 1319-17 (R-777-2017), 1162-22 (O-132-2022), 0623-23 (O-074-2023), 0699-23 (O-080-2023), 1235-24 (O-138-2024), 1210-24 (O-139-2024), 0032-25 (O-001-2025), 1042-24 (O-002-2025)
- LFUCG ordinance text (O-080-2023 §12 six-month enforcement deferral; ZOTA draft/PC text for O-074-2023)
- lexingtonky.gov — Short-Term Rentals page; Nov. 27, 2023 press release (Jan. 11, 2024 registration deadline)
- Lane Report / Airbnb announcement (Jan. 18, 2018) — local TRT collection effective Feb. 1, 2018
- VisitLEX 2018 Short Term Rental Guide
- Kentucky Acts Ch. 212 (HB 8); KY DOR / KTIA HB 8 transient room tax materials
- CivicLex / Lexington Herald-Leader reporting on 2023–2025 implementation, Granicus, and Dec. 2024 density amendments
