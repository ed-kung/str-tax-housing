# Tucson, AZ short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Tucson, AZ (first unchecked city). Tucson has never enacted a dedicated STR land-use/permit ordinance; binding regulation is Arizona’s statewide preemption and tax framework (SB 1350 → HB 2672 → SB 1168). The city’s main STR-specific action is Ordinance 12215 (Dec. 16, 2025; eff. March 1, 2026), creating a 10% occupational license tax on non-hotel vacation/short-term rentals. Airbnb has collected Tucson municipal lodging taxes via the ADOR partnership since **2017-01-01**; no Airbnb–city data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Tucson, AZ (index 32).
- Reviewed Arizona chaptered laws (SB 1350 / Ch. 208; HB 2672 / Ch. 240; SB 1168 / Ch. 343), ADOR Model City Tax Code Tucson profile and rate updates, Airbnb Arizona/Tucson help articles, and Tucson.com coverage of the Dec. 16, 2025 tax package.
- Confirmed Tucson has no stand-alone STR permit/registry (business license + statewide TPT license only); SB 1348 (2020 Tax Corrections Act) was excluded as non-substantive for STR policy.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| City STR code | No dedicated STR permit, primary-residence, host-presence, or day-cap ordinance. Airbnb’s Tucson help page points to general UDC/business-license/tax rules only. |
| State preemption | SB 1350 (eff. 2017-01-01) barred local STR bans and classification/use/occupancy regulation; HB 2672 (eff. 2019-08-27) added contact-info authority, nonresidential-use ban, TPT display; SB 1168 (eff. 2022-09-24) authorized limited local permits/insurance/neighbor notice and higher fines—Tucson has not used the permit authority. |
| City tax | Historical hotel/transient occupational tax (6% + bed surtax) applied to STRs under hotel code 044; Ord. 12215 (2025-12-16; eff. 2026-03-01) created 10% non-hotel STR rate (code 544). |
| Airbnb tax | **2017-01-01** — ADOR/Airbnb voluntary OLM collection of state, county, and local transient taxes, including Tucson’s municipal lodging tax. |
| Airbnb data sharing | **null** — remittance via ADOR only; no city portal/API/delisting channel; no Tucson STR permit program. |

## Legislative history recorded

1. **SB 1350 (Laws 2016, Ch. 208)** — State of Arizona — Passage 2016-05-12; effective/enforced 2017-01-01 — `primary_framework`: true  
2. **HB 2672 (Laws 2019, Ch. 240)** — State of Arizona — Passage 2019-05-21; effective/enforced 2019-08-27 — `primary_framework`: false  
3. **SB 1168 (Laws 2022, Ch. 343)** — State of Arizona — Passage 2022-07-06; effective/enforced 2022-09-24 — `primary_framework`: false  
4. **Ord. 12215 / 12218** — City of Tucson — Passage 2025-12-16; effective/enforced 2026-03-01 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Tucson entry)
- Report: `agent/reports/2026-08-08-tucson-str-legislative-history.md`
