# IS 477 Project Plan

## Dataset Files and Sources

- **GDP dataset:** `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx`
  - Link to dataset: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
- **Access to electricity dataset:** `API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_987.xlsx`
  - Link to dataset: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS
- **Life expectancy dataset:** `API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx`
  - Link to dataset: https://data.worldbank.org/indicator/SP.DYN.LE00.IN

All datasets obtained from World Bank Group (World Bank Group - International Development, Poverty and Sustainability)

## Overview

The goal of our project is to explore the relationships between economic development, life expectancy, and access to electricity across different countries and regions. We will use three datasets from the World Bank: GDP (current US$), life expectancy at birth, and access to electricity (% of population). By combining these datasets, we hope to better understand how economic conditions are associated with people's living conditions in different parts of the world.

To accomplish this, we will first examine the structure and quality of each dataset, including missing values, data consistency, and differences in available years. We will then clean and organize the datasets using Python and Pandas. Since all three datasets contain country codes and yearly observations, we plan to use country codes and years as common keys to join them into one dataset. We will also distinguish individual countries and territories from regional and income-group aggregates to avoid misleading comparisons.

After integration, we will evaluate the quality of the combined dataset and use basic statistical analysis and visualizations to explore relationships between the three indicators. Throughout the project, we will document our data sources, cleaning methods, and integration process so that our workflow can be reproduced.

## Team Responsibilities

- **Owen** will focus on the datasets and their limitations. He will organize the downloaded data, describe the sources and indicators, check data quality, and review licenses and ethical concerns.
- **Xingyi** will manage the project timeline and track gaps that need further work or team discussion, coordinate team tasks and help clean and combine the datasets.
- **Alexander** will focus on the project overview and research questions. Guide the analysis, help create visualizations, and summarize the findings.

## Research Questions

Our main research question is:

**How are GDP, life expectancy, and access to electricity related across different countries and regions?**

To explore this question, we will focus on three smaller questions:

1. What is the relationship between a country's GDP and its life expectancy? Do countries with higher GDP generally have longer life expectancy?
2. What is the relationship between a country's GDP and its population's access to electricity? Do countries with higher GDP generally have greater access to electricity?
3. How does access to electricity relate to life expectancy, and are there countries that show different patterns from the overall trends?

## Datasets

We will be using 3 datasets from World Bank’s archives to answer our research questions:

- **GDP (Current US$):** GDP is the total amount of income earned through the production of goods and services in an economic territory during an accounting period. This dataset measures the total size of each country’s economy in US dollars, from 1960 onward.
- **Access to electricity (% of population):** This gives the share of each country’s population with electricity access, with data starting around 1990.
- **Life expectancy at birth, total (years):** This gives the average number of years a newborn (male or female) is expected to live, from 1960 onward.

These datasets were all most recently updated on Oct. 8 of this year, so the data is quite up to date. All of the datasets go up to the year 2024 or 2025, so we can get a pretty accurate and modern measure of all the data we will be using. Each dataset contributes a different but related piece of information: economic output, infrastructure/living conditions, and health quality. Together they will allow us to examine how wealth, electricity access, and life expectancy are connected (our 3 sub-questions). In terms of how they can be integrated, all three files share the same structure and identifiers. Each row is a country or region, identified by the columns Country Name and Country Code, and each following column for data is a year. We can link these datasets by matching on Country Code and year.

## Timeline

- **October 22:** Complete and commit the project plan on GitHub.
- **October 29:** Organize the downloaded datasets and document their sources, indicator definitions, file formats, and applicable licenses. Calculate SHA-256 checksums to record file integrity and establish a clear folder structure for raw data, cleaned data, scripts, documentation, and results. Responsible: Owen
- **November 5:** Check the accuracy, completeness, timeliness, and consistency of each dataset. Look for missing values, duplicate records, differences in available years, and records representing regions or income groups. Based on these checks, we will choose the years to study and decide how to clean the data. Responsible: Owen
- **November 12:** Complete the initial cleaning and integration scripts. Organize each dataset so that each row represents one country in one year, then combine the three datasets using country codes and years. Record the changes we make and identify records that do not match. Responsible: Xingyi
- **November 17:** Check the accuracy, completeness, timeliness, and consistency of the combined dataset. Look for duplicate records, check which countries and years remain after combining the data, and summarize the data. Update the project plan and draft the status report. Each member will write a short summary of their contributions. Responsible: Xingyi, Alexander
- **November 19:** Finish the status report and commit all work completed so far to GitHub.
- **November 26:** Finish the basic statistical analysis and visualizations. We will create a run-all script that runs the separate scripts in order, from data acquisition through analysis. We will also list the required software packages and versions. Responsible: Xingyi, Alexander
- **December 2:** Finish the data dictionary, machine-readable metadata, references, licenses, and all required sections of the final README. We will download a fresh copy of the repository and test the full workflow, fixing any problems that prevent it from running. Responsible: All members.
- **December 6:** Review the results, documentation, file links, and each member’s contributions. Check the project against the final submission checklist and confirm that running the workflow produces the reported results. Responsible: All members
- **December 8:** Commit to GitHub, submit URL.

## Constraints

After looking at our datasets, we identified some possible setbacks. One downside with this data is that, unlike life expectancy, electricity access data starts for most countries at 1990 rather than 1960. These empty values could be explained by some sort of data collection limit (for instance, World Bank might have only started collecting this type of data starting at 1990), but it’s something to keep in mind as we continue our research. GDP is also missing some data in the early years for countries such as Afghanistan, Armenia, and Curacao, which should also be addressed. In terms of data usage, all 3 of the datasets operate under CC BY-4.0, meaning that the data can be copied, modified, and distributed in any format for any purpose, as long as notification of any changes and credit are given.

## Gaps

We still need to select the years to include in our analysis. Although the three datasets have year columns, some countries may not have data for all three indicators in the same years. We will compare their coverage before selecting the study period.

We also need to decide how to handle missing values and which countries to include. We will check how many records would be removed if we only use records with all three indicators available. We also need to confirm how to identify regional and income-group records so that they are kept separate from individual countries.

Another question is how to interpret GDP in our analysis. The selected dataset measures total GDP in current US dollars, which reflects the size of an economy rather than average income per person. We will discuss how this affects our research questions and the conclusions we can draw.

Finally, we may need further guidance on workflow automation and machine-readable metadata as these topics are covered in class.
