# Chesapeake, VA — Short-term rental legislative history

**Summary:** Chesapeake has no post-Airbnb dedicated STR ordinance. Airbnb-style lodging is regulated as **bed and breakfast/tourist home establishments** under **Ord. No. 01-O-098 (TA-Z-01-18)** (adopted 2001-10-16; effective/enforced **2001-11-15**), which confines legal operation to the **A-1** and **HC** districts with a City Council **CUP**, a **10-days-in-30** stay limit, and related operating standards. State law added registry enabling (**SB 1578 / Ch. 741**, 2017), platform local TOT collection and monthly address/gross-receipts reporting (**HB 518 / SB 651**, effective **2022-10-01**), and limits on *new* primary-residence CUP mandates (**SB 544 / Ch. 700 & 792**, 2024) without repealing Chesapeake’s 2001 framework. City **Ord. 25-O-038** raised the lodging flat tax from $1 to $2 (eff. **2025-07-01**); **Ord. 25-O-052** clarified intermediary monthly reporting in § 30-354. Airbnb municipal TOT collection and monthly locality data reporting for Chesapeake begin **2022-10-01**.

## City processed

- **City:** Chesapeake, Virginia  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 88)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary framework (2001; still operative).** Ord. 01-O-098 / TA-Z-01-18 defines B&B/tourist homes and adds Zoning Ordinance §§ 13-1600 et seq.: CUP-only in A-1 or HC; max guest stay 10 days within any 30-day period; guest register; parking, residential-character, and HC building-date limits. No later city ordinance created a separate Airbnb/STR code chapter.

2. **State registry enabling (2017).** SB 1578 (§ 15.2-983) authorized local STR registries; Chesapeake did not adopt a separate registry ordinance and continues CUP + Commissioner of the Revenue lodging-tax / business-license registration.

3. **Platform taxes & data (2022-10-01).** HB 518/SB 651 require intermediaries to collect/remit local TOT and file monthly address/gross-receipts reports. Airbnb previously collected Virginia sales tax under voluntary arrangements; municipal Chesapeake lodging/TOT collection begins with the statewide mandate.

4. **2024 primary-residence CUP limit.** SB 544 (Ch. 700 & 792) bars *new* post-2023 local CUP/special-exception requirements for owner primary-residence STRs; it does not invalidate Chesapeake’s pre-2024 Ord. 01-O-098 rules.

5. **2025 lodging-tax adjustments.** Ord. 25-O-038 ($1→$2 flat per night) and Ord. 25-O-052 (intermediary reporting clarification) amend City Code § 30-354 effective 2025-07-01. Note: City Code Article XIV “Short-Term Rental Tax” taxes tangible personal property rentals, not lodging/Airbnb stays.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Ord. No. 01-O-098 (TA-Z-01-18) B&B/tourist home | City of Chesapeake | 2001-10-16 | 2001-11-15 | 2001-11-15 | true |
| SB 1578 / Ch. 741 (§ 15.2-983) | Commonwealth of Virginia | 2017-03-24 | 2017-07-01 | 2017-07-01 | false |
| HB 518 / SB 651 (Ch. 7 & 640) | Commonwealth of Virginia | 2022-03-02 | 2022-10-01 | 2022-10-01 | false |
| SB 544 / Ch. 700 & 792 | Commonwealth of Virginia | 2024-04-17 | 2024-07-01 | 2024-07-01 | false |
| Ord. No. 25-O-038 (flat TOT $1→$2) | City of Chesapeake | 2025-05-13 | 2025-07-01 | 2025-07-01 | false |
| Ord. No. 25-O-052 (intermediary reporting) | City of Chesapeake | 2025-06-10 | 2025-07-01 | 2025-07-01 | false |

## Airbnb dates

- **airbnb_tax_collection_date:** `2022-10-01` (municipal lodging/TOT via statewide intermediary mandate; not earlier state-sales-tax-only collection)
- **airbnb_data_sharing_date:** `2022-10-01` (Va. Code § 58.1-3826 monthly address/gross-receipts reports; later clarified locally by Ord. 25-O-052)

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Chesapeake entry)
- Script: `agent/scripts/update_chesapeake_str_regulations.py`
- Report: `agent/reports/2026-08-08-chesapeake-str-legislative-history.md`

## Key sources

- Chesapeake Zoning Ordinance §§ 13-1600 et seq. and Art. 3 definition (Zoneomics/Municode cites for Ord. 01-O-098, 10-16-01; effective date of TA-Z-01-18 = 2001-11-15); Ord. 10-O-127 administrative title changes only
- City of Chesapeake Commissioner of the Revenue lodging tax materials (8% + flat per-night); City Code Ch. 30 Art. XI (TOT) vs Art. XIV (personal-property short-term rental tax)
- City Council minutes: Ord. 25-O-038 (2025-05-13; eff. 2025-07-01); Ord. 25-O-052 (2025-06-10 Consent Agenda; eff. 2025-07-01)
- Virginia LIS: SB 1578 (2017 Ch. 741); HB 518 / SB 651 (2022 Ch. 7 & 640); SB 544 (2024 Ch. 700 & 792); Va. Code §§ 15.2-983, 58.1-3826
- Virginia Tax Ruling 22-144; Airbnb newsroom “Supporting Virginia’s new tax collection and remittance law”; Avalara Oct. 2022 intermediary guidance
