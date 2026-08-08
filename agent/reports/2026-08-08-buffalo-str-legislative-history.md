# Buffalo, NY short-term rental legislative history

Researched and updated the Buffalo, NY entry in `AGENT_DATA_PATH/str_regulations.json` (index 80), the first list item lacking `agent_checked`. Added `legislative_history` (7 binding actions from 2010–2025), Airbnb municipal tax-collection and data-sharing fields, and `agent_checked: 1`.

## Summary

Buffalo’s primary municipal STR framework dates to the October 29, 2019 Shared Housing ordinance amending Chapter 264 (registration, inspections, and special-use permits for non-owner-occupied units). That regime was restated in a November 24, 2020 Chapter 264 rewrite and then relocated into dedicated Chapter 380 on February 20, 2024, with higher fees/fines, historic-district review, and tighter zoning/safety rules. County-level Erie Local Law 1-2024 (effective January 4, 2024) extended the 3% hotel occupancy tax to STRs; the city separately imposed a 3% municipal occupancy tax (authorized by 2025 Laws Ch. 59 Part TT / Tax Law §1202-kk; local law July 22, 2025; collections from September 1, 2025). Airbnb help docs show collection of the Buffalo city tax; no city–Airbnb enforcement data-sharing arrangement was found.

## Legislative history (included)

| Date | Action |
| --- | --- |
| 2010-07-16 / eff. 2011-05-01 | NYS Ch. 225/566 — Class A MDL illegal-hotels rule (statewide) |
| 2019-10-29 | Buffalo Ch. 264 Shared Housing STR licensing (**primary_framework**) |
| 2020-11-24 | Res. 20-1431 — Ch. 264 repeal/replace restating STR rules |
| 2023-12-07 / eff. 2024-01-04 | Erie County LL 1-2024 Occupancy Tax Modernization Act |
| 2024-02-20 | Buffalo Ch. 380 dedicated STR Housing code + fee/fine hikes |
| 2025-05-09 | NYS Ch. 59 Part TT — Tax Law §1202-kk Buffalo hotel-tax authority |
| 2025-07-22 / tax 2025-09-01 | Buffalo Hotel/Motel Occupancy Tax local law (3%) |

Temporary Common Council moratoria (Oct 2023; Dec 2024) were treated as non-ordinance resolutions and omitted. Proposed Dec 2024 ownership-cap / 5% historic-district amendments were not clearly finally enacted as binding code changes.

## Airbnb fields

- **Tax collection:** `2025-09-01` — first municipal Buffalo occupancy-tax date shown as collected on Airbnb (help/article/2319 + city tax effective date). Erie County Aug 1, 2024 VCA is county-only and excluded.
- **Data sharing:** `null` — no documented direct Airbnb–City compliance/API connection.

## Artifacts

- Updated JSON: `$AGENT_DATA_PATH/str_regulations.json` (Buffalo entry)
- Update script: `agent/scripts/update_buffalo_str_regulations.py`
