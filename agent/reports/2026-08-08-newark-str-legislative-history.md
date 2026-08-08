# Newark, NJ — Short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Newark, NJ (first unchecked city). Newark’s primary STR framework is **Ord. 6PSF-B / File 18-1550** (Chapter 18:14, adopted **2019-09-05**): annual $250 Engineering permit, principal-residence-only hosting, inspections, and operating rules. Companion **2019-08-07** ordinances added zoning standards (including a 60-day/year cap), extended the **6% hotel occupancy tax** and **1.5% Tourism Improvement District** fee to transient accommodations. State **P.L. 2018, c. 49** (operative **2018-10-01**) and **P.L. 2019, c. 235** govern marketplace tax collection. Active permit enforcement was announced **2024-09-04** after a **2023-12-20** platform-verification amendment. Airbnb began collecting Newark’s municipal 6% hotel tax under a VCA announced **2016-04-12**; no documented Airbnb–city compliance data connection go-live was found.

## City processed

- **City:** Newark, New Jersey  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 65)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary framework (2019):** Chapter 18:14 (Ord. 6PSF-B, File 18-1550) requires an annual STR permit ($250), Certificate of Code Compliance, owner principal-residence configurations only, insurance, responsible-party contacts, nuisance/parking rules, and up to $2,000/day fines. Zoning File 18-1549 (same package) separately permits STRs as accessory use with a 60-day cumulative annual cap and max five units per host.

2. **Taxes/fees (2019 + state law):** File 18-1590 extended Newark’s 6% hotel occupancy tax to transient accommodations; File 18-1722 added STRs to the Greater Newark TID 1.5% license fee. State P.L. 2018, c. 49 (eff. 2018-10-01) authorized municipal STR hotel taxes and marketplace remittance; P.L. 2019, c. 235 narrowed taxable direct rentals but kept marketplace collection.

3. **Enforcement lag:** nj.com (Jan 2020) reported hosts still awaiting permitting/tax rollout months after adoption. Mayor Baraka announced the city was **now enforcing** the permit ordinance on **2024-09-04** (Patch), after Ord. 6PSF-G (2023-12-20) added booking-service verification/reporting duties. `enforcement_date` for the 2019 regulatory ordinances and 2023 platform amendment is **2024-09-04**.

4. **Additional registration (2023):** Ord. 6PSF-d / File 23-0335 (2023-04-05) requires citywide rental registration / Certificate of Habitability, with STRs on an annual cycle (120-day initial deadline ~2023-08-03).

5. **Airbnb tax collection:** **2016-04-12** — City/Airbnb VCA for municipal 6% hotel tax (NJ.com, AP, Skift). Later ordinances codified transient-accommodation tax coverage.

6. **Airbnb data sharing:** **null** — No primary-source City Portal/API go-live; 2023 ordinance creates platform verification duties, but implementation date for an Airbnb direct connection was not documented.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| P.L. 2018, c. 49 | State of New Jersey | 2018-07-01 | 2018-10-01 | 2018-10-01 | false |
| File 18-1549 (zoning STR standards) | City of Newark | 2019-08-07 | 2019-08-07 | 2024-09-04 | false |
| File 18-1590 (6% hotel/TA tax) | City of Newark | 2019-08-07 | 2019-08-07 | 2019-08-07 | false |
| File 18-1722 (TID 1.5% on STRs) | City of Newark | 2019-08-07 | 2019-08-07 | 2019-08-07 | false |
| P.L. 2019, c. 235 | State of New Jersey | 2019-08-09 | 2019-08-09 | 2019-08-09 | false |
| Ord. 6PSF-B / File 18-1550 (Ch. 18:14) | City of Newark | 2019-09-05 | 2019-09-05 | 2024-09-04 | true |
| Ord. 6PSF-d / File 23-0335 (rental registration) | City of Newark | 2023-04-05 | 2023-04-05 | 2023-08-03 | false |
| Ord. 6PSF-G (platform verification) | City of Newark | 2023-12-20 | 2023-12-20 | 2024-09-04 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Newark entry)
- Script: `agent/scripts/update_newark_str_regulations.py`
- Report: `agent/reports/2026-08-08-newark-str-legislative-history.md`

## Key sources

- Newark Legistar Files 18-1549, 18-1550, 18-1590, 18-1722, 23-0335
- Newark eCode Chapter 18:14 (Ord. 6PSF-B, 9-5-2019; amended Ord. 6PSF-G, 12-20-2023); zoning §41:4-612
- P.L. 2018, c. 49; P.L. 2019, c. 235; NJ Division of Taxation TB-81R / transient accommodations guidance
- NJ.com (2016-04-12 VCA; 2019-08-11 / 2020-01-11 STR ordinances); Patch (2024-09-04 enforcement announcement); Skift (2016 Newark tax agreement)
