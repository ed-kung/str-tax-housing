# Detroit, MI short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Detroit, MI (first unchecked city). Detroit has never adopted a dedicated short-term rental licensing ordinance. The only binding STR-specific legislative action since 2008 is **Ordinance No. 37-17** (Fifth General Text Amendment), which added a zoning prohibition on using a dwelling to accommodate paid overnight guests as a home occupation (now Sec. 50-12-492(d)), effective **2018-02-06**. City officials deferred enforcement almost immediately; CPC materials later state the Law Department found the provision too vague to enforce (`enforcement_date`: null). Later 2019 and 2024 STR drafts were never enacted. Airbnb collects only Michigan’s statewide 6% use tax (from 2017-07-01)—not a Detroit municipal tax—so `airbnb_tax_collection_date` is null. No Airbnb–city data-sharing connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Detroit, MI (index 25).
- Compiled binding actions from Detroit.gov LPD/CPC reports, Municode Sec. 50-12-492, Airbnb Michigan tax help article 2310, and contemporaneous reporting (Patch, Curbed, Detroit News summaries via secondary citations).
- Excluded non-binding drafts/resolutions: 2019 Ayers STR package (CPC hearing; never formally voted), Jan 3, 2024 Whitfield Calloway / LPD draft STR ordinance (not adopted), Michigan HB 4722 (House-passed 2021; expired without Senate enactment).
- Excluded the Oct 29, 2024 general rental-housing overhaul (Chapter 8 Article XV): it regulates rental registration/inspection generally and does not create an STR framework.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (1 entry), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2018 | No dedicated STR ordinance; B&Bs already barred in R1/R2; STRs largely unregulated as a distinct use. |
| Primary / only binding STR rule | Ord. 37-17 Fifth GTA: paid overnight guests prohibited as home occupation; eff. 2018-02-06. Exact Council roll-call date not located in digitized 2017 Journal Pt. 1 (ends mid-2017); contemporaneous news places enactment in 2017 after CPC’s Sept 8, 2017 Council transmittal. |
| Enforcement | Cease-and-desist letters ~Feb 2018, then public deferral of ticketing; Law Department later called the language too vague. Still on books; not actively enforced as STR regime. |
| Failed follow-ons | 2019 Ayers Chapter 9 / Chapter 61 package (primary residence, 90-day cap, 1,000-ft spacing, registration)—not adopted. 2024 draft Subdivision C licensing—not adopted. Sixth GTA initially proposed removing the overnight-guest ban, then left it in place after STR effort stalled. |
| Taxes | No City of Detroit accommodations tax collected by Airbnb. State 6% use tax only (Airbnb–Treasury agreement; collection from 2017-07-01). |
| Airbnb data sharing | None documented. |

## Legislative history (1 entry)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. No. 37-17 / Fifth GTA (overnight guests as home occupation) | null (2017; exact date not found) | 2018-02-06 | null | yes |

## Airbnb fields

- `airbnb_tax_collection_date`: **null** — Airbnb Michigan help lists only state 6% use tax (plus Genesee/Kent county taxes); no Detroit municipal levy collected via platform.
- `airbnb_data_sharing_date`: **null** — no official city/Airbnb data feed, portal, or delisting agreement found; platform duties appeared only in unadopted drafts.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Detroit, MI entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_detroit.bak`
- Report: `agent/reports/2026-08-08-detroit-str-legislative-history.md`
