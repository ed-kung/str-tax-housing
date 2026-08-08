"""Add short-term-rental legislative history and platform enforcement data for Los Angeles, CA.

Updates the first unchecked entry in AGENT_DATA_PATH/str_regulations.json.
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
        "title": "Ordinance No. 185451 (Council File 12-1824-S1), \"Party House\" / Loud or Unruly Gatherings Ordinance - LAMC Sec. 41.58.1",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-02-21",
        "effective_date": "2018-04-15",
        "summary": (
            "Adopted by the City Council February 21, 2018, approved by Mayor Garcetti February 27, 2018, "
            "published March 6, 2018 and effective April 15, 2018. Added LAMC Sec. 41.58.1 declaring loud or "
            "unruly gatherings at a residence a public nuisance and subjecting both the property owner and the "
            "responsible party (including a person renting the residence) to escalating administrative "
            "citations, and amended LAMC Sec. 11.2.04 on fine amounts. LAPD posts a notice of violation on the "
            "residence, and the Council amended the ordinance so that home-sharing and short-term rental "
            "activity is barred at the property while a notice of violation is posted. It is a general nuisance "
            "law rather than a short-term rental regime, but it was driven largely by party houses operated as "
            "short-term rentals and gave the city its first STR-specific enforcement hook, a year before the "
            "Home-Sharing Ordinance took effect."
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
        "title": "Ordinance No. 185931 (Council File 14-1635-S2), \"Home-Sharing Ordinance\" - LAMC Sec. 12.22 A.32",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2018-12-11",
        "effective_date": "2019-07-01",
        "summary": (
            "Adopted by the City Council December 11, 2018 after roughly four years of hearings (Council File "
            "14-1635 opened 2014), approved by the Mayor and published December 21, 2018, effective July 1, "
            "2019, with enforcement deferred to November 1, 2019 after a four-month implementation and outreach "
            "phase. Amended LAMC Secs. 12.03, 12.12.2, 12.13, 12.13.5, 12.22, 12.24, 19.01 and 21.7.2 and added "
            "Sec. 12.22 A.32. Short-term rental (30 consecutive days or less) had already been prohibited under "
            "the city's zoning code in most residential zones, so the ordinance simultaneously created the "
            "first legal pathway for home-sharing and imposed a binding registration and enforcement regime on "
            "an activity that had been largely unpoliced. Key provisions: home-sharing is an accessory use "
            "limited to the host's primary residence, defined as the sole residence in which the host lives "
            "more than six months of the calendar year; a cap of 120 rented days per calendar year unless the "
            "host obtains an Extended Home-Sharing registration (unlimited days, requiring at least six months "
            "of prior registration or 60 days of hosting, no nuisance violations, a much higher fee and "
            "discretionary review with a public hearing if two or more citations were issued in the prior three "
            "years); mandatory registration with the Department of City Planning, an annual renewal, and the "
            "registration number posted on every advertisement; a Transient Occupancy Tax registration "
            "certificate unless the host lists exclusively on platforms with a city Platform Agreement; a "
            "per-night fee for each booked night, deposited into a short-term rental enforcement fund, with the "
            "amount deferred to a later Council action; and exclusion of units covered by the Rent "
            "Stabilization Ordinance, covenanted affordable units, units in buildings whose owner has opted "
            "out, and units withdrawn under the Ellis Act within the preceding five years. Hosting platforms "
            "are barred from completing booking transactions for unregistered listings and must comply with the "
            "administrative guidelines, provide required data, or sign a Platform Agreement. Listings in the "
            "city fell from roughly 36,600 before the program to about 85 percent below that level by 2021."
        ),
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "increase",
            "time_restrictions": "increase",
            "unit_type_restrictions": "increase",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
    {
        "title": "City Council Resolution adopting Appendix A of the Home-Sharing Administrative Guidelines (hosting platform responsibilities) and the Master Platform Agreement (Council File 14-1635-S2)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2019-10-30",
        "effective_date": "2019-11-01",
        "summary": (
            "LAMC Sec. 12.22 A.32(f) required hosting platforms to support enforcement but left the mechanics to "
            "guidelines that the Council had to adopt by resolution. The Planning and Land Use Management "
            "Committee approved Appendix A on October 22, 2019 and the Council adopted the resolution and the "
            "Master Platform Agreement template on October 30, 2019 (Council action final November 1, 2019, the "
            "Home-Sharing Ordinance enforcement date). Appendix A gives platforms three compliance options: "
            "follow the ordinance's default duties, verify registration numbers under the administrative "
            "guidelines, or execute a Platform Agreement with the city. A Platform Agreement is available only "
            "to platforms that already have a Transient Occupancy Tax collection agreement with the Office of "
            "Finance and that agree to collect the per-night fee; it obligates the platform to remove "
            "categorically ineligible listings supplied by the city and, once the application programming "
            "interface is live, to stop bookings and block calendars within 96 hours of a city Removal Notice. "
            "Each individual platform agreement must also be approved by the Council."
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
        "title": "City Council action setting the Home-Sharing per-night fee at $3.10 (LAMC Sec. 19.01, Council File 14-1635-S2)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2020-11-10",
        "effective_date": "2020-12-01",
        "summary": (
            "The Home-Sharing Ordinance created a per-night fee on every booked home-sharing night but deferred "
            "setting the amount. On November 10, 2020 the City Council set the fee at $3.10 per night, and hosts "
            "became subject to it starting in December 2020. Revenue is dedicated to short-term rental "
            "enforcement. Platforms with a Platform Agreement collect and remit the fee to City Planning on "
            "behalf of their hosts (in practice only Airbnb); hosts booking through other platforms must self "
            "report and pay, and City Planning estimated compliance among those hosts at roughly 35 percent. "
            "The city collected about $1.34 million in per-night fees between January and July 2021. This is a "
            "cost and reporting obligation on top of the 14 percent Transient Occupancy Tax."
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
            "Signed by Governor Newsom and chaptered September 24, 2021 as an urgency statute, so it took effect "
            "immediately. Amended Government Code Secs. 25132 and 36900 to let cities and counties raise "
            "maximum fines for infractions of a short-term rental ordinance that pose a threat to public health "
            "or safety to $1,500 for a first violation, $3,000 for a second within a year, and $5,000 for each "
            "additional violation within a year, well above the $100/$200/$500 general infraction caps. It does "
            "not apply to a first-time failure to register or to pay a business license fee, and jurisdictions "
            "must offer a hardship waiver. This is enabling legislation: it raises the ceiling on penalties Los "
            "Angeles may impose for Home-Sharing Ordinance violations without itself changing what conduct is "
            "allowed, and the City Attorney's November 2024 report to the Council recommended using higher fine "
            "authority already available under the LAMC."
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
            "Signed October 13, 2023 and operative July 1, 2024. Added Business and Professions Code Sec. "
            "17568.6, barring any place of short-term lodging, and any website, application or centralized "
            "platform advertising one, from displaying a room rate that excludes mandatory fees, and requiring "
            "the total price including all government taxes and fees to be shown before the consumer reserves "
            "the stay. It expressly covers short-term rentals of 30 consecutive days or less booked through a "
            "platform. Violations carry civil penalties of up to $10,000 each, enforceable by a city attorney, "
            "district attorney, county counsel or the Attorney General, so the Los Angeles City Attorney can "
            "enforce it against Airbnb and similar platforms. It is a price-disclosure mandate on platforms "
            "rather than a land use or registration rule."
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
        "title": "City Council action adopting recommendations to strengthen Home-Sharing Ordinance enforcement (Council File 14-1635-S10)",
        "jurisdiction": "City of Los Angeles",
        "passage_date": "2025-03-18",
        "effective_date": "2025-03-18",
        "summary": (
            "This is a Council action adopting committee recommendations, not an ordinance; the implementing "
            "amendments to LAMC Sec. 12.22 A.32 were still in committee as of mid-2026. Acting on a 2021 motion "
            "by Councilmember Raman and reports from City Planning, the Los Angeles Housing Department and the "
            "City Attorney, the Council on March 18, 2025 directed departments to consolidate permitting and "
            "enforcement in a single unit, build a public portal of registrations and citations, hire more "
            "hearing officers, inspect properties before issuing permits, tighten proof-of-primary-residence "
            "requirements, restructure fees and fines, require platforms to verify registration electronically "
            "before completing a booking, and add a private right of action allowing any interested party to "
            "sue over unlawful short-term rental activity. Two changes took effect administratively right away: "
            "the city stopped sending written notices of code violation to illegal listings before referring "
            "them for citation, and it launched the public permit portal. Included because it materially "
            "changed enforcement practice, but it is a directive rather than enacted law."
        ),
        "measures": {
            "registration_requirements": "increase",
            "rental_type_restrictions": "no change",
            "time_restrictions": "no change",
            "unit_type_restrictions": "no change",
            "host_presence_requirements": "no change",
            "primary_residence_requirements": "increase",
            "host_compliance_requirements": "increase",
            "platform_compliance_requirements": "increase",
        },
    },
]

PLATFORM_ENFORCEMENT = [
    {
        "title": "Airbnb voluntary Transient Occupancy Tax collection agreement with the City of Los Angeles",
        "effective_date": "2016-08-01",
        "summary": (
            "Announced July 18, 2016 by city officials and Airbnb and effective August 1, 2016, an initially "
            "three-year voluntary collection agreement under which Airbnb collects and remits the city's 14 "
            "percent Transient Occupancy Tax on bookings made through its platform, sparing hosts from "
            "remitting it themselves. The agreement lets the city audit the remittances and preserves its "
            "ability to pursue hosts for prior tax liabilities, and it applies only to Airbnb bookings, not to "
            "bookings on other platforms. It was signed while short-term rentals were still effectively "
            "prohibited by the zoning code and while the Home-Sharing Ordinance was being drafted, and could be "
            "amended or terminated if the city adopted new short-term rental rules. The city administrative "
            "officer initially projected $5.8 million a year; Airbnb reported collecting and remitting more "
            "than $275 million between August 2016 and June 2023. Under the later Home-Sharing Administrative "
            "Guidelines, a TOT collection agreement with the Office of Finance became a precondition for "
            "signing a Home-Sharing Platform Agreement, and hosts who list exclusively on such platforms are "
            "relieved of separate TOT registration."
        ),
        "tax_compliance": "yes",
        "registration_compliance": "no",
        "other_compliance": "no",
    },
    {
        "title": "Home-Sharing Platform Agreement between the City of Los Angeles and Airbnb, Inc. (Council File 14-1635-S9)",
        "effective_date": "2019-11-06",
        "summary": (
            "The Council adopted the Master Platform Agreement template on October 30, 2019 and entered into an "
            "individual agreement with Airbnb on November 6, 2019 (Council action final November 8, 2019); "
            "Airbnb was and has remained the only hosting platform with such an agreement, covering roughly 55 "
            "percent of city listings. Beginning the later of November 1, 2019 or seven days after the city "
            "supplied its list, Airbnb had to take down listings the city identified as categorically "
            "ineligible - units subject to the Rent Stabilization Ordinance, covenanted affordable units, units "
            "in buildings whose owner opted out of home-sharing, and single-family properties subject to an "
            "Ellis Act withdrawal within five years - unless the listing carried a valid city registration "
            "number, and to cancel pending reservations for them. The agreement also commits Airbnb to collect "
            "and remit the Transient Occupancy Tax and the per-night fee for its hosts and sets up the "
            "application programming interface obligations. Airbnb removed thousands of ineligible units "
            "between late 2019 and early 2020."
        ),
        "tax_compliance": "yes",
        "registration_compliance": "yes",
        "other_compliance": (
            "yes - removal of rent-stabilized, covenanted affordable, owner-opted-out and Ellis Act listings, "
            "and collection of the per-night enforcement fee"
        ),
    },
    {
        "title": "City-Airbnb application programming interface for automated removal of non-compliant listings",
        "effective_date": "2020-08-31",
        "summary": (
            "Under the platform agreement the city (through its compliance vendor, formerly Host Compliance, "
            "now Granicus) sends Removal Notices over an application programming interface when a listing lacks "
            "a valid registration number, claims a false exemption, or is otherwise ineligible; Airbnb must "
            "stop bookings, block the calendar and remove the listing within 96 hours. After a two-week test in "
            "which about 1,350 listings were removed, Airbnb launched full API use on August 31, 2020, "
            "described by City Planning as the first system of its kind. Listings dropped roughly 14 percent "
            "immediately, and non-compliant listings fell from about 6,000 in August 2020 to about 2,300 and "
            "then to about 1,500 by August 2021. Later refinements include an Exempt List of licensed hotels "
            "and transient occupancy residential structures (December 2020), an API upgrade on July 6, 2021 "
            "targeting listings falsely claiming exemptions, and an Allow List of remaining permitted nights so "
            "platforms can block calendars at the 120-day cap. Separately, City Planning and neighborhood "
            "prosecutors agreed a protocol with Airbnb for submitting nuisance-property evidence through "
            "Airbnb's law enforcement portal, under which several dozen properties were delisted."
        ),
        "tax_compliance": "no",
        "registration_compliance": "yes",
        "other_compliance": (
            "yes - automated enforcement of the 120-day cap, of false exemption claims, and of nuisance "
            "delisting through Airbnb's law enforcement portal"
        ),
    },
    {
        "title": "Airbnb collection and remittance of the Home-Sharing per-night enforcement fee",
        "effective_date": "2020-12-01",
        "summary": (
            "After the Council set the per-night fee at $3.10 on November 10, 2020, hosts became liable for it "
            "starting December 2020. Because the Master Platform Agreement conditions eligibility on agreeing "
            "to collect the fee, Airbnb collects and remits it directly to the Department of City Planning on "
            "behalf of its hosts rather than leaving hosts to self-report; the first remittances arrived in "
            "January 2021 and roughly $1.34 million was collected in the first seven months of 2021. Hosts "
            "using platforms without an agreement must pay through the city's online portal, and City Planning "
            "estimated their compliance rate at only about 35 percent, so the arrangement is the main reason "
            "the fee is collected at all."
        ),
        "tax_compliance": (
            "yes - the per-night fee is a city enforcement fee collected alongside the 14 percent Transient "
            "Occupancy Tax that Airbnb already remits"
        ),
        "registration_compliance": "no",
        "other_compliance": "yes - funds the city's short-term rental enforcement program",
    },
]


def main() -> None:
    with JSON_PATH.open() as f:
        records = json.load(f)

    target = next(
        r for r in records if r["city"] == CITY and r["state"] == STATE
    )
    if target.get("agent_checked"):
        raise SystemExit(f"{CITY}, {STATE} is already marked agent_checked")

    target["legislative_history"] = LEGISLATIVE_HISTORY
    target["platform_enforcement"] = PLATFORM_ENFORCEMENT
    target["agent_checked"] = True

    with JSON_PATH.open("w") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"Updated {CITY}, {STATE}: "
        f"{len(LEGISLATIVE_HISTORY)} laws, {len(PLATFORM_ENFORCEMENT)} enforcement arrangements"
    )


if __name__ == "__main__":
    main()
