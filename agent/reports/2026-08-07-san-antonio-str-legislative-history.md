# San Antonio, TX short-term rental legislative history

San Antonio was the first entry in `str_regulations.json` without `agent_checked`. Its short-term rental
regulation is unusually simple compared with the cities already coded: Texas has never enacted a binding
STR statute, so the entire history is three City of San Antonio ordinances. The city went from no STR
rules at all to a permit-and-density regime in November 2018 (Ordinance 2018-11-01-0858), tightened the
density math in a routine Unified Development Code amendment effective January 2023 (Ordinance
2022-11-03-0831), and overhauled fees, enforcement and platform obligations in June 2024 (Ordinance
2024-06-13-0433). The 2024 ordinance is what finally forced Airbnb to collect the city's hotel occupancy
tax; the city puts that start date at March 10, 2025. There is no evidence Airbnb has ever shared
listing- or host-level data with San Antonio, so `airbnb_data_sharing_date` is null.

## What was done

- Located San Antonio, TX as the first unchecked city in `AGENT_DATA_PATH/str_regulations.json`.
- Researched binding city, county and state actions affecting Airbnb-style rentals from 2008 forward,
  working from the ordinance texts on `docsonline.sanantonio.gov`, the Municode codification of City Code
  Chapter 16 Article XXII and UDC Sec. 35-374.01, City of San Antonio Finance and Development Services
  fact sheets, and contemporaneous reporting (San Antonio Report, Texas Public Radio, Express-News, AP).
- Wrote the three ordinances, the two Airbnb dates, and `agent_checked: True` into the JSON.

## Legislative history

| Ordinance | Passed | Effective | Substance |
| --- | --- | --- | --- |
| 2018-11-01-0858 | 2018-11-01 | 2018-11-01 (90-day grace period for existing operators) | First STR ordinance. Type 1 / Type 2 split, $100 three-year permit, HOT registration prerequisite, 12.5% block-face density cap on Type 2, permit number in all ads, revocation and $200-$500 daily fines. |
| 2022-11-03-0831 | 2022-11-03 | 2023-01-01 | Omnibus UDC amendment. Type 2 block-face density must round down rather than up; new applications above the cap need a Board of Adjustment special exception; ADUs used as STRs must comply with Sec. 35-374.01, which confines them to Type 1. |
| 2024-06-13-0433 | 2024-06-13 | 2024-06-13, except Sec. 16-1104.01 (HOT) on 2024-09-12 | Fees to $300 (Type 1) / $450 (Type 2), 45-day application completeness deadline, one-year bar for false documentation, corner-lot block-face rule, monthly HOT reporting even at zero, platform collection of city and county HOT, platform removal of unpermitted listings within 10 business days, compliance meetings, administrative and injunctive enforcement, revocation after three citations in three years, posted quiet hours. |

The 2018 ordinance passed 8-2 and the 2024 ordinance 9-0; under Section 7 of each, eight or more
affirmative votes make the ordinance effective immediately, which is why passage and effective dates
coincide. Airbnb and HomeAway both wrote in support of the 2018 ordinance.

## Airbnb dates

- `airbnb_tax_collection_date`: **2025-03-10**. Airbnb has collected the 6% Texas state HOT since
  May 1, 2017 under an agreement with the Comptroller, but that is state tax, not tax on behalf of the
  city. Talks with San Antonio in 2018 stalled over Airbnb's request to waive hosts' back taxes, and no
  voluntary agreement was ever reached. City HOT collection was instead compelled by Sec. 16-1104.01 of
  the 2024 ordinance. Implementation slipped past the announced October 1, 2024 target; the city's own
  STR page and its January 2026 fact sheet both state that platforms began paying City HOT on operators'
  behalf effective March 10, 2025, when the revised reporting portal launched. The first covered receipts
  were February 2025 bookings, so an alternative defensible coding is 2025-02-01.
- `airbnb_data_sharing_date`: **null**. The 2024 ordinance's compliance mechanism runs from the city to
  the platform (the city identifies listings by URL and the platform must remove them within ten business
  days), not the reverse. San Antonio relies on a third-party vendor (Avenu Insights / Host Compliance) to
  detect unpermitted listings, and the city's March 2025 platform-deductions webinar states that platform
  HOT is "remitted to the city with no detail" and that properties receive no property-level credit,
  which is the opposite of a data-sharing arrangement.

## Judgment calls

- **No state-level entries.** The Texas Municipal League confirms there is no state statute preempting or
  authorizing municipal STR regulation. Preemption bills failed in 2017 (SB 451), 2019 (HB 3773, HB 3778,
  SB 1888) and 2023 (HB 2665, amended down to an interim study). SB 1592 (2025), which would have made
  platforms responsible for collecting local HOT statewide, passed the Senate but died in House Ways &
  Means. The relevant Texas appellate decisions (Tarr v. Timberwood Park, Zaatari v. City of Austin,
  City of Grapevine v. Muns) are judicial, not legislative, and were excluded.
- **SB 929 (2023) excluded.** It amended Tex. Loc. Gov't Code Sec. 211.019 to require cities to allow or
  compensate nonconforming uses created by zoning changes, which does constrain how San Antonio could
  wind down existing Type 2 STRs. It was left out because it is general zoning law and does not regulate
  short-term rentals as such.
- **Measure coding notes.** The 2018 ordinance is coded `time_restrictions: increase` because the STR
  definition sets a 12-hour floor on stays, barring hourly rentals. The 2024 ordinance is coded
  `primary_residence_requirements: increase` because it created the first permit fee differential
  ($300 vs. $450) penalizing non-owner-occupied rentals, even though the Type 1 / Type 2 definitions
  themselves were unchanged.

## Artifacts

- Script: `agent/scripts/03_str_regulations_san_antonio_tx.py`
- Updated data: `AGENT_DATA_PATH/str_regulations.json` (timestamped backup written alongside it)
