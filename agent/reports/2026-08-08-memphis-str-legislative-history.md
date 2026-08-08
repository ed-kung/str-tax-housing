# Memphis, TN short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Memphis, TN (first unchecked city). Memphis’s first STR framework is Ordinance 5631 (passed 2016-11-01; effective 2017-03-01; tax/fee enforcement delayed to 2017-05-01), a light-touch tax ordinance (3.5% occupancy tax + $2/room-night assessment) without permitting. Ordinance 5856 (passed 2023-03-21; effective/enforced 2023-07-01) added Public Works permitting ($300/$150) subject to Tennessee’s Short-Term Rental Unit Act legacy rules. Airbnb has collected Memphis municipal occupancy taxes since 2017-06-01; no direct Airbnb–city listing/data connection was found.

## What was done

- Identified first list item lacking `agent_checked`: Memphis, TN (index 28).
- Compiled binding city and state STR-related legislation from 2008 onward from Memphis Granicus ordinance text (Ord. 5631 PDF via Shelby County Document Center; Ord. 5856 MetaViewer), council agendas (clips 9299/9303/9325/9350), Tennessee Pub. Ch. 972 and 787 / TN DOR Occupancy 20-20, Airbnb newsroom (May 2017), and reputable news (Commercial Appeal, Tennessean, Avalara, Action News 5).
- Excluded Shelby County Ord. 488 (2018-08-13), which applies only to unincorporated Shelby County, not the City of Memphis.
- Updated `AGENT_DATA_PATH/str_regulations.json` with `legislative_history` (4 entries), Airbnb tax/data fields, and `agent_checked: 1`.

## Main findings

| Theme | Finding |
| --- | --- |
| Primary tax framework | Ord. 5631 (2016-11-01) creates STR definition, carves STRs out of UDC rooming-house rules, 3.5% privilege tax + $2/room-night assessment, voluntary platform remittance; permits were stripped before adoption. |
| Tax timing | Ordinance effective 2017-03-01; Council delayed tax/fee start to 2017-05-01 pending Airbnb deal. |
| State legacy / preemption | Pub. Ch. 972 (2018-05-17) grandfathered already-operating STRs against later local restrictions; cited in Ord. 5856 applicability. |
| State marketplace occupancy | Pub. Ch. 787 (eff. 2021-01-01) requires STR marketplaces to remit local occupancy taxes to TN DOR. |
| Permitting framework | Ord. 5856 (third reading 2023-03-21; eff. 2023-07-01) requires DPW permits, insurance, local responsible party, listing permit numbers; pre-7/1/2023 operators generally grandfathered. |
| Airbnb tax | Municipal occupancy + TID assessment collection date **2017-06-01** (Airbnb/Commercial Appeal). |
| Airbnb data sharing | **null** — tax VCA only; city uses Develop901 + third-party listing monitoring. |

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Memphis entry)
- Report: `agent/reports/2026-08-08-memphis-str-legislative-history.md`
