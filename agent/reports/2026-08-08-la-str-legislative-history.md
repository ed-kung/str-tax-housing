# Los Angeles STR legislative history

Updated the first unchecked city in `AGENT_DATA_PATH/str_regulations.json` (Los Angeles, CA) with legislative history from 2008 onward, Airbnb municipal tax and data-sharing fields, and `agent_checked: 1`.

## Summary

Los Angeles’s Airbnb-relevant STR regime is centered on Ordinance 185931 (Home-Sharing Ordinance), adopted 2018-12-11, effective 2019-07-01, and actively enforced from 2019-11-01. It legalizes short-term rentals only in a host’s primary residence (generally 120 nights/year unless Extended Home-Sharing), with registration, unit-type bans (RSO/affordable/Ellis), platform duties, and fees/fines. Companion Ordinance 186197 created the Short-Term Rental Enforcement Trust Fund; a 2020 Council resolution set the per-night fee; Ordinance 188796 (2025) raised Home-Sharing registration fees. Airbnb began collecting the City’s 14% TOT on 2016-08-01; the Home-Sharing API with Airbnb went live 2020-08-31 (Platform Agreement approved 2019-11-06). County STR rules and California SB 346 were excluded (unincorporated-only / enabling without a new LA ordinance).

## Legislative history (4 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. 185931 Home-Sharing Ordinance | 2018-12-11 | 2019-07-01 | 2019-11-01 | yes |
| Ord. 186197 STR Enforcement Trust Fund | 2019-06-18 | 2019-07-28 | 2019-07-28 | no |
| Resolution: Home-Sharing per-night fee (CF 14-1635-S7) | 2020-11-10 | 2020-12-01 | 2020-12-01 | no |
| Ord. 188796 Planning fee update (incl. Home-Sharing) | 2025-12-10 | 2026-02-23 | 2026-02-23 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: 2016-08-01 — voluntary City TOT collection agreement; Office of Finance and Airbnb ($275M+ remitted Aug 2016–Jun 2023).
- `airbnb_data_sharing_date`: 2020-08-31 — Home-Sharing API launch after Nov 2019 Platform Agreement; City Planning (2021-09-08) and LA Times (2020-08-31).

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Los Angeles, CA entry)
