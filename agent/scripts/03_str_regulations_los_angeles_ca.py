"""Add short-term-rental legislative history and Airbnb cooperation dates for Los Angeles, CA.

Updates the Los Angeles entry in AGENT_DATA_PATH/str_regulations.json and marks it checked.
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY = "Los Angeles"
STATE = "CA"

LEGISLATIVE_HISTORY = [
    {
        "title": "Ordinance No. 185,451 (Council File 12-1824-S1), \"Party House\" ordinance - LAMC Sec. 41.58.1, Loud or Unruly Gatherings",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-02-21",
        "effective_date": "2018-04-15",
        "summary": (
            "Passed by the City Council February 21, 2018, approved by Mayor Garcetti February 27, 2018, "
            "posted March 6, 2018 and effective April 15, 2018. Added LAMC Sec. 41.58.1, declaring a loud or "
            "unruly gathering at a residence a public nuisance and making both the property owner and the "
            "responsible party (defined to include any person who rents or leases the residence) liable for "
            "escalating administrative fines of $100, $500, $1,000, $2,000, $4,000 and $8,000, applied across "
            "different residences owned or rented by the same person. A police-posted notice must remain on the "
            "front door for 30 days and an absentee owner becomes citable for later violations once served. "
            "This is a general nuisance ordinance rather than a short-term rental regime - its text says nothing "
            "about short-term rentals - but it grew out of Council File 12-1824 on commercial party houses, many "
            "of them operated as short-term rentals, and it was the city's only enforcement tool aimed at that "
            "conduct in the year before the Home-Sharing Ordinance took effect."
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
        "title": "Ordinance No. 185,931 (Council File 14-1635-S2), \"Home-Sharing Ordinance\" - LAMC Sec. 12.22 A.32",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-12-11",
        "effective_date": "2019-07-01",
        "summary": (
            "Adopted by the City Council December 11, 2018 after a legislative process that began with a June "
            "2015 Council motion and roughly ten public hearings, approved by Mayor Garcetti December 17, 2018, "
            "published December 21, 2018, effective July 1, 2019, with enforcement deferred to November 1, 2019 "
            "to allow a four-month registration window. Amended LAMC Secs. 12.03, 12.12.2, 12.13, 12.13.5, "
            "12.22, 12.24, 19.01 and 21.7.2 and added Sec. 12.22 A.32. Because the zoning code already barred "
            "transient occupancy of 30 days or less in most residential zones (confirmed in Chen v. Kraft "
            "(2016)), the ordinance both created the first legal pathway for Airbnb-style rentals and imposed "
            "the city's first enforceable regime on a market that had grown to roughly 36,600 listings without "
            "meaningful oversight. Key terms: home-sharing is an accessory use permitted only in the host's "
            "primary residence, defined as the sole residence where the host lives at least six months of the "
            "year; a cap of 120 rented days per calendar year unless the host obtains an Extended Home-Sharing "
            "registration (administrative clearance, or discretionary review with a public hearing if the host "
            "has recent citations); annual registration with the Department of City Planning, with the "
            "registration number displayed on every advertisement; a prior Transient Occupancy Tax registration "
            "certificate; one registration and one booked listing per host at a time; a per-night fee on every "
            "booked night, with the amount left to a later Council action; and categorical exclusion of units "
            "subject to the Rent Stabilization Ordinance, covenanted or income-restricted affordable units, "
            "units withdrawn under the Ellis Act within five years, RSO units converted to single-family homes "
            "within five years, accessory dwelling units permitted on or after January 1, 2017 that are not the "
            "host's primary residence, and any space not approved for residential use. Tenants need written "
            "landlord approval. Hosting platforms may not complete booking transactions for unregistered, "
            "over-cap or multiple listings and must provide booking data to the city, unless they comply with "
            "the administrative guidelines or sign a Platform Agreement; the ordinance also wrote hosting "
            "platforms into the Transient Occupancy Tax code. The ordinance does not require the host to be "
            "present during a stay and does not distinguish private-room from whole-unit rentals, so whole-home "
            "rental of a registered primary residence remains legal within the night cap. City listings fell "
            "roughly 74 percent from 36,600 in 2019 to about 9,500 in 2023."
        ),
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "no change",
            "time_restrictions": "increase",
            "unit_type_restrictions": "increase",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "City Council resolution adopting Appendix A of the Home-Sharing Administrative Guidelines and the Master Platform Agreement (Council Files 14-1635-S2 and 14-1635-S9)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2019-10-30",
        "effective_date": "2019-11-01",
        "summary": (
            "LAMC Sec. 12.22 A.32(f)(6) let the Council specify by resolution how hosting platforms satisfy their "
            "statutory duties, and Sec. 12.22 A.32(i) makes the resulting Administrative Guidelines binding "
            "(\"No one shall fail to comply\"), so this is enacted regulation rather than a recommendation. The "
            "Council adopted Appendix A and the Master Platform Agreement template on October 30, 2019, two days "
            "before Home-Sharing Ordinance enforcement began on November 1, 2019. Platforms may satisfy their "
            "obligations three ways: follow the ordinance's default duties; follow Appendix A, which offers an "
            "application programming interface method (query the city database at each booking, transmitting "
            "host name and identifier, street address, registration number and nights booked) or a manual weekly "
            "spreadsheet method with takedown of unpermitted listings within two business days; or sign a "
            "Platform Agreement. Only a platform that already holds a Transient Occupancy Tax collection "
            "agreement with the Office of Finance and agrees to collect the per-night fee may sign a Platform "
            "Agreement, and each individual agreement needs separate Council approval. Under an agreement the "
            "platform must remove city-identified categorically ineligible listings and, once the interface is "
            "live, stop bookings and block calendars within 96 hours of a city removal notice."
        ),
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "no change",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "Ordinance No. 186,197 (Short-Term Rental Enforcement Trust Fund, LAAC Sec. 5.576.1) and the City Council resolution of November 10, 2020 setting the Home-Sharing per-night fee (Council File 14-1635-S7)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2020-11-10",
        "effective_date": "2020-12-01",
        "summary": (
            "The Home-Sharing Ordinance required every booked home-sharing night to carry a per-night fee under "
            "LAMC Sec. 12.22 A.32(e)(5) but left the amount to a later resolution. The Council first created the "
            "receiving fund by ordinance: Ordinance No. 186,197 was adopted June 18, 2019, published June 26, "
            "2019 and effective July 28, 2019, adding the Short-Term Rental Enforcement Trust Fund to the "
            "Administrative Code. After a consultant fee study the Council set the rate at $3.10 per night on "
            "November 10, 2020, effective December 1, 2020, indexed annually to the Los Angeles-Long Beach-"
            "Anaheim CPI-U; it stood at $3.30 as of September 1, 2025. The fee funds registration processing, "
            "monitoring, citation and litigation work. Platforms with a Platform Agreement must collect and remit "
            "it for their hosts, which in practice means Airbnb; hosts on other platforms self-report through the "
            "city portal, and City Planning estimated their compliance at about 35 percent. The fee is on top of "
            "the 14 percent Transient Occupancy Tax."
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
        "title": "Senate Bill 60 (Chapter 307, Statutes of 2021) - residential short-term rental ordinances: health or safety infractions: maximum fines",
        "jurisdiction": "State of California",
        "passage_date": "2021-09-24",
        "effective_date": "2021-09-24",
        "summary": (
            "Passed by the Legislature September 1, 2021, approved by Governor Newsom and chaptered September 24, "
            "2021 as an urgency statute effective immediately. Amended Government Code Secs. 25132 and 36900 to "
            "let a city raise the maximum fine for an infraction of its short-term rental ordinance that poses a "
            "threat to public health or safety to $1,500 for a first violation, $3,000 for a second within a "
            "year and $5,000 for each additional violation within a year, far above the general $100/$200/$500 "
            "infraction caps. The higher fines do not apply to a first-time failure to register or to pay a "
            "business license fee, and the jurisdiction must offer a hardship waiver. Prompted by fatal "
            "shootings at short-term rental party houses in Orinda and elsewhere, including Los Angeles. This is "
            "enabling legislation: it raises the ceiling on penalties Los Angeles may attach to Home-Sharing "
            "Ordinance violations without changing what conduct is permitted."
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
        "title": "Assembly Bill 537 (Chapter 805, Statutes of 2023) - short-term lodging: advertising: rates",
        "jurisdiction": "State of California",
        "passage_date": "2023-10-13",
        "effective_date": "2024-07-01",
        "summary": (
            "Signed by Governor Newsom October 13, 2023, effective January 1, 2024 and operative July 1, 2024. "
            "Added Business and Professions Code Sec. 17568.6, barring any place of short-term lodging and any "
            "website, application or centralized platform that advertises one from displaying a room rate that "
            "omits mandatory fees, and requiring the total price including all government taxes and fees to be "
            "shown before the consumer reserves. It expressly covers short-term rentals of 30 consecutive days "
            "or less booked through a platform, so it reaches Airbnb listings in Los Angeles, and the "
            "$10,000-per-violation civil penalty is enforceable by the Los Angeles City Attorney among others. "
            "It is a price-disclosure mandate rather than a land use, registration or occupancy rule."
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
        "title": "Ordinance No. 188,796 (Council File 09-0969-S4) - comprehensive City Planning fee update, including Home-Sharing registration fees",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2025-12-22",
        "effective_date": "2026-02-23",
        "summary": (
            "Council action final December 22, 2025, ordinance published December 30, 2025, effective February "
            "23, 2026. A comprehensive update of LAMC Article 9 and 15 planning fees following City Planning's "
            "2025 fee study, it raised the cost of participating in the Home-Sharing program roughly five-fold: "
            "regular Home-Sharing registration and annual renewal from $89 to $441, Extended Home-Sharing "
            "administrative clearance and renewal from $850 to $883, and Extended Home-Sharing discretionary "
            "review from $5,660 to $12,798. It changed no substantive eligibility rule, but it is a binding "
            "ordinance that materially raised the price of lawful registration, particularly for hosts seeking "
            "to exceed the 120-night cap."
        ),
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "no change",
        },
    },
]

AIRBNB_TAX_COLLECTION_DATE = "2016-08-01"
AIRBNB_DATA_SHARING_DATE = "2020-08-31"


def main() -> None:
    with JSON_PATH.open() as f:
        records = json.load(f)

    target = next(r for r in records if r["city"] == CITY and r["state"] == STATE)
    if target.get("agent_checked"):
        raise SystemExit(f"{CITY}, {STATE} is already marked agent_checked")

    target["legislative_history"] = LEGISLATIVE_HISTORY
    target["airbnb_tax_collection_date"] = AIRBNB_TAX_COLLECTION_DATE
    target["airbnb_data_sharing_date"] = AIRBNB_DATA_SHARING_DATE
    target["agent_checked"] = True

    with JSON_PATH.open("w") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} legislative entries")


if __name__ == "__main__":
    main()
