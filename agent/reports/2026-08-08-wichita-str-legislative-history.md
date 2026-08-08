# Wichita, KS short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Wichita, KS (first unchecked city). Binding City STR framework is companion Ordinances 52-265 (Ch. 3.40 licensing) and 52-266 (UZC Short Term Rental use / Administrative Permit path), both passed 2023-09-19 and effective/enforced 2023-09-22; Ord. 52-544 (2024-09-10 / 2024-09-13) added STR-specific nuisance-party penalties. State SB 50 (veto overridden 2021-05-03; effective 2021-07-01) mandates marketplace collection of local Transient Guest Tax. Airbnb began collecting Wichita’s municipal 6% TGT under the statewide KDOR agreement on **2017-02-01**; no direct Airbnb–City data-sharing arrangement was found.

## What was done

- Identified first list item lacking `agent_checked`: Wichita, KS (index 50).
- Compiled binding City/State actions from 2008 onward from City STR pages and signed Ordinances 52-265 / 52-266 / 52-544, MAPC/DAB workshop materials on pre-2023 Hotel/Motel and Bed-and-Breakfast treatment, KDOR TGT rate tables, KS SB 50 legislative history, Airbnb’s Kansas occupancy-tax help article, Kansas City Star reporting on the 2017 VCA, and contemporaneous KMUW / KWCH / Wichita Eagle coverage.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2023 | No dedicated STR definition/license. Unsupervised stays &lt;7 days treated as Hotel/Motel (commercial districts only); onsite B&B = Conditional Use in most residential districts; ≥7-day rentals treated as ordinary dwellings. |
| Licensing framework | Ord. 52-265 (passed 2023-09-19; effective 2023-09-22) created annual $225/unit license, insurance, Good Neighbor rules, occupancy/gathering limits, and 24/7 local contact. |
| Zoning framework | Ord. 52-266 (same dates) defined Short Term Rental in the City, allowed owner-occupied by right, and required Administrative Permit (or Conditional Use after protest) for non-owner-occupied STRs in SF-10 / SF-5 / TF-3 / MF-18 / MF-29. |
| Nuisance follow-up | All-residential party-house draft deferred Sept. 2023; Ord. 52-544 (2024-09-10; effective 2024-09-13) created Ch. 5.08 limited to STRs. |
| State tax remittance | SB 50 (override 2021-05-03; effective 2021-07-01) requires marketplace facilitators to collect/remit local TGT. |
| Airbnb tax | Municipal TGT collection: **2017-02-01** (statewide KDOR VCA covering Wichita 6% TGT). |
| Airbnb data sharing | **null** — City uses Granicus/Host Compliance monitoring; no Airbnb City Portal / API feed documented. |

## Legislative history recorded

1. **SB 50 (marketplace facilitators)** — State of Kansas — 2021-05-03 / 2021-07-01 — `primary_framework`: false  
2. **Ordinance No. 52-265 (Ch. 3.40 licensing)** — City of Wichita — 2023-09-19 / 2023-09-22 — `primary_framework`: true  
3. **Ordinance No. 52-266 (UZC STR zoning)** — City of Wichita — 2023-09-19 / 2023-09-22 — `primary_framework`: true  
4. **Ordinance No. 52-544 (Ch. 5.08 nuisance parties)** — City of Wichita — 2024-09-10 / 2024-09-13 — `primary_framework`: false  

Non-binding items excluded: MAPC Policy 20 revisions; Resolution No. 248-2023; District Advisory Board presentations; Sedgwick County Commission UZC action for unincorporated areas (STRs not permitted in County residential districts); and the deferred 2023 all-residential nuisance-party draft superseded by Ord. 52-544.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Wichita entry)
- Script: `agent/scripts/update_wichita_str_regulations.py`
- Report: `agent/reports/2026-08-08-wichita-str-legislative-history.md`
