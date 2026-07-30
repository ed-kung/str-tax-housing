# ALFIN crosswalk (treatment cities → finance units)

Built a 1:many crosswalk from the 50 STR-policy cities to relevant Census ALFIN governmental units. Output has **113 rows**: 100 city-government IDs (2 ID schemes × 50 cities) plus 13 special-district IDs for tourism/lodging/convention-related authorities in 6 cities.

## What was done

- Script: `agent/scripts/03_alfin_crosswalk.py`
- Matched each policy city to its municipal ALFIN unit via `treatment_alfin_cities_match.parquet` (from `02_treatment_alfin_cities_match.py`), keeping **all IDs** for that `NAME`+`STATE` (old and new Census ID systems).
- Added special districts whose names indicate lodging/tourism/convention (or common HOT-funded facility) revenue authority, assigned to at most one policy city:
  - Prefer districts that name the city.
  - For county/metro districts without a city name, attach only if that county has a single policy city and the name matches a regional tourism/convention pattern (avoids suburban false positives such as Orland Park or Kent).
  - Shared-county pairs (e.g. Los Angeles / Long Beach) get a district only when the district name identifies one city.

## Main findings

- For **44 of 50** cities, the only relevant ALFIN units are the city governments themselves. Lodging taxes and STR license/permit fees are typically collected by the municipality, not by a separate special district in these data.
- Special districts included (unique names):
  - Los Angeles — Los Angeles Convention and Exhibition Center Authority
  - Chicago — Metropolitan Pier and Exposition Authority (Chicago)
  - Detroit — Detroit Regional Convention Facility Authority
  - Houston — Harris County-Houston Sports Authority
  - Milwaukee — Wisconsin Center District
  - Seattle — Washington State Convention Center Public Facilities District; WA State Major League Baseball Stadium Public Facilities District
- Long Beach does **not** receive the LA Convention Authority (name assigns it to Los Angeles only).
- Counties, townships, housing authorities, fire/water/park districts, and generic BIDs were excluded as not clearly assessing STR-related taxes/fees.

## Artifacts

- Crosswalk CSV: `/Users/ekung/Dropbox/projects/str-tax-housing-bot/alfin_crosswalk.csv`
- Script: `agent/scripts/03_alfin_crosswalk.py`
