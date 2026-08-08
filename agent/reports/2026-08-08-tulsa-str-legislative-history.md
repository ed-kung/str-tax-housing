# Tulsa, OK short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Tulsa, OK (first unchecked city). Tulsa’s primary STR framework is the March 11, 2020 package—Ord. 24323 (Title 21 Ch. 26 licensing) and Ord. 24328 (Title 42 zoning use)—both effective/enforced **2020-07-01**. Airbnb has collected Tulsa’s municipal 5% lodging tax since **2018-03-01**; no direct Airbnb–city listing/data connection was found (compliance via Host Compliance / Deckard).

## What was done

- Identified first list item lacking `agent_checked`: Tulsa, OK (index 47).
- Compiled binding city STR legislation from 2008 onward from Municode ordinance PDFs (Ords. 24323, 24328), City of Tulsa STR FAQ / Business Licensing pages, Airbnb help articles 2323 and 3604, and reputable news (Public Radio Tulsa, KTUL).
- Confirmed no post-2020 amendments to Title 21 Ch. 26; pending Nov. 2026 hotel-tax rate hike is not yet binding law and was excluded.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (2 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2020 | Zoning treated Airbnb-style rentals as bed-and-breakfasts requiring Board of Adjustment special exception; little dedicated STR licensing (Public Radio Tulsa 2018; TMAPC ZCA-13 record). |
| Primary framework | Ord. 24323 (licensing) + Ord. 24328 (zoning), passed 2020-03-11, effective/enforced 2020-07-01: annual $375 license, 24/7 local contact (1-hour response), license # in ads, 8-guest cap, STRs allowed by right citywide as principal or accessory use; no owner-occupancy or on-site host mandate; events banned. |
| Council choice | Council rejected TMAPC recommendation that non-owner-occupied STRs need special approval (Public Radio Tulsa, 2020-03-12). |
| Later changes | No substantive STR ordinance amendments found after 2020. City rebid compliance monitoring (Deckard, 2025). Proposed lodging-tax increase to 9.9% set for Nov. 3, 2026 ballot (effective 2027-01-01 if approved)—not yet law. |
| State law | No statewide STR preemption or licensing statute displacing Tulsa’s home-rule framework. |
| Airbnb tax | Municipal lodging-tax collection date **2018-03-01** (city/Airbnb announcement; Airbnb help art. 2323). |
| Airbnb data sharing | **null** — third-party scraping/monitoring (Host Compliance, then Deckard); tax deal only. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Tulsa entry)
- Report: `agent/reports/2026-08-08-tulsa-str-legislative-history.md`
