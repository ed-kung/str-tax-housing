# El Paso, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for El Paso, TX (first unchecked city). El Paso had no dedicated STR land-use ordinance until Ordinance No. 019840 (2026-02-03), which defines STRs in Title 20 and treats them as by-right under base residential zoning (ending the prior bed-and-breakfast special-permit classification). Texas H.B. 1905 (2015) made STRs “hotels” for HOT purposes, but the City did not collect municipal HOT from STRs until a June 9, 2026 resolution directed collection to begin 90–180 days later. Airbnb’s Texas tax page does not list El Paso for municipal HOT; no Airbnb–city data connection was found.

## What was done

- Identified first unchecked city in `AGENT_DATA_PATH/str_regulations.json`: **El Paso, TX**.
- Reviewed City of El Paso Legistar materials (File 26-0022 / Ordinance 019840; File 26-0726 resolution; Feb. 3 and June 9, 2026 Council minutes), City press release on STR HOT, Planning staff STR briefings, Texas H.B. 1905, and Airbnb’s Texas occupancy-tax help article.
- Updated the El Paso JSON object with `legislative_history`, Airbnb tax/data fields, and `agent_checked: 1`.

## Binding legislative history (included)

1. **H.B. 1905 (2015)** — State of Texas; signed 2015-06-20; effective/enforced 2015-09-01. Defines STRs as “hotels” for state and local HOT (Tax Code §§ 156 / 351 / 352). Relevant because El Paso’s Chapter 3.12 municipal HOT thereby applies to STRs as a matter of state law, even though the City long did not collect from STR operators.
2. **Ordinance No. 019840 (2026-02-03)** — City of El Paso primary STR zoning framework. Adds § 20.02.870.5 STR definition (<30 consecutive days; excludes B&B; base residential zoning standards apply). Effective upon adoption (Charter § 3.14). Does not create permits, density caps, or platform duties.

## Binding actions noted but excluded from `legislative_history`

- **June 9, 2026 Resolution (Legistar File 26-0726)** — Unanimously approved resolution authorizing the City Manager to begin collecting Chapter 3.12 HOT on STRs under Tax Code § 156.001(b), with collection to start 90–180 days after adoption. Excluded because project guidelines omit non-ordinance resolutions unless they become binding legislation; this is an administrative collection directive under existing HOT law rather than a code amendment.

## Airbnb tax and data fields

| Field | Value |
| --- | --- |
| `airbnb_tax_collection_date` | `null` |
| `airbnb_data_sharing_date` | `null` |

- Municipal HOT collection window opens no earlier than ~2026-09-07; Airbnb’s Texas help page lists state HOT and many cities’ local HOT but **not** El Paso.
- No documented Airbnb–City listing/data API or compliance portal.

## Artifacts

- Updated: `/Users/ekung/Dropbox/projects/str-tax-housing-bot/str_regulations.json` (El Paso entry)
- Next unchecked city after this update: Las Vegas, NV
