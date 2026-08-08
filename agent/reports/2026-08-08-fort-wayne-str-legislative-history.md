# Fort Wayne, IN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Fort Wayne, IN (first unchecked city). Fort Wayne has no city STR permit/registry ordinance; Indiana’s 2018 HEA 1035 (IC 36-1-24) is the primary framework, reinforced by 2026 HEA 1210’s rental-cap preemption. Airbnb has collected Allen County Innkeeper’s Tax since 2019-07-01 under state marketplace-facilitator rules (rate raised to 8% effective 2019-11-01). No direct Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Fort Wayne, IN (index 82).
- Compiled binding state and county STR-related legislation from 2008 onward from Indiana General Assembly enrolled acts (HEA 1035, HEA 1001, HEA 1402, HEA 1210), Indiana DOR CIT guidance, Airbnb help article 2596, Allen County / Visit Fort Wayne reporting, and local news (Journal Gazette, WANE, WOWO).
- Confirmed absence of a Fort Wayne Common Council STR-specific ordinance (zoning treats traditional bed-and-breakfast as a special use; general housing registration is not an STR framework).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| City STR ordinance | None adopted; Fort Wayne relies on state preemption plus generally applicable codes. |
| State preemption | HEA 1035 / IC 36-1-24 (signed 2018-03-14, effective 2018-07-01) protects primary-residence STRs and caps local permit design; primary framework for Fort Wayne. |
| Platform tax collection | HEA 1001 marketplace-facilitator rules (signed 2019-04-29, effective 2019-07-01) require Airbnb to collect sales tax and Allen County CIT. |
| County lodging tax | HEA 1402 (signed 2019-05-06) authorized, and Allen County Council adopted, raising CIT from 7% to 8% (DOR effective 2019-11-01). No separate Fort Wayne city lodging tax. |
| Further preemption | HEA 1210 (signed 2026-03-12, effective 2026-07-01) bans local rental caps/restrictions on residential rental use; little displacement effect in Fort Wayne (no prior cap). |
| Airbnb tax | Local CIT collection date **2019-07-01** (DOR + Airbnb Indiana help article). |
| Airbnb data sharing | **null** — no City Portal, compliance API, or platform reporting arrangement identified. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Fort Wayne entry)
- Report: `agent/reports/2026-08-08-fort-wayne-str-legislative-history.md`
