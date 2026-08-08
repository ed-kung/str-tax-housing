# Henderson, NV short-term rental legislative history

Updated `str_regulations.json` for Henderson, NV (first unchecked city), documenting STR legislative history from 2008 onward, Airbnb municipal tax-collection and platform data-sharing dates, and setting `agent_checked` to 1.

## Summary

Henderson’s modern Airbnb-style STVR program begins with **Ordinance 3591** (passed 2019-07-16; effective 2019-10-14), which opened residential neighborhoods to registered short-term vacation rentals with fees, noise/nuisance rules, and transient lodging tax filing. The city briefly **moratoriumed new registrations** (2020-09-01) and then adopted **Ordinance 3736** (2020-11-17) with 1,000-foot spacing and tighter enforcement. Nevada **AB 363** (signed 2021-06-04; operative 2022-07-01) and local **Ordinance 3840** (2022-02-15) aligned Henderson with statewide Clark County city requirements, including accommodations-facilitator tax remittance and quarterly reporting. Airbnb municipal tax collection and the first binding platform compliance-data duties are dated **2022-07-01**.

## Legislative history (binding actions)

| Date | Action |
| --- | --- |
| 2017-06-04 / eff. 2017-07-01 | NV AB 321 (Ch. 347) — enabling hosting-platform quarterly reports/subpoenas |
| 2019-07-16 / eff. 2019-10-14 | Henderson Ord. 3591 — primary STVR registration framework in residential areas |
| 2020-09-01 | 90-day moratorium on new STVR registrations |
| 2020-11-17 | Henderson Ord. 3736 — 1,000-ft spacing, faster complaint response, higher fines |
| 2021-06-04 / eff. 2022-07-01 | NV AB 363 (Ch. 388) — Clark County city STR / accommodations-facilitator framework |
| 2022-02-15 | Henderson Ord. 3840 — AB 363 conformity (state license, density, platform reports, etc.) |

## Airbnb tax and data dates

- **`airbnb_tax_collection_date`:** `2022-07-01` — City FAQs / AB 363 require facilitators to collect and remit Henderson TOT; Avalara (Nov 2020) confirmed Airbnb was not collecting in Henderson before AB 363.
- **`airbnb_data_sharing_date`:** `2022-07-01` — First binding city–platform quarterly reporting / listing-verification channel via Ord. 3840 + AB 363; city FAQs state no Airbnb business relationship / City Portal-style feed beforehand.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Henderson entry, index 56)
- Script: `agent/scripts/update_henderson_str_regulations.py`

## Sources (selected)

- City of Henderson STVR page and Development Code revisions list (Ords. 3591, 3736, 3840)
- City STVR FAQs (munirevs / cityofhenderson) on AB 363 tax remittance and platform relationship
- Las Vegas Review-Journal / KTNV / Nevada Current / Nevada Independent coverage (2019–2022)
- Airbnb help articles 2315 (NV occupancy tax) and 2640 (Henderson rules)
- Avalara MyLodgeTax (2019 / 2020 Henderson posts)
- Nevada AB 321 (Ch. 347, 2017) and AB 363 (Ch. 388, 2021) enrolled texts / LCB STR brief
