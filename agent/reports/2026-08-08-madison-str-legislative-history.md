# Madison, WI short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Madison, WI (first unchecked city). Madison’s primary STR framework is **ORD-13-00185** (2013-10-29 / eff. 2013-11-06), which added Tourist Rooming Houses to the Zoning Code with primary-residence and unhosted 30-day rules. **2017 Wis. Act 59** (§ 66.1014) constrained local bans on 7+ day rentals; **ORD-20-00036** (eff. 2020-04-15; ZTRHP required 2020-10-01) created the annual § 9.29 permit; **ORD-23-00067** (2023-07-21) dual-tracked 1–6 vs. 7–29 night rules; **ORD-25-00033** (2025-06-03) raised the application fee to $300. Airbnb began collecting Madison municipal room tax on **2017-05-01**. No Airbnb–city compliance data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Madison, WI (index 76).
- Compiled binding actions from Madison Legistar (Files 31136 / ORD-13-00185, 58895 / ORD-20-00036, 78146 / ORD-23-00067, 87992 / ORD-25-00033), city Building Inspection TRH pages and ZTRHP materials, Wis. Stat. § 66.1014 / 2017 Wis. Act 59, Airbnb Madison help article, and Wisconsin State Journal / Reason coverage of the 2013 and 2017 actions.
- Excluded RES-17-00224 (Airbnb tax VCA authorization—captured in tax fields), Host Compliance contract File 46226 (third-party scraping), File 04162 transient-hotel hourly-rental rules, and non-binding study/recommendation materials.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework (2013) | ORD-13-00185: TRH zoning use; primary residence; 30-day unhosted cap; health license + room tax. |
| State preemption (2017) | Wis. Stat. § 66.1014 limits local bans on 7+ day residential rentals; TRH license if >10 nights/year. |
| City permit (2020) | ORD-20-00036 / MGO § 9.29 annual ZTRHP; city required permit as of 2020-10-01. |
| Dual track (2023) | ORD-23-00067: primary-residence track for 1–6 night stays; 180-day track for 7–29 night stays. |
| Fee update (2025) | ORD-25-00033: application fee $100 → $300. |
| Airbnb municipal tax | **2017-05-01** — City 10% room tax via voluntary collection agreement. |
| Airbnb data sharing | **null** — Host Compliance scraping only; no City Portal/API. |

## Legislative history (5 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| ORD-13-00185 TRH zoning | 2013-10-29 | 2013-11-06 | 2013-11-06 | yes |
| 2017 Wis. Act 59 (§ 66.1014) | 2017-09-21 | 2017-09-23 | 2017-09-23 | no |
| ORD-20-00036 § 9.29 ZTRHP | 2020-03-31 | 2020-04-15 | 2020-10-01 | no |
| ORD-23-00067 dual-track TRH | 2023-07-11 | 2023-07-21 | 2023-07-21 | no |
| ORD-25-00033 application fee | 2025-05-20 | 2025-06-03 | 2025-06-03 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2017-05-01** — Airbnb Madison help article; follows RES-17-00224 VCA for municipal room tax (MGO § 4.21).
- `airbnb_data_sharing_date`: **null** — no documented direct Airbnb–city compliance data connection.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Madison, WI entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_madison.bak`
- Script: `agent/scripts/update_madison_str_regulations.py`
