# Dallas, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Dallas, TX (first unchecked city). Dallas had no dedicated STR land-use/licensing framework until companion Ordinances 32482 (zoning ban in single-family districts) and 32473 (Chapter 42B registration/platform rules) on 2023-06-14; both were enjoined on 2023-12-06 before active enforcement and remain blocked. Earlier binding actions were Texas H.B. 1905 (2015 HOT definition), Ord. 32058 (2021 Chapter 27 defense for HOT-paying STRs), and Ord. 32363 (2023 local HOT increase to 9%). Airbnb collects Texas state HOT but not Dallas municipal HOT; no operational Airbnb–city data connection was identified.

## What was done

- Identified first list item lacking `agent_checked`: Dallas, TX (index 8).
- Compiled binding City/State actions from 2008 onward using AmLegal ordinance PDFs, Dallas Legistar, City Controller HOT pages, Fifth Court of Appeals / trial-court materials, and reputable reporting (Dallas Morning News, Avalara).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2023 regime | STRs treated as hotels for HOT via H.B. 1905; City HOT registration/remittance (host-side) with expanded portal activity by ~Oct 2019; Ord. 32058 (2021) exempted HOT-paying STRs from Chapter 27 long-term rental registration prosecution. No zoning definition of STR lodging before 2023. |
| Primary STR framework (enjoined) | Ord. 32482 + 32473 (passed 2023-06-14; published/effective 2023-06-17; enforcement deferred ~6 months to ~2023-12-14). Ban in single-family zones; Chapter 42B annual $404 registration, occupancy/noise/density rules, platform reporting/booking limits. |
| Enforcement status | Temporary injunction 2023-12-06 blocked both ordinances before active enforcement; appellate affirmances followed; City continues enforcing pre-existing HOT, property standards, noise, and nuisance rules only. |
| Local HOT rate | Ord. 32363 raised City HOT from 7% to 9% effective 2023-01-01 (venue 2% add-on), expressly applying to STR stays. |
| Airbnb tax | **null** — no municipal collection agreement; platforms collect state 6% HOT only (May 1, 2017 statewide). |
| Airbnb data sharing | **null** — Chapter 42B platform monthly reports never went live due to injunction; no earlier direct data connection found. |

## Legislative history recorded

1. **H.B. 1905** — State of Texas — Passage 2015-06-20; effective/enforced 2015-09-01 — `primary_framework`: false  
2. **Ordinance No. 32058** — City of Dallas — Passage 2021-12-08; effective/enforced 2021-12-11 — `primary_framework`: false  
3. **Ordinance No. 32363** — City of Dallas — Passage 2022-12-14; effective/enforced 2023-01-01 — `primary_framework`: false  
4. **Ordinance No. 32482** — City of Dallas — Passage 2023-06-14; effective 2023-06-17; enforcement **null** (enjoined) — `primary_framework`: true  
5. **Ordinance No. 32473** — City of Dallas — Passage 2023-06-14; effective 2023-06-17; enforcement **null** (enjoined) — `primary_framework`: true  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Dallas entry)
- Report: `agent/reports/2026-08-08-dallas-str-legislative-history.md`
