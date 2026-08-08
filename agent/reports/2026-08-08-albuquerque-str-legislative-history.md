# Albuquerque, NM short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Albuquerque, NM (first unchecked city). Albuquerque’s primary STR framework is Ordinance O-20-30 (Enactment O-2020-038), creating ROA § 13-19 (permit, insurance, occupancy/gathering limits, Good Neighbor Agreement), effective 2021-04-23. Earlier state SB 106 and city O-19-71 closed the three-room lodgers’-tax loophole and imposed marketplace collection (and briefly monthly listing disclosure, later removed by O-21-75/O-21-68). Airbnb began collecting Albuquerque’s municipal Lodgers’ Tax and Hospitality Fee under a voluntary agreement in October 2017. No lasting Airbnb–city data connection found. Failed bills O-23-69 and O-26-5 were excluded.

## What was done

- Identified first list item lacking `agent_checked`: Albuquerque, NM (index 31).
- Compiled binding state and city STR-related legislation from 2008 onward from NM Legislature (SB 106 final PDF / Ch. 25), CABQ Legistar and enacted ordinance PDFs (O-19-71, O-20-30, O-21-75/O-21-68, O-25-75), City STR Task Force page and report, Treasury lodgers’-tax materials, Airbnb help article 2318, LodgingRevs PR (2021-04-14), and news (KRQE, Avalara, Las Cruces Sun-News).
- Excluded non-binding R-18-49 (task force) and failed ordinances O-23-69 (permit caps / local manager; failed 2023-08-21) and O-26-5 (separation requirement; failed 2026-02-02).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | O-20-30 / § 13-19 (passed 2020-10-05; eff. 2021-04-23) — permit-based, not a ban or primary-residence-only regime. |
| Tax base expansion | NM SB 106 + city O-19-71 removed &lt;3-room exemption; platforms must collect city lodgers’ tax / hospitality fee from 2020-01-01. |
| Platform data | O-19-71 required monthly listing disclosure; O-21-75/O-21-68 removed that duty in 2021. |
| Later tightening (failed) | O-23-69 (1,200 citywide cap, 3 permits/person) and O-26-5 (separation) failed. |
| Distressed lodging | O-25-75 (2025) adds guest-log / tax-lien tools for problem lodging, including STRs. |
| Airbnb tax | **2017-10-01** — municipal Lodgers’ Tax (5%) + Hospitality Fee (1%) via VCA. |
| Airbnb data sharing | **null** — no documented lasting Airbnb–city feed/API/MOU. |

## Legislative history (5 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| NM SB 106 (Laws 2019, Ch. 25) | 2019-02-04 | 2020-01-01 | 2020-01-01 | no |
| O-19-71 / O-2019-024 | 2019-09-04 | 2020-01-01 | 2020-01-01 | no |
| O-20-30 / O-2020-038 (§ 13-19) | 2020-10-05 | 2021-04-23 | 2021-04-23 | yes |
| O-21-75 / O-21-68 (remove listing disclosure) | 2021-09-08 | 2021-10-04 | 2021-10-04 | no |
| C/S O-25-75 / O-2025-016 (distressed lodging) | 2025-05-05 | 2025-05-23 | 2025-05-23 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2017-10-01** — City Treasury materials report an Airbnb voluntary collection agreement in October 2017 for Albuquerque Lodgers’ Tax and Hospitality Fee (municipal).
- `airbnb_data_sharing_date`: **null** — monthly marketplace disclosure under O-19-71 was repealed in 2021; no operational Airbnb–city data connection found (LodgingRevs is third-party).

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Albuquerque, NM entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_albuquerque.bak`
- Report: `agent/reports/2026-08-08-albuquerque-str-legislative-history.md`
