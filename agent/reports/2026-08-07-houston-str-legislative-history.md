# Houston, TX short-term-rental legislative history

Houston was the first entry in `AGENT_DATA_PATH/str_regulations.json` without `agent_checked: True` (index 3). Houston is a late and light regulator: it had no short-term-rental ordinance of any kind until Ordinance No. 2025-322, passed unanimously by City Council on April 16, 2025 and effective January 1, 2026, which creates a registration-only regime with no density cap, no primary-residence or owner-occupancy rule, and no restriction on whole-home or single-family rentals. Before that, the only STR-specific legal obligation on Houston hosts was tax: Texas HB 1905 (2015) wrote short-term rentals into the Tax Code definition of "hotel," making them subject to the 6 percent state and 7 percent City of Houston hotel occupancy taxes. Airbnb began collecting the city's municipal HOT on July 1, 2019 under an agreement with Houston First Corporation (it had started collecting the state HOT on May 1, 2017). No Airbnb–Houston data-sharing arrangement was found; the city buys listing identification and complaint intake from Granicus Host Compliance instead, so `airbnb_data_sharing_date` is coded null.

## What was written

Three `legislative_history` entries plus the two Airbnb date keys and `agent_checked: True` were written to the Houston record.

| Law | Jurisdiction | Passed | Effective |
| --- | --- | --- | --- |
| HB 1905, 84th Leg. (Tax Code Sec. 156.001(b)) | State of Texas | 2015-06-20 | 2015-09-01 |
| Ordinance No. 2025-322 (Ch. 28, Art. XXIII) | City of Houston | 2025-04-16 | 2026-01-01 |
| HB 2464, 89th Leg. (Loc. Gov't Code Sec. 229.902) | State of Texas | 2025-06-12 | 2025-06-12 |

- `airbnb_tax_collection_date`: `2019-07-01`
- `airbnb_data_sharing_date`: `null`

## Findings

**HB 1905 (2015).** An omnibus tax bill whose Section 22(a) added Tax Code Sec. 156.001(b): for purposes of Chapters 156, 351, 352 "or other law," hotel includes a short-term rental, meaning a rental to someone who is not a permanent resident (no right to 30 consecutive days). The bill calls this a clarification of existing law. It is the basis for HOT liability on Houston Airbnb hosts and is coded as an increase in host compliance requirements only.

**Ordinance No. 2025-322.** Registration-based, administered by the Administration and Regulatory Affairs Department. $275 annual fee per unit plus a $33.10 administrative fee; separate non-transferable certificate per unit; applications require owner and operator contacts, proof of ownership or owner permission, 24-hour emergency contact, all platform listing URLs, an acknowledgement that STR use does not violate deed restrictions or HOA rules, human-trafficking awareness training, and proof of HOT registration or remittance. Operating rules add a one-night minimum stay, a ban on advertising special events, registration number and occupancy limits on all listings, an emergency contact who must respond within one hour, and posting of the certificate inside the unit. Revocation triggers include HOT non-payment, two noise convictions in 12 months, and one conviction for enumerated violent, trafficking or prostitution offenses at the property; three revocations for one owner in 24 months can take down all their certificates. Platforms must display registration numbers, may not list unregistered units, and must delist within 10 business days of city notice. Fines run $100–$500 per day.

Coded as increases in registration, time, host compliance and platform compliance requirements. Time restrictions is coded increase solely because of the one-night minimum stay; there is no annual night cap. Rental type, unit type, host presence and primary residence are all no change — a proposed density cap was dropped before passage over the legal risk created by *Zaatari v. City of Austin* and the Dallas litigation.

**HB 2464 (2025).** A home-based business preemption bill, but Sec. 229.902(d)(2) expressly preserves municipal authority to regulate short-term rentals. Included because it is binding law that removes a preemption argument against Ordinance 2025-322, which took effect six months later; all eight measures are coded no change.

## Judgement calls

- **Effective date of the Houston ordinance** is coded 2026-01-01, the date in Section 6 of the ordinance itself. Council passage was April 16, 2025 (emergency clause, final passage on the date of introduction). Implementation then slipped administratively: the registration portal opened October 1, 2025 rather than August 1; active enforcement began April 1, 2026; and platform delisting notices were pushed first to April 1, 2026 and then to January 1, 2027. None of those deferrals were ordinance amendments, so none appear in the legislative history.
- **Third-party sites (CityRuleLookup, StaySTRA) report a $1 million liability insurance requirement.** That was in the December 2024 committee draft; it is not in the adopted ordinance text, so it is excluded.
- **Excluded as non-legislative:** *Tarr v. Timberwood Park* (Tex. 2018) and *Zaatari v. Austin* (judicial); HB 2665 (2023), which was amended down to an interim study; SB 1592 / HB 2433 (2025) on platform tax collection, which died in the House. Texas still has no STR preemption statute.
- **Excluded as not STR-specific:** the City of Houston's July 1, 2011 designation of Houston First Corporation as its HOT collection agent, and Harris County's HOT.
- **`airbnb_data_sharing_date` is null.** Searches surfaced no Airbnb–Houston data-sharing agreement or Airbnb City Portal participation. Under the ordinance the information flow runs the other way: the city notifies platforms which listings to remove. Listing identification comes from the city's Granicus Host Compliance contract (up to $1,640,159.54 through FY29 via Carahsoft).

## Artifacts

- Script: `agent/scripts/03_str_regulations_houston_tx.py`
- Updated: `AGENT_DATA_PATH/str_regulations.json` (Houston entry, index 3)
- Backup of prior state: `AGENT_DATA_PATH/str_regulations.json.bak`

## Sources

- Adopted ordinance text and Exhibit A: `houstontx.gov/ara/rp/Short-Term-Rental-Ordinance-Adopted.pdf`
- City press release, April 17, 2025: `houstontx.gov/ara/20250417.html`
- ARA FAQ (April 25, 2025), Director Rules and Regulations, and STR registration pages
- Texas Legislature Online bill histories for HB 1905 (84R) and HB 2464 (89R); Tax Code Sec. 156.001
- Houston First Corporation HOT FAQs (July 1, 2019 Airbnb collection date); Airbnb newsroom, "Houston's Tourism and Arts Industries Receive a Financial Boost"
- Dallas Morning News and Houston Chronicle coverage of the May 1, 2017 Texas Comptroller agreement
- Houston Public Media, Houston Press, and Avalara coverage of passage and enforcement
