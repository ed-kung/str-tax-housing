"""Write the New York, NY entry into AGENT_DATA_PATH/str_regulations.json.

Fills legislative_history plus the Airbnb tax-collection and data-sharing fields for
the first city in the file lacking `agent_checked`.
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY, STATE = "New York", "NY"


def measures(
    registration="no change",
    rental_type="no change",
    time="no change",
    unit_type="no change",
    host_presence="no change",
    primary_residence="no change",
    nuisance="no change",
    host_compliance="no change",
    platform_compliance="no change",
    fees_taxes_fines="no change",
):
    return {
        "registration_requirements": registration,
        "rental_type_restrictions": rental_type,
        "time_restrictions": time,
        "unit_type_restrictions": unit_type,
        "host_presence_requirements": host_presence,
        "primary_residence_requirements": primary_residence,
        "nuisance_requirements": nuisance,
        "host_compliance_requirements": host_compliance,
        "platform_compliance_requirements": platform_compliance,
        "fees_taxes_fines": fees_taxes_fines,
    }


LEGISLATIVE_HISTORY = [
    {
        "title": "Chapter 225 of the Laws of 2010 (S6873-B / A10008-B), the \"Illegal Hotel Law\" - amendments to the Multiple Dwelling Law and the NYC Administrative Code",
        "jurisdiction": "New York State",
        "passage_date": "2010-07-16",
        "effective_date": "2011-05-01",
        "enforcement_date": "2011-05-01",
        "summary": "Became law July 16, 2010 with Governor Paterson's approval; a chapter amendment agreed at signing pushed the effective date to May 1, 2011. Deleted the phrase \"as a rule\" from MDL Sec. 4(8)(a) so that dwelling units in Class A multiple dwellings (three or more units) may be used only for \"permanent residence purposes,\" defined as occupancy by the same natural person or family for 30 consecutive days or more. Rentals of fewer than 30 days remain lawful only where the permanent occupant is present and boarders, roomers or lodgers live within the household with free and unobstructed access to the whole unit. One- and two-family homes and legal Class B transient buildings are not covered. This overrode the 330 Continental LLC decision that had blocked city enforcement and is the statutory foundation of New York City's de facto ban on unhosted Airbnb-style rentals. SRO owners sought to enjoin it on takings grounds; the injunction was denied (Dexter 345 Inc. v. Cuomo) and the Mayor's Office of Special Enforcement began issuing transient-occupancy violations under the new definition immediately on May 1, 2011 (about 1,820 of the 1,897 violations issued in 2011 came after that date).",
        "measures": measures(
            rental_type="increase",
            time="increase",
            unit_type="increase",
            host_presence="increase",
            primary_residence="increase",
            host_compliance="increase",
        ),
        "primary_framework": True,
    },
    {
        "title": "Local Law 45 of 2012 (Int. No. 404-A of 2010) - fines for illegal conversions of dwelling units from permanent residences",
        "jurisdiction": "New York City",
        "passage_date": "2012-10-02",
        "effective_date": "2012-12-01",
        "enforcement_date": "2012-12-01",
        "summary": "Passed by the City Council on September 12, 2012 and approved by Mayor Bloomberg on October 2, 2012; effective 60 days after enactment. Added Admin. Code Sec. 28-210.3, making it unlawful for an owner or occupant of a Class A multiple dwelling (or occupancy group J-2/R-2 unit) to use, offer, permit or convert the unit for other than permanent residence purposes, and added item 16 to Sec. 28-201.2.1 so that violations involving more than one dwelling unit, or repeat violations at the same unit or building, are classified as \"immediately hazardous.\" That classification carries substantially higher civil penalties (roughly $1,000-$25,000) and allows faster Department of Buildings and OSE action including vacate orders. It changed the consequences of violating the 2010 state law rather than what rentals are legal.",
        "measures": measures(host_compliance="increase", fees_taxes_fines="increase"),
        "primary_framework": False,
    },
    {
        "title": "Chapter 396 of the Laws of 2016 (S6340-A / A8704-C) - advertising ban for illegal short-term rentals (MDL Sec. 121; NYC Admin. Code Sec. 27-287.1)",
        "jurisdiction": "New York State",
        "passage_date": "2016-10-21",
        "effective_date": "2016-10-21",
        "enforcement_date": "2017-01-30",
        "summary": "Signed by Governor Cuomo on October 21, 2016, effective immediately. Added MDL Sec. 121 and NYC Admin. Code Sec. 27-287.1 making it unlawful to advertise the occupancy or use of a Class A multiple dwelling unit for occupancy that would violate the 30-day permanent-residence rule, with civil penalties of up to $1,000 for a first violation, $5,000 for a second and $7,500 for third and subsequent violations, enforced in New York City by the Mayor's Office of Special Enforcement. It does not reach one- and two-family homes or hosted rentals of a spare room. Airbnb sued the State and the City to enjoin it (Airbnb v. Schneiderman); a December 2, 2016 settlement resolved the challenge on the understanding that the law would be enforced against hosts and advertisers rather than against the platform, and OSE issued its first summonses under the law in the week of January 30, 2017 (17 violations against two operators, reported February 6-7, 2017).",
        "measures": measures(
            rental_type="increase",
            host_compliance="increase",
            fees_taxes_fines="increase",
        ),
        "primary_framework": False,
    },
    {
        "title": "Local Law 146 of 2018 (Int. No. 981-A of 2018) - regulation of short-term residential rentals (booking service data reporting)",
        "jurisdiction": "New York City",
        "passage_date": "2018-08-06",
        "effective_date": "2019-02-02",
        "enforcement_date": None,
        "summary": "Passed by the Council July 18, 2018 and approved by Mayor de Blasio August 6, 2018; effective 180 days later. Added Chapter 21 of Title 26 of the Admin. Code requiring booking services (Airbnb, HomeAway/Vrbo and others) to file monthly reports with the Mayor's Office of Special Enforcement listing, for every short-term rental transaction, the rental address, the host's full legal name, address, phone and email, the listing URL, whether the entire unit was rented, nights booked, fees charged and the host's payout account information, with penalties of the greater of $1,500 per listing per reporting period or the platform's prior-year fees for that listing. Airbnb and HomeAway sued; Judge Engelmayer (S.D.N.Y.) preliminarily enjoined the law on January 3, 2019 on Fourth Amendment grounds and it never took effect. The implementing rule was published but never operative, and the requirements were replaced by Local Law 64 of 2020 following the City's settlement with Airbnb, after which the HomeAway case was dismissed as moot (October 7, 2020).",
        "measures": measures(platform_compliance="increase", fees_taxes_fines="increase"),
        "primary_framework": False,
    },
    {
        "title": "Local Law 64 of 2020 (Int. No. 1976 of 2020) - amendments to booking service reporting requirements for short-term rentals",
        "jurisdiction": "New York City",
        "passage_date": "2020-07-07",
        "effective_date": "2021-01-03",
        "enforcement_date": "2021-01-03",
        "summary": "Signed by Mayor de Blasio on July 7, 2020 to implement the City's settlement of Airbnb's challenge to Local Law 146. Amended Chapter 21 of Title 26 of the Admin. Code to narrow reporting: reports are quarterly rather than monthly, and cover only \"qualifying listings\" (entire dwelling units, or accommodations for three or more guests) with more than four rental days in a reporting period; hosts may be given anonymized payout identifiers. Booking services still must disclose the rental address, host name and contact information, listing URL, whether the entire unit was rented and the number of nights rented. The law and OSE's implementing rules took effect January 3, 2021; the initial reporting period ran January 3 to March 31, 2021 with the first report due May 31, 2021, after which reports are due 45 days after each calendar quarter. Airbnb notified hosts of the disclosure requirement and roughly 29,000 hosts left the platform, cutting NYC listings by about 21 percent.",
        "measures": measures(platform_compliance="increase", fees_taxes_fines="increase"),
        "primary_framework": False,
    },
    {
        "title": "Local Law 18 of 2022 (Int. No. 2309-A of 2021), the \"Short-Term Rental Registration Law\"",
        "jurisdiction": "New York City",
        "passage_date": "2022-01-09",
        "effective_date": "2023-01-09",
        "enforcement_date": "2023-09-05",
        "summary": "Passed by the Council December 9, 2021 and enacted January 9, 2022 after Mayor Adams returned it unsigned without a veto. Added Chapters 31 and 32 to Title 26 of the Admin. Code: hosts must register each short-term rental with the Mayor's Office of Special Enforcement and display the registration number, registration is limited to a natural person who is the permanent occupant of the unit, OSE must refuse registration for NYCHA units, units in wholly rent-regulated buildings and units in buildings on a Prohibited Buildings List that owners may self-report to, and booking services may not charge or collect fees for a transaction unless they have verified a valid registration number (or that the unit is exempt) through the City's verification system. Registration costs $145; penalties reach $5,000 per violation for unregistered hosts (or three times illegal revenue) and up to $1,500 per unverified transaction for platforms. The substantive chapters took effect January 9, 2023 and the penalty provisions May 9, 2023; OSE opened the registration portal in March 2023 and, after Airbnb's state-court challenge was dismissed in August 2023, began enforcing platform verification on September 5, 2023, when the major platforms removed unverified listings. More than 3,000 registrations have been granted and over 14,000 buildings placed on the prohibited list; OSE began revocation proceedings against non-compliant registered hosts in April 2025 and filed its first Local Law 18 lawsuit in May 2025.",
        "measures": measures(
            registration="increase",
            unit_type="increase",
            primary_residence="increase",
            host_compliance="increase",
            platform_compliance="increase",
            fees_taxes_fines="increase",
        ),
        "primary_framework": True,
    },
    {
        "title": "Chapter 672 of the Laws of 2024 (S885-C / A4130-C), the statewide short-term rental registry and tax law, as amended by Chapter 99 of the Laws of 2025 (S820 / A5686)",
        "jurisdiction": "New York State",
        "passage_date": "2024-12-21",
        "effective_date": "2025-03-01",
        "enforcement_date": "2025-03-01",
        "summary": "Signed by Governor Hochul on December 21, 2024 (some accounts say December 24) contingent on a chapter amendment, which was signed February 28, 2025 as Chapter 99 of 2025. The registry provisions are county-based and expressly exempt New York City, whose own Local Law 18 registry is recognized, so the law's practical effect for the city is fiscal: it added Tax Law Sec. 1132(m) and related provisions extending state and local sales tax and the New York City $1.50 per night hotel unit fee to short-term rental unit occupancy and making booking services registered New York State sales tax vendors responsible for collecting and remitting that tax on all occupancies they facilitate, with operators relieved of collection when the platform collects. It also requires booking services to report quarterly to the Department of State on bookings by county. Tax collection provisions took effect March 1, 2025 (registry provisions November 22, 2025), and the amendment expressly preserves existing voluntary collection agreements between platforms and municipalities.",
        "measures": measures(
            host_compliance="increase",
            platform_compliance="increase",
            fees_taxes_fines="increase",
        ),
        "primary_framework": False,
    },
]

ENTRY = {
    "city": CITY,
    "state": STATE,
    "legislative_history": LEGISLATIVE_HISTORY,
    "airbnb_tax_collection_date": "2025-03-01",
    "airbnb_tax_collection_date_explanation": (
        "New York City never signed a voluntary collection agreement with Airbnb: the company offered to "
        "collect lodging taxes in 2014 and again in its October 2016 five-point proposal, and city and state "
        "officials rebuffed the offers because a tax deal would legitimize rentals that were illegal under the "
        "Multiple Dwelling Law. City-level collection therefore began only under Chapter 672 of the Laws of 2024 "
        "as amended by Chapter 99 of the Laws of 2025, which made booking services registered New York State "
        "sales tax vendors responsible for collecting sales tax and the New York City hotel unit fee on "
        "short-term rental occupancy effective March 1, 2025. In New York City the tax Airbnb now collects "
        "(7-8.875 percent \"state\" sales tax plus the $1.50 per night New York City Hotel Unit Fee) includes "
        "the city's own 4.5 percent local sales tax and the NYC-specific unit fee, so municipal-level revenue "
        "is being collected. Timing was confirmed against archived versions of Airbnb's New York occupancy tax "
        "help page (airbnb.com/help/article/2319): snapshots from October 2023, May 2024, August 2024, October "
        "2024 and January 1, 2025 list only upstate county hotel/motel occupancy taxes and contain no New York "
        "State or New York City sales tax or unit fee, while the March 17, 2025 snapshot adds the \"State of New "
        "York\" section with the state/local sales tax and the New York City Hotel Unit Fee. This also refutes "
        "secondary sources that date Airbnb's NYC tax collection to the start of Local Law 18 enforcement on "
        "September 5, 2023. Airbnb still does not collect New York City's own 5.875 percent Hotel Room "
        "Occupancy Tax administered by the Department of Finance."
    ),
    "airbnb_data_sharing_date": "2021-01-03",
    "airbnb_data_sharing_date_explanation": (
        "Local Law 64 of 2020 and the Office of Special Enforcement's implementing rules took effect January 3, "
        "2021, and the rules set the initial reporting period as January 3 through March 31, 2021 (first report "
        "due May 31, 2021), so listing- and host-level data from Airbnb first began to be captured for the city "
        "on that date. Earlier steps did not transfer data: Local Law 146 of 2018 would have started monthly "
        "reporting on February 2, 2019 but was preliminarily enjoined on January 3, 2019 and never operated, and "
        "the 2020 settlement in which Airbnb agreed to hand over host data (Airbnb voluntarily dismissed its "
        "suit on July 14, 2020) was the negotiated origin of the reporting regime rather than an actual data "
        "connection. A tighter, two-way connection followed on September 5, 2023, when platforms began querying "
        "the city's Local Law 18 verification system before processing transactions."
    ),
    "agent_checked": 1,
}


def main():
    with JSON_PATH.open() as f:
        data = json.load(f)

    idx = next(
        i for i, item in enumerate(data) if item["city"] == CITY and item["state"] == STATE
    )
    if data[idx].get("agent_checked"):
        raise SystemExit(f"{CITY}, {STATE} already has agent_checked set; aborting.")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(JSON_PATH, JSON_PATH.with_suffix(f".json.{stamp}.bak"))

    data[idx] = ENTRY
    with JSON_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated index {idx}: {CITY}, {STATE} with {len(LEGISLATIVE_HISTORY)} laws.")


if __name__ == "__main__":
    main()
