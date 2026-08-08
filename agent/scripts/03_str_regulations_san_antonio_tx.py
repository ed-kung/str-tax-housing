"""Add short-term-rental legislative history for San Antonio, TX to str_regulations.json."""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY, STATE = "San Antonio", "TX"


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
        "title": "City of San Antonio Ordinance 2018-11-01-0858 - City Code Chapter 16, Article XXII (Short Term Rentals) and Unified Development Code Sec. 35-374.01, San Antonio's first short-term rental ordinance",
        "jurisdiction": "City of San Antonio",
        "passage_date": "2018-11-01",
        "effective_date": "2018-11-01",
        "summary": "Passed by City Council 8-2 on November 1, 2018 following a stakeholder task force convened after a February 2017 Council Consideration Request; the regulations took effect immediately, with a 90-day grace period (to roughly January 30, 2019) before existing operators could be cited. The ordinance created Chapter 16, Article XXII and UDC Sec. 35-374.01, defining a short term rental as a residential dwelling unit or portion thereof rented for less than 30 consecutive days and not less than 12 hours, and splitting STRs into Type 1 (owner or operator occupied, owner generally present, may rent less than a whole unit) and Type 2 (not owner or operator occupied, must rent an entire dwelling unit). Every unit needs its own permit ($100 application, $100 renewal, three-year term) supported by owner/operator/agent contact information, a 24-hour emergency contact, floor and parking plans, a sworn health-and-safety self-certification, and written proof of registration with the Finance Department for Hotel Occupancy Tax. Type 1 units are allowed by right with no density cap; Type 2 units are capped at 12.5 percent of the units on a residential block face (at least one per block face) and at one unit in multi-family buildings of five to seven units or 12.5 percent in buildings of eight or more, with a Board of Adjustment special exception ($400) required to exceed the cap. STRs were added as permitted uses across residential zoning districts but are barred from C-3, L, I-1 and I-2, and any property receiving a City Housing Incentive is ineligible for a Type 2 permit. Other provisions include occupancy limits under the property maintenance code, off-street parking, insurance, fire extinguisher and smoke/CO detector requirements, a ban on weddings and other event uses, a requirement that the permit number appear in every advertisement or online listing, mandatory remittance of state, county and city HOT, permit revocation after three confirmed citations in any six-month period or for HOT arrearage unpaid 90 days after a delinquency notice, and Class C misdemeanor fines of $200 to $500 per day. Type 2 STRs already registered and current on HOT as of November 1, 2018 could claim nonconforming rights, which do not transfer on sale. Airbnb and HomeAway both submitted letters supporting the ordinance.",
        "measures": measures(
            registration="increase",
            rental_type="increase",
            time="increase",
            unit_type="increase",
            host_presence="increase",
            primary_residence="increase",
            host_compliance="increase",
        ),
    },
    {
        "title": "City of San Antonio Ordinance 2022-11-03-0831 - annual Unified Development Code amendments, Sec. 35-374.01 short-term rental density calculation and accessory dwelling unit cross-reference",
        "jurisdiction": "City of San Antonio",
        "passage_date": "2022-11-03",
        "effective_date": "2023-01-01",
        "summary": "Adopted November 3, 2022 as part of the periodic omnibus UDC amendment cycle under UDC Sec. 35-111, effective January 1, 2023. The STR-relevant change added to Sec. 35-374.01(c) the rule that the permitted number of Type 2 short term rentals on a block face or within a multi-family structure shall not round up (14 units x 12.5 percent = 1.75, so one Type 2 STR is permitted), tightening a block-face cap that staff had previously administered by rounding. Renewal applications that had already been approved administratively through rounding up remain eligible for renewal without a Board of Adjustment special exception, but new applications exceeding 12.5 percent of block-face units must obtain a special exception under Sec. 35-399.03. The same ordinance amended Sec. 35-371 (Accessory Dwellings) to add subsection (a)(4) requiring that accessory dwelling units used as short-term rentals comply with Sec. 35-374.01, which in combination with the ADU owner-occupancy rule confines ADU short-term rentals to Type 1 (owner living on site) and excludes Type 2 use of ADUs. Permit fees, permit procedures, HOT obligations and platform duties were untouched.",
        "measures": measures(
            rental_type="increase",
            unit_type="increase",
        ),
    },
    {
        "title": "City of San Antonio Ordinance 2024-06-13-0433 - amendments to City Code Chapter 16, Article XXII (Short Term Rentals): permit fees, enforcement, and platform obligations",
        "jurisdiction": "City of San Antonio",
        "passage_date": "2024-06-13",
        "effective_date": "2024-06-13",
        "summary": "Passed 9-0 on June 13, 2024, the first overhaul of the 2018 ordinance, following a stakeholder task force directed by the Planning and Community Development Committee in November 2023. Because it carried eight or more affirmative votes it took effect immediately, except new Sec. 16-1104.01 (Hotel Occupancy Tax) which took effect 90 days after enactment on September 12, 2024. Three-year permit fees rose from $100 to $300 for Type 1 and $450 for Type 2, the first fee differential penalizing non-owner-occupied rentals, with the extra revenue funding a dedicated STR code compliance officer. Applications are denied and the fee forfeited if required information is not supplied within 45 days, and providing false documentation triggers a one-year bar on reapplying for that property. A new Sec. 16-1103(b)(3) blocks corner-lot operators from choosing the more favorable block face. New Sec. 16-1104.01 requires every owner or operator to file a monthly HOT report even when the unit was not rented or a platform collected on their behalf, and requires any short term rental platform that collects Texas state HOT in San Antonio to collect and remit City of San Antonio and Bexar County HOT directly to the city; platforms that do not collect state HOT are exempt and their operators remain personally liable. Sec. 16-1103(c) requires all platforms to make owners include a permit number in every San Antonio listing and to remove, within ten business days, any listing the city identifies by URL as lacking a valid, unexpired, unrevoked permit. Enforcement was strengthened with mandatory compliance meetings with the Development Services director for properties generating excessive complaints, civil enforcement before an administrative hearing officer or by district court injunction alongside criminal citations, revocation after three accepted citations over a rolling three-year period (replacing three in six months), and posted quiet hours (10 p.m.-6 a.m. Sunday-Thursday, 11 p.m.-6 a.m. Friday-Saturday, 63 decibels) for units with outdoor amenities. Density caps and the Type 1 / Type 2 structure were not changed. Implementation of platform tax collection slipped past the announced October 1, 2024 date; the city's revised portal launched March 10, 2025 with Airbnb and Vrbo collecting City HOT beginning with February 2025 receipts.",
        "measures": measures(
            registration="increase",
            primary_residence="increase",
            host_compliance="increase",
            platform_compliance="increase",
        ),
    },
]

SAN_ANTONIO_UPDATE = {
    "legislative_history": LEGISLATIVE_HISTORY,
    # Airbnb had collected the 6% Texas state HOT since 2017-05-01 under an agreement with the
    # Comptroller, but never had a voluntary collection agreement with San Antonio; talks in 2018
    # stalled over back taxes. City HOT collection by Airbnb was compelled by Ordinance
    # 2024-06-13-0433 (Sec. 16-1104.01). The city's official date for platforms paying City HOT on
    # operators' behalf is 2025-03-10, when the revised reporting portal launched; the first
    # covered receipts were February 2025 bookings.
    "airbnb_tax_collection_date": "2025-03-10",
    # No evidence of Airbnb sharing listing- or host-level data with San Antonio. The 2024
    # ordinance runs the other way (the city notifies platforms of listings to remove by URL),
    # the city relies on a third-party scraping vendor (Avenu / Host Compliance) to find
    # unpermitted units, and the city's March 2025 webinar states platform HOT is "remitted to
    # the city with no detail" and properties get no property-level credit.
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
    matches[0].update(SAN_ANTONIO_UPDATE)

    with JSON_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"updated {CITY}, {STATE}: {len(LEGISLATIVE_HISTORY)} legislative history entries")


if __name__ == "__main__":
    main()
