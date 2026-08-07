# Regs → FiSC unit crosswalk

Built a 1:1 crosswalk from `regs_unit_list.csv` (100 cities) to `fisc_unit_list.csv`. **84** regs cities matched a FiSC unit; **16** have no confident same-state match in FiSC (left blank).

## What was done

- Script: `agent/scripts/04_regs_fisc_xwalk.py`
- Parsed FiSC `city_name` (`ST: City`), dropped aggregate Average/Median rows
- Matched within state using normalized names (`Fort`↔`Ft`, `Saint`↔`St`, strip periods/hyphens)
- Accepted one non-exact alias: Oklahoma City → `OK: Oklahoma`
- Rejected weak fuzzy matches (e.g. North Las Vegas ↛ Las Vegas, Irvine ↛ Riverside)

## Main findings

- Exact/normalized matches cover most overlapping cities (including Fort Worth → `TX: Ft. Worth`)
- Unmatched regs cities are absent from FiSC (no HI units at all; several AZ/CA/NJ/NV/TX suburbs not in the FiSC sample)
- Output has one row per regs entity; columns preserved: `city`, `state`, `fisc_id`, `city_name`, `city_types`

## Artifacts

- Crosswalk: `/Users/ekung/Dropbox/projects/str-tax-housing-bot/regs_fisc_xwalk.csv`
- Script: `agent/scripts/04_regs_fisc_xwalk.py`
