# Indianapolis, IN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Indianapolis, IN (first unchecked city). Indiana’s 2018 HEA 1035 still caps local STR power; Indianapolis’s first city framework is the 2024 Chapter 852 permit/registry (mandatory 2025-01-01). Airbnb has collected Marion County Innkeeper’s Tax since 2019-07-01 under state marketplace-facilitator rules; no direct Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Indianapolis, IN (index 15).
- Compiled binding city and state STR-related legislation from 2008 onward from Indiana General Assembly enrolled acts, Indianapolis–Marion County Code (Municode Ch. 852), Indiana DOR CIT guidance, Airbnb help article 2596, and reputable news (WRTV, WIBC, IndyStar/Avalara).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2018 local rules | Indianapolis deferred STR-specific regulation (IBJ 2016); no grandfathered pre-2018 STR ordinance. |
| State preemption | HEA 1035 / IC 36-1-24 (signed 2018-03-14, effective 2018-07-01) protects primary-residence STRs, bars local bans, and caps permit fees at $150 with free renewals. |
| Platform tax collection | HEA 1001 marketplace-facilitator rules (signed 2019-04-29, effective 2019-07-01) require Airbnb to collect sales tax and County Innkeeper’s Tax, including Marion County’s 10% CIT. |
| City framework | G.O. 25, 2024 / Proposal 205 (passed 2024-08-12; mandatory/enforced 2025-01-01) creates annual STR permits via DBNS under Ch. 852. |
| Airbnb tax | Local CIT collection date **2019-07-01** (DOR + Airbnb Indiana help article). |
| Airbnb data sharing | **null** — IndyStar reports Airbnb declined a listing-data request; city exploring scraping; Ch. 852 has no platform duties. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Indianapolis entry)
- Report: `agent/reports/2026-08-08-indianapolis-str-legislative-history.md`
