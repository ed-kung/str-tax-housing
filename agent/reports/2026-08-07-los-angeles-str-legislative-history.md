# Los Angeles, CA short-term rental legislative history

**Summary.** Los Angeles was the first unchecked city in `AGENT_DATA_PATH/str_regulations.json`. Its short-term rental regime is dominated by a single ordinance: the Home-Sharing Ordinance (Ordinance No. 185931), adopted December 11, 2018, effective July 1, 2019, with enforcement beginning November 1, 2019. It restricted short-term rentals to a host's primary residence, capped them at 120 nights a year absent an Extended Home-Sharing registration, excluded rent-stabilized and covenanted affordable units, and required both host registration and platform cooperation. Everything before it was either general nuisance law (the 2018 Party House Ordinance) or a tax arrangement (the August 2016 Airbnb Transient Occupancy Tax agreement); everything after it has been implementation and enforcement machinery rather than new substantive restrictions. Los Angeles is unusual in the strength of its platform relationship: Airbnb is the only hosting platform that has signed a Home-Sharing Platform Agreement with the city, and the automated removal interface it launched on August 31, 2020 is the most consequential enforcement event after the ordinance itself. Seven legislative entries and four platform enforcement entries were written to the JSON file.

## Legislative history recorded

| Date passed | Effective | Jurisdiction | Law |
| --- | --- | --- | --- |
| 2018-02-21 | 2018-04-15 | City | Ordinance 185451, Party House / Loud or Unruly Gatherings (LAMC 41.58.1) |
| 2018-12-11 | 2019-07-01 | City | Ordinance 185931, Home-Sharing Ordinance (LAMC 12.22 A.32) |
| 2019-10-30 | 2019-11-01 | City | Resolution adopting Appendix A (platform responsibilities) and the Master Platform Agreement |
| 2020-11-10 | 2020-12-01 | City | Council action setting the per-night fee at $3.10 |
| 2021-09-24 | 2021-09-24 | State | SB 60 (Ch. 307, 2021), higher STR infraction fines |
| 2023-10-13 | 2024-07-01 | State | AB 537 (Ch. 805, 2023), total-price disclosure for short-term lodging |
| 2025-03-18 | 2025-03-18 | City | Council action adopting enforcement recommendations (CF 14-1635-S10) |

Two entries are Council actions rather than enacted ordinances and are labelled as such in their summaries: the November 10, 2020 per-night fee setting and the March 18, 2025 enforcement package. The 2025 item was included because it changed enforcement practice immediately (the city stopped mailing warning letters before citation and launched a public permit portal), even though the corresponding ordinance amendments were still in committee as of mid-2026.

## Platform enforcement recorded

| Effective | Arrangement |
| --- | --- |
| 2016-08-01 | Airbnb voluntary Transient Occupancy Tax collection agreement (14 percent; over $275M remitted through June 2023) |
| 2019-11-06 | Home-Sharing Platform Agreement with Airbnb; removal of categorically ineligible listings from November 1, 2019 |
| 2020-08-31 | Automated removal interface; 96-hour takedown of unregistered listings, false-exemption and 120-day-cap enforcement |
| 2020-12-01 | Airbnb collection and remittance of the $3.10 per-night enforcement fee |

## Notable findings and judgment calls

- **The ordinance both legalized and restricted.** Short-term rentals under 30 days were already prohibited in most residential zones before 2019, so the Home-Sharing Ordinance created the first legal pathway while simultaneously imposing registration, a 120-day cap and unit exclusions. The `measures` fields code it as an increase in restrictions, which matches how it operated in practice: listings fell from about 36,600 to roughly 85 percent below that level by 2021. Anyone using this for identification should be aware of the ambiguity.
- **Host presence is coded "no change."** Los Angeles requires primary residence but, unlike New York, does not require the host to be present during a guest's stay; whole-home rental of one's own primary residence while away is the core permitted use.
- **Enforcement date lags the effective date by four months.** The ordinance was effective July 1, 2019 (registration portal opened) but enforcement began November 1, 2019. For event-study purposes November 2019 (or August 2020, when the API went live) is probably the sharper break than July 2019.
- **Airbnb never sued Los Angeles** over the Home-Sharing Ordinance, in contrast to New York and San Francisco. The city's relationship with the platform has been cooperative throughout, which is why the platform enforcement list is longer and more operative here than the legislative list after 2019.

## Excluded, with reasons

- **Los Angeles County short-term rental ordinance** — applies only to unincorporated areas, not within city limits.
- **Coastal Act Protectors v. City of Los Angeles (2022)** and **People v. Venice Suites, LLC (2021)** — court decisions, not legislation. The first upheld enforcement of the Home-Sharing Ordinance in the Venice coastal zone without a coastal development permit; the second limited enforcement against apartment-house operators and prompted the pending LAMC 12.03 technical amendment.
- **Pending items as of August 2026** — the Vacation Rental Ordinance for non-primary residences (CF 25-0029-S1, reactivated June 2025), the LAMC 12.03 technical amendment (CF 14-1635-S13, PLUM approved March 24, 2026), and the private right of action draft ordinance (City Attorney report May 7, 2026). None has been adopted.
- **Ordinance 188,796** — a comprehensive City Planning fee update effective February 23, 2026 that raised home-sharing application fees; a fee schedule rather than a substantive STR rule.

## Sources

Primary sources were the Los Angeles City Clerk council files (14-1635-S2, 14-1635-S9, 14-1635-S10, 14-1635-S13, 20-0995, 25-0029-S1, 12-1824-S1), the text of Ordinances 185931 and 185451, the Home-Sharing Administrative Guidelines and the Master and Airbnb Platform Agreements, the Department of City Planning progress report of September 8, 2021, City Planning and Office of Finance program pages, the California Legislative Information texts of SB 60 and AB 537, and the Airbnb newsroom release on Los Angeles tax remittances. Secondary corroboration came from the Los Angeles Times coverage of the August 2020 API launch and Councilmember Raman's March 18, 2025 press release.

## Artifacts

- Script: `agent/scripts/03_str_regulations_los_angeles_ca.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (Los Angeles entry now has `legislative_history`, `platform_enforcement`, `agent_checked: true`)
