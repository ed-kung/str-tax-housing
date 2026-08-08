# Santa Ana, CA — Short-term rental legislative history

**Summary:** Santa Ana had no dedicated STR ordinance until **2024**, when it expressly banned Airbnb-style rentals under 30 days. **Urgency Ord. NS-3060** (April 2, 2024) and companion **NS-3061** (adopted April 16; eff. May 16, 2024) added SAMC Article XXI. After CEQA litigation impaired enforcement of the April package, the City reenacted the ban as **Ord. NS-3072** (adopted Dec. 3, 2024; eff. Jan. 2, 2025), with a companion **Nov. 20, 2024 administrative-fine resolution**. On **April 20, 2026**, Orange County Superior Court ordered NS-3072 set aside for CEQA noncompliance. No Airbnb municipal TOT collection or direct city–Airbnb data connection found.

## City processed

- **City:** Santa Ana, California  
- **Source file:** `AGENT_DATA_PATH/str_regulations.json` (index 64)  
- **Marked:** `agent_checked: 1`

## Main findings

1. **Pre-2024 practice was permissive zoning, not an STR statute.** The City long treated STRs as unauthorized because they were not listed uses under SAMC §41-190. That general zoning theory is not recorded as a post-2008 STR-specific legislative act; explicit Article XXI bans begin in April 2024.

2. **Primary framework is a citywide ban.** NS-3060/3061 and later NS-3072 prohibit hosted home-sharing and unhosted short-term/vacation rentals under 30 consecutive days, ban advertising, declare a public nuisance, and authorize criminal/civil/administrative remedies. No registration/permit pathway; no platform API duties in the ordinances.

3. **Litigation timeline.** April 2024 ordinances faced a CEQA suit (enforcement impaired; some citations rescinded). NS-3072 reenacted the ban with a GPU EIR addendum / Class 1 exemption theory; OC Superior Court set aside NS-3072 on April 20, 2026 (SASTRA). Status as of research date: ban ordinance ordered set aside.

4. **TOT / Airbnb.** Santa Ana hotel TOT exists, but residential STRs were prohibited rather than taxed via a host program. Airbnb CA help article 2297 does not list Santa Ana municipal collection → `airbnb_tax_collection_date` **null**. No City Portal / SB 346 local activating ordinance → `airbnb_data_sharing_date` **null**.

## Legislative history entries written

| Law | Jurisdiction | Passage | Effective | Enforcement | Primary framework |
| --- | --- | --- | --- | --- | --- |
| Ord. NS-3060 (urgency Article XXI ban) | City of Santa Ana | 2024-04-02 | 2024-04-02 | 2024-04-02 | true |
| Ord. NS-3061 (standard Article XXI ban) | City of Santa Ana | 2024-04-16 | 2024-05-16 | 2024-05-16 | false |
| Admin. fine resolution (OA 2024-04 companion) | City of Santa Ana | 2024-11-20 | 2024-11-20 | 2024-11-20 | false |
| Ord. NS-3072 (repeal/reenact Article XXI) | City of Santa Ana | 2024-12-03 | 2025-01-02 | 2025-01-02 | true |

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.json` (Santa Ana entry)
- Script: `agent/scripts/update_santa_ana_str_regulations.py`
- Report: `agent/reports/2026-08-08-santa-ana-str-legislative-history.md`

## Key sources

- City of Santa Ana — “City Council bans short-term residential rentals” press release; Ord. NS-3072 PDF (Municipal Code Corporation download); Code Enforcement administrative-fine FAQ
- CEQANet NOD — Short-Rental Prohibition Ordinance Project (OA No. 2024-04; SCH 2020029087)
- OC Register (Apr. 4, 2024); Voice of OC (Apr. 2024; Dec. 2024)
- Orange County Grand Jury City of Santa Ana response (Dec. 5, 2025) re: NS-3072
- Angel Law / SASTRA / New Santa Ana coverage of April 20, 2026 CEQA set-aside of NS-3072
- Airbnb help article 2297 (CA occupancy tax collection) — Santa Ana not listed
