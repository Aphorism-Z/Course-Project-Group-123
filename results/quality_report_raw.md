# Raw data quality report

gdp: completeness

- Records: 266, year columns: 66
- Ovr missing pct: 15.6%
- Years w no data in any record: 0
- Records w no data in any year: 4
 -Gibraltar, Not classified, Korea, Dem. People's Rep., British Virgin Islands

gdp: timeliness

- Release date: nan
- First / Last year data shown: 1960 / 2025
- Records w data in past 3 yrs: {'2023': 252, '2024': 248, '2025': 234}

CONSISTENCY ACROSS DATASETS

- Same set of country codes in all files: True
- Dupe country codes per file: {'gdp': 0, 'life_exp': 0, 'elec': 0}
- Country names that differ from the GDP file: {'life_exp': 0, 'elec': 0}

- gdp: accuracy

- Lowest value: 2585955.87411804 (Tuvalu, 1970)
- Highest value: 118350166039396.0 (World, 2025)
- Yearly changes above 50%: 194

life_exp: completeness

- Records: 266, year columns: 66
- Ovr missing pct: 2.1%
- Years w no data in any record: 1(2025 to 2025)
- Records w no data in any year: 1
 -Not classified

life_exp: timeliness

- Release date: nan
- First / Last year data shown: 1960 / 2024
- Records w data in past 3 yrs: {'2023': 265, '2024': 265, '2025': 0}

CONSISTENCY ACROSS DATASETS

- Same set of country codes in all files: True
- Dupe country codes per file: {'gdp': 0, 'life_exp': 0, 'elec': 0}
- Country names that differ from the GDP file: {'life_exp': 0, 'elec': 0}

- life_exp: accuracy

- Lowest value: 10.989 (South Sudan, 1988)
- Highest value: 86.497 (Monaco, 2024)
- Yearly changes above 50%: 16

elec: completeness

- Records: 266, year columns: 66
- Ovr missing pct: 53.7%
- Years w no data in any record: 31(1960 to 2025)
- Records w no data in any year: 2
 -American Samoa, Not classified

elec: timeliness

- Release date: nan
- First / Last year data shown: 1990 / 2024
- Records w data in past 3 yrs: {'2023': 263, '2024': 263, '2025': 0}

CONSISTENCY ACROSS DATASETS

- Same set of country codes in all files: True
- Dupe country codes per file: {'gdp': 0, 'life_exp': 0, 'elec': 0}
- Country names that differ from the GDP file: {'life_exp': 0, 'elec': 0}

- elec: accuracy

- Lowest value: 0.533898532390594 (Uganda, 1994)
- Highest value: 100.0 (Aruba, 1990)
- Yearly changes above 50%: 58
