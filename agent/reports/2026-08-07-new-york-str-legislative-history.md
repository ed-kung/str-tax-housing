# New York, NY short-term-rental legislative history

**Summary.** New York, NY was the first city in `AGENT_DATA_PATH/str_regulations.json` without an
`agent_checked` value, so I researched its short-term-rental legislative history from 2008 forward and
wrote the entry back to the file with `agent_checked: 1`. Seven binding actions were identified: four
New York City local laws and three New York State chapters. The substantive rule that defines the New
York market — a 30-day minimum stay in Class A multiple dwellings unless the permanent occupant is
present — comes from state law (Chapter 225 of the Laws of 2010, enforced from May 1, 2011), while the
regime that actually binds platform activity is the city's registration law (Local Law 18 of 2022,
enforced from September 5, 2023). Both are flagged `primary_framework: true`. Airbnb began collecting
city-level tax in New York on **2025-03-01**, not in 2023 as several secondary sources claim, and the
first real data connection to the city dates to **2021-01-03** under Local Law 64 of 2020.

## Legislative history written to the JSON

| Passage | Effective | Enforced | Jurisdiction | Law |
| --- | --- | --- | --- | --- |
| 2010-07-16 | 2011-05-01 | 2011-05-01 | NY State | Ch. 225 of 2010, "Illegal Hotel Law" (MDL Sec. 4(8)(a)) — primary framework |
| 2012-10-02 | 2012-12-01 | 2012-12-01 | NYC | Local Law 45 of 2012, fines for illegal conversions |
| 2016-10-21 | 2016-10-21 | 2017-01-30 | NY State | Ch. 396 of 2016, advertising ban (MDL Sec. 121) |
| 2018-08-06 | 2019-02-02 | never | NYC | Local Law 146 of 2018, monthly booking-service reporting |
| 2020-07-07 | 2021-01-03 | 2021-01-03 | NYC | Local Law 64 of 2020, quarterly booking-service reporting |
| 2022-01-09 | 2023-01-09 | 2023-09-05 | NYC | Local Law 18 of 2022, registration law — primary framework |
| 2024-12-21 | 2025-03-01 | 2025-03-01 | NY State | Ch. 672 of 2024 as amended by Ch. 99 of 2025, registry and STR taxes |

## Findings and judgment calls

- **Enforcement dates diverge from effective dates three times.** Local Law 146 of 2018 was
  preliminarily enjoined on Fourth Amendment grounds on January 3, 2019, a month before its February 2,
  2019 effective date, and was superseded by Local Law 64 of 2020 before the injunction lifted, so its
  `enforcement_date` is null. The 2016 advertising ban was effective on signing but Airbnb's federal
  challenge was pending until a December 2, 2016 settlement; the Mayor's Office of Special Enforcement
  issued its first summonses in the week of January 30, 2017. Local Law 18 was effective January 9,
  2023 but platform verification was only enforced from September 5, 2023, after Airbnb's state-court
  challenge was dismissed.
- **Airbnb tax collection: 2025-03-01.** New York City never entered a voluntary collection agreement;
  it rebuffed Airbnb's 2014 and October 2016 offers because a tax deal would legitimize rentals that
  were illegal under state law. Collection began only when Chapter 672 of 2024 / Chapter 99 of 2025
  made booking services registered New York State sales tax vendors. The tax Airbnb collects in the
  city (7-8.875 percent sales tax plus the $1.50 per night New York City Hotel Unit Fee) embeds the
  city's own 4.5 percent local sales tax, so this qualifies as municipal-level collection. Airbnb still
  does not collect the separate 5.875 percent NYC Hotel Room Occupancy Tax.
- **Evidence for that date.** Archived versions of Airbnb's New York occupancy tax help page
  (`airbnb.com/help/article/2319`) list only upstate county hotel/motel occupancy taxes in the October
  2023, May 2024, August 2024, October 2024 and January 1, 2025 snapshots, with no state or city sales
  tax and no unit fee; the March 17, 2025 snapshot adds the "State of New York" section containing both.
  This contradicts aggregator sites (e.g. cityrulelookup.com) that date NYC collection to the start of
  Local Law 18 enforcement on September 5, 2023.
- **Airbnb data sharing: 2021-01-03.** Local Law 64 and the OSE rules took effect that day and set the
  initial reporting period as January 3 to March 31, 2021 (first report due May 31, 2021). The June/July
  2020 settlement produced the regime but transferred no data, and Local Law 146's reporting never
  operated. The tighter two-way connection — platforms querying the city's verification system before
  processing a transaction — followed on September 5, 2023.
- **Chapter number correction.** An earlier version of this record (in `str_regulations_old.json`)
  cited the 2024 state law as Chapter 656; the Senate action log for S885-C shows it was signed as
  Chapter 672 on December 21, 2024. Some secondary sources say December 24 ("Christmas Eve"); the
  Senate press release describes the signing as occurring on Saturday, which was December 21.
- **Nothing enacted after 2022 at the city level.** Airbnb-backed Intros 948-A and 1107-2024, which
  would have allowed unhosted rentals in one- and two-family homes, died in committee at the end of the
  2024-2025 session (final hearing December 18, 2025) and are excluded as non-binding.

## Artifacts

- `agent/scripts/03_str_regulations_new_york.py` — script that writes the entry (idempotent; refuses to
  overwrite an already-checked city and takes a timestamped backup first).
- `AGENT_DATA_PATH/str_regulations.json` — updated in place, index 0.
- `AGENT_DATA_PATH/str_regulations.json.20260807-234143.bak` — pre-update backup.

The next city without `agent_checked` is Los Angeles, CA.
