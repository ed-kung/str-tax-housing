# New York, NY short-term rental legislative history and platform enforcement

New York, NY was the first entry in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked`. I researched the city's short-term rental regulatory history from 2008 forward and added `legislative_history` (7 enacted laws), `platform_enforcement` (4 arrangements), and `agent_checked: true` to that record. The defining feature of New York City is that the binding restriction is a *state* law — the 2010 Multiple Dwelling Law amendment banning sub-30-day rentals of Class A units without the permanent occupant present — and that every subsequent city measure through 2022 was an enforcement mechanism layered on top of that prohibition rather than a change to what is legal. The one exception is Local Law 18 of 2022, which added a registration-and-verification regime whose September 5, 2023 enforcement date coincided with a roughly 70-90 percent drop in NYC Airbnb listings. No relaxation of these rules has been enacted as of August 2026; the two Airbnb-backed rollback bills (Int. 948-2024 and Int. 1107-2024, reintroduced as Int. 879-2026) were not passed and are opposed by the current administration.

## Laws recorded

| Law | Jurisdiction | Passed | Effective |
| --- | --- | --- | --- |
| Ch. 225 of the Laws of 2010 (S6873-B), "Illegal Hotel Law" | New York State | 2010-07-16 | 2011-05-01 |
| Local Law 45 of 2012 (Int. 404-A) — illegal conversion fines | New York City | 2012-10-02 | 2012-12-01 |
| Ch. 396 of the Laws of 2016 (A8704-C) — advertising ban | New York State | 2016-10-21 | 2016-10-21 |
| Local Law 146 of 2018 (Int. 981-A) — monthly platform data reporting | New York City | 2018-08-06 | 2019-02-02 (enjoined 2019-01-03, never operative) |
| Local Law 64 of 2020 (Int. 1976) — quarterly platform data reporting | New York City | 2020-07-07 | 2021-01-03 |
| Local Law 18 of 2022 (Int. 2309-A) — Short-Term Rental Registration Law | New York City | 2022-01-09 | 2023-09-05 (rules 2023-03-06) |
| Ch. 656 of the Laws of 2024 as amended by Ch. 99 of 2025 — statewide registry and STR sales tax | New York State | 2024-12-24 | 2025-03-01 |

## Platform enforcement arrangements recorded

1. **2016 advertising-law settlement** (2016-12-02). Airbnb dropped its suit after the city agreed to enforce the advertising ban against hosts rather than the platform. Notable because it *reduced* platform liability.
2. **2020 host data-sharing settlement / Local Law 64** (effective 2021-01-03). Quarterly reporting on entire-unit and three-plus-guest listings to the Mayor's Office of Special Enforcement.
3. **Local Law 18 registration verification** (effective 2023-09-05). Airbnb must check registration numbers against the OSE verification API before processing bookings; also enforces the Prohibited Buildings List.
4. **Airbnb as registered NY sales tax vendor** (effective 2025-03-01). A state statutory obligation, not a negotiated city agreement — NYC declined Airbnb's 2016 offer of a voluntary hotel-tax deal and still has no separate occupancy-tax agreement with the platform.

## Coding notes

- `effective_date` for Local Law 18 is set to the enforcement start (2023-09-05) rather than the statutory 12/16-month dates, since that is when behavior actually bound. The statutory and rulemaking dates are stated in the summary.
- Local Law 146 is retained despite never taking effect, because it triggered the litigation that produced Local Law 64 and the 2020 settlement.
- Proposed but unenacted bills (Int. 948-2024, Int. 1107-2024, Int. 879-2026) were excluded from `legislative_history`.
- Local Law 77 of 2023 was checked and excluded: it is a general construction-code technical-corrections law that happens to touch the one-family dwelling definition, not an STR measure.

## Sources

Primary: NYS Chapter 225 of 2010 text (nyc.gov), NYS Chapter 396 of 2016 text (nyc.gov), NYC Council Legistar records for Int. 404-A/2010, Int. 981-A/2018, Int. 1976/2020, Int. 2309-A/2021, OSE registration and reporting law pages (nyc.gov/site/specialenforcement), OSE final rules PDFs, NYC Rules adopted-rule records, NYS Tax Department publication on sales tax on short-term rental unit occupancy, Airbnb Help Center article 2319. Secondary: NY State Senate press releases, NYC Council press release (2012-09-12), AP/Reuters/NYT coverage of the 2016 and 2020 settlements, SDNY opinions in *Airbnb v. City of New York*, NYSAC implementation memos on the 2024 state STR law.

## Artifacts

- Script: `agent/scripts/03_str_regulations_new_york_ny.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (New York, NY record)
