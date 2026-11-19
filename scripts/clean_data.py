from pathlib import Path

import pandas as pd

folder = Path(__file__).resolve().parents[1]
output_dir = folder / "data" / "cleaned"
output_dir.mkdir(parents=True, exist_ok=True)

datasets = [
    ("API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx", "GDP", "gdp_long.csv"),
    ("API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx", "LifeExpectancy", "life_expectancy_long.csv"),
]

for filename, indicator, output_name in datasets:
    data = pd.read_excel(folder / "data" / "raw" / filename, header=4)
    years = [column for column in data.columns if str(column).isdigit()]

    cleaned = data.melt(
        id_vars=["Country Code", "Country Name"],
        value_vars=years,
        var_name="Year",
        value_name=indicator,
    )
    cleaned["Year"] = cleaned["Year"].astype(int)
    cleaned.to_csv(output_dir / output_name, index=False)
    print(f"{output_name}: {len(cleaned):,} rows")
