# Columbus, OH short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Columbus, OH (first unchecked city). Columbus’s STR regime begins with Ordinance 2145-2018 (permits effective 2019-01-01), with tax rules in Ordinance 0362-2019 (5.1% lodging excise tax effective 2019-03-01) and later Chapter 598 amendments through 1959-2021. Airbnb’s official Ohio tax page does not list Columbus for automatic municipal tax collection, and no Airbnb–city data portal/MOU was found.

## What was done

- Identified first list item lacking `agent_checked`: Columbus, OH (index 13).
- Compiled binding city STR legislation from 2008 onward using Columbus Legistar, Municode ordinance listings, city License Section / tax FAQ materials, Airbnb help pages, and contemporary news (WOSU, ABC6, WCBE, WBNS/Dorans).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary city framework | Ord. 2145-2018 (final action 2018-08-03): Chapter 598 STR permits, insurance, emergency contact, platform permit-number / records duties; permit requirement effective **2019-01-01**; penalties **2019-03-01**. No annual night cap in the enacted version. |
| Tax framework | Ord. 0362-2019 (2019-02-06): Chapter 371 amended for STR lodging excise tax; city materials put the **5.1%** STR lodging tax in force **2019-03-01**. |
| Later Chapter 598 changes | Ord. 0352-2019 (clarifications); Ord. 1079-2019 (reorganization, booking-service permit rule, consolidated penalties); Ord. 3221-2019 (mandatory BCI checks for all applicants, 2020); Ord. 1959-2021 (enforcement / denial-suspension-revocation / appeals, emergency 2021-07-15). |
| State law | No enacted Ohio statewide STR preemption or platform-tax mandate found for this period (e.g., HB 563 / later bills did not become law). |
| Airbnb tax | **null** — Airbnb Ohio occupancy-tax article lists Cuyahoga County, Cincinnati, and Cleveland only; not Columbus municipal tax. |
| Airbnb data sharing | **null** — no City Portal / MOU / direct data connection documented. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Columbus, OH entry)
- Report: `agent/reports/2026-08-08-columbus-str-legislative-history.md`
