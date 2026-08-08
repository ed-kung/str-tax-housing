# Laredo, TX — short-term rental legislative history

**Summary:** Documented Laredo’s STR regulatory timeline from 2008 onward and updated `str_regulations.json` (index 86). Laredo has no dedicated short-term-rental ordinance. Binding controls are the Land Development Code land-use charts (Ord. 93-O-228 / § 24-63.2; chart date 1993-11-22) that prohibit Hotel/Motel in residential districts and allow Bed and Breakfast only in R-O among residential zones (with Appendix A owner-occupancy, six-room, guest-register, and HOT-proof requirements), plus Texas H.B. 1905 (2015) clarifying that STRs are “hotels” for state/local HOT. City Finance materials report a 14% combined HOT stack (7% City + 1% Webb County + 6% State). Airbnb collects only Texas state HOT for Laredo listings; no municipal platform tax agreement or direct Airbnb–City data connection was identified.

## City processed

- **City:** Laredo, TX
- **JSON index:** 86
- **`agent_checked`:** 1

## Legislative history (binding actions)

| Date | Instrument | Role |
| --- | --- | --- |
| 1993-11-22 | Ord. 93-O-228 / LDC § 24-63.2 Land Use Charts + Appendix A B&B/Hotel definitions | Primary land-use framework for transient lodging (still operative) |
| 2015-06-20 / eff. 2015-09-01 | H.B. 1905 (Tax Code § 156.001) | Statewide STR-as-hotel clarification for HOT |

Primary local framework: **Ord. 93-O-228 / § 24-63.2 + Appendix A** (`primary_framework: true`). No post-2008 city ordinance creating an STR registry, night cap, or platform duties was found.

## Airbnb tax / data sharing

- **`airbnb_tax_collection_date`:** `null` — Airbnb’s Texas occupancy-tax help page does not list Laredo among cities where Airbnb remits municipal HOT; Comptroller materials confirm Airbnb’s May 1, 2017 Texas collection covers the 6% state HOT, with hosts responsible for local HOT.
- **`airbnb_data_sharing_date`:** `null` — No City Portal / API / compliance feed identified; no dedicated STR registration program that would typically pair with platform data sharing.

## Sources (selected)

- City of Laredo Land Development Code § 24-63.2 Land Use Charts (Hotel/Motel and Bed and Breakfast rows; Ord. 93-O-228 chart date) and Appendix A definitions (Zoneomics / City LDC materials)
- City of Laredo Finance — Current Tax Rates (7% City / 1% Webb County / 6% State HOT)
- City of Laredo Tax Assessor/Collector — Hotel/Motel reporting resources
- Texas H.B. 1905 (Acts 2015, 84th Leg., R.S., ch. 1255, § 22(a)); Tax Code § 156.001
- Airbnb Help: Occupancy tax collection and remittance by Airbnb in Texas
- Texas Comptroller Airbnb HOT FAQ / 2017 press coverage (state HOT collection from 2017-05-01)

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Laredo entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_laredo.bak`
- Script: `agent/scripts/update_laredo_str_regulations.py`
