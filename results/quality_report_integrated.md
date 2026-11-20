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
