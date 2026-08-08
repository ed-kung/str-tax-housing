# Denver, CO short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Denver, CO (first unchecked city). Denver’s primary STR framework is the June 2016 primary-residence licensing ordinance (Ord. 262-16), effective/enforced 2017-01-01, paired with a zoning text amendment the same day. Airbnb has collected Denver’s municipal Lodger’s Tax since 2018-04-01; no direct Airbnb–city listing/data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Denver, CO (index 18).
- Compiled binding city and state STR-related legislation from 2008 onward from Denvergov STR laws page, signed ordinances (CB16-0262 / Ord. 262-16; CB20-0240 / Ord. 240-20; CB20-1229 / Ord. 1229-20), Denver Zoning Code §11.8.10 materials, Colorado HB19-1240, Denver Finance Lodger’s Tax guidance, Airbnb Denver help article, and reputable news (CPR, Denverite, Colorado Politics, BusinessDen, Denver Post).
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (5 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Pre-2016 | Residential STRs were effectively illegal under zoning; little active enforcement until the 2016 package. |
| Primary framework | Ord. 262-16 / CB16-0262 (passed 2016-06-13; mandatory 2017-01-01) creates Chapter 33 licensing: primary residence only, Lodger’s Tax account, safety/insurance/ad posting, guest brochure. Soft educational rollout mid-2016; active enforcement from 2017-01-01. |
| Zoning companion | CB16-0261 (same day) adds DZC accessory-use STR standards (§11.8.10), tying legality to primary-residence operation. |
| Fee / primary-residence upgrade | Ord. 240-20 / CB20-0240 (passed 2020-03-31; effective 2020-04-01) strengthens primary-residence standards and raises fees to $50 application + $100/year. |
| Platform accountability | Ord. 1229-20 / CB20-1229 (passed 2020-11-23; city-stated effective 2021-02-01) bars platforms from processing unlicensed bookings ($1,000/day) and requires multi-year transaction records. |
| State tax | HB19-1240 marketplace-facilitator sales-tax duties (marketplace provisions effective 2019-10-01) cover state/state-administered taxes, not Denver Lodger’s Tax. |
| Airbnb tax | Municipal Lodger’s Tax collection date **2018-04-01** (Denver Finance STR taxation PDF; BusinessDen). |
| Airbnb data sharing | **null** — no City Portal/API/bulk feed/delist channel; city uses third-party listing monitoring; CB20-1229 is liability + records retention, not a direct data connection. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Denver entry)
- Report: `agent/reports/2026-08-08-denver-str-legislative-history.md`
