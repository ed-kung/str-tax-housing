"""Add explanation keys for the two Airbnb date fields in str_regulations.json.

For every city already marked `agent_checked`, insert
`airbnb_tax_collection_date_explanation` and `airbnb_data_sharing_date_explanation`
immediately after the date field each one describes. The text summarizes how the
date (or the decision to code it null) was reached, drawn from the per-city
research reports under `agent/reports/`.

Run:
    .venv/bin/python agent/scripts/03_str_regulations_date_explanations.py
"""

import json
import os
import shutil
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = os.environ["AGENT_DATA_PATH"]
JSON_PATH = os.path.join(AGENT_DATA_PATH, "str_regulations.json")

TAX_KEY = "airbnb_tax_collection_date"
DATA_KEY = "airbnb_data_sharing_date"
TAX_EXPL_KEY = f"{TAX_KEY}_explanation"
DATA_EXPL_KEY = f"{DATA_KEY}_explanation"

# (city, state) -> (expected tax date, tax explanation, expected data date, data explanation).
# The expected dates guard against writing an explanation onto a value that has changed.
EXPLANATIONS = {
    ("New York", "NY"): (
        "2025-03-01",
        "New York City never entered a voluntary collection agreement with Airbnb: it declined "
        "Airbnb's 2016 offer of a hotel-tax deal, and Airbnb still does not collect the separate "
        "5.875 percent NYC Hotel Room Occupancy Tax. Collection of a city-level tax began only "
        "under Ch. 656 of the Laws of 2024 as amended by Ch. 99 of 2025, which extended state and "
        "local sales tax and the $1.50 per night NYC hotel unit fee to short-term rental occupancy "
        "and made booking services registered NYS sales tax vendors responsible for collecting it. "
        "The statutory effective date of March 1, 2025 is used; the NYSAC implementation memo says "
        "collections \"may begin\" that day, and the March 25, 2025 date appearing in some trade "
        "coverage refers to the registry provisions rather than to tax collection.",
        "2021-01-03",
        "Local Law 64 of 2020 took effect January 3, 2021, and the Office of Special Enforcement's "
        "rule sets the initial reporting period as January 3 through March 31, 2021 with the first "
        "report due May 31, 2021, so that is when listing- and host-level data actually began to be "
        "captured and reported. The June 12, 2020 settlement of Airbnb's federal suit, in which "
        "Airbnb agreed to hand over host data, is the negotiated origin but transferred no data "
        "itself. Local Law 146 of 2018 would have started monthly reporting on February 2, 2019 but "
        "was preliminarily enjoined on January 3, 2019 and never operated.",
    ),
    ("Los Angeles", "CA"): (
        "2016-08-01",
        "A voluntary collection agreement with the city, announced July 18, 2016 as an initially "
        "three-year deal, under which Airbnb began collecting and remitting the city's 14 percent "
        "Transient Occupancy Tax on its own bookings on August 1, 2016 -- more than two years before "
        "any short-term rental ordinance existed. Airbnb's newsroom reports remitting over $275 "
        "million between August 2016 and June 2023, and holding a TOT collection agreement with the "
        "Office of Finance later became a precondition for signing a Home-Sharing Platform Agreement.",
        "2020-08-31",
        "The date Airbnb went live on the city's Home-Sharing compliance API after a two-week test, "
        "per City Planning's 2021 and 2023 reports to Council; listings fell a further 14 percent "
        "immediately afterward. Two earlier dates were considered and rejected: Council approval of "
        "Airbnb's individual Platform Agreement on November 6, 2019 (final November 8), and Airbnb's "
        "removal of thousands of categorically ineligible listings between late 2019 and early 2020, "
        "which reflected data flowing from the city to Airbnb rather than the reverse. Sustained "
        "Airbnb-to-city listing data for compliance began with the API.",
    ),
    ("Chicago", "IL"): (
        "2015-02-15",
        "Airbnb began collecting Chicago lodging taxes on hosts' behalf on February 15, 2015 under a "
        "voluntary arrangement following the city budget director's November 2014 initiative to "
        "capture the hotel tax on short-term rentals. The date was reported contemporaneously "
        "(Washington Post, January 2015) and is repeated in the short-term-rental policy literature; "
        "it precedes the 2016 Shared Housing Ordinance by more than a year.",
        "2017-03-14",
        "The 2016 Shared Housing Ordinance made Airbnb a licensed short term residential rental "
        "intermediary with twice-monthly unit-list and bi-monthly aggregate reporting duties to "
        "BACP, but those provisions were stayed in the HomeAway/Mendez federal litigation until "
        "March 14, 2017, so no data flowed on the ordinance's original December 17, 2016 date. The "
        "NBER working paper on Chicago home-sharing regulation likewise dates the start of Airbnb's "
        "data sharing with the city to March 2017.",
    ),
    ("Houston", "TX"): (
        "2019-07-01",
        "Airbnb began collecting the City of Houston's 7 percent municipal hotel occupancy tax on "
        "July 1, 2019 under an agreement with Houston First Corporation, the city's designated HOT "
        "collection agent; the date comes from Houston First's HOT FAQs and Airbnb's newsroom "
        "announcement. Airbnb's earlier May 1, 2017 start date under its Texas Comptroller agreement "
        "was not used because it covers only the 6 percent state HOT, not tax collected on behalf of "
        "the city.",
        None,
        "Coded null. Searches surfaced no Airbnb-Houston data-sharing agreement and no Airbnb City "
        "Portal participation. Under Ordinance No. 2025-322 the information flow runs the other way: "
        "the city notifies platforms which listings to remove, and listing identification comes from "
        "the city's Granicus Host Compliance contract rather than from Airbnb.",
    ),
    ("Phoenix", "AZ"): (
        "2017-01-01",
        "Governor Ducey and the Arizona Department of Revenue announced a partnership under which "
        "Airbnb began collecting and remitting state transaction privilege tax, county excise tax and "
        "municipal transient lodging tax -- including Phoenix's -- on January 1, 2017, the day SB 1350 "
        "took effect. Airbnb was the only marketplace doing so until SB 1382 made registration "
        "mandatory for all online lodging marketplaces on January 1, 2019.",
        None,
        "Coded null. No Airbnb City Portal arrangement or memorandum of understanding with Phoenix "
        "was found. The city runs enforcement through its own SHAPE PHX permit portal and the "
        "Neighborhood Services Department, and the platform reporting that does exist under A.R.S. "
        "Sec. 42-5076 goes to the state Department of Revenue in aggregate form and expressly may "
        "not identify individual operators.",
    ),
    ("Philadelphia", "PA"): (
        "2015-07-15",
        "Bill No. 150441-A extended the 8.5 percent Hotel Room Rental Tax to short-term rentals "
        "effective July 1, 2015 and authorized booking agents to collect it, but two Inquirer reports "
        "(July 3, 2015 and June 15, 2016) both state that the city began collecting the tax on July "
        "15, 2015, with Airbnb named as the collecting booking agent; the date of actual collection "
        "is used rather than the ordinance date. A 2018 Department of Revenue post confirms Airbnb "
        "was then the only platform remitting the Hotel Tax on hosts' behalf. Airbnb's separate July "
        "1, 2016 start on Pennsylvania's 6 percent state hotel occupancy tax is a state agreement and "
        "was not used.",
        "2023-03-30",
        "Airbnb declined to hand over host addresses without a formal legal demand, so the city "
        "issued subpoenas; notices Airbnb sent to hosts in late March 2023 state that the company had "
        "to produce responsive documents on March 30, 2023, which is the first documented instance of "
        "Airbnb actually transferring data to the city for compliance and enforcement. Booking agents "
        "have since filed recurring Transaction History Reports with L&I listing host name, property "
        "address, license type and license number, analyzed in the June 2026 City Controller report. "
        "The 2015 ordinance's operator-list-on-request duty and the reporting duty added by Sec. "
        "9-3910(5) in 2021 both predate this but produced no documented transfer.",
    ),
    ("San Antonio", "TX"): (
        "2025-03-10",
        "No voluntary agreement was ever reached -- 2018 talks stalled over Airbnb's request that the "
        "city waive hosts' back taxes -- so city HOT collection was compelled by Sec. 16-1104.01 of "
        "Ordinance 2024-06-13-0433. Implementation slipped past the announced October 1, 2024 target; "
        "the city's own short-term rental page and its January 2026 fact sheet both state that "
        "platforms began paying City HOT on operators' behalf effective March 10, 2025, when the "
        "revised reporting portal launched. The first covered receipts were February 2025 bookings, "
        "so 2025-02-01 is a defensible alternative coding. Airbnb's May 1, 2017 Comptroller agreement "
        "covers only the 6 percent state HOT and was not used.",
        None,
        "Coded null. No evidence was found that Airbnb has ever given San Antonio listing- or "
        "host-level data. The 2024 ordinance's compliance mechanism runs from the city to the "
        "platform (the city identifies listings by URL and the platform must remove them within ten "
        "business days), the city relies on a third-party vendor (Avenu Insights / Host Compliance) "
        "to detect unpermitted listings, and the city's March 2025 platform-deductions webinar states "
        "that platform HOT is remitted to the city with no detail and no property-level credit.",
    ),
    ("San Diego", "CA"): (
        "2015-07-01",
        "Airbnb began collecting the city's 10.5 percent Transient Occupancy Tax and the 0.55 percent "
        "Tourism Marketing District assessment from guests on July 1, 2015 under a voluntary "
        "collection agreement, at a time when the city was pursuing hosts for back taxes. This is "
        "roughly eight years before platform collection became mandatory, which happened under SDMC "
        "Sec. 510.0201(e) as the 2021 STRO ordinance became enforceable.",
        "2023-05-01",
        "SDMC Sec. 510.0201(f) requires hosting platforms to file monthly listing-level reports "
        "(license number, responsible person, street address, days booked), and that obligation "
        "attached when the STRO license requirement became enforceable on May 1, 2023, with the first "
        "report due June 30, 2023. An October 2021 City Treasurer memo confirms that before then "
        "platforms remitted TOT in aggregate and gave the city no host-level data. The ordinance's "
        "2021 passage date was not used because Coastal Commission certification delayed "
        "enforceability by about two years.",
    ),
    ("Dallas", "TX"): (
        None,
        "Coded null. Airbnb has never had a voluntary collection agreement with the City of Dallas: "
        "one was being drafted in August 2016 but was never executed, and renewed pushes in February "
        "2022 and a June 2023 council directive to the city manager also produced nothing. The 9 "
        "percent city HOT is host-remitted through the City Controller's Office (dallas.munirevs.com). "
        "Airbnb's May 1, 2017 Comptroller agreement covers only the 6 percent Texas state HOT, which "
        "is not tax collected on behalf of the city.",
        None,
        "Coded null. The only data-sharing mechanism Dallas ever adopted is the monthly platform "
        "report required by City Code Sec. 42B-14(c), part of the Ch. 42B ordinance that has been "
        "enjoined since December 6, 2023 and has never been enforced. The city instead identifies "
        "listings with third-party data-scraping software, which the Controller's Office credits with "
        "recovering roughly $5.5 million from non-remitting operators since 2020.",
    ),
}


def insert_after(record: dict, anchor: str, key: str, value: str) -> dict:
    """Return a copy of record with key inserted immediately after anchor."""
    out = {}
    for k, v in record.items():
        if k == key:
            continue
        out[k] = v
        if k == anchor:
            out[key] = value
    if key not in out:
        raise KeyError(f"anchor {anchor!r} not found in record")
    return out


def main() -> None:
    with open(JSON_PATH) as f:
        records = json.load(f)

    checked = [r for r in records if r.get("agent_checked")]
    missing = {(r["city"], r["state"]) for r in checked} - set(EXPLANATIONS)
    if missing:
        raise ValueError(f"No explanation written for checked cities: {sorted(missing)}")

    backup = f"{JSON_PATH}.{datetime.now():%Y%m%d-%H%M%S}.bak"
    shutil.copy2(JSON_PATH, backup)

    updated = []
    for record in records:
        key = (record.get("city"), record.get("state"))
        if not record.get("agent_checked") or key not in EXPLANATIONS:
            updated.append(record)
            continue

        tax_date, tax_expl, data_date, data_expl = EXPLANATIONS[key]
        if record.get(TAX_KEY) != tax_date or record.get(DATA_KEY) != data_date:
            raise ValueError(
                f"{key}: dates in the file ({record.get(TAX_KEY)}, {record.get(DATA_KEY)}) "
                f"do not match the researched values ({tax_date}, {data_date})"
            )

        record = insert_after(record, TAX_KEY, TAX_EXPL_KEY, tax_expl)
        record = insert_after(record, DATA_KEY, DATA_EXPL_KEY, data_expl)
        updated.append(record)
        print(f"annotated {key[0]}, {key[1]}")

    with open(JSON_PATH, "w") as f:
        json.dump(updated, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"backup: {backup}")


if __name__ == "__main__":
    main()
