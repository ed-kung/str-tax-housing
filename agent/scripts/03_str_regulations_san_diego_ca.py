"""Add short-term-rental legislative history for San Diego, CA to str_regulations.json."""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY, STATE = "San Diego", "CA"


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
        "title": "City of San Diego Ordinances O-20977 and O-20978 - San Diego's first short-term residential occupancy licensing regulations and related code enforcement authority (suspended by referendum and repealed before taking effect)",
        "jurisdiction": "City of San Diego",
        "passage_date": "2018-08-02",
        "effective_date": "2018-09-01",
        "summary": "San Diego's first attempt to write short-term rentals into the Municipal Code. On July 16, 2018 the City Council rejected Mayor Kevin Faulconer's proposal 3-6 and then adopted, 6-3, a compromise championed by Councilmembers Barbara Bry and Lorie Zapf; final passage of the two ordinances was August 2, 2018. O-20978 defined short term residential occupancy as occupancy of a dwelling unit for less than one month (matching the Transient Occupancy Tax definition in SDMC Sec. 35.0102) and required an annual STRO license. A host could hold a license only for the host's primary residence plus one additional dwelling unit on the same parcel, which effectively banned whole-home rental of second homes citywide; the Mission Beach exception in earlier drafts was struck so the rules applied everywhere. Whole-home rental of the primary residence while the host was away was capped at six months (180 days) per year, and a three consecutive night minimum stay applied in the Coastal Overlay Zone and the Downtown Community Plan area. Hosts also had to obtain a Transient Occupancy Tax certificate, remit TOT plus a new per-night affordable housing impact fee monthly, obtain a Neighborhood Use Permit for dwellings with four or more bedrooms, post the license number in every advertisement or listing, comply with a good neighbor policy including a posted local contact, and keep detailed records of each rental for three years; three notices of violation in a 12-month period could trigger revocation. Hosting platforms picked up new duties to police listings. O-20977 designated the City Treasurer as a director and enforcement official and gave departments under the City Manager authority to issue administrative subpoenas. The ordinances would nominally have taken effect 30 days after final passage with licensing and enforcement beginning July 1, 2019, but a referendary petition backed by Airbnb, HomeAway and Share San Diego submitted roughly 62,000 signatures on August 30, 2018 (well above the 35,823 required) and was certified sufficient on September 25, 2018, suspending both ordinances so that they never became operative.",
        "measures": measures(
            registration="increase",
            rental_type="increase",
            time="increase",
            unit_type="increase",
            host_presence="increase",
            primary_residence="increase",
            host_compliance="increase",
            platform_compliance="increase",
        ),
    },
    {
        "title": "City of San Diego Ordinance O-21008 - granting the referendary petition against Ordinances O-20977 and O-20978 and repealing them",
        "jurisdiction": "City of San Diego",
        "passage_date": "2018-11-20",
        "effective_date": "2018-12-20",
        "summary": "Faced with a certified referendum, the Council's only options were to repeal the 2018 regulations or send them to the voters in 2020. At a special meeting on October 22, 2018 the Council voted 8-1 (Zapf dissenting) to repeal, citing the cost of a ballot fight and the threat of years of litigation; the second reading was November 13, 2018 and final passage November 20, 2018. The repeal wiped out the STRO license, the primary residence limit, the 180-day whole-home cap, the coastal and downtown minimum stay, the affordable housing impact fee and the platform duties before any of them took effect, and under the rule summarized in City Attorney Memorandum of Law MS-2018-15 the Council could not adopt an essentially similar ordinance for one year after the repeal. San Diego was left with no short-term-rental-specific code: hosts remained subject only to Transient Occupancy Tax, the Rental Unit Business Tax, general nuisance and zoning rules, and the City Attorney's standing position (March 2017 Memorandum of Law) that short-term rentals are not an enumerated permitted use in residential zones.",
        "measures": measures(
            registration="decrease",
            rental_type="decrease",
            time="decrease",
            unit_type="decrease",
            host_presence="decrease",
            primary_residence="decrease",
            host_compliance="decrease",
            platform_compliance="decrease",
        ),
    },
    {
        "title": "City of San Diego Ordinance O-21305 - San Diego Municipal Code Chapter 5, Article 10 (Short-Term Residential Occupancy and Hosting Platforms), the STRO ordinance",
        "jurisdiction": "City of San Diego",
        "passage_date": "2021-04-14",
        "effective_date": "2021-05-29",
        "summary": "San Diego's current short-term rental regime, built on a July 2020 memorandum of understanding between Expedia Group and UNITE HERE Local 30 and carried by Council President Jennifer Campbell. The Planning Commission recommended approval 7-0 on December 3, 2020, the City Council adopted the ordinance 8-1 on April 6, 2021, Mayor Todd Gloria signed it on April 14, 2021, and it became effective outside the Coastal Overlay Zone on May 29, 2021. Rather than amend the zoning code, the ordinance uses the police power to add Chapter 5, Article 10 defining short term residential occupancy as occupancy of a dwelling unit or part of one for less than one month and making it unlawful without a license. Four tiers apply: Tier 1 for home share or whole home use of 20 days or less per calendar year (home share only in the host's primary residence, one Tier 1 license per dwelling unit per year); Tier 2 for home share of more than 20 days, allowed only in the host's primary residence, which the host must occupy at least 275 days of the calendar year; Tier 3 for whole home rental of more than 20 days outside Mission Beach, with a two consecutive night minimum stay and a hard cap of 1 percent of the City's housing units excluding Mission Beach (roughly 5,400 licenses) awarded by lottery; and Tier 4 for whole home rental of more than 20 days inside the Mission Beach Community Planning Area, with the same two-night minimum and a cap of 30 percent of Mission Beach housing units. A host may hold only one license and operate only one dwelling unit at a time, licenses run two years and are not transferable between hosts or properties, and applications require a Transient Occupancy Tax certificate, proof of Rental Unit Business Tax payment, and proof of primary residence for home share. Operating conditions include a good neighbor policy, a posted local contact who must respond within one hour, the license number in listings, human trafficking awareness training, quarterly reports and a minimum 90 days of annual use for Tier 3 and Tier 4, and revocation for repeat violations. Division 2 imposes the first platform obligations: hosting platforms must notify hosts of the license and TOT rules, may not complete a booking for a unit that is not on the City's license registry, must use reasonable efforts to block Tier 1 bookings past 20 days, must collect and remit TOT monthly when they collect rent, must report listing-level data to the City monthly, and must keep transaction records for four years. The ordinance also repealed the bed and breakfast and boarder and lodger land use regulations from the Land Development Code. Because parts of Secs. 510.0102 and 510.0104 amended the certified Local Coastal Program, the licensing requirement could not apply in the Coastal Overlay Zone until the California Coastal Commission certified the amendment, and the license requirement was initially scheduled to begin July 1, 2022.",
        "measures": measures(
            registration="increase",
            rental_type="increase",
            time="increase",
            host_presence="increase",
            primary_residence="increase",
            host_compliance="increase",
            platform_compliance="increase",
        ),
    },
    {
        "title": "Senate Bill 60 (Chapter 307, Statutes of 2021) - residential short-term rental ordinances: health or safety infractions: maximum fines",
        "jurisdiction": "State of California",
        "passage_date": "2021-09-24",
        "effective_date": "2021-09-24",
        "summary": "Passed by the Legislature September 1, 2021, approved by Governor Newsom and chaptered September 24, 2021 as an urgency statute effective immediately. Amended Government Code Secs. 25132 and 36900 to let a city raise the maximum fine for an infraction of its short-term rental ordinance that poses a threat to public health or safety to $1,500 for a first violation, $3,000 for a second within a year and $5,000 for each additional violation within a year, far above the general $100/$200/$500 infraction caps. The higher fines do not apply to a first-time failure to register or to pay a business license fee, and the jurisdiction must offer a hardship waiver. This is enabling legislation: it raises the ceiling on penalties San Diego can attach to STRO violations without changing what conduct is permitted, and it arrived while the City was building the enforcement program for the STRO ordinance adopted five months earlier.",
        "measures": measures(host_compliance="increase"),
    },
    {
        "title": "City of San Diego Resolution R-313742 - adopting fees for short-term residential occupancy applications and licenses and amending the Rate Book of City Fees and Charges",
        "jurisdiction": "City of San Diego",
        "passage_date": "2021-10-25",
        "effective_date": "2021-10-25",
        "summary": "Binding fee resolution implementing the cost-recovery side of Ordinance O-21305, adopted October 25, 2021 with a waiver of Council Policy 100-05. It set the initial two-year STRO fees at a $25 application fee plus a $100 license fee for Tier 1, $25 plus $225 for Tier 2, and $70 plus $1,000 for Tier 3 and Tier 4, and added them to the City's rate book. The fees put a price on the new license and made whole-home operators, who pay roughly ten times the Tier 1 rate, carry most of the program's cost; no substantive operating rule changed.",
        "measures": measures(registration="increase"),
    },
    {
        "title": "City of San Diego Ordinance O-21436 - amending the implementation date for the short-term residential occupancy regulations adopted in Ordinance O-21305",
        "jurisdiction": "City of San Diego",
        "passage_date": "2022-02-24",
        "effective_date": "2022-03-26",
        "summary": "The City Council voted 8-1 on February 1, 2022 to postpone the date on which an STRO license becomes required, with final passage February 24, 2022. Staff argued the delay was needed to let the California Coastal Commission review and certify the Local Coastal Program amendment (heard in March 2022), to run the Tier 3 and Tier 4 lottery, to stage hiring and training of enforcement staff, and to give hosts holding advance bookings notice. The original July 1, 2022 start date was dropped and the City ultimately set May 1, 2023 as the date on which operating without a license became unlawful, so the 2022 summer season passed with no license requirement. The ordinance changed only timing; no tier, cap, occupancy, tax or platform provision was altered.",
        "measures": measures(),
    },
    {
        "title": "City of San Diego Ordinance O-21464 - amendments adopting the California Coastal Commission's suggested modifications to the STRO regulations (Local Coastal Program Amendment No. LCP-6-SAN-21-0046-2)",
        "jurisdiction": "City of San Diego",
        "passage_date": "2022-06-27",
        "effective_date": "2022-08-10",
        "summary": "Because the STRO definitions in SDMC Sec. 510.0102 and the tier rules in Sec. 510.0104(b)-(e) expanded the City's certified Local Coastal Program, they could not operate in the Coastal Overlay Zone until the Coastal Commission acted. The City filed LCP Amendment No. LCP-6-SAN-21-0046-2 on October 8, 2021; at its March 2022 hearing (item W14f) the Commission denied the amendment as submitted and certified it with four suggested modifications. The City Council adopted those modifications in O-21464, with final passage June 27, 2022 and an effective date of August 10, 2022. The substantive modifications require that Tier 3 licenses awarded by lottery be distributed to each Community Planning Area in proportion to that area's share of the applicant pool, so that coastal neighborhoods such as Pacific Beach, La Jolla and Ocean Beach are guaranteed a share of the capped whole-home licenses, and add a new Sec. 510.0112 sunset clause under which the coastal-zone licensing requirement expires January 1, 2030 unless amended or extended for good cause by the Coastal Commission's Executive Director. The remaining modifications add editor's notes identifying which provisions are part of the certified LCP and therefore cannot be amended locally without Commission certification. The practical effect was to extend the entire STRO licensing scheme, including the 1 percent citywide cap, the 30 percent Mission Beach cap, the two-night minimum stay and the primary residence rules, into the coastal communities where most San Diego short-term rentals are located.",
        "measures": measures(
            registration="increase",
            rental_type="increase",
            time="increase",
            host_presence="increase",
            primary_residence="increase",
            host_compliance="increase",
        ),
    },
    {
        "title": "Assembly Bill 537 (Chapter 805, Statutes of 2023) - short-term lodging: advertising: rates",
        "jurisdiction": "State of California",
        "passage_date": "2023-10-13",
        "effective_date": "2024-07-01",
        "summary": "Signed by Governor Newsom October 13, 2023, effective January 1, 2024 and operative July 1, 2024. Added Business and Professions Code Sec. 17568.6, barring any place of short-term lodging and any website, application or centralized platform that advertises one from displaying a room rate that omits mandatory fees, and requiring the total price including all government taxes and fees to be shown before the consumer reserves. It expressly covers short-term rentals of 30 consecutive days or less booked through a platform, so it reaches Airbnb listings in San Diego, where guests pay the 10.5 percent Transient Occupancy Tax plus the Tourism Marketing District assessment on top of rent and cleaning fees. It is a price-disclosure mandate rather than a land use, registration or occupancy rule, and it is enforceable by city attorneys with a civil penalty of up to $10,000 per violation.",
        "measures": measures(host_compliance="increase", platform_compliance="increase"),
    },
    {
        "title": "City of San Diego Resolution R-316035 - approving updated fees for STRO applications and licenses issued under SDMC Chapter 5, Article 10, Division 1",
        "jurisdiction": "City of San Diego",
        "passage_date": "2025-02-18",
        "effective_date": "2025-03-01",
        "summary": "The first cost-recovery update since the program launched, approved by the City Council on February 11, 2025 and recorded as Resolution R-316035 on February 18, 2025, effective March 1, 2025 to coincide with the first wave of renewals for two-year licenses expiring April 30, 2025. New and renewal fees rose to a $33 application fee plus a $193 license fee for Tier 1, $33 plus $284 for Tier 2, and $41 plus $1,129 for Tier 3 and Tier 4, roughly doubling the Tier 1 and Tier 2 charges set in 2021 and raising the whole-home charge from $1,070 to $1,170 per two-year term. Renewal remains conditioned on an active Transient Occupancy Tax certificate with no back taxes owed, a paid Rental Unit Business Tax account, and a Business Tax Certificate for hosts who do not own the unit.",
        "measures": measures(registration="increase"),
    },
    {
        "title": "Senate Bill 346 (Chapter 751, Statutes of 2025), the Short-Term Rental Facilitator Act of 2025 - Government Code Secs. 50990-50996",
        "jurisdiction": "State of California",
        "passage_date": "2025-10-13",
        "effective_date": "2026-01-01",
        "summary": "Approved by Governor Newsom and chaptered October 13, 2025, effective January 1, 2026. On request by a local agency, a short-term rental facilitator (a platform such as Airbnb or Vrbo that collects payment for stays of 30 days or less) must report the physical address, including nine-digit ZIP code, of each short-term rental in the jurisdiction, and, if that is not enough to identify the unit, the assessor parcel number, listing URL and unit-level detail. Reporting may be required no more often than quarterly unless the agency collects Transient Occupancy Tax monthly, in which case monthly reports may be required; the statute also authorizes administrative fines for non-reporting and audits of a facilitator's TOT records. San Diego already receives monthly listing-level reports under SDMC Sec. 510.0201(f) and, as of mid-2026, had not adopted a conforming SB 346 ordinance, so for the City the statute mainly supplies a state-law backstop and stronger penalty authority for platform data reporting rather than a new obligation.",
        "measures": measures(platform_compliance="increase"),
    },
]


SAN_DIEGO_UPDATE = {
    "legislative_history": LEGISLATIVE_HISTORY,
    # Airbnb began voluntarily collecting the City's 10.5% Transient Occupancy Tax and the 0.55%
    # Tourism Marketing District assessment from guests on Wednesday, July 1, 2015, under a
    # voluntary collection agreement negotiated with the City Treasurer; before that hosts filed
    # monthly TOT returns themselves. Platform collection only became a legal requirement in 2021
    # under SDMC Sec. 510.0201(e).
    "airbnb_tax_collection_date": "2015-07-01",
    # Platform data sharing is a creature of the STRO ordinance: SDMC Sec. 510.0201(f) requires
    # monthly listing-level reports (license number, responsible person, street address, days
    # booked). The obligation attached when the STRO requirements took effect on May 1, 2023, with
    # the first monthly report (May 2023 data) due June 30, 2023. Before that the City Treasurer
    # reported in an October 2021 memo that platforms remitted TOT in the aggregate and gave the
    # City no host-level data; the City later used administrative subpoenas to compel reporting.
    "airbnb_data_sharing_date": "2023-05-01",
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
    matches[0].update(SAN_DIEGO_UPDATE)

    with JSON_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} legislative history entries")


if __name__ == "__main__":
    main()
