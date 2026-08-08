# Plano, TX — short-term rental legislative history

**Summary:** Documented Plano’s STR regulatory timeline from 2008 onward and updated `str_regulations.json` (index 72). Binding actions are Texas H.B. 1905 (2015 HOT definition), City Ordinance 2023-5-1 (interim ban effective 2023-05-15), and the April 22, 2024 permanent package—Ordinance 2024-4-13 (zoning; ~2024-04-29 upon publication) and Ordinance 2024-4-14 (registration; effective/enforced 2024-08-01). Airbnb began collecting Plano’s 7% municipal HOT on 2019-05-01; no direct Airbnb–City compliance data connection was identified.

## City processed

- **City:** Plano, TX
- **JSON index:** 72
- **`agent_checked`:** 1

## Legislative history (binding actions)

| Date | Instrument | Role |
| --- | --- | --- |
| 2015-06-20 / eff. 2015-09-01 | H.B. 1905 (Tax Code § 156.001) | Statewide STR-as-hotel clarification for HOT |
| 2023-05-08 / eff. 2023-05-15 | Ordinance 2023-5-1 | One-year interim ban on new dwelling-unit STRs |
| 2024-04-22 / eff. ~2024-04-29 | Ordinance 2024-4-13 | Permanent STR zoning (repeals interim ban) |
| 2024-04-22 / eff. 2024-08-01 | Ordinance 2024-4-14 | Annual STR registration / Short-Term Rental Code |

Primary local framework: Ordinances **2024-4-13** (land use) and **2024-4-14** (registration), both `primary_framework: true`.

## Airbnb tax / data sharing

- **`airbnb_tax_collection_date`:** `2019-05-01` — first Texas municipal Airbnb VCA; City HOT instructions and Airbnb/news releases confirm May 1, 2019 start for Plano’s 7% HOT (distinct from 2017 state-only collection).
- **`airbnb_data_sharing_date`:** `null` — HOT remittances are lump-sum without listing detail; registration imposes only a platform notice duty; City uses Neumo + Deckard, not an Airbnb API/portal.

## Sources (selected)

- City of Plano Ordinances 2023-5-1, 2024-4-13, 2024-4-14 (CivicPlus / NovusAgenda)
- City HOT remittance instructions; STR Task Force Memo #2
- Airbnb announcement / Dallas Morning News / Community Impact (April 2019 tax agreement; 2023–2024 ordinance coverage)

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Plano entry)
- Script: `agent/scripts/update_plano_str_regulations.py`
