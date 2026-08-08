# North Las Vegas STR legislative history

Updated `str_regulations.json` for North Las Vegas, NV (first unchecked city): local STR licensing began October 21, 2020 (Ords. 3040/3041); AB 363 and June 15, 2022 conformity ordinances (3123/3127) tightened standards and platform duties effective July 1, 2022. Airbnb does not appear to collect North Las Vegas municipal transient lodging tax; facilitator quarterly reporting under amended NRS 268.0957 is treated as the first platform data-sharing channel (2022-07-01).

## Findings

- **Primary local framework (2020-10-21):** Ordinance 3040 (Title 17 CUP zoning) and companion Ordinance 3041 ($900 annual license; 13% TLT applied to residential STRs). Review-Journal and City Council agenda confirm final adoption October 21, 2020; Airbnb host article treats that date as effective.
- **State framework (AB 363, Ch. 388, 2021):** Applies to Clark County cities including North Las Vegas; operative July 1, 2022 for facilitator tax remittance and quarterly reporting mandates, apartment bans, resort buffers, minimum stays, etc.
- **Local AB 363 conformity (2022-06-15):** Ordinances 3123 (Title 5 licensing—state license, occupancy/min-stay, platform license-number affidavit) and 3127 (Title 17—2,500-ft resort buffer, HOA letter, apartment/RV bans, security plan).
- **Airbnb tax collection:** Official Airbnb Nevada occupancy-tax page lists Clark County, Henderson, and Las Vegas but not North Las Vegas; City and Airbnb NLV pages still assign remittance to the host/operator. `airbnb_tax_collection_date` left null.
- **Airbnb data sharing:** No pre-2022 City Portal/AB 321 local reporting ordinance found. First binding facilitator→city quarterly reporting duty is AB 363’s amendment to NRS 268.0957, operative 2022-07-01.

## Sources

- City of North Las Vegas STR and Transient Lodging Tax pages; Municode ordinance PDFs 3040/3041/3123/3127
- Las Vegas Review-Journal (Oct. 23, 2020); Nevada Independent (2022 statewide AB 363 implementation)
- Avalara MyLodgeTax (June 2021); Airbnb help articles 2315 and 2913; NRS 268.0957 / 268.09799
- Vrbo lodging-tax table (NLV collection start 2024-10-01 noted for contrast only)

## Artifacts

- `AGENT_DATA_PATH/str_regulations.json` (North Las Vegas entry, index 74)
- `agent/scripts/update_north_las_vegas_str_regulations.py`
