# New York, NY short-term rental legislative history

New York, NY was the first entry in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked`. I researched the city's short-term rental regulatory history from 2008 forward and added `legislative_history` (7 enacted laws), `airbnb_tax_collection_date`, `airbnb_data_sharing_date`, and `agent_checked: true` to that record. The defining feature of New York City is that the binding restriction is a *state* law — the 2010 Multiple Dwelling Law amendment banning sub-30-day rentals of Class A units without the permanent occupant present — and that every subsequent city measure through 2022 was an enforcement mechanism layered on top of that prohibition rather than a change to what is legal. The one exception is Local Law 18 of 2022, which added a registration-and-verification regime whose September 5, 2023 enforcement date coincided with a roughly 70-90 percent drop in NYC Airbnb listings. No relaxation has been enacted as of August 2026; the Airbnb-backed rollback bills (Int. 948-2024, Int. 1107-2024, and Int. 879-2026, introduced April 30, 2026) remain in the Housing and Buildings Committee and are opposed by the Office of Special Enforcement.

## Laws recorded

| Law | Jurisdiction | Passed | Effective |
| --- | --- | --- | --- |
| Ch. 225 of the Laws of 2010 (S6873-B), "Illegal Hotel Law" | New York State | 2010-07-16 | 2011-05-01 |
| Local Law 45 of 2012 (Int. 404-A) — illegal conversion fines | New York City | 2012-10-02 | 2012-12-02 |
| Ch. 396 of the Laws of 2016 (A8704-C) — advertising ban | New York State | 2016-10-21 | 2016-10-21 |
| Local Law 146 of 2018 (Int. 981-A) — monthly platform data reporting | New York City | 2018-08-06 | 2019-02-02 (enjoined 2019-01-03, never operative) |
| Local Law 64 of 2020 (Int. 1976) — quarterly platform data reporting | New York City | 2020-07-07 | 2021-01-03 |
| Local Law 18 of 2022 (Int. 2309-A) — Short-Term Rental Registration Law | New York City | 2022-01-09 | 2023-09-05 (rules 2023-03-06) |
| Ch. 656 of the Laws of 2024 as amended by Ch. 99 of 2025 — statewide registry and STR sales tax | New York State | 2024-12-24 | 2025-03-01 |

## Airbnb tax collection and data sharing

- **`airbnb_tax_collection_date`: 2025-03-01.** New York City has no voluntary occupancy-tax collection agreement with Airbnb — the city declined Airbnb's 2016 offer of a hotel-tax deal, and Airbnb still does not collect the separate 5.875% NYC Hotel Room Occupancy Tax. Collection of a city-level tax began only under Ch. 656 of 2024 as amended by Ch. 99 of 2025, which extended state and local sales tax and the $1.50 per night NYC unit fee to short-term rental occupancy effective March 1, 2025 and made booking services registered NYS sales tax vendors. Airbnb's own help page now lists the 7-8.875% state sales tax and the NYC Hotel Unit Fee. Some trade sources put Airbnb's operational start at March 25, 2025; the NYSAC implementation memo says collections "may begin March 1, 2025," and the March 25 date in press coverage refers to the registry provisions, so the statutory effective date is used.
- **`airbnb_data_sharing_date`: 2021-01-03.** Local Law 64 of 2020 took effect that day, and OSE's rule sets the initial reporting period as January 3 through March 31, 2021, with the first report due May 31, 2021. The June 12, 2020 settlement in which Airbnb agreed to hand over host data is the negotiated origin, but January 3, 2021 is when data actually began to be captured and reported. Local Law 146 of 2018 would have started monthly reporting on February 2, 2019 but was enjoined a month earlier and never operated.

## Coding notes

- `effective_date` for Local Law 18 is set to the enforcement start (2023-09-05) rather than the statutory 12/16-month dates, since that is when behavior actually bound. The statutory and rulemaking dates are stated in the summary.
- Local Law 146 is retained despite never taking effect, because it triggered the litigation that produced Local Law 64 and the 2020 settlement.
- Proposed but unenacted bills (Int. 948-2024, Int. 1107-2024, Int. 879-2026) were excluded from `legislative_history`.
- Local Law 77 of 2023 was checked and excluded: it is a general construction-code technical-corrections law that happens to touch the one-family dwelling definition, not an STR measure.
- Local Law 45's effective date was verified as December 2, 2012 against the Department of Buildings construction-code amendment index, not December 1 as a 60-day count from the September 12 Council vote would suggest; the 60 days run from the October 2 mayoral approval.

## Sources

Primary: NYS Chapter 225 of 2010 and Chapter 396 of 2016 texts (nyc.gov), Local Law 45 of 2012 certified text (intro.nyc) and DOB construction-code amendment index, NYC Council Legistar records for Int. 981-A/2018, Int. 1976/2020 and Int. 2309-A/2021, OSE registration and reporting law pages and final rules PDFs (nyc.gov/site/specialenforcement), NYC Rules adopted-rule records, NYS Tax Department 2025 sales tax changes summary (tax.ny.gov), NYSAC STR implementation memos (March 25 and May 28, 2025), Airbnb Help Center article 2319. Secondary: NYC Council press release (2012-09-12), AP/Reuters/NYT coverage of the 2016 and 2020 settlements, SDNY opinions in *Airbnb v. City of New York*, Brick Underground and Brooklyn Paper coverage of the 2026 rollback bills, NCPR coverage of the 2024 state law.

## Artifacts

- Script: `agent/scripts/03_str_regulations_new_york_ny.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (New York, NY record)
