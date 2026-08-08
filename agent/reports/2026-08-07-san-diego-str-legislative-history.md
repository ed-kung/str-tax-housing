# San Diego, CA short-term-rental legislative history

San Diego was the first entry in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked`. I researched the city's short-term-rental legislative history back to 2008 and added ten binding actions to the record: two 2018 city ordinances that were suspended by referendum and repealed before taking effect, the 2021 STRO ordinance that is the current regime, its fee resolutions and implementation-date amendment, the 2022 ordinance adopting the Coastal Commission's modifications, and three California statutes that bind San Diego hosts and platforms. The defining feature of San Diego's history is that the city had no short-term-rental-specific code at all until the STRO license requirement became enforceable on May 1, 2023, roughly two years after the ordinance was signed, because the Coastal Commission had to certify the Local Coastal Program amendment covering the beach communities where most listings sit. Airbnb began collecting the city's Transient Occupancy Tax voluntarily on July 1, 2015, eight years before the city could require it.

## Timeline entered

| Passage | Effective | Jurisdiction | Action |
| --- | --- | --- | --- |
| 2018-08-02 | 2018-09-01 (never operative) | City of San Diego | Ordinances O-20977 and O-20978, first STRO licensing regulations |
| 2018-11-20 | 2018-12-20 | City of San Diego | Ordinance O-21008, granting the referendary petition and repealing both ordinances |
| 2021-04-14 | 2021-05-29 | City of San Diego | Ordinance O-21305, SDMC Chapter 5, Article 10 (the STRO ordinance) |
| 2021-09-24 | 2021-09-24 | State of California | SB 60 (Ch. 307, Stats. 2021), higher STR infraction fines |
| 2021-10-25 | 2021-10-25 | City of San Diego | Resolution R-313742, initial STRO application and license fees |
| 2022-02-24 | 2022-03-26 | City of San Diego | Ordinance O-21436, delaying the license requirement past July 1, 2022 |
| 2022-06-27 | 2022-08-10 | City of San Diego | Ordinance O-21464, Coastal Commission suggested modifications (LCP-6-SAN-21-0046-2) |
| 2023-10-13 | 2024-07-01 | State of California | AB 537 (Ch. 805, Stats. 2023), all-in pricing for short-term lodging |
| 2025-02-18 | 2025-03-01 | City of San Diego | Resolution R-316035, updated STRO fees |
| 2025-10-13 | 2026-01-01 | State of California | SB 346 (Ch. 751, Stats. 2025), Short-Term Rental Facilitator Act |

## Main findings

- **The 2018 regulations never took effect.** The Council adopted the Bry/Zapf compromise 6-3 on July 16, 2018 (final passage August 2), limiting licenses to a host's primary residence plus one unit on the same parcel, capping whole-home use of the primary residence at 180 days a year, and imposing a three-night minimum in the coastal zone and downtown. A referendum petition backed by Airbnb, HomeAway and Share San Diego submitted about 62,000 signatures on August 30, 2018 and was certified sufficient on September 25, suspending the ordinances. The Council repealed them 8-1 on October 22, 2018 rather than face a 2020 ballot fight, which also barred an "essentially similar" ordinance for one year.
- **The 2021 STRO ordinance uses the police power, not zoning.** O-21305 added SDMC Chapter 5, Article 10 rather than amending the Land Development Code, which let the city impose licensing, caps and a lottery without reclassifying properties. Four tiers: Tier 1 (20 days or less), Tier 2 (home share in the primary residence, host resident 275 days a year), Tier 3 (whole home outside Mission Beach, capped at 1 percent of housing units, two-night minimum, lottery) and Tier 4 (whole home in Mission Beach, capped at 30 percent). One license per host, one unit per host, two-year non-transferable terms.
- **Coastal Commission review drove a two-year implementation lag.** Parts of Secs. 510.0102 and 510.0104 amended the certified Local Coastal Program, so they could not apply in the Coastal Overlay Zone until certified. The Council pushed the start date past July 1, 2022 (O-21436), the Commission certified with four suggested modifications in March 2022, the Council adopted them in O-21464 (effective August 10, 2022), and the license requirement finally became enforceable May 1, 2023. Two of the modifications matter substantively: Tier 3 lottery licenses must be distributed proportionally by Community Planning Area, and coastal-zone licensing sunsets January 1, 2030 unless extended.
- **Airbnb tax collection long predates regulation.** Airbnb started collecting the 10.5 percent TOT and the 0.55 percent Tourism Marketing District assessment from guests on July 1, 2015 under a voluntary collection agreement, while the city was pursuing hosts for back taxes. Platform collection only became mandatory under SDMC Sec. 510.0201(e) in 2021.
- **Data sharing started with enforcement, not with the ordinance.** SDMC Sec. 510.0201(f) requires monthly listing-level reports (license number, responsible person, street address, days booked), and that obligation attached on May 1, 2023, with the first report due June 30, 2023. An October 2021 City Treasurer memo confirms that before then platforms remitted TOT in aggregate and gave the city no host-level data; the city later used administrative subpoenas to compel reporting, and reported over 7,000 illegal listings removed in the program's first year.
- **No further city amendments through mid-2026.** Post-2022 city action has been limited to fee resolutions. A reported loophole allowing owners to obtain a license after a no-fault eviction remained unfixed as of July 2026, and a 2026 proposal for a whole-home STR tax died in committee.

## Coding notes

- The 2018 package is recorded as a single entry because O-20977 (enforcement authority) and O-20978 (licensing) were adopted and repealed together. Its `effective_date` is the nominal 30-days-after-passage date; the summary states that the referendum suspended it so it never became operative.
- O-21436 is coded "no change" on all eight measures because it changed only the implementation date.
- O-21464 is coded as an increase on the land-use and host measures, since its practical effect was to extend the licensing scheme into the Coastal Overlay Zone, but "no change" on platform compliance because Division 2 was never part of the certified LCP.
- The two fee resolutions are included as binding law (they amend the city's rate book) and are coded as increases in registration requirements only.
- SB 346 is included because it is binding statewide from January 1, 2026, though San Diego has not adopted a conforming ordinance and already obtains equivalent data under its own code.

## Artifacts

- Script: `agent/scripts/03_str_regulations_san_diego_ca.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (San Diego, CA entry; `agent_checked: true`)
- Backup of prior file: `AGENT_DATA_PATH/str_regulations.<timestamp>.json.bak`

## Key sources

- San Diego Municipal Code Chapter 5, Article 10, Divisions 1 and 2 (docs.sandiego.gov municode)
- City Clerk resolutions and ordinances index (O-20977, O-20978, O-21008, O-21305, O-21436, O-21464, R-313742, R-316035)
- City Attorney Memorandum of Law MS-2018-15 (October 2018 repeal and referendum effects)
- California Coastal Commission staff report, LCP-6-SAN-21-0046-2, item W14f, March 2022
- Office of the City Treasurer STRO program pages, host operating requirements checklist, and hosting platform reporting guidelines
- City Auditor hotline report 20-001 (July 2019), identifying O-20977 and O-20978
- NBC 7 San Diego (July 2015 Airbnb TOT collection), Times of San Diego and San Diego Union-Tribune (July and October 2018), KPBS (April 2021 mayoral signature, May 2023 enforcement launch)
- California legislative counsel records for SB 60, AB 537 and SB 346
