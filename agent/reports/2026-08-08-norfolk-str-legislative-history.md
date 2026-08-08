# Norfolk, VA — Short-term rental legislative history

**Summary:** Norfolk’s primary city STR framework is the Oct. 23, 2018 zoning text amendment creating Homestay and Vacation Rental uses (registry/CUP paths; program enforcement from **2019-01-01**). Earlier, the Mar. 1, 2018 zoning rewrite had allowed only limited R-C CUP vacation rentals. Major updates include Ord. **48814** (2022-06-28; primary-residence definitions and tighter multifamily/safety standards), Ord. **47894**/**49866** (West Freemason vacation-rental CUP open 2020, closed 2025), and Ord. **50,139** (STR flat tax per bedroom from **2026-01-01**). State law enabled local registries (**SB 1578**, 2017), mandated platform local TOT collection and monthly address reporting (**HB 518/SB 651**, **2022-10-01**), and limited *new* primary-residence CUP rules (**SB 544**, 2024). Airbnb municipal TOT collection and monthly locality data reporting for Norfolk begin **2022-10-01**.

## City processed

- **City:** Norfolk, Virginia  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 95)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary framework (2018–2019).** Oct. 23, 2018 zoning text amendment authorized Homestay (owner present) and Vacation Rental (owner absent) citywide via zoning certificate/registration and/or CUP, with business license and lodging-tax duties. Legal effective date in Council minutes is 2018-10-23; active registry/enforcement launch was Jan. 1, 2019.

2. **2022 standards update (Ord. 48814).** Redefined Homestay/Vacation Rental around primary residence, standardized district rules, and increased multifamily/safety/CUP triggers. A later Apr. 23, 2024 “technical revisions” item (proposed revert to owner-present definitions) was continued pending SB 544 and was not adopted.

3. **Platform taxes & data (2022-10-01).** HB 518/SB 651 plus Norfolk Ord. 48924 require intermediaries to collect/remit Norfolk TOT and file monthly property-level reports. Pre-mandate Avalara guidance: Airbnb collected only VA state sales tax for Norfolk; hosts remitted municipal TOT.

4. **West Freemason.** Ord. 47894 (2020-02-25) allowed vacation rentals by CUP in HC-WF1/HC-WF2; Ord. 49866 (2025-02-25) removed that use (existing CUP at 358 W. Freemason may run to expiration).

5. **2026 room-tax change.** Ord. 50,139 (eff. 2026-01-01) applies the $3 flat tax per bedroom per night for STRs.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| SB 1578 / Ch. 741 (§ 15.2-983) | Commonwealth of Virginia | 2017-03-24 | 2017-07-01 | 2017-07-01 | false |
| 2018 Zoning Ordinance rewrite (limited R-C CUP STR) | City of Norfolk | 2018-01-23 | 2018-03-01 | 2018-03-01 | false |
| Citywide Homestay/Vacation Rental ZTA | City of Norfolk | 2018-10-23 | 2018-10-23 | 2019-01-01 | true |
| Ord. No. 47894 (West Freemason VR CUP) | City of Norfolk | 2020-02-25 | 2020-02-25 | 2020-02-25 | false |
| Ord. No. 48814 (STR standards update) | City of Norfolk | 2022-06-28 | 2022-06-28 | 2022-06-28 | false |
| HB 518 / SB 651 (Ch. 7 & 640) | Commonwealth of Virginia | 2022-03-02 | 2022-10-01 | 2022-10-01 | false |
| Ord. No. 48924 (lodging intermediary TOT) | City of Norfolk | 2022-09-13 | 2022-10-01 | 2022-10-01 | false |
| SB 544 / Ch. 700 & 792 | Commonwealth of Virginia | 2024-04-17 | 2024-07-01 | 2024-07-01 | false |
| Ord. No. 49866 (West Freemason VR removal) | City of Norfolk | 2025-02-25 | 2025-02-25 | 2025-02-25 | false |
| Ord. No. 50,139 (STR room tax per bedroom) | City of Norfolk | 2025-10-07 | 2026-01-01 | 2026-01-01 | false |

## Airbnb dates

- **airbnb_tax_collection_date:** `2022-10-01` (municipal lodging/TOT via statewide intermediary mandate + Ord. 48924; not earlier state-sales-tax-only collection)
- **airbnb_data_sharing_date:** `2022-10-01` (Va. Code § 58.1-3826 monthly address/gross-receipts reports; mirrored in Ord. 48924)

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Norfolk entry)
- Script: `agent/scripts/update_norfolk_str_regulations.py`
- Backup: `AGENT_DATA_PATH/str_regulations.json.pre_norfolk.bak`
- Report: `agent/reports/2026-08-08-norfolk-str-legislative-history.md`

## Key sources

- Norfolk City Council minutes/IQM2: Oct. 23, 2018 STR ZTA; Ord. 47894 (2020-02-25); Ord. 48814 (2022-06-28); Ord. 48924 (2022-09-13; eff. 2022-10-01); Ord. 49866 (2025-02-25); Ord. 50,139 (2025-10-07; eff. 2026-01-01)
- City of Norfolk Planning presentations (May/Oct 2018 STR briefings); STR program pages; Homestay/Vacation Rental Tax / Fiduciary Taxes pages
- Virginian-Pilot (2018-10-24) on Oct. 23 adoption and Jan. 1, 2019 program start; Avalara Sept. 2022 Norfolk tax note; Airbnb newsroom “Supporting Virginia’s new tax collection and remittance law”
- Virginia LIS: SB 1578 (2017 Ch. 741); HB 518 / SB 651 (2022 Ch. 7 & 640); SB 544 (2024 Ch. 700 & 792); Va. Code §§ 15.2-983, 58.1-3826; Virginia Tax Ruling 22-144
