# Dallas, TX short-term rental legislative history

## Summary

Dallas was the first unchecked city in `AGENT_DATA_PATH/str_regulations.json` (index 8). I researched its short-term rental (STR) legislative history from 2008 forward and added six binding legislative actions, all concentrated in 2023-2026. Dallas is unusual among large cities in that it passed **no** STR-specific law before 2023 despite four years of study (2019-2023), and the two ordinances it did pass on June 14, 2023 — Ordinance No. 32482, which zones STRs out of every single-family and other residential district, and Ordinance No. 32473, which adds City Code Chapter 42B requiring annual registration, inspections, occupancy caps, a two-night minimum stay, multifamily density caps and platform booking/reporting duties — have been enjoined since December 6, 2023 and have never been enforced. The injunction was affirmed by the Fifth Court of Appeals three times in 2025 and the city's petition for review remains pending at the Texas Supreme Court (No. 25-0748), so as of mid-2026 the only enforceable citywide STR requirement is hotel occupancy tax (HOT) registration and remittance. Both platform keys are null: Airbnb has never had a voluntary collection agreement with the City of Dallas (it collects only the 6% Texas state HOT, since May 1, 2017), and there is no evidence it has ever shared listing data with the city, which instead uses a third-party scraping vendor.

## What was done

- Located the first entry without `agent_checked` in `str_regulations.json` (Dallas, TX).
- Researched city, county and state action from 2008 forward, prioritizing primary documents: the full adopted texts of Ordinance Nos. 32473, 32482, 32556 and 33302 (American Legal Publishing PDFs of the signed ordinances, including proof-of-publication pages), the City of Dallas Planning & Development and Controller's Office STR pages, Texas Legislature Online bill text and histories, the Fifth Court of Appeals memorandum opinion on rehearing, and the Texas Supreme Court docket. Secondary sources (Dallas Morning News, KERA, Dallas Observer, D Magazine, Texas Municipal League, Avalara) were used for vote counts, enforcement dates and litigation posture.
- Wrote `agent/scripts/03_str_regulations_dallas_tx.py`, which backs up the JSON and writes the Dallas entry.
- Verified all six entries carry the full eight-field `measures` dict and that the entry now has `agent_checked: true`.

## Legislative history recorded (6 entries)

| Passed | Effective | Jurisdiction | Action |
| --- | --- | --- | --- |
| 2023-05-08 | 2023-05-19 | Texas | SB 929 (88R) — notice and compensation before revoking a nonconforming use (Loc. Gov't Code 211.006, 211.019) |
| 2023-06-14 | 2023-06-14 | Dallas | Ord. 32473 — City Code Ch. 42B, STR registration ordinance (13-0) |
| 2023-06-14 | 2023-06-14 | Dallas | Ord. 32482 — Development Code Chs. 51/51A, "short-term rental lodging" use, residential-zone ban (12-3) |
| 2023-09-20 | 2023-10-01 | Dallas | Ord. 32556 — FY 2023-24 fee ordinance, cut Sec. 42B-5 fees from $404/$234 to $248/$144 |
| 2025-05-25 | 2025-06-12 | Texas | HB 2464 (89R) — home-based business preemption with express STR carve-out |
| 2026-01-14 | 2026-02-01 | Dallas | Ord. 33302 — retimed HOT penalty (15%) and interest (10%/yr) in Secs. 44-39 and 44-56 |

## Main findings

- **Nothing binding before 2023.** The recitals in both June 2023 ordinances document the whole pre-history as study, not law: staff review starting in 2019, first committee briefing February 18, 2020, a task force from June 12, 2020 (restructured November 2021), a City Plan Commission hearing authorized December 2, 2021, and the Plan Commission's December 8, 2022 recommendation. A 2011 City Auditor report had already flagged that Dallas had no policies for "short-term vacation rentals." Through 2022 STR hosts were subject only to the generally applicable 9% city HOT (Ch. 44, Arts. V and VII), Ch. 27 minimum property standards, and noise/nuisance rules.
- **The 2023 package is a near-ban plus a strict license.** Ord. 32482 permits STRs by right only in MO(A), GO(A), multifamily, central area, mixed use, multiple commercial and urban corridor districts. Ord. 32473 layers on annual registration with pre-approval and renewal inspections, denial for tax delinquency or two prior citations, revocation of all of an owner's registrations for repeat or "egregious" offenses, 3 people/bedroom and 12-person occupancy caps, a two-night minimum stay, a one-hour local-responsible-party response requirement, and multifamily density caps (3% of units in multifamily zoning, 20% in nonresidential, zero in structures of 20 or fewer units). Platform duties are real but never operative: no fee collection for unregistered units or ancillary services, plus a monthly listing-level report to the director.
- **Enforcement has never begun.** Both ordinances took effect on passage but barred enforcement for six months; the city targeted December 13, 2023. Judge Monica McCoy Purdy enjoined both on December 6, 2023 (DC-23-16845). The Fifth Court affirmed February 7, 2025, reaffirmed on rehearing July 18, 2025, and denied en banc reconsideration August 19, 2025, finding a likely Texas constitutional due-course-of-law and retroactivity violation. Dallas petitioned SCOTX October 16, 2025 citing the June 2026 FIFA World Cup; merits briefing was ordered March 27, 2026 with no ruling as of the research date. Practical consequence for the panel data: the recorded 2023 "treatment" produced no enforced registration regime, and the $248 fee has never been charged.
- **State law cuts against the city.** SB 929, effective three and a half weeks before the ordinances and applicable to zoning changes considered on or after June 1, 2023, requires Dallas either to pay owners for stopping a nonconforming use (relocation/termination costs plus lost market value) or to let them operate until they recover that amount. HB 2464 (2025) explicitly preserves municipal STR authority, and SB 1567 (2025), the occupancy-limit preemption, applies only to home-rule cities under 250,000 population near large universities and so does not reach Dallas. SB 1592 (2025), which would have centralized platform collection of local HOT through the Comptroller, passed the Senate April 10, 2025 but died in House Ways & Means — so it is excluded.
- **Tax enforcement is the live channel.** Because Ch. 42B is enjoined, HOT is the city's only STR-specific lever. Ord. 33302 (effective February 1, 2026) moved the 15% penalty trigger to three months past due and started 10% interest the day after the due date. The Controller's Office told the Finance Committee it had recovered roughly $5.5 million from non-remitting operators since 2020 using data-scraping software, had detected 3,495 active STRs as of September 30, 2024 with nearly 45% not paying HOT, and was pursuing about 2,000 non-payers ahead of the World Cup.
- **`airbnb_tax_collection_date`: null.** Airbnb collects the 6% Texas state HOT for all Texas bookings from May 1, 2017 under its Comptroller agreement, but the 9% Dallas tax is host-remitted through the City Controller's Office (dallas.munirevs.com). A voluntary collection agreement was being drafted in August 2016 and never executed; renewed pushes in February 2022 and a June 2023 council directive to the city manager also produced nothing. Note this differs from the Houston (2019-07-01) and San Antonio (2025-03-10) entries, where city-level collection did begin.
- **`airbnb_data_sharing_date`: null.** The only data-sharing mechanism Dallas ever adopted is the Sec. 42B-14(c) monthly platform report, which is enjoined. The city relies on third-party scraping instead.

## Judgement calls

- Excluded the December 2023 injunction and the 2025 appellate opinions from `legislative_history` (judicial, not legislative), but described them in the affected ordinance summaries since they determine whether the ordinances bind.
- Excluded the June 2023 council direction to the city manager to negotiate a platform collection agreement (direction, not binding law) and SB 1592 (did not pass).
- Coded SB 929 as "no change" across all eight measures: it imposes notice and compensation duties on the city rather than changing what hosts may do. Its effect on Dallas is explained in the summary.
- Coded Ord. 32556 as `registration_requirements: decrease` (fee cut), consistent with treating fee increases as registration increases elsewhere in the dataset.
- Coded the Ch. 42B local-responsible-party rule as *not* a host-presence requirement (a one-hour response obligation, not presence during the stay).

## Artifacts

- `agent/scripts/03_str_regulations_dallas_tx.py` — script that writes the Dallas entry.
- `AGENT_DATA_PATH/str_regulations.json` — updated Dallas entry (`agent_checked: true`); 9 of 100 cities now checked, next unchecked is Jacksonville.
- `AGENT_DATA_PATH/str_regulations.20260807-224503.json.bak` — pre-update backup.
