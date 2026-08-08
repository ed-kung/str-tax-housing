# Charlotte, NC short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Charlotte, NC (first unchecked city). Charlotte has never enacted a dedicated short-term rental (STR) ordinance; proposed UDO registration/400-foot separation rules were withdrawn in April 2022 after *Schroeder v. City of Wilmington*. Binding law is state preemption of local rental registration/permits (S.L. 2011-281 → 2016-122 → 2019-73 → Chapter 160D-1207). Airbnb began collecting Mecklenburg County room occupancy tax for Charlotte stays on **2015-06-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Charlotte, NC (index 14).
- Compiled binding state actions relevant to Charlotte STR regulation from North Carolina session laws, UNC School of Government guidance, the *Schroeder* opinion, Charlotte Observer / WFAE / Axios coverage of the UDO, Airbnb Charlotte tax help materials, and May 2015 News & Observer / Mountain Xpress reporting on the NC voluntary collection agreement.
- Confirmed that Charlotte’s adopted UDO (passed 2022-08-22, effective 2023-06-01) contains no short-term-rental use, permit, or registry (proposed STR language was removed before adoption).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| City STR code | None enacted. Draft UDO would have required zoning permits and 400-ft separation for whole-dwelling STRs; City Attorney advised removal after *Schroeder* (Apr 2022). |
| State preemption | S.L. 2011-281 barred general local renting permits; S.L. 2016-122 (eff. 2017-01-01) expressly barred rental registration; S.L. 2019-73 applied those limits to Vacation Rental Act properties; Chapter 160D-1207(c) (eff. 2020-06-19 via S.L. 2020-25) is the current codification. |
| *Schroeder* | N.C. Court of Appeals (2022-04-05) struck Wilmington STR registration and inseverable linked rules under 160D-1207(c); affirmed cities may still use general zoning/police-power tools Charlotte has not adopted for STRs. |
| Local lodging tax | Mecklenburg County 8% room occupancy tax applies to private-home accommodations under 90 days; Charlotte has no separate city occupancy tax on top of the county levy. |
| Airbnb tax | **2015-06-01** — Airbnb VCA began collecting Mecklenburg occupancy tax (+ NC sales tax) for Charlotte bookings. |
| Airbnb data sharing | **null** — lump-sum remittance under VCA; no city portal/API/delisting channel. |

## Legislative history recorded

1. **S.L. 2011-281 (SB 683)** — State of North Carolina — Passage/effective/enforced 2011-06-23 — `primary_framework`: true  
2. **S.L. 2016-122 (SB 326)** — State of North Carolina — Passage 2016-07-28; effective/enforced 2017-01-01 — `primary_framework`: true  
3. **S.L. 2019-73 (SB 483)** — State of North Carolina — Passage/effective/enforced 2019-07-01 — `primary_framework`: false  
4. **S.L. 2019-111 (SB 355) / S.L. 2020-25 (SB 720)** — State of North Carolina — Passage 2019-07-11; effective/enforced 2020-06-19 — `primary_framework`: true  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Charlotte entry)
- Report: `agent/reports/2026-08-08-charlotte-str-legislative-history.md`
