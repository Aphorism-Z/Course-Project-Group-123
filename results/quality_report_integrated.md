# Integrated data quality

## 1. Accuracy

- Negative GDP values: 0.
- Life expectancy outside 0–120 years: 0.
- Electricity access outside 0–100%: 0.

These ranges screen for implausible values. We also compared the merged values with the cleaned inputs to check that the join preserved them.

- GDP differences on matching keys: 0.
- ElectricityAccess differences on matching keys: 0.
- LifeExpectancy differences on matching keys: 0.

## 2. Completeness

| Column | Missing values | Missing percentage |
| --- | ---: | ---: |
| Country Code | 0 | 0.0% |
| Country Name | 0 | 0.0% |
| Year | 0 | 0.0% |
| GDP | 2,745 | 15.6% |
| ElectricityAccess | 9,434 | 53.7% |
| LifeExpectancy | 365 | 2.1% |

- Expected country-year pairs from the three cleaned inputs: 17,556.
- Expected pairs missing from the merge: 0.
- Unexpected pairs in the merge: 0.
- Rows with all three indicators: 7,817 (44.5%).
- Rows missing all three indicators: 127.

## 3. Timeliness

- Merged year labels: 1960–2025.
- Years with all three indicators: 1990–2024.
- The [source documentation](../docs/DATA_SOURCES.md) records October 8, 2026 as the workbook release date. Annual row counts are listed below.

| Indicator | First observation year | Last observation year |
| --- | ---: | ---: |
| GDP | 1960 | 2025 |
| ElectricityAccess | 1990 | 2024 |
| LifeExpectancy | 1960 | 2024 |

## 4. Consistency

- Year column type when read by pandas: `int64`.
- Rows missing a country code or year: 0.
- Present country codes outside the three-uppercase-letter format: 0.
- Country codes linked to multiple names: 0.

## 5. Duplicate records

- Exact duplicate rows: 0.
- Duplicate country-year rows: 0.

## 6. Dataset summary

- Shape: 17,556 rows and 6 columns.
- Reporting entities: 266, including countries, territories, and aggregates.
- Distinct year labels: 66.
- Entities with all three indicators in at least one row: 260.
- Entity codes with no complete row: ASM, GIB, INX, PRK, VGB, XKX.

Summary statistics include every available value in the merged CSV.

```text
           GDP  ElectricityAccess  LifeExpectancy
count 1.48e+04           8.12e+03        1.72e+04
mean  1.28e+12               81.5            64.9
std   5.93e+12               28.2            11.1
min   2.59e+06              0.534              11
25%   2.42e+09               70.3            57.8
50%   1.81e+10               98.6            67.3
75%   2.14e+11                100              73
max   1.18e+14                100            86.5
```

The [SHA-256 manifest](../data/raw/CHECKSUMS.sha256) documents raw file integrity.

<details>
<summary>Year-by-year counts and reporting-entity codes</summary>

| Year | Merged rows | Rows with all three indicators |
| ---: | ---: | ---: |
| 1960 | 266 | 0 |
| 1961 | 266 | 0 |
| 1962 | 266 | 0 |
| 1963 | 266 | 0 |
| 1964 | 266 | 0 |
| 1965 | 266 | 0 |
| 1966 | 266 | 0 |
| 1967 | 266 | 0 |
| 1968 | 266 | 0 |
| 1969 | 266 | 0 |
| 1970 | 266 | 0 |
| 1971 | 266 | 0 |
| 1972 | 266 | 0 |
| 1973 | 266 | 0 |
| 1974 | 266 | 0 |
| 1975 | 266 | 0 |
| 1976 | 266 | 0 |
| 1977 | 266 | 0 |
| 1978 | 266 | 0 |
| 1979 | 266 | 0 |
| 1980 | 266 | 0 |
| 1981 | 266 | 0 |
| 1982 | 266 | 0 |
| 1983 | 266 | 0 |
| 1984 | 266 | 0 |
| 1985 | 266 | 0 |
| 1986 | 266 | 0 |
| 1987 | 266 | 0 |
| 1988 | 266 | 0 |
| 1989 | 266 | 0 |
| 1990 | 266 | 89 |
| 1991 | 266 | 100 |
| 1992 | 266 | 117 |
| 1993 | 266 | 132 |
| 1994 | 266 | 138 |
| 1995 | 266 | 148 |
| 1996 | 266 | 160 |
| 1997 | 266 | 170 |
| 1998 | 266 | 180 |
| 1999 | 266 | 188 |
| 2000 | 266 | 250 |
| 2001 | 266 | 251 |
| 2002 | 266 | 255 |
| 2003 | 266 | 255 |
| 2004 | 266 | 255 |
| 2005 | 266 | 255 |
| 2006 | 266 | 256 |
| 2007 | 266 | 257 |
| 2008 | 266 | 257 |
| 2009 | 266 | 259 |
| 2010 | 266 | 259 |
| 2011 | 266 | 260 |
| 2012 | 266 | 258 |
| 2013 | 266 | 258 |
| 2014 | 266 | 259 |
| 2015 | 266 | 258 |
| 2016 | 266 | 257 |
| 2017 | 266 | 257 |
| 2018 | 266 | 257 |
| 2019 | 266 | 257 |
| 2020 | 266 | 256 |
| 2021 | 266 | 256 |
| 2022 | 266 | 255 |
| 2023 | 266 | 251 |
| 2024 | 266 | 247 |
| 2025 | 266 | 0 |

**Reporting-entity codes retained**

ABW, AFE, AFG, AFW, AGO, ALB, AND, ARB, ARE, ARG, ARM, ASM, ATG, AUS, AUT, AZE, BDI, BEL, BEN, BFA, BGD, BGR, BHR, BHS, BIH, BLR, BLZ, BMU, BOL, BRA, BRB, BRN, BTN, BWA, CAF, CAN, CEB, CHE, CHI, CHL, CHN, CIV, CMR, COD, COG, COL, COM, CPV, CRI, CSS, CUB, CUW, CYM, CYP, CZE, DEU, DJI, DMA, DNK, DOM, DZA, EAP, EAR, EAS, ECA, ECS, ECU, EGY, EMU, ERI, ESP, EST, ETH, EUU, FCV, FIN, FJI, FRA, FRO, FSM, GAB, GBR, GEO, GHA, GIB, GIN, GMB, GNB, GNQ, GRC, GRD, GRL, GTM, GUM, GUY, HIC, HKG, HND, HPC, HRV, HTI, HUN, IBD, IBT, IDA, IDB, IDN, IDX, IMN, IND, INX, IRL, IRN, IRQ, ISL, ISR, ITA, JAM, JOR, JPN, KAZ, KEN, KGZ, KHM, KIR, KNA, KOR, KWT, LAC, LAO, LBN, LBR, LBY, LCA, LCN, LDC, LIC, LIE, LKA, LMC, LMY, LSO, LTE, LTU, LUX, LVA, MAC, MAF, MAR, MCO, MDA, MDG, MDV, MEA, MEX, MHL, MIC, MKD, MLI, MLT, MMR, MNA, MNE, MNG, MNP, MOZ, MRT, MUS, MWI, MYS, NAC, NAM, NCL, NER, NGA, NIC, NLD, NOR, NPL, NRU, NZL, OED, OMN, OSS, PAK, PAN, PER, PHL, PLW, PNG, POL, PRE, PRI, PRK, PRT, PRY, PSE, PSS, PST, PYF, QAT, ROU, RUS, RWA, SAS, SAU, SDN, SEN, SGP, SLB, SLE, SLV, SMR, SOM, SRB, SSA, SSD, SSF, SST, STP, SUR, SVK, SVN, SWE, SWZ, SXM, SYC, SYR, TCA, TCD, TEA, TEC, TGO, THA, TJK, TKM, TLA, TLS, TMN, TON, TSA, TSS, TTO, TUN, TUR, TUV, TZA, UGA, UKR, UMC, URY, USA, UZB, VCT, VEN, VGB, VIR, VNM, VUT, WLD, WSM, XKX, YEM, ZAF, ZMB, ZWE

</details>
