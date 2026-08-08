# Boston, MA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Boston, MA (first unchecked city). Primary host/platform framework is **CBC §9-14** (Docket #0764), passed **2018-06-13**, signed **2018-06-15**, effective/enforced for hosts **2019-01-01** (investor ban + registration; platform data/delisting delayed by Airbnb litigation until the **2019-08-29** settlement). State **Chapter 337** (approved **2018-12-28**) extended room occupancy taxes and intermediary collection to STRs effective **2019-07-01**. Boston Docket **#0644** raised the local rooms rate to **6.5%** and adopted **3%** community impact fees effective **2019-07-01**. Zoning **Text Amendment No. 444** (Application No. 491) closed the executive-suite loophole effective **2020-01-10**. Airbnb has collected Boston municipal lodging taxes since **2019-07-01** and established settlement-based data sharing / city-directed delisting on **2019-08-29**.

## What was done

- Identified first list item lacking `agent_checked`: Boston, MA (index 24).
- Compiled binding city and state actions from Boston.gov ordinance PDF / STR program pages, Massachusetts session laws and DOR TIR 19-3 / DLS room-tax databank, court filings in *Airbnb v. City of Boston*, and contemporaneous reporting (WBUR, AP, Boston Herald, Boston Globe, Council notes).
- Excluded non-binding resolutions and the Aug 2019 settlement itself from `legislative_history` (settlement informs enforcement and Airbnb data fields only).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2018 baseline | No dedicated STR ordinance; Airbnb-style rentals largely unregulated in Boston. |
| Primary framework | Docket #0764 / CBC §9-14: owner-occupant-only home-share / limited-share / owner-adjacent model; annual ISD registry; booking-agent duties. |
| Litigation | Airbnb sued Nov 2018; stipulation delayed platform fines/data sharing; May 3, 2019 PI enjoined §9-14.10(b); settlement Aug 29, 2019 restored data sharing and delisting. |
| State tax/insurance | Chapter 337 (as amended by St. 2019, c. 5): STR room occupancy tax, intermediary collection, $1M insurance, statewide registry; eff. 2019-07-01. |
| Local tax | Docket #0644: 6.5% local rooms + 3% CIF (both §3D options); DLS effective 2019-07-01. |
| Zoning cleanup | Text Amd. No. 444 (App. 491): executive suites no longer by-right conversion path around §9-14; eff. 2020-01-10. |
| Airbnb tax | Municipal Boston local option + convention center fee (and CIF where applicable) collected via platform from **2019-07-01**. |
| Airbnb data sharing | Settlement **2019-08-29**; registration field **2019-09-01**; unregistered listings removed by **2019-12-01**. |

## Legislative history (4 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Docket #0764 / CBC §9-14 | 2018-06-13 | 2019-01-01 | 2019-01-01 | yes |
| St. 2018, c. 337 (as amd. St. 2019, c. 5) | 2018-12-28 | 2019-07-01 | 2019-07-01 | no |
| Docket #0644 (6.5% + CIF) | 2019-04-24 | 2019-07-01 | 2019-07-01 | no |
| Zoning Text Amd. No. 444 | 2020-01-08 | 2020-01-10 | 2020-01-10 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2019-07-01** — Airbnb Boston help article + Chapter 337 / DLS municipal rate effective date; includes City local option and convention center fee (not state-only).
- `airbnb_data_sharing_date`: **2019-08-29** — City–Airbnb settlement establishing monthly listing data reports and city-directed delisting after platform provisions were stayed in litigation.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Boston, MA entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_boston.bak`
- Report: `agent/reports/2026-08-08-boston-str-legislative-history.md`
