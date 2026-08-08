# New York City short-term rental regulation dates

**Summary.** New York, NY was the first row in `AGENT_DATA_PATH/str_regulations.csv` without `agent_checked == True`, so I researched its short-term rental (STR) regulation timeline and filled in the row. NYC's first substantial city-level STR law is **Local Law 146 of 2018**, passed by the City Council on 2018-07-18 and signed by Mayor de Blasio on 2018-08-06, which required booking platforms to report host and transaction data to the Mayor's Office of Special Enforcement (OSE). Its nominal effective date of 2019-02-02 never arrived: the SDNY preliminarily enjoined the law on 2019-01-03, and the reporting regime only actually took effect on **2021-01-03** after the Council enacted settlement-mandated amendments as Local Law 64 of 2020. Airbnb's formal enforcement cooperation with the city dates to the **2020-06-12** settlement, under which Airbnb dropped its lawsuit and agreed to quarterly host/transaction data sharing. NYC has **no** tax-collection arrangement with Airbnb. Confidence is High: all dates trace to primary sources (local law texts, NYC Council Legistar, OSE, the SDNY opinion).

## Dates recorded

| Field | Value | Basis |
| --- | --- | --- |
| `passage_date` | 2018-07-18 | City Council passage of Local Law 146 of 2018 (Int. 981-A); signed by the Mayor 2018-08-06 |
| `effective_date` | 2021-01-03 | Date the booking-service reporting regime actually took effect, per OSE, following Local Law 64 of 2020 |
| `enforcement_cooperation_date` | 2020-06-12 | de Blasio–Airbnb settlement announcement: quarterly host/transaction data sharing for enforcement |
| `tax_cooperation_date` | None | No voluntary collection agreement between NYC and Airbnb exists |
| `agent_confidence` | High | |

## Reasoning and caveats

**Which law counts as "first substantial."** The binding prohibition on Airbnb-style rentals in NYC is *state* law, not city policy: Chapter 225 of the Laws of 2010 amended the Multiple Dwelling Law to bar rentals under 30 days in Class A multiple dwellings. It became law 2010-07-16 and, via a chapter amendment, took effect 2011-05-01. The earliest *city* action in this space, Local Law 45 of 2012 (Council passage 2012-09-12, mayoral approval 2012-10-02), only raised fines for illegal conversions of dwelling units and did not create an STR regime. I therefore coded Local Law 146 of 2018 as the first substantial city-passed STR policy, since it is the first city law that directly regulates Airbnb-style platforms.

**Why the effective date is 2021 rather than 2019.** Local Law 146 was written to take effect 180 days after enactment, i.e. 2019-02-02. Airbnb and HomeAway sued, and Judge Engelmayer (SDNY) preliminarily enjoined the ordinance on 2019-01-03 on Fourth Amendment grounds. The regime became operative only after the 2020 settlement was codified in Local Law 64 of 2020 (enacted 2020-07-07), which OSE states took effect 2021-01-03. Anyone wanting the nominal statutory date instead should use 2019-02-02.

**Later, more binding regime.** Local Law 18 of 2022, the Short-Term Rental Registration Law, is the city law that actually curtailed Airbnb activity in NYC. The Council passed it 2021-12-09; it became law unsigned on 2022-01-09; enforcement began 2023-09-05. If the analysis needs the date STR supply actually collapsed in NYC, 2023-09-05 is the relevant date, not the values recorded here.

**Enforcement cooperation.** On 2020-06-12 Mayor de Blasio and Airbnb jointly announced a settlement: Airbnb dismissed its federal suit and agreed to provide the city with quarterly reports (address, host name and contact, nights booked, amount received, listing URL) for listings offering an entire home or three-plus guests and booked five or more nights per quarter. Private/shared rooms for two or fewer guests were exempted. The city was required to amend the ordinance to match, which it did through Local Law 64 of 2020; data began flowing with the first reporting period starting 2021-01-03.

**Tax cooperation.** I found no formal NYC–Airbnb tax arrangement. Airbnb publicly campaigned in 2014 to be allowed to collect and remit roughly $21M/year in NYC and state lodging taxes and was rebuffed; the hotel lobby opposed it and officials cited legal barriers. Airbnb's 2018 and 2022 Albany budget testimony confirms it holds voluntary collection agreements with ~35–37 New York counties but explicitly not with NYC, and asked the legislature to mandate collection of the NYC Hotel Room Occupancy Tax. Airbnb does currently collect NY State sales tax and the state-imposed NYC hotel unit fee, but that flows from NYS Tax Law obligations on booking services, not from a city agreement, and the NYC Hotel Room Occupancy Tax administered by the Department of Finance is not covered. A secondary aggregator site claims Airbnb began collecting NYC hotel taxes on 2023-09-05 alongside Local Law 18 enforcement; I could not corroborate that against Airbnb's own help center or any city source, so I did not record it.

## Sources

- Local Law 146 of 2018 text and City Clerk certification; NYC Council Legistar file Int 0981-2018
- Local Law 64 of 2020 text; NYC Council Legistar file Int 1976-2020; OSE rulemaking notice
- Local Law 18 of 2022 text; NYC Council/intro.nyc; OSE Registration Law page (nyc.gov/site/specialenforcement)
- OSE "Laws and Rules" page confirming the reporting law took effect 2021-01-03
- SDNY preliminary injunction opinion, *Airbnb, Inc. v. City of New York*, 2019-01-03
- NYS Chapter 225 of the Laws of 2010 (nyc.gov/assets/buildings)
- Local Law 45 of 2012 text (intro.nyc)
- Airbnb newsroom "A Message to Our New York City Hosts"; AP, CityLand, NY Post coverage of the 2020-06-12 settlement
- Airbnb testimony to the NYS Joint Budget Committee (2018-01-24 and 2022-02-16) on county VCAs and the absence of NYC collection authority
- Airbnb Help Center article 2319 on occupancy tax collection in New York

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.csv` (New York, NY row; `agent_checked` set to True)
- Script: `agent/scripts/03_update_str_regulations_row.py` — reusable single-row updater; edit the `CITY`/`STATE`/`FIELDS` constants and rerun for the next city
