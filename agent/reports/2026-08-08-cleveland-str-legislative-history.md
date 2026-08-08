# Cleveland, OH short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Cleveland, OH (first unchecked city). Cleveland’s STR regime began with **Ordinance No. 30-16** (passed 2016-06-06, eff. 2016-07-01) applying the 3% city transient occupancy tax via booking agents and creating the limited-lodging pathway ahead of the RNC; **Ordinance No. 1444-16** (2017-01-23, eff. 2017-01-26) left §337.251 Limited Lodging as the lasting zoning text (primary residence, &lt;91 days/year, ≤30 consecutive days)—later described by city officials as unenforceable. **Ordinance No. 561-2026** (passed 2026-06-01; STR chapter effective 180 days later on **2026-11-28**) replaces that framework with licensing, a 10% density cap, local-contact rules, and booking-agent registration. Airbnb municipal TOT collection: **2016-07-01**. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Cleveland, OH (index 53).
- Compiled binding city legislation from Cleveland Legistar (Ord. 561-2026 final text/legislative summary), American Legal Codified Ordinances citations for §§193.02/193.121 and 337.251, Ideastream / Cleveland Scene / Avalara / The Hill contemporaneous reporting, Cuyahoga County’s April 2016 Airbnb county-tax press release, and Airbnb Ohio tax help articles.
- Excluded non-binding or unadopted items: Ord. 198-18 (limited-lodging moratorium, tabled), Ord. 462-2020 (amendment to §337.251, tabled), Ohio SB 104 / HB 109 (pending preemption; not enacted).
- Excluded Ord. 586-16 (last prior amendment to §337.02 One-Family Districts) because the surviving text does not establish STR rules; 561-2026 merely uses it as the prior amendment citation when adding STRs as a permitted use.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Initial framework (2016) | Ord. 30-16: Chapter 193 booking-agent TOT rules + limited lodging package; eff. **2016-07-01**. |
| Lasting limited lodging text | Ord. 1444-16 → §337.251 (eff. **2017-01-26**): primary residence (&gt;51%), &lt;91 days/year, ≤30 consecutive days; rental-registration exemption for qualifying limited lodging. |
| Limited lodging enforcement | City legal/council discussion in 2026 and Avalara reporting: owner-occupancy/day-cap regime not actively/constitutionally enforceable → `enforcement_date` **null** for 1444-16. |
| New primary framework (2026) | Ord. 561-2026 (passed **2026-06-01**): Chapter 686B license ($150), insurance, local contact (1-hour), 10% density cap, nuisance revocation, booking-agent registration; repeals §337.251. STR provisions effective **180 days after passage = 2026-11-28** (not Legistar’s general 2026-07-01 date). |
| Airbnb municipal tax | **2016-07-01** — city 3% TOT via Ord. 30-16; Airbnb currently lists Cleveland TOT collection. County 5.5%/6.5% collection from **2016-04-01** is county-only and not used. |
| Airbnb data sharing | **null** — no City Portal / API / enforcement feed documented. |

## Legislative history (3 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. No. 30-16 (limited lodging / TOT booking agents) | 2016-06-06 | 2016-07-01 | 2016-07-01 | yes |
| Ord. No. 1444-16 (§337.251 Limited Lodging) | 2017-01-23 | 2017-01-26 | null | yes |
| Ord. No. 561-2026 (Chapter 686B STR licensing) | 2026-06-01 | 2026-11-28 | 2026-11-28 | yes |

## Airbnb fields

- `airbnb_tax_collection_date`: **2016-07-01** — Ord. 30-16 effective date for booking-agent collection of Cleveland’s 3% TOT; pre-ordinance Airbnb help listed only county tax; RNC-era reporting confirmed city-tax collection.
- `airbnb_data_sharing_date`: **null** — no documented direct compliance/enforcement data connection between Airbnb and the City of Cleveland.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Cleveland, OH entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_cleveland.bak`
- Script: `agent/scripts/update_cleveland_str_regulations.py`
- Report: `agent/reports/2026-08-08-cleveland-str-legislative-history.md`
