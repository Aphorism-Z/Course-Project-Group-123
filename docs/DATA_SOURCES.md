## GDP Dataset

- URL: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD 
- Raw file: [API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx](../data/raw/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx)
- Indicator code: NY.GDP.MKTP.CD
- Definition: GDP is the total amount of income earned through the production of goods and services in an economic territory during an accounting period. This dataset measures the total size of each country’s economy in US dollars. This dataset is expressed in current prices, meaning no adjustments have been made to account for price changes over time.
- Coverage: 1960-2025 (2025 partial)
- Unit: US Dollars
- Download date: 10/22/2026
- Release date: 10/8/2026
- License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)	
- Credit: World Bank (https://datacatalog.worldbank.org/public-licenses#cc-by)

## Access to electricity dataset

- URL: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS 
- Raw file: [API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_987.xlsx](../data/raw/API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_987.xlsx)
- Indicator code: EG.ELC.ACCS.ZS
- Definition: This gives the share of each country’s population with electricity access. Data are collected from industry, national surveys and international sources.
- Coverage: 1990-2024
- Unit: Percent of Population
- Download date: 10/22/2026
- Release date: 10/8/2026
- License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)	
- Credit: World Bank (https://datacatalog.worldbank.org/public-licenses#cc-by) 

## Life expectancy dataset

- URL: https://data.worldbank.org/indicator/SP.DYN.LE00.IN 
- Raw file: [API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx](../data/raw/API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx)
- Indicator code: SP.DYN.LE00.IN
- Definition: This gives the average number of years a newborn (male or female) is expected to live if prevailing patterns of mortality at the time of birth remained constant throughout its life.
- Coverage: 1960-2024
- Unit: Years
- Download date: 10/22/2026
- Release date: 10/8/2026
- License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)	
- Credit: World Bank (https://datacatalog.worldbank.org/public-licenses#cc-by)

## File layout (all three raw files)

The three workbooks share the same structure.

- Sheets: each workbook has one sheet. Its name is the filename's indicator code, cut off at Excel's 31-character limit.
- Title rows: rows 1 to 4 hold metadata, not data. Cell B1 says `World Development Indicators`, and cell B3 holds the `Last Updated Date` (2026-10-08).
- Header row: row 5 holds the column names.
- Data rows: rows 6 to 271 contain 266 records, one per country or aggregate.
- Identifier columns: `Country Name`, `Country Code`, `Indicator Name`, and `Indicator Code`. The last two repeat the same value on every row.
- Year columns: one column for each year from 1960 to 2025 (66 columns), so each sheet is 70 columns wide.
- Format: the data is in wide format (years across, countries down). It must be reshaped to one row per country and year before the datasets can be joined on `Country Code` and year.
- Missing values: a year with no data is an empty cell.
- Shared keys: all three files list the same 266 country codes with the same names, and no code appears twice.
- Aggregates: the 266 records include regions and income groups (for example `ARB`, Arab World) as well as individual countries. The files have no column that marks which is which.
- Reading in pandas: `pd.read_excel(path, header=4)` skips the four title rows.


## License and Attribution

- All three datasets are from the World Bank and licensed CC BY 4.0. Cleaned and integrated files in this repository are modified versions of the originals; the changes are documented in the cleaning scripts.
