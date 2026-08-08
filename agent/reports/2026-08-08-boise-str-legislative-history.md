# Boise STR legislative history

Updated `str_regulations.json` for Boise, ID (first unchecked city). Boise’s primary city STR framework was Ordinance 7-22 (adopted 2022-03-15, effective 2022-05-01), creating an annual licensing program with safety, quiet-hour, insurance, and local-representative rules. Idaho HB 583 (signed 2026-03-16, effective 2026-07-01) preempted local STR licensing; Boise repealed Chapter 22 via ORD-14-26 (effective 2026-05-18). No City of Boise municipal lodging tax exists (Airbnb collects state and GBAD taxes only). No Airbnb–City data-sharing connection was found.

## Findings

- **State framework (HB 216 / 2017):** Short-term Rental and Vacation Rental Act (Ch. 239; eff. 2018-01-01) barred local STR bans, required residential zoning treatment, prohibited regulating marketplaces, and required marketplace tax collection/remittance through the State Tax Commission.
- **HB 452 (2018):** Clarified § 67-6539 so cities/counties cannot prohibit STRs in parts of a jurisdiction (not only citywide); effective 2018-07-01.
- **Ordinance 7-22 (2022):** City primary framework—annual STR license ($80), insurance, quiet hours, safety equipment, trash, license display, local representative; no whole-home ban, day caps, or host-presence/primary-residence rules. Enforced from 2022-05-01 until repeal.
- **HB 583 / ORD-14-26 (2026):** State law bans local STR licenses/fees/permits and most STR-only restrictions; Boise repealed Title 3, Chapter 22 effective 2026-05-18. City continues generally applicable nuisance/noise/parking enforcement.
- **Airbnb tax collection:** `null` for municipal tax. Airbnb agreement with Idaho Tax Commission began **2016-12-01** for state sales, travel-and-convention, and GBAD auditorium-district taxes; City of Boise itself levies no lodging/occupancy tax.
- **Airbnb data sharing:** `null`. State law bars local marketplace regulation; no City Portal or enforcement data feed identified.

## Sources

- Idaho Legislature: HB 216 (2017 Ch. 239); HB 452 (2018 Ch. 79); HB 583 (2026 Ch. 22) bill texts and status pages
- Boise City Code Title 3, Chapter 22 (AmLegal; Ord. 7-22); City of Boise short-term rental license page; ORD-14-26 publication notice (Idaho Statesman / McClatchy legals)
- Idaho Statesman / Idaho News / Idaho Press coverage of Ord. 7-22 and HB 506/583 debates
- Idaho State Tax Commission lodging/marketplace guidance; Airbnb help article 2302; contemporaneous reporting on Dec. 1, 2016 Airbnb–Idaho tax agreement

## Artifacts

- `AGENT_DATA_PATH/str_regulations.json` (Boise entry, index 94)
- `agent/scripts/update_boise_str_regulations.py`
