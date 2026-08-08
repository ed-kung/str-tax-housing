# Austin, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Austin, TX (first unchecked city). Austin created a Type 1/2 licensing framework in 2012 (expanded with Type 3 in 2013), then attempted a 2016 Type 2 phase-out and occupancy/assembly limits that courts later voided in material part (`Zaatari` 2019; `Anding` 2023). The current framework is the 2025 Title 4 overhaul (accessory-use zoning, Chapter 4-23 licensing/density rules, platform HOT from 2025-04-01, and platform license/delist duties from 2026-07-01).

## What was done

- Identified first list item lacking `agent_checked`: Austin, TX (index 10).
- Compiled binding City/State actions from 2008 onward from Austin EDIMS ordinance PDFs, City Financial Services / Development Services pages, Texas appellate and federal court materials, and reputable reporting (Austin Monitor, Statesman, KUT, KXAN).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (8 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Original framework | Ord. 20120802-122 (passed 2012-08-02; effective/enforced 2012-10-01) created Type 1/2 licensing, Type 2 3% census-tract cap, HOT proof, and local contact/notification rules. |
| 2013 expansion | Ord. 20130926-144 (effective 2014-01-01) added Type 3 multifamily caps and limited owner-present partial-unit Type 1 rentals. |
| State HOT | H.B. 1905 (effective 2015-09-01) confirmed STRs are “hotels” for state/local HOT. |
| 2016 crackdown (partly void) | Ord. 20160223-A001 froze new Type 2 licenses, added occupancy/assembly limits, and set Type 2 phase-out by 2022-04-01. `Zaatari` (2019-11-27) voided phase-out and assembly/occupancy limits; `Anding` (2023-08-01) voided the continuing homestead/Type 2 bar. April 2022 termination never took effect. |
| 2025 rebuild | Ord. 20250227-041: platform City HOT from **2025-04-01**. Ord. 20250227-039/040: accessory-use zoning + Title 4 Chapter 4-23 transition (operator rules 2025-10-01). Ord. 20250911-012: density/spacing, two-year licenses, nuisance tools; platform license field + delist duties from **2026-07-01**. |
| Airbnb tax | Municipal platform collection: **2025-04-01** (no earlier City VCA; state-only HOT since 2017). |
| Airbnb data sharing | **2026-07-01** — first binding City↔platform listing license field / delist-on-notice duties. |

## Legislative history recorded

1. **Ordinance No. 20120802-122** — City of Austin — 2012-08-02 / 2012-10-01 — `primary_framework`: true  
2. **Ordinance No. 20130926-144** — City of Austin — 2013-09-26 / 2014-01-01 — `primary_framework`: false  
3. **H.B. 1905** — State of Texas — 2015-06-20 / 2015-09-01 — `primary_framework`: false  
4. **Ordinance No. 20160223-A001** — City of Austin — 2016-02-23 / 2016-03-05 (Parts 4–5 2017-04-01) — `primary_framework`: true  
5. **Ordinance No. 20250227-041** — City of Austin — 2025-02-27 / 2025-04-01 — `primary_framework`: false  
6. **Ordinance No. 20250227-039** — City of Austin — 2025-02-27 / 2025-10-01 — `primary_framework`: false  
7. **Ordinance No. 20250227-040** — City of Austin — 2025-02-27 / effective 2025-03-10; operator application 2025-10-01 — `primary_framework`: true  
8. **Ordinance No. 20250911-012** — City of Austin — 2025-09-11 / 2025-10-01 (platforms 2026-07-01) — `primary_framework`: true  

Resolutions and withdrawn proposals (e.g., 2015 code-amendment resolutions; never-adopted denser February 2025 platform package provisions) were excluded as non-binding.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Austin entry)
- Report: `agent/reports/2026-08-08-austin-str-legislative-history.md`
