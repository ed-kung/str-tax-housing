# New York City STR legislative history

Updated the first unchecked city in `AGENT_DATA_PATH/str_regulations.json` (New York, NY) with legislative history from 2008 onward, Airbnb municipal tax and data-sharing fields, and `agent_checked: 1`.

## Summary

New York City’s Airbnb-relevant STR regime rests on two primary frameworks: the 2010 state Multiple Dwelling Law “illegal hotels” amendment (Class A units generally limited to permanent residence / 30+ day occupancy) and Local Law 18 of 2022 (host registration plus platform verification, actively enforced from 2023-09-05). Intermediate laws added advertising penalties (2016), attempted then enjoined platform data reporting (LL 146/2018), and an enforceable narrowed reporting regime after the Airbnb settlement (LL 64/2020, effective 2021-01-03). No confirmed date was entered for Airbnb collection of NYC’s municipal hotel occupancy tax; state-administered sales tax / hotel unit fee collection does not qualify. First city data-sharing date is 2021-01-03.

## Legislative history (6 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ch. 225/2010 (MDL Class A), as amd. Ch. 566/2010 | 2010-07-16 | 2011-05-01 | 2011-05-01 | yes |
| Ch. 396/2016 advertising ban | 2016-10-21 | 2016-10-21 | 2016-10-21 | no |
| Local Law 146/2018 data reporting | 2018-08-06 | 2019-02-02 | null (enjoined) | no |
| Local Law 64/2020 reporting amendment | 2020-07-07 | 2021-01-03 | 2021-01-03 | no |
| Local Law 18/2022 registration | 2022-01-09 | 2023-01-09 | 2023-09-05 | yes |
| Ch. 672/2024 statewide booking-service tax (amd. Ch. 99/2025) | 2024-12-24 | 2025-03-01 | 2025-03-01 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: null — official Airbnb NY help lists NYS sales tax and the state-administered NYC Hotel Unit Fee, not NYC DOF Hotel Room Occupancy Tax; municipal-tax rule not met.
- `airbnb_data_sharing_date`: 2021-01-03 — first enforceable direct reporting under LL 64 after LL 146 was enjoined; LL 18 verification API followed on 2023-09-05.

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (New York, NY entry)
