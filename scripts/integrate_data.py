from pathlib import Path

import pandas as pd

folder = Path(__file__).resolve().parent[1] / "data" / "cleaned"
keys = ["Country Code", "Year"]

gdp = pd.read_csv(folder / "gdp_long.csv")
electricity = pd.read_csv(folder / "electricity_access_long.csv")
life = pd.read_csv(folder / "life_expectancy_long.csv")

# Keep all country-year pairs and check that each key is unique.
integrated = (
    gdp.merge(
        electricity[keys + ["ElectricityAccess"]],
        on=keys,
        how="outer",
        validate="one_to_one",
    )
    .merge(
        life[keys + ["LifeExpectancy"]],
        on=keys,
        how="outer",
        validate="one_to_one",
    )
    .sort_values(keys)
)

output = folder / "world_bank_integrated.csv"
integrated.to_csv(output, index=False)

indicators = ["GDP", "ElectricityAccess", "LifeExpectancy"]
complete_rows = integrated[indicators].notna().all(axis=1).sum()

print(f"Total rows: {len(integrated):,}")
print(f"Rows with all three indicators: {complete_rows:,}")
print(f"Saved to: {output}")