# Raw data quality

The following data quality findings and checks were done manually.

## 1. Lowest life expectancy value
- The lowest reported life_exp value for a country was 10.989. This was recorded as a value for South Sudan in 1988.
- What I found: https://countryeconomy.com/demography/life-expectancy/south-sudan?year=1988
- This outside source reinforces the fact that this value is correct. Sudan was facing extreme famine in 1988, largely due to the civil war going on within the country at that time. This caused the life expectancy to plummet to the value that we see recorded. Therefore, this value will be kept.

## 2. Accuracy spot-checks against another source
- The following are spot checks of data for a given country and year that I selected at random. 
- The source we will be using for this test is https://countryeconomy.com/

| Country | Year | Indicator | Our Value | Other Source value |
|---|---|---|---|---|
| Italy | 1975 | Life Expectancy | 72.6473 | 72.65 |
| Japan | 2001 | GDP | 4.4T | 4.534T |

## 3. Note on why integration is feasible
- The layouts of the raw data are identical. all three files have one sheet, the header on row 5, four identifier columns, and one column per year from 1960 to 2025.
- All three datasets contain the same 266 Country Code values, with no duplicates and identical country names, so Country Code plus Year identifies one observation in each dataset.
- Electricity access starts in 1990, and life expectancy and electricity access both end in 2024, so all 3 indicators overlap in 1990-2024, giving us 35 years of values to compare.
