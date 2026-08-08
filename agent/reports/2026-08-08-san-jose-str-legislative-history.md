# San Jose, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for San Jose, CA (first unchecked city). Ordinance 29523 (Dec. 16, 2014; effective Jan. 16, 2015) remains the primary STR framework (hosted/unhosted rules, 180-day unhosted cap, TOT, business tax). Later ADU packages (Ord. 30353/urgency Dec. 2019; Ord. 30480 Sept. 2020) barred STRs in ADUs and cleaned up definitions. Airbnb began collecting municipal TOT on **2015-02-01**; no documented Airbnb–City listing/compliance data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: San Jose, CA (index 12).
- Compiled binding City ordinances from 2008 onward from San Jose Municipal Code / Legistar materials, City ADU ordinance archive, comparative city staff reports, Airbnb hosting guidance, and reputable secondary sources (Mercury News/East Bay Times; STR-facts VCA compilation).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | **Ord. 29523** (final council action 2014-12-16; effective/enforced 2015-01-16) legalized Incidental Transient Occupancy under SJMC Ch. 20.80 Part 2.5 with 180-day unhosted cap, occupancy/local-contact/recordkeeping rules, business tax certificate, and 10% TOT. |
| ADU STR ban | **Ord. 30353 + urgency** (council 2019-12-17; urgency effective immediately) amended §20.80.160 to prohibit ITO in Accessory Dwelling Units (state ADU alignment). |
| Definition clean-up | **Ord. 30480** (adopted 2020-09-29; effective 2020-10-29) revised §20.80.150 ITO definition for ADU terminology; did not replace 2014 framework. |
| Airbnb tax | Municipal TOT platform collection: **2015-02-01** (San Jose VCA effective date in published Airbnb agreement compilation). |
| Airbnb data sharing | **null** — tax VCA only; no City Portal / API / binding platform listing-data duties identified; no SB 346 local activating ordinance found. |

## Legislative history recorded

1. **Ordinance No. 29523** — City of San Jose  
   - Passage 2014-12-16; effective/enforced 2015-01-16  
   - `primary_framework`: true

2. **Ordinance No. 30353 and companion urgency ordinance** — City of San Jose  
   - Passage/effective/enforced 2019-12-17  
   - `primary_framework`: false

3. **Ordinance No. 30480** — City of San Jose  
   - Passage 2020-09-29; effective/enforced 2020-10-29  
   - `primary_framework`: false

No additional binding City/County/State STR regulatory ordinances specific to regulating Airbnb-style rentals in San Jose were identified between 2008 and research date beyond these (general TOT rate structure predated STRs; California SB 346 requires a local activating ordinance not found for San Jose).

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (San Jose entry)
- Report: `agent/reports/2026-08-08-san-jose-str-legislative-history.md`
