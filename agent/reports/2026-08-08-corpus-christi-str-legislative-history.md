# Corpus Christi, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Corpus Christi, TX (first unchecked city). Binding STR land-use control began with UDC Ord. 029048 (2011) banning sub-month rentals in single-family districts; dedicated permitting arrived with Ord. 032642 (2022-01-11) and the current Type 1/Type 2 framework in Ord. 032801 (2022-06-28, effective 2022-07-11), later adjusted by consolidated-permit Ord. 033077 (2023-06-27). Airbnb began collecting the City’s 9% HOT on 2019-11-01 under a Council-authorized VCA; no listing-level Airbnb data-sharing connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Corpus Christi, TX (index 61).
- Compiled binding City/State actions from 2008 onward from City STR pages and signed ordinance PDFs, Legistar files 21-1663 / 22-1091 / 23-0838 / 19-1373, UDC adoption materials, Texas H.B. 1905, Airbnb’s Texas occupancy-tax help page, and contemporaneous reporting (KRIS, KIIITV, Caller-Times, South Texas Community News).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-permit zoning | UDC Ord. 029048 (passed 2011-05-10; effective 2011-07-01) § 5.2.24 barred SF rentals under one month citywide (later narrowed to Padre/Mustang Island ADP by Ord. 032801). |
| State HOT | H.B. 1905 (effective 2015-09-01) confirmed STRs are hotels for HOT. |
| First permit law | Ord. 032642 (2022-01-11): annual STR permit; phased effective 2022-03-15 (Padre/Flour Bluff) then ~180 days for rest of City. |
| Current framework | Ord. 032801 (2022-06-28; effective 2022-07-11): Type 1/Type 2, 15% Type 2 block-face cap, SF allowed except Padre/Mustang Island ADP, $250 fee after 2022, local-contact/nuisance rules. |
| 2023 adjustment | Ord. 033077 (2023-06-27; pub. 2023-07-03): consolidated permit for large multifamily buildings with a sole operator. |
| Airbnb tax | Municipal platform collection: **2019-11-01** (Council VCA motion 2019-10-15; HomeAway VCA states Nov 1, 2019; Airbnb listed for City 9% HOT). |
| Airbnb data sharing | **null** — aggregate HOT remittances only; City scrapes ads / uses MuniRevs, not an Airbnb compliance feed. |

## Legislative history recorded

1. **Ordinance No. 029048 (UDC § 5.2.24)** — City of Corpus Christi — 2011-05-10 / 2011-07-01 — `primary_framework`: true  
2. **H.B. 1905** — State of Texas — 2015-06-20 / 2015-09-01 — `primary_framework`: false  
3. **Ordinance No. 032642** — City of Corpus Christi — 2022-01-11 / 2022-03-15 — `primary_framework`: true  
4. **Ordinance No. 032801** — City of Corpus Christi — 2022-06-28 / 2022-07-11 — `primary_framework`: true  
5. **Ordinance No. 033077** — City of Corpus Christi — 2023-06-27 / 2023-07-03 — `primary_framework`: false  

Non-binding / excluded: 2018 CVB STR briefing (no action); Council Motion M2019-172 authorizing Airbnb/HomeAway VCAs (contract authorization, not an STR regulatory ordinance; used only for tax-date evidence); individual PUD rezonings for specific Island properties.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Corpus Christi entry)
- Script: `agent/scripts/update_corpus_christi_str_regulations.py`
- Report: `agent/reports/2026-08-08-corpus-christi-str-legislative-history.md`
