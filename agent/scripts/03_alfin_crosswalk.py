"""Build 1:many crosswalk from treatment cities to relevant ALFIN units.

Writes alfin_crosswalk.csv to AGENT_DATA_PATH with:
  city, state (from policy file) + all alfin_units columns + explanation

Includes:
  - City governments matched via treatment_alfin_cities_match.parquet
    (all IDs under both Census ID schemes)
  - Special districts that may assess lodging/tourism-related taxes or fees,
    uniquely assigned to at most one treatment city
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")

RAW_DATA_PATH = Path(os.environ["RAW_DATA_PATH"])
MY_DATA_PATH = Path(os.environ["MY_DATA_PATH"])
AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])

POLICY_PATH = (
    RAW_DATA_PATH / "sales-analysis-redfin/data/best_treatment_dates_2026-07.csv"
)
UNITS_PATH = MY_DATA_PATH / "processed_data/alfin_units.parquet"
CITY_MATCH_PATH = AGENT_DATA_PATH / "treatment_alfin_cities_match.parquet"
OUT_PATH = AGENT_DATA_PATH / "alfin_crosswalk.csv"

UNIT_COLS = [
    "ID",
    "UNIT_TYPE_CODE",
    "NAME",
    "STATE",
    "STATE_FIPS",
    "COUNTY_FIPS",
    "PLACE_FIPS",
    "FUNCTION_CODE",
    "UNIT_TYPE",
    "FUNCTION",
]

# Special districts whose names indicate lodging / tourism / convention revenue
# authority (or common HOT-funded facility districts).
SD_RELEVANT_RE = re.compile(
    r"(?:"
    r"TOURIS(?:M|T)|HOTEL|LODGING|VISITORS?|CONVENTION|HOSPITALITY|"
    r"TRANSIENT|OCCUPANCY|SHORT[\s-]?TERM|VACATION\s+RENTAL|"
    r"DESTINATION\s+MARKET|\bTBID\b|\bTMD\b|"
    r"EXPOSITION|PIER\s+AND\s+EXPOSITION|"
    r"SPORTS?\s+AUTHORITY|SPORT\s+COMPLEX|"
    r"PUBLIC\s+FACILITIES\s+DISTRICT|CENTER\s+DISTRICT|"
    r"STADIUM\s+(?:PUBLIC\s+FACIL|AUTHORITY)|ARENA\s+AUTHORITY"
    r")",
    re.I,
)

# County/metro-wide districts that may lack the city name in the title but still
# receive lodging/tourism assessments for the (sole) treatment city in-county.
# Excludes suburban "Orland Park Metro Exposition"-style names.
SD_REGIONAL_RE = re.compile(
    r"(?:"
    r"CONVENTION|TOURIS(?:M|T)|VISITORS?|LODGING|HOSPITALITY|"
    r"TRANSIENT|OCCUPANCY|SHORT[\s-]?TERM|"
    r"WISCONSIN\s+CENTER\s+DISTRICT|"
    r"MAJOR\s+LEAGUE\s+BASEBALL\s+STADIUM|"
    r"METROPOLITAN\s+PIER\s+AND\s+EXPOSITION"
    r")",
    re.I,
)

# Place-name tokens that mean the district serves a different municipality
# even when it contains the treatment city string (e.g. CHICAGO HEIGHTS).
SUBURB_AFTER_RE = re.compile(
    r"^(?:HEIGHTS|RIDGE|LAWN|GROVE|HILLS|PARK|VALLEY|SPRINGS|BEACH|"
    r"SHORES|WOODS|FALLS|CREEK|VIEW|SOUTH\b.*SUBURBAN)\b",
    re.I,
)


def normalize_city_token(city: str) -> str:
    s = city.upper().strip()
    s = s.replace(".", "")
    s = re.sub(r"\bFORT\b", "FT", s)
    s = re.sub(r"\bSAINT\b", "ST", s)
    s = re.sub(r"\s+", " ", s)
    return s


def name_mentions_city(name: str, city: str) -> bool:
    """True if district name references the city as its own place, not a suburb."""
    name_u = name.upper()
    city_u = normalize_city_token(city)
    m = re.search(r"\b" + re.escape(city_u) + r"\b", name_u)
    if not m:
        return False
    after = name_u[m.end() :].strip()
    if SUBURB_AFTER_RE.match(after):
        return False
    return True


def city_explanation(city: str) -> str:
    return (
        f"Municipal government of {city}; primary local authority for STR "
        f"licensing/permit fees, lodging/occupancy taxes, and related charges."
    )


def sd_explanation(city: str, name: str) -> str:
    return (
        f"Special district ({name}) linked to {city} whose name indicates "
        f"tourism, lodging, convention, or related facility finance that may "
        f"assess lodging taxes, tourism assessments, or similar charges."
    )


def assign_special_districts(
    units: pd.DataFrame, city_match: pd.DataFrame
) -> pd.DataFrame:
    """Return SD rows with city/state/explanation; each ID at most once."""
    sd = units[units["UNIT_TYPE"] == "Special District"].copy()
    sd = sd[sd["NAME"].str.contains(SD_RELEVANT_RE, na=False)]

    # Treatment cities per (STATE, COUNTY_FIPS) for uniqueness rules.
    county_cities: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for r in city_match.itertuples(index=False):
        key = (r.STATE, r.COUNTY_FIPS)
        county_cities.setdefault(key, []).append((r.city, r.state))

    assigned: dict[str, dict] = {}  # ID -> row dict

    for r in city_match.itertuples(index=False):
        cand = sd[sd["STATE"] == r.STATE].copy()
        if cand.empty:
            continue

        same_county = cand["COUNTY_FIPS"] == r.COUNTY_FIPS
        mentions = cand["NAME"].map(lambda n: name_mentions_city(n, r.city))

        # Keep if (same county) or (name mentions this city).
        cand = cand[same_county | mentions]
        if cand.empty:
            continue

        peers = county_cities.get((r.STATE, r.COUNTY_FIPS), [(r.city, r.state)])
        peer_cities = [c for c, _ in peers]

        for _, row in cand.iterrows():
            unit_id = row["ID"]
            mentions_self = name_mentions_city(row["NAME"], r.city)
            mentions_peers = [
                c for c in peer_cities if name_mentions_city(row["NAME"], c)
            ]

            # Uniqueness / attachment rules:
            # 1) Name mentions exactly one treatment city among peers -> that city
            # 2) Name mentions this city (even if county differs) -> this city
            # 3) Name mentions no peer cities, and this is the sole treatment
            #    city in the district's county -> that city
            # 4) Otherwise skip (cannot uniquely assign)
            if len(mentions_peers) == 1 and mentions_peers[0] != r.city:
                continue
            if len(mentions_peers) > 1:
                continue
            if not mentions_self:
                # Only attach unnamed districts when they are clearly
                # county/metro tourism-facility authorities and this is the
                # unique treatment city in that county.
                if len(peer_cities) != 1:
                    continue
                if row["COUNTY_FIPS"] != r.COUNTY_FIPS:
                    continue
                if not SD_REGIONAL_RE.search(str(row["NAME"])):
                    continue

            if unit_id in assigned and assigned[unit_id]["city"] != r.city:
                # Prefer the city named in the district title.
                if mentions_self and not name_mentions_city(
                    row["NAME"], assigned[unit_id]["city"]
                ):
                    pass  # overwrite below
                else:
                    continue

            rec = {c: row[c] for c in UNIT_COLS}
            rec["city"] = r.city
            rec["state"] = r.state
            rec["explanation"] = sd_explanation(r.city, row["NAME"])
            assigned[unit_id] = rec

    if not assigned:
        return pd.DataFrame(columns=["city", "state", *UNIT_COLS, "explanation"])
    return pd.DataFrame(assigned.values())


def main() -> None:
    policy = pd.read_csv(POLICY_PATH)
    cities = policy[["city", "state"]].drop_duplicates()
    assert len(cities) == 50

    if not CITY_MATCH_PATH.exists():
        raise FileNotFoundError(
            f"Missing {CITY_MATCH_PATH}; run 02_treatment_alfin_cities_match.py first"
        )
    city_match = pd.read_parquet(CITY_MATCH_PATH)
    assert len(city_match) == 50

    units = pd.read_parquet(UNITS_PATH)

    # --- City governments (all IDs for matched NAME+STATE) ---
    city_units = units[units["UNIT_TYPE"] == "City"].merge(
        city_match[["city", "state", "NAME", "STATE"]],
        on=["NAME", "STATE"],
        how="inner",
    )
    assert city_units["city"].nunique() == 50
    assert city_units["ID"].nunique() == len(city_units), "duplicate city IDs"
    city_units = city_units.copy()
    city_units["explanation"] = city_units["city"].map(city_explanation)

    # --- Special districts ---
    sd_units = assign_special_districts(units, city_match)

    out = pd.concat(
        [
            city_units[["city", "state", *UNIT_COLS, "explanation"]],
            sd_units[["city", "state", *UNIT_COLS, "explanation"]],
        ],
        ignore_index=True,
    )

    # Each TARGET ID at most once
    assert not out["ID"].duplicated().any(), out.loc[out["ID"].duplicated(keep=False)]
    # All 50 cities represented
    assert out["city"].nunique() == 50
    missing = set(zip(cities["city"], cities["state"])) - set(
        zip(out["city"], out["state"])
    )
    assert not missing, missing

    out = out.sort_values(["state", "city", "UNIT_TYPE_CODE", "NAME", "ID"]).reset_index(
        drop=True
    )

    AGENT_DATA_PATH.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_PATH, index=False)

    n_city = (out["UNIT_TYPE"] == "City").sum()
    n_sd = (out["UNIT_TYPE"] == "Special District").sum()
    print(f"Wrote {len(out)} rows to {OUT_PATH}")
    print(f"  City government rows: {n_city} ({out.loc[out['UNIT_TYPE']=='City','ID'].nunique()} IDs)")
    print(f"  Special district rows: {n_sd}")
    if n_sd:
        print("\nSpecial districts:")
        print(
            out.loc[
                out["UNIT_TYPE"] == "Special District",
                ["city", "state", "NAME", "FUNCTION"],
            ]
            .drop_duplicates()
            .to_string(index=False)
        )
    print("\nRows per city:")
    print(out.groupby(["city", "state"]).size().sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()
