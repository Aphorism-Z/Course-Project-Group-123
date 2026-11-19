from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
raw = root / "data" / "raw"
results = root / "results"

files = {
    "gdp": "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx",
    "life_exp": "API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx",
    "elec": "API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_987.xlsx"
}

def load(name):
    df = pd.read_excel(raw / files[name], header=4)
    df.columns = [str(int(c)) if isinstance(c, (int,float)) else c for c in df.columns]
    return df
def year_columns(df):
    return [c for c in df.columns if c.isdigit()]
def long_format(df,name):
    out = df.melt(id_vars = ["Country Code, Country Name"], value_vars=year_columns(df),
                  var_name = "year", value_name = name)
    out['year'] = out['year'].astype(int)
    return out.dropna(subset=[name])
def assess_completeness(name,df):
    years = year_columns(df)
    missing = df[years].isna()
    per_year = missing.mean()
    per_year.rename("missing_share").rename_axis("year").to_csv(results / f"missing_by_year_{name}.csv")
    empty_years = per_year[per_year == 1].index.tolist()
    nodata = df.loc[missing.all(axis=1), ["Country Code", "Country Name"]]
    nodata.to_csv(results / f"nodata_records_{name}.csv", index=False)
    df.assign(missing_years=missing.sum(axis=1))[["Country Code", "Country Name", "missing_years"]] \
      .to_csv(results / f"missing_by_record_{name}.csv", index=False)

    lines = [
        f"{name}: completeness", "",
        f"- Records: {len(df)}, year columns: {len(years)}",
        f"- Ovr missing pct: {missing.mean().mean():.1%}",
        f"- Years w no data in any record: {len(empty_years)}" + (f"({empty_years[0]} to {empty_years[-1]})" if empty_years else ""),
        f"- Records w no data in any year: {len(nodata)}",
    ]
    if len(nodata) > 0:
        lines.append(" -" + ", ".join(nodata["Country Name"]))
    lines.append("")
    return lines
def main():
    results.mkdir(exist_ok=True)
    data = {name: load(name) for name in files}
    report = ['# Raw data quality report', '']
    for name, df in data.items():
        print(name, df.shape, df.columns[:6].tolist(), year_columns(df)[:10])
        report += assess_completeness(name,df)
    (results / "quality_report_raw.md").write_text("\n".join(report), encoding="utf-8")
if __name__ == "__main__":
    main()


