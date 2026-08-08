# Toledo, OH short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Toledo, OH (first unchecked city). Toledo’s STR regime is established by a single binding ordinance—**Ordinance No. 267-21** (passed/approved **2021-12-07**)—enacting Municipal Code **Chapter 702** with permit requirements effective **60 days later (2022-02-05)**. No later amending ordinance, municipal Airbnb tax-collection agreement, or Airbnb–city compliance data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Toledo, OH (index 84).
- Compiled binding legislation from Toledo Legistar (O-267-21 full text), American Legal Chapter 702 citations, the City’s Short-Term Rental Permit page, and contemporaneous NBC24 / Signal Ohio coverage.
- Searched Toledo Legistar for Airbnb, lodging-tax, hosting-platform, and Chapter 702 amendments; only O-267-21 is a binding STR ordinance (2025 HCD “Short Term Rentals” items are committee reports, not enacted law).
- Checked Airbnb’s Ohio occupancy-tax help article and found no Toledo/Lucas County municipal collection listing.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (1 entry), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | Ord. 267-21 → TMC Chapter 702: $50/unit annual STR operating permit; insurance; life-safety; occupancy 2/bedroom + 2; 24/7 local contact (45-minute response); neighbor notice; ad permit-number display; fines $100/week up to $500. |
| Effective / enforcement | Permit provisions effective **2022-02-05** (§702.06: 60 days after 2021-12-07 adoption). No injunction or superseding law found; city still administers permits → `enforcement_date` = effective date. |
| Later legislation | No Chapter 702 amendments in Legistar/Am. Legal. 2025 committee discussions not binding. |
| Airbnb municipal tax | **null** — Airbnb Ohio help lists only Cuyahoga County, Cincinnati, Cleveland; no City of Toledo lodging-tax VCA documented. |
| Airbnb data sharing | **null** — no City Portal / API / enforcement feed documented. |

## Legislative history (1 entry)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. No. 267-21 (Chapter 702 Short-Term Rentals) | 2021-12-07 | 2022-02-05 | 2022-02-05 | yes |

## Airbnb fields

- `airbnb_tax_collection_date`: **null** — no documented municipal-level Airbnb collection for Toledo.
- `airbnb_data_sharing_date`: **null** — no documented direct compliance/enforcement data connection.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Toledo, OH entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_toledo.bak`
- Script: `agent/scripts/update_toledo_str_regulations.py`
- Report: `agent/reports/2026-08-08-toledo-str-legislative-history.md`
