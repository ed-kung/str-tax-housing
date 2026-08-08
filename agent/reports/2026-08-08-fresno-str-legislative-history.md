# Fresno, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Fresno, CA (first unchecked city). Fresno’s primary STR framework is Bill B-32 (adopted Sept. 26, 2019; effective Oct. 27, 2019), adding FMC §7-1249 annual STR permitting, nuisance/contact/recordkeeping rules, and TOT remittance. Bill B-11 (adopted April 27, 2023) expanded the TOT “Operator” definition to include crowdsourcing platforms. Airbnb began collecting Fresno municipal TOT under a VCA on **2024-04-01**; no Airbnb–city listing/compliance data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Fresno, CA (index 33).
- Reviewed Fresno Legistar files ID19-11148 / ID19-11318 (STR permit), ID 23-614 / ID 23-649 (TOT operator amendment), ID 24-335 (Airbnb VCA), City Finance STR/TOT web pages, Airbnb Fresno hosting and California occupancy-tax help articles, and local reporting (Fresno Bee, GV Wire, The Business Journal, SJV Sun).
- Excluded Fresno County’s unincorporated-area STR ordinance and Bill B-27 (2024 squatter-removal remedy for STRs/hotels) as not core city regulation of Airbnb-style STR operations.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (2 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary city STR code | FMC §7-1249 (Bill B-32, 2019): annual owner-held STR permit; whole- or partial-unit stays ≤30 days; TOT remittance; 24/7 contact; nuisance prevention; 3-year records; permit number on ads; bar on nonresidential structures (vehicles, sheds, tents, etc.). No primary-residence, host-presence, or annual day-cap rules. |
| Platform tax duty | Bill B-11 (2023) treats managing agents / crowdsourcing platforms as TOT “Operators.” Actual Airbnb remittance required a separate VCA. |
| City tax | 12% Transient Occupancy Tax (+ 2% TBID per City/Airbnb guidance). City staff reported STR TOT collection commencing 2020-01-01; first STR TOT account May 2020. |
| Airbnb tax | **2024-04-01** — VCA approved 2024-03-07; agreement effective date and collection start April 1, 2024 for municipal TOT. |
| Airbnb data sharing | **null** — VCA is aggregate tax remittance (+ limited optional Registered Host docs); no registry API / listing gate / enforcement feed. |

## Legislative history recorded

1. **Bill B-32 (FMC §7-1249)** — City of Fresno — Passage 2019-09-26; effective/enforced 2019-10-27 — `primary_framework`: true  
2. **Bill B-11 (FMC §7-602 Operator amendment)** — City of Fresno — Passage 2023-04-27; effective/enforced 2023-05-28 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Fresno entry)
- Report: `agent/reports/2026-08-08-fresno-str-legislative-history.md`
