# Minneapolis, MN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Minneapolis, MN (first unchecked city). Minneapolis’s primary STR framework is Ordinance 2017-054 (Ch. 244 host licensing/registration, effective Dec. 1, 2017; active enforcement from March 21, 2018), with companion platform licensing Ordinance 2017-055 (Ch. 351). December 2020 Ordinances 2020-061/062 tightened host caps (one non-homestead STR; 10% cap in 20+ unit buildings) and platform delisting duties. Airbnb began collecting Minnesota state sales tax and DOR-administered local sales taxes—including Minneapolis municipal sales tax—on **2018-10-01** under marketplace-provider rules; no Airbnb–city direct data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Minneapolis, MN (index 45).
- Compiled binding city and state STR-related legislation from 2008 onward from Municode (Ords. 2017-054/055, 2020-061/062; Code §§ 244.1845, Ch. 351), Minneapolis LIMS File 2019-00707 / council agendas, Star Tribune / FOX 9 / MinnPost reporting, MN DOR Fact Sheet 164M and Revenue Notices 12-07 / 17-06, Minn. Stat. §§ 297A.61 / 297A.66, Airbnb Help article 2311 (current and Wayback Aug 2019), Avalara Airbnb tax guides (Apr 2018 vs July 2019), and Duluth city press (for contrast on first MN municipal lodging agreement).
- Excluded non-binding staff recommendations/resolutions and unpassed 2019 Fletcher proposal materials beyond what became the 2020 ordinances.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (6 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | Ord. 2017-054 (§ 244.1845 host license/registration) — primary; Ord. 2017-055 (Ch. 351 platforms) companion. |
| 2020 tightening | Ords. 2020-061/062 (Dec 4, 2020): one non-homestead STR cap; 10% cap in large buildings; insurance/management/neighbor notice; license # on listings + platform delist duty. |
| Municipal STR taxes | Minneapolis Entertainment Tax (3%) applies to all short-term lodging; Minneapolis Lodging Tax (3%) only for >50-room establishments. Also Minneapolis sales tax 0.5%. |
| Airbnb tax | **2018-10-01** — MN marketplace collection start; includes DOR-administered local sales taxes (Minneapolis city sales tax). |
| Airbnb data sharing | **null** — no City Portal/API; Ch. 351 is request/delist based; city budgeted scraping. |

## Legislative history (6 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| 2011 Minn. 1Sp Sess. ch. 7 art. 3 (accommodations intermediary tax base) | 2011-07-20 | 2011-07-21 | 2011-07-21 | no |
| 2017 Minn. 1Sp Sess. ch. 1 art. 3 (§ 297A.66 marketplace / lodging) | 2017-05-30 | 2018-10-01 | 2018-10-01 | no |
| Minneapolis Ord. 2017-054 (Ch. 244 / § 244.1845 hosts) | 2017-10-20 | 2017-12-01 | 2018-03-21 | yes |
| Minneapolis Ord. 2017-055 (Ch. 351 platforms) | 2017-10-20 | 2017-12-01 | 2018-03-21 | no |
| Minneapolis Ord. 2020-061 (§ 244.1845 amendments) | 2020-12-04 | 2020-12-04 | 2020-12-04 | no |
| Minneapolis Ord. 2020-062 (§ 351.100 amendments) | 2020-12-04 | 2020-12-04 | 2020-12-04 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2018-10-01** — municipal: Minneapolis local sales tax (and later special local taxes per Airbnb 2311) collected via MN DOR after marketplace rules took effect; Avalara Apr 2018 still listed MN as non-collecting.
- `airbnb_data_sharing_date`: **null** — no documented direct Airbnb–Minneapolis data connection.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Minneapolis, MN entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_minneapolis.bak`
- Report: `agent/reports/2026-08-08-minneapolis-str-legislative-history.md`
