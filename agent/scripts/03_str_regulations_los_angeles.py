"""Fill in the Los Angeles, CA record in AGENT_DATA_PATH/str_regulations.json.

Research sources are city clerk council files (14-1635-S2, 14-1635-S7, 14-1635-S9,
14-1635-S10, 12-1824-S1), LA City Planning / LAHD / Office of Finance pages,
Airbnb's newsroom, California legislative records, and contemporaneous LA Times
reporting.
"""

import json
import os

from dotenv import load_dotenv

load_dotenv()

JSON_PATH = os.path.join(os.environ["AGENT_DATA_PATH"], "str_regulations.json")

NO_CHANGE = "no change"
INCREASE = "increase"
DECREASE = "decrease"

MEASURE_KEYS = [
    "registration_requirements",
    "rental_type_restrictions",
    "time_restrictions",
    "unit_type_restrictions",
    "host_presence_requirements",
    "primary_residence_requirements",
    "nuisance_requirements",
    "host_compliance_requirements",
    "platform_compliance_requirements",
    "fees_taxes_fines",
]


def measures(**kwargs):
    m = {k: NO_CHANGE for k in MEASURE_KEYS}
    m.update(kwargs)
    return m


LEGISLATIVE_HISTORY = [
    {
        "title": 'Ordinance No. 185451, the "Party House Ordinance" (Loud or Unruly Gatherings) - adding LAMC Section 41.58.1 and amending LAMC Section 11.2.04',
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-02-21",
        "effective_date": "2018-04-15",
        "enforcement_date": "2018-04-15",
        "summary": (
            "Adopted by the City Council on February 21, 2018, approved by Mayor Garcetti on February 27, 2018, "
            "published March 6, 2018 and effective April 15, 2018 (Council File 12-1824-S1). Added LAMC Section 41.58.1 "
            "declaring \"loud or unruly gatherings\" at a residence (or within 500 feet of it) a public nuisance and making "
            "both the property owner and any \"responsible party\" - expressly including any person who rents, leases or is "
            "otherwise in charge of the residence - liable for escalating administrative citations under the City's "
            "Administrative Citation Enforcement program, plus cost recovery for repeat police response. It was written "
            "largely in response to short-term rental \"party houses\" advertised on home-sharing platforms and predates the "
            "City's substantive short-term rental framework. It was later wired directly into short-term rental regulation: "
            "the 2018 Home-Sharing Ordinance suspends a host's registration for 30 days after a loud-or-unruly-gathering "
            "citation, and the required guest Code of Conduct cites Section 41.58.1. Enforcement by LAPD and the "
            "Department of Building and Safety began on the effective date."
        ),
        "measures": measures(
            nuisance_requirements=INCREASE,
            host_compliance_requirements=INCREASE,
            fees_taxes_fines=INCREASE,
        ),
        "primary_framework": False,
    },
    {
        "title": 'Ordinance No. 185931, the "Home-Sharing Ordinance" - amending LAMC Sections 12.03, 12.12.2, 12.13, 12.13.5, 12.22, 12.24, 19.01 and 21.7.2',
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-12-11",
        "effective_date": "2019-07-01",
        "enforcement_date": "2019-11-01",
        "summary": (
            "Adopted by the City Council on December 11, 2018 after roughly four years of hearings (Council File 14-1635-S2), "
            "concurred in by Mayor Garcetti and published December 21, 2018, with a delayed effective date of July 1, 2019. "
            "Added LAMC Section 12.22 A.32, which for the first time affirmatively permits short-term rentals (stays of 30 "
            "consecutive days or less) as an accessory use in residential zones, where they had previously been prohibited "
            "outright but essentially unenforced. Home-sharing is limited to the host's primary residence (occupied at least "
            "six months of the year), capped at 120 nights per calendar year unless the host obtains a discretionary Extended "
            "Home-Sharing registration, and limited to one registration per person and one booking at a time. Hosts must "
            "register with the Department of City Planning, display the registration number in every advertisement, obtain "
            "landlord consent if a renter, obtain a Transient Occupancy Registration Certificate unless listing exclusively on "
            "a platform with a Platform Agreement, keep three years of records, provide safety equipment and a guest Code of "
            "Conduct, and observe occupancy and noise limits (no more than two persons per habitable room, no amplified music "
            "after 10 p.m., no evening outdoor gatherings over eight people, no events). Units subject to the Rent "
            "Stabilization Ordinance, income-restricted or covenanted affordable units, Ellis Act-withdrawn units, RSO units "
            "converted to single-family homes within five years, and post-January 2017 accessory dwelling units the host does "
            "not live in are all ineligible. Hosting platforms may not complete booking transactions for unregistered listings "
            "or for hosts past their night cap, must give the City a responsible contact, and must report listing- and "
            "booking-level data to City Planning at least monthly, unless they instead follow Appendix A of the Administrative "
            "Guidelines or sign a Platform Agreement. Fines run to $500 per day (or twice the nightly rate) for advertising "
            "violations and $2,000 per day for exceeding the night cap, and two verified citations trigger revocation and a "
            "one-year bar. City Planning issued Administrative Guidelines on June 28, 2019 and opened the registration portal "
            "on the July 1, 2019 effective date, starting a 120-day implementation and outreach phase; citations and fines "
            "began on the November 1, 2019 enforcement date, when unregistered listings had to come down. Application of the "
            "ordinance in the Venice coastal zone without a coastal development permit was challenged in Coastal Act "
            "Protectors v. City of Los Angeles, but the trial court denied relief and the Court of Appeal affirmed on "
            "February 24, 2022 as time-barred, so enforcement was never suspended. Listings advertising City properties fell "
            "roughly 74 percent between 2019 and 2023, from about 36,600 to about 9,500."
        ),
        "measures": measures(
            registration_requirements=INCREASE,
            rental_type_restrictions=INCREASE,
            time_restrictions=INCREASE,
            unit_type_restrictions=INCREASE,
            primary_residence_requirements=INCREASE,
            nuisance_requirements=INCREASE,
            host_compliance_requirements=INCREASE,
            platform_compliance_requirements=INCREASE,
            fees_taxes_fines=INCREASE,
        ),
        "primary_framework": True,
    },
    {
        "title": "Ordinance No. 186197 - creating the Short-Term Rental Enforcement Trust Fund (Los Angeles Administrative Code Sections 5.576 and 5.576.1)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2019-06-18",
        "effective_date": "2019-07-28",
        "enforcement_date": "2019-07-28",
        "summary": (
            "Adopted by the City Council on June 18, 2019, concurred in by the Mayor and published June 26, 2019, effective "
            "July 28, 2019 (Council File 14-1635-S7, City Attorney report R19-0129). Companion fiscal measure to the "
            "Home-Sharing Ordinance: it added Administrative Code Section 5.576 establishing the Short-Term Rental "
            "Enforcement Trust Fund, administered by the Department of City Planning and funded by ten percent of net "
            "Transient Occupancy Tax revenue attributable to transient uses other than hotels, motels, bed and breakfasts, "
            "transient occupancy residential structures and hostels, plus the home-sharing per-night fee, and restricted "
            "spending to registration, monitoring, citation and complaint-intake activity. Section 5.576.1 authorized the "
            "per-night fee whose amount was left to a later Council resolution; after an NBS fee study the Council set it at "
            "$3.10 per night on November 10, 2020, effective December 1, 2020 with annual CPI adjustment (it reached $3.30 as "
            "of September 1, 2025). Airbnb, as the only platform with a Platform Agreement, collects and remits the fee on "
            "behalf of its hosts; the first remittances arrived in January 2021 and the City collected about $2.24 million in "
            "2021 and $2.18 million in 2022."
        ),
        "measures": measures(fees_taxes_fines=INCREASE),
        "primary_framework": False,
    },
    {
        "title": "Senate Bill 60 (Glazer), Chapter 307, Statutes of 2021 - residential short-term rental ordinances: health or safety infractions: maximum fines (Government Code Section 36900)",
        "jurisdiction": "California",
        "passage_date": "2021-09-24",
        "effective_date": "2021-09-24",
        "enforcement_date": None,
        "summary": (
            "Passed by the Legislature on September 1, 2021, approved by Governor Newsom and chaptered September 24, 2021 as "
            "an urgency statute effective immediately. Amended Government Code Section 36900 to lift the ordinary $100/$200/"
            "$500 administrative infraction caps for violations of a residential short-term rental ordinance that pose a "
            "threat to public health or safety, allowing cities to impose up to $1,500 for a first violation, $3,000 for a "
            "second within a year and $5,000 for each additional violation within a year, subject to a hardship waiver "
            "process; the enhanced fines do not apply to a first-time failure to register or pay a license fee. The bill was "
            "prompted by shootings and violent parties at short-term rentals, including in Los Angeles. It is enabling rather "
            "than self-executing for the City: as of the City Attorney's November 26, 2024 report to Council File 14-1635-S10, "
            "Los Angeles was still charging $500 per violation under LAMC Section 12.22 A.32(g)(4) and was studying other "
            "mechanisms (advertising fines tied to nightly rate, square-footage-based Administrative Citation Enforcement "
            "fines, misdemeanor filings) to raise penalties, so the higher SB 60 maximums have not been put into active use in "
            "the City of Los Angeles."
        ),
        "measures": measures(fees_taxes_fines=INCREASE),
        "primary_framework": False,
    },
]

AIRBNB_TAX_COLLECTION_DATE = "2016-08-01"
AIRBNB_TAX_COLLECTION_DATE_EXPLANATION = (
    "The City of Los Angeles Office of Finance states on its Transient Occupancy Tax Requirements page that "
    "\"Beginning on August 1, 2016, AirBnB has agreed to collect and remit TOT on behalf of property owners within the City "
    "of Los Angeles who utilize their service.\" Airbnb's own newsroom post announcing that it had remitted more than $275 "
    "million to the city likewise says the voluntary collection agreement \"went into effect August 1, 2016\" and covers the "
    "city's 14 percent lodging tax. The three-year agreement was announced by city officials in late June 2016 and reported "
    "the same week by NBC Los Angeles and CBS Los Angeles, which put the first-year revenue estimate at $5.8 million. The tax "
    "is municipal: the 14 percent Transient Occupancy Tax is imposed by the City under LAMC Article 1.7 and administered by "
    "the City's Office of Finance, not by the State or the County. The agreement predates the 2018 Home-Sharing Ordinance, "
    "which later amended LAMC Section 21.7.2 to make home-sharing expressly subject to the TOT and required hosts to obtain a "
    "Transient Occupancy Registration Certificate unless they list exclusively on a platform holding a collection agreement."
)

AIRBNB_DATA_SHARING_DATE = "2019-11-06"
AIRBNB_DATA_SHARING_DATE_EXPLANATION = (
    "The Home-Sharing Ordinance took effect July 1, 2019 and obligated every hosting platform to give City Planning "
    "listing- and booking-level data at least monthly (LAMC Section 12.22 A.32(f)(4)), with enforcement of platform duties "
    "starting November 1, 2019, but the City's own reporting treats the Airbnb Platform Agreement as the point at which the "
    "direct connection was established. The Council adopted the Master Platform Agreement on October 30, 2019; Airbnb signed "
    "its individual agreement on October 31, 2019 (Council File 14-1635-S9); and the Council approved it on November 6, 2019, "
    "with the action final November 8, 2019. City Planning's October 4, 2023 report to Council File 14-1635-S10 states: \"On "
    "November 6, 2019, the City Council approved and the City entered into a platform agreement with the Airbnb hosting "
    "platform. Between the end of 2019 and the beginning of 2020, Airbnb removed thousands of ineligible short-term rental "
    "units from its platform.\" Under that agreement the City transmits a list of categorically ineligible listings (rent "
    "stabilized units, covenanted affordable units, owner-opted-out buildings and recent Ellis Act single-family properties) "
    "that Airbnb must take down, and Airbnb must carry the City registration number field on listings, which is the first "
    "point at which the City could directly act against listings on the platform. Full automation followed later: after a "
    "two-week test rollout, Airbnb launched its use of the City's API on August 31, 2020 (announced by the City and reported "
    "by the Los Angeles Times the same day), under which Airbnb queries the City API at least every 24 hours with listing, "
    "host and booking data and must remove listings within 96 hours of a City removal notice. Airbnb remains the only "
    "platform with a Los Angeles platform agreement and API connection."
)


def main():
    with open(JSON_PATH) as f:
        data = json.load(f)

    idx = next(
        i
        for i, rec in enumerate(data)
        if rec.get("city") == "Los Angeles" and rec.get("state") == "CA"
    )
    rec = data[idx]
    assert not rec.get("agent_checked"), "Los Angeles record already checked"

    rec["legislative_history"] = LEGISLATIVE_HISTORY
    rec["airbnb_tax_collection_date"] = AIRBNB_TAX_COLLECTION_DATE
    rec["airbnb_tax_collection_date_explanation"] = AIRBNB_TAX_COLLECTION_DATE_EXPLANATION
    rec["airbnb_data_sharing_date"] = AIRBNB_DATA_SHARING_DATE
    rec["airbnb_data_sharing_date_explanation"] = AIRBNB_DATA_SHARING_DATE_EXPLANATION
    rec["agent_checked"] = 1

    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"updated record {idx}: {rec['city']}, {rec['state']}")


if __name__ == "__main__":
    main()
