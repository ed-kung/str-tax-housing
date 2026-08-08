# Los Angeles, CA short-term-rental legislative history

Los Angeles was the first entry in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked: true`. I researched the city's short-term-rental (STR) legislative history from 2008 forward, wrote seven binding legislative actions into a `legislative_history` list, added `airbnb_tax_collection_date` (2016-08-01) and `airbnb_data_sharing_date` (2020-08-31), and marked the record checked. The single dominant action is the Home-Sharing Ordinance (Ordinance No. 185,931), adopted 2018-12-11, effective 2019-07-01, enforced from 2019-11-01, which restricts STRs to a host's registered primary residence with a 120-night annual cap. Nothing binding happened at the city level between 2008 and early 2018: STRs of 30 days or less were already prohibited by the zoning code in most residential zones (confirmed by *Chen v. Kraft* (2016)), and the city simply did not enforce it. Notably, Airbnb's voluntary tax agreement (2016) predates any STR ordinance by more than two years.

## Entries written to `legislative_history`

| Effective | Title | Jurisdiction |
| --- | --- | --- |
| 2018-04-15 | Ordinance No. 185,451, "Party House" / Loud or Unruly Gatherings (LAMC 41.58.1) | City |
| 2019-07-01 | Ordinance No. 185,931, Home-Sharing Ordinance (LAMC 12.22 A.32) | City |
| 2019-11-01 | Council resolution adopting Appendix A of the Home-Sharing Administrative Guidelines and the Master Platform Agreement | City |
| 2020-12-01 | Ordinance No. 186,197 (Short-Term Rental Enforcement Trust Fund) plus the 2020-11-10 per-night fee resolution | City |
| 2021-09-24 | SB 60 (Ch. 307, Stats. 2021), enhanced fines for STR ordinance infractions | State |
| 2024-07-01 | AB 537 (Ch. 805, Stats. 2023), all-in price disclosure for short-term lodging | State |
| 2026-02-23 | Ordinance No. 188,796, comprehensive planning fee update (Home-Sharing fees) | City |

## Main findings

- **The Home-Sharing Ordinance is the only substantive land-use regime.** Council adoption 2018-12-11, mayoral approval 2018-12-17, publication 2018-12-21, effective 2019-07-01, enforcement start 2019-11-01. Primary residence only (six months of the year), 120 nights per calendar year unless the host obtains Extended Home-Sharing approval, one registration and one booked listing per host, registration number required on every advertisement, prior TOT registration certificate required, and categorical exclusion of RSO units, covenanted affordable units, Ellis Act withdrawals within five years, converted RSO single-family homes within five years, and post-2017 ADUs that are not the host's primary residence. City listings fell about 74% between 2019 and 2023 (36,600 to 9,500).
- **No host-presence requirement.** Unlike New York, Los Angeles allows whole-home rental of a registered primary residence while the host is away, so `host_presence_requirements` is coded "no change" throughout, and `rental_type_restrictions` is coded "no change" for the Home-Sharing Ordinance because it does not distinguish private-room from whole-unit rentals. The binding constraint is the primary-residence rule, coded separately.
- **Platform obligations were built in two layers.** The ordinance itself bars platforms from completing bookings for unregistered, over-cap or multiple listings; the Council's 2019-10-30 resolution then adopted Appendix A of the Administrative Guidelines and the Master Platform Agreement template, which set out the API method, the manual weekly spreadsheet method, and the Platform Agreement route. I treated this as binding law rather than a mere resolution because LAMC 12.22 A.32(i) provides that "No one shall fail to comply with the Administrative Guidelines."
- **`airbnb_tax_collection_date` = 2016-08-01.** Announced 2016-07-18 as an initially three-year voluntary agreement; Airbnb collects and remits the city's 14% Transient Occupancy Tax on its own bookings only. Airbnb reported remitting over $275 million between August 2016 and June 2023. A TOT collection agreement with the Office of Finance later became a precondition for signing a Home-Sharing Platform Agreement.
- **`airbnb_data_sharing_date` = 2020-08-31.** This is the date Airbnb went live on the city's compliance API after a two-week test, per City Planning's 2021 and 2023 reports to Council. Two earlier dates are defensible and were rejected: the Council approved the individual Airbnb Platform Agreement on 2019-11-06 (final 2019-11-08), and Airbnb removed thousands of city-identified categorically ineligible listings between late 2019 and early 2020 — but that was data flowing from the city to Airbnb, not the reverse. Sustained Airbnb-to-city listing data for compliance began with the API. Its launch cut listings a further ~14% immediately.
- **Airbnb is the only platform with a Platform Agreement**, and it also collects and remits the per-night enforcement fee ($3.10 from 2020-12-01, $3.30 as of 2025-09-01) for its hosts. City Planning estimated self-reporting compliance by hosts on non-agreement platforms at only ~35%.

## Excluded items and why

- **Short-Term Rental Technical Amendment Ordinance** (CF 14-1635-S13), which would amend LAMC 12.03 to declare that STR of dwelling units was never a permitted use, rebutting *People v. Venice Suites, LLC* (2021). Approved by the City Planning Commission 2025-09-25 and by PLUM 2026-03-24, but not yet adopted by the full Council, so not binding.
- **Council action of 2025-03-18** (CF 14-1635-S10) directing amendments to the Home-Sharing Ordinance, including a private right of action and mandatory platform booking verification. This is a directive to departments, not enacted law; draft amendments were still in committee as of mid-2026. A prior version of the agent script included this entry with a caveat; I dropped it to comply with the "binding legislative actions only" rule.
- **Vacation Rental Ordinance** allowing non-primary-residence rentals, possibly tied to the 2026 World Cup and 2028 Olympics (CF 25-0029-S1 / 18-1246). Held by PLUM 2026-05-12; never adopted.
- **Los Angeles County's STR ordinance**, which applies only to unincorporated areas and not inside the city.
- **Pre-2018 city actions.** The June 2015 Council motion directing City Planning to draft an ordinance, the 2016 City Planning Commission recommendation (CPC-2016-1243), and the various CAO sharing-economy studies are all non-binding steps toward Ordinance No. 185,931.

## Judgment calls

- **Ordinance No. 185,451 (Party House)** contains no STR-specific text — I verified the full ordinance. I included it because it arose from Council File 12-1824 on commercial party houses operated largely as STRs and was the city's only relevant enforcement tool in the year before the Home-Sharing Ordinance, but I coded every measure "no change" except `host_compliance_requirements` and said plainly in the summary that it is a general nuisance ordinance. A prior draft of this work asserted that the ordinance bars home-sharing while a violation notice is posted; that claim is not in the ordinance text and I could not verify it elsewhere, so it is not repeated.
- **Ordinance No. 188,796** is a general planning fee ordinance, not an STR measure, but it raised regular Home-Sharing registration from $89 to $441 and Extended Home-Sharing discretionary review from $5,660 to $12,798, so it is coded as an increase in registration requirements.
- **AB 537** is a consumer price-disclosure statute rather than a housing or land-use rule. It is included because it expressly covers STRs booked through platforms and is enforceable by the Los Angeles City Attorney.
- Coding is relative to the pre-existing legal baseline. Because the zoning code already prohibited STRs, the Home-Sharing Ordinance is technically a legalization, but every measure it introduced is an enforceable constraint where none previously operated, so it is coded as increasing restrictions.

## Artifacts

- Script: `agent/scripts/03_str_regulations_los_angeles_ca.py` (rewritten from an earlier version that used a `platform_enforcement` list; it now writes the current `airbnb_tax_collection_date` / `airbnb_data_sharing_date` schema)
- Data: `AGENT_DATA_PATH/str_regulations.json`, Los Angeles record updated with `legislative_history` (7 entries), `airbnb_tax_collection_date`, `airbnb_data_sharing_date`, `agent_checked: true`

## Primary sources consulted

- LA City Clerk council files 14-1635-S2, S7, S9, S10, S11, S13; 12-1824-S1; 09-0969-S4
- Ordinance No. 185,451 full text (cityclerk.lacity.org)
- Home-Sharing Ordinance FAQ and Administrative Guidelines (planning.lacity.gov); LAHD Home Sharing Ordinance page
- City Planning reports to Council dated 2019-10-18, 2021-09-08 and 2023-10-04 (API launch, platform agreement, listing counts)
- City of Los Angeles / Airbnb Home-Sharing Platform Agreement (CF 14-1635-S9, 2019-10-31)
- LA Office of Finance TOT requirements page; Airbnb newsroom ($275M remitted, Aug 2016–Jun 2023); LA Times / NBC LA / Fortune coverage of the July 2016 agreement
- California Legislative Information for SB 60 (2021) and AB 537 (2023)
- *Coastal Act Protectors v. City of Los Angeles* (2022) and *Chen v. Kraft* (2016) for the pre-ordinance legal baseline
