# Oklahoma City, OK short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Oklahoma City, OK (first unchecked city). OKC’s primary STR framework is the January 15, 2019 home-sharing package (Ords. 26,081 / 26,082), effective/enforced 2019-02-14. Major 2024–2025 updates add a temporary density moratorium, a voter-approved hotel-tax hike to 9.25%, and permanent occupancy/night/density rules (Ords. 27,742 / 27,743, effective 2025-02-16). Airbnb has collected OKC municipal Hotel Tax since **2017-09-01**; no direct Airbnb–city listing/data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Oklahoma City, OK (index 19).
- Compiled binding city STR-related legislation from 2008 onward from City of OKC press releases and Home Sharing License page, Municode ordinances (26,081; 26,082; 27,605; 27,610; 27,742; 27,743), Oklahoma County election materials, Airbnb help articles 2323/2528, and reputable news (AP/KJRH/News9, The Oklahoman, KOSU, KOCO, OKCMAR, OK Gazette).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (8 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2019 | Zoning did not clearly allow residential STRs; informal hotel-tax / license expectations existed with little structure (OK Gazette). |
| Primary framework | Ords. 26,081 (zoning) + 26,082 (Chapter 13 licensing), passed 2019-01-15, effective/enforced 2019-02-14: annual license, safety equipment, 30-day stay cap, special exceptions for non-primary and HP districts (HP also requires host on site), grandfathering for pre-1/15/2019 operators. |
| License fees | Ord. 27,605 (passed 2024-05-21; effective 2024-07-01) raised annual license from $24 to $100.80 (with further scheduled increases). June 17, 2025 fee action raised BOA special-exception filing fee from $300 to $1,100. |
| Density pause | Emergency 180-day moratorium (2024-07-16) blocked new special exceptions that would exceed ~10%/block density pending permanent rules. |
| Hotel tax | Ord. 27,610 voter-approved 2024-08-27; rate 5.5%→9.25% effective 2024-10-01; applies to hotels and home shares. |
| 2025 rules | Ords. 27,742 / 27,743 (passed 2024-12-17; effective/enforced 2025-02-16): 16-person occupancy cap, 10 nights/month without special exception, permanent 10% block cap for special-exception STRs, parking (1 per 4 guests), covenant/traffic considerations, stronger denial/revocation tools. |
| State law | No statewide STR preemption found that displaces OKC’s home-rule framework. |
| Airbnb tax | Municipal Hotel Tax collection date **2017-09-01** (AP/city agreement reporting); later rate change reflected in Airbnb help article. |
| Airbnb data sharing | **null** — city uses third-party scraping (Deckard Technologies); no City Portal/API/delist channel with Airbnb. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Oklahoma City entry)
- Report: `agent/reports/2026-08-08-oklahoma-city-str-legislative-history.md`
