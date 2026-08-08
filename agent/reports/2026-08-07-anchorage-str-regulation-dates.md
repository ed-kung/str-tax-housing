# Anchorage, AK short-term rental regulation dates

## Summary

Filled in the Anchorage, AK row of `AGENT_DATA_PATH/str_regulations.csv`, the first row lacking `agent_checked == True`. Anchorage is a late regulator: its first substantive short-term-rental (STR) ordinance is AO 2025-115(S-2), passed by the Assembly on 2025-12-16 and effective 2026-05-01. An earlier licensing ordinance passed in March 2024 but was vetoed and never took effect. Airbnb has been collecting and remitting Anchorage's 12% room tax since 2016-08-01 under a voluntary hosting-platform agreement, roughly nine years before the city regulated STRs directly. Confidence recorded as **High** because all three dates come from official Municipality of Anchorage ordinance text or Treasury Division reports.

## Values written

| Field | Value |
| --- | --- |
| `passage_date` | 2025-12-16 |
| `effective_date` | 2026-05-01 |
| `airbnb_cooperation_date` | 2016-08-01 |
| `agent_confidence` | High |
| `agent_checked` | True |

## Findings

### Passage and effective dates

**AO 2025-115(S-2)** amended Anchorage Municipal Code to add new Chapter 10.90 requiring owners to register STRs with the Municipal Clerk and display the registration number on hosting-platform listings; amended Title 12 tax-reporting requirements for hosting platforms; amended Title 21 to explicitly allow STRs in all residential zoning districts and some commercial districts; and removed bed and breakfasts as a separate use type.

- Passed and approved by the Anchorage Assembly on **December 16, 2025**, by a 10-2 vote (ordinance signature block; vote count per Alaska Business Magazine).
- Section 15 of the ordinance: "This ordinance shall be effective May 1 [February 9], 2026" — the effective date was amended to **May 1, 2026** from an earlier February 9, 2026 proposal.
- Registration portal opened May 1, 2026 with a 90-day grace period; registration deadline July 30, 2026. AMC 10.90.020F barred fines until 90 days after May 1, 2026.
- AR 2026-213 (passed July 21, 2026) extended the pre-fine compliance window for owners served a notice of violation through September 30, 2026.

### Prior failed attempt (not used as passage date)

**AO 2023-110(S-1)** would have created an STR licensing program with fees ($200–$400), insurance requirements, a 24/7 responsible manager, and a fine schedule. The Assembly passed it 7-5 on March 19, 2024, but Mayor Dave Bronson vetoed it on March 20, 2024 (veto given date March 22, 2024 on the ordinance document). Sponsors said an override was not expected and the matter was dead. Since it never became law, it is not the passage date.

### Airbnb cooperation

Anchorage's 12% room tax (AMC 12.20) long predates Airbnb. Relevant sequence:

- **AO 2016-66** (approved June 21, 2016, effective immediately upon passage) created AMC 12.20.031, "Registered hosting platforms," establishing a **voluntary** registration/collection/remittance framework specifically to bring platforms like Airbnb into room tax compliance. The Assembly presentation confirms Treasury had been in negotiations with Airbnb for several months.
- Anchorage Daily News (July 9, 2016) reported the city was finalizing an agreement with Airbnb to collect the bed tax at booking, slated to take effect August 1, with the Municipal Treasurer projecting ~$200,000 in added annual revenue.
- MOA Treasury Division quarterly room tax summary reports (2016 through 2026 editions) state: "Airbnb.com began collecting and remitting tax on transactions entered into on or after August 1, 2016." This official confirmation is the basis for `airbnb_cooperation_date = 2016-08-01`.
- HomeAway began collecting and remitting on November 1, 2019.
- **AO 2019-99(S)** (effective August 20, 2019) converted the hosting-platform agreement from voluntary to mandatory, catalyzed by *South Dakota v. Wayfair*.
- **AO 2024-81(S)** (effective January 1, 2025) added supplemental room-level data reporting requirements for registered hosting platforms.

Because the room tax ordinances are tax-collection measures rather than STR regulation, they are recorded in the Airbnb cooperation column, not as the passage date.

### Note for the analysis

Anchorage's treatment date falls after the end of the currently available tax panel (FiSC data runs through 2023), so for the difference-in-differences design Anchorage functions as a never-treated / not-yet-treated control city. The 2016 Airbnb tax agreement is, however, within sample if platform tax collection is of independent interest.

## Sources

- AO 2025-115(S-2), As Corrected: https://www.muni.org/Departments/Assembly/SiteAssets/Pages/FOCUS-Housing/AO%202025-115(S-2),%20As%20Corrected.pdf
- STR Registration FAQs, Municipal Clerk: https://www.muni.org/Departments/Assembly/Clerk/Licensing/SiteAssets/Pages/Short-Term-Rental-Registration-Program/2026-0224%20STR%20Registration%20FAQs%20for%20Webpage.pdf
- AR 2026-213, As Amended: https://www.muni.org/Departments/Assembly/Clerk/Licensing/SiteAssets/Pages/Short-Term-Rental-Registration-Program/AR%202026-213,%20As%20Amended.pdf
- AO 2023-110(S-1) with mayoral veto: https://www.muni.org/Lists/AssemblyListDocuments/Attachments/1331878/AO%202023-110(S-1),%20As%20Amended%20With%20Mayoral%20Veto.pdf
- AO 2016-66, As Amended: https://www.muni.org/Lists/AssemblyListDocuments/Attachments/631964/AO%202016-066,%20As%20Amended%20OCR.pdf
- AO 2019-99(S), As Amended: https://www.muni.org/Lists/AssemblyListDocuments/Attachments/622365/AO%202019-099(S),%20As%20Amended%20OCR.pdf
- AO 2025-97 worksession packet (legislative history of Anchorage STR actions): https://www.muni.org/Departments/Assembly/Documents/AO%202025-97%20Worksession.pdf
- MOA Room Tax Returns Summary by Quarter, 2016: https://www.muni.org/Departments/finance/treasury/programtaxes/roomtax/Documents/Tax%20summary%20reports/tax-summary-2016.pdf
- AMC Chapter 10.90 (eCode360): https://ecode360.com/49354271
- AMC Chapter 12.20 Room Tax (eCode360): https://ecode360.com/49358495
- ADN, "As Airbnb continues to grow, Alaska hotels are wary" (2016-07-09)
- ADN, "Bronson vetoes Assembly ordinance with new rules for Airbnbs..." (2024-03-20)
- Alaska Business Magazine, "Anchorage Short-Term Rental Registration Starts in May"

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.csv` (Anchorage row only)
- This report: `agent/reports/2026-08-07-anchorage-str-regulation-dates.md`
