# Richmond, VA — Short-term rental legislative history

**Summary:** Richmond’s primary city STR framework is **Ord. No. 2019-343** (passed **2020-06-22**; effective/enforced **2020-07-01**), which first permitted STRs as an accessory use with a biennial permit, primary-residence (185+ days) rule, and safety/occupancy standards—replacing a prior zoning posture in which STRs were not permitted except via Special Use Permit. Major updates are **Ord. No. 2023-151** (municipal 8% TOT extended to STRs/intermediaries, **2023-07-01**) and **Ord. No. 2023-235** (**2023-09-25**; fee to $600; multifamily caps; primary-residence limited to residential districts). State law enabled local registries (**SB 1578**, 2017), mandated platform local TOT collection and monthly address reporting (**HB 518/SB 651**, **2022-10-01**), and limited *new* primary-residence CUP rules (**SB 544**, 2024). Airbnb municipal TOT collection and monthly locality data reporting for Richmond STRs begin **2023-07-01** (when city code first taxed STRs), not the earlier statewide intermediary effective date.

## City processed

- **City:** Richmond, Virginia  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 97)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary framework (2020).** Ord. No. 2019-343 legalized STRs citywide as an accessory use with a biennial Certificate of Zoning Compliance (~$300), owner-operator and 185-day primary-residence requirements, unlimited nights, whole-home or room rentals, and safety/nuisance rules. City press release (Aug. 7, 2020) and STR program page confirm July 1, 2020 effective/portal launch.

2. **Municipal TOT & platform duties (2023-07-01).** Ord. No. 2023-151 replaced the hotel-only (10+ bedroom) lodging-tax article so the 8% TOT covers short-term accommodations; intermediaries collect/remit and file monthly address/gross-receipts reports. Desired/express effective date July 1, 2023.

3. **2023 zoning update (Ord. 2023-235).** Kept primary residence in residential districts (DMV/registrar verification), removed it in non-residential districts, capped multifamily STRs (lesser of 10 or 1/3 of units), set eight-adult occupancy cap, and raised the biennial fee to $600.

4. **State context.** SB 1578 (2017) enabled local registries; HB 518/SB 651 (eff. 2022-10-01) created statewide intermediary TOT/reporting duties that Richmond implemented for STRs only after Ord. 2023-151; SB 544 (2024) constrains new primary-residence CUP rules without undoing Richmond’s existing administrative permit framework.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| SB 1578 / Ch. 741 (§ 15.2-983) | Commonwealth of Virginia | 2017-03-24 | 2017-07-01 | 2017-07-01 | false |
| Ord. No. 2019-343 (STR zoning framework) | City of Richmond | 2020-06-22 | 2020-07-01 | 2020-07-01 | true |
| HB 518 / SB 651 (Ch. 7 & 640) | Commonwealth of Virginia | 2022-03-02 | 2022-10-01 | 2022-10-01 | false |
| Ord. No. 2023-151 (STR transient occupancy tax) | City of Richmond | 2023-05-22 | 2023-07-01 | 2023-07-01 | false |
| Ord. No. 2023-235 (STR zoning revisions) | City of Richmond | 2023-09-25 | 2023-09-25 | 2023-09-25 | false |
| SB 544 / Ch. 700 & 792 | Commonwealth of Virginia | 2024-04-17 | 2024-07-01 | 2024-07-01 | false |

## Airbnb dates

- **airbnb_tax_collection_date:** `2023-07-01` (municipal 8% TOT on STRs via Ord. 2023-151; not earlier state-sales-tax-only collection, and not Oct. 1, 2022 statewide intermediary date because Richmond’s tax base excluded STRs until July 2023)
- **airbnb_data_sharing_date:** `2023-07-01` (monthly intermediary address/gross-receipts reports under Ord. 2023-151 / Va. Code § 58.1-3826 as applied to Richmond STR TOT)

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Richmond entry)
- Script: `agent/scripts/update_richmond_str_regulations.py`
- Backup: `AGENT_DATA_PATH/str_regulations.json.pre_richmond.bak`
- Report: `agent/reports/2026-08-08-richmond-str-legislative-history.md`

## Key sources

- City of Richmond press release (Aug. 7, 2020): STR regulations effective July 1 after June 22 Council passage
- RVA.gov Short-Term Rentals page (Ord. 2019-343 background; Ord. 2023-235 adopted Sept. 25, 2023; current rules)
- Richmond Legistar: ORD. 2019-343 (final action 2020-06-22); ORD. 2023-151 (final action 2023-05-22; § 4 effective July 1, 2023); ORD. 2023-235 (adopted 2023-09-25; effective upon adoption)
- City Finance O&R for ORD. 2023-151 (purpose: extend TOT to STRs/intermediaries; desired effective date July 1, 2023)
- Avalara (July 11, 2023): Richmond 8% lodging tax on STRs as of July 1, 2023
- Airbnb newsroom: “Supporting Virginia’s new tax collection and remittance law” (HB 518)
- Virginia LIS / Tax Ruling 22-144: SB 1578 (2017 Ch. 741); HB 518 / SB 651 (2022 Ch. 7 & 640; eff. 2022-10-01); SB 544 (2024 Ch. 700 & 792); Va. Code §§ 15.2-983, 58.1-3826
- VPM (2020-06-22) and Richmond BizSense (2019) contemporaneous coverage of Ord. 2019-343 rules
