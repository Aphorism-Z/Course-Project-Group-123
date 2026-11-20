from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/cleaned"
KEYS = ["Country Code", "Year"]
SOURCES = {
    "GDP": "gdp_long.csv",
    "ElectricityAccess": "electricity_access_long.csv",
    "LifeExpectancy": "life_expectancy_long.csv",
}


def main():
    data = pd.read_csv(DATA / "world_bank_integrated.csv")
    indicators = list(SOURCES)
    complete = data.dropna(subset=indicators)

    # 1. Accuracy: flag values outside reasonable ranges.
    gdp = data["GDP"]
    life = data["LifeExpectancy"]
    electricity = data["ElectricityAccess"]
    report = [
        "# Integrated data quality",
        "",
        "## 1. Accuracy",
        "",
        f"- Negative GDP values: {gdp.lt(0).sum():,}.",
        f"- Life expectancy outside 0–120 years: {(life.lt(0) | life.gt(120)).sum():,}.",
        f"- Electricity access outside 0–100%: {(electricity.lt(0) | electricity.gt(100)).sum():,}.",
        "",
        "These ranges screen for implausible values. We also compared the merged "
        "values with the cleaned inputs to check that the join preserved them.",
        "",
    ]
    expected_keys = set()
    merged_keys = set(data[KEYS].dropna().itertuples(index=False, name=None))
    for indicator, filename in SOURCES.items():
        source = pd.read_csv(DATA / filename)
        expected_keys.update(source[KEYS].dropna().itertuples(index=False, name=None))
        matched = source.merge(data[KEYS + [indicator]], on=KEYS, suffixes=("_input", "_merged"))
        equal = np.isclose(
            matched[f"{indicator}_input"], matched[f"{indicator}_merged"],
            rtol=1e-12, atol=0, equal_nan=True,
        )
        report.append(f"- {indicator} differences on matching keys: {(~equal).sum():,}.")

    # 2. Completeness: count missing values and compare expected country-year keys.
    missing = data.isna()
    missing_counts = missing.sum()
    missing_percent = missing.mean()
    report.extend([
        "", "## 2. Completeness", "",
        "| Column | Missing values | Missing percentage |",
        "| --- | ---: | ---: |",
    ])
    for column in data.columns:
        report.append(f"| {column} | {missing_counts[column]:,} | {missing_percent[column]:.1%} |")
    report.extend([
        "",
        f"- Expected country-year pairs from the three cleaned inputs: {len(expected_keys):,}.",
        f"- Expected pairs missing from the merge: {len(expected_keys - merged_keys):,}.",
        f"- Unexpected pairs in the merge: {len(merged_keys - expected_keys):,}.",
        f"- Rows with all three indicators: {len(complete):,} ({len(complete) / len(data):.1%}).",
        f"- Rows missing all three indicators: {missing[indicators].all(axis=1).sum():,}.",
    ])

    # 3. Timeliness: check the year labels and the years with actual observations.
    rows_by_year = data["Year"].value_counts().sort_index()
    complete_by_year = complete["Year"].value_counts().reindex(rows_by_year.index, fill_value=0)
    report.extend([
        "", "## 3. Timeliness", "",
        f"- Merged year labels: {data['Year'].min()}–{data['Year'].max()}.",
        f"- Years with all three indicators: {complete['Year'].min()}–{complete['Year'].max()}.",
        "- The [source documentation](../docs/DATA_SOURCES.md) records October 8, 2026 "
        "as the workbook release date. Annual row counts are listed below.",
        "",
        "| Indicator | First observation year | Last observation year |",
        "| --- | ---: | ---: |",
    ])
    for indicator in indicators:
        years = data.loc[data[indicator].notna(), "Year"]
        report.append(f"| {indicator} | {years.min()} | {years.max()} |")

    # 4. Consistency: check the year type and country code format.
    codes = data["Country Code"]
    malformed_codes = codes.notna() & ~codes.str.fullmatch("[A-Z]{3}", na=False)
    names_per_code = data.groupby("Country Code")["Country Name"].nunique()
    report.extend([
        "", "## 4. Consistency", "",
        f"- Year column type when read by pandas: `{data['Year'].dtype}`.",
        f"- Rows missing a country code or year: {missing[KEYS].any(axis=1).sum():,}.",
        f"- Present country codes outside the three-uppercase-letter format: {malformed_codes.sum():,}.",
        f"- Country codes linked to multiple names: {names_per_code.gt(1).sum():,}.",
    ])

    # 5. Duplicates: compare full rows and country-year pairs separately.
    report.extend([
        "", "## 5. Duplicate records", "",
        f"- Exact duplicate rows: {data.duplicated().sum():,}.",
        f"- Duplicate country-year rows: {data.duplicated(subset=KEYS).sum():,}.",
    ])

    # 6. Summary: describe the indicators and list the entities and years retained.
    country_codes = sorted(codes.dropna().unique())
    complete_codes = set(complete["Country Code"].dropna())
    no_complete_rows = sorted(set(country_codes) - complete_codes)
    stats = data[indicators].describe()
    report.extend([
        "", "## 6. Dataset summary", "",
        f"- Shape: {data.shape[0]:,} rows and {data.shape[1]} columns.",
        f"- Reporting entities: {len(country_codes)}, including countries, territories, and aggregates.",
        f"- Distinct year labels: {data['Year'].nunique()}.",
        f"- Entities with all three indicators in at least one row: {len(complete_codes)}.",
        f"- Entity codes with no complete row: {', '.join(no_complete_rows) or 'None'}.",
        "",
        "Summary statistics include every available value in the merged CSV.",
        "",
        "```text",
        stats.to_string(float_format=lambda value: f"{value:,.3g}"),
        "```",
        "",
        "The [SHA-256 manifest](../data/raw/CHECKSUMS.sha256) documents raw file integrity.",
        "",
        "<details>",
        "<summary>Year-by-year counts and reporting-entity codes</summary>",
        "",
        "| Year | Merged rows | Rows with all three indicators |",
        "| ---: | ---: | ---: |",
    ])
    for year, count in rows_by_year.items():
        report.append(f"| {year} | {count:,} | {complete_by_year[year]:,} |")
    report.extend(["", "**Reporting-entity codes retained**", "",
                   ", ".join(country_codes), "", "</details>"])
    output = ROOT / "results/quality_report_integrated.md"
    output.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
