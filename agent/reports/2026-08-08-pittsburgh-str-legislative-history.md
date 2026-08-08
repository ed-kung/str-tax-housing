# Pittsburgh, PA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Pittsburgh, PA (first unchecked city). Binding STR-relevant law is thin: Allegheny County **Ord. 04-16** (2016-03-22) authorized booking-agent collection/reporting of the county hotel tax; Pennsylvania **Act 109 of 2018** (eff. **2019-01-22**) expanded state/local hotel-tax duties for booking agents; City **Ord. 23-2023** (passed 2023-09-26; program operative **2024-12-19**) rewrote Chapter 781 to cover short-term homestays, but court orders have kept enforcement voluntary (`enforcement_date` null). No City of Pittsburgh municipal occupancy/STR tax → `airbnb_tax_collection_date` null. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Pittsburgh, PA (index 67).
- Compiled binding actions from Allegheny County Code (Ord. 04-16), County Treasurer hotel-tax materials, PA DOR booking-agent guidance / Act 109 (H.B. 1511) legislative history, Pittsburgh Legistar file 2022-0270 (Ord. 23-2023), PLI Dec. 19, 2024 rules transmittal, Councilman Wilson / mayor announcements, AAMP May 2025 court-stay reporting, WESA coverage of still-pending Chapter 768 bills, and Airbnb’s Pittsburgh host help article.
- Excluded Ord. 60-2015 Chapter 781 (rental units defined as terms exceeding 15 consecutive days within 30 days—typical Airbnb stays excluded) and Ord. 42-2021 (fee-book cleanup for the non-STR-focused 2015 framework).
- Excluded non-enacted dedicated STR licensing/zoning proposals (e.g., Chapter 768 File 2025-2081 and related zoning files still in committee / session resets).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| County tax platform rules (2016) | Ord. 04-16: booking agents may collect/remit Allegheny County hotel tax; reporting duties. |
| State booking-agent tax (2018/19) | Act 109 eff. **2019-01-22**: platforms collect state + applicable local hotel taxes; accommodation fees taxable. |
| City primary framework (2023/24) | Ord. 23-2023 / Chapter 781: registration + inspection covers short-term homestays; operative **2024-12-19**. |
| Enforcement stayed | Planned June 1, 2025 mandatory enforcement blocked by Allegheny CCP stay; still voluntary. |
| No city STR tax | Lodging taxes are state + Allegheny County only. |
| Airbnb municipal tax | **null** — no Pittsburgh municipal occupancy/STR tax. |
| Airbnb data sharing | **null** — no city portal / listing compliance feed documented. |

## Legislative history (3 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Allegheny County Ord. 04-16 | 2016-03-22 | 2016-03-22 | 2016-03-22 | no |
| PA Act 109 of 2018 (H.B. 1511) | 2018-10-24 | 2019-01-22 | 2019-01-22 | no |
| Pittsburgh Ord. 23-2023 (Ch. 781) | 2023-09-26 | 2024-12-19 | null | yes |

## Airbnb fields

- `airbnb_tax_collection_date`: **null** — no municipal STR/occupancy tax; PA DOR/Airbnb state (and Allegheny county) collections do not qualify under project rules.
- `airbnb_data_sharing_date`: **null** — no documented Airbnb–City of Pittsburgh direct compliance data connection; county booking-agent reporting duties are not a city data link.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Pittsburgh, PA entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_pittsburgh.bak`
- Script: `agent/scripts/update_pittsburgh_str_regulations.py`
- Report: `agent/reports/2026-08-08-pittsburgh-str-legislative-history.md`
