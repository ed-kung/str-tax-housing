# Bakersfield, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Bakersfield, CA (first unchecked city). Until 2026, the city treated Airbnb/Vrbo-style short-term rentals as an unpermitted use (~500 listings operating anyway). The City Council’s first STR ordinance (adopted **2026-06-10**, effective ~**2026-07-10**) creates annual permitting, nuisance/operating rules, multifamily unit caps, and platform remittance of the city’s existing 12% Transient Lodging Tax. Full permit-program enforcement is not yet active (city awaiting a third-party administrator; late-2026 target), so `enforcement_date` is null. Airbnb municipal tax collection and data-sharing dates are **null**—Airbnb’s official California TOT help article does not list Bakersfield, and no City Portal / SB 346 implementing feed was found.

## What was done

- Identified first list item lacking `agent_checked`: Bakersfield, CA (index 46).
- Reviewed KGET coverage (Planning Commission / first reading / adoption), Bakersfield Californian adoption reporting (published 2026-06-11), City Council June 10, 2026 meeting video, Housing & Community Development Committee October 2025 direction to draft an ordinance, Airbnb California occupancy-tax help article (2297), California SB 346 (enabling only), and secondary hosting guides (BNBCalc, Host Report).
- Excluded non-binding Housing Element Action 6.8, October 2025 committee direction, Kern County unincorporated TOT, and SB 346 (no local activating ordinance identified).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (1 entry), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2026 status | City officials: STRs not allowed under then-current law; ~500 listings operated without city permits/TOT. |
| Primary city STR code | First STR ordinance — Passage 2026-06-10; effective ~2026-07-10; `primary_framework`: true. Annual permit + business tax certificate; 2 guests/bedroom (kids ≤12 excluded); 24/7 contact (1-hour response); $500k liability insurance; pool/spa curfew 10 p.m.–7 a.m.; ~20% multifamily unit cap; posted notices; TOT via platforms. |
| City tax | Existing 12% Transient Lodging Tax (BMC Ch. 3.40, since 1993) extended to STRs; first reading amended to have platforms collect/remit. |
| Airbnb tax | **null** — Ordinance directs platform collection, but Airbnb help article 2297 does not list Bakersfield; no VCA start date found. |
| Airbnb data sharing | **null** — No City Portal / registry API / SB 346 local invocation found. |
| Enforcement | Technically effective ~2026-07-10; full enforcement delayed to late 2026 per city spokesperson Joe Conroy → `enforcement_date` null. |

## Legislative history recorded

1. **Short-Term Rental Ordinance (first STR permit framework)** — City of Bakersfield — Passage 2026-06-10; effective 2026-07-10; enforcement null — `primary_framework`: true

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Bakersfield entry)
- Report: `agent/reports/2026-08-08-bakersfield-str-legislative-history.md`
