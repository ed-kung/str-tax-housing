# Chandler, AZ short-term rental regulation dates

## Summary

Chandler, AZ was the first row in `AGENT_DATA_PATH/str_regulations.csv` without `agent_checked == True`. Chandler's first substantive short-term rental (STR) regulation was Ordinance No. 4939, which created City Code Chapter 22 ("Short-Term Rentals") and was adopted October 12, 2020; the requirements applied as of November 16, 2020. There is no Chandler-specific agreement with Airbnb. Arizona municipal transaction privilege tax (TPT) is collected by the state, and Airbnb's partnership with the Arizona Department of Revenue — announced by Gov. Doug Ducey in late 2016 — began collecting and remitting state and city TPT on behalf of hosts effective January 1, 2017. Confidence was recorded as **High** for the passage and effective dates, with the caveat that the Airbnb date is statewide rather than city-negotiated.

## Dates recorded

| Field | Value |
| --- | --- |
| `passage_date` | 2020-10-12 |
| `effective_date` | 2020-11-16 |
| `airbnb_cooperation_date` | 2017-01-01 |
| `agent_confidence` | High |
| `agent_checked` | True |

## Findings and reasoning

**Regulatory timeline.** Arizona's 2016 SB 1350 (A.R.S. § 9-500.39) preempted cities from banning or restricting STRs, effective January 1, 2017, so Chandler had no authority to regulate STRs before then. A 2019 amendment (HB 2672) restored limited authority — owner/emergency contact collection and a "verified violation" process — and Chandler responded with Ordinance No. 4939, creating Chapter 22 of the City Code. A 2022 amendment (HB 2374 / SB 1168) allowed municipal licensing, which Chandler implemented via Ordinance No. 5048.

**Passage date (2020-10-12).** The Municode codification note for every section of Chandler City Code Chapter 22 reads `(Ord. No. 4939, § 2(Exh.), 10-12-20; Ord. No. 5048, § 2(Exh.), 4-13-23, eff. 8-1-23)`. City staff independently confirmed the timing in the March 20, 2023 council study session: the Council "final adopted an ordinance to reflect those changes in state statute … October of 2020," and described the 2023 update as similar to "what we established when we first incorporated short-term rental ordinance into our code." This is treated as Chandler's first substantial STR policy.

**Effective date (2020-11-16).** The City of Chandler Tax & License page states: "Historically, as of November 16, 2020, City Code Chapter 22, required short-term rentals to be registered and operate under certain requirements." This is roughly 35 days after adoption rather than the standard 30-day Arizona referendum window, but it is the city's own stated date and was preferred over an inferred 30-day calculation.

**Airbnb arrangement (2017-01-01).** No Chandler-specific data-sharing or tax-collection agreement with Airbnb was found, and none would be expected: under SB 1350, online lodging marketplaces register with the Arizona Department of Revenue, which collects municipal TPT and distributes it to cities. Gov. Ducey and Airbnb announced a partnership in late 2016 under which Airbnb electronically files and remits state and local TPT on behalf of hosts, beginning January 1, 2017. Airbnb later reported $11.5M in Arizona tax revenue for 2017, its first year in the partnership, and $53.3M cumulative through late 2019.

**Later amendment (not recorded).** Ordinance No. 5048 was tentatively adopted March 20, 2023, given final adoption April 13, 2023, and took effect August 1, 2023. It replaced registration with a mandatory annual license ($250, prorated quarterly, expiring each June 30), added written neighbor notification, in-unit posting of license and emergency contact information, a prohibition on non-residential uses, up-to-12-month license suspension for repeated verified violations, and civil penalties up to $1,000/month for unlicensed operation. The delayed effective date was to allow system setup and community education. Chandler had 299 voluntarily registered STRs in 2022, with 131 calls for service at 46 identified properties.

**Confidence rationale.** High. Both the passage and effective dates come from official sources — the codified ordinance history in Municode and the city's own Tax & License page — and are corroborated by city staff testimony on the record. The one soft spot, noted in `agent_notes`, is that `airbnb_cooperation_date` reflects a statewide Arizona arrangement rather than a Chandler-negotiated agreement.

## Sources

- Chandler City Code Chapter 22, Municode Library: https://library.municode.com/az/chandler/codes/code_of_ordinances?nodeId=PTIIIPUSA_CH22SHRMRE
- City of Chandler Tax and License: https://www.chandleraz.gov/business/tax-and-license
- City of Chandler Short Term Rental: https://www.chandleraz.gov/business/tax-and-license/short-term-rental
- Chandler City Council Study Session transcript, March 20, 2023: https://chandleraz.new.swagit.com/videos/222395
- Chandler City Council Regular Meeting agenda packet, April 13, 2023: https://public.destinyhosted.com/chanddocs/2023/CC/20230413_855/AGENDApacket__04-13-23_0605_851.pdf
- A.R.S. § 9-500.39: https://azleg.gov/ars/9/00500-39.htm
- Arizona DOR Online Lodging Marketplace factsheet: https://azdor.gov/sites/default/files/2023-03/PUBLICATION_OLMfactsheet.pdf
- "Chandler Council OKs rental licenses, other new requirements," Daily Independent
- "Arizona takes steps toward embracing sharing economy," AZ Big Media

## Artifacts

- Updated: `AGENT_DATA_PATH/str_regulations.csv` (row 1, Chandler AZ)
