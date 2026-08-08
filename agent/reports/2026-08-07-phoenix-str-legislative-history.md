# Phoenix, AZ short-term rental legislative history

Phoenix was the first city in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked`. I researched its short-term rental (STR) legislative history back to 2008 and added twelve binding entries, along with `airbnb_tax_collection_date` (2017-01-01) and `airbnb_data_sharing_date` (null), then set `agent_checked: true`. The Phoenix story is unusual because state law, not the city, has driven almost every change: Arizona's 2016 preemption statute (SB 1350) barred cities from regulating STRs as a distinct use, and each subsequent Phoenix ordinance (2020 registry, 2023 permit program, 2024 and 2026 ADU owner-occupancy amendments) exists only because the legislature later handed a specific, narrow power back to cities. Phoenix had no STR-specific ordinance before 2020, so there is nothing binding to record between 2008 and 2016.

## Timeline recorded

| Date passed | Jurisdiction | Action |
| --- | --- | --- |
| 2016-05-12 | Arizona | SB 1350 (Ch. 208): preemption of local STR regulation; online lodging marketplace tax classification (effective 2017-01-01) |
| 2018-04-11 | Arizona | SB 1382 (Ch. 189): marketplace tax registration mandatory from 2019-01-01 |
| 2019-05-21 | Arizona | HB 2672 (Ch. 240): emergency contact authority, nonresidential-use ban, TPT license on ads |
| 2020-01-08 | Phoenix | Ord. G-6653: first STR ordinance, city registry, prohibited uses, escalating fines |
| 2022-07-06 | Arizona | SB 1168: cities may require a permit/license (capped at $250), insurance, neighbor notice, suspensions |
| 2023-09-06 | Phoenix | Z-TA-5-23-Y: ADUs legalized citywide but barred from STR use |
| 2023-09-20 | Phoenix | Ord. G-7156: registration replaced by annual permit program (effective 2023-11-06) |
| 2024-05-21 | Arizona | HB 2720 (Ch. 196): preempts ADU STR bans, allows owner-residence rule for post-2024-09-14 ADUs |
| 2024-11-13 | Phoenix | Ord. G-7317: repeals the ADU STR prohibition |
| 2024-11-13 | Phoenix | Ord. G-7323: notarized owner-residence attestation for new-ADU properties (narrow) |
| 2025-05-23 | Arizona | HB 2928 (Ch. 217): restates the ADU owner-residence authority, extends framework to counties |
| 2026-03-04 | Phoenix | Ord. G-7495: owner-residence attestation extended to all post-2024-09-14 ADUs (effective 2026-04-04) |

## Notes on the coded measures

- The 2016 preemption is coded as a decrease across registration, rental type, time, unit type, host presence and primary residence, since it voided existing local bans and minimum-stay rules statewide and blocked Phoenix from adopting any. Platform compliance increases because the same act created the marketplace tax license and remittance duty.
- Phoenix has never imposed a cap, a primary-residence rule for ordinary homes, a host-presence rule, or a nights-per-year limit; state law forbids all of them. The only owner-occupancy requirement in Phoenix applies to properties with an accessory dwelling unit completed on or after 2024-09-14.
- The two 2024 ordinances were adopted at the same council meeting and pull in opposite directions: G-7317 removed the ADU STR ban (unit type decrease) while G-7323 added the ADU owner-residence attestation (primary residence increase).
- Effective dates for Phoenix ordinances without a stated operative date are 30 days after passage, the Arizona referendum window; this is confirmed by the city's own published dates for G-7156 (passed 2023-09-20, effective 2023-11-06 as specified in the ordinance) and G-7495 (passed 2026-03-04, effective 2026-04-04).

## Airbnb tax and data

- **Tax collection: 2017-01-01.** Governor Ducey and the Arizona Department of Revenue announced a partnership under which Airbnb began collecting and remitting state transaction privilege tax, county excise tax and municipal transient lodging tax (including Phoenix's) on 2017-01-01, the day SB 1350 took effect. Airbnb was the only platform doing so until SB 1382 made registration mandatory for all marketplaces on 2019-01-01.
- **Data sharing: none found.** Phoenix runs enforcement through its own SHAPE PHX permit portal and the Neighborhood Services Department. Platform reporting under A.R.S. Sec. 42-5076 flows to the state Department of Revenue in aggregate and expressly may not identify individual operators, and no Airbnb City Portal or memorandum of understanding with Phoenix was found. Recorded as null.

## Artifacts

- Script: `agent/scripts/03_str_regulations_phoenix.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json`
- Backup of prior file: `AGENT_DATA_PATH/str_regulations.20260807-204247.json.bak`

## Caveats

- The 2023 ADU text amendment is identified by its case number (Z-TA-5-23-Y); I could not confirm its G-number from a primary source.
- The reported $2,500-per-day penalty on platforms that list an unpermitted Phoenix property comes from Arizona Republic coverage of the adopted G-7156 rules rather than from the ordinance text, which I could not retrieve directly (phoenix.municipal.codes blocked automated requests).
