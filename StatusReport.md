# Milestone 3 Status Report

## Task Updates
### Raw Data Organization and Documentation

Owen organized the three original World Bank Excel workbooks in [data/raw](data/raw/). The files contain GDP in current US dollars, access to electricity as a percentage of the population, and life expectancy at birth in years. The repository includes [indicator and source documentation](docs/DATA_SOURCES.md), a [data license document](DATA_LICENSE.md), and a [SHA-256 checksum list](data/raw/CHECKSUMS.sha256).

### Raw Data Quality Assessment

Owen completed the initial quality assessment of the three source files. Each workbook contains 266 reporting entities and 66 year columns. Across those columns, 15.6% of GDP values, 53.7% of electricity access values, and 2.1% of life expectancy values are missing. The workbooks contain the same set of country codes. The assessment found no duplicate codes within a workbook and no differences in the names associated with those codes across workbooks. The assessment also flagged large year-to-year changes for review. The methods and findings are available in the [assessment script](scripts/raw_data_quality_assessment.py) and the [raw data quality report](results/quality_report_raw.md).
### Initial Data Cleaning and Integration

I reshaped the three World Bank datasets into long format so that each row represents one reporting entity in one year. The intermediate files are [GDP](data/cleaned/gdp_long.csv), [electricity access](data/cleaned/electricity_access_long.csv), and [life expectancy](data/cleaned/life_expectancy_long.csv).

I merged the three tables using `Country Code` and `Year` and saved the result as [world_bank_integrated.csv](data/cleaned/world_bank_integrated.csv). The merged table contains 17,556 rows with no missing or duplicate merge keys. I kept the original missing indicator values. Of the merged rows, 7,817 have values for all three indicators.

The [cleaning script](scripts/clean_data.py) converts the three Excel files into long-format tables, and the [integration script](scripts/integrate_data.py) merges them by `Country Code` and `Year`.

### Post-Integration Assessment

The [post-integration audit script](scripts/data_quality_assessment.py) produces a [quality report](results/quality_report_integrated.md) with coverage and missing-value counts. For accuracy, the script compares the integrated values against the cleaned input tables using country code and year. It found no missing keys or value mismatches, including when checking whether missing values stayed missing. All observed values also passed basic range checks for GDP, electricity access, and life expectancy. For consistency, the script found zero exact duplicate rows, duplicate country-year keys, missing key values, or country codes with conflicting names. Together, these results show that the integration preserved the observations from the cleaned input tables.

For completeness, all 266 reporting entities and 66 year labels from 1960 through 2025 survived the outer join. They include countries, territories, and aggregates. Of 17,556 integrated rows, 7,817 (44.5%) have all three values, covering 260 entities. Electricity access has the highest missing share at 53.7%, followed by GDP at 15.6% and life expectancy at 2.1%. For timeliness, the workbooks were updated on October 8, 2026. The latest year with all three indicators is 2024, which has 247 complete rows. The 2025 rows contain 234 GDP values and no observations for the other two indicators.

## Updated Timeline

- **October 22 — Initial project plan (all members).** Completed. The initial plan is available in the [project-plan release](https://github.com/Aphorism-Z/Course-Project-Group-123/releases/tag/project-plan).
- **October 29 — Raw data organization (Owen).** Completed. The original workbooks, source documentation, license information, and checksum list were pushed to GitHub on November 18.
- **November 5 — Raw data quality assessment (Owen).** The initial assessment of all three workbooks and its results were committed by November 19.
- **November 12 — Initial cleaning and integration (Xingyi).** Completed on November 19. The repository contains the two processing scripts, the three long-format tables, and the integrated dataset.
- **November 17 — Integrated data assessment (Xingyi and Alexander).** In progress. We completed the initial merge checks. The review of aggregate rows and year coverage is pending. The proposed target is November 30.
- **November 19 — Milestone 3 status report (all members).** Finalize the report and project plan update, commit individual contribution summaries, and publish the `status-report` release.
- **November 26 — Analysis, visualizations, and workflow (Xingyi and Alexander).** The proposed target is December 3, after Thanksgiving break. Complete the initial analysis and figures, connect the scripts, and document the software dependencies.
- **December 2 — Documentation and workflow testing (all members).** The proposed target is December 5. Finish the data dictionary, metadata, and final README, then test the workflow from a fresh copy of the repository.
- **December 6 — Final review (all members).** Review the report, results, repository links, and contributions.
- **December 8 — Final submission (all members).** Publish the final release and submit its URL.

## Changes to the Project Plan
The original plan targeted November 12 for initial cleaning and integration. We completed that work on November 19. We have verified the structure and values of the merged dataset. The remaining work is to define the sample for analysis, including how to identify aggregate rows and choose a period with adequate coverage across all three indicators.

The proposed timeline places the remaining data checks and initial analysis after Thanksgiving break. Reviewing the analysis sample first will allow us to report which entities and years the comparisons represent.
## Challenges and Next Steps
**Uneven coverage across indicators.** GDP has reported values from 1960 through 2025, life expectancy from 1960 through 2024, and electricity access from 1990 through 2024. Coverage varies by reporting entity within those ranges. We preserved missing values during cleaning and integration. We propose 1990–2024 as a candidate period, subject to a review of country-level coverage. Before choosing the final years, we will count how many countries have values for all three indicators in each year. The [raw data quality report](results/quality_report_raw.md) documents these differences in coverage.

**Country and aggregate records appear together.** The source files contain records for individual countries as well as regions, income groups, and the world total. We kept these records in the integrated table. Before comparing countries, we will review the World Bank metadata to identify the aggregate codes. The [aggregate review file](results/records_for_agg_review.csv) provides a starting point.

**Large changes need context.** The assessment script flagged unusually large year-to-year changes. A flagged change may reflect a real event. Before excluding any flagged values, we will review those that could materially affect the analysis and document the basis for any exclusion. The flags are available for [GDP](results/large_jumps_gdp.csv), [electricity access](results/large_jumps_elec.csv), and [life expectancy](results/large_jumps_life_exp.csv).
## Individual Contributions

### Xingyi Wang
For this milestone, I converted the three World Bank datasets into long format, joined them by country code and year, and added the three intermediate tables and the integrated dataset to the repository.
### Owen Rives
For this milestone, I organized the raw World Bank files and documented their sources, indicator definitions and licenses, recorded SHA-256 checksums, wrote a script that tests the raw data's accuracy, completeness, timeliness, and consistency, and added the quality report and my manual spot-check notes to the repository.
### Alexander Zhao
For this milestone, I worked on the post-integration data quality assessment. I checked accuracy, completeness, etc again for the integrated data. A final data quality assessment file is added as well.
