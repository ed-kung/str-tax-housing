"""Add short-term-rental legislative history for Phoenix, AZ to str_regulations.json."""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY, STATE = "Phoenix", "AZ"


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
        "title": "Arizona Senate Bill 1350 (Laws 2016, Chapter 208) - state preemption of local vacation rental and short-term rental regulation; online lodging marketplace tax classification",
        "jurisdiction": "State of Arizona",
        "passage_date": "2016-05-12",
        "effective_date": "2017-01-01",
        "summary": "Signed by Governor Doug Ducey on May 12, 2016 with a delayed effective date of January 1, 2017. Added A.R.S. Sec. 9-500.38 (cities/towns, later renumbered 9-500.39) and Sec. 11-269.15 (counties, later 11-269.17), barring municipalities from prohibiting vacation rentals or short-term rentals and from restricting or regulating them based on their classification, use or occupancy. Local regulation was confined to public health and safety (fire and building codes, sanitation, traffic, waste, pollution, designation of an emergency point of contact), generally applicable residential use, zoning, noise, property maintenance and nuisance ordinances, and bans on using an STR to house sex offenders, operate a sober living home, sell illegal drugs or run adult-oriented businesses. The act overrode existing local bans and minimum-stay rules (Sedona, Jerome, Scottsdale were the cited targets) and the state later ordered Sedona to stop requiring STR licenses. On the tax side it added the online lodging marketplace classification (A.R.S. Sec. 42-5076) and A.R.S. Sec. 42-5005(L), allowing a marketplace such as Airbnb to register with the Arizona Department of Revenue and remit state transaction privilege tax, county excise tax and municipal transient lodging tax (including Phoenix's) on behalf of hosts, with hosts excluded from tax on those marketplace-facilitated bookings. Phoenix had no STR-specific ordinance at the time, so the immediate practical effect in Phoenix was to lock in the city's inability to regulate STRs as a distinct land use and to shift tax collection to platforms.",
        "measures": measures(
            registration="decrease",
            rental_type="decrease",
            time="decrease",
            unit_type="decrease",
            host_presence="decrease",
            primary_residence="decrease",
            host_compliance="decrease",
            platform_compliance="increase",
        ),
    },
    {
        "title": "Arizona Senate Bill 1382 (Laws 2018, Chapter 189) - mandatory online lodging marketplace tax registration",
        "jurisdiction": "State of Arizona",
        "passage_date": "2018-04-11",
        "effective_date": "2019-01-01",
        "summary": "Signed by Governor Ducey on April 11, 2018. Amended A.R.S. Sec. 42-5005(L) so that the previously voluntary online lodging marketplace license became mandatory: beginning from and after December 31, 2018, every online lodging marketplace (Airbnb, Vrbo/HomeAway, and others) must register with the Arizona Department of Revenue for a license and remit state, county and municipal taxes due on bookings it facilitates, including the City of Phoenix transient lodging and privilege taxes. It also removed the pre-2019 carve-out in Sec. 42-5076(C) that excluded unregistered marketplaces from the classification and excluded from the tax base charges for lodging classified as class one property. Airbnb had already been collecting Arizona taxes voluntarily since January 1, 2017; this law extended the same obligation to all platforms. It imposed no land-use, licensing or occupancy restrictions on hosts.",
        "measures": measures(platform_compliance="increase"),
    },
    {
        "title": "Arizona House Bill 2672 (Laws 2019, Chapter 240) - vacation rentals; short-term rentals; regulation",
        "jurisdiction": "State of Arizona",
        "passage_date": "2019-05-21",
        "effective_date": "2019-08-27",
        "summary": "Signed by Governor Ducey on May 21, 2019 and effective on the 2019 general effective date. The first rollback of the 2016 preemption: it amended A.R.S. Sec. 9-500.39 to let cities require the owner of a vacation or short-term rental to give the city contact information for the owner or a designee able to respond to complaints in person, by phone or by email at any time of day before the property is offered for rent, and it barred nonresidential uses of an STR, including special events requiring a permit and retail, restaurant or banquet space uses ('party house' provisions). It added A.R.S. Sec. 42-5042, prohibiting an online lodging operator from offering or renting an accommodation without a current transaction privilege tax license and requiring the TPT license number on every advertisement, with civil penalties of $250 for a first offense and $1,000 thereafter, and added Sec. 42-1125.02 civil penalties for verified violations plus a duty for cities to report verified violations to the Department of Revenue within 30 days. Cities still could not require a permit or license, cap STRs, or impose occupancy, primary-residence or minimum-stay rules. This is the statute Phoenix relied on when it created its registry in January 2020.",
        "measures": measures(registration="increase", host_compliance="increase"),
    },
    {
        "title": "City of Phoenix Ordinance G-6653 - Phoenix City Code Chapter 10, Article XVI (Short-Term Vacation Rental), registration requirement",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2020-01-08",
        "effective_date": "2020-02-07",
        "summary": "Phoenix's first short-term rental ordinance, passed by the City Council on January 8, 2020 to implement the authority granted by HB 2672, and effective 30 days after passage. It added Phoenix City Code Sections 10-193 through 10-197, requiring the owner of any vacation rental (including owner-occupied rentals) to register the unit with the city on a city-specified platform and to supply the owner's name (or statutory agent), the rental address, and a phone number and email for the owner or agent authorized to respond to complaints in person, by phone or by email at any hour; changes had to be re-registered within 10 days. The city issued a registration number that had to appear, along with a prescribed notice of prohibited uses, in every online listing, and the responsible contact information had to be posted within 10 feet of the primary entrance. When asked by a police officer, the owner or agent had to be on site or reachable by phone or text within 60 minutes. The ordinance restated the state list of prohibited uses (nonresidential use, permitted special events, retail/restaurant/banquet/event-center use, housing sex offenders, sober living homes, liquor, illegal drugs, pornography, obscenity, nude or topless dancing, adult-oriented businesses) and set escalating civil sanctions of $500, $1,000 and $1,500 within a 12-month period plus class 1 misdemeanor liability. It expressly provided that the online lodging marketplace is not responsible for violations committed by an operator advertising on its platform. No fee, cap, occupancy, primary-residence or minimum-stay requirement was imposed.",
        "measures": measures(registration="increase", host_compliance="increase"),
    },
    {
        "title": "Arizona Senate Bill 1168 (55th Legislature, Second Regular Session, 2022) - vacation rentals; short-term rentals; enforcement",
        "jurisdiction": "State of Arizona",
        "passage_date": "2022-07-06",
        "effective_date": "2022-09-24",
        "summary": "Signed by Governor Ducey on July 6, 2022 and effective on the 2022 general effective date. It rewrote A.R.S. Sec. 9-500.39 (and the county analogue Sec. 11-269.17) to let cities require STR owners to obtain and maintain a local regulatory permit or license, with the application limited to owner/agent contact information, the property address, proof of a state transaction privilege tax license, emergency contact information, an acknowledgment agreeing to comply with applicable law, and a fee capped at the lesser of actual cost or $250. Cities must issue or deny within seven business days and may deny only on enumerated grounds, including that the owner or designee is a registered sex offender or has a qualifying violent felony within five years. It also authorized cities to require pre-rental written notice to adjacent and diagonally opposite residential properties with an attestation of compliance, display of the permit or license number on every advertisement, at least $500,000 in liability insurance (or listing through a platform providing equal coverage), and a $1,000-per-30-day penalty for failing to supply emergency contact information. It set escalating civil penalties for verified violations ($500/one night's rent, $1,000/two nights', $3,500/three nights'), required cities to adopt an administrative suspension process of up to 12 months for repeat or serious verified violations, and allowed the Department of Revenue to suspend an owner's TPT license after three verified violations in 12 months. The bar on prohibiting STRs, capping their number, or restricting them by classification, use or occupancy remained. Phoenix used this authority to convert its registry into a permit program in 2023.",
        "measures": measures(registration="increase", host_compliance="increase"),
    },
    {
        "title": "City of Phoenix Zoning Ordinance Text Amendment Z-TA-5-23-Y - accessory dwelling units legalized, short-term rental use of ADUs prohibited",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2023-09-06",
        "effective_date": "2023-10-06",
        "summary": "Approved 8-1 by the City Council on September 6, 2023 and effective 30 days later. The city's first ADU (casita) ordinance amended the Phoenix Zoning Ordinance to allow one accessory dwelling unit on single-family detached lots citywide, subject to size, height, setback and lot-coverage standards. Language added before the vote expressly prohibited using an ADU as a short-term rental; city staff argued this was defensible under A.R.S. Sec. 9-500.39 because the primary dwelling could still be rented short-term, so no property was banned from STR use outright. Councilmember Waring cast the lone no vote over STR enforcement concerns. The prohibition applied only to the accessory unit, not to whole-home or partial-home STRs generally, and it was preempted by state HB 2720 the following year and repealed by Ordinance G-7317 in November 2024.",
        "measures": measures(unit_type="increase"),
    },
    {
        "title": "City of Phoenix Ordinance G-7156 - Phoenix City Code Chapter 10, Article XVI amended, short-term rental permit program",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2023-09-20",
        "effective_date": "2023-11-06",
        "summary": "Adopted unanimously by the City Council on September 20, 2023 to implement SB 1168, replacing the 2020 registration system with an annual permit program that took effect November 6, 2023. It rewrote City Code Sections 10-193 through 10-206: no one may rent or offer a short-term rental without a current, unsuspended STR permit from the Planning and Development Department (Sec. 10-195), permits run one year at a nonrefundable fee of up to $250 and must be renewed at least 15 working days before expiration (Sec. 10-196), and applications (Sec. 10-197) must include owner and agent contact details, the rental address, a valid Arizona TPT license, evidence of at least $500,000 in liability insurance (or a platform providing equivalent coverage), evidence of registration with the Maricopa County Assessor, an acknowledgment of compliance, and a notarized attestation that the owner is not a registered sex offender and has no qualifying violent felony within five years. Owners must also designate a 24/7 emergency contact who responds within 60 minutes (Sec. 10-198), send certified-mail notices of intent to adjacent and diagonally opposite single-family properties and to HOAs or registered neighborhood associations within 600 feet (Sec. 10-199), run registered sex offender background checks on guests (Sec. 10-200, 10-204), display the permit and permit number in the unit and on every advertisement (Sec. 10-201), and comply with standards and operating requirements (Sec. 10-205). The city must approve or deny within seven days, denials, non-renewals and suspensions are appealable (Sec. 10-203), and permits may be suspended for up to 12 months after three court-adjudicated violations in 12 months or one serious violation (Sec. 10-202). Penalties escalate from $500 or one night's rent to $1,000 or two nights' to $3,500 or three nights', with up to $1,000 per month for operating unpermitted; press coverage of the adopted rules also reported a fine of up to $2,500 per day on platforms that list a Phoenix property without a valid permit. The SHAPE PHX portal opened for applications on October 26, 2023, permits began issuing November 6, 2023, and active enforcement began January 15, 2024. No cap, primary-residence, host-presence or minimum/maximum-stay requirement was imposed.",
        "measures": measures(
            registration="increase",
            host_compliance="increase",
            platform_compliance="increase",
        ),
    },
    {
        "title": "Arizona House Bill 2720 (Laws 2024, Chapter 196) - accessory dwelling units; requirements",
        "jurisdiction": "State of Arizona",
        "passage_date": "2024-05-21",
        "effective_date": "2024-09-14",
        "summary": "Signed by Governor Katie Hobbs on May 21, 2024, effective on the 2024 general effective date of September 14, 2024. Added A.R.S. Sec. 9-461.18, requiring municipalities of at least 75,000 residents to allow at least one attached and one detached ADU as a permitted use on any single-family lot and barring them from prohibiting the advertisement of the house or the ADU as separately leased long-term rentals; cities that failed to adopt compliant regulations by January 1, 2025 would lose the ability to regulate ADUs at all. It also added A.R.S. Sec. 9-500.39(B)(9), which for the first time lets a city require the owner of a short-term rental to reside on the property if the property contains an ADU whose certificate of occupancy, certificate of completion or similar final approval was issued on or after September 14, 2024 (and not if issued on or before September 13, 2024, or where the owner had a vested right to build before that date and the A.R.S. Sec. 12-1134 limitation period has not run). The League of Arizona Cities and Towns opposed the bill precisely because it did not let cities bar STR use of casitas; the law preempted Phoenix's September 2023 ADU short-term rental ban while granting a narrow owner-occupancy tool for newly built ADUs. Hobbs said she hoped to address short-term rentals separately.",
        "measures": measures(unit_type="decrease", primary_residence="increase"),
    },
    {
        "title": "City of Phoenix Ordinance G-7317 (Zoning Ordinance Text Amendment Z-TA-2-24-Y) - ADU regulations conformed to HB 2720, ADU short-term rental prohibition repealed",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2024-11-13",
        "effective_date": "2024-12-13",
        "summary": "Adopted by the City Council on November 13, 2024 after a Planning Commission hearing on November 7, 2024, and effective 30 days later; it had to be in place by January 1, 2025 or Phoenix would have lost all ADU regulatory authority under HB 2720. It amended Zoning Ordinance Sections 202, 603-609, 701, 703 and 706 to allow at least one attached and one detached ADU per single-family lot (a third detached unit on lots of one acre or more when one is restricted-affordable), reduce setbacks, and raise lot coverage in the RE-43, RE-24, R1-14 and RE-35 districts. Most relevant here, the staff report for Z-TA-2-24-Y expressly removed the city's existing prohibition on using an ADU as a short-term rental, on the grounds that A.R.S. Sec. 9-500.39(B) does not list an ADU STR ban among the permitted forms of local regulation. Owner-occupancy for ADUs used as STRs was handled separately through the licensing code in Ordinance G-7323, adopted the same day.",
        "measures": measures(unit_type="decrease"),
    },
    {
        "title": "City of Phoenix Ordinance G-7323 - Phoenix City Code Sections 10-197 and 10-204 amended to incorporate A.R.S. Sec. 9-500.39(B)(9)",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2024-11-13",
        "effective_date": "2024-12-13",
        "summary": "Adopted after a public hearing at the November 13, 2024 City Council formal meeting and effective 30 days later. It amended City Code Sec. 10-197 (short-term rental permit application content) to require, where the STR is on a property with an accessory dwelling unit whose certificate of occupancy was issued on or after September 14, 2024, a notarized attestation that the property owner will reside on the same property, and it conformed Sec. 10-204 (prohibited uses) to state law. As adopted, the owner-residence attestation was narrow: it applied only where the property contains two or more ADUs, or to applications submitted on or after December 20, 2027. The ordinance implements the authority created by HB 2720 and does not extend owner-occupancy to short-term rentals generally.",
        "measures": measures(registration="increase", primary_residence="increase"),
    },
    {
        "title": "Arizona House Bill 2928 (Laws 2025, Chapter 217) - accessory dwelling units; requirements (counties) and clarification of ADU short-term rental owner-residence authority",
        "jurisdiction": "State of Arizona",
        "passage_date": "2025-05-23",
        "effective_date": "2025-09-26",
        "summary": "Signed by Governor Hobbs on May 23, 2025, effective on the 2025 general effective date. It extended the 2024 municipal ADU framework to counties by adding A.R.S. Sec. 11-810.01 and amended A.R.S. Sec. 9-500.39(B)(9) and Sec. 11-269.17 to restate the short-term rental owner-residence authority in terms of when the accessory dwelling unit was constructed or received its certificate of occupancy, keeping the September 14, 2024 dividing line and the carve-out for owners with pre-existing rights to build. For Phoenix the change is technical: it confirms and stabilizes the city's ability to require an STR owner to live on a property with a post-September 2024 ADU, and it was followed by Phoenix Ordinance G-7495 in 2026. It does not otherwise alter registration, rental type, duration or platform obligations.",
        "measures": measures(primary_residence="increase"),
    },
    {
        "title": "City of Phoenix Ordinance G-7495 - Phoenix City Code Sec. 10-197 amended, owner-occupancy attestation for short-term rentals on properties with new ADUs",
        "jurisdiction": "City of Phoenix",
        "passage_date": "2026-03-04",
        "effective_date": "2026-04-04",
        "summary": "Passed by the City Council on March 4, 2026 and effective April 4, 2026 (codified in the May 18, 2026 code update). It broadened the owner-residence requirement added by G-7323: any short-term rental permit application for a property that has an accessory dwelling unit with a certificate of occupancy issued on or after September 14, 2024 must now include a notarized attestation that the owner will reside on the same property, plus proof of address such as a recent utility bill or a matching Arizona ID. The prior limitations, which applied the attestation only where the property contained two or more ADUs or where the application was filed on or after December 20, 2027, were struck. The rest of the permit regime (the $250 annual fee, $500,000 liability insurance, Arizona TPT license, Maricopa County Assessor registration, seven-day decision window, permit number on all advertising) is unchanged, and ADUs completed on or before September 13, 2024 remain exempt from the owner-occupancy requirement.",
        "measures": measures(registration="increase", primary_residence="increase"),
    },
]

PHOENIX_UPDATE = {
    "legislative_history": LEGISLATIVE_HISTORY,
    # Airbnb-Arizona Department of Revenue agreement announced by Gov. Ducey; Airbnb began
    # collecting and remitting state TPT, county excise and city transient lodging taxes
    # (including Phoenix's) on January 1, 2017.
    "airbnb_tax_collection_date": "2017-01-01",
    # No evidence of an Airbnb agreement to share listing-level data with the City of Phoenix.
    # Platform reporting under A.R.S. Sec. 42-5076 runs to the state Department of Revenue in
    # aggregate and expressly does not identify individual operators.
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
    matches[0].update(PHOENIX_UPDATE)

    with JSON_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} legislative history entries")


if __name__ == "__main__":
    main()
