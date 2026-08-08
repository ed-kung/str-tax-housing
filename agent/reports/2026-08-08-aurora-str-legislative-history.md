# Aurora, CO short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Aurora, CO (first unchecked city). Binding City STR framework began with Ordinance 2016-64 (passed/effective 2016-12-05), requiring business/lodger’s licenses and license numbers in STR advertisements. Ordinance 2020-19 (passed 2020-06-22; effective 2020-08-01) made marketplace facilitators collect City sales and 8% lodger’s taxes. Ordinance 2021-63 (2021-11-22) codified primary-residence operation, a 180-day whole-home cap, one-booking-at-a-time rules, and neighborhood-impact duties. Ordinance 2024-41 (2024-09-09) added $1,000/day platform liability for unlicensed or non-primary-residence bookings. Airbnb remits Aurora’s municipal Lodger’s Tax under the 2020 marketplace/lodger framework (`airbnb_tax_collection_date`: **2020-08-01**). No documented Airbnb–City direct data-sharing connection; `airbnb_data_sharing_date` is null.

## What was done

- Identified first list item lacking `agent_checked`: Aurora, CO (index 51).
- Reviewed Aurora Municipal Code §§26-215–26-220 and Ch. 130 lodger’s/marketplace provisions; City-published Ord. 2020-19 PDF (OCR); City STR FAQs (Mar 2024 / Oct 2025); City Taxes marketplace notice; CML marketplace tracking; Airbnb Colorado help article 2298; Sentinel Colorado 2015–2016 coverage of the home-occupation/license transition; and HB19-1240 for state marketplace sales-tax duties.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2016 | Complaint-driven treatment; Nov 2015 administrative path treated STRs as home occupations with business license + 8% lodger’s tax (first license issued ~2015-11-06). Not treated as the binding primary STR ordinance. |
| First City STR code | Ord. 2016-64 (2016-12-05) created §26-219 licensing/advertising rules; proposed 75% host-occupancy / whole-home ban was dropped. |
| Municipal platform tax | Ord. 2020-19 (effective **2020-08-01**) requires marketplace facilitators to collect City sales tax and lodger’s tax. |
| Primary residence / day cap | Ord. 2021-63 (2021-11-22): primary residence required; whole-home STRs ≤180 days/365; one booking at a time; nuisance mitigation. |
| Platform liability | Ord. 2024-41 (2024-09-09): unlawful for platforms to take payment for unlicensed or non-primary STRs; $1,000/day civil penalty. |
| Airbnb tax date | **2020-08-01** — Ord. 2020-19 lodger’s-tax marketplace duty; Airbnb help confirms current 8% Lodger’s Tax remittance. |
| Airbnb data sharing | **null** — no API/City Portal feed documented; 2016 reporting said Airbnb would not share enforcement data. |

## Legislative history recorded

1. **Ord. 2016-64 (Ch. 26 STR unlawful acts)** — City of Aurora — 2016-12-05 — `primary_framework`: true  
2. **HB19-1240 (state marketplace facilitators)** — State of Colorado — 2019-05-23 / 2019-10-01 — `primary_framework`: false  
3. **Ord. 2020-19 (marketplace / lodger’s tax)** — City of Aurora — 2020-06-22 / 2020-08-01 — `primary_framework`: false  
4. **Ord. 2021-63 (definitions, primary residence, 180-day cap)** — City of Aurora — 2021-11-22 — `primary_framework`: true  
5. **Ord. 2024-41 (platform liability)** — City of Aurora — 2024-09-09 — `primary_framework`: false  

Non-binding / excluded: 2015 administrative home-occupation recognition and committee study sessions; proposed 75% occupancy ban that was not enacted; HOA private restrictions.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Aurora, CO entry)
- Script: `agent/scripts/update_aurora_str_regulations.py`
- Report: `agent/reports/2026-08-08-aurora-str-legislative-history.md`
