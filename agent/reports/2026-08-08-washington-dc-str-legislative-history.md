# Washington, DC short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Washington, DC (first unchecked city). The District’s primary STR framework is **D.C. Law 22-307** (Bill 22-92 / Act 22-563), passed 2018-11-13, law-effective 2019-04-25, applicability **2019-10-01**, with active license enforcement only after a grace period ended **2022-06-09**. Companion **Z.C. Order 19-15** (emergency 2019-10-24; final effective 2020-02-14) authorized STRs as accessory residential uses so licenses could issue. Airbnb has collected DC’s 14.5% Transient Lodging Tax since **2015-02-15**; binding platform monthly reporting / City Portal compliance support dates to final rules effective **2021-12-03**.

## What was done

- Identified first list item lacking `agent_checked`: Washington, DC (index 21).
- Compiled binding District legislation and Zoning Commission action from 2008 onward from the D.C. Law Library (Law 22-307), Z.C. Order 19-15 final rulemaking PDF, DCRA/DLCP STR pages and GovDelivery bulletins, Airbnb host/tax notices and DC economic report, and reputable coverage (Washington Post, Curbed DC, UrbanTurf, DCist).
- Excluded non-binding Council letters/resolutions, the 2019 emergency independent-analysis act (procurement study only), DCRA implementing rules as a separate “law” entry (treated as implementation of Law 22-307), and the pending Short-Term Rental Regulation Amendment Act of 2026 (not enacted).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (2 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2018 baseline | No dedicated STR licensing chapter; residential STRs were widely operating while zoning treated many short stays as prohibited lodging (rarely enforced). Transient lodging tax already applied. |
| Primary framework | **Law 22-307** (passed 2018-11-13; Mayor returned unsigned Jan 2019; became law 2019-04-25): primary-residence-only licensing, hosted vs 90-night vacation rental cap, host safety/insurance/tax duties, and booking-service reporting, delist-on-notice, and tax remittance. Applicability **2019-10-01**. |
| Zoning companion | **Z.C. Order 19-15** (emergency **2019-10-24**; final effective **2020-02-14**): defines/permits STRs as accessory to principal residential use so DCRA could license under the Act. |
| Implementation lag | Final DCRA rules **2021-12-03** (68 DCR 012598); applications **2022-01-10**; active enforcement after grace period **2022-06-09**. |
| Airbnb tax | District Transient Lodging Tax (14.5%) collection began **2015-02-15** (voluntary agreement; later reinforced by Law 22-307). |
| Airbnb data sharing | Binding monthly booking-service reports under Law 22-307 / 14 DCMR Ch. 99 operative **2021-12-03**; Airbnb reports City Portal support for DLCP enforcement. |

## Legislative history (2 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| D.C. Law 22-307 (STR Regulation Act of 2018) | 2018-11-13 | 2019-10-01 | 2022-06-09 | yes |
| Z.C. Order 19-15 (zoning text amendment) | 2019-10-24 | 2019-10-24 | 2019-10-24 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **2015-02-15** — Airbnb/DC occupancy-tax program launch; Washington Post / TechCrunch / Nat’l Law Review / host notice.
- `airbnb_data_sharing_date`: **2021-12-03** — final rulemaking making monthly platform reports operative; Airbnb City Portal partnership with DLCP noted in 2024 Airbnb DC economic report.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Washington, DC entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_washington_dc.bak`
- Report: `agent/reports/2026-08-08-washington-dc-str-legislative-history.md`
