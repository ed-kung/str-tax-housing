# Lincoln, NE short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Lincoln, NE (first unchecked city). Binding city STR framework is the June 14, 2021 package—Ordinances **21073** (zoning), **21074** (4% Hotel Occupation Tax extended to STRs), and **21075** (LMC Ch. 5.39 licensing)—with **Ord. 21104** (2021-08-16) moving the license operative date to **2021-09-20**; host enforcement grace ended **2021-11-29**, and STR occupation-tax remittance began **2021-11-01**. State **LB 57** (eff. 2019-09-06) bars local STR bans; **LB 284** (eff. 2019-04-01) requires marketplace sales/lodging tax collection. Airbnb began collecting Lincoln’s municipal local option sales tax (with state sales/county lodging) in **September 2019**; it does **not** collect Lincoln’s 4% occupation tax. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Lincoln, NE (index 70).
- Compiled binding City/State actions from 2008 onward from City STR pages, signed Ordinances 21073/21074/21075, LMC Ch. 5.39 / Title 27 citations (incl. Ord. 21104), City Treasurer occupation-tax FAQs, Nebraska slip laws LB 57 / LB 284, DOR GIL 1-19-1, and Airbnb Nebraska occupancy-tax materials.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2021 | No dedicated STR license; informal home-occupation treatment (host presence / limited floor area). |
| State preemption | LB 57 (§ 18-1758) bars municipal STR bans; allows health/safety regulation and occupation taxes. |
| Marketplace taxes | LB 284 requires MMP collection of state/local sales and state/county lodging taxes (not city occupation tax). |
| City primary framework | Ord. 21073 (zoning conditional use) + Ord. 21075 (annual $250 license, occupancy/nuisance rules); operative **2021-09-20**. |
| City STR tax | Ord. 21074 extends 4% Hotel Occupation Tax to STRs; Treasurer FAQ effective **2021-11-01**; hosts remit via Host Compliance. |
| Date delay | Ord. 21104 (2021-08-16) changed license start from Aug 1 to Sept 20, 2021. |
| Airbnb tax | Municipal local sales tax collection: **2019-09-01**; 4% occupation tax **not** collected by Airbnb. |
| Airbnb data sharing | **null** — Host Compliance scraping/portal only; no Airbnb City Portal/API. |

## Legislative history recorded

1. **LB 57 / § 18-1758** — State of Nebraska — 2019-03-07 / 2019-09-06 — `primary_framework`: false  
2. **LB 284 (marketplace facilitators)** — State of Nebraska — 2019-03-21 / 2019-04-01 — `primary_framework`: false  
3. **Ordinance No. 21073 (zoning)** — City of Lincoln — 2021-06-14 / 2021-09-20 — `primary_framework`: true  
4. **Ordinance No. 21074 (occupation tax)** — City of Lincoln — 2021-06-14 / 2021-11-01 — `primary_framework`: false  
5. **Ordinance No. 21075 (Ch. 5.39 licensing)** — City of Lincoln — 2021-06-14 / 2021-09-20 — `primary_framework`: true  
6. **Ordinance No. 21104 (operative-date delay)** — City of Lincoln — 2021-08-16 / 2021-09-20 — `primary_framework`: false  

Non-binding / excluded: Planning staff reports and dropped draft primary-residence / 600-ft spacing proposals; Ord. 21786 (2025) definitional cleanup without material STR policy change; Lancaster County zoning for areas outside Lincoln’s 3-mile ETJ.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Lincoln entry)
- Script: `agent/scripts/update_lincoln_str_regulations.py`
- Report: `agent/reports/2026-08-08-lincoln-str-legislative-history.md`
