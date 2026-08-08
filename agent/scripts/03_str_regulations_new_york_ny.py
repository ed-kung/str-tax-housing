"""Add short-term-rental legislative history for New York, NY.

Updates the first unchecked entry in AGENT_DATA_PATH/str_regulations.json.
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY = "New York"
STATE = "NY"

LEGISLATIVE_HISTORY = [
    {
        "title": "Chapter 225 of the Laws of 2010 (S6873-B / A10008-B), \"Illegal Hotel Law\" / \"Home Protection Law\" - amendments to the Multiple Dwelling Law",
        "jurisdiction": "New York State",
        "passage_date": "2010-07-16",
        "effective_date": "2011-05-01",
        "summary": (
            "Amended MDL Sec. 4(8)(a) by deleting the phrase \"as a rule\" so that dwelling units in Class A "
            "multiple dwellings (buildings with three or more units) may be occupied only for \"permanent "
            "residence purposes,\" defined as occupancy by the same person or household for 30 consecutive days "
            "or more. Rentals of fewer than 30 days are permitted only when the permanent occupant is present "
            "and the guests have free access to the whole unit (i.e., hosted stays with boarders, roomers or "
            "lodgers). One- and two-family homes and legal Class B transient buildings are not covered. This is "
            "the statutory foundation of New York City's de facto ban on unhosted Airbnb-style rentals; it also "
            "eliminated ambiguity that had blocked city enforcement after the 330 Continental LLC decision."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "increase",
            "time_restrictions": "increase",
            "unit_type_restrictions": "increase",
            "host_presence_requirements": "increase",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "no change",
        },
    },
    {
        "title": "Local Law 45 of 2012 (Int. No. 404-A of 2010) - fines for illegal conversions of dwelling units from permanent residences",
        "jurisdiction": "New York City",
        "passage_date": "2012-10-02",
        "effective_date": "2012-12-02",
        "summary": (
            "Passed by the City Council on September 12, 2012 and approved by Mayor Bloomberg on October 2, "
            "2012; effective 60 days after enactment. Added Admin. Code Sec. 28-210.3 prohibiting the illegal "
            "conversion of permanent residential units to transient use, set civil penalties of roughly "
            "$1,000-$25,000, and classified conversions involving more than one dwelling unit (or repeat "
            "violations at the same unit or building) as \"immediately hazardous\" under Sec. 28-201.2.1, which "
            "permits higher fines and faster enforcement by the Department of Buildings and the Mayor's Office "
            "of Special Enforcement. It did not change what rentals are legal, only the consequences of "
            "violating the 2010 state law."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "no change",
        },
    },
    {
        "title": "Chapter 396 of the Laws of 2016 (A8704-C / S6340-A) - advertising ban for illegal short-term rentals",
        "jurisdiction": "New York State",
        "passage_date": "2016-10-21",
        "effective_date": "2016-10-21",
        "summary": (
            "Signed by Governor Cuomo on October 21, 2016 and effective immediately. Added MDL Sec. 121 and "
            "NYC Admin. Code Sec. 27-287.1 making it unlawful to advertise the occupancy or use of a Class A "
            "multiple dwelling unit for other than permanent residence purposes, with civil penalties of up to "
            "$1,000 for a first violation, $5,000 for a second, and $7,500 for third and subsequent violations. "
            "Enforcement in New York City is assigned to the Mayor's Office of Special Enforcement. It does not "
            "apply to one- and two-family homes or to hosted rentals of a spare room while the resident is "
            "present. Airbnb sued immediately; a December 2, 2016 settlement confirmed the city would enforce "
            "the law against hosts/advertisers rather than against the platform."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "increase",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "increase",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "no change",
        },
    },
    {
        "title": "Local Law 146 of 2018 (Int. No. 981-A) - regulation of short-term residential rentals (booking service data reporting)",
        "jurisdiction": "New York City",
        "passage_date": "2018-08-06",
        "effective_date": "2019-02-02",
        "summary": (
            "Passed by the Council July 18, 2018 and signed by Mayor de Blasio August 6, 2018. Added Admin. "
            "Code Ch. 21 of Title 26, requiring booking services (Airbnb, HomeAway/Vrbo, etc.) to file monthly "
            "transaction reports with the Mayor's Office of Special Enforcement listing the address of each "
            "short-term rental, the host's full legal name, address, phone and email, listing URL, whether the "
            "entire unit was rented, nights booked, platform fees, and host payout account information. "
            "Penalties were the greater of $1,500 per listing per period or the prior year's fees for that "
            "listing. Scheduled to take effect February 2, 2019, but Judge Engelmayer (S.D.N.Y.) preliminarily "
            "enjoined it on January 3, 2019 on Fourth Amendment grounds, so it never actually operated; it was "
            "superseded by Local Law 64 of 2020."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "Local Law 64 of 2020 (Int. No. 1976) - requiring booking services to report short-term housing rental transactions",
        "jurisdiction": "New York City",
        "passage_date": "2020-07-07",
        "effective_date": "2021-01-03",
        "summary": (
            "Enacted July 7, 2020 to implement the June 12, 2020 settlement of Airbnb's federal challenge to "
            "Local Law 146. It replaced monthly reporting on all listings with quarterly reporting on "
            "\"qualifying listings\" only - listings that offer (or appear to offer) an entire dwelling unit or "
            "that accommodate three or more guests - and exempted listings booked four or fewer nights in a "
            "quarter and listings in exempt Class B multiple dwellings. Reports still include the rental "
            "address, host identity and contact information, listing URL, nights booked and host payouts, and "
            "are due within 45 days of quarter end. Relative to the enjoined 2018 law it narrowed platform "
            "obligations, but relative to the status quo in force it imposed the city's first operative "
            "platform data-reporting duty."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "Local Law 18 of 2022 (Int. No. 2309-A of 2021), \"Short-Term Rental Registration Law\"",
        "jurisdiction": "New York City",
        "passage_date": "2022-01-09",
        "effective_date": "2023-09-05",
        "summary": (
            "Passed by the Council December 9, 2021 and enacted January 9, 2022 after the mayor returned it "
            "unsigned. Added Admin. Code Ch. 31 and 32 of Title 26. Hosts must register each short-term rental "
            "with the Mayor's Office of Special Enforcement ($145 fee), post the registration number in all "
            "advertisements, display the registration certificate and exit diagram in the unit, and retain "
            "transaction records. Registration is limited to permanent occupants, capped at one registration "
            "per host, denied for rent-regulated and NYCHA units and for buildings on a new Prohibited "
            "Buildings List (over 21,000 buildings), and conditioned on the host being present with no more "
            "than two guests and no locks on interior doors. Booking services are barred from processing "
            "transactions for unverified listings. Statutory effective dates were 12 and 16 months after "
            "enactment; OSE's implementing rules took effect March 6, 2023 (applications opened) and platform "
            "verification enforcement began September 5, 2023, which is the operative date used here. NYC "
            "Airbnb listings fell roughly 70-90 percent afterward."
        ),
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "increase",
            "time_restrictions": "no change",
            "unit_type_restrictions": "increase",
            "host_presence_requirements": "increase",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "Chapter 656 of the Laws of 2024 (S885-C / A4130-C) as amended by Chapter 99 of the Laws of 2025 - statewide short-term rental registry and sales tax on short-term rental unit occupancy",
        "jurisdiction": "New York State",
        "passage_date": "2024-12-24",
        "effective_date": "2025-03-01",
        "summary": (
            "Signed December 24, 2024 and amended by a chapter amendment signed February 28, 2025. Extended "
            "New York State and local sales tax and the $1.50 per night New York City unit fee to short-term "
            "rental unit occupancy effective March 1, 2025, and made booking services registered sales tax "
            "vendors responsible for collecting and remitting that tax on the bookings they facilitate "
            "(relieving hosts who book only through such platforms). It also created a statewide short-term "
            "rental registry administered through counties, with registry provisions effective in fall 2025, "
            "but New York City is expressly exempt from the county registry requirement because Local Law 18 "
            "already provides one. For New York City the practical effect is on tax collection rather than on "
            "registration or land use."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
]

# Airbnb has no voluntary occupancy-tax agreement with New York City; NYC declined
# Airbnb's 2016 offer. Collection began only when Ch. 656 of 2024 (as amended by
# Ch. 99 of 2025) made booking services registered NYS sales tax vendors and applied
# the NYC $1.50/night unit fee to short-term rental occupancy on 2025-03-01. Airbnb
# still does not collect the separate 5.875% NYC Hotel Room Occupancy Tax.
AIRBNB_TAX_COLLECTION_DATE = "2025-03-01"

# Local Law 64 of 2020 took effect 2021-01-03, the start of the initial reporting
# period for booking services; the first quarterly report to the Mayor's Office of
# Special Enforcement covered 2021-01-03 through 2021-03-31 and was due 2021-05-31.
AIRBNB_DATA_SHARING_DATE = "2021-01-03"


def main() -> None:
    with JSON_PATH.open() as f:
        records = json.load(f)

    target = next(
        r for r in records if r["city"] == CITY and r["state"] == STATE
    )
    if target.get("agent_checked"):
        raise SystemExit(f"{CITY}, {STATE} is already marked agent_checked")

    target["legislative_history"] = LEGISLATIVE_HISTORY
    target["airbnb_tax_collection_date"] = AIRBNB_TAX_COLLECTION_DATE
    target["airbnb_data_sharing_date"] = AIRBNB_DATA_SHARING_DATE
    target["agent_checked"] = True

    with JSON_PATH.open("w") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} laws recorded")


if __name__ == "__main__":
    main()
