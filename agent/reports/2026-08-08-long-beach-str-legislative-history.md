# Long Beach, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Long Beach, CA (first unchecked city). Primary STR framework is ORD-20-0024 (June 23, 2020; effective Oct. 24, 2020; inland enforcement after April 22, 2021 registration deadline), expanded by emergency ORD-20-0045 (Dec. 15, 2020) to allow un-hosted/non-primary STRs (800-unit cap), and restated by ORD-22-0011 (March 15, 2022) for Coastal Commission LCPA mods (coastal enforcement Sept. 6, 2022). Measure B raised municipal TOT to 13% (July 1, 2020). Airbnb municipal TOT collection began **2019-04-01**; Airbnb City Portal / registration-number listing gating documented by **2021-06-01**.

## What was done

- Identified first list item lacking `agent_checked`: Long Beach, CA (index 43).
- Reviewed City ordinances ORD-20-0024, ORD-20-0045, ORD-22-0011; Legistar files 20-0453, 20-1203, 22-0248, 20-1127; City press releases on registration launch and coastal enforcement; Measure B materials; Press-Telegram Airbnb TOT coverage; Long Beach Business Journal City Portal / June 1, 2021 platform enforcement article; FY24 Innovation and Efficiency STR notes.
- Excluded Dec. 2018 Council policy direction (non-binding) and California SB 346 (2025 enabling statute; no Long Beach implementing ordinance found as of research date).
- Updated `$AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary city STR code | LBMC Ch. 5.77 via ORD-20-0024 (2020): annual registration; initially hosted primary-residence only; ADU/affordable/SRO bans; platform data/takedown duties; TOT; $1,000 fines. |
| Major expansion | ORD-20-0045 (Dec. 2020 emergency): un-hosted allowed; 800 non-primary cap; 90-day un-hosted cap on primary residences. |
| Coastal | Enforcement deferred until CCC LCPA certification (May 13, 2022) after ORD-22-0011 accepted suggested mods; coastal enforcement start Sept. 6, 2022. |
| Municipal TOT | 12% until Measure B; 13% from July 1, 2020. |
| Airbnb tax | **2019-04-01** — VCA; City staff report File 20-1127 + Press-Telegram. |
| Airbnb data sharing | **2021-06-01** — City Portal in use by May 2021; automatic registration-number listing removal on Airbnb/Vrbo as of June 1, 2021 (LBBJ). |

## Legislative history recorded

1. **Measure B (LBMC §3.64.035 TOT +1%)** — City of Long Beach (voters) — Passage 2020-03-03; effective/enforced 2020-07-01 — `primary_framework`: false  
2. **ORD-20-0024 (Ch. 5.77)** — City of Long Beach — Passage 2020-06-23; effective 2020-10-24; enforced 2021-04-22 (inland) — `primary_framework`: true  
3. **ORD-20-0045 (Ch. 5.77 restatement)** — City of Long Beach — Passage/effective 2020-12-15; enforced 2021-04-22 — `primary_framework`: false  
4. **ORD-22-0011 (Ch. 5.77 coastal LCPA mods)** — City of Long Beach — Passage 2022-03-15; effective 2022-04-15; coastal enforcement 2022-09-06 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Long Beach entry)
- Report: `agent/reports/2026-08-08-long-beach-str-legislative-history.md`
