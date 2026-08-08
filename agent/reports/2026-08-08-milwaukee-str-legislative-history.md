# Milwaukee, WI short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Milwaukee, WI (first unchecked city). Milwaukee’s primary STR framework is state law—2017 Wisconsin Act 59 creating Wis. Stat. § 66.1014 (preemption of local bans on 7+ day residential rentals; tourist rooming house license for >10 nights/year) plus lodging-marketplace tax collection duties—administered locally by DNS as DATCP agent. The City’s first binding STR-specific ordinance is File 241547 (signed 2026-08-03; effective 2026-08-20), creating Code § 105-80 (platform incident reporting, 250-foot neighbor notice of TRH applications, public licensed-STR list). Airbnb began collecting Milwaukee Local Exposition room taxes (including the City-only 7% additional) on 2017-07-01 via its Wisconsin DOR agreement. No Airbnb–city direct data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Milwaukee, WI (index 30).
- Compiled binding state and city STR-related legislation from 2008 onward from Wisconsin session laws / LFB Act 59 summary, Wis. Stat. §§ 66.0615 and 66.1014, DOR Pub. 410 and marketplace guidance, Airbnb help article 2337 and Airbnb/WisBusiness tax announcements, Milwaukee Legistar (Files 241547, 230171, 191576, 240589, 260564), City Attorney opinion on File 241547, DNS tourist rooming house page, and news (Urban Milwaukee, Milwaukee Journal Sentinel).
- Excluded non-binding Resolution 230171 (study/recommendations only); unpassed Files 191576 (zoning), 240589 (TRH license ordinance), and 260564 (residency); and 2025 Act 129 (nonsubstantive correction bill).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | 2017 Wis. Act 59 (§ 66.1014 + lodging-marketplace tax rules)—not a Milwaukee city licensing code. |
| City licensing | DNS administers state tourist rooming house licenses; compliance historically low; no separate comprehensive city STR license ordinance enacted. |
| City STR ordinance | File 241547 / § 105-80 (signed 2026-08-03; eff. 2026-08-20): notices, public list, report incidents to platforms. |
| Local lodging tax | Wisconsin Center District Local Exposition Taxes: 3% basic (Milwaukee County) + 7% additional (City of Milwaukee only); DOR-administered. |
| Airbnb tax | **2017-07-01** — DOR agreement includes Local Exposition taxes for Milwaukee. |
| Airbnb data sharing | **null** — no City Portal/API; File 241547 is city→platform notice only. |

## Legislative history (4 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| 2017 Wis. Act 59 (§§ 66.0615 / 66.1014) | 2017-09-21 | 2017-09-23 | 2017-09-23 | yes |
| 2019 Wis. Act 10 (marketplace sales tax) | 2019-07-03 | 2020-01-01 | 2020-01-01 | no |
| 2021 Wis. Act 55 (room tax / marketplace remittance) | 2021-06-29 | 2021-10-01 | 2021-10-01 | no |
| Milwaukee File 241547 (§ 105-80) | 2026-08-03 (mayor signed) | 2026-08-20 | 2026-08-20 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2017-07-01** — municipal/local: City of Milwaukee 7% additional Local Exposition room tax (plus county basic) collected under Airbnb–Wisconsin DOR agreement.
- `airbnb_data_sharing_date`: **null** — no documented direct Airbnb–Milwaukee data connection.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Milwaukee, WI entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_milwaukee.bak`
- Report: `agent/reports/2026-08-08-milwaukee-str-legislative-history.md`
