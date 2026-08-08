"""Add the Chicago, IL short-term-rental legislative history to str_regulations.json.

Writes the "legislative_history", "airbnb_tax_collection_date",
"airbnb_data_sharing_date" and "agent_checked" keys for the Chicago entry in
AGENT_DATA_PATH/str_regulations.json, matching the schema already used for the
New York and Los Angeles entries.
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
        "title": "Vacation Rental Ordinance (Coun. J. 11-3-10, p. 104527) - new Municipal Code Chapter 4-207 (recodified in 2012 as MCC 4-6-300) and companion Zoning Ordinance amendments",
        "jurisdiction": "City of Chicago",
        "passage_date": "2010-11-03",
        "effective_date": "2011-01-01",
        "summary": "Chicago's first short-term rental regime, adopted after roughly two years of negotiation and 30 drafts led by Ald. Brendan Reilly (42nd) and Ald. Edward Burke (14th); the substitute passed the joint License and Zoning committees in June 2010 and the City Council on November 3, 2010, with a deliberately delayed effective date of January 1, 2011. Added Chapter 4-207 (renumbered to MCC 4-6-300 by the May 9, 2012 license reform ordinance) creating a \"vacation rental\" license for a dwelling unit with six or fewer sleeping rooms rented for transient occupancy: $500 for a two-year license, at least $1 million in liability insurance, hotel-style inspection, sanitation and life-safety standards, a guest registry retained three years, the license number in every advertisement, a posted evacuation diagram and local contact, occupancy caps by square footage, and fines of $500-$1,000 per day for unlicensed operation. Rentals of less than 24 consecutive hours, more than one rental per 24-hour period, and hourly advertising were prohibited. Companion zoning amendments (MCC 17-2-0200, 17-3-0200, 17-15-0307) barred new vacation rentals in RS and low-density RT residential districts dominated by single-family homes and two- and three-flats, grandfathering only units that could prove more than a year of operation before January 1, 2011 and that obtained a license within 180 days; condominium units required homeowners-association approval and no more than six units per building could be licensed. Month-to-month leases, bed-and-breakfast establishments, hotels and rentals of a room while the owner is present were outside the definition. The ordinance was widely reported as unenforced: only about 200 units were licensed by early 2016 against 4,000-5,500 units advertised online.",
        "measures": measures(
            registration_requirements="increase",
            rental_type_restrictions="increase",
            time_restrictions="increase",
            unit_type_restrictions="increase",
            host_compliance_requirements="increase",
        ),
    },
    {
        "title": "2011 Revenue Ordinance amendment to the Chicago Hotel Accommodations Tax (MCC Ch. 3-24) (Coun. J. 11-17-10)",
        "jurisdiction": "City of Chicago",
        "passage_date": "2010-11-17",
        "effective_date": "2011-07-01",
        "summary": "Part of the City Council's November 17, 2010 revenue package for fiscal 2011, passed two weeks after the vacation rental ordinance. It deleted the seven-unit-per-building threshold from the definition of \"hotel accommodations\" in MCC 3-24-020 and named vacation rentals expressly, so that every licensed or licensable vacation rental became subject to the city's 3.5 percent Hotel Accommodations Tax regardless of building size, effective July 1, 2011. The tax reached non-owner-occupied dwellings; units that are the owner's permanent residence and domicile (with the owner absent no more than 120 days in 12 months) and month-to-month rentals were excluded. This is the provision that first pulled Airbnb-style rentals into the city's lodging tax base; the base rate later rose to 4.5 percent. It changed tax liability rather than land use or licensing eligibility.",
        "measures": measures(host_compliance_requirements="increase"),
    },
    {
        "title": "Cook County Hotel Accommodations Tax Ordinance (Code of Ordinances Ch. 74, Art. XXI, Secs. 74-800 to 74-849), adopted in the FY2016 budget",
        "jurisdiction": "Cook County",
        "passage_date": "2015-11-18",
        "effective_date": "2016-05-01",
        "summary": "Proposed by Board President Toni Preckwinkle to close a gap in the county's FY2016 budget and approved by the Cook County Board of Commissioners on November 18, 2015; the ordinance took effect November 13, 2015 but collection began May 1, 2016. It imposes a 1 percent county tax on the gross rental charge for the use of any hotel accommodation in Cook County, borne by the guest and collected and remitted by owners, managers and operators, which raised the combined Chicago lodging tax rate to roughly 17.4 percent. The county applies the tax to short-term rentals: its guidance instructs Airbnb-type hosts to confirm that their booking facilitator is registered with the Cook County Department of Revenue and collecting the tax, and hosts who book independently must register and remit themselves. A December 14, 2023 amendment (effective immediately) broadened \"gross rental or leasing charge\" to capture service, cleaning and similar fees. The county measure affects tax liability only, not registration or land use.",
        "measures": measures(host_compliance_requirements="increase"),
    },
    {
        "title": "Shared Housing Ordinance, O2016-5111 - new MCC Chapters 4-13 (short term residential rental intermediaries and advertising platforms), 4-14 (shared housing units), 4-16 (shared housing unit operators) and 4-17 (restricted residential zones)",
        "jurisdiction": "City of Chicago",
        "passage_date": "2016-06-22",
        "effective_date": "2017-03-14",
        "summary": "Mayor Rahm Emanuel's home-sharing ordinance, passed 43-7 on June 22, 2016 after months of contentious debate; it added 49 sections to the Municipal Code and amended nine more. Effective dates were staggered: the new 4 percent Vacation Rental and Shared Housing Surcharge under MCC 3-24-030(B) began July 1, 2016; the regulatory provisions were scheduled for December 17, 2016 but were postponed by an agreed order and then stayed by the federal court in Mendez/HomeAway v. City of Chicago until March 14, 2017, the day after Judge Sara Ellis denied a preliminary injunction, which is the operative date used here. The ordinance created a \"shared housing unit\" registration administered through licensed platforms, required platforms to hold a short term residential rental intermediary license (a $10,000 flat fee plus $60 per listed unit) or an advertising platform license, barred booking transactions for unregistered or unlicensed units, and required twice-monthly unit lists, bi-monthly aggregate reports, a quality-of-life plan and a 24-hour complaint hotline. Hosts must be natural persons, must include the registration number in every listing, and are subject to occupancy, insurance, sanitation and guest-record rules. Eligibility limits include: no more than one-quarter of the units or six units (whichever is fewer) in buildings of five or more units; only one shared housing unit in buildings of two to four units, which must be the host's primary residence; single-family homes eligible only if they are the host's primary residence; a Prohibited Buildings List through which owners and associations can opt entire buildings out; and a precinct-level opt-out process creating Restricted Residential Zones under Chapter 4-17. The pre-existing vacation rental license under MCC 4-6-300 was retained for units booked offline or through advertising platforms.",
        "measures": measures(
            registration_requirements="increase",
            rental_type_restrictions="increase",
            unit_type_restrictions="increase",
            primary_residence_requirements="increase",
            host_compliance_requirements="increase",
            platform_compliance_requirements="increase",
        ),
    },
    {
        "title": "Amendments to the Shared Housing Ordinance (Coun. J. 2-22-17, p. 43564) - MCC 4-6-300, 4-13-215, 4-13-235 and Chapter 4-14",
        "jurisdiction": "City of Chicago",
        "passage_date": "2017-02-22",
        "effective_date": "2017-03-14",
        "summary": "Passed while the Shared Housing Ordinance was stayed in federal court and took effect with it on March 14, 2017. The amendments narrowed the provisions most exposed in the litigation, including the terms on which the city could reach hosts' guest records without legal process (the plaintiffs dropped their Stored Communications Act claim in the amended complaint that followed), and added MCC 4-13-215, which requires each licensed intermediary to post a summary of the ordinance's requirements conspicuously on its platform and, as a condition of listing, to make each host attest that it has reviewed the summary and acknowledge that listing and operating a short-term rental is subject to those requirements. Net effect: a modest relaxation of host record-production exposure paired with a new platform-side notice and attestation duty.",
        "measures": measures(
            host_compliance_requirements="decrease",
            platform_compliance_requirements="increase",
        ),
    },
    {
        "title": "First Restricted Residential Zone designations, 13th Ward (O2017-3884, O2017-3904 and companion ordinances)",
        "jurisdiction": "City of Chicago",
        "passage_date": "2017-06-28",
        "effective_date": "2017-06-28",
        "summary": "The first use of the Chapter 4-17 precinct opt-out created by the Shared Housing Ordinance. After Ald. Marty Quinn (13th) completed the petition process - a legal voter in a precinct containing RS1, RS2 or RS3 zoned property must gather valid signatures from 25 percent of the precinct's registered voters within 90 days, subject to a 30-day challenge window - the Zoning Committee approved designations for four of the ward's 48 precincts on June 22, 2017 and the City Council passed them on June 28, 2017. Each ordinance designates the precinct a Restricted Residential Zone in which all new or additional shared housing units and vacation rentals are prohibited, takes effect on passage and publication, and remains in effect for four years. Units lawfully established before the designation are grandfathered until their registration or license lapses or the property changes hands. Additional precincts followed in the 13th and 23rd Wards from October 2017 onward, making this a rolling, geographically targeted supply restriction rather than a one-time event.",
        "measures": measures(unit_type_restrictions="increase"),
    },
    {
        "title": "O2018-4988 - 2 percent domestic violence surcharge added to the Vacation Rental and Shared Housing Surcharge (MCC 3-24-030)",
        "jurisdiction": "City of Chicago",
        "passage_date": "2018-07-25",
        "effective_date": "2018-12-01",
        "summary": "Raised the city's home-sharing surcharge from 4 percent to 6 percent of the gross rental charge for shared housing units, vacation rentals and bed-and-breakfast establishments, on top of the 4.5 percent Hotel Accommodations Tax, with the additional 2 percent dedicated to services for survivors of domestic violence. Collection of the increased rate began December 1, 2018 and, as with the original surcharge, platforms that are licensed intermediaries collect and remit it on the bookings they facilitate. A rate change only: it did not alter registration eligibility, land use limits or reporting duties.",
        "measures": measures(),
    },
    {
        "title": "Shared Housing Reform Ordinance, SO2020-3986 (Coun. J. 9-9-20, p. 20269) - amendments to MCC 4-6-300, 4-13, 4-14, 4-16 and 4-17",
        "jurisdiction": "City of Chicago",
        "passage_date": "2020-09-09",
        "effective_date": "2020-10-17",
        "summary": "Mayor Lori Lightfoot's reform ordinance, passed September 9, 2020 and published October 7, 2020. Per the city's press release, the single-night rental prohibition, the enhanced enforcement authority and the Restricted Residential Zone expansion took effect ten days after publication, on October 17, 2020, and Airbnb blocked one-night bookings in Chicago from that date; the remaining reforms were set for April 1, 2021 and were later pushed to June 1, 2021. The ordinance bars renting a shared housing unit or vacation rental for fewer than two consecutive nights and bars more than one rental within any 48-hour period, until the BACP commissioner and the police superintendent jointly promulgate rules finding single-night rentals can be conducted safely (a provision later challenged in Mendez v. City of Chicago). It lets the city revoke a registration after a single illegal party or overcrowding incident and lowers the threshold for other nuisance conditions, expands the zoning districts in which precincts can petition for a Restricted Residential Zone, and moves the registration process away from the platforms: hosts must apply directly to BACP, pay a $125 annual registration fee, and receive approval before a unit may be listed, with platforms barred from listing units that lack city approval. Platform license fees were restructured into tiers ($10,000 for 1,000 or more units, $7,500 for 500-999, $5,000 for fewer than 500) plus the $60 per-unit fee.",
        "measures": measures(
            registration_requirements="increase",
            time_restrictions="increase",
            unit_type_restrictions="increase",
            host_compliance_requirements="increase",
            platform_compliance_requirements="increase",
        ),
    },
    {
        "title": "Amendment delaying the shared housing registration provisions (Coun. J. 3-24-21, p. 28843) - MCC 4-6-300, 4-13 and 4-14",
        "jurisdiction": "City of Chicago",
        "passage_date": "2021-03-24",
        "effective_date": "2021-04-01",
        "summary": "BACP told the License Committee on March 17, 2021 that it needed more time to build and test the system making the city the point of intake for registration applications, and the City Council passed the delay on March 24, 2021. It moved the effective date of the September 2020 ordinance's registration provisions - direct application to BACP, city approval before listing, the $125 fee, and the platform ban on listing unapproved units - from April 1, 2021 to June 1, 2021, and made conforming amendments across Chapters 4-6, 4-13 and 4-14. The single-night rental ban and enhanced enforcement powers already in force were unaffected. Substantively a two-month postponement of an announced tightening rather than a new requirement.",
        "measures": measures(),
    },
    {
        "title": "SO2024-0013637 - short-term, shared housing and vacation rental transparency and reporting amendments (Coun. J. 5-21-25, p. 28493) - MCC Chapters 4-6, 4-13 and 4-14",
        "jurisdiction": "City of Chicago",
        "passage_date": "2025-05-21",
        "effective_date": "2025-05-21",
        "summary": "Substitute ordinance sponsored by Ald. Bennett Lawson (44), approved by the License and Consumer Protection Committee in May 2025 and passed by the City Council on May 21, 2025 (the date the Municipal Code annotations carry; the ordinance's own effective clause was not verified, and industry guidance described the monthly reporting duty as operative by July 2025). Licensees must file a monthly report with BACP covering each unit listed during the period: the registration or license number, address and ward, the exact number of nights rented, the rent paid by guests, a cumulative tally of nights booked for the remainder of the calendar year, the total tax remitted to the city for that unit, and a current telephone number for the host and local contact. BACP must in turn send each alderman a quarterly ward-level report covering citations, violations and disciplinary actions, and must maintain a database of the city's short-term rentals. The ordinance also requires listings to disclose occupancy limits, a local contact person and all costs and fees charged to guests, tightens aldermanic access to rental records, and adds a Cook County homeowner exemption from certain disclosure requirements.",
        "measures": measures(
            registration_requirements="increase",
            host_compliance_requirements="increase",
            platform_compliance_requirements="increase",
        ),
    },
    {
        "title": "Illinois Public Act 104-0006 (SB 2510, FY2026 revenue omnibus), Article 10 - Hotel Operators' Occupation Tax Act extended to short-term rentals",
        "jurisdiction": "State of Illinois",
        "passage_date": "2025-06-16",
        "effective_date": "2025-07-01",
        "summary": "Signed June 16, 2025 as part of the state's FY2026 revenue package and effective July 1, 2025. Article 10 amended the definition of \"hotel\" in 35 ILCS 145/2 to include short-term rentals - owner-occupied, tenant-occupied or non-owner-occupied dwellings where at least one room is rented for fewer than 30 consecutive days with accommodations reserved in advance - so that Airbnb-style operators became subject to the state Hotel Operators' Occupation Tax (5 percent plus an additional 1 percent, each on 94 percent of gross rental receipts) that previously reached only conventional lodging. It also added a definition of \"hosting platform,\" excluded platform fees from taxable \"rent,\" and provided that for re-renters of hotel rooms only, \"hotel\" does not include a short-term rental. The change reaches STR operators in Chicago through the state tax base; it does not alter city registration or land use rules.",
        "measures": measures(host_compliance_requirements="increase"),
    },
    {
        "title": "2026 Revenue Ordinance, Article XII (Shared Housing Fines and Fees) (Coun. J. 12-19-25) - MCC 4-5-010 and related fee and fine provisions",
        "jurisdiction": "City of Chicago",
        "passage_date": "2025-12-19",
        "effective_date": "2026-01-01",
        "summary": "Adopted with the city's 2026 budget package. Effective January 1, 2026 the annual Shared Housing Unit registration fee rose from $150 to $250 per unit, the Shared Housing Unit Operator License (required of hosts approved for more than one unit) rose from $250 to $500 for a two-year term, and a Commissioner's Adjustment application - the route to an exception from the primary residence and building-cap rules - costs $360; intermediary and advertising platform license fees remain tiered by unit count plus $60 per listed unit. The ordinance also raised general unlicensed-business fines and provides for biennial CPI-based fee adjustments starting in 2028. It raises the cost of compliance without changing eligibility, rental type or land use restrictions.",
        "measures": measures(
            registration_requirements="increase",
            host_compliance_requirements="increase",
        ),
    },
    {
        "title": "Illinois Public Act 104-0468 (SB 3068) - hotel marketplace facilitators under the Hotel Operators' Occupation Tax Act",
        "jurisdiction": "State of Illinois",
        "passage_date": "2026-06-16",
        "effective_date": "2026-07-01",
        "summary": "Effective as an act on June 16, 2026, with its substantive rules operating from July 1, 2026 (Illinois Department of Revenue Informational Bulletin FY 2026-33). It defines \"hotel marketplace facilitator\" to include re-renters of hotel rooms and hosting platforms for short-term rentals, removes the former 200-transaction threshold, and provides that a facilitator meeting a $100,000 tax remittance threshold over the preceding 12 months is the hotel operator for the bookings it facilitates: it must register with IDOR and remit the state and IDOR-administered local hotel operators' occupation taxes, while the underlying operator no longer incurs that tax on those bookings. Re-renters may no longer claim a credit for tax paid to hotel operators. For Chicago hosts the practical effect is to shift state-administered lodging tax collection onto Airbnb and comparable platforms.",
        "measures": measures(
            host_compliance_requirements="decrease",
            platform_compliance_requirements="increase",
        ),
    },
]

CHICAGO = {
    "legislative_history": LEGISLATIVE_HISTORY,
    "airbnb_tax_collection_date": "2015-02-15",
    "airbnb_data_sharing_date": "2017-03-14",
    "agent_checked": True,
}


def main():
    load_dotenv()
    path = Path(os.environ["AGENT_DATA_PATH"]) / "str_regulations.json"
    data = json.loads(path.read_text())

    idx = next(i for i, x in enumerate(data) if not x.get("agent_checked"))
    entry = data[idx]
    if (entry["city"], entry["state"]) != ("Chicago", "IL"):
        raise SystemExit(f"first unchecked entry is {entry['city']}, {entry['state']}, not Chicago, IL")

    dates = [e["passage_date"] for e in LEGISLATIVE_HISTORY]
    if dates != sorted(dates):
        raise SystemExit("legislative_history is not sorted by passage_date")

    shutil.copy2(path, path.with_suffix(".json.bak"))
    entry.update(CHICAGO)
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"updated index {idx} ({entry['city']}, {entry['state']}) with "
          f"{len(LEGISLATIVE_HISTORY)} legislative_history entries -> {path}")


if __name__ == "__main__":
    main()
