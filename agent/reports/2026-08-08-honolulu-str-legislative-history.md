# Honolulu, HI — Short-term rental legislative history

**Summary:** Honolulu’s modern STR framework is **Ordinance 19-18 (2019)**, which layered advertising bans, high fines, limited hosted B&B registration, and platform duties onto 1980s resort/NUC zoning. **Ordinance 22-7 (2022)** tried to raise the minimum rental period to 90 days but was blocked by federal injunction before/at effectiveness. State **Act 1 (2021)** enabled and **Ordinance 21-33** imposed a 3% municipal OTAT (host-remitted; Airbnb does not collect). Airbnb–City MOUs effective **2020-11-18** created TMK/TAT listing fields and a delisting channel. Later ordinances (24-14, 25-2, 25-52) and **Act 17 (2024)** refined registration and county zoning authority.

## City processed

- **City:** Honolulu, Hawaii  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 54)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Pre-2008 baseline (context only):** 1980s LUO rules generally barred under-30-day vacation rentals outside resort areas and limited grandfathered NUCs; no major new binding STR ordinance identified between 2008 and Ordinance 19-18.

2. **Ordinance 19-18 (signed 2019-06-25; effective/enforced 2019-08-01)** is the primary modern framework: ad bans, prima facie advertising evidence, steep fines, limited hosted B&Bs, continued TVU restrictions outside resort/designated areas, platform compliance duties.

3. **Ordinance 20-30 (2020-09-17)** delayed B&B/platform registration start from 2020-10-01 to 2021-04-30; advertising enforcement continued.

4. **Ordinance 22-7 (signed 2022-04-26; slated 2022-10-23)** raised the minimum to 90 days; preliminary injunction 2022-10-13 and permanent injunction (Dec 2023) blocked the core 30–89-day ban → `enforcement_date: null`. Resort-area registration proceeded (DPP online registration from 2022-10-24).

5. **Taxes:** Act 1 (veto override 2021-07-06; eff. 2021-07-01) authorized county TAT; Ordinance 21-33 created 3% OTAT effective 2021-12-14. **Airbnb tax collection date: null** (hosts remit OTAT/GET/TAT).

6. **Airbnb data sharing: 2020-11-18** — MOU effective date (announced 2020-11-24); TMK/TAT fields and delisting cooperation; monthly reports incompletely enforced per later reporting.

7. **Act 17 (2024-05-03)** clarified county power to regulate duration/amortize transient accommodations after the HILSTRA litigation. Ordinances **24-14**, **25-2**, and **25-52** adjusted registration paperwork and recodified STR use standards in the LUO rewrite.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Ord. 19-18 (Bill 89) | City & County of Honolulu | 2019-06-25 | 2019-08-01 | 2019-08-01 | true |
| Ord. 19-32 | City & County of Honolulu | 2019-12-15 | 2020-07-01 | 2020-07-01 | false |
| Ord. 20-30 (Bill 50) | City & County of Honolulu | 2020-09-17 | 2020-09-17 | 2020-09-17 | false |
| Act 1, 1st Spec. Sess. 2021 (HB 862) | State of Hawaii | 2021-07-06 | 2021-07-01 | 2021-07-01 | false |
| Ord. 21-33 (Bill 40) | City & County of Honolulu | 2021-12-14 | 2021-12-14 | 2021-12-14 | false |
| Ord. 22-7 (Bill 41) | City & County of Honolulu | 2022-04-26 | 2022-10-23 | null | false |
| Act 17 (SB 2919) | State of Hawaii | 2024-05-03 | 2024-05-03 | 2024-05-03 | false |
| Ord. 24-14 (Bill 53) | City & County of Honolulu | 2024-06-25 | 2024-07-26 | 2024-07-26 | false |
| Ord. 25-2 (Bill 64) | City & County of Honolulu | 2025-01-03 | 2025-09-30 | 2025-09-30 | false |
| Ord. 25-52 | City & County of Honolulu | 2025-11-05 | 2025-11-05 | 2025-11-05 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Honolulu entry)
- Script: `agent/scripts/update_honolulu_str_regulations.py`
- Report: `agent/reports/2026-08-08-honolulu-str-legislative-history.md`

## Key sources

- City Council / hnldoc: Ordinance 19-18 status; Bill 50 → Ordinance 20-30 public notice (SA1296056); Bill 40 → Ordinance 21-33; Bill 41 → Ordinance 22-7; Bill 64 → Ordinance 25-2; DPP memo on Ordinances 24-14 / 25-2
- Honolulu DPP LUO ordinance index; STR FAQ (registration from 2022-10-24; OTAT remittance contacts)
- Star-Advertiser: Mayor signs Bill 89 (2019-06-26); Airbnb/Expedia MOU (2020-11-24/25); 90-day injunction coverage (2024-01-01)
- Civil Beat: Aug. 1, 2019 digital stings; 2025 platform-report enforcement gaps
- U.S. District Court D. Haw.: HILSTRA preliminary injunction (2022-10-13); permanent injunction (Dec 2023)
- State: Act 1, 1st Spec. Sess. 2021 (HB 862 veto override 2021-07-06); Act 17 / Gov. Green signing (2024-05-03); SLH 2024 Act 17 PDF
- City BFS OTAT announcement/FAQs; Avalara MyLodgeTax Honolulu; Airbnb help article 894 (Honolulu)
