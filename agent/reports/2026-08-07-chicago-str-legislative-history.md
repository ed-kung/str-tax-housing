# Chicago, IL short-term-rental legislative history

The first entry in `AGENT_DATA_PATH/str_regulations.json` without `"agent_checked": True` was index 2, Chicago, IL. I compiled 13 binding city, county and state actions from 2010 through mid-2026 that regulate or tax Airbnb-style rentals in Chicago, wrote them to the Chicago entry as `legislative_history` (sorted by passage date, same schema as the existing New York and Los Angeles entries), and added `airbnb_tax_collection_date` = 2015-02-15, `airbnb_data_sharing_date` = 2017-03-14 and `agent_checked` = true. The two pivotal events are the 2010 Vacation Rental Ordinance (Council journal 11-3-10, effective January 1, 2011), which created the vacation rental license and barred new whole-unit rentals in low-density residential zones, and the 2016 Shared Housing Ordinance (O2016-5111, passed June 22, 2016), whose 4 percent surcharge began July 1, 2016 but whose regulatory core was stayed by the federal court in the HomeAway/Mendez litigation until March 14, 2017. Later actions tightened the regime (single-night rental ban and city-controlled registration in 2020, monthly operator reporting in 2025) and shifted lodging tax collection onto platforms (Illinois P.A. 104-0006 in 2025 and P.A. 104-0468 in 2026).

## What was done

- Identified the first unchecked city and matched the schema used for the already-completed New York and Los Angeles entries (rich narrative `summary`; `measures` values limited to `increase`, `decrease`, `no change`).
- Reconstructed the legislative history from primary sources where reachable: the American Legal Publishing municipal code annotations (which give Council journal dates), the City of Chicago BACP posting of the 2010 vacation rental ordinance and its licensing fact sheet, the September 9, 2020 mayoral press release, the March 13, 2017 opinion in the federal challenge to the Shared Housing Ordinance, HomeAway's complaint, the Cook County hotel tax ordinance and Department of Revenue guidance, the December 2025 Chicago revenue ordinance as published in the Council journal, the Illinois compiled statutes source notes, and Illinois Department of Revenue Informational Bulletin FY 2026-33. Chicago Legistar's API and full-text pages are behind Cloudflare and could not be fetched directly; news reporting (Chicago Sun-Times, Chicago Tribune, WTTW, The Daily Line) and Avalara/industry compliance guidance filled the remaining gaps.
- Excluded non-binding items (committee recommendations, mayoral proposals that were superseded) and purely technical recodifications, notably the May 9, 2012 license reform ordinance that renumbered Chapter 4-207 to MCC 4-6-300 and P.A. 104-0417 (August 15, 2025), which made drafting changes to the same hotel tax definitions.

## Entries written (passage date -> effective date)

| Passage | Effective | Jurisdiction | Action |
| --- | --- | --- | --- |
| 2010-11-03 | 2011-01-01 | City | Vacation Rental Ordinance, Chapter 4-207 (now 4-6-300) plus zoning amendments |
| 2010-11-17 | 2011-07-01 | City | Hotel Accommodations Tax extended to all vacation rentals (7-unit threshold deleted) |
| 2015-11-18 | 2016-05-01 | Cook County | 1 percent county Hotel Accommodations Tax, applied to short-term rentals |
| 2016-06-22 | 2017-03-14 | City | Shared Housing Ordinance, O2016-5111 (4 percent surcharge from 2016-07-01) |
| 2017-02-22 | 2017-03-14 | City | Litigation-driven amendments; added platform summary/attestation duty (4-13-215) |
| 2017-06-28 | 2017-06-28 | City | First Restricted Residential Zone designations, 13th Ward |
| 2018-07-25 | 2018-12-01 | City | Surcharge raised 4 to 6 percent for domestic violence services |
| 2020-09-09 | 2020-10-17 | City | Shared Housing Reform Ordinance, SO2020-3986 (single-night ban; registration moved to BACP) |
| 2021-03-24 | 2021-04-01 | City | Registration provisions delayed from April 1 to June 1, 2021 |
| 2025-05-21 | 2025-05-21 | City | SO2024-0013637 monthly operator reporting, disclosure and database requirements |
| 2025-06-16 | 2025-07-01 | State | P.A. 104-0006: state Hotel Operators' Occupation Tax extended to short-term rentals |
| 2025-12-19 | 2026-01-01 | City | 2026 revenue ordinance: registration fee $150 to $250, operator license $250 to $500 |
| 2026-06-16 | 2026-07-01 | State | P.A. 104-0468: hosting platforms as hotel marketplace facilitators |

## Airbnb tax collection and data sharing

- `airbnb_tax_collection_date` = **2015-02-15**. Airbnb began collecting Chicago lodging taxes on behalf of hosts on February 15, 2015, following the city budget director's November 2014 initiative to capture the hotel tax on short-term rentals; the date was reported contemporaneously (Washington Post, January 2015) and repeated in the short-term-rental policy literature.
- `airbnb_data_sharing_date` = **2017-03-14**. The Shared Housing Ordinance made Airbnb a licensed short term residential rental intermediary with twice-monthly unit-list and bi-monthly aggregate reporting duties to BACP. Those provisions were stayed until March 14, 2017, and the NBER working paper on Chicago home-sharing regulation dates the start of Airbnb's data sharing with the city to March 2017.

## Caveats

- The effective date for SO2024-0013637 is recorded as its passage date (2025-05-21). The substitute's own effective clause could not be retrieved (Legistar full text is Cloudflare-protected); the Municipal Code annotations carry the May 21, 2025 journal, and Avalara's early-July 2025 coverage described the monthly reporting duty as already in force, so the true operative date is likely a few weeks after the date recorded.
- The 2016 Shared Housing Ordinance carries three real dates (surcharge 2016-07-01, originally scheduled 2016-12-17, judicially stayed to 2017-03-14). The single `effective_date` field holds 2017-03-14, the date the regulatory regime actually began; the summary states the surcharge date explicitly, which matters for tax-revenue work.
- Restricted Residential Zone designations are recurring precinct-level ordinances, not a single event. Only the first tranche (June 28, 2017) is recorded, with the rolling nature noted in the summary; a complete list would require enumerating each precinct ordinance in Legistar.
- Cook County's coverage of short-term rentals rests on the county's own administrative guidance rather than an ordinance amendment naming short-term rentals, so the 2015 entry is dated to the adoption of the county tax itself.
- The 2021-03-24 delay and the 2018 surcharge increase are recorded with all `measures` at "no change" because they postponed or repriced existing obligations rather than changing regulatory substance.

## Artifacts

- `agent/scripts/03_str_regulations_chicago.py` - idempotent-by-inspection script holding the Chicago data; it verifies that the first unchecked entry is Chicago, IL and that entries are sorted by passage date, backs up the JSON, then writes the update.
- `AGENT_DATA_PATH/str_regulations.json` - updated in place (Chicago entry at index 2).
- `AGENT_DATA_PATH/str_regulations.json.bak` - pre-update backup.
