"""Add the Houston, TX short-term-rental legislative history to str_regulations.json.

Writes the "legislative_history", "airbnb_tax_collection_date",
"airbnb_data_sharing_date" and "agent_checked" keys for the Houston entry in
AGENT_DATA_PATH/str_regulations.json, matching the schema already used for the
New York, Los Angeles and Chicago entries.
"""

import json
import os
import shutil
from pathlib import Path

from dotenv import load_dotenv

M = ("registration_requirements", "rental_type_restrictions", "time_restrictions",
     "unit_type_restrictions", "host_presence_requirements",
     "primary_residence_requirements", "host_compliance_requirements",
     "platform_compliance_requirements")


def measures(**kwargs):
    out = {k: "no change" for k in M}
    for k, v in kwargs.items():
        if k not in out:
            raise KeyError(k)
        out[k] = v
    return out


LEGISLATIVE_HISTORY = [
    {
        "title": "Texas House Bill 1905, 84th Legislature (Acts 2015, 84th Leg., R.S., Ch. 1255), Sec. 22(a) - Tax Code Sec. 156.001(b), \"hotel\" includes a short-term rental",
        "jurisdiction": "State of Texas",
        "passage_date": "2015-06-20",
        "effective_date": "2015-09-01",
        "summary": "An omnibus state and local tax bill signed by Governor Abbott on June 20, 2015. Section 22(a) amended Tax Code Sec. 156.001 by adding subsection (b), providing that for purposes of the hotel occupancy tax imposed under Chapter 156 (the 6 percent state tax), Chapter 351 (municipal hotel occupancy taxes), Chapter 352 (county hotel occupancy taxes) \"or other law,\" the term \"hotel\" includes a short-term rental, defined as the rental of all or part of a residential property to a person who is not a permanent resident under Sec. 156.101 (i.e., someone without the right to occupy for 30 consecutive days or more). The bill states the amendment is a clarification of existing law. This is the statutory basis on which Airbnb-style rentals in Houston owe the 6 percent state HOT and the City of Houston's 7 percent municipal HOT (collected by Houston First Corporation); Houston had no STR-specific regulatory ordinance at the time, so this was the only STR-specific legal obligation on Houston hosts until 2026. It affects tax liability and host reporting duties only, not land use, licensing eligibility or rental type.",
        "measures": measures(host_compliance_requirements="increase"),
    },
    {
        "title": "City of Houston Ordinance No. 2025-322 - Code of Ordinances Chapter 28, Article XXIII (Short-Term Rentals)",
        "jurisdiction": "City of Houston",
        "passage_date": "2025-04-16",
        "effective_date": "2026-01-01",
        "summary": "Houston's first short-term rental regulation, passed unanimously by City Council on April 16, 2025 under an emergency clause (final passage on the date of introduction at the Mayor's written request) and taking effect at 12:01 a.m. on January 1, 2026. It adds Chapter 28, Article XXIII, defining a short-term rental as a dwelling unit or portion of one rented or offered for rent for less than 30 consecutive days (excluding boarding homes, bed and breakfasts, hotels, lodging facilities, alternate housing facilities, federal/state-regulated sleeping facilities, and sale-leaseback arrangements). It is unlawful to operate, rent, lease or advertise an STR without a certificate of registration; one certificate is required per unit, valid one year, non-transferable, void on sale, at a $275 annual fee (plus a $33.10 administrative fee). Applications must supply the address, owner/operator/agent contact details, proof of ownership or owner permission, entity documents, 24-hour emergency contact names and numbers, the names and URLs of all booking platforms used in the prior 12 months, an owner acknowledgement that STR use does not violate deed restrictions, HOA rules, bylaws, condominium or lease terms or minimum occupancy duration requirements, proof of annual human trafficking awareness training, a sworn compliance statement, and proof of registration for or remittance of hotel occupancy taxes. Operating rules impose a one-night minimum stay, mandatory payment of HOT under Chapter 44, Article III and state law, a ban on advertising or hosting special events (weddings, receptions, parties, concerts), a requirement that all public listings display the registration number and maximum occupancy, an emergency contact reachable at all times who must respond within one hour, and posting of the certificate inside the unit. Registrations may be denied or revoked for false information, HOT non-payment, two abated nuisances, two noise-ordinance convictions in 12 months, or one conviction for enumerated violent, trafficking, prostitution, firearm or disorderly conduct offenses at the property; three revocations for the same owner within 24 months allows revocation of all their remaining certificates. Platforms must notify Houston hosts of the registration requirement, must require and prominently display the certificate number on listings, may not list an STR without one, and must remove a listing within 10 business days of city notice. Violations carry fines of $100 to $500 per day. A proposed density cap was dropped before passage over legal concerns (following Zaatari v. Austin and the Dallas litigation), and the ordinance imposes no whole-home, owner-occupancy, primary-residence, host-presence, unit-type or annual-night-cap restrictions. Implementation slipped administratively: the registration portal opened October 1, 2025 rather than August 1, active enforcement began April 1, 2026, and platform delisting notices were deferred to January 1, 2027.",
        "measures": measures(
            registration_requirements="increase",
            time_restrictions="increase",
            host_compliance_requirements="increase",
            platform_compliance_requirements="increase",
        ),
    },
    {
        "title": "Texas House Bill 2464, 89th Legislature (2025) - Local Government Code Sec. 229.902, municipal authority over home-based businesses",
        "jurisdiction": "State of Texas",
        "passage_date": "2025-06-12",
        "effective_date": "2025-06-12",
        "summary": "Signed by Governor Abbott and effective immediately on June 12, 2025 (two-thirds vote). It adds Local Government Code Sec. 229.902, barring municipalities from prohibiting or licensing \"no-impact home-based businesses\" while preserving their power to require compliance with fire, building, health, sanitation, traffic, waste, pollution and noise rules. Sec. 229.902(d)(2) expressly provides that the section does not prohibit a municipality from adopting or enforcing an ordinance regulating the operation of a short-term rental unit. Texas has never enacted STR preemption (HB 2665 in 2023 was reduced to an interim study; SB 1592/HB 2433 on platform tax collection died in 2025), and the main statewide constraints on city STR rules remain judicial (Zaatari v. City of Austin, City of Grapevine v. Muns, the Dallas injunction). HB 2464 therefore neither loosens nor tightens Houston's STR rules; it removes a potential preemption argument against Ordinance No. 2025-322, which took effect roughly six months later.",
        "measures": measures(),
    },
]

HOUSTON = {
    "legislative_history": LEGISLATIVE_HISTORY,
    "airbnb_tax_collection_date": "2019-07-01",
    "airbnb_data_sharing_date": None,
    "agent_checked": True,
}


def main():
    load_dotenv()
    path = Path(os.environ["AGENT_DATA_PATH"]) / "str_regulations.json"
    data = json.loads(path.read_text())

    idx = next(i for i, x in enumerate(data) if not x.get("agent_checked"))
    entry = data[idx]
    if (entry["city"], entry["state"]) != ("Houston", "TX"):
        raise SystemExit(f"first unchecked entry is {entry['city']}, {entry['state']}, not Houston, TX")

    dates = [e["passage_date"] for e in LEGISLATIVE_HISTORY]
    if dates != sorted(dates):
        raise SystemExit("legislative_history is not sorted by passage_date")

    shutil.copy2(path, path.with_suffix(".json.bak"))
    entry.update(HOUSTON)
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"updated index {idx} ({entry['city']}, {entry['state']}) with "
          f"{len(LEGISLATIVE_HISTORY)} legislative_history entries -> {path}")


if __name__ == "__main__":
    main()
