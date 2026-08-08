# Los Angeles, CA short-term-rental legislative history

Los Angeles was the first record in `AGENT_DATA_PATH/str_regulations.json` without an `agent_checked`
value. I researched the city's short-term-rental legislative history back to 2008 and filled in the
record. The finding in one line: Los Angeles had no binding STR-specific legislation at all until 2018,
then adopted its primary framework — the Home-Sharing Ordinance (Ordinance No. 185931) — on December 11,
2018, effective July 1, 2019 and enforced from November 1, 2019. Airbnb began collecting the city's own
14 percent Transient Occupancy Tax on August 1, 2016 under a voluntary agreement, more than two years
before the city had any regulatory framework, and established a direct compliance data connection with
the city on November 6, 2019 when the Council approved its Platform Agreement, automated via the city's
API on August 31, 2020.

## What was recorded

Four binding laws, in order:

1. **Ordinance No. 185451, the "Party House Ordinance"** (City of Los Angeles), passed 2018-02-21,
   effective and enforced 2018-04-15. Added LAMC Section 41.58.1 making loud or unruly gatherings at a
   residence a public nuisance with escalating administrative fines, reaching the person who rents the
   residence out. Written largely in response to STR party houses and later cross-referenced by the
   Home-Sharing Ordinance's suspension rules and guest Code of Conduct.
2. **Ordinance No. 185931, the "Home-Sharing Ordinance"** (City of Los Angeles), passed 2018-12-11,
   effective 2019-07-01, enforced 2019-11-01. The city's primary framework (`primary_framework: true`).
   Legalizes short-term rentals as an accessory use in residential zones but only in a registered primary
   residence, caps them at 120 nights a year absent an Extended Home-Sharing registration, excludes rent
   stabilized and covenanted affordable units, and imposes host record-keeping, safety, occupancy and
   noise rules plus platform booking-verification and monthly data-reporting duties.
3. **Ordinance No. 186197, Short-Term Rental Enforcement Trust Fund** (City of Los Angeles), passed
   2019-06-18, effective 2019-07-28. Companion fiscal ordinance directing ten percent of STR-attributable
   TOT and the home-sharing per-night fee into a dedicated enforcement fund, and authorizing the per-night
   fee later set by Council resolution at $3.10 effective 2020-12-01.
4. **SB 60 (Glazer), Chapter 307, Statutes of 2021** (California), passed and effective 2021-09-24 as an
   urgency statute. Raises the maximum administrative fines cities may impose for health-or-safety STR
   ordinance infractions to $1,500/$3,000/$5,000. `enforcement_date` is null: as of the City Attorney's
   November 26, 2024 report, Los Angeles was still charging $500 per violation and had not adopted the
   higher maximums.

`airbnb_tax_collection_date`: **2016-08-01**. Confirmed by the LA Office of Finance TOT page and Airbnb's
own newsroom post; the 14 percent TOT is a city tax under LAMC Article 1.7, so it qualifies as
municipal-level collection.

`airbnb_data_sharing_date`: **2019-11-06**. Airbnb signed its Platform Agreement 2019-10-31 (CF
14-1635-S9) and the Council approved it 2019-11-06, after which the city began sending Airbnb lists of
categorically ineligible listings to take down. The daily-query API launched 2020-08-31.

## Judgment calls

- **Excluded non-binding actions.** The Master Platform Agreement resolution (2019-10-30), the Airbnb
  Platform Agreement itself (2019-11-06), the Administrative Guidelines (2019-06-28) and the per-night fee
  resolution (2020-11-10) are all implementing instruments rather than legislation, so they appear in
  summaries and explanations rather than as `legislative_history` entries.
- **Excluded the Vacation Rental Ordinance.** The proposed ordinance to allow STRs in non-primary
  residences (CF 18-1246) has been pending since 2020, was reinstated in June 2025 and is still in
  committee as of mid-2026 alongside an Olympics-related temporary program (CF 25-0029-S1). Never adopted.
- **Excluded California AB 537** (2023, short-term lodging price advertising). It is a general consumer
  price-disclosure law applying to all lodging including hotels, not an STR regulation.
- **Nothing between 2008 and 2018.** The pre-existing prohibition on transient use in residential zones
  predates 2008 and no STR-specific ordinance was adopted in that window; the city's own planning reports
  and LA Times reporting describe the pre-2018 rules as effectively unenforceable.
- **Coastal zone.** Coastal Act Protectors v. City of Los Angeles (2022) 75 Cal.App.5th 526 challenged
  application of the Home-Sharing Ordinance in the Venice coastal zone without a coastal development
  permit. Both the trial court and the Court of Appeal rejected it, so enforcement was never suspended and
  the enforcement date is unchanged.

## Artifacts

- Script: `agent/scripts/03_str_regulations_los_angeles.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (record index 1, Los Angeles CA, `agent_checked: 1`)
- Pre-edit backup: `/tmp/str_regulations.backup.json` (only index 1 differs)

## Primary sources

- Council files 14-1635-S2 (Home-Sharing Ordinance), 14-1635-S7 (Trust Fund, per-night fee),
  14-1635-S9 (Airbnb Platform Agreement), 14-1635-S10 (enforcement), 12-1824-S1 (Party House Ordinance),
  18-1246 and 25-0029-S1 (proposed vacation rentals), all at cityclerk.lacity.org
- LA City Planning Home-Sharing Administrative Guidelines (2019-06-28) and the October 4, 2023 enforcement
  report to CF 14-1635-S10
- LA Office of Finance, Transient Occupancy Tax Requirements
- Airbnb newsroom, "City of Los Angeles collected more than $275 million in taxes from Airbnb"
- Los Angeles Times, "L.A., Airbnb launch system meant to help enforce rental rules" (2020-08-31)
- California Legislative Information, SB 60 (2021-2022)

## Next unchecked city

Chicago, IL.
