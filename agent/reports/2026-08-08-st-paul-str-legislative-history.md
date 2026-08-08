# St. Paul, MN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for St. Paul, MN (first unchecked city). St. Paul’s primary STR framework is Ordinance 17-49 (Chapter 379 host/platform licensing, effective Dec. 2, 2017; active enforcement from about April 1, 2018 after March 2018 warning notices), with companion zoning Ord. 17-38, fee Ord. 17-47, Class R definitions Ord. 17-48, and April 2018 Ord. 18-14 amendments that narrowed some platform duties. Airbnb began collecting Minnesota state sales tax and DOR-administered local sales/special taxes—including St. Paul municipal sales tax and lodging tax applicable to typical STRs—on **2018-10-01** under marketplace-provider rules; no dated Airbnb–city direct data connection found.

## What was done

- Identified first list item lacking `agent_checked`: St. Paul, MN (index 66).
- Compiled binding city and state STR-related legislation from 2008 onward from St. Paul Legistar (Ords. 17-38, 17-47, 17-48, 17-49, 18-14), city STR program pages/PDFs, Star Tribune / Pioneer Press / MinnPost reporting, MN DOR Revenue Notices 12-07 / 17-06 and Special Local Taxes materials, Airbnb Help article 2311, and Avalara Apr 2018 Airbnb tax guidance.
- Excluded non-binding RES 16-181 (study request) and individual license adverse-action resolutions.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | Ord. 17-49 (Ch. 379 host + platform licensing) — primary; Ord. 17-38 zoning companion. |
| 2018 adjustment | Ord. 18-14 (Apr 11, 2018): removed platform “licensed hosts only” booking duty; ZIP-aggregate quarterly reports; deleted Ch. 379 petty-misdemeanor penalty; added host ad/registry duties. |
| Municipal STR taxes | St. Paul sales tax 1.5%; lodging tax 3% (<50 rooms) / 7% (50+ rooms); DOR-administered. |
| Airbnb tax | **2018-10-01** — MN marketplace collection start; includes DOR local sales/special taxes covering St. Paul. |
| Airbnb data sharing | **null** — quarterly report/delist duties exist; no dated City Portal/API/feed documented. |

## Legislative history (6 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| 2011 Minn. 1Sp Sess. ch. 7 art. 3 (accommodations intermediary tax base) | 2011-07-20 | 2011-07-21 | 2011-07-21 | no |
| 2017 Minn. 1Sp Sess. ch. 1 art. 3 (§ 297A.66 marketplace / lodging) | 2017-05-30 | 2018-10-01 | 2018-10-01 | no |
| St. Paul Ord. 17-38 (zoning §§ 65.645 et al.) | 2017-10-25 | 2017-12-02 | 2018-04-01 | no |
| St. Paul Ord. 17-49 (Ch. 379 hosts/platforms) | 2017-10-25 | 2017-12-02 | 2018-04-01 | yes |
| St. Paul Ord. 17-47 (§ 310.18 fees) | 2017-10-25 | 2017-12-02 | 2018-04-01 | no |
| St. Paul Ord. 18-14 (Ch. 379 amendments) | 2018-04-11 | 2018-05-18 | 2018-05-18 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2018-10-01** — municipal: St. Paul local sales tax and lodging tax (DOR-administered special local taxes) collected via MN DOR after marketplace rules took effect; Avalara Apr 2018 still listed MN as non-collecting.
- `airbnb_data_sharing_date`: **null** — no documented direct Airbnb–St. Paul data connection start date.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (St. Paul, MN entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_st_paul.bak`
- Script: `agent/scripts/update_st_paul_str_regulations.py`
- Report: `agent/reports/2026-08-08-st-paul-str-legislative-history.md`
