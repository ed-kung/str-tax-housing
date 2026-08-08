# Cincinnati, OH short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Cincinnati, OH (first unchecked city). Cincinnati’s STR regime is **Ordinance No. 125-2019** (passed 2019-04-24; eff./enforced **2019-07-01**), creating CMC Chapters 856 (registration) and 315 (7% excise tax). **Ordinance No. 206-2019** (passed 2019-06-19; §315-27 amendments eff. **2019-07-01**) redirected tax deposits to General Fund 050 while tying estimated STR revenue to a minimum affordable-housing capital appropriation. Airbnb municipal tax collection: **2019-10-01**. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Cincinnati, OH (index 63).
- Compiled binding legislation from the City PDF of Ord. 125-2019, Legistar file 201900700 / April 24, 2019 council minutes, Ord. 206-2019 PDF (file 201900992), City Finance STR page and Rules & Regulations (eff. 11/6/2023), July 1, 2019 registration-portal press release, August 2023 Internal Audit, CityBeat coverage, and Airbnb’s Ohio occupancy-tax help article.
- Excluded non-enacted 2018–early-2019 STR bills (files 201800479, 201801597, 201801690, 201900527, 201900593 — indefinitely postponed / filed-sunset; no enactment numbers).
- Excluded Ord. 406-2019 (Chapter 874 residential rental registration), which expressly exempts rentals of 30 days or less.
- Excluded Hamilton County lodging tax (hotel definition: five or more rooms) and administrative Rules & Regulations (not binding legislation).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (2 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework (2019) | Ord. 125-2019: registration + 7% excise tax; eff. **2019-07-01**. |
| Unit / affordable-housing limits | Cap on STRs in 5+ unit buildings; ban on subsidized affordable units as STRs. |
| No night / primary-residence caps | No annual day cap; no host-presence or primary-residence requirement (local “responsible person” within 50 miles). |
| Revenue routing | Ord. 206-2019 amended §315-27 (eff. **2019-07-01**): tax to Fund 050; estimated revenue floors affordable-housing CIP appropriation. |
| Airbnb municipal tax | **2019-10-01** — VCA / voluntary withholding of City 7% excise tax. |
| Airbnb data sharing | **null** — VCA yields aggregate tax returns only; no listing-level compliance feed documented. |

## Legislative history (2 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. No. 125-2019 (Ch. 856 / 315) | 2019-04-24 | 2019-07-01 | 2019-07-01 | yes |
| Ord. No. 206-2019 (§315-27 revenue) | 2019-06-19 | 2019-07-01 | 2019-07-01 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2019-10-01** — City Finance page and Rules & Regulations: Airbnb voluntary withholding of the municipal 7% STR excise tax began 10/1/2019; Airbnb help currently lists Cincinnati collection.
- `airbnb_data_sharing_date`: **null** — 2023 Internal Audit: Airbnb VCA reports aggregate tax figures only, without host/guest PII or listing-level enforcement data.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Cincinnati, OH entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_cincinnati.bak`
- Script: `agent/scripts/update_cincinnati_str_regulations.py`
- Report: `agent/reports/2026-08-08-cincinnati-str-legislative-history.md`
