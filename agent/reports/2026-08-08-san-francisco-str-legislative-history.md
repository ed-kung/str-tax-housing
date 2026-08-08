# San Francisco, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for San Francisco, CA (first unchecked city). Primary host framework is Ordinance 218-14 (operative 2015-02-01): permanent-resident registry with 275-night residency / ~90-night unhosted cap. Platform verification duties from Ordinances 104-16 / 178-16 were stayed in litigation until the May–June 2017 Airbnb settlement (Board endorsement 2017-06-02) and Ordinance 089-17’s reasonable-care standard. Airbnb has collected SF municipal TOT since 2014-10-01; listing/compliance data sharing dates to the 2017 settlement.

## What was done

- Identified first list item lacking `agent_checked`: San Francisco, CA (index 16).
- Compiled binding Chapter 41A ordinances from SF Board of Supervisors / Legistar PDFs, City Attorney settlement materials, OSTR platform guidelines, Airbnb SF tax help article, and contemporaneous news (SFGate, SF Chronicle, Reuters).
- Excluded failed/vetoed proposals (e.g., Proposition F; 60-day and 120-day hard-cap bills that did not become law) and non-binding resolutions except as context for the settlement endorsement date.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2015 baseline | Chapter 41A / Planning Code banned tourist/transient (&lt;30-day) use of residential units citywide. |
| Primary framework | Ordinance **218-14** (enacted 2014-10-27; operative/enforced **2015-02-01**): permanent-resident exception, registry, insurance, TOT duties; 275-night residency ⇒ max 90 unhosted nights. |
| Enforcement office | Ordinance **130-15** (effective **2015-08-29**): created OSTR; quarterly host reports; expanded private right of action; Ellis Act–related limits. |
| Platform rules | **104-16** (2016-06-24; never enforced as listing-gate) → **178-16** (enacted 2016-08-11; booking-fee verification; stayed in suit) → **089-17** (effective 2017-05-14; reasonable-care standard). |
| Settlement / data | Settlement signed 2017-05-01; Board Resolution 208-17 enacted **2017-06-02**; full unregistered-listing purge ~**2018-01-16**. |
| Airbnb tax | Municipal TOT collection began **2014-10-01** (Airbnb + SFGate/CBS). |
| Airbnb data sharing | **2017-06-02** — settlement endorsement required monthly listing feeds, registration gating, and delisting (distinct from Aug 2015 QWC tax data). |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (San Francisco entry)
- Report: `agent/reports/2026-08-08-san-francisco-str-legislative-history.md`
