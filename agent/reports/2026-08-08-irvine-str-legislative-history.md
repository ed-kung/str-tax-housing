# Irvine, CA — Short-term rental legislative history

**Summary:** Irvine’s dedicated STR framework is **Zoning Ordinance Chapter 3-25**, created by **Ordinance No. 18-05** (adopted April 24, 2018; effective May 24, 2018), which bans residential short-term rentals (≤30 consecutive days) and advertising thereof as an express restatement of the City’s prior hotel/motel-use prohibition. Companion **Ord. 18-06** set elevated STR administrative fines ($1,500 / $3,000 / $5,000). **Ord. 21-01** (adopted Jan. 26, 2021; effective Feb. 25, 2021) bars hosting platforms from completing Irvine STR bookings and requires platform reporting. **Ord. 22-12** (Aug. 2022) made technical updates to violation language. No Airbnb municipal TOT collection or City Portal / direct compliance data connection found.

## City processed

- **City:** Irvine, California  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 62)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary framework is municipal Chapter 3-25 (Ord. 18-05).** Before 2018 the City treated residential STRs as prohibited hotel/motel uses (documented in a May 24, 2016 City Council STR study session). Ord. 18-05 codified an explicit ban, advertising prohibition, nuisance declaration, and enforcement remedies. No STR permit/registration pathway exists for residential units.

2. **Enforcement package.** Ord. 18-06 (same adoption date) created STR-specific elevated infraction fines. Proactive listing enforcement intensified around May 2019 with a Host Compliance contract (staff later reported listings falling from ~1,500 to ~500+). Ord. 21-01 then imposed platform booking bans and reporting duties. Ord. 22-12 clarified Chapter 3-25 violation/prosecution language without changing the ban.

3. **Airbnb tax collection:** **null** — Airbnb’s California occupancy-tax list omits Irvine; City TOT (8%) + IHID (2%) materials address hotel/motel operators; residential STRs are illegal.

4. **Airbnb data sharing:** **null** — enforcement uses third-party listing scrapers and Ord. 21-01’s unilateral platform duties; no City Portal or voluntary Airbnb data connection identified.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Ord. 18-05 (Ch. 3-25 STR ban) | City of Irvine | 2018-04-24 | 2018-05-24 | 2018-05-24 | true |
| Ord. 18-06 (elevated STR fines) | City of Irvine | 2018-04-24 | 2018-05-24 | 2018-05-24 | false |
| Ord. 21-01 (platform booking/reporting) | City of Irvine | 2021-01-26 | 2021-02-25 | 2021-02-25 | false |
| Ord. 22-12 (technical updates to §3-25-5) | City of Irvine | 2022-08-09 | 2022-09-08 | 2022-09-08 | false |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Irvine entry)
- Script: `agent/scripts/update_irvine_str_regulations.py`
- Report: `agent/reports/2026-08-08-irvine-str-legislative-history.md`

## Key sources

- City of Irvine City Council minutes — April 24, 2018 (second reading/adoption of Ords. 18-05 and 18-06); January 12 and January 26, 2021 (Ord. 21-01 first/second reading)
- Irvine Zoning Ordinance Chapter 3-25 (Municode) — Ord. citations 18-05, 21-01, 22-12
- City Council staff report (Jan. 12, 2021) — platform ordinance background; Host Compliance contract (Dec. 2018) and May 2019 proactive enforcement counts
- City Council May 24, 2016 STR study-session presentation — pre-2018 hotel/motel prohibition interpretation
- Avalara MyLodgeTax (Feb. 23, 2021) — secondary coverage of platform transaction ban (effective-date reporting differed from 30-day rule after Jan. 26 adoption; Municode/council minutes control)
- Airbnb Help article 2297 (CA occupancy tax collection list) — Irvine not listed; article 2991 (Irvine, CA) — long-term (30+ night) hosting guidance only
- City of Irvine Transient Occupancy Tax pages — hotel/motel operator remittance
