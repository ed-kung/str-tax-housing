# Winston-Salem, NC — Short-term rental legislative history

**Summary:** Winston-Salem has no dedicated city short-term-rental ordinance. Binding post-2008 STR-relevant law is primarily North Carolina’s rental-registration/permit preemption sequence (S.L. 2011-281 → 2016-122 → 2019-73 → 160D-1207 via 2019-111/2020-25), plus S.L. 2019-246 facilitator occupancy-tax duties. Local zoning still routes hosted paid lodging through the joint Winston-Salem/Forsyth County UDO Bed and Breakfast use (pre-2008 owner-occupancy rules in RS districts). Forsyth County levies a 6% occupancy tax (no separate city levy); Airbnb currently collects NC local occupancy taxes, but Forsyth was not in the 2015 four-county launch and no documented first Forsyth collection date was found (`airbnb_tax_collection_date`: null). No Airbnb–city data connection found.

## City processed

- **City:** Winston-Salem, North Carolina  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 90)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **No dedicated city STR framework.** Official and secondary sources confirm Winston-Salem/Forsyth have no stand-alone STR permit or registry. NCGS 160D-1207(c) bars general rental registration/renting-permission schemes. Hosted overnight lodging in residential districts is addressed under the joint UDO Bed and Breakfast use (§2-5.9: owner-occupied in RS districts; Special Use Permit from ZBA in many residential districts). Whole-house Airbnb-style rentals are not carved out as a separate UDO use.

2. **State preemption is the primary post-2008 regulatory constraint.** Same statutory chain as Durham/Charlotte: S.L. 2011-281, 2016-122, 2019-73, and Chapter 160D recodification. Local UDO-CC10 (City Council consideration April 2021) made technical Chapter 160D conformity amendments. *Schroeder v. City of Wilmington* (2022) confirmed the registration bar applies to STR schemes.

3. **Occupancy tax is county-level.** Forsyth County levies a 6% room occupancy and tourism development tax (under-90-day stays, including Airbnb-style rentals), authorized by local acts (S.L. 1983-908 as amended, including S.L. 2009-157 administrative changes). The City does not levy a separate municipal occupancy tax; local acts share a portion of county proceeds with Winston-Salem.

4. **Airbnb tax collection:** **null** — Forsyth County occupancy tax exists and Airbnb’s current NC help article states all local city/county occupancy taxes are collected, but the May 18, 2015 VCA announcement covered only Wake, Durham, Mecklenburg, and Buncombe. No Forsyth-specific first-collection date found.

5. **Airbnb data sharing:** **null** — City Portal launch listed Raleigh, not Winston-Salem; no Winston-Salem portal/API/compliance feed documented. NC remittances are described as lump-sum without host-level identification.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| S.L. 2011-281 (SB 683) | State of North Carolina | 2011-06-23 | 2011-06-23 | 2011-06-23 | true |
| S.L. 2016-122 (SB 326) | State of North Carolina | 2016-07-28 | 2017-01-01 | 2017-01-01 | true |
| S.L. 2019-73 (SB 483) | State of North Carolina | 2019-07-01 | 2019-07-01 | 2019-07-01 | false |
| S.L. 2019-111 / 2020-25 | State of North Carolina | 2019-07-11 | 2020-06-19 | 2020-06-19 | true |
| S.L. 2019-246 (SB 557) | State of North Carolina | 2019-11-08 | 2020-02-01 | 2020-02-01 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Winston-Salem entry)
- Script: `agent/scripts/update_winston_salem_str_regulations.py`
- Report: `agent/reports/2026-08-08-winston-salem-str-legislative-history.md`

## Key sources

- Winston-Salem/Forsyth County UDO (Bed and Breakfast §2-5.9 / use table; UDO-166 owner-occupancy, 2007); UDO-CC10 Chapter 160D conformity (City Council Action Request, Apr. 13, 2021)
- Forsyth County Tax Administration Room Occupancy Tax materials (6% county levy; applies to short stays)
- News & Observer / Bloomberg Law coverage of Airbnb’s May 18, 2015 NC tax announcement (Wake, Durham, Mecklenburg, Buncombe only)
- Airbnb help article 2320 (NC occupancy taxes — all local city/county occupancy taxes collected)
- Airbnb City Portal launch (Raleigh listed; Winston-Salem not)
- N.C. Session Laws 2011-281, 2016-122, 2019-73, 2019-111, 2020-25, 2019-246; G.S. 160D-1207; G.S. 153A-155; Forsyth occupancy-tax local acts (S.L. 1983-908 et seq.)
- *Schroeder v. City of Wilmington* (N.C. Ct. App. 2022); UNC SOG Coates’ Canons (McLaughlin, Nov. 2022) on Airbnb occupancy-tax remittance
