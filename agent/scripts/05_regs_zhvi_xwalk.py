"""Build 1:1 crosswalk from regs_unit_list to zhvi_unit_list.

For each regs (city, state), pick the best ZHVI city-unit match.
Writes regs_zhvi_xwalk.csv to AGENT_DATA_PATH with original column names:
  city, state, zhvi_id, region_name, state_name, region_type
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

MY_DATA_PATH = Path(os.environ["MY_DATA_PATH"])
AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])

REGS_PATH = MY_DATA_PATH / "raw_data/regs_unit_list.csv"
ZHVI_PATH = MY_DATA_PATH / "raw_data/zhvi_unit_list.csv"
OUT_PATH = AGENT_DATA_PATH / "regs_zhvi_xwalk.csv"

FUZZY_THRESHOLD = 0.85
ZHVI_COLS = ["zhvi_id", "region_name", "state_name", "region_type"]


def normalize_city(name: str) -> str:
    s = str(name).upper().strip()
    s = s.replace(".", "")
    s = re.sub(r"\bFORT\b", "FT", s)
    s = re.sub(r"\bSAINT\b", "ST", s)
    s = s.replace("-", " ")
    s = re.sub(r"\s+", " ", s)
    return s


def prepare_zhvi(zhvi: pd.DataFrame) -> pd.DataFrame:
    out = zhvi[zhvi["region_type"] == "city"].copy()
    out["city_n"] = out["region_name"].map(normalize_city)
    return out.reset_index(drop=True)


def score_pair(regs_city_n: str, zhvi_city_n: str) -> float:
    if regs_city_n == zhvi_city_n:
        return 1.0
    if regs_city_n == zhvi_city_n + " CITY":
        return 0.95
    return SequenceMatcher(None, regs_city_n, zhvi_city_n).ratio()


def fuzzy_match(row: pd.Series, zhvi: pd.DataFrame) -> dict:
    empty = {c: pd.NA for c in ZHVI_COLS}
    cand = zhvi[zhvi["state_name"] == row["state"]]
    if cand.empty:
        return empty
    scored = sorted(
        ((score_pair(row["city_n"], r.city_n), r) for r in cand.itertuples(index=False)),
        key=lambda x: x[0],
        reverse=True,
    )
    best_score, best = scored[0]
    if best_score < FUZZY_THRESHOLD:
        return empty
    return {c: getattr(best, c) for c in ZHVI_COLS}


def main() -> None:
    regs = pd.read_csv(REGS_PATH)
    zhvi_raw = pd.read_csv(ZHVI_PATH)
    assert list(regs.columns) == ["city", "state"]
    assert list(zhvi_raw.columns) == ZHVI_COLS
    assert not regs.duplicated(["city", "state"]).any()

    zhvi = prepare_zhvi(zhvi_raw)
    regs = regs.copy()
    regs["city_n"] = regs["city"].map(normalize_city)

    exact = regs.merge(
        zhvi,
        left_on=["state", "city_n"],
        right_on=["state_name", "city_n"],
        how="left",
        indicator=True,
    )
    assert not exact.duplicated(["city", "state"]).any(), (
        "Multiple ZHVI cities matched the same regs city"
    )

    unmatched_mask = exact["_merge"] == "left_only"
    if unmatched_mask.any():
        fuzzy_rows = exact.loc[unmatched_mask].apply(
            lambda r: fuzzy_match(r, zhvi), axis=1, result_type="expand"
        )
        exact.loc[unmatched_mask, ZHVI_COLS] = fuzzy_rows[ZHVI_COLS].to_numpy()

    out = exact[["city", "state", *ZHVI_COLS]].copy()
    out["zhvi_id"] = pd.to_numeric(out["zhvi_id"], errors="coerce").astype("Int64")

    assert len(out) == len(regs)
    assert not out.duplicated(["city", "state"]).any()
    assert list(out.columns) == ["city", "state", *ZHVI_COLS]

    AGENT_DATA_PATH.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_PATH, index=False)

    n_matched = out["zhvi_id"].notna().sum()
    n_exact = (
        out.dropna(subset=["region_name"])
        .assign(
            regs_n=lambda d: d["city"].map(normalize_city),
            zhvi_n=lambda d: d["region_name"].map(normalize_city),
        )
        .query("regs_n == zhvi_n")
        .shape[0]
    )
    unmatched = out.loc[out["zhvi_id"].isna(), ["city", "state"]]

    print(f"Wrote {len(out)} rows to {OUT_PATH}")
    print(f"  Matched: {n_matched} (exact normalized: {n_exact})")
    print(f"  Unmatched: {len(unmatched)}")
    if len(unmatched):
        print(unmatched.to_string(index=False))
    alias = out[
        out["zhvi_id"].notna()
        & (out["city"].map(normalize_city) != out["region_name"].map(normalize_city))
    ]
    if len(alias):
        print("\nNon-exact accepted matches:")
        print(alias[["city", "state", "region_name", "zhvi_id"]].to_string(index=False))


if __name__ == "__main__":
    main()
