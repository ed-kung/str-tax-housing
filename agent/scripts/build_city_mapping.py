"""Map each policy-data city to the closest tax (FiSC) and ZHVI city names.

Writes city_mapping.csv to AGENT_DATA_PATH with columns:
  policy_city, tax_city, zhvi_city
"""

from __future__ import annotations

import os
import re
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")

RAW_DATA_PATH = Path(os.environ["RAW_DATA_PATH"])
AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])

# AGENTS.md names best_treatment_dates_2026-0y.csv; on disk the dated file is 2026-07.
POLICY_CANDIDATES = [
    RAW_DATA_PATH / "sales-analysis-redfin/data/best_treatment_dates_2026-0y.csv",
    RAW_DATA_PATH / "sales-analysis-redfin/data/best_treatment_dates_2026-07.csv",
    RAW_DATA_PATH / "sales-analysis-redfin/data/best_treatment_dates.csv",
]
TAX_PATH = RAW_DATA_PATH / "lincoln-institute/FiSC-Full-Dataset-2023-Update.xlsx"
ZHVI_PATH = RAW_DATA_PATH / "zhvi/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
OUT_PATH = AGENT_DATA_PATH / "city_mapping.csv"


def resolve_policy_path() -> Path:
    for path in POLICY_CANDIDATES:
        if path.exists():
            return path
    raise FileNotFoundError(
        "No policy file found among: " + ", ".join(str(p) for p in POLICY_CANDIDATES)
    )


def normalize_city(name: str) -> str:
    s = name.lower().strip()
    s = s.replace(".", "")
    s = re.sub(r"\bfort\b", "ft", s)
    s = re.sub(r"\bsaint\b", "st", s)
    s = re.sub(r"\s+", " ", s)
    return s


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_city(a), normalize_city(b)).ratio()


def parse_tax_cities(tax: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for name in sorted(tax["city_name"].dropna().unique()):
        if name.startswith("Average") or name.startswith("Median"):
            continue
        m = re.match(r"^([A-Z]{2}):\s*(.+)$", name)
        if not m:
            continue
        rows.append({"tax_city": name, "state": m.group(1), "city": m.group(2)})
    return pd.DataFrame(rows)


def closest_tax_city(city: str, state: str, tax_cities: pd.DataFrame) -> str:
    cands = tax_cities[tax_cities["state"] == state]
    if cands.empty:
        raise ValueError(f"No tax cities for state {state}")
    best = max(cands.itertuples(index=False), key=lambda r: similarity(city, r.city))
    return best.tax_city


def closest_zhvi_city(city: str, state: str, zhvi: pd.DataFrame) -> str:
    cands = zhvi[zhvi["State"] == state]
    if cands.empty:
        raise ValueError(f"No ZHVI cities for state {state}")

    exact = cands[cands["RegionName"].map(normalize_city) == normalize_city(city)]
    if not exact.empty:
        return exact.sort_values("SizeRank").iloc[0]["RegionName"]

    scored = [
        (similarity(city, row.RegionName), row.SizeRank, row.RegionName)
        for row in cands.itertuples(index=False)
    ]
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[0][2]


def main() -> None:
    policy_path = resolve_policy_path()
    policy = pd.read_csv(policy_path)
    tax = pd.read_excel(TAX_PATH, sheet_name="Data", usecols=["city_name"])
    zhvi = pd.read_csv(ZHVI_PATH, usecols=["RegionName", "State", "SizeRank"])

    tax_cities = parse_tax_cities(tax)

    rows = []
    for _, row in policy.iterrows():
        policy_city = row["city"]
        state = row["state"]
        rows.append(
            {
                "policy_city": policy_city,
                "tax_city": closest_tax_city(policy_city, state, tax_cities),
                "zhvi_city": closest_zhvi_city(policy_city, state, zhvi),
            }
        )

    out = pd.DataFrame(rows)
    AGENT_DATA_PATH.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_PATH, index=False)
    print(f"Wrote {len(out)} rows to {OUT_PATH}")
    print(f"Policy source: {policy_path}")
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
