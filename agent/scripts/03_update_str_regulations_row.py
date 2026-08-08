"""Update a single city row in AGENT_DATA_PATH/str_regulations.csv.

Edit the CITY/STATE and FIELDS constants below, then run:
    .venv/bin/python agent/scripts/03_update_str_regulations_row.py
"""

import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = os.environ["AGENT_DATA_PATH"]
CSV_PATH = os.path.join(AGENT_DATA_PATH, "str_regulations.csv")

CITY = "New York"
STATE = "NY"

FIELDS = {
    "passage_date": "2018-07-18",
    "effective_date": "2021-01-03",
    "enforcement_cooperation_date": "2020-06-12",
    "tax_cooperation_date": "None",
    "agent_confidence": "High",
    "agent_checked": "True",
    "agent_notes": (
        "First substantial city-level STR law is Local Law 146 of 2018 (Int. 981-A), "
        "passed by the City Council 2018-07-18 and signed by Mayor de Blasio 2018-08-06; "
        "it required booking services (Airbnb, HomeAway, etc.) to report host and transaction "
        "data to the Mayor's Office of Special Enforcement (OSE). Nominal effective date was "
        "2019-02-02, but SDNY preliminarily enjoined the law on 2019-01-03 (Airbnb v. City of "
        "New York) and it never took effect in that form; the reporting regime only took effect "
        "2021-01-03, after the Council enacted the settlement-mandated amendments as Local Law 64 "
        "of 2020 (enacted 2020-07-07), so effective_date is coded 2021-01-03. "
        "Caveats: the binding ban on Airbnb-style rentals in NYC is STATE law (Multiple Dwelling "
        "Law amendment, Ch. 225 of 2010, signed 2010-07-16, effective 2011-05-01), not city "
        "policy; the earliest related city action was Local Law 45 of 2012 (Council passage "
        "2012-09-12, approved 2012-10-02), which only raised fines for illegal conversions rather "
        "than creating an STR regime. The far more binding city regime is Local Law 18 of 2022 "
        "(host registration; Council passage 2021-12-09, became law unsigned 2022-01-09, "
        "enforcement from 2023-09-05). "
        "enforcement_cooperation_date = 2020-06-12, when de Blasio and Airbnb announced a "
        "settlement in which Airbnb dismissed its suit and agreed to quarterly sharing of host "
        "and transaction data for enforcement (implemented via LL 64/2020; data flowed from "
        "2021-01-03). "
        "tax_cooperation_date = None: NYC never entered a voluntary collection agreement with "
        "Airbnb. Airbnb publicly sought one in 2014 and was rebuffed; Airbnb has VCAs with ~37 NY "
        "counties but not NYC. Airbnb collects NY State sales tax and the state-imposed NYC hotel "
        "unit fee under NYS Tax Law booking-service rules, not under any city-Airbnb arrangement, "
        "and the NYC Hotel Room Occupancy Tax is not covered by such an arrangement. "
        "Sources: NYC Council Legistar (Int 0981-2018, Int 1976-2020), local law texts, "
        "nyc.gov/specialenforcement, SDNY opinion of 2019-01-03, NYS Ch. 225 of 2010, "
        "Airbnb newsroom, AP and CityLand coverage of the 2020-06-12 settlement."
    ),
}


def main() -> None:
    df = pd.read_csv(CSV_PATH, dtype=str)
    mask = (df["city"] == CITY) & (df["state"] == STATE)
    if mask.sum() != 1:
        raise ValueError(f"Expected exactly 1 row for {CITY}, {STATE}; found {mask.sum()}")

    for column, value in FIELDS.items():
        df.loc[mask, column] = value

    df.to_csv(CSV_PATH, index=False)
    print(df.loc[mask].to_string())


if __name__ == "__main__":
    main()
