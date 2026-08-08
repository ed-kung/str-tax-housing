# Atlanta, GA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Atlanta, GA (first unchecked city). Atlanta’s primary STR framework is Ordinance **20-O-1656** (adopted 2021-03-15; effective 2022-03-01; city-stated enforcement 2023-03-05 after repeated penalty suspensions). Companion zoning Ord. **21-O-0682** (2021-12-06) authorized STRs citywide; SPI-18 Home Park ban Ord. **25-O-1249** (2025-08-18) is the main later restriction. Airbnb has collected Atlanta’s municipal 8% hotel-motel tax under Georgia **HB 317** since **2021-07-01**; no Airbnb–city direct data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Atlanta, GA (index 36).
- Reviewed Atlanta ordinance text and Legistar/council records (20-O-1656, 21-O-0426, 21-O-0682/Z-21-85, 22-O-1241, 22-O-1878, 25-O-1249), city STR and ATL311 pages, Georgia HB 317 / DCA hotel-motel materials, Airbnb Georgia tax help and Atlanta policy posts, and coverage (AJC, SaportaReport, GPB, WSB).
- Excluded non-enacted proposals (24-O-1687 terminated; 26-O-1084 pending) and non-binding resolutions (e.g., STR commission).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (7 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary city framework | Ord. 20-O-1656: annual STR license ($150) for primary residence + one additional unit; 24/7 agent; neighbor notice; listing license number; 3-strike/$500 penalties; 8% hotel-motel tax. |
| Effective / enforcement timing | Effectiveness delayed to **2022-03-01** (21-O-0426). Penalty authority suspended by 22-O-1241 and 22-O-1878 (plus DCP administrative delays). City ATL311 states enforcement effective **2023-03-05**; later reporting describes weak on-the-ground enforcement. |
| Zoning | Ord. 21-O-0682 (Dec. 6, 2021): defines STR and permits use in residential/SPI dwelling districts; ADU STRs require owner onsite. |
| Neighborhood ban | Ord. 25-O-1249 (Aug. 18, 2025): prohibits STRs in SPI-18 Home Park (new licenses barred; existing licensed units reported grandfathered). |
| State tax / platforms | HB 317 (signed 2021-04-21; eff. 2021-07-01): marketplace innkeepers must collect/remit local hotel-motel taxes and state $5 fee. |
| Airbnb tax | **2021-07-01** — first known municipal collection via HB 317 + Airbnb Georgia occupancy-tax practice; Airbnb reports remitting Atlanta local occupancy taxes. |
| Airbnb data sharing | **null** — no City Portal/API/data-connection announcement; HB 317 does not require listing-data sharing. |

## Legislative history recorded

1. **Ord. 20-O-1656** — City of Atlanta — Passage 2021-03-15; effective 2022-03-01; enforcement 2023-03-05 — `primary_framework`: true  
2. **HB 317 (Act 21)** — State of Georgia — Passage 2021-04-21; effective/enforced 2021-07-01 — `primary_framework`: false  
3. **Ord. 21-O-0426** — City of Atlanta — Passage 2021-07-06; effective/enforced 2021-07-14 — `primary_framework`: false  
4. **Ord. 21-O-0682 (Z-21-85)** — City of Atlanta — Passage/effective 2021-12-06; enforcement 2022-03-01 — `primary_framework`: false  
5. **Ord. 22-O-1241** — City of Atlanta — Passage/effective/enforced 2022-04-18 — `primary_framework`: false  
6. **Ord. 22-O-1878** — City of Atlanta — Passage/effective/enforced 2022-12-05 — `primary_framework`: false  
7. **Ord. 25-O-1249 (2025-29)** — City of Atlanta — Passage/effective/enforced 2025-08-18 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Atlanta entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_atlanta.bak`
- Report: `agent/reports/2026-08-08-atlanta-str-legislative-history.md`
