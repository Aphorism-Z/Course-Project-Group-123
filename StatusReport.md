# Milestone 3 Status Report

## Task Updates
### Initial Data Cleaning and Integration

I reshaped the three World Bank datasets into long format so that each row represents one reporting entity in one year. The intermediate files are [GDP](data/cleaned/gdp_long.csv), [electricity access](data/cleaned/electricity_access_long.csv), and [life expectancy](data/cleaned/life_expectancy_long.csv).

I merged the three tables using `Country Code` and `Year` and saved the result as [world_bank_integrated.csv](data/cleaned/world_bank_integrated.csv). The merged table contains 17,556 rows with no missing or duplicate merge keys. I kept the original missing indicator values. Of the merged rows, 7,817 have values for all three indicators.
## Updated Timeline

## Changes to the Project Plan

## Challenges and Next Steps

## Individual Contributions

### Xingyi Wang
For this milestone, I converted the three World Bank datasets into long format, joined them by country code and year, and added the three intermediate tables and the integrated dataset to the repository.
### Owen Rives

### Alexander Zhao
