# Lubbock, TX — short-term rental legislative history

**Summary:** Documented Lubbock’s STR regulatory timeline from 2008 onward and updated `str_regulations.json` (index 83). Binding actions are Texas H.B. 1905 (2015 HOT definition), Lubbock County’s 2% venue HOT order (2019-06-10; collection 2019-07-01), City Ordinances 2019-O0127 (registration; permit effective 2019-10-01) and 2019-O0128 (7% city HOT for STRs; enforced 2020-01-01), and UDC Ordinance 2023-O0054 (effective 2023-10-01) recodifying STR limited-use/primary-residence rules and permits. Airbnb collects only Texas state HOT for Lubbock listings; no municipal platform tax agreement or direct Airbnb–City data connection was identified.

## City processed

- **City:** Lubbock, TX
- **JSON index:** 83
- **`agent_checked`:** 1

## Legislative history (binding actions)

| Date | Instrument | Role |
| --- | --- | --- |
| 2015-06-20 / eff. 2015-09-01 | H.B. 1905 (Tax Code § 156.001) | Statewide STR-as-hotel clarification for HOT |
| 2019-06-10 / eff. 2019-07-01 | Lubbock County venue HOT order (2%) | County HOT on hotels/STRs for Expo Center venue |
| 2019-09-10 / permit eff. 2019-10-01 | Ordinance 2019-O0127 | First city STR registration/permit regime |
| 2019-09-10 / eff. 2020-01-01 | Ordinance 2019-O0128 | Article 18.03 HOT expressly covers STRs (7%) |
| 2023-05-09 / eff. 2023-10-01 | Ordinance 2023-O0054 (UDC Ch. 39) | Limited-use STR standards + § 39.07.029 permit |

Primary local framework: **2019-O0127** (registration) and **2023-O0054** (current UDC land-use/permit framework), both `primary_framework: true`.

## Airbnb tax / data sharing

- **`airbnb_tax_collection_date`:** `null` — City FAQs state platforms collect state HOT only; hosts remit Lubbock’s 7% municipal HOT via the City portal. Airbnb’s Texas state collection (2017-05-01) is not municipal-level.
- **`airbnb_data_sharing_date`:** `null` — Permits/taxes run through Deckard Rentalscape (formerly MUNIRevs); no Airbnb API/compliance data feed found.

## Sources (selected)

- City of Lubbock Council minutes (2019-09-10): Ordinances 2019-O0127 / 2019-O0128
- Lubbock Code Art. 18.03 HOT; UDC §§ 39.02.018c.6, 39.07.029 (Ord. 2023-O0054)
- City STR FAQ / Rentalscape portal materials (mylubbock.us)
- Lubbock County Commissioners Court hotel occupancy tax levy order (2019-06-10)
- Texas H.B. 1905; Avalanche-Journal / KCBD coverage (2019 STR registration & tax)

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Lubbock entry)
- Script: `agent/scripts/update_lubbock_str_regulations.py`
