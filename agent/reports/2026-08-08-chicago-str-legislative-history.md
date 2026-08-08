# Chicago STR legislative history

Updated the first unchecked city in `AGENT_DATA_PATH/str_regulations.json` (Chicago, IL) with legislative history from 2008 onward, Airbnb municipal tax and data-sharing fields, and `agent_checked: 1`.

## Summary

Chicago’s Airbnb-relevant STR regime is centered on Ordinance O2016-5111 (Shared Housing Ordinance), passed 2016-06-22, nominally effective ~2016-12-17, and actively enforced from 2017-03-14 after litigation delayed implementation. It licensed intermediaries like Airbnb, required shared-housing registration with platform bulk registration/reporting, set primary-residence and unit-cap rules, created Restricted Residential Zones, and added a 4% homelessness surcharge. Earlier 2010 vacation-rental licensing (Chapter 4-207 / later §4-6-300) and a Nov 2010 hotel-tax expansion covered non-owner-occupied vacation rentals. A Feb 2017 amendment narrowed guest-record production to warrant/subpoena; O2018-4988 added a 2% domestic-violence surcharge (effective 2018-12-01); SO2020-3986 (2020-09-09) banned single-night rentals and overhauled registration (key provisions effective 2020-10-17; application/fee changes 2021-04-01). Airbnb began collecting Chicago’s municipal hotel tax on 2015-02-15; platform/city registration data sharing became enforceable 2017-03-14.

## Legislative history (6 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Vacation Rental Ord. (Ch. 4-207 / §4-6-300) | 2010-06-22 | 2011-01-01 | 2011-01-01 | no |
| Hotel tax expansion to vacation rentals | 2010-11-17 | 2011-07-01 | 2011-07-01 | no |
| O2016-5111 Shared Housing Ordinance | 2016-06-22 | 2016-12-17 | 2017-03-14 | yes |
| Feb 2017 guest-record amendment | 2017-02-22 | 2017-02-22 | 2017-03-14 | no |
| O2018-4988 2% DV surcharge | 2018-07-25 | 2018-12-01 | 2018-12-01 | no |
| SO2020-3986 Shared Housing reform | 2020-09-09 | 2020-10-17 | 2020-10-17 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: 2015-02-15 — voluntary collection/remittance of Chicago hotel accommodations tax (Airbnb announcement; TechCrunch; later Airbnb remittance releases).
- `airbnb_data_sharing_date`: 2017-03-14 — intermediary bulk registration/reporting obligations under O2016-5111 became enforceable after Keep Chicago Livable stay; operational registration-number issuance continued into Aug 2017.

## Notes

- Individual Restricted Residential Zone precinct ordinances were omitted (local implementations of the 2016 Chapter 4-17 framework).
- Exact full-Council vote day for the 2010 vacation-rental ordinance is less clearly cited than the June 22–23, 2010 committee substitute; `passage_date` uses that substitute date with effective date 2011-01-01 from official BACP materials.

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Chicago, IL entry)
- Backup: `AGENT_DATA_PATH/str_regulations.json.pre_chicago.bak`
