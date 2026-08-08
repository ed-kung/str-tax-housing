# Houston STR legislative history research

**Summary:** Researched and recorded Houston, TX short-term rental legislative history (from 2008), Airbnb municipal tax-collection date, and Airbnb data-sharing status in `AGENT_DATA_PATH/str_regulations.json`. Houston had no dedicated STR land-use/registration ordinance until Ordinance No. 2025-322 (passed 2025-04-16; effective/enforced 2026-01-01). State H.B. 1905 (2015) clarified that STRs are “hotels” for occupancy-tax purposes. Airbnb began collecting Houston’s 7% municipal HOT on 2019-07-01; no direct Airbnb–City compliance data connection is documented yet (platform delisting notices slated for 2027-01-01).

## City processed

- **Houston, TX** (index 3 in `str_regulations.json`; first entry lacking `agent_checked`)

## Legislative history recorded

1. **H.B. 1905 (Acts 2015, 84th Leg., ch. 1255, § 22(a))** — Texas Tax Code § 156.001  
   - Signed 2015-06-20; effective/enforced 2015-09-01  
   - Explicitly includes short-term rentals in the “hotel” definition for state and municipal/county HOT  
   - `primary_framework`: false

2. **Ordinance No. 2025-322 (Chapter 28, Article XXIII)** — City of Houston  
   - Passed 2025-04-16; effective and host-enforcement 2026-01-01  
   - First city registration-based STR framework ($275 certificate; platform notice/delisting duties; nuisance/crime revocation grounds)  
   - `primary_framework`: true  
   - Platform delisting notices deferred to 2027-01-01 per City STR page (as of research date)

## Airbnb fields

| Field | Value |
| --- | --- |
| `airbnb_tax_collection_date` | `2019-07-01` (Houston First / Airbnb municipal HOT agreement) |
| `airbnb_data_sharing_date` | `null` (no API/data feed; platform delisting not yet begun) |

## Primary sources used

- City of Houston ARA press release (2025-04-17) and adopted ordinance PDF / Exhibit A  
- City STR registration page (`houstontx.gov/ara/str.html`) and registration checklist (Ord. 2025-322)  
- Texas Legislature history / enrolled text for H.B. 1905  
- Airbnb newsroom: Houston HOT collection starting July 1, 2019  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Houston entry; `agent_checked`: 1)
