# Explanations for the Airbnb tax collection and data sharing dates

Added `airbnb_tax_collection_date_explanation` and `airbnb_data_sharing_date_explanation` to each of the nine cities in `AGENT_DATA_PATH/str_regulations.json` that carry `agent_checked: true` (New York, Los Angeles, Chicago, Houston, Phoenix, Philadelphia, San Antonio, San Diego, Dallas). The explanations were not researched afresh: each per-city report already under `agent/reports/` documents how its two dates were reached, including the alternatives that were considered and rejected, so the text is a condensation of those reports. The remaining 91 cities were left untouched. No other field of any record was modified, and each explanation is inserted immediately after the date field it describes.

## Where the dates come from

Four distinct mechanisms produced the tax collection dates, and the explanations say which applies:

| City | Tax date | Mechanism |
| --- | --- | --- |
| Chicago | 2015-02-15 | Voluntary agreement, no ordinance in force |
| San Diego | 2015-07-01 | Voluntary agreement, no ordinance in force |
| Los Angeles | 2016-08-01 | Voluntary agreement, no ordinance in force |
| Philadelphia | 2015-07-15 | Ordinance authorized booking-agent collection; date of actual collection used |
| Phoenix | 2017-01-01 | State statute plus state-negotiated partnership covering municipal tax |
| Houston | 2019-07-01 | Agreement with the city's designated collection agent (Houston First) |
| San Antonio | 2025-03-10 | Compelled by city ordinance after voluntary talks failed |
| New York | 2025-03-01 | Compelled by state statute after the city refused a voluntary deal |
| Dallas | null | No agreement ever executed; city HOT is host-remitted |

Data sharing dates split more simply between an ordinance reporting duty becoming operative (New York 2021-01-03, Chicago 2017-03-14, San Diego 2023-05-01), a voluntary API launch (Los Angeles 2020-08-31), a subpoena response (Philadelphia 2023-03-30), and no sharing at all (Houston, Phoenix, San Antonio, Dallas).

## Recurring distinctions the explanations make explicit

- **State tax collection is not city tax collection.** Airbnb's May 1, 2017 Texas Comptroller agreement covers only the 6 percent state HOT and is the reason Houston, San Antonio and Dallas do not use that date. The same distinction is drawn for Philadelphia (state 6 percent hotel occupancy tax, from 2016-07-01) and Phoenix, where the state partnership is used precisely because it did cover municipal transient lodging tax.
- **Enacted is not operative.** Chicago's data date is the judicial stay expiry rather than the ordinance's original effective date; San Diego's is the post-Coastal-Commission enforceability date, about two years after passage; New York's rejects the enjoined 2018 law in favor of the 2020 replacement; Philadelphia's tax date is the reported first collection two weeks after the ordinance date.
- **Direction of data flow matters.** Houston, San Antonio and Dallas all have platform obligations under which the *city* tells the platform what to delist. That is not Airbnb-to-city data sharing and is why those entries are null. The same reasoning excluded Los Angeles's late-2019 listing removals in favor of the August 2020 API launch.
- **Alternative codings are stated where they exist.** San Antonio (2025-02-01, first covered receipts) and New York (2025-03-25, appearing in trade coverage but referring to the registry) both carry a defensible alternative, noted in the explanation text.

## Note on Dallas

Dallas has `agent_checked: true` and a six-entry legislative history but null for both dates. It was treated as filled and given explanations of why each date is null, since the null is a researched finding rather than missing work. If the intent was to skip it, remove the two keys from the Dallas record.

## Artifacts

- Script: `agent/scripts/03_str_regulations_date_explanations.py` — guards on the existing date values before writing, so it fails rather than mislabeling a date that has since changed
- Updated data: `AGENT_DATA_PATH/str_regulations.json`
- Backup of prior file: `AGENT_DATA_PATH/str_regulations.json.20260807-231222.bak`

Verified after writing that record count, ordering, and every pre-existing key and value are unchanged, and that the two new keys appear on exactly the nine checked cities.
