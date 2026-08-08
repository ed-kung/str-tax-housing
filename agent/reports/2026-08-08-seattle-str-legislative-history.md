# Seattle, WA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Seattle, WA (first unchecked city). Primary host/platform framework is Ordinance **125490** (SMC Ch. 6.600), effective/enforced **2019-01-01** (licenses issued starting 2019-01-02): operator licensing with a general two-unit cap tied to primary residence, platform licensing, listing license numbers, City-directed delisting, and electronic reporting. Companion land-use Ordinance **125483** took effect **2018-01-07** (full compliance for preexisting uses by **2019-01-07**). A dedicated city STR tax (Ord. **125442**) was repealed by Ord. **125594** after state **2SHB 2015** expanded convention-center lodging tax to STRs. Airbnb has collected Seattle-applicable local lodging taxes since **2015-10-15**; platform compliance data reporting to the City began with the first quarterly report due **2019-04-15**.

## What was done

- Identified first list item lacking `agent_checked`: Seattle, WA (index 17).
- Compiled binding City ordinances and the key state lodging-tax statute from Seattle Legistar / Municode, WA DOR, City FAS STR pages, Clerk File 321081, and contemporaneous reporting (GeekWire, Seattle Times, Urbanist).
- Excluded non-binding resolutions, retired CB 119403 (legacy-operator amendment never enacted), and Ord. 125872 (creates a revenue fund for PFD remittances; does not regulate STR operations).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2017 baseline | No dedicated STR land-use/licensing chapter; STRs treated as ordinary residential use; lodging taxes collected via state system. |
| Land use | Ord. **125483** (passed 2017-12-04; effective **2018-01-07**): defines/permits STR use, requires business + STR licenses, household occupancy limits; preexisting uses had one year to comply. |
| Primary framework | Ord. **125490** (passed 2017-12-11; Chapter 6.600 effective/enforced **2019-01-01**): unit caps, operator/platform licenses, platform reporting & delisting. Litigation did not stay rollout. |
| City STR tax | Ord. **125442** (passed 2017-11-13; tax slated **2019-01-01**) never enforced; repealed by Ord. **125594** (effective **2018-08-01**) to qualify for 2SHB 2015 remittances. |
| State lodging tax | **2SHB 2015** (effective **2018-10-01**) applied convention-center lodging tax to STRs / small premises and tied Seattle remittances to repeal of the city STR tax. |
| Airbnb tax | Municipal/local lodging taxes (special hotel/motel taxes applicable in Seattle) collected via WA DOR beginning **2015-10-15**. |
| Airbnb data sharing | Platform electronic reporting obligations under Ord. 125490; first quarterly report due **2019-04-15** (monthly listing/license reports from **2019-06-15**). |

## Legislative history (5 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. 125442 (STR tax) | 2017-11-13 | 2019-01-01 | null | no |
| Ord. 125483 (land use) | 2017-12-04 | 2018-01-07 | 2019-01-07 | no |
| Ord. 125490 (licensing Ch. 6.600) | 2017-12-11 | 2019-01-01 | 2019-01-01 | yes |
| 2SHB 2015 (state lodging tax) | 2018-03-05 | 2018-10-01 | 2018-10-01 | no |
| Ord. 125594 (tax repeal) | 2018-06-04 | 2018-08-01 | 2018-08-01 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2015-10-15** — WA DOR + GeekWire; Mayor Murray statement on Seattle collection; city Ord. 125442 tax never collected.
- `airbnb_data_sharing_date`: **2019-04-15** — first quarterly platform data submission under Ord. 125490 / FAS STR-4 implementation schedule.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Seattle, WA entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_seattle.bak`
- Report: `agent/reports/2026-08-08-seattle-str-legislative-history.md`
