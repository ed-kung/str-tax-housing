# San Antonio, TX short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for San Antonio, TX (first unchecked city). San Antonio’s STR regime began with Ordinance 2018-11-01-0858 (Type 1/Type 2 permits and 12.5% Type 2 density caps); a 2022 UDC package (Ord. 2022-11-03-0831, effective 2023-01-01) tightened Type 2 density math via round-down; Ordinance 2024-06-13-0433 added platform delisting and City HOT remittance duties, higher fees, and stronger enforcement. Airbnb began collecting San Antonio municipal HOT on 2025-03-10; the first operational Airbnb–city listing-compliance connection is 2024-06-13.

## What was done

- Identified first list item lacking `agent_checked`: San Antonio, TX (index 6).
- Compiled binding City ordinances from 2008 onward from official ordinance PDFs (docsonline.sanantonio.gov), City Finance/DSD guidance, and reputable news (TPR, KSAT, San Antonio Report / Rivard Report, Community Impact, Express-News).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| First city framework | Ord. 2018-11-01-0858 (passed/effective 2018-11-01; permit-offense enforcement 2019-02-11 after 90-day grace) created Chapter 16 Art. XXII permits and UDC §35-374.01 Type 1/Type 2 zoning with 12.5% Type 2 density caps. |
| Density tightening | Ord. 2022-11-03-0831 (UDC package; effective 2023-01-01) required rounding down Type 2 density calculations (city DSD STR briefings). |
| Platform / HOT overhaul | Ord. 2024-06-13-0433 (effective immediately 2024-06-13 except HOT §16-1104.01 on 2024-09-12) raised fees to $300/$450, mandated platform delisting of unpermitted listings within 10 business days, and required state-HOT-collecting platforms to remit City HOT. |
| Airbnb tax | Municipal City HOT platform collection: **2025-03-10** (City Finance STR page; DSD webinar). Distinct from Airbnb’s May 1, 2017 Texas *state* HOT agreement. |
| Airbnb data sharing | **2024-06-13** — first binding City→platform listing-removal / permit-number requirement under Ord. 2024-06-13-0433. |

## Legislative history recorded

1. **Ordinance 2018-11-01-0858** — City of San Antonio  
   - Passage/effective 2018-11-01; enforcement 2019-02-11  
   - `primary_framework`: true

2. **Ordinance 2022-11-03-0831** — City of San Antonio  
   - Passage 2022-11-03; effective/enforced 2023-01-01  
   - `primary_framework`: false

3. **Ordinance 2024-06-13-0433** — City of San Antonio  
   - Passage/effective/enforced 2024-06-13 (HOT remittance section delayed to 2024-09-12; Airbnb City HOT collection began 2025-03-10)  
   - `primary_framework`: true

No additional binding City/County/State STR regulatory ordinances specific to San Antonio were identified between 2008 and research date beyond these (task-force/consideration requests and the 2017 state tax collection agreement were excluded as non-legislative / state-tax-only).

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (San Antonio entry)
- Report: `agent/reports/2026-08-08-san-antonio-str-legislative-history.md`
