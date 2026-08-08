# Reno STR legislative history

Updated `str_regulations.json` for Reno, NV (first unchecked city). Reno still has no dedicated short-term-rental permitting ordinance; STRs are treated as transient lodging for RSCVA-administered room tax. Airbnb began collecting that combined municipal/county tax on 2016-03-15. No Airbnb–City enforcement data connection was found. The only post-2008 binding actions with clear STR relevance are state AB 321 (platform-report enabling), state AB 396 (ADUs; local option to ban ADU transient lodging), and City Ordinance 6727 (2025-10-08), which allows ADUs without a 28-day minimum stay.

## Findings

- **No primary city STR framework:** City Business Licensing staff report (June 4, 2025) and October 2025 council/press coverage confirm Reno has not adopted a dedicated STR registration, spacing, occupancy, or platform-compliance ordinance. Washoe County’s 2021 STR permit program applies only to unincorporated areas, not city limits. June 2025 council discussion directed staff toward drafting (not binding law).
- **Tax / licensing baseline:** Reno STRs are subject to RSCVA transient lodging tax licenses and the combined city/county room tax under RMC Title III, Section 2 (pre-2008 framework; RSCVA FAQ notes homeowner vacation-rental licensing as of 2014-07-01). Owner-occupied room rentals have historically been treated as a gray area / exclusion under the transient-lodging definition.
- **AB 321 (2017):** State enabling for optional city/county platform quarterly reports and subpoenas; Reno has not adopted a local implementing ordinance.
- **AB 396 / Ord. 6727 (2025):** State ADU mandate (Ch. 365; prep 2025-06-06, operative 2026-07-01) allows localities to ban ADU transient lodging. Reno Ordinance 6727 (adopted 2025-10-08; effective ~2025-10-09 on clerk filing) authorizes ADUs and deliberately omits the Planning Commission’s proposed 28-day minimum, leaving ADUs eligible for STR use.
- **Airbnb tax collection:** `2016-03-15` from RSCVA Airbnb Host FAQ; corroborated by RSCVA budget (“beginning March 2016”) and Airbnb help article 2315 (Reno/Sparks/Washoe collection of City or County Transient Lodging Tax).
- **Airbnb data sharing:** `null`. Tax VCA is not an enforcement feed; Nevada Current reported host identity/location confidentiality under the RSCVA agreement; no AB 321 city ordinance or City Portal found.

## Sources

- City of Reno June 4, 2025 Item C.3 staff report and presentation (PrimeGov); reno.gov ADU ordinance page / Ord. 6727 PDF
- RGJ (2014-05-19; 2025-10-08); 2 News / Fox Reno / Nevada Current ADU and Washoe STR coverage; This Is Reno (2020; 2025)
- RSCVA Airbnb Host FAQ (3.01.16); RSCVA Transient Lodging Tax FAQs; RSCVA Regulations; Airbnb help article 2315
- NRS / Statutes: AB 321 (Ch. 347, 2017); AB 396 (Ch. 365, 2025); Legislative Counsel Short-term Rentals brief

## Artifacts

- `AGENT_DATA_PATH/str_regulations.json` (Reno entry, index 79)
- `agent/scripts/update_reno_str_regulations.py`
