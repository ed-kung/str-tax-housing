# Riverside, CA — Short-term rental legislative history

**Summary:** The City of Riverside had no dedicated STR ordinance until **Ordinance No. 7678** (adopted Aug. 6, 2024; effective Sept. 5, 2024) added **RMC Chapter 5.55**, requiring a Business Tax Certificate, occupancy/nuisance/local-contact rules, and broker TOT remittance duties. **Measure V** (Nov. 2, 2010) raised municipal TOT from 11% to 13% in phases (first increase July 1, 2012). Airbnb began collecting City TOT under a VCA on **2018-12-01** (may later have lapsed; hosts currently self-remit). No City Portal / direct compliance data connection found. Riverside County Ord. 927 applies only outside city limits.

## City processed

- **City:** Riverside, California  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 60)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Primary STR framework is municipal Chapter 5.55 (Ord. 7678).** Introduced July 16, 2024; adopted August 6, 2024; effective September 5, 2024. Staff confirmed that before adoption the City lacked STR-specific operational standards and relied on general nuisance laws. Chapter 5.55 is a relatively light framework (business tax certificate, not a separate STR permit; no citywide unit cap or primary-residence rule).

2. **TOT.** Measure V (voter-approved Nov. 2, 2010) increased TOT under RMC Chapter 5.32 from 11% → 12% (July 1, 2012) → 13% (July 1, 2014). Chapter 5.32 already covered dwelling/tourist-home stays under 30 days.

3. **Airbnb tax collection:** **2018-12-01** — City Council approved an Airbnb Voluntary Collection Agreement on Oct. 16, 2018 with collection starting Dec. 1, 2018 (municipal 13% TOT). Airbnb’s current CA tax list and Riverside host help article indicate hosts now self-remit City TOT (VCA may have terminated); Dec. 1, 2018 remains the first documented start.

4. **Airbnb data sharing:** **null** — 2018 VCA was anonymized aggregate tax remittance only; no City Portal / listing verification feed identified for the city.

5. **County vs city.** Riverside County Ordinance 927 (and amendments) regulate unincorporated areas only and were excluded.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Measure V (TOT increase, RMC §5.32.020) | City of Riverside (voters) | 2010-11-02 | 2012-07-01 | 2012-07-01 | false |
| Ord. 7678 (Ch. 5.55 STR framework) | City of Riverside | 2024-08-06 | 2024-09-05 | 2024-09-05 | true |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Riverside entry)
- Script: `agent/scripts/update_riverside_str_regulations.py`
- Report: `agent/reports/2026-08-08-riverside-str-legislative-history.md`

## Key sources

- City of Riverside Legistar Files 24-2034 / 24-2240 (Chapter 5.55 introduction July 16, 2024; adoption Aug. 6, 2024) and attached ordinance / staff report
- City of Riverside Legistar File 18-3339 (Airbnb VCA, Oct. 16, 2018) — agreement text and Finance staff report
- Press-Enterprise coverage of Oct. 16, 2018 Airbnb TOT vote (Dec. 1 start)
- Measure V materials / RMC §5.32.020 TOT ordinance (riversideca.gov/tot); City audit describing Nov. 2, 2010 approval and phased rate increases
- Airbnb Help: California occupancy tax collection list (Riverside County unincorporated only); Airbnb Riverside, CA hosting guidance (host self-remit of City TOT; cites Chapter 5.55)
