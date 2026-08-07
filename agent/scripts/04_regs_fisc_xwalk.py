"""Build 1:1 crosswalk from regs_unit_list to fisc_unit_list.

For each regs (city, state), pick the best FiSC unit match.
Writes regs_fisc_xwalk.csv to AGENT_DATA_PATH with original column names:
  city, state, fisc_id, city_name, city_types
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
FISC_PATH = MY_DATA_PATH / "raw_data/fisc_unit_list.csv"
OUT_PATH = AGENT_DATA_PATH / "regs_fisc_xwalk.csv"

# Minimum same-state fuzzy ratio to accept a non-exact match.
FUZZY_THRESHOLD = 0.85


def normalize_city(name: str) -> str:
    s = str(name).upper().strip()
    s = s.replace(".", "")
    s = re.sub(r"\bFORT\b", "FT", s)
    s = re.sub(r"\bSAINT\b", "ST", s)
    s = s.replace("-", " ")
    s = re.sub(r"\s+", " ", s)
    return s


def parse_fisc(fisc: pd.DataFrame) -> pd.DataFrame:
    """Keep real FiSC cities; split city_name into state + city."""
    out = fisc[fisc["city_name"].str.contains(": ", na=False)].copy()
    parts = out["city_name"].str.split(": ", n=1, expand=True)
    out["fisc_state"] = parts[0]
    out["fisc_city"] = parts[1]
    out["city_n"] = out["fisc_city"].map(normalize_city)
    return out.reset_index(drop=True)


def score_pair(regs_city_n: str, fisc_city_n: str) -> float:
    """Similarity score in [0, 1], with a bonus for FiSC short-name aliases."""
    if regs_city_n == fisc_city_n:
        return 1.0
    # e.g. Oklahoma City ↔ Oklahoma (FiSC short form)
    if regs_city_n == fisc_city_n + " CITY":
        return 0.95
    return SequenceMatcher(None, regs_city_n, fisc_city_n).ratio()


def best_match(row: pd.Series, fisc: pd.DataFrame) -> dict:
    """Return best fisc columns for one regs row (or nulls if no confident match)."""
    empty = {"fisc_id": pd.NA, "city_name": pd.NA, "city_types": pd.NA}
    cand = fisc[fisc["fisc_state"] == row["state"]]
    if cand.empty:
        return empty

    scored = [
        (score_pair(row["city_n"], r.city_n), r)
        for r in cand.itertuples(index=False)
    ]
    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best = scored[0]
    if best_score < FUZZY_THRESHOLD:
        return empty
    return {
        "fisc_id": best.fisc_id,
        "city_name": best.city_name,
        "city_types": best.city_types,
    }


def main() -> None:
    regs = pd.read_csv(REGS_PATH)
    fisc_raw = pd.read_csv(FISC_PATH)
    assert list(regs.columns) == ["city", "state"]
    assert list(fisc_raw.columns) == ["fisc_id", "city_name", "city_types"]
    assert not regs.duplicated(["city", "state"]).any()

    fisc = parse_fisc(fisc_raw)
    regs = regs.copy()
    regs["city_n"] = regs["city"].map(normalize_city)

    matches = regs.apply(lambda r: best_match(r, fisc), axis=1, result_type="expand")
    out = pd.concat([regs[["city", "state"]], matches], axis=1)
    out["fisc_id"] = pd.to_numeric(out["fisc_id"], errors="coerce").astype("Int64")

    assert len(out) == len(regs)
    assert not out.duplicated(["city", "state"]).any()
    assert list(out.columns) == ["city", "state", "fisc_id", "city_name", "city_types"]

    AGENT_DATA_PATH.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_PATH, index=False)

    n_matched = out["fisc_id"].notna().sum()
    n_exact = (
        out.dropna(subset=["city_name"])
        .assign(
            regs_n=lambda d: d["city"].map(normalize_city),
            fisc_n=lambda d: d["city_name"].str.split(": ", n=1).str[1].map(normalize_city),
        )
        .query("regs_n == fisc_n")
        .shape[0]
    )
    unmatched = out.loc[out["fisc_id"].isna(), ["city", "state"]]

    print(f"Wrote {len(out)} rows to {OUT_PATH}")
    print(f"  Matched: {n_matched} (exact normalized: {n_exact})")
    print(f"  Unmatched: {len(unmatched)}")
    if len(unmatched):
        print(unmatched.to_string(index=False))
    alias = out[
        out["fisc_id"].notna()
        & (
            out["city"].map(normalize_city)
            != out["city_name"].str.split(": ", n=1).str[1].map(normalize_city)
        )
    ]
    if len(alias):
        print("\nNon-exact accepted matches:")
        print(alias[["city", "state", "city_name"]].to_string(index=False))


if __name__ == "__main__":
    main()
