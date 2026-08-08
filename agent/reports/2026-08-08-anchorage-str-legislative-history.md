# Anchorage, AK — Short-term rental legislative history

**Summary:** Until 2025 Anchorage regulated Airbnb-style lodging mainly through the municipal **12% room/bed tax** and hosting-platform remittance rules (**AO 2016-66**, **AO 2019-99(S)**), not land-use registration. A March 2024 licensing ordinance (**AO 2023-110**) was vetoed and never became law. **AO 2024-81(S)** briefly required platform STR data with tax returns (eff. 2025-01-01) but was not complied with and was later repealed. **AO 2025-115(S-2)** (eff. **2026-05-01**) is the primary STR framework: free annual registration, listing-number display, platform booking bans for unregistered units, and zoning that expressly allows STRs while absorbing the old bed-and-breakfast use. Airbnb municipal tax collection began about **2016-08-01**; no direct Airbnb–city compliance data connection was found.

## City processed

- **City:** Anchorage, Alaska  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 73)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **AO 2016-66 (2016-06-21)** created AMC 12.20.031 for voluntary registered hosting platforms to collect/remit the 12% room tax; operators using only a registered platform were largely relieved of individual room-tax registration for those bookings.

2. **Airbnb tax collection ~2016-08-01.** ADN (2016-07-10) quoted Treasurer Dan Moore that an Airbnb agreement to collect the municipal bed tax at booking was slated for August 1, 2016—municipal tax (Alaska has no state lodging tax).

3. **AO 2019-99(S) (2019-08-20)** made registration/collection/remittance mandatory for platforms that accept guest payment (post-*Wayfair*), replacing the voluntary-agreement model.

4. **AO 2023-110(S-1)** licensing program passed March 19, 2024 but was vetoed March 20, 2024 with no override—excluded from legislative history as non-binding.

5. **AO 2024-81(S) (passed 2024-09-10; eff. 2025-01-01)** required supplemental STR operator/unit data with platform tax returns. Assembly materials later said platforms did not provide the data; **AO 2025-115** deleted the requirement. `enforcement_date` set to null.

6. **AO 2025-115(S-2) (passed 2025-12-16; eff. 2026-05-01)** is the primary STR framework (AMC Ch. 10.90 + Title 21 STR use). Fines delayed until 90 days after effective date (**2026-07-30**). Airbnb’s host help article aligns with registration display and post-grace blocking of noncompliant listings.

7. **Airbnb data sharing:** null — no City Portal/API; AO 2024-81 data mandate unsuccessful and repealed; aggregate tax remittance and platform self-enforcement of registration numbers are not treated as a dated direct city data connection.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| AO 2016-66, As Amended | Municipality of Anchorage | 2016-06-21 | 2016-06-21 | 2016-06-21 | false |
| AO 2019-99(S), As Amended | Municipality of Anchorage | 2019-08-20 | 2019-08-20 | 2019-08-20 | false |
| AO 2024-81(S), As Amended | Municipality of Anchorage | 2024-09-10 | 2025-01-01 | null | false |
| AO 2025-115(S-2), Corrected | Municipality of Anchorage | 2025-12-16 | 2026-05-01 | 2026-07-30 | true |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Anchorage entry)
- Script: `agent/scripts/update_anchorage_str_regulations.py`
- Report: `agent/reports/2026-08-08-anchorage-str-legislative-history.md`

## Key sources

- Municipality of Anchorage — AO 2016-66, As Amended (approved 2016-06-21); ADN coverage 2016-06-22 and 2016-07-10
- Municipality of Anchorage — AO 2019-99(S), As Amended (approved 2019-08-20)
- Municipality of Anchorage / DocumentCloud — AO 2024-81(S); Alaska's News Source 2024-09-12; ADN 2024-09-02
- ADN 2024-03-20 — Bronson veto of AO 2023-110(S-1) licensing program
- Municipality of Anchorage — AO 2025-115(S-2), Corrected; AMC Ch. 10.90 (ecode360); STR Registration FAQs; AR 2026-213
- ADN 2025-12-17 — Assembly passes registration tracking, rejects 5% STR tax ballot
- Airbnb Help — Anchorage, AK hosting rules (registration / July 30, 2026 grace)
- AO 2025-97 worksession PDF — legislative chronology and AO 2024-81 non-response note
