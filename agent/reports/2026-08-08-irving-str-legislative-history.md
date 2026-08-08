# Irving, TX short-term rental legislative history

Researched and updated the Irving, TX entry in `AGENT_DATA_PATH/str_regulations.json` (index 87), the first list item lacking `agent_checked`. Added `legislative_history` (6 binding actions from 2015–2026), Airbnb municipal tax-collection and data-sharing fields, and `agent_checked: 1`.

## Summary

Irving’s primary municipal STR framework is **Ordinance 2022-10550** (passed 2022-02-24; effective/enforced **2022-10-01**), creating Chapter 8, Article XI registration for single-family STRs ($200 fee, HOT account, one-hour emergency agent, guest postings). **Ord. 2025-11095** (2025-04-10) expanded registration to all residential structures (including multifamily), added $1M insurance, a 24-hour minimum stay, adult-primary-guest rules, event-center advertising bans, and a graduated revocation process. **Ord. 2026-11269** (2026-05-07; key standards from **2026-05-08**) added a 10% block-face density denial rule, single-family parking/one-lodging-agreement limits, floor plans, and fire-safety equipment. **Ord. 2026-160-UDC** (2026-07-30; eff. **2026-07-31**) requires CUPs for new STRs in most “R” residential single-family/townhome districts, with existing registered STRs treated as legal nonconforming. State **H.B. 1905** (eff. 2015-09-01) confirmed STRs are “hotels” for HOT. Airbnb’s Texas tax help page currently lists Irving’s 9% municipal HOT as platform-collected, but no official start date was found (`airbnb_tax_collection_date` null). No Airbnb–city compliance data connection found.

## Legislative history (included)

| Date | Action |
| --- | --- |
| 2015-06-20 / eff. 2015-09-01 | Texas H.B. 1905 — STR = hotel for HOT |
| 2022-02-24 / eff. 2022-10-01 | Ord. 2022-10550 — Ch. 8 Art. XI STR registration (**primary_framework**) |
| 2023-09-14 | Ord. 2023-10801 — Ch. 8 fee repeal / consolidated fee schedule alignment |
| 2025-04-10 | Ord. 2025-11095 — multifamily registration, insurance, min stay, enforcement |
| 2026-05-07 / standards 2026-05-08 | Ord. 2026-11269 — parking, 10% block face, fire safety, one lodging agreement |
| 2026-07-30 / eff. 2026-07-31 | Ord. 2026-160-UDC — CUP for new STRs in most residential “R” districts |

## Airbnb fields

- **Tax collection:** `null` — Airbnb help/article/2331 currently lists Irving 9% municipal HOT as collected on-platform (absent on Wayback 2023-03-06; present by 2023-10-04), but no official start-date announcement; City STR materials and Airbnb’s Irving responsible-hosting page still tell hosts to remit local HOT.
- **Data sharing:** `null` — no documented direct Airbnb–City compliance/API connection.

## Artifacts

- Updated JSON: `$AGENT_DATA_PATH/str_regulations.json` (Irving entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_irving.bak`
- Update script: `agent/scripts/update_irving_str_regulations.py`
