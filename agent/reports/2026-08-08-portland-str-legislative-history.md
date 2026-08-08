# Portland, OR short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Portland, OR (first unchecked city). Portland’s primary ASTR framework is **Ordinance 186736** (RICAP 6 / PCC Ch. 33.207), passed **2014-07-30**, effective/enforced **2014-08-29**: Type A permit for 1–2 bedrooms with 270-day resident occupancy, Type B conditional use for 3–5 bedrooms. Follow-ons expand multi-dwelling eligibility (**186976**), codify booking-agent tax/data duties (**186985**), add a **$4/night** housing fee (**189031**), mandate platform registry or pass-through data sharing (**189557**), and tighten 2024 ASTR advertising/data rules (**191779**). State **HB 2656** (eff. **2013-10-07**) required lodging intermediaries to collect taxes on the retail price. Airbnb began collecting Portland municipal (+ Multnomah County) lodging taxes **2014-07-01**; monthly compliance data sharing began **2019-12-01** under the Aug 30, 2019 Airbnb MOU.

## What was done

- Identified first list item lacking `agent_checked`: Portland, OR (index 26).
- Compiled binding actions from Portland.gov / eFiles ordinances, PCC Ch. 33.207 / 6.04 / 6.09, City Auditor STR audit follow-up (Oct 2019), BPS adopted reports, OLIS HB 2656, and contemporaneous AP/Oregonian/OPB/Columbian coverage.
- Excluded technical-only or incidental amendments: Ord. **188259** (RICAP 8 notice-figure clarification), Ord. **187339**/**188170** (general TLT housekeeping), Ord. **190380**/**190687**/**190851** (Shelter-to-Housing / historic / Residential Infill packages with only incidental 33.207 touch-ups), and Ord. **191957** (2025 code reorganization).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (7 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2014 | Residential STRs generally required B&B conditional use; informal Airbnb listings grew without dedicated ASTR permits. |
| Primary framework | Ord. **186736** (2014-07-30; eff. **2014-08-29**): Ch. 33.207 Type A permit / Type B CU; 270-day residency; initially single-dwelling-focused. |
| Multi-dwelling | Ord. **186976** (eff. **2015-02-13**): expands Type A to apartments/condos with 1-unit or 25% cap. |
| Tax / platforms | Ord. **186985** (eff. **2015-02-20**): booking-agent tax remit + address/host data on request + permit-number advertising. Ord. **189031** (eff. **2018-08-01**): $4/night fee. Ord. **189557** (eff. **2019-07-12**): registry gating or pass-through data MOU. |
| 2024 updates | Ord. **191779** / RICAP 10 (eff. **2024-10-01**): ad capacity limits, transactional data on request, Type B ban in commercial zones, unit-based revocation bar. |
| State tax | **HB 2656** (final House passage 2013-06-24; eff. **2013-10-07**): intermediary collection on retail price (OTC litigation followed). |
| Airbnb tax | Municipal (+ county) lodging tax collection via VCA from **2014-07-01** (first U.S. city). |
| Airbnb data sharing | Tax VCA did **not** share host IDs; monthly compliance feed from **2019-12-01** after Aug 30, 2019 MOU. |

## Legislative history (7 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| HB 2656 (OR lodging tax intermediaries) | 2013-06-24 | 2013-10-07 | 2013-10-07 | no |
| Ord. 186736 (ASTR Ch. 33.207) | 2014-07-30 | 2014-08-29 | 2014-08-29 | yes |
| Ord. 186976 (multi-dwelling ASTRs) | 2015-01-14 | 2015-02-13 | 2015-02-13 | no |
| Ord. 186985 (booking agent TLT duties) | 2015-01-21 | 2015-02-20 | 2015-02-20 | no |
| Ord. 189031 ($4 nightly fee / Ch. 6.09) | 2018-06-20 | 2018-08-01 | 2018-08-01 | no |
| Ord. 189557 (registry or data-sharing) | 2019-06-12 | 2019-07-12 | 2019-07-12 | no |
| Ord. 191779 (RICAP 10 ASTR updates) | 2024-06-13 | 2024-10-01 | 2024-10-01 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2014-07-01** — AP / Columbian / Oregonian; Portland–Airbnb VCA collecting City 6% TLT (+ Multnomah County lodging tax).
- `airbnb_data_sharing_date`: **2019-12-01** — City Auditor follow-up; first monthly Airbnb pass-through registration/transactional data delivery under Aug 30, 2019 MOU implementing Ord. 189557.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Portland, OR entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_portland.bak`
- Report: `agent/reports/2026-08-08-portland-str-legislative-history.md`
