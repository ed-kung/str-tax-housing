# Huntsville, AL short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Huntsville, AL (last unchecked city). Huntsville has no dedicated STR permit ordinance; Airbnb-style rentals are regulated as hotel/motel/tourist-home lodging under zoning plus a 2018 business-license schedule amendment (Ord. 18-243, primary framework), city lodging tax (Ord. 12-365 / 17-456 / 26-484), and 2024 zoning definition clarifications (Ord. 24-289). Alabama Act 2024-334 adds platform collection/reporting duties statewide. Airbnb municipal tax collection and city data-sharing dates are both null.

## What was done

- Identified first list item lacking `agent_checked`: Huntsville, AL (index 99).
- Compiled binding city and state STR-relevant legislation from 2008 onward from City of Huntsville code/pages and blog, Municode, ALDOR notices, Alabama SB150/Act 2024-334, Speakin' Out News legal notices, and local reporting (al.com, WAFF, WHNT, Axios).
- Confirmed absence of a dedicated STR registry ordinance; STRs are treated as motels/tourist homes for zoning (R-2B and commercial/industrial lodging districts).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| City STR ordinance | No dedicated STR chapter; Ord. **18-243** (2018-04-26) created the lodging business-license category for STRs — **primary framework**. |
| Zoning | Pre-existing R-2B/commercial hotel-motel-tourist-home permissions; Ord. **24-289** (2024-05-23; effective on publication 2024-05-29) defines Transient/Residence to reinforce residential-district limits. |
| Lodging tax | Ord. **12-365** (2012) modern rewrite; Ord. **17-456** raised rate to 9% + $2 (effective 2017-10-01); Ord. **26-484** adds 1% (to 10%) effective 2026-10-01 for VBC expansion. |
| State platform law | Act **2024-334** (signed 2024-05-09): intermediary collection of state + parallel local levies for transactions on/after 2025-01-01; annual address reports to ALDOR. |
| Airbnb tax | **null** — Airbnb Alabama help article lists other cities’ municipal lodging taxes but not Huntsville; city directs hosts to remit via OneSpot. |
| Airbnb data sharing | **null** — no City Portal / compliance API / city data feed identified. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Huntsville entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_huntsville.bak`
- Script: `agent/scripts/update_huntsville_str_regulations.py`
- Report: `agent/reports/2026-08-08-huntsville-str-legislative-history.md`
