# Regs → ZHVI unit crosswalk

Built a 1:1 crosswalk from `regs_unit_list.csv` (100 cities) to `zhvi_unit_list.csv`. **All 100** regs cities matched a ZHVI city unit via normalized exact name+state match.

## What was done

- Script: `agent/scripts/05_regs_zhvi_xwalk.py`
- Restricted ZHVI candidates to `region_type == city`
- Matched within state using normalized names (`Fort`↔`Ft`, `Saint`↔`St`, strip periods/hyphens)
- Fuzzy same-state fallback available (threshold 0.85); not needed for this regs list

## Main findings

- Every regs city has a unique ZHVI counterpart after normalization (including Fort Worth, St. Louis, St. Petersburg, Winston-Salem)
- Output has one row per regs entity; columns preserved: `city`, `state`, `zhvi_id`, `region_name`, `state_name`, `region_type`

## Artifacts

- Crosswalk: `/Users/ekung/Dropbox/projects/str-tax-housing-bot/regs_zhvi_xwalk.csv`
- Script: `agent/scripts/05_regs_zhvi_xwalk.py`
