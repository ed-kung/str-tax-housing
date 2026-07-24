# City mapping across policy, tax, and ZHVI

Matched all 50 policy cities to the closest FiSC tax city and ZHVI city (state-constrained fuzzy match) and wrote `city_mapping.csv` for downstream merges.

## What was done

- Built `agent/scripts/build_city_mapping.py` to load policy, Lincoln FiSC tax, and Zillow ZHVI city lists.
- For each policy city, restricted candidates to the same state, then chose the closest name via normalized string similarity (`Fort`/`Ft`, `Saint`/`St`, punctuation). ZHVI ties prefer lower `SizeRank` (larger cities).
- Policy source used: `best_treatment_dates_2026-07.csv` (the `2026-0y` path named in `AGENTS.md` was not present on disk; cities are the same across available policy files).

## Main findings

- All 50 policy cities matched a tax and ZHVI city.
- ZHVI matches were exact on city name within state for every city.
- Tax matches were exact after normalization except two FiSC naming quirks (already noted in existing notebooks):
  - `Fort Worth` → `TX: Ft. Worth`
  - `Oklahoma City` → `OK: Oklahoma`

## Artifacts

- Mapping CSV: `/Users/ekung/Dropbox/projects/str-tax-housing-bot/city_mapping.csv`
- Script: `agent/scripts/build_city_mapping.py`
