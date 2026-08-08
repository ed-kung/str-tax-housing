"""Add the Philadelphia, PA short-term-rental legislative history to str_regulations.json.

Writes to AGENT_DATA_PATH/str_regulations.json, updating the entry for the first
city in the list that does not yet have "agent_checked": True.
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

AGENT_DATA_PATH = Path(os.environ["AGENT_DATA_PATH"])
JSON_PATH = AGENT_DATA_PATH / "str_regulations.json"

CITY = "Philadelphia"
STATE = "PA"

LEGISLATIVE_HISTORY = [
    {
        "title": "City of Philadelphia Bill No. 110845 - repeal and replacement of Title 14 of The Philadelphia Code (Zoning and Planning); Visitor Accommodations use category",
        "jurisdiction": "City of Philadelphia",
        "passage_date": "2011-12-15",
        "effective_date": "2012-08-22",
        "summary": "Passed by City Council on December 15, 2011, signed by Mayor Michael Nutter on December 22, 2011, and effective eight months later on August 22, 2012. The ordinance repealed the 1962-era zoning code and adopted an entirely new Title 14. It is included here because it created the use framework that still governs short-term rentals in Philadelphia: 'Visitor Accommodations' (Sec. 14-601(7)(n)) is a commercial use, permitted by right only in certain commercial, mixed-use and industrial districts and not in lower-density residential districts, and the code recognized no accessory residential short-term rental use. The practical effect through June 2015 was that renting a dwelling unit or room to transients in a residential district was not a permitted use, which is why the 2015 ordinance was described as 'legalizing' Airbnb in Philadelphia. It imposed no host registration, host-presence, primary-residence or platform obligations of its own, and did not change the pre-existing prohibition on transient lodging in residential districts; it recodified it.",
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "no change",
            "platform_compliance_requirements": "no change",
        },
    },
    {
        "title": "City of Philadelphia Bill No. 150441-A - 'Limited Lodging' added to the Zoning Code (Sec. 14-604(13)); Hotel Room Rental Tax extended to short-term rentals (Chapter 19-2400)",
        "jurisdiction": "City of Philadelphia",
        "passage_date": "2015-06-18",
        "effective_date": "2015-07-01",
        "summary": "Introduced by Councilmember William Greenlee on behalf of the Nutter administration in May 2015 and timed to the September 2015 papal visit, passed 15-0 by City Council and signed by Mayor Michael Nutter on June 18, 2015, effective July 1, 2015. Philadelphia's first short-term-rental-specific law and the largest US city at the time to legalize online-platform rentals. It added Sec. 14-604(13) 'Limited Lodging' as an accessory use of a dwelling unit, permitted only when arranged through a booking agent, in two categories: Limited Lodging, Short Term (fewer than 91 days of visitor accommodation per year, no more than 30 consecutive days per visitor, no use permit required) and Limited Lodging Home (more than 90 but no more than 180 days per year, use permit required, and only conducted by the 'primary resident,' defined as the owner entitled to a homestead exclusion or a renter living in the unit more than half the year with the owner's authorization). Operating standards required the unit to remain a household living unit with no more than three unrelated occupants including the host, prohibited signs, separate street-visible entrances and changes to residential character, restricted guests of lodgers to 8:00 a.m. to midnight, required smoke and carbon monoxide alarms, trash and noise notifications, host or designee contact information for complaints, one year of records demonstrating primary residency and rental dates, and subjected limited lodging to the Fair Practices Ordinance. Rentals longer than 30 days required a rental license. On the tax side it amended Chapter 19-2400 to define 'booking agent,' to let a booking agent collect and remit the 8.5% Hotel Room Rental Tax, Tourism and Marketing Tax and Hospitality Promotion Tax on the operator's behalf, and to require booking agents on request to give the Department of Revenue a list of all Philadelphia operators with addresses and contact information, to report quarterly on listed operators for whom they do not collect, and to notify operators of their tax and license obligations, with fines up to $2,000 per occurrence.",
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "decrease",
            "time_restrictions": "increase",
            "unit_type_restrictions": "decrease",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "Pennsylvania Act 109 of 2018 (House Bill 1511) - hotel occupancy tax; booking agents; accommodation fees; Tourism Promotion Fund",
        "jurisdiction": "Commonwealth of Pennsylvania",
        "passage_date": "2018-10-24",
        "effective_date": "2019-01-22",
        "summary": "Signed by Governor Tom Wolf on October 24, 2018 and effective 90 days later. It amended Article II of the Tax Reform Code of 1971 to add definitions of 'booking agent,' 'accommodation fee' and 'discount room charge' and to rewrite Section 210 so that a booking agent collecting payment for rent must collect and remit the 6% state hotel occupancy tax and, expressly, any additional or optional local hotel tax imposed under the Pennsylvania Intergovernmental Cooperation Authority Act for Cities of the First Class and 64 Pa.C.S. Ch. 60 (Pennsylvania Convention Center Authority), the statutes that authorize Philadelphia's hotel room rental taxes, as well as under the Community and Economic Improvement Act, The County Code and the Second Class County Code. The tax base was extended to the booking agent's accommodation fee, with that portion deposited in a new Tourism Promotion Fund, and an operator was relieved of liability for tax owed on the accommodation fee. This converted platform tax collection in Philadelphia from a voluntary arrangement (Airbnb had collected the city tax since July 2015 and the state tax since July 1, 2016) into a statutory duty applying to all booking agents. It imposed no licensing, zoning, occupancy or land-use requirements on hosts.",
        "measures": {
            "registration_requirements": "no change",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "decrease",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "City of Philadelphia Bill No. 210081 - Limited Lodging Operator License and Limited Lodging and Hotels Booking Agent License (Philadelphia Code Secs. 9-3909 to 9-3911); amendments to Sec. 14-604(13) and Chapter 19-2400",
        "jurisdiction": "City of Philadelphia",
        "passage_date": "2021-06-10",
        "effective_date": "2022-04-01",
        "summary": "Introduced by Councilmember Mark Squilla in February 2021 after nuisance and violence complaints in his district, modeled on Boston and New York City rules, passed unanimously by City Council on June 10, 2021 and signed by Mayor Jim Kenney on June 23, 2021. The zoning and hotel tax sections (Sections 3 and 4) took effect immediately on June 23, 2021; the licensing sections (Sections 1 and 2) took effect April 1, 2022. It rewrote Sec. 14-604(13) to remove the two limited lodging categories and the 90-day permit threshold and 180-day annual cap, leaving Limited Lodging as accommodation of visitors by the primary resident for no more than 30 consecutive days per visitor, with 'primary resident' narrowed to a natural person who owns the unit and holds the homestead exclusion, or a renter who is a natural person, occupies the unit as a primary domicile more than half the year and has written authorization from the owner. New Sec. 9-3909 requires a Limited Lodging Operator License ($150 per year) for any limited lodging, available only to a primary resident (and in the Tenth Councilmanic District only to a primary resident who owns the property, excluding renters), conditioned on a commercial activity license, no outstanding Title 4 violations, proof of zoning compliance, disclosure of every natural person holding more than a 49% equity interest in the property or owner (or the two largest interests), and lead paint safety compliance; the license number must appear in all advertising. New Sec. 9-3910 requires any booking agent to hold a Limited Lodging and Hotels Booking Agent License ($7,000 initial, $5,000 renewal), to obtain evidence of a valid operator license or hotel-designated rental license and written consent to disclose information to the City before booking a property, to remove a listing within five business days of City notice that it is unlicensed, and to report operator transaction information to the Department on the schedule the Department sets by regulation. Sec. 9-3911 makes violations Class II offenses per day (up to $1,000 per day), with ownership misrepresentation a Class III offense. Chapter 19-2400 was amended to make booking agent collection and remittance of the Hotel Room Rental Tax, Tourism and Marketing Tax and Hospitality Promotion Tax mandatory for limited lodging rather than optional. Units with no primary resident fall outside limited lodging entirely and require a Visitor Accommodations zoning permit (available by right only in commercial and mixed-use districts, otherwise requiring a Zoning Board of Adjustment variance) plus a hotel-designated rental license. Implementation was administratively deferred twice, from April 1, 2022 to July 1, 2022 and then to January 1, 2023, when platforms began requiring license numbers; L&I began ordering delisting of unlicensed properties on July 12, 2023.",
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "increase",
            "time_restrictions": "decrease",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "City of Philadelphia Bill No. 230647 - shared retaining wall exception to licensing bars, including the Limited Lodging Operator License (Sec. 9-3909(4)(b))",
        "jurisdiction": "City of Philadelphia",
        "passage_date": "2023-11-30",
        "effective_date": "2023-12-13",
        "summary": "Passed by City Council on November 30, 2023, signed by Mayor Kenney on December 13, 2023 and effective immediately. The ordinance is principally about unsafe and imminently dangerous shared retaining walls (Title 4 Subcodes A and PM), but it also amended Sec. 9-3909(4)(b) to add an exception allowing the Department of Licenses and Inspections to promulgate regulations under which a Limited Lodging Operator License may be issued despite an outstanding violation of Section PM-108.1.3 (unsafe shared retaining walls), with parallel exceptions for rental licenses under Sec. 9-3901(2) and Certificates of Rental Suitability under Sec. 9-3903(2). This is a narrow technical relaxation of one disqualifying condition for the short-term rental operator license; it changed no zoning, occupancy, residency, duration or platform requirement.",
        "measures": {
            "registration_requirements": "decrease",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "no change",
            "host_compliance_requirements": "no change",
            "platform_compliance_requirements": "no change",
        },
    },
]

AIRBNB_TAX_COLLECTION_DATE = "2015-07-15"
AIRBNB_DATA_SHARING_DATE = "2023-03-30"


def main() -> None:
    with open(JSON_PATH) as f:
        data = json.load(f)

    idx = next(i for i, rec in enumerate(data) if not rec.get("agent_checked"))
    rec = data[idx]
    if (rec["city"], rec["state"]) != (CITY, STATE):
        raise SystemExit(
            f"First unchecked entry is {rec['city']}, {rec['state']}, expected {CITY}, {STATE}"
        )

    rec["legislative_history"] = LEGISLATIVE_HISTORY
    rec["airbnb_tax_collection_date"] = AIRBNB_TAX_COLLECTION_DATE
    rec["airbnb_data_sharing_date"] = AIRBNB_DATA_SHARING_DATE
    rec["agent_checked"] = True

    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    print(f"Updated index {idx}: {rec['city']}, {rec['state']} "
          f"({len(LEGISLATIVE_HISTORY)} legislative entries)")


if __name__ == "__main__":
    main()
