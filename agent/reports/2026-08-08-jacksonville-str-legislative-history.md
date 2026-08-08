# Jacksonville, FL short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Jacksonville, FL (first unchecked city). Jacksonville/Duval never enacted a dedicated STR ordinance (Ord. 2019-238 was withdrawn). Binding regulation is state law: Ch. 2011-119 (vacation rental licensing + broad preemption) and Ch. 2014-71 (current s. 509.032(7)(b) ban on local prohibition or duration/frequency rules, with June 1, 2011 grandfathering). A November 2022 circuit court dismissal (16-2022-CA-3550) rejected the City’s use of generic Chapter 656 hotel/motel definitions against STRs. Airbnb collects Florida state sales tax for Duval hosts but not the 6% local TDT; no Airbnb–city data connection was found. Ch. 2025-190 (SB 180) further freezes more restrictive local land-development rules through October 1, 2027.

## What was done

- Identified first list item lacking `agent_checked`: Jacksonville, FL (index 9).
- Compiled binding state actions and confirmed the absence of enacted city STR legislation using Florida session laws, Duval Tax Collector TDT pages, City Council auditor/TDC materials, WJCT/Florida Politics/News4Jax reporting, Action News Jax coverage of the Willis enforcement case, and Airbnb’s Florida occupancy-tax help article.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| City STR code | None enacted. Special Committee (2018) studied the issue; Ord. 2019-238 (registration/host-presence proposal) withdrawn June 2019. |
| De facto local practice | City treated under-7-day residential stays as hotel/motel uses under generic Ch. 656 definitions; enforcement attempt dismissed Nov 2022 (16-2022-CA-3550) as conflicting with s. 509.032 and not grandfathered. |
| State preemption | Ch. 2011-119 (eff. 2011-06-02); narrowed by Ch. 2014-71 (eff. 2014-07-01) to current text—no local ban or duration/frequency regulation except pre-6/1/2011 ordinances. |
| State licensing | DBPR vacation-rental public lodging license under ch. 509 remains required for qualifying transient dwellings. |
| Local TDT | 6% Duval Convention/TDT applies to transient stays; host self-remits monthly. No platform remittance agreement. |
| SB 180 (2025) | Land-development “more restrictive” freeze through 2027 cited by City counsel as limiting new STR zoning/regs. |
| Airbnb tax | **null** — state sales/surtax only; Duval TDT not collected by Airbnb. |
| Airbnb data sharing | **null** — no operational direct data/compliance connection. |

## Legislative history recorded

1. **Ch. 2011-119 (CS/CS/CS/HB 883)** — State of Florida — Passage/effective/enforced 2011-06-02 — `primary_framework`: true  
2. **Ch. 2014-71 (SB 356)** — State of Florida — Passage 2014-06-13; effective/enforced 2014-07-01 — `primary_framework`: true  
3. **Ch. 2025-190 (CS/CS/SB 180)** — State of Florida — Passage/effective/enforced 2025-06-26 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Jacksonville entry)
- Report: `agent/reports/2026-08-08-jacksonville-str-legislative-history.md`
