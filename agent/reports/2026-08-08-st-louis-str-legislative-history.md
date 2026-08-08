# St. Louis, MO short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for St. Louis, MO (first unchecked city). The city’s first binding STR framework is **Ordinance 71729** (signed 2023-11-06; operative 2024-11-06), with companion zoning **Ordinance 71730**, Zone A update **Ordinance 71940**, voter-approved **Proposition S** (2024-11-05), and implementing **Ordinance 72095** (2026-02-23) for the 3% STR license fee. Ordinance 71729 never reached active enforcement (April 2025 TRO; city still not enforcing). Airbnb began collecting City hotel/convention taxes on **2018-12-01**. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: St. Louis, MO (index 75).
- Compiled binding actions from City Board Bills/Ordinances 71729, 71730, 71881/Proposition S, 71940, and 72095; Mayor and License Collector press releases; Building Division STR permit pages and court-order notice; STLPR / St. Louis Magazine / Spectrum coverage of litigation and Prop S; Airbnb Missouri occupancy-tax help article.
- Excluded non-binding debate, failed/unenacted proposals, Missouri DOR statewide Airbnb tax collection (state-level only), and Granicus/Host Compliance listing scraping (not an Airbnb data share).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework (2023/24) | Ord. 71729: permits, 2-night minimum, agent-on-site-in-1-hour, Non-Occupied caps, platform permit/registry duties. |
| Zoning companion | Ord. 71730: STR permitted use citywide (eff. 2023-12-06); Ord. 71940 makes Zone A conditional use. |
| Enforcement stayed | TRO 2025-04-22 before May 6, 2025 compliance deadline; city still not enforcing 71729. |
| Prop S / 3% fee | Voters approved 2024-11-05; Ord. 72095 (2026-02-23) created collection via STR business license + 3% fee. |
| Airbnb municipal tax | **2018-12-01** — City Convention & Sports (3.5%) + Convention & Tourism (3.75%) taxes. |
| Airbnb data sharing | **null** — no City Portal / API; 71729 platform rules unenforced. |

## Legislative history (5 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. 71729 (BB 33) STR permitting | 2023-11-06 | 2024-11-06 | null | yes |
| Ord. 71730 (BB 34) zoning Ch. 26.76 | 2023-11-06 | 2023-12-06 | 2023-12-06 | no |
| Proposition S (via Ord. 71881) 3% fee | 2024-11-05 | 2024-11-05 | null | no |
| Ord. 71940 (BB 113) Zone A CUP | 2024-12-10 | 2024-12-10 | null | no |
| Ord. 72095 (BB 126) license + 3% fee | 2026-02-23 | 2026-02-23 | 2026-02-23 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2018-12-01** — City License Collector / Airbnb voluntary agreement for municipal hotel/convention taxes (not state-only).
- `airbnb_data_sharing_date`: **null** — no documented direct Airbnb–city compliance data connection; Ord. 71729 platform verification never actively enforced.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (St. Louis, MO entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_st_louis.bak`
- Script: `agent/scripts/update_st_louis_str_regulations.py`
