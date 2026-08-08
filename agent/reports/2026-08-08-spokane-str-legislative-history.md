# Spokane, WA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Spokane, WA (first unchecked city). Primary framework is **Ordinance C35252** (SMC Ch. 17C.316), effective/enforced **2015-06-17**: Type A/B permitting, residency rules outside RMF/RHD, business license, neighbor notice, and nuisance-based revocation. Major 2023 rewrite (**C36391**, effective **2023-09-01**) expanded STRs to all zones allowing residential uses, added multifamily unit caps and life-safety requirements, and dropped the old owner/operator residency rule; companion **C36392** raised permit fees and attempted a $4/night platform fee that was never collected and was repealed by **C36482** (2024). Statewide **SHB 1798 / RCW 64.37** (effective **2019-07-28**) added insurance, safety, and platform registration duties. Airbnb has collected Spokane-applicable local sales taxes via WA DOR since **2015-10-15**; no direct Airbnb–City data connection was found (Granicus scraping only).

## What was done

- Identified first list item lacking `agent_checked`: Spokane, WA (index 96).
- Compiled binding City ordinances and the key statewide STR statute from Spokane Official Gazette / SMC, WA Legislature / RCW 64.37, WA DOR, City STR project pages, and contemporaneous reporting (Spokesman-Review, GeekWire, Center Square).
- Excluded Housing Action Plan resolutions and non-binding study materials; omitted Ord. C36702 (2025 UDC update that re-touched STR section stamps without a clear substantive STR policy rewrite in available sources).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | Ord. **C35252** (passed 2015-05-04; effective **2015-06-17**): Chapter 17C.316 Type A/B STR permitting in residential zones. |
| State baseline | **SHB 1798** (signed 2019-05-09; effective **2019-07-28**): RCW 64.37 insurance, safety, tax, and platform registration duties. |
| 2023 rewrite | Ord. **C36391** (effective **2023-09-01**): all zones with residential uses; unit caps; life-safety form/inspections; grandfathering; removed Type A residency requirement. |
| Fees / platform fee | Ord. **C36392** (effective **2023-08-18**): higher permit fees + $4/night platform fee (never implemented). Ord. **C36482** repealed the platform fee (effective **2024-06-27**). |
| Enforcement ramp-up | City began proactive Granicus-based compliance outreach in **January 2024** after a post-adoption grace period. |
| Airbnb tax | Local retail sales tax on lodging collected via WA DOR beginning **2015-10-15**; special hotel/motel tax generally limited to 40+ unit lodging. |
| Airbnb data sharing | None identified; platform fee reporting never enforced; City uses Granicus listing monitoring. |

## Legislative history (5 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. C35252 (Ch. 17C.316) | 2015-05-04 | 2015-06-17 | 2015-06-17 | yes |
| SHB 1798 / Ch. 346 (RCW 64.37) | 2019-05-09 | 2019-07-28 | 2019-07-28 | no |
| Ord. C36391 (code amendments) | 2023-07-10 | 2023-09-01 | 2023-09-01 | no |
| Ord. C36392 (fees / platform fee) | 2023-07-10 | 2023-08-18 | 2023-08-18 | no |
| Ord. C36482 (platform fee repeal) | 2024-05-20 | 2024-06-27 | 2024-06-27 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2015-10-15** — WA DOR Airbnb tax topic; statewide voluntary collection of state/local retail sales taxes (and special hotel/motel where applicable).
- `airbnb_data_sharing_date`: **null** — no City Portal/API/feed; C36392 platform reporting never enforced; Granicus third-party monitoring only.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Spokane, WA entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_spokane.bak`
- Script: `agent/scripts/update_spokane_str_regulations.py`
- Report: `agent/reports/2026-08-08-spokane-str-legislative-history.md`
