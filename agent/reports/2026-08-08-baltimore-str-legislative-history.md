# Baltimore, MD short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Baltimore, MD (first unchecked city). Baltimore’s primary STR framework is Ordinance 19-217 (Council Bill 18-0189), signed 2019-01-28: primary-residence licensing (DHCD/Housing Commissioner; Subtitle 48 effective/enforced 2019-12-31) plus extension of the 9.5% city hotel tax to hosting-platform STR bookings (tax amendments operative on enactment). Maryland Ch. 704/758 (2019-05-25; eff. 2019-06-01) requires STR platforms to collect state sales tax; Ch. 638 (2025-05-20; eff. 2027-07-01) will centralize local hotel-tax remittance (including Baltimore Art. 28 §21-2) through the Comptroller. Airbnb currently collects Baltimore’s municipal hotel tax, but no official start date was found (`airbnb_tax_collection_date` null); no Airbnb–city direct data connection found.

## What was done

- Identified first list item lacking `agent_checked`: Baltimore, MD (index 29).
- Compiled binding city and state STR-related legislation from 2008 onward from Baltimore Legistar (File 18-0189 / Enactment 19-217), ordinance 3rd-reader text, Baltimore City Code Art. 15 Subtitle 48 and Art. 28 §§21-1–21-4, DHCD short-term rental pages and GovDelivery quarterly update, Maryland session laws (Ch. 704/758 of 2019; Ch. 638 of 2025), Airbnb help article 2309, Avalara occupancy-tax guide archives, and news (Baltimore Sun, WYPR, Maryland Reporter/Post-Examiner, VRM Intel, Daily Record).
- Excluded failed 2016 Council Bill 16-0737 (hotel tax on hosting intermediaries; died in committee) and non-binding recommendations/resolutions.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (3 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary framework | Ord. 19-217 (signed 2019-01-28): Art. 15 Subtitle 48 licensing + Art. 28 hotel-tax extension to platforms/hosts. |
| Tax timing | Ordinance text set tax amendments for 2018-12-31; enactment 2019-01-28 made tax operative on signing. Licensing Subtitle 48 effective/enforced 2019-12-31 (DHCD). |
| Core rules | Permanent-residence-only licenses (narrow grandfathered second unit); unhosted ≤60 days/year; $200 biennial fee; platform license verification, 3-day delisting, recordkeeping; 9.5% hotel tax. |
| State sales tax | Ch. 704/758 (eff. 2019-06-01): STR platforms must collect/remit 6% MD sales and use tax. |
| Future local-tax admin | Ch. 638 (eff. 2027-07-01): qualifying intermediaries remit local hotel taxes (incl. Baltimore §21-2) to Comptroller. |
| Airbnb tax | Municipal collection confirmed on Airbnb help article 2309; **start date unknown** (null)—not collecting as of Mar 2019 reporting; collecting by mid/late 2019 per Avalara. |
| Airbnb data sharing | **null** — on-request verification/records/delisting duties in ordinance; no City Portal/API announcement. |

## Legislative history (3 entries)

| Law | Passage | Effective | Enforced | Primary framework |
| --- | --- | --- | --- | --- |
| Ord. 19-217 (CB 18-0189) | 2019-01-28 | 2019-01-28 (tax); licensing 2019-12-31 | 2019-12-31 (licensing) | yes |
| MD Ch. 704 / 758 (2019) | 2019-05-25 | 2019-06-01 | 2019-06-01 | no |
| MD Ch. 638 (2025) | 2025-05-20 | 2027-07-01 | 2027-07-01 | no |

## Airbnb fields

- `airbnb_tax_collection_date`: **null** — municipal 9.5% hotel tax is collected on-platform today (Airbnb article 2309), but no official City/Airbnb start-date announcement; Mar 2019 reporting still cited only Montgomery County among MD hotel-tax agreements.
- `airbnb_data_sharing_date`: **null** — Subtitle 48 imposes verification, notice-based delisting, and on-request records; no documented direct Airbnb–Baltimore data connection.

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Baltimore, MD entry)
- Backup: `$AGENT_DATA_PATH/str_regulations.json.pre_baltimore.bak`
- Report: `agent/reports/2026-08-08-baltimore-str-legislative-history.md`
