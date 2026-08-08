# Jersey City, NJ — STR legislative history

Updated `AGENT_DATA_PATH/str_regulations.json` for Jersey City (index 71), the first entry lacking `agent_checked`. Research covered city ordinances, New Jersey transient-accommodation tax statutes, Airbnb tax-collection reporting, and whether any Airbnb–city data connection exists.

## Summary

Jersey City first taxed STRs under Ord. 15.039 (April 2015), then affirmatively legalized them with light zoning rules under Ord. 15.137 (October 2015) in tandem with an Airbnb agreement to collect the city’s 6% hotel tax. After rapid listing growth, Ord. 19-077 (adopted June 2019; effective January 1, 2020) created Chapter 255’s restrictive permit/owner-occupancy/60-night framework; voters upheld it in a November 2019 referendum, and federal courts rejected a takings challenge. State P.L. 2018, c. 49 / 2019, c. 235 layered marketplace tax duties. Ord. 25-059 (2025) tightened Chapter 255 definitions and enforcement. Airbnb municipal tax collection began around the October 2015 agreement; no documented Airbnb direct data-sharing connection was found.

## Legislative history (binding acts)

| Date | Instrument | Role |
| --- | --- | --- |
| 2015-04-08 | Ord. 15.039 | Extended 6% hotel occupancy tax to STRs |
| 2015-10-28/30 | Ord. 15.137 | Primary legalization/zoning framework (≤5 units unlicensed; owner or lessee hosts) |
| 2018-07-01 / 2018-10-01 | P.L. 2018, c. 49 | Statewide transient-accommodation taxes; marketplace collection |
| 2019-06-25 / 2020-01-01 | Ord. 19-077 (Ch. 255) | Current primary restrictive permit framework; referendum upheld 2019-11-05 |
| 2019-08-09 | P.L. 2019, c. 235 | Narrowed state tax to marketplace / professionally managed units |
| 2025-06-11 | Ord. 25-059 | Chapter 255 definition/enforcement amendments (incl. intermediary & 275-day principal residence) |

Not included as binding legislation: the November 2019 referendum (voter confirmation of Ord. 19-077, not a new ordinance); a May 2023 amendment proposal reported as introduced but not evidenced as separately enacted.

## Airbnb tax and data fields

- **`airbnb_tax_collection_date`**: `2015-10-12` — Mayor Fulop announced Airbnb would collect/remit the municipal 6% hotel tax; contemporaneous reporting places platform charging in October 2015; first remittances for February 2016 reported via WSJ/Skift.
- **`airbnb_data_sharing_date`**: `null` — no primary-source City Portal / API / compliance feed; city has used third-party scrapers (e.g., Granicus).

## Artifacts

- Script: `agent/scripts/update_jersey_city_str_regulations.py`
- Updated JSON: `$AGENT_DATA_PATH/str_regulations.json` (Jersey City entry; `agent_checked: 1`)
