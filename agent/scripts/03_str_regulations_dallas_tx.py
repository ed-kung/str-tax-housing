"""Add short-term-rental legislative history for Dallas, TX to str_regulations.json."""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY, STATE = "Dallas", "TX"


def measures(
    registration="no change",
    rental_type="no change",
    time="no change",
    unit_type="no change",
    host_presence="no change",
    primary_residence="no change",
    host_compliance="no change",
    platform_compliance="no change",
):
    return {
        "registration_requirements": registration,
        "rental_type_restrictions": rental_type,
        "time_restrictions": time,
        "unit_type_restrictions": unit_type,
        "host_presence_requirements": host_presence,
        "primary_residence_requirements": primary_residence,
        "host_compliance_requirements": host_compliance,
        "platform_compliance_requirements": platform_compliance,
    }


LEGISLATIVE_HISTORY = [
    {
        "title": "Senate Bill 929, 88th Texas Legislature, Regular Session (2023) - notice and compensation a municipality must provide before revoking a nonconforming land use (Local Government Code Secs. 211.006 and 211.019)",
        "jurisdiction": "State of Texas",
        "passage_date": "2023-05-08",
        "effective_date": "2023-05-19",
        "summary": "Passed the Senate March 30, 2023 and the House May 5, 2023, signed by Governor Abbott May 19, 2023 and effective immediately. Texas has no statute that either preempts or expressly authorizes municipal short-term rental regulation, so cities such as Dallas regulate under home-rule and Local Government Code Secs. 51.001 and 54.004 authority; SB 929 instead attacks the amortization side of that authority. New Sec. 211.019 lets an owner continue a use that becomes nonconforming because of a zoning change, and if the city requires the owner or lessee to stop the nonconforming use, entitles that person to either (1) payment for costs directly related to stopping the use plus the loss in the property's market value, or (2) continuation of the nonconforming use until those amounts are recovered through continued business activity. Amended Sec. 211.006 adds individual mailed notice, at least 10 days before any hearing on a zoning change that would create a nonconforming use, to every owner and occupant of affected property, in statutorily prescribed 14-point bold text. The Act reaches any zoning change considered on or after June 1, 2023 and any order to stop a nonconforming use issued on or after February 1, 2023, so it applied directly to the short-term rental zoning ordinance Dallas adopted five weeks later and is the statutory backdrop to the operators' argument that the city could not extinguish their existing rentals without compensation. The statute changes no substantive rule about who may rent a home short term or how; it raises the legal and fiscal cost to Dallas of eliminating rentals that were lawful before the zoning change.",
        "measures": measures(),
    },
    {
        "title": "City of Dallas Ordinance No. 32473 - adding Dallas City Code Chapter 42B, \"Short-Term Rentals,\" and amending Sec. 27-30 (the short-term rental registration ordinance)",
        "jurisdiction": "City of Dallas",
        "passage_date": "2023-06-14",
        "effective_date": "2023-06-14",
        "summary": "Dallas's first short-term-rental-specific regulatory code, adopted 13-0 near midnight on June 14, 2023 after five hours of public comment (Councilmember Casey Thomas and Mayor Eric Johnson were absent for the vote) and published June 17, 2023. The ordinance followed four years of study recited in its own findings: staff review beginning in 2019, the Quality of Life, Arts and Culture Committee's first briefing on February 18, 2020, a task force first convened June 12, 2020 and restructured in November 2021 to add operators and platforms, City Plan Commission authorization of a hearing on December 2, 2021, and the Plan Commission's December 8, 2022 recommendation to treat short-term rentals as a lodging use barred from residential districts. Chapter 42B defines a short-term rental as a full or partial rentable unit with a kitchen, bathroom and bedroom rented for fewer than 30 consecutive days or one month, whichever is less, and makes it an offense to own, operate, or even advertise one without a city registration. Registration is per property, expires one year after issuance or on transfer of ownership, and originally cost $404 annually with a $234 reinspection fee. Applications must disclose owner, host, local responsible party, lienholder, property manager and, for entities, the form of organization and every principal, plus the host's photo ID and the Chapter 44 hotel occupancy tax registration number, and must carry the host's written acknowledgement of occupancy, parking, noise, advertising and revocation rules. The director inspects before approval and again at each renewal (waived if no violations in the previous 12 months), and must deny registration if the property fails inspection or zoning, if there were two or more code citations in the preceding 12 months, if multitenant density caps would be exceeded, or if the owner or host is delinquent in ad valorem or hotel occupancy taxes owed to the city. Two or more citations in a year, or a single egregious offense involving drugs, prostitution or a serious breach of the peace, allows revocation of that registration and every other registration held by the same owner or host, with a one-year bar on reapplying. Operating rules cap occupancy at three people per bedroom and 12 people total, limit each rentable unit to one short-term rental, set a two-night minimum stay, ban amplified sound audible past the property line between 10:00 p.m. and 7:00 a.m., limit guest vehicles to available off-street spaces, require the registration number and the occupancy, noise, vehicle and two-night-minimum rules in every listing or advertisement, and impose density caps in multitenant structures of three percent of units in multifamily zoning, 20 percent in nonresidential zoning, and zero in any structure with 20 or fewer units. A host must designate a notarized local responsible party reachable 24/7 who must appear at the property within one hour of city notice of an emergency and who may be required to accept service of citations. Division-level platform duties bar a hosting platform from collecting any fee for a booking, or for ancillary services such as cleaning, insurance or concierge service, unless both the platform and the unit are registered, and require registered platforms to file a monthly electronic report of every Dallas listing showing location and whether the listing is a room or a whole unit. Violations carry fines up to $500 with each day a separate offense, and Sec. 42B-16 required a council committee to review the chapter by June 14, 2025. The ordinance took effect on passage and publication but barred enforcement action for six months, and the city targeted December 13, 2023 to begin enforcing; on December 6, 2023 Judge Monica McCoy Purdy of the 95th District Court granted the Dallas Short-Term Rental Alliance a temporary injunction (Cause No. DC-23-16845) blocking enforcement of both 2023 ordinances, so the registration program has never been administered and the fee has never been charged.",
        "measures": measures(
            registration="increase",
            rental_type="increase",
            time="increase",
            unit_type="increase",
            host_compliance="increase",
            platform_compliance="increase",
        ),
    },
    {
        "title": "City of Dallas Ordinance No. 32482 - amending Chapters 51 and 51A of the Dallas Development Code to create the \"short-term rental lodging\" use (the short-term rental zoning ordinance)",
        "jurisdiction": "City of Dallas",
        "passage_date": "2023-06-14",
        "effective_date": "2023-06-14",
        "summary": "The companion zoning ordinance adopted at the same June 14, 2023 meeting by a 12-3 vote (Councilmembers Chad West, Casey Thomas and Jaime Resendez dissenting) and published June 17, 2023, endorsing the City Plan Commission's December 8, 2022 recommendation over the recommendation of the zoning and code departments, which had asked the council to allow short-term rentals in all districts and control them through the code amendment alone. Because short-term rentals had never been a recognized land use in the Dallas Development Code, the ordinance adds \"short-term rental lodging\" to the lodging use categories of Secs. 51-4.216.1 and 51A-4.205, defined as a full or partial rentable unit with a kitchen, bathroom and bedroom rented for fewer than 30 consecutive days per rental period, and permits it by right only in MO(A), GO(A), multifamily, central area, mixed use, multiple commercial and urban corridor districts. The use is therefore prohibited in every single-family, duplex, townhouse, clustered housing and agricultural district and in planned development and conservation districts with those base zonings, which is what made the ordinance a de facto ban: city staff counted roughly 1,800 rentals registered for hotel occupancy tax at the time and about 1,000 of them in single-family zones, against outside estimates of as many as 6,000 rentals citywide. Additional provisions require one off-street parking space per bedroom used as short-term rental lodging, limit each rentable unit to one short-term rental, require compliance with Chapter 42B, bar the use in a multifamily structure that received a Division 51A-4.900 density bonus, and bar operating a rental as a commercial amusement or restaurant without a certificate of occupancy for that use. The council's findings state that the transient nature of short-term rentals makes them a non-residential use incompatible with single-family districts, that they harm residents' peaceful enjoyment through noise and overparking, and that continued operation in single-family neighborhoods removes housing stock during a housing crisis. Violations carry fines up to $2,000. Like the registration ordinance it took effect on passage and publication with enforcement barred for six months, was to be enforced beginning December 13, 2023, and was enjoined on December 6, 2023; the Fifth Court of Appeals affirmed the injunction on February 7, 2025, reaffirmed it on rehearing July 18, 2025 and denied en banc reconsideration August 19, 2025, holding the operators likely to succeed on Texas constitutional due course of law and retroactivity claims, and the city's October 16, 2025 petition for review (Tex. No. 25-0748) was still pending with merits briefing ordered March 27, 2026.",
        "measures": measures(
            rental_type="increase",
            unit_type="increase",
            host_compliance="increase",
        ),
    },
    {
        "title": "City of Dallas Ordinance No. 32556 - Fiscal Year 2023-24 fee ordinance, amending Dallas City Code Sec. 42B-5 (short-term rental registration and reinspection fees)",
        "jurisdiction": "City of Dallas",
        "passage_date": "2023-09-20",
        "effective_date": "2023-10-01",
        "summary": "The omnibus fee and rate ordinance adopted with the FY 2023-24 budget on September 20, 2023, effective October 1, 2023. Section 23 amends Sec. 42B-5 to cut the annual short-term rental registration fee from the $404.00 set three months earlier in Ordinance No. 32473 to $248.00, with the initial inspection still included, and to cut the reinspection fee from $234.00 to $144.00; the accompanying September 15, 2023 staff memo (agenda item 23-2328) presented the amounts as cost-recovery figures for the application and inspection workload. These are the amounts in the codified City Code, but because the December 6, 2023 injunction blocks Chapter 42B the fee has never actually been assessed. No substantive registration, zoning, occupancy, stay-length or platform rule was altered; the ordinance only lowered the price of the license.",
        "measures": measures(registration="decrease"),
    },
    {
        "title": "House Bill 2464, 89th Texas Legislature, Regular Session (2025) - municipal authority to regulate home-based businesses (Local Government Code Sec. 229.902)",
        "jurisdiction": "State of Texas",
        "passage_date": "2025-05-25",
        "effective_date": "2025-06-12",
        "summary": "Passed the House May 14, 2025 by 128-4 and the Senate May 25, 2025 by 29-2, signed by Governor Abbott June 12, 2025 and effective immediately on the two-thirds vote. The Act bars a municipality from prohibiting a \"no-impact home-based business,\" from requiring a license or permit to operate one, or from requiring the property to be rezoned for nonresidential use, and constrains regulation of other home-based businesses. It matters for Dallas short-term rentals only because of the carve-out the legislature added between the introduced and enrolled versions: new Sec. 229.902(d)(2) states that the section does not prohibit a municipality from adopting or enforcing an ordinance regulating the operation of a short-term rental unit, and Sec. 229.902(d)(1) preserves private deed restrictions and homeowners' association rules. The Texas Municipal League and city legal summaries accordingly read HB 2464 as leaving municipal short-term rental authority untouched, so the statute neither adds nor removes any requirement on Dallas hosts or platforms; it forecloses an argument that the new home-based-business preemption had swept short-term rentals in with home occupations. The companion occupancy-limit preemption enacted the same session, Senate Bill 1567, reaches only home-rule cities under 250,000 population that contain or adjoin a university with more than 20,000 students and therefore does not apply to Dallas.",
        "measures": measures(),
    },
    {
        "title": "City of Dallas Ordinance No. 33302 - amending Dallas City Code Secs. 44-39 and 44-56 (timing of penalties and interest on delinquent hotel occupancy tax)",
        "jurisdiction": "City of Dallas",
        "passage_date": "2026-01-14",
        "effective_date": "2026-02-01",
        "summary": "Adopted January 14, 2026 and published January 17, 2026 following the Committee on Finance's December 9, 2025 review of hotel occupancy tax penalties, interest and collections (item 25-3536A), effective February 1, 2026. The ordinance rewrites the penalty subsections of both Article V (the 7 percent hotel occupancy tax) and Article VII (the additional 2 percent tax) of Chapter 44, which together impose the 9 percent city hotel occupancy tax that every short-term rental in Dallas owes on stays of fewer than 30 days. The 15 percent penalty, previously triggered on the 25th day of the month following collection, now attaches when the tax remains unpaid three months after the due date, and the 10 percent annual interest, previously accruing 30 days after the due date, now runs from the first day after the tax is due; the city states the penalty and interest cannot be waived or forgiven, and a 1 percent discount remains for payment postmarked by the 15th. The change is significant for short-term rentals because hotel occupancy tax registration with the City Controller's Office is the only citywide short-term-rental requirement Dallas can actually enforce while Chapter 42B and the zoning ban are enjoined: the Controller's Office reported to the Finance Committee that it had recovered about $5.5 million from non-remitting operators since 2020 using third-party data-scraping software, had detected 3,495 active rentals as of September 30, 2024 with nearly 45 percent not paying the tax, and was pursuing roughly 2,000 non-paying operators ahead of the June 2026 FIFA World Cup. No registration, zoning, occupancy or platform rule changed; the ordinance tightens the tax-remittance obligation hosts already had.",
        "measures": measures(host_compliance="increase"),
    },
]

DALLAS_UPDATE = {
    "legislative_history": LEGISLATIVE_HISTORY,
    # Airbnb has never had a voluntary collection agreement with the City of Dallas. It has
    # collected and remitted the 6% Texas state HOT for all Texas bookings since 2017-05-01 under
    # an agreement with the Comptroller, but the 9% city HOT is registered for and remitted by the
    # host through the City Controller's Office (dallas.munirevs.com). A city VCA was drafted in
    # August 2016 and never executed; a February 2022 push and a June 2023 council directive to the
    # city manager to negotiate with platforms also produced no agreement, and city and
    # third-party sources confirm no platform collection agreement as of mid-2026.
    "airbnb_tax_collection_date": None,
    # No evidence Airbnb has ever shared listing- or host-level data with Dallas. Chapter 42B would
    # have compelled monthly platform listing reports, but it has been enjoined since 2023-12-06
    # and never administered. The city instead identifies unregistered rentals with a third-party
    # data-scraping vendor, and staff told council in 2024 that their tools are limited to code,
    # noise and nuisance enforcement plus HOT registration outreach.
    "airbnb_data_sharing_date": None,
    "agent_checked": True,
}


def main():
    with JSON_PATH.open() as f:
        data = json.load(f)

    matches = [c for c in data if c["city"] == CITY and c["state"] == STATE]
    if len(matches) != 1:
        raise SystemExit(f"expected 1 entry for {CITY}, {STATE}; found {len(matches)}")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(JSON_PATH, JSON_PATH.with_name(f"str_regulations.{stamp}.json.bak"))
    matches[0].update(DALLAS_UPDATE)

    with JSON_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} legislative history entries")


if __name__ == "__main__":
    main()
