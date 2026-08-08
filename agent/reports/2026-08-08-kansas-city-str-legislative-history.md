# Kansas City, MO short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Kansas City, MO (first unchecked city). The city’s first STR framework was Ordinance 170771 (passed 2018-02-22; effective/enforced Aug 2018). The current primary regime is CS Ord. 230268 (passed 2023-05-04; effective 2023-06-15), with companion zoning Ord. 230267 banning new non-resident STRs in R districts. Voters approved a 7.5% Transient Boarding and Accommodation Tax and $3 occupancy fee on 2023-04-04 (implemented Ords. 230364/230363, effective 2023-08-01). Ord. 250965 (2025-11-13) added temporary Major Event registrations for the 2026 World Cup. Airbnb municipal lodging-tax remittance and a city–Airbnb direct data connection were not documented; both Airbnb date fields are null.

## What was done

- Identified first list item lacking `agent_checked`: Kansas City, MO (index 37).
- Reviewed KCMO Legistar/clerk files (Ords. 170771, 230014, 230015, 230267, 230268, 230363, 230364, 250965), City Auditor STR reports, KCMO STR/tax pages, Airbnb Missouri/KC help articles, and KCUR / Ballotpedia / Avalara coverage.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (8 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| First city framework | Ord. 170771 (2018) created Type 1/Type 2 zoning permits under § 88-321; enforcement ~2018-08-08; compliance remained very low. |
| Current framework | CS Ords. 230267/230268 (2023-05-04) moved registration to Neighborhood Services (Ch. 56), required registration before listing, raised penalties, and barred new non-resident STRs in residential zones. |
| Municipal lodging tax/fee | Ballot Questions 2–3 (Apr 4, 2023) authorized 7.5% TBAT + $3/night fee; Ords. 230364/230363 effective **2023-08-01**. |
| World Cup adjustment | CS Ord. 250965 (2025-11-13) created $50 Major Event registrations for designated ≤90-day windows (World Cup: 2026-05-03–2026-07-31). |
| Airbnb tax | **null** — Airbnb MO page collects state/local sales taxes and lists lodging remittance for other MO cities, not KCMO’s TBAT/$3 fee. |
| Airbnb data sharing | **null** — platform must honor public registry / records-on-request rules; no documented API or automated data feed. |

## Legislative history recorded

1. **Ord. 170771 (§ 88-321)** — City of Kansas City, MO — Passage 2018-02-22; effective 2018-08-06; enforced 2018-08-08 — `primary_framework`: true  
2. **Ord. 230014 (Question 3 occupancy fee referral)** — Passage 2023-01-12; voter approval/effective 2023-04-04; enforced 2023-08-01 — `primary_framework`: false  
3. **Ord. 230015 (Question 2 TBAT referral)** — Passage 2023-01-12; voter approval/effective 2023-04-04; enforced 2023-08-01 — `primary_framework`: false  
4. **CS Ord. 230267 (zoning / non-resident R-district ban)** — Passage/effective/enforced 2023-05-04 — `primary_framework`: false  
5. **CS Ord. 230268 (Ch. 56 registration)** — Passage 2023-05-04; effective/enforced 2023-06-15 — `primary_framework`: true  
6. **Ord. 230363 (§ 40-168 $3 fee)** — Passage 2023-05-11; effective/enforced 2023-08-01 — `primary_framework`: false  
7. **Ord. 230364 (§§ 68-585 et seq. 7.5% TBAT)** — Passage 2023-05-11; effective/enforced 2023-08-01 — `primary_framework`: false  
8. **CS Ord. 250965 (Major Event registration)** — Passage/effective/enforced 2025-11-13 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Kansas City, MO entry)
- Report: `agent/reports/2026-08-08-kansas-city-str-legislative-history.md`
