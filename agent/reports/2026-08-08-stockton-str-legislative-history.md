# Stockton, CA short-term rental legislative history

**Summary:** Researched and filled `str_regulations.json` for Stockton, CA (first unchecked city). Stockton has **no stand-alone STR permit ordinance**; the operative framework is the longstanding **SMC Chapter 3.28 Uniform Transient Occupancy Tax** (8% operator registration/collection). A July 2022 draft Chapter 5.82 STR license ordinance was forwarded from committee but **never enacted**. Binding lodging assessments under the Stockton Tourism Business Improvement District (formed 2010; renewed/increased 2024) add fees on short-term room revenue. Airbnb does **not** collect Stockton municipal TOT (help article 2297 excludes Stockton from San Joaquin County collection; no city VCA found). No Airbnb–city data connection found. Updated entry with `agent_checked: 1`.

## What was done

- Identified first list item lacking `agent_checked`: **Stockton, CA** (index 59).
- Reviewed Stockton Municipal Code Chapter 3.28 (eCode360); Legistar/Granicus files **22-0508** (STR discussion) and **22-0696** (draft Chapter 5.82 ordinance + redline/PPT); confirmed Matter 22-0696 has no passage/enactment date and Chapter 5.82 is not in the code.
- Reviewed STBID Resolutions **10-0406** (2010-12-14), **2014-11-04-1601-01**, and **2024-11-19-1601-01/02** (minutes: 6-0 approval; 5% assessment effective 2025-01-01) and the August 13, 2024 Management District Plan.
- Checked Airbnb California occupancy-tax help article **2297** (San Joaquin County expressly excludes Stockton) and SB 346 (enabling only; no Stockton conforming ordinance).
- Excluded: never-adopted 2022 Chapter 5.82 draft; committee discussion items; San Joaquin County TOT/STR rules (unincorporated only); SB 346 without local activation; B&B inn standards (SMC 16.80.090) as a separate use from whole-home Airbnb operations.

## Main findings

| Theme | Finding |
| --- | --- |
| Dedicated STR ordinance | **None.** 2022 draft Ch. 5.82 (license, 200-day cap, platform TOT duties) never adopted. |
| Primary city framework | **SMC Ch. 3.28 TOT** — operator registration + 8% tax on stays ≤30 days; broad “hotel” definition covers STRs. |
| Lodging assessment | **STBID** — formed Dec. 14, 2010 (4%); renewed Nov. 19, 2024 at **5%** (→5.5% in year 6) effective Jan. 1, 2025. |
| Airbnb municipal tax | **null** — article 2297 excludes Stockton from county collection; no city VCA listed. |
| Airbnb data sharing | **null** — no City Portal / SB 346 local ordinance. |

## Legislative history recorded

1. **SMC Chapter 3.28 Uniform Transient Occupancy Tax** — City of Stockton — passage/effective null (pre-2008 prior code); enforcement treated as continuous from 2008-01-01 — `primary_framework`: true  
2. **Resolution No. 10-0406 (STBID formation)** — Passage/effective/enforced 2010-12-14 — `primary_framework`: false  
3. **Resolution No. 2024-11-19-1601-02 (STBID renewal / rate increase)** — Passage 2024-11-19; effective/enforced 2025-01-01 — `primary_framework`: false  

## Artifacts

- Updated: `$AGENT_DATA_PATH/str_regulations.json` (Stockton entry)
- Script: `agent/scripts/update_stockton_str_regulations.py`
- Report: `agent/reports/2026-08-08-stockton-str-legislative-history.md`
