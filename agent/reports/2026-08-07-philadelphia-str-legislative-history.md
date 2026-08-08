# Philadelphia, PA short-term-rental legislative history

Philadelphia was the sixth city in `AGENT_DATA_PATH/str_regulations.json` and the first without `agent_checked: True`. Its short-term-rental history has two turning points and little else. Bill No. 150441-A (June 2015) legalized and taxed platform rentals in residential districts for the first time, creating the accessory "Limited Lodging" use with a 180-day annual cap and extending the 8.5% Hotel Room Rental Tax to short-term rentals with booking agents authorized to collect it. Bill No. 210081 (June 2021) replaced that regime with a licensing system: every host needs a Limited Lodging Operator License restricted to primary residents, every platform needs a Booking Agent License and must delist unlicensed properties, and the 180-day cap was dropped. A single state law is relevant, Pennsylvania Act 109 of 2018, which made booking agent collection of the state and Philadelphia hotel taxes a statutory duty rather than a voluntary agreement. Five binding actions were recorded, plus `airbnb_tax_collection_date` of 2015-07-15 and `airbnb_data_sharing_date` of 2023-03-30.

## What was recorded

| Passed | Effective | Jurisdiction | Action |
| --- | --- | --- | --- |
| 2011-12-15 | 2012-08-22 | City | Bill No. 110845, new Zoning Code with the Visitor Accommodations use |
| 2015-06-18 | 2015-07-01 | City | Bill No. 150441-A, Limited Lodging use and Hotel Tax on short-term rentals |
| 2018-10-24 | 2019-01-22 | State | Act 109 of 2018 (HB 1511), booking agent hotel occupancy tax collection |
| 2021-06-10 | 2022-04-01 | City | Bill No. 210081, operator and booking agent licenses |
| 2023-11-30 | 2023-12-13 | City | Bill No. 230647, shared retaining wall exception to license issuance |

## Notes on judgment calls

The 2011 zoning code replacement is included even though it is not short-term-rental legislation, because Sec. 14-601(7)(n) "Visitor Accommodations" is still the operative use category for any unit without a primary resident and is the reason non-owner-occupied rentals are confined to commercial and mixed-use districts. All eight of its measures are coded "no change" since it recodified an existing prohibition rather than tightening one.

Bill No. 210081 has a split effective date written into Section 5: the zoning and hotel tax amendments took effect immediately on June 23, 2021, and the licensing chapters on April 1, 2022. The April 2022 date is recorded as the effective date because the licensing regime is the substantive change. Implementation was then deferred twice by administrative action rather than by ordinance, to July 1, 2022 and then to January 1, 2023, so no separate legislative entries exist for the delays. Actual enforcement began July 12, 2023, when L&I started ordering booking agents to delist unlicensed properties.

Bill No. 230647 is principally a shared-retaining-wall ordinance. It is included because it amended Sec. 9-3909(4)(b), the operator license disqualification for outstanding Title 4 violations, which is a narrow relaxation coded as a decrease in registration requirements.

Excluded: Mayor Parker's 2026 budget proposal to raise the short-term rental tax rate by 6 percentage points, which City Council removed from the preliminary budget in June 2026 and which would in any case have required state enabling legislation. Also excluded are Bills 180939-A, 250774, 250329-AA and 250980-A, which amend rental licensing and non-resident landlord registration generally rather than short-term rentals.

## Airbnb dates

`airbnb_tax_collection_date` is 2015-07-15. The 2015 ordinance took effect July 1, but two Inquirer reports (July 3, 2015 and June 15, 2016) both state the city began collecting the 8.5% occupancy tax on July 15, 2015, with Airbnb named as the collecting booking agent. The city later confirmed in a 2018 Department of Revenue post that Airbnb, uniquely among platforms at the time, collects and remits the Hotel Tax on hosts' behalf. Airbnb separately began collecting Pennsylvania's 6% state hotel occupancy tax on July 1, 2016 under a voluntary agreement with the Department of Revenue.

`airbnb_data_sharing_date` is 2023-03-30. Airbnb declined to hand over host addresses without a formal legal demand, so the city issued subpoenas; hosts received Airbnb notices in late March 2023 stating the company had to produce responsive documents on March 30, 2023. Booking agents have since submitted recurring Transaction History Reports to L&I listing host name, property address, license type and license number, which the City Controller analyzed in its June 2026 review. Note that the 2015 ordinance already obligated booking agents to supply operator lists on request, and Sec. 9-3910(5) added a reporting duty in 2021, but the March 2023 subpoena response is the first documented instance of Airbnb actually transferring data for compliance and enforcement.

## Sources

Certified bill texts from American Legal Publishing (150441-A, 210081, 230647, 110845) and Philadelphia Legistar; Pennsylvania Act 109 of 2018 from palegis.us; City of Philadelphia announcements from phila.gov (July 2022 zoning and license guidance, July 2023 delisting notice, October 2023 short-term rental webinar, September 2025 Limited Lodging FAQ); the June 2026 City Controller report on short-term rentals; and reporting from the Philadelphia Inquirer, WHYY, Billy Penn and Bisnow.

## Artifacts

- `agent/scripts/03_str_legislative_history_philadelphia.py` — script that writes the entry
- `AGENT_DATA_PATH/str_regulations.json` — updated in place, index 5 (`Philadelphia`, `PA`)
