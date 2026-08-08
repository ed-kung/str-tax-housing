# Garland, TX short-term rental legislative history

Researched and updated the Garland, TX entry in `AGENT_DATA_PATH/str_regulations.json` (index 93), the first list item lacking `agent_checked`. Added `legislative_history` (4 binding actions from 2015–2026), Airbnb municipal tax-collection and data-sharing fields, and `agent_checked: 1`.

## Summary

Garland’s primary municipal STR framework is **Ordinance 7403** (passed/effective/enforced **2023-02-21**), creating Chapter 26, Article VI and Chapter 32 single-family permit rules for residential STRs (permit, inspection, landline, neighbor notice, placard, prohibited-conduct/enforcement). **Ord. 7625** (passed/effective **2025-09-02**; city-announced enforcement **2025-09-11**) added a 48-hour minimum stay, on-street parking ban, $500 minimum annual fee, liability insurance, floor plans, annual re-inspection, and stronger suspension/compliance tools. **Ord. 7677** (passed **2026-06-02** on consent) adds occupant liability for continued use of unpermitted STRs and right-of-way notice signage at revoked-permit properties. State **H.B. 1905** (eff. 2015-09-01) confirmed STRs are “hotels” for HOT. Airbnb’s Texas tax help page currently lists Garland’s 7% municipal HOT as platform-collected (present in the earliest Wayback capture of the page, 2021-10-27), but no official start date was found (`airbnb_tax_collection_date` null). No Airbnb–city compliance data connection found.

## Legislative history (included)

| Date | Action |
| --- | --- |
| 2015-06-20 / eff. 2015-09-01 | Texas H.B. 1905 — STR = hotel for HOT |
| 2023-02-21 | Ord. 7403 — Ch. 26 Art. VI + Ch. 32 STR permit framework (**primary_framework**) |
| 2025-09-02 / enf. 2025-09-11 | Ord. 7625 — min stay, parking, $500 fee, insurance, inspections, enforcement |
| 2026-06-02 | Ord. 7677 — occupant liability for unpermitted STRs; revoked-permit notice signs |

## Airbnb fields

- **Tax collection:** `null` — Airbnb help/article/2331 currently lists Garland 7% municipal HOT as collected on-platform (already present in Wayback 2021-10-27), but no official start-date announcement or City VCA date found.
- **Data sharing:** `null` — no documented direct Airbnb–City compliance/API connection.

## Artifacts

- Updated JSON: `$AGENT_DATA_PATH/str_regulations.json` (Garland entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_garland.bak`
- Update script: `agent/scripts/update_garland_str_regulations.py`
